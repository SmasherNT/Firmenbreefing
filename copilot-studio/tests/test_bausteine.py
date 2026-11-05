#!/usr/bin/env python3
"""Durchlauf der Werkzeug-Bausteine W1–W5 mit den synthetischen Demodaten.

Die Denk-Agenten werden mit den Demo-Entscheidungen simuliert. Die Werkzeug-
Agenten laufen aus ihren gebauten Skill-Paketen, so wie in Copilot Studio.
Der Lauf-Ordner wechselt vor jedem Schritt seinen Pfad, um getrennte
Sandboxen nachzustellen. Aufruf aus dem Repository-Stamm:

    python3 -m unittest discover -s copilot-studio/tests -p 'test_*.py'
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
STUDIO = HERE.parent
ROOT = STUDIO.parent
SKRIPTE = {"W1": "w1_pruefpaket.py", "W2": "w2_befunde.py", "W3": "w3_freigabe.py",
           "W4": "w4_bewertungskontext.py", "W5": "w5_rendern.py"}
KOPF = ("schema_version", "mode", "role", "run_id", "company", "as_of", "scope")


def laden(name, pfad):
    spec = importlib.util.spec_from_file_location(name, pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def demo_daten(ziel):
    """Erzeugt die Demo und fängt Manifest, Module und Plan ab."""
    demo = laden("demo_bausteine", ROOT / "examples" / "build-demo.py")
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
    return gefangen, Path(ziel)


def vorlaeufige_ids(modul):
    """Wie ein Denk-Agent: ohne Kopf und mit Quellen-IDs Q1, Q2 …"""
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


class BausteinKette(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="bausteine-"))
        pakete = cls.tmp / "pakete"
        lauf = subprocess.run([sys.executable, str(STUDIO / "skills-bauen.py"), "--out", str(pakete)],
                              capture_output=True, text=True)
        assert lauf.returncode == 0, lauf.stdout + lauf.stderr
        cls.skills = {}
        daten = json.loads((STUDIO / "bausteine.json").read_text(encoding="utf-8"))
        for b in daten["bausteine"]:
            if b["id"] in SKRIPTE:
                ordner = cls.tmp / "skills" / b["skill"]
                with zipfile.ZipFile(pakete / (b["skill"] + ".zip")) as zf:
                    zf.extractall(ordner)
                cls.skills[b["id"]] = ordner / SKRIPTE[b["id"]]
        cls.demo, cls.demo_ordner = demo_daten(cls.tmp / "demo")
        cls.env = {**os.environ, "BRIEFING_ARBEIT": str(cls.tmp / "arbeit")}
        cls.lauf = cls.tmp / "sharepoint-0"
        cls.zaehler = 0

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def umziehen(self):
        """Lauf-Ordner unter neuem Pfad, wie in einer neuen Sandbox."""
        type(self).zaehler += 1
        neu = self.tmp / ("sharepoint-" + str(self.zaehler))
        shutil.move(str(self.lauf), str(neu))
        type(self).lauf = neu

    def werkzeug(self, wid, *argumente, erwartet=True):
        self.umziehen()
        lauf = subprocess.run([sys.executable, str(self.skills[wid]), "--lauf", str(self.lauf), *argumente],
                              capture_output=True, text=True, env=self.env)
        ausgabe = lauf.stdout + lauf.stderr
        if erwartet:
            self.assertEqual(lauf.returncode, 0, wid + " " + " ".join(argumente) + "\n" + ausgabe)
        # Letzte Zeile: Liste für das Zurückschreiben nach SharePoint.
        letzte = lauf.stdout.strip().splitlines()[-1]
        self.assertTrue(letzte.startswith("DATEIEN "), letzte)
        liste = json.loads(letzte[len("DATEIEN "):])
        self.assertTrue(all((self.lauf / d).exists() for d in liste["geaendert"]))
        return lauf.returncode, ausgabe

    def lesen(self, name):
        return json.loads((self.lauf / name).read_text(encoding="utf-8"))

    def schreiben(self, name, daten):
        (self.lauf / name).write_text(json.dumps(daten, ensure_ascii=False, indent=2), encoding="utf-8")

    def dokumentpruefung(self):
        """Simuliert A07: alle zugewiesenen Paare als A geprüft."""
        for job in sorted(self.lauf.glob("pruefjob-*.json")):
            ansicht = json.loads(job.read_text(encoding="utf-8"))
            dokumente = [dict(source_id=d["source"]["id"], original_read=True, note="SIMULIERT: Original gelesen",
                              findings=[dict(claim_id=c, depth="A", status="geprüft", note="SIMULIERT: belegt")
                                        for c in d["review_fact_ids"]]) for d in ansicht["documents"]]
            self.schreiben(job.name.replace("pruefjob", "befund"),
                           dict(run_id=ansicht["run_id"], company=ansicht["company"], as_of=ansicht["as_of"],
                                phase=ansicht["phase"], job_id=ansicht["job_id"], documents=dokumente))

    def leitpruefung(self, phase):
        """Simuliert A08 aus der Leitprüfungs-Eingabe."""
        eingabe = self.lesen("leitpruefung-eingabe.json")
        auftrag = eingabe["pruefauftrag"]
        entscheid = dict(status="freigegeben", review_scope="SIMULIERT", material_errors=[])
        if phase == "basis":
            entscheid.update(scope_and_mappings_checked=True, review_groups=[dict(
                claim_ids=sorted(c["id"] for c in eingabe["aussagen"]), depth="A", status="geprüft", note="SIMULIERT")])
        else:
            def ids(wert):
                return sorted(wert) if isinstance(wert, (list, dict)) else []
            entscheid["review_groups"] = [dict(claim_ids=ids(auftrag.get("claims_to_review")), depth="A",
                                               status="geprüft", note="SIMULIERT")]
            entscheid["reuse_fact_ids"] = ids(auftrag.get("fact_reuse_candidates"))
            pruefen = ids(auftrag.get("facts_to_verify"))
            entscheid["fact_groups"] = [dict(claim_ids=pruefen, depth="A", status="geprüft", note="SIMULIERT")] if pruefen else []
        self.schreiben("leitentscheid.json", entscheid)

    def test_kette(self):
        demo = self.demo
        self.lauf.mkdir()
        # A01 (simuliert)
        self.schreiben("facts-run.json", demo["manifest"])
        self.schreiben("comparison-plan.json", demo["plan"])
        (self.lauf / "auftrag.md").write_text("Fiktiver Offline-Test", encoding="utf-8")
        # A02–A05 (simuliert, ohne Kopf, vorläufige Quellen-IDs)
        for modul in demo["module"]:
            self.schreiben(modul["role"] + "-facts.json", vorlaeufige_ids(modul))

        # Prüftor 1
        self.werkzeug("W1", "--phase", "basis")
        ergebnis = self.lesen("pruefergebnis.json")
        self.assertTrue(ergebnis["bestanden"], ergebnis)
        self.assertGreater(ergebnis["jobs"], 0)
        portfolio = self.lesen("portfolio-facts.json")
        self.assertEqual(portfolio["role"], "portfolio")
        self.assertTrue(all(q["id"].startswith("S-") for q in portfolio["source_proposals"]))
        self.dokumentpruefung()
        self.werkzeug("W2", "--phase", "basis")
        self.leitpruefung("basis")
        self.werkzeug("W3", "--phase", "basis")
        self.assertTrue(self.lesen("pruefergebnis.json")["bestanden"], self.lesen("pruefergebnis.json"))

        # Bewertung
        self.werkzeug("W4", "--schritt", "positioning")
        positionierung = json.loads((self.demo_ordner / "positioning.json").read_text(encoding="utf-8"))
        self.schreiben("positioning.json", {k: positionierung[k] for k in
                                            ("status", "interpretations", "research_requests", "shared_limitations")})
        self.werkzeug("W4", "--schritt", "swot")
        self.assertTrue(self.lesen("pruefergebnis.json")["bestanden"], self.lesen("pruefergebnis.json"))
        swot = json.loads((self.demo_ordner / "swot.json").read_text(encoding="utf-8"))
        self.schreiben("swot.json", {k: swot[k] for k in
                                     ("status", "interpretations", "research_requests", "shared_limitations")})

        # Prüftor 2
        self.werkzeug("W1", "--phase", "final")
        self.assertTrue(self.lesen("pruefergebnis.json")["bestanden"], self.lesen("pruefergebnis.json"))
        self.dokumentpruefung()
        self.werkzeug("W2", "--phase", "final")
        self.leitpruefung("final")
        self.werkzeug("W3", "--phase", "final")
        self.assertTrue(self.lesen("pruefergebnis.json")["bestanden"], self.lesen("pruefergebnis.json"))

        # Ausgabe
        self.werkzeug("W5")
        html = (self.lauf / "briefing.html").read_text(encoding="utf-8")
        demo_html = (self.demo_ordner / "briefing-demo.html").read_text(encoding="utf-8")
        # Gleiche Daten und Entscheidungen ergeben dieselbe HTML wie der heutige Ablauf.
        self.assertEqual(html, demo_html)

    def test_rueckgabe_bei_fehler(self):
        """Ein kaputtes Modul geht an den zuständigen Baustein zurück."""
        lauf = self.tmp / "fehlerlauf"
        lauf.mkdir()
        demo = self.demo
        (lauf / "facts-run.json").write_text(json.dumps(demo["manifest"], ensure_ascii=False), encoding="utf-8")
        (lauf / "comparison-plan.json").write_text(json.dumps(demo["plan"], ensure_ascii=False), encoding="utf-8")
        for modul in demo["module"]:
            modul = vorlaeufige_ids(modul)
            if (modul.get("claims") or [{}])[0].get("id", "").startswith("P"):
                modul["claims"][0]["id"] = "X1"
            name = {"T": "context", "P": "portfolio", "C": "cluster", "M": "market"}
            rolle = next(name[c["id"][0]] for c in modul["claims"] if c["id"][0] in name)
            (lauf / (rolle + "-facts.json")).write_text(json.dumps(modul, ensure_ascii=False), encoding="utf-8")
        lauf_w1 = subprocess.run([sys.executable, str(self.skills["W1"]), "--lauf", str(lauf), "--phase", "basis"],
                                 capture_output=True, text=True, env=self.env)
        self.assertEqual(lauf_w1.returncode, 1, lauf_w1.stdout + lauf_w1.stderr)
        ergebnis = json.loads((lauf / "pruefergebnis.json").read_text(encoding="utf-8"))
        self.assertFalse(ergebnis["bestanden"])
        self.assertIn("portfolio", ergebnis["rueckgabe"], ergebnis)


class GemeinsamerBlock(unittest.TestCase):
    def test_identisch(self):
        bloecke = set()
        for datei in SKRIPTE.values():
            pfad = next(STUDIO.glob("bausteine/W*/skill/" + datei))
            text = pfad.read_text(encoding="utf-8")
            bloecke.add(text[text.index("# --- gemeinsam: anfang"):text.index("# --- gemeinsam: ende")])
        self.assertEqual(len(bloecke), 1, "gemeinsamer Block weicht zwischen den Werkzeug-Skills ab")


if __name__ == "__main__":
    unittest.main()
