#!/usr/bin/env python3
"""Prüft Skills und Instructions der drei Agenten und packt alles als ZIP.

  python3 tools/build.py            abgeleitete Dateien erzeugen, prüfen, Tests ausführen, dist/ neu schreiben
  python3 tools/build.py --pruefen  nur prüfen, ob dist/ und die abgeleiteten Dateien aktuell sind (Exit 1, wenn nicht)

Abgeleitete Dateien (nie von Hand ändern):
  skills/briefing-html/scripts/briefing.py   Kopie von skills/briefing-grundlagen/scripts/briefing.py
  skills/briefing-html/scripts/vorlagen.py   alle Dateien aus html-vorlagen/ als Python-Texte, weil der
                                             Agent Builder in Skills z. B. keine .css-Dateien annimmt
"""
import argparse, hashlib, io, os, re, subprocess, sys, zipfile

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTEN = {
    "recherche": ["briefing-grundlagen", "firmenbasis-person", "portfolio", "cluster", "markt-wettbewerb",
                  "fokusthema", "interpretation"],
    "pruefung": ["briefing-grundlagen", "pruefung-vertiefung", "firmenbasis-person", "portfolio", "cluster",
                 "markt-wettbewerb", "fokusthema", "interpretation"],
    "html": ["briefing-html"],
}
TITEL = {"recherche": "Firmenbriefing Recherche", "pruefung": "Firmenbriefing Prüfung", "html": "Firmenbriefing HTML"}
QUELLE = os.path.join("skills", "briefing-grundlagen", "scripts", "briefing.py")
KOPIE = os.path.join("skills", "briefing-html", "scripts", "briefing.py")
VORLAGEN_QUELLE = "html-vorlagen"
VORLAGEN_ZIEL = os.path.join("skills", "briefing-html", "scripts", "vorlagen.py")
# Dateitypen, die der Agent Builder in Skills annimmt (Microsoft Learn, „Skills in declarative agents“,
# Tabelle „Supported file and script types“, Stand 18.11.2026). Alles andere lehnt der Upload ab.
ERLAUBT = {".json", ".xml", ".yaml", ".yml", ".ini", ".config", ".utf8", ".docx", ".doc", ".docm", ".pdf",
           ".txt", ".rtf", ".md", ".ppt", ".pptx", ".ppsm", ".xlsx", ".xls", ".xlsm", ".csv", ".tsv", ".html",
           ".htm", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".log",
           ".py", ".js", ".mjs", ".cjs", ".ts", ".mts", ".sh", ".bash"}
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
        if os.path.splitext(rel)[1].lower() not in ERLAUBT:
            fehler.append("%s: Dateityp von %s nimmt der Agent Builder nicht an" % (name, rel))
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


def vorlagen_py():
    """Erzeugt vorlagen.py: jede Datei aus html-vorlagen/ als Text, zeilenweise, damit Änderungen lesbar bleiben."""
    ordner = os.path.join(BASIS, VORLAGEN_QUELLE)
    teile = ['"""Eingebettete Vorlagen für briefing_html.py und die Bausteine *-html.py.',
             "",
             "Automatisch erzeugt von tools/build.py aus html-vorlagen/. Nicht von Hand ändern.",
             "Der Agent Builder nimmt in Skills keine .css-Dateien an; deshalb liegen alle Vorlagen hier.",
             '"""', "", "VORLAGEN = {"]
    for datei in sorted(os.listdir(ordner)):
        with open(os.path.join(ordner, datei), encoding="utf-8") as f:
            zeilen = f.read().splitlines(keepends=True)
        teile.append("    %r: (" % datei)
        teile += ["        %r" % z for z in zeilen] or ["        ''"]
        teile.append("    ),")
    teile += ["}", "", "", "def vorlage(name):",
              '    """Text einer Vorlage, z. B. vorlage("portfolio.css")."""', "    return VORLAGEN[name]", ""]
    return "\n".join(teile).encode("utf-8")


def abgeleitete_pruefen(synchronisieren):
    fehler = []
    for ziel, inhalt, text in (
            (KOPIE, open(os.path.join(BASIS, QUELLE), "rb").read(), "Kopie von briefing.py im Skill briefing-html ist veraltet"),
            (VORLAGEN_ZIEL, vorlagen_py(), "vorlagen.py im Skill briefing-html passt nicht zu html-vorlagen/")):
        pfad = os.path.join(BASIS, ziel)
        if synchronisieren:
            with open(pfad, "wb") as f:
                f.write(inhalt)
        elif not os.path.exists(pfad) or open(pfad, "rb").read() != inhalt:
            fehler.append(text)
    return fehler


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
        if len(daten) > GRENZEN["zip_bytes"] and not name.startswith("firmenbriefing-drei-agenten"):
            fehler.append("%s größer als 10 MB" % name)
    zeilen = ["# Pakete zum Hochladen", "", "Automatisch erzeugt von tools/build.py. Nicht von Hand ändern.", ""]
    for agent, liste in AGENTEN.items():
        zeilen += ["## Agent „%s“" % TITEL[agent], "", "| Datei | Größe | SHA-256 (gekürzt) |", "|---|---|---|"]
        for s in liste:
            d = pakete["skills/%s.zip" % s]
            zeilen.append("| skills/%s.zip | %d Bytes | %s |" % (s, len(d), hashlib.sha256(d).hexdigest()[:16]))
        zeilen.append("")
    d = pakete["machbarkeitstest/briefing-machbarkeit.zip"]
    zeilen += ["## Machbarkeitstest", "", "| Datei | Größe | SHA-256 (gekürzt) |", "|---|---|---|",
               "| machbarkeitstest/briefing-machbarkeit.zip | %d Bytes | %s |" % (len(d), hashlib.sha256(d).hexdigest()[:16]), ""]
    pakete["paket.md"] = "\n".join(zeilen).encode("utf-8")
    # Gesamtpaket: alles, was der Nutzer zum Einrichten braucht, in einer Datei.
    gesamt = [(os.path.join(BASIS, q), "firmenbriefing-drei-agenten/" + z) for q, z in (
        ("README.md", "README.md"), ("ANLEITUNG.md", "ANLEITUNG.md"), ("architektur.png", "architektur.png"),
        ("machbarkeitstest/README.md", "machbarkeitstest/README.md"), ("machbarkeitstest/testprotokoll.md", "machbarkeitstest/testprotokoll.md"))
        if os.path.exists(os.path.join(BASIS, q))]
    for agent in AGENTEN:
        for datei, ziel in (("instructions.md", "%s-instructions.md" % agent), ("agent.md", "%s-einstellungen.md" % agent)):
            gesamt.append((os.path.join(BASIS, "agenten", agent, datei), "firmenbriefing-drei-agenten/agenten/%s/%s" % (agent, ziel)))
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w", zipfile.ZIP_DEFLATED) as z:
        def schreibe(name, inhalt):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, inhalt)
        for pfad, name in gesamt:
            with open(pfad, "rb") as f:
                schreibe(name, f.read())
        for name, inhalt in sorted(pakete.items()):
            if name.endswith(".zip"):
                schreibe("firmenbriefing-drei-agenten/" + name, inhalt)
        schreibe("firmenbriefing-drei-agenten/paket.md", pakete["paket.md"])
    pakete["firmenbriefing-drei-agenten.zip"] = puffer.getvalue()
    return fehler, pakete


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pruefen", action="store_true", help="nur prüfen, ob dist/ aktuell ist")
    ap.add_argument("--ohne-tests", action="store_true")
    a = ap.parse_args()
    fehler = abgeleitete_pruefen(not a.pruefen)
    if fehler:
        print("\n".join("FEHLER: " + f for f in fehler))
        return 1
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
    print("Gesamtpaket: dist/firmenbriefing-drei-agenten.zip")
    return 0


if __name__ == "__main__":
    sys.exit(main())
