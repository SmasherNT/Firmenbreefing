#!/usr/bin/env python3
"""Baut die Skill-Pakete der Copilot-Studio-Bausteine aus dem Repository.

Jedes Paket enthält den Inhalt von bausteine/<ID>/skill/ (SKILL.md und bei
Werkzeug-Agenten das Startskript) im Wurzelverzeichnis sowie die in
bausteine.json genannten Dateien mit ihren Repository-Pfaden
(references/..., scripts/...).
Die Dateien werden nur beim Bauen in das Paket gelegt; im Repository gibt es
keine Kopien. Aufruf aus dem Repository-Stamm:

    python3 copilot-studio/skills-bauen.py --out dist/skills
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
# Grenzen für hochgeladene Skill-Archive; im eigenen Mandanten bestätigen.
MAX_DATEIEN = 100
MAX_BYTES = 10 * 1024 * 1024


def dateien(eintrag):
    pfad = ROOT / eintrag
    if eintrag.endswith("/"):
        if not pfad.is_dir():
            raise FileNotFoundError(eintrag)
        return sorted(p for p in pfad.rglob("*")
                      if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    if not pfad.is_file():
        raise FileNotFoundError(eintrag)
    return [pfad]


def bauen(baustein, ziel):
    skill_ordner = HERE / "bausteine" / baustein["ordner"] / "skill"
    if not (skill_ordner / "SKILL.md").is_file():
        raise FileNotFoundError(skill_ordner / "SKILL.md")
    inhalt = [(p, p.relative_to(skill_ordner).as_posix()) for p in sorted(skill_ordner.rglob("*"))
              if p.is_file() and "__pycache__" not in p.parts]
    for eintrag in baustein["skill_dateien"]:
        inhalt += [(p, p.relative_to(ROOT).as_posix()) for p in dateien(eintrag)]
    hinweise = []
    paket = ziel / (baustein["skill"] + ".zip")
    with zipfile.ZipFile(paket, "w", zipfile.ZIP_DEFLATED) as zf:
        for quelle, name in inhalt:
            zf.write(quelle, name)
    groesse = paket.stat().st_size
    if len(inhalt) > MAX_DATEIEN:
        hinweise.append(f"mehr als {MAX_DATEIEN} Dateien")
    if groesse > MAX_BYTES:
        hinweise.append("größer als 10 MB")
    return dict(baustein=baustein["id"], paket=str(paket), dateien=len(inhalt),
                bytes=groesse, hinweise=hinweise)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="Zielordner für die .zip-Pakete")
    parser.add_argument("--nur", nargs="*", help="nur diese Baustein-IDs, z. B. A02 W1")
    args = parser.parse_args()
    daten = json.loads((HERE / "bausteine.json").read_text(encoding="utf-8"))
    ziel = Path(args.out)
    ziel.mkdir(parents=True, exist_ok=True)
    ergebnis, fehler = [], []
    for baustein in daten["bausteine"]:
        if args.nur and baustein["id"] not in args.nur:
            continue
        try:
            ergebnis.append(bauen(baustein, ziel))
        except FileNotFoundError as exc:
            fehler.append(f"{baustein['id']}: fehlt {exc}")
    print(json.dumps(dict(pakete=ergebnis, fehler=fehler), ensure_ascii=False, indent=2))
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
