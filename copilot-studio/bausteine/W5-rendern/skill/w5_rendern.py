#!/usr/bin/env python3
"""W5 Briefing rendern: erzeugt briefing.html mit der bestehenden Vorlage.

Aufruf: python3 w5_rendern.py --lauf <Lauf-Ordner>

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
        geaendert, geloescht = [], sorted(str(p) for p in self.entfernt)
        if self.arbeit != self.ordner:
            for rel in self.entfernt:
                ziel = self.ordner / rel
                if ziel.exists():
                    ziel.unlink()
            for quelle in sorted(self.arbeit.rglob("*")):
                if quelle.is_file():
                    rel = quelle.relative_to(self.arbeit)
                    ziel = self.ordner / rel
                    if not ziel.exists() or ziel.read_bytes() != quelle.read_bytes():
                        ziel.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(quelle, ziel)
                        geaendert.append(rel.as_posix())
        # Liste für das Zurückschreiben in den SharePoint-Lauf-Ordner.
        print("DATEIEN " + json.dumps(dict(geaendert=geaendert, geloescht=geloescht), ensure_ascii=False))
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


# --- W5 Briefing rendern ---
import argparse


def main():
    parser = argparse.ArgumentParser(description="W5 Briefing rendern")
    parser.add_argument("--lauf", required=True)
    args = parser.parse_args()
    with Lauf(args.lauf) as lauf:
        a = lauf.arbeit
        manifest = lesen(a / "facts-run.json")
        argumente = ["--manifest", "facts-run.json", "--facts", "review-packet.json", "--basis-review", "review-basis.md"]
        voll = set(manifest.get("selected_roles", [])) == set(KERN)
        if voll:
            argumente += ["--positioning", "positioning.json", "--positioning-context", "positioning-context.json",
                          "--swot", "swot.json", "--swot-context", "swot-context.json",
                          "--final-review", "review-final.md", "--full"]
            if (a / "comparison-plan.json").exists():
                argumente += ["--plan", "comparison-plan.json"]
        fehlend = [x for x in argumente if x.endswith((".json", ".md")) and not (a / x).exists()]
        if fehlend:
            print("Fehlende Eingangsdatei: " + ", ".join(fehlend))
            return 1
        ok, daten, text = skript("render-briefing.py", *argumente, "--out", "briefing.html", cwd=a)
        if not ok:
            print(text)
            return 1
        print("briefing.html geschrieben (" + ("Vollbriefing" if voll else "Kurzbriefing") + ")")
        return 0


if __name__ == "__main__":
    sys.exit(main())
