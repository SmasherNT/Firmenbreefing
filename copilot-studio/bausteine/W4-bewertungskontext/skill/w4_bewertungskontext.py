#!/usr/bin/env python3
"""W4 Bewertungskontext: erzeugt den Kontext für Positionierung bzw. SWOT und prüft die Positionierung formal.

Aufruf: python3 w4_bewertungskontext.py --lauf <Lauf-Ordner> --schritt positioning|swot

Teil des Skills; nutzt die vorhandenen Skripte unter scripts/ im Skill-Paket.
Ändert keine Inhalte und trifft keine Prüfentscheidungen.
"""
# --- gemeinsam: anfang (in allen Werkzeug-Skills identisch) ---
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent
SCRIPTS = SKILL / "scripts"
# Fester Arbeitspfad: Die Prüfskripte speichern Pfade in ihren Prüfsummen.
# Jeder Werkzeug-Agent arbeitet deshalb unter demselben Pfad, egal wo der
# Lauf-Ordner liegt.
ARBEIT = Path(os.environ.get("BRIEFING_ARBEIT", "/tmp/firmenbriefing"))
PS = "_pruefstand"
KERN = ("context", "portfolio", "cluster", "market")


def lesen(pfad):
    pfad = Path(pfad)
    text = pfad.read_text(encoding="utf-8")
    if pfad.suffix == ".md":
        treffer = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
        text = treffer.group(1) if treffer else text
    return json.loads(text)


def schreiben(pfad, daten):
    pfad = Path(pfad)
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(json.dumps(daten, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def skript(name, *argumente, cwd):
    """Ruft ein vorhandenes Skript aus scripts/ auf; liefert (ok, json_ausgabe, text)."""
    lauf = subprocess.run([sys.executable, str(SCRIPTS / name), *map(str, argumente)],
                          cwd=cwd, capture_output=True, text=True)
    text = (lauf.stdout or "") + (lauf.stderr or "")
    try:
        daten = json.loads(lauf.stdout) if lauf.stdout.strip() else {}
    except json.JSONDecodeError:
        daten = {}
    return lauf.returncode == 0, daten, text.strip()


class Lauf:
    """Kopiert den Lauf-Ordner an den festen Arbeitspfad und schreibt Änderungen zurück."""

    def __init__(self, ordner):
        self.ordner = Path(ordner).resolve()
        if not self.ordner.is_dir():
            raise SystemExit("Lauf-Ordner nicht gefunden: " + str(ordner))
        manifest = self.ordner / "facts-run.json"
        run_id = lesen(manifest).get("run_id") if manifest.exists() else None
        self.arbeit = ARBEIT / re.sub(r"[^A-Za-z0-9_.-]", "_", run_id or self.ordner.name)
        self.entfernt = []

    def __enter__(self):
        if self.arbeit != self.ordner:
            if self.arbeit.exists():
                shutil.rmtree(self.arbeit)
            shutil.copytree(self.ordner, self.arbeit)
        return self

    def entfernen(self, muster):
        for pfad in list(self.arbeit.glob(muster)):
            pfad.unlink()
            self.entfernt.append(pfad.relative_to(self.arbeit))

    def __exit__(self, *fehler):
        if self.arbeit == self.ordner:
            return False
        for rel in self.entfernt:
            ziel = self.ordner / rel
            if ziel.exists():
                ziel.unlink()
        for quelle in self.arbeit.rglob("*"):
            if quelle.is_file():
                ziel = self.ordner / quelle.relative_to(self.arbeit)
                if not ziel.exists() or ziel.read_bytes() != quelle.read_bytes():
                    ziel.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(quelle, ziel)
        return False


def owner_von_id(cid):
    cid = str(cid)
    treffer = re.match(r"F_([A-Za-z0-9_-]+?)_\d", cid)
    if treffer:
        return "focus:" + treffer.group(1)
    for praefix, owner in (("T", "context"), ("H", "context"), ("P", "portfolio"), ("C", "cluster"),
                           ("M", "market"), ("I", "positioning"), ("S", "swot")):
        if re.match(praefix + r"(?![a-z])[-\w]*$", cid) and not cid.startswith("S-"):
            return owner
    return None


def fehler_zuordnen(fehler, quellen_owner=None):
    """Ordnet Fehlermeldungen der Skripte dem zuständigen Baustein zu."""
    rueckgabe = {}
    for meldung in fehler:
        meldung = str(meldung)
        kopf = meldung.split(":", 2)
        owner = None
        if kopf[0] in KERN:
            owner = kopf[0]
        elif kopf[0] == "focus" and len(kopf) > 1 and kopf[1].strip():
            owner = "focus:" + kopf[1].strip()
        elif kopf[0].startswith(("manifest", "comparison plan", "criterion")):
            owner = "auftrag"
        elif kopf[0].startswith("S-") and quellen_owner:
            for o in quellen_owner.get(kopf[0], ["werkzeug"]):
                rueckgabe.setdefault(o, []).append(dict(ids=[kopf[0]], reason=meldung, action="Quellenangabe korrigieren"))
            continue
        else:
            owner = owner_von_id(kopf[0])
        rueckgabe.setdefault(owner or "werkzeug", []).append(
            dict(ids=[kopf[0]] if owner_von_id(kopf[0]) else [], reason=meldung,
                 action="Fehler beheben und Datei vollständig neu schreiben"))
    return rueckgabe


def pruefergebnis(ordner, schritt, phase=None, bestanden=False, jobs=0, rueckgabe=None, fehler=None):
    daten = dict(schritt=schritt, phase=phase, bestanden=bool(bestanden), jobs=jobs,
                 rueckgabe=rueckgabe or {}, fehler=fehler or [])
    schreiben(Path(ordner) / "pruefergebnis.json", daten)
    print(json.dumps(daten, ensure_ascii=False, indent=2))
    return 0 if bestanden else 1
# --- gemeinsam: ende ---


# --- W4 Bewertungskontext ---
import argparse
import importlib.util


def check_modul():
    spec = importlib.util.spec_from_file_location("check_interpretation", SCRIPTS / "check-interpretation.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def a_fakten(a):
    review = lesen(a / "review-basis.md")
    return sorted(z["id"] for z in review.get("claims", [])
                  if z.get("depth") == "A" and z.get("status") in ("geprüft", "übernommen")
                  and owner_von_id(z["id"]) in KERN)


def bewertung_vervollstaendigen(a, rolle, manifest):
    kontext = lesen(a / f"{rolle}-context.json")
    daten = lesen(a / f"{rolle}.json")
    daten.update(schema_version=1, mode="interpret-v2", role=rolle,
                 **{k: manifest[k] for k in ("run_id", "company", "as_of", "scope")},
                 input_fingerprint=kontext["fingerprint"])
    if rolle == "positioning" and kontext.get("plan_fingerprint"):
        daten["plan_fingerprint"] = kontext["plan_fingerprint"]
    daten.setdefault("research_requests", [])
    daten.setdefault("shared_limitations", [])
    schreiben(a / f"{rolle}.json", daten)
    return daten


def main():
    parser = argparse.ArgumentParser(description="W4 Bewertungskontext")
    parser.add_argument("--lauf", required=True)
    parser.add_argument("--schritt", choices=("positioning", "swot"), required=True)
    args = parser.parse_args()
    with Lauf(args.lauf) as lauf:
        a = lauf.arbeit
        manifest = lesen(a / "facts-run.json")
        gemeinsam = ["--manifest", "facts-run.json", "--facts", "review-packet.json", "--review", "review-basis.md"]
        plan = ["--plan", "comparison-plan.json"] if (a / "comparison-plan.json").exists() else []
        if lesen(a / "review-basis.md").get("status") != "freigegeben":
            return pruefergebnis(a, "bewertungskontext", args.schritt,
                                 rueckgabe={"werkzeug": [dict(ids=[], reason="review-basis.md ist nicht freigegeben", action="Prüftor 1 wiederholen")]})
        if args.schritt == "positioning":
            optionen = ["--prepare", "--portfolio", "--module-insights"]
            if "regional_presence" in lesen(a / "portfolio-facts.json"):
                optionen.append("--presence")
            markt = ["--market", "market-facts.json"] if (a / "market-facts.json").exists() else []
            ok, daten, text = skript("check-interpretation.py", *optionen, *gemeinsam, *plan, *markt,
                                     "--claim-ids", *a_fakten(a), "--out", "positioning-context.json", cwd=a)
            if not ok:
                fehler = daten.get("errors") or [text]
                return pruefergebnis(a, "bewertungskontext", "positioning", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
            return pruefergebnis(a, "bewertungskontext", "positioning", bestanden=True)

        if not (a / "positioning.json").exists():
            print("Fehlende Eingangsdatei: positioning.json")
            return 1
        positionierung = bewertung_vervollstaendigen(a, "positioning", manifest)
        ok, daten, text = skript("check-interpretation.py", *gemeinsam, "--context", "positioning-context.json",
                                 "--output", "positioning.json", *plan, "--out", f"{PS}/positioning-validation.json", cwd=a)
        if not ok:
            fehler = daten.get("errors") or [text]
            return pruefergebnis(a, "bewertungskontext", "swot",
                                 rueckgabe={"positioning": [dict(ids=[], reason=f, action="Fehler beheben") for f in fehler]}, fehler=fehler)
        fragen = {}
        for frage in positionierung.get("research_requests", []):
            if frage.get("blocking"):
                fragen.setdefault(frage.get("target_role") or "werkzeug", []).append(
                    dict(ids=frage.get("related_claim_ids", []), reason="Rückfrage aus der Positionierung",
                         action="gezielt recherchieren und ergänzen", frage=frage.get("question", "")))
        if fragen:
            return pruefergebnis(a, "bewertungskontext", "swot", rueckgabe=fragen)
        # Unbewertete Matrixzellen, Produkte und Regionen sind keine SWOT-Grundlage
        # (gleiche Regel wie check-interpretation.py).
        unbewertet = check_modul().unassessed
        i_ids = [z["id"] for z in positionierung.get("interpretations", []) if not unbewertet(z)]
        ok, daten, text = skript("check-interpretation.py", "--prepare", *gemeinsam, "--positioning", "positioning.json",
                                 "--positioning-context", "positioning-context.json", *plan,
                                 "--interpretation-ids", *i_ids, "--out", "swot-context.json", cwd=a)
        if not ok:
            fehler = daten.get("errors") or [text]
            return pruefergebnis(a, "bewertungskontext", "swot", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
        return pruefergebnis(a, "bewertungskontext", "swot", bestanden=True)


if __name__ == "__main__":
    sys.exit(main())
