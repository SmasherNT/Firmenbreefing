#!/usr/bin/env python3
"""Prüft Skills und Instructions und packt die Skills als ZIP für Agent Builder / Copilot Studio.

  python3 tools/build.py            prüfen, Tests ausführen, dist/ neu schreiben
  python3 tools/build.py --pruefen  nur prüfen, ob dist/ aktuell ist (Exit 1, wenn nicht)
"""
import argparse, hashlib, io, os, re, subprocess, sys, zipfile

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTEN = {
    "firmenbriefing": ["briefing-standards", "briefing-ausgabe", "firmenbasis-person", "portfolio",
                       "cluster", "markt-wettbewerb", "fokusthema", "interpretation"],
    "briefing-pruefung": ["briefing-standards", "briefing-ausgabe", "quellenpruefung", "ableitungspruefung"],
}
GRENZEN = {"skills_je_agent": 8, "skill_md_zeichen": 20000, "instructions_zeichen": 8000,
           "datei_bytes": 25 * 1024 * 1024, "zip_bytes": 10 * 1024 * 1024, "dateien_je_agent": 350,
           "ordnertiefe": 3, "beschreibung_zeichen": 1024}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
IGNORIEREN = ("__pycache__", ".pyc", ".DS_Store")


def dateien(ordner):
    for wurzel, dirs, files in os.walk(ordner):
        dirs[:] = sorted(d for d in dirs if d not in IGNORIEREN)
        for f in sorted(files):
            if not f.endswith(IGNORIEREN):
                pfad = os.path.join(wurzel, f)
                yield pfad, os.path.relpath(pfad, ordner).replace(os.sep, "/")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    werte = {}
    for zeile in m.group(1).splitlines():
        if ":" in zeile:
            k, v = zeile.split(":", 1)
            werte[k.strip()] = v.strip()
    return werte


def pruefe_skill(ordner, fehler):
    name = os.path.basename(ordner)
    pfad = os.path.join(ordner, "SKILL.md")
    if not os.path.exists(pfad):
        fehler.append("%s: SKILL.md fehlt" % name)
        return []
    text = open(pfad, encoding="utf-8").read()
    fm = frontmatter(text)
    if fm.get("name") != name:
        fehler.append("%s: name im Frontmatter muss dem Ordnernamen entsprechen" % name)
    if not NAME_RE.match(name) or len(name) > 64:
        fehler.append("%s: Name nur Kleinbuchstaben, Ziffern und Bindestriche, max. 64" % name)
    if not 1 <= len(fm.get("description", "")) <= GRENZEN["beschreibung_zeichen"]:
        fehler.append("%s: description fehlt oder ist länger als 1024 Zeichen" % name)
    if len(text) >= GRENZEN["skill_md_zeichen"]:
        fehler.append("%s: SKILL.md hat %d Zeichen, erlaubt unter 20000" % (name, len(text)))
    liste = list(dateien(ordner))
    for p, rel in liste:
        if os.path.getsize(p) > GRENZEN["datei_bytes"]:
            fehler.append("%s: %s größer als 25 MB" % (name, rel))
        if rel.count("/") > GRENZEN["ordnertiefe"]:
            fehler.append("%s: %s liegt tiefer als drei Ordner" % (name, rel))
    return liste


def zip_bytes(liste):
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w", zipfile.ZIP_DEFLATED) as z:
        for p, rel in liste:
            info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            with open(p, "rb") as f:
                z.writestr(info, f.read())
    return puffer.getvalue()


def bauen():
    fehler, pakete = [], {}
    skills = sorted(d for d in os.listdir(os.path.join(BASIS, "skills")) if os.path.isdir(os.path.join(BASIS, "skills", d)))
    for s in skills:
        liste = pruefe_skill(os.path.join(BASIS, "skills", s), fehler)
        pakete["skills/%s.zip" % s] = zip_bytes(liste)
    probe = os.path.join(BASIS, "machbarkeitstest", "briefing-machbarkeit")
    pakete["machbarkeitstest/briefing-machbarkeit.zip"] = zip_bytes(pruefe_skill(probe, fehler))
    for agent, liste in AGENTEN.items():
        if len(liste) > GRENZEN["skills_je_agent"]:
            fehler.append("%s: mehr als acht Skills" % agent)
        for s in liste:
            if s not in skills:
                fehler.append("%s: Skill %s fehlt" % (agent, s))
        n = sum(len(list(dateien(os.path.join(BASIS, "skills", s)))) for s in liste if s in skills)
        if n > GRENZEN["dateien_je_agent"]:
            fehler.append("%s: %d Dateien in allen Skills, erlaubt 350" % (agent, n))
        text = open(os.path.join(BASIS, "agenten", agent, "instructions.md"), encoding="utf-8").read()
        if len(text) > GRENZEN["instructions_zeichen"]:
            fehler.append("%s: Instructions haben %d Zeichen, erlaubt 8000" % (agent, len(text)))
    for name, daten in pakete.items():
        if len(daten) > GRENZEN["zip_bytes"]:
            fehler.append("%s größer als 10 MB" % name)
    zeilen = ["# Pakete zum Hochladen", "", "Automatisch erzeugt von tools/build.py. Nicht von Hand ändern.", ""]
    for agent, liste in AGENTEN.items():
        zeilen += ["## Agent %s" % agent, "", "| Datei | Größe | SHA-256 (gekürzt) |", "|---|---|---|"]
        for s in liste:
            d = pakete["skills/%s.zip" % s]
            zeilen.append("| skills/%s.zip | %d Bytes | %s |" % (s, len(d), hashlib.sha256(d).hexdigest()[:16]))
        zeilen.append("")
    d = pakete["machbarkeitstest/briefing-machbarkeit.zip"]
    zeilen += ["## Machbarkeitstest", "", "| Datei | Größe | SHA-256 (gekürzt) |", "|---|---|---|",
               "| machbarkeitstest/briefing-machbarkeit.zip | %d Bytes | %s |" % (len(d), hashlib.sha256(d).hexdigest()[:16]), ""]
    pakete["pakete.md"] = "\n".join(zeilen).encode("utf-8")
    return fehler, pakete


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pruefen", action="store_true", help="nur prüfen, ob dist/ aktuell ist")
    ap.add_argument("--ohne-tests", action="store_true")
    a = ap.parse_args()
    fehler, pakete = bauen()
    if fehler:
        print("\n".join("FEHLER: " + f for f in fehler))
        return 1
    dist = os.path.join(BASIS, "dist")
    if a.pruefen:
        veraltet = [n for n, d in pakete.items() if not os.path.exists(os.path.join(dist, n)) or open(os.path.join(dist, n), "rb").read() != d]
        print("dist/ ist aktuell" if not veraltet else "dist/ veraltet: " + ", ".join(veraltet))
        return 1 if veraltet else 0
    if not a.ohne_tests:
        r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", os.path.join(BASIS, "tests"), "-t", BASIS, "-q"])
        if r.returncode:
            print("FEHLER: Tests fehlgeschlagen, dist/ nicht geschrieben")
            return 1
    for name, daten in pakete.items():
        ziel = os.path.join(dist, name)
        os.makedirs(os.path.dirname(ziel), exist_ok=True)
        with open(ziel, "wb") as f:
            f.write(daten)
    print("%d Dateien nach dist/ geschrieben" % len(pakete))
    return 0


if __name__ == "__main__":
    sys.exit(main())
