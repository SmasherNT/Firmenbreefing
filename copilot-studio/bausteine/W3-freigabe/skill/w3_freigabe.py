#!/usr/bin/env python3
"""W3 Freigabe: führt Leitentscheid und Befunde zusammen, wendet die Freigaberegeln an, schreibt Review und Prüfergebnis.

Aufruf: python3 w3_freigabe.py --lauf <Lauf-Ordner> --phase basis|final

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


# --- W3 Freigabe ---
import argparse


def rueckgabe_aus_entscheid(entscheid):
    rueckgabe = {}
    gruppen = list(entscheid.get("review_groups", [])) + list(entscheid.get("fact_groups", []))
    for gruppe in gruppen:
        if gruppe.get("status") not in ("Korrektur", "offen"):
            continue
        ids = gruppe.get("claim_ids", [])
        owner = gruppe.get("owner") or (owner_von_id(ids[0]) if ids else None) or "werkzeug"
        rueckgabe.setdefault(owner, []).append(dict(ids=ids, reason=gruppe.get("reason") or gruppe.get("note", ""),
                                                    action=gruppe.get("action", "")))
    for fehler in entscheid.get("material_errors", []):
        if isinstance(fehler, dict):
            ids = fehler.get("claim_ids", [])
            owner = fehler.get("owner") or (owner_von_id(ids[0]) if ids else None) or "werkzeug"
            rueckgabe.setdefault(owner, []).append(dict(ids=ids, reason=fehler.get("reason", ""), action=fehler.get("action", "")))
        else:
            rueckgabe.setdefault("werkzeug", []).append(dict(ids=[], reason=str(fehler), action=""))
    return rueckgabe


def main():
    parser = argparse.ArgumentParser(description="W3 Freigabe")
    parser.add_argument("--lauf", required=True)
    parser.add_argument("--phase", choices=("basis", "final"), required=True)
    args = parser.parse_args()
    phase = args.phase
    with Lauf(args.lauf) as lauf:
        a = lauf.arbeit
        if not (a / "leitentscheid.json").exists():
            print("Fehlende Eingangsdatei: leitentscheid.json")
            return 1
        work = lesen(a / PS / f"review-work-{phase}.json")
        plan = lesen(a / PS / f"review-split-{phase}.json")
        funde = lesen(a / PS / f"source-findings-{phase}.json")
        validierung = f"{PS}/facts-validation.json" if phase == "basis" else f"{PS}/interpretation-validation.json"
        entscheid = lesen(a / "leitentscheid.json")
        entscheid.update(schema_version=1, **{k: work[k] for k in ("run_id", "company", "as_of")}, phase=phase,
                         review_work_fingerprint=work["fingerprint"], plan_fingerprint=plan["fingerprint"],
                         source_collection_fingerprint=funde["fingerprint"])
        entscheid.pop("source_checks", None)
        schreiben(a / PS / f"leitentscheid-{phase}.json", entscheid)
        rueckgabe = rueckgabe_aus_entscheid(entscheid)
        teile = sorted(p.name for p in a.glob("befund-*.json"))
        ok, daten, text = skript("review-shards.py", "merge", "--plan", f"{PS}/review-split-{phase}.json",
                                 "--work", f"{PS}/review-work-{phase}.json", "--facts", "review-packet.json",
                                 "--parts", *teile, "--lead", f"{PS}/leitentscheid-{phase}.json",
                                 "--validation", validierung, "--out", f"{PS}/review-merged-{phase}.json", cwd=a)
        if not ok:
            fehler = daten.get("errors") or [text]
            for owner, eintraege in fehler_zuordnen(fehler).items():
                rueckgabe.setdefault(owner, []).extend(eintraege)
            return pruefergebnis(a, "freigabe", phase, rueckgabe=rueckgabe, fehler=fehler)
        ok, daten, text = skript("stamp-review.py", "--draft", f"{PS}/review-merged-{phase}.json",
                                 "--validation", validierung, "--work", f"{PS}/review-work-{phase}.json",
                                 "--out", f"review-{phase}.md", cwd=a)
        if not ok:
            fehler = daten.get("errors") or [text]
            for owner, eintraege in fehler_zuordnen(fehler).items():
                rueckgabe.setdefault(owner, []).extend(eintraege)
            return pruefergebnis(a, "freigabe", phase, rueckgabe=rueckgabe, fehler=fehler)
        status = lesen(a / f"review-{phase}.md").get("status")
        bestanden = status == "freigegeben" and not rueckgabe
        if not bestanden and not rueckgabe:
            rueckgabe["werkzeug"] = [dict(ids=[], reason="Leitprüfung meldet Status " + str(status), action="Leitentscheid prüfen")]
        return pruefergebnis(a, "freigabe", phase, bestanden=bestanden, rueckgabe=rueckgabe)


if __name__ == "__main__":
    sys.exit(main())
