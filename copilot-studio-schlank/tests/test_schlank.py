#!/usr/bin/env python3
"""Durchlauf der schlanken Variante mit den synthetischen Demodaten.

Die Denk-Agenten R1, R2 und B1 werden mit den Demo-Ergebnissen simuliert. Der
Werkzeug-Agent läuft aus seinem gebauten Skill-Paket. Geprüft wird:
- Vollbriefing und Kurzbriefing entstehen ohne Prüfagenten,
- die HTML hat denselben Inhalt wie der heutige Ablauf,
- sie ist sichtbar als ungeprüfter Entwurf gekennzeichnet und behauptet
  nirgends eine Prüfung.

Aufruf aus dem Repository-Stamm:

    python3 -m unittest discover -s copilot-studio-schlank/tests -p 'test_*.py'
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHLANK = HERE.parent
ROOT = SCHLANK.parent
KOPF = ("schema_version", "mode", "role", "run_id", "company", "as_of", "scope")


def laden(name, pfad):
    spec = importlib.util.spec_from_file_location(name, pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def demo_daten(ziel):
    demo = laden("demo_schlank", ROOT / "examples" / "build-demo.py")
    gefangen = {}
    original = demo.FACTS.build

    def mitschreiben(manifest, module, plan=None):
        gefangen.update(manifest=json.loads(json.dumps(manifest)), module=json.loads(json.dumps(module)),
                        plan=json.loads(json.dumps(plan)))
        return original(manifest, module, plan)

    demo.FACTS.build = mitschreiben
    try:
        demo.generate(ziel)
    finally:
        demo.FACTS.build = original
    return gefangen


def wie_agent(modul):
    """Ohne Kopf und mit vorläufigen Quellen-IDs, wie ein Recherche-Agent liefert."""
    zuordnung = {}
    for q in modul.get("source_proposals", []) + (modul.get("network") or {}).get("sources", []):
        zuordnung.setdefault(q["id"], "Q" + str(len(zuordnung) + 1))
    text = json.dumps(modul, ensure_ascii=False)
    for alt, neu in zuordnung.items():
        text = text.replace('"' + alt + '"', '"' + neu + '"')
    modul = json.loads(text)
    for k in KOPF:
        modul.pop(k, None)
    return modul


class Schlank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="schlank-"))
        lauf = subprocess.run([sys.executable, str(ROOT / "copilot-studio" / "skills-bauen.py"),
                               "--quelle", str(SCHLANK), "--out", str(cls.tmp / "pakete")],
                              capture_output=True, text=True)
        assert lauf.returncode == 0, lauf.stdout + lauf.stderr
        with zipfile.ZipFile(cls.tmp / "pakete" / "schlank-werkzeug.zip") as zf:
            zf.extractall(cls.tmp / "werkzeug")
        cls.werkzeug_py = cls.tmp / "werkzeug" / "werkzeug.py"
        cls.demo = demo_daten(cls.tmp / "demo")
        cls.demo_html = (cls.tmp / "demo" / "briefing-demo.html").read_text(encoding="utf-8")
        cls.env = {**os.environ, "BRIEFING_ARBEIT": str(cls.tmp / "arbeit")}
        cls.werkzeug_modul = laden("werkzeug_schlank", cls.werkzeug_py)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def schritt(self, lauf, schritt):
        ergebnis = subprocess.run([sys.executable, str(self.werkzeug_py), "--lauf", str(lauf), "--schritt", schritt],
                                  capture_output=True, text=True, env=self.env)
        self.assertEqual(ergebnis.returncode, 0, schritt + "\n" + ergebnis.stdout + ergebnis.stderr)
        self.assertTrue(json.loads((lauf / "pruefergebnis.json").read_text(encoding="utf-8"))["bestanden"])

    def schreiben(self, lauf, name, daten):
        (lauf / name).write_text(json.dumps(daten, ensure_ascii=False, indent=2), encoding="utf-8")

    def keine_pruefbehauptung(self, html):
        self.assertIn("Ungeprüfter Entwurf", html)
        for behauptung in ("Geprüfte Fakten", "vollständig geprüft", "Prüftiefe A · übernommen", "Prüftiefe A · geprüft"):
            self.assertNotIn(behauptung, html)

    def test_vollbriefing(self):
        lauf = self.tmp / "voll"
        lauf.mkdir()
        demo = self.demo
        self.schreiben(lauf, "facts-run.json", demo["manifest"])            # R2 auftrag
        self.schreiben(lauf, "comparison-plan.json", demo["plan"])
        (lauf / "auftrag.md").write_text("Fiktiver Offline-Test", encoding="utf-8")
        for modul in demo["module"]:                                         # R1, R2
            self.schreiben(lauf, modul["role"] + "-facts.json", wie_agent(modul))
        self.schritt(lauf, "fakten")
        self.assertTrue((lauf / "positioning-context.json").exists())
        pos = json.loads((self.tmp / "demo" / "positioning.json").read_text(encoding="utf-8"))
        self.schreiben(lauf, "positioning.json", {k: pos[k] for k in                # B1 positioning
                                                  ("status", "interpretations", "research_requests", "shared_limitations")})
        self.schritt(lauf, "swot")
        swot = json.loads((self.tmp / "demo" / "swot.json").read_text(encoding="utf-8"))
        self.schreiben(lauf, "swot.json", {k: swot[k] for k in                       # B1 swot
                                           ("status", "interpretations", "research_requests", "shared_limitations")})
        self.schritt(lauf, "abschluss")
        html = (lauf / "briefing.html").read_text(encoding="utf-8")
        self.keine_pruefbehauptung(html)
        review = (lauf / "review-basis.md").read_text(encoding="utf-8")
        self.assertIn("keine unabhängige Prüfung", review)
        # Inhalt identisch zum heutigen Ablauf; nur die Prüfkennzeichnung unterscheidet sich.
        erwartet = self.werkzeug_modul.kennzeichnen(self.demo_html.replace("Prüftiefe A · geprüft", "Prüftiefe A · übernommen"))
        self.assertEqual(html, erwartet)

    def test_kurzbriefing(self):
        lauf = self.tmp / "kurz"
        lauf.mkdir()
        manifest = dict(self.demo["manifest"], selected_roles=["context", "portfolio"],
                        topics=[t for t in self.demo["manifest"]["topics"] if t.get("page") != "market"])
        manifest.pop("market_title", None)
        self.schreiben(lauf, "facts-run.json", manifest)
        (lauf / "auftrag.md").write_text("Fiktiver Offline-Test", encoding="utf-8")
        def nur_eigene(wert, eigene):
            # Im Kurzbriefing gibt es keine Markt- oder Cluster-Aussagen, auf die verwiesen werden kann.
            if isinstance(wert, dict):
                return {k: ([c for c in v if c in eigene] if k == "claim_ids" else nur_eigene(v, eigene)) for k, v in wert.items()}
            if isinstance(wert, list):
                return [nur_eigene(x, eigene) for x in wert]
            return wert
        for modul in self.demo["module"]:
            if modul["role"] in ("context", "portfolio"):
                eigene = {c["id"] for m in self.demo["module"] if m["role"] in ("context", "portfolio") for c in m["claims"]}
                self.schreiben(lauf, modul["role"] + "-facts.json", wie_agent(nur_eigene(modul, eigene)))
        self.schritt(lauf, "fakten")
        self.assertFalse((lauf / "positioning-context.json").exists())
        self.schritt(lauf, "abschluss")
        self.keine_pruefbehauptung((lauf / "briefing.html").read_text(encoding="utf-8"))

    def test_badge_wird_ersetzt(self):
        html = self.werkzeug_modul.kennzeichnen(
            '<div class="badge">Geprüfte Fakten &amp; Analysteninterpretation</div><main></main>')
        self.assertIn("Ungeprüfter Entwurf · ohne unabhängige Quellenprüfung", html)
        self.assertNotIn("Geprüfte Fakten", html)


if __name__ == "__main__":
    unittest.main()
