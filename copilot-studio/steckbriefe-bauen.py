#!/usr/bin/env python3
"""Erzeugt bausteine/<ID>/agent.md (Steckbrief und Anweisungen) aus bausteine.json.

Aufruf aus dem Repository-Stamm:

    python3 copilot-studio/steckbriefe-bauen.py [Ordner mit bausteine.json]
"""
import json
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
data = json.loads((root / "bausteine.json").read_text(encoding="utf-8"))

PARAM = {
    "focus_id": "die ID genau eines Fokusthemas (focus_id)",
    "job": "die Nummer genau eines Prüfjobs (job)",
    "phase": "die Phase: basis oder final",
    "schritt": "den Schritt (schritt)",
    "modul": "das Modul (modul)",
}

SITE = "https://<firma>.sharepoint.com/sites/<site>"

# SharePoint-Aktionen (englische Oberfläche · deutsche Oberfläche): wofür, Einstellungen der Inputs
SP_LESEN = [
    ("Get file content using path", "Dateiinhalt mithilfe des Pfads abrufen", "Eingangsdatei lesen",
     "Site Address: Custom value `" + SITE + "` · File Path: Dynamically fill with AI"),
    ("Create file", "Datei erstellen", "neue Ausgangsdatei schreiben",
     "Site Address: Custom value · Folder Path, File Name, File Content: Dynamically fill with AI"),
    ("Get file metadata using path", "Dateimetadaten mithilfe des Pfads abrufen", "ID einer vorhandenen Datei für „Update file“",
     "Site Address: Custom value · File Path: Dynamically fill with AI"),
    ("Update file", "Datei aktualisieren", "vorhandene Ausgangsdatei überschreiben",
     "Site Address: Custom value · File Identifier, File Content: Dynamically fill with AI"),
]
SP_ORDNER = [
    ("Get folder metadata using path", "Ordnermetadaten mithilfe des Pfads abrufen", "ID des Lauf-Ordners und seiner Unterordner",
     "Site Address: Custom value · Folder Path: Dynamically fill with AI"),
    ("List folder", "Ordner auflisten", "alle Dateien und Unterordner finden, auch `_pruefstand/`",
     "Site Address: Custom value · File Identifier (Ordner-ID): Dynamically fill with AI"),
    ("Delete file", "Datei löschen", "Dateien entfernen, die das Skript gelöscht hat",
     "Site Address: Custom value · File Identifier: Dynamically fill with AI"),
]


def trenner(xs):
    """Semikolon, wenn die Einträge nach Modulen gegliedert sind (\"modul: dateien\")."""
    return "; " if any(": " in x for x in xs) else ", "


def liste(xs):
    return trenner(xs).join(f"`{x}`" if not x.startswith(("bei ", "Prüfstand")) and "(" not in x and "…" not in x and " " not in x else x for x in xs)

for b in data["bausteine"]:
    denk = b["art"] == "denk"
    tools = ["SharePoint-Connector (siehe unten)"]
    if denk and b["websuche"].startswith("an"):
        tools.append("Websuche und Abruf einzelner Webseiten/PDFs")
    elif denk:
        tools.append("Abruf einzelner Webseiten/PDFs (nur zum Prüfen)" if b["id"] in ("A07", "A08") else "keine Webtools")
    else:
        tools.append("Code-Ausführung in der Sandbox (Python 3)")
    params = "".join(f" und {PARAM[p]}" for p in b["parameter"])
    korr = ""
    if b["korrektur"]:
        korr = (" Liegt zusätzlich `pruefergebnis.json` mit Einträgen für dich vor, "
                "liest du auch diese Datei und deine bisherige Ausgabe und korrigierst genau die genannten Punkte.")
    lines = [
        f"# {b['id']} · {b['titel']}",
        "",
        b["kurz"],
        "",
        "## Steckbrief",
        "",
        "| Einstellung | Wert |",
        "|---|---|",
        f"| Art | {'Denk-Agent' if denk else 'Werkzeug-Agent (führt nur Skripte aus)'} |",
        f"| Skill | `{b['skill']}`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |",
        f"| Modell | {b['modell']}" + (f" (heute Effort {b['effort_heute']})" if b['effort_heute'] != '–' else "") + " |",
        f"| Websuche | {b['websuche']} |",
        f"| Tools | {'; '.join(tools)} |",
        "| Gedächtnis | keines, jeder Aufruf startet frisch |",
        f"| Modus | {b['modus']} |",
        f"| Bisher | {b['bisher']} |",
        "",
        "## Anschlüsse",
        "",
        "| | Dateien im Lauf-Ordner |",
        "|---|---|",
        "| Aufruf mit | Pfad des Lauf-Ordners" + "".join(f", `{p}`" for p in b["parameter"]) + " |",
        f"| Eingänge | {liste(b['eingaenge'])} |",
        f"| Ausgänge | {liste(b['ausgaenge'])} |",
    ]
    if b["korrektur"]:
        lines.append("| Bei Korrektur zusätzlich | `pruefergebnis.json`, eigene bisherige Ausgabe |")
    aktionen = SP_LESEN + ([] if denk else SP_ORDNER)
    lines += ["", "## SharePoint-Tools einrichten", "",
              "Copilot Studio: **Tools → Add a tool → Connector → SharePoint**, je Aktion einmal hinzufügen.",
              "Unter **Inputs** die Site-Adresse fest eintragen (Custom value), alles andere füllt der Agent",
              "aus der Aufrufnachricht `Lauf-Ordner: <Bibliothek>/<Ordner>`. **Authentication:** „End user“",
              "(jeder Nutzer braucht Schreibrechte auf die Bibliothek) oder „Maker-provided“.", "",
              "| Aktion (englisch) | deutsche Oberfläche | wofür | Inputs |", "|---|---|---|---|"]
    lines += [f"| {en} | {de} | {zweck} | {inp} |" for en, de, zweck, inp in aktionen]
    lines += ["", "## Anweisungen (in Copilot Studio einfügen)", "", "```text"]
    text = [
        f"Du bist der Baustein {b['id']} „{b['titel']}“ eines Firmenbriefing-Systems.",
        "Du startest ohne Vorwissen und rufst keine anderen Agenten auf.",
        f"Du erhältst den Pfad eines Lauf-Ordners in SharePoint{params}.",
        "Deine Eingangsdateien: " + trenner(b["eingaenge"]).join(b["eingaenge"]) + "." + korr.replace("`", ""),
        "Deine Ausgangsdateien: " + trenner(b["ausgaenge"]).join(b["ausgaenge"]) + ".",
        f"Arbeite immer nach dem Skill „{b['skill']}“.",
    ]
    if denk:
        text += [
            "Lies jede Eingangsdatei mit „Get file content using path“ (Pfad: Lauf-Ordner/Dateiname).",
            "Schreibe jede Ausgangsdatei mit „Create file“ in den Lauf-Ordner. Gibt es sie dort schon, hole ihre ID "
            "mit „Get file metadata using path“ und überschreibe sie mit „Update file“.",
            "Lies und schreibe keine anderen Dateien.",
        ]
    else:
        text += [
            "1. Hole die ID des Lauf-Ordners mit „Get folder metadata using path“, liste mit „List folder“ alle Dateien "
            "und Unterordner auf (auch _pruefstand/ und tiefer) und lade jede Datei mit „Get file content using path“ "
            "in einen lokalen Ordner der Sandbox, mit gleicher Unterordnerstruktur.",
            "2. Führe genau den einen Befehl aus deinem Skill aus, mit dem lokalen Ordner als --lauf.",
            "3. Die letzte Zeile der Ausgabe beginnt mit DATEIEN und nennt geaendert und geloescht. Schreibe jede Datei "
            "aus geaendert mit „Create file“ (bzw. „Get file metadata using path“ und „Update file“, wenn sie schon "
            "existiert) an denselben relativen Pfad im Lauf-Ordner zurück und lösche jede Datei aus geloescht mit "
            "„Delete file“.",
            "Du änderst keine Inhalte, bewertest nichts und ergänzt nichts. Fehlermeldungen gibst du wörtlich weiter.",
        ]
    text += [
        "Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.",
        "Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.",
    ]
    lines += text + ["```", ""]
    out = root / "bausteine" / b["ordner"] / "agent.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out.relative_to(root))
