#!/usr/bin/env python3
"""W2 Befunde bündeln: vervollständigt die Befunde der Dokumentprüfung und erzeugt die Eingabe der Leitprüfung.

Aufruf: python3 w2_befunde.py --lauf <Lauf-Ordner> --phase basis|final

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


# --- W2 Befunde bündeln ---
import argparse


def befunde_vervollstaendigen(a, phase, work, plan):
    dateien = sorted(a.glob("befund-*.json"))
    for pfad in dateien:
        befund = lesen(pfad)
        nummer = pfad.stem.split("-")[-1]
        befund.update(schema_version=1, format="review-source-part-v1",
                      **{k: work[k] for k in ("run_id", "company", "as_of")}, phase=phase,
                      job_id="sources-" + nummer, review_work_fingerprint=work["fingerprint"],
                      plan_fingerprint=plan["fingerprint"])
        schreiben(pfad, befund)
    return [p.name for p in dateien]


def main():
    parser = argparse.ArgumentParser(description="W2 Befunde bündeln")
    parser.add_argument("--lauf", required=True)
    parser.add_argument("--phase", choices=("basis", "final"), required=True)
    args = parser.parse_args()
    phase = args.phase
    with Lauf(args.lauf) as lauf:
        a = lauf.arbeit
        work = lesen(a / PS / f"review-work-{phase}.json")
        plan = lesen(a / PS / f"review-split-{phase}.json")
        erwartet = {"befund-" + j["id"].split("-")[-1] + ".json" for j in plan["jobs"]}
        fehlend = sorted(erwartet - {p.name for p in a.glob("befund-*.json")})
        if fehlend:
            print("Fehlende Eingangsdatei: " + ", ".join(fehlend))
            return 1
        teile = befunde_vervollstaendigen(a, phase, work, plan)
        ok, daten, text = skript("review-shards.py", "collect", "--plan", f"{PS}/review-split-{phase}.json",
                                 "--work", f"{PS}/review-work-{phase}.json", "--facts", "review-packet.json",
                                 "--parts", *teile, "--out", f"{PS}/source-findings-{phase}.json", cwd=a)
        if not ok:
            print(text)
            return 1
        ok, auftrag, text = skript("review-work.py", "show", "--work", f"{PS}/review-work-{phase}.json", cwd=a)
        if not ok:
            print(text)
            return 1
        packet = lesen(a / "review-packet.json")
        eingabe = dict(
            phase=phase, run_id=work["run_id"], company=work["company"], as_of=work["as_of"],
            auftrag=(a / "auftrag.md").read_text(encoding="utf-8") if (a / "auftrag.md").exists() else "",
            pruefauftrag=auftrag,
            befunde=lesen(a / PS / f"source-findings-{phase}.json"),
            aussagen=packet["claims"], quellen=packet["sources"],
            darstellung=packet.get("module_views", []), module=packet.get("module_context", []),
            netzwerk=packet.get("network"))
        if phase == "final":
            for name in ("positioning", "swot", "positioning-context", "swot-context"):
                eingabe[name.replace("-", "_")] = lesen(a / f"{name}.json")
        schreiben(a / "leitpruefung-eingabe.json", eingabe)
        print("leitpruefung-eingabe.json geschrieben")
        return 0


if __name__ == "__main__":
    sys.exit(main())
