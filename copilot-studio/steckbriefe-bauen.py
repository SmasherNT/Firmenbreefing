#!/usr/bin/env python3
"""Erzeugt bausteine/<ID>/agent.md (Steckbrief und Anweisungen) aus bausteine.json.

Aufruf aus dem Repository-Stamm:

    python3 copilot-studio/steckbriefe-bauen.py
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / "bausteine.json").read_text(encoding="utf-8"))

PARAM = {
    "focus_id": "die ID genau eines Fokusthemas (focus_id)",
    "job": "die Nummer genau eines Prüfjobs (job)",
    "phase": "die Phase: basis oder final",
    "schritt": "den Schritt: positioning oder swot",
}

def liste(xs):
    return ", ".join(f"`{x}`" if not x.startswith(("bei ", "Prüfstand")) and "(" not in x and "…" not in x and " " not in x else x for x in xs)

for b in data["bausteine"]:
    denk = b["art"] == "denk"
    tools = ["SharePoint: Datei lesen und Datei schreiben (Lauf-Ordner)"]
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
    lines += ["", "## Anweisungen (in Copilot Studio einfügen)", "", "```text"]
    text = [
        f"Du bist der Baustein {b['id']} „{b['titel']}“ eines Firmenbriefing-Systems.",
        "Du startest ohne Vorwissen und rufst keine anderen Agenten auf.",
        f"Du erhältst den Pfad eines Lauf-Ordners{params}.",
        "Lies ausschließlich deine Eingangsdateien: " + ", ".join(b["eingaenge"]) + "." + korr.replace("`", ""),
        f"Arbeite immer nach dem Skill „{b['skill']}“.",
    ]
    if not denk:
        text.append("Du führst genau den einen Befehl aus deinem Skill aus. Du änderst keine Inhalte, "
                    "bewertest nichts und ergänzt nichts. Fehlermeldungen gibst du wörtlich weiter.")
    text += [
        "Schreibe ausschließlich deine Ausgangsdateien: " + ", ".join(b["ausgaenge"]) + ". Vorhandene überschreibst du.",
        "Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.",
        "Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.",
    ]
    lines += text + ["```", ""]
    out = root / "bausteine" / b["ordner"] / "agent.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out.relative_to(root))
