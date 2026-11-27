#!/usr/bin/env python3
"""Machbarkeitstest für die Firmenbriefing-Skills. Nur Standardbibliothek; Excel optional."""
import argparse, json, os, platform, re, sys, urllib.request

KENNUNG = "machbarkeit-1"


def umgebung():
    print("Python:", sys.version.split()[0], "|", platform.platform())
    print("Arbeitsverzeichnis:", os.getcwd())
    hier = os.path.dirname(os.path.abspath(__file__))
    print("Skriptordner:", hier)
    try:
        print("Dateien im Skill:", sorted(os.listdir(os.path.dirname(hier))))
    except OSError as e:
        print("Skillordner nicht lesbar:", e)
    try:
        import openpyxl
        print("openpyxl:", openpyxl.__version__)
    except ImportError:
        print("openpyxl: nicht vorhanden")
    try:
        with urllib.request.urlopen("https://example.com", timeout=5) as r:
            print("Netz aus dem Skript: erreichbar, Status", r.status)
    except Exception as e:
        print("Netz aus dem Skript: nicht erreichbar (%s)" % type(e).__name__)
    print("Kennung:", KENNUNG)


def html(out):
    daten = {"kennung": KENNUNG, "text": "Umlaute äöü und Zeichen <>&"}
    block = json.dumps(daten, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    with open(out, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Machbarkeitstest</title></head>'
                '<body><h1>Machbarkeitstest Firmenbriefing</h1><p>Wenn diese Seite im Browser öffnet, funktioniert die HTML-Ausgabe.</p>'
                '<script type="application/json" id="briefing-daten">%s</script></body></html>' % block)
    print("geschrieben:", out)


def excel(out):
    from openpyxl import Workbook
    wb = Workbook()
    wb.active.title = "_daten"
    wb.active.append([json.dumps({"kennung": KENNUNG}, ensure_ascii=False)])
    wb.save(out)
    print("geschrieben:", out)


def lesen(pfad):
    if pfad.lower().endswith((".html", ".htm")):
        with open(pfad, encoding="utf-8") as f:
            m = re.search(r'<script type="application/json" id="briefing-daten">(.*?)</script>', f.read(), re.S)
        daten = json.loads(m.group(1)) if m else {}
    else:
        from openpyxl import load_workbook
        daten = json.loads(load_workbook(pfad, read_only=True)["_daten"]["A1"].value)
    print("gelesen:", daten)
    print("Ergebnis:", "OK" if daten.get("kennung") == KENNUNG else "FEHLER, Datenblock fehlt oder ist verändert")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="befehl", required=True)
    sub.add_parser("umgebung")
    for name in ("html", "excel"):
        sub.add_parser(name).add_argument("--out", required=True)
    sub.add_parser("lesen").add_argument("--datei", required=True)
    a = ap.parse_args()
    {"umgebung": lambda: umgebung(), "html": lambda: html(a.out), "excel": lambda: excel(a.out), "lesen": lambda: lesen(a.datei)}[a.befehl]()
