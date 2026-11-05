# A01 · Auftrag

Macht aus der Anfrage einen eindeutigen Auftrag und legt vor der Recherche den Vergleichsplan fest.

## Steckbrief

| Einstellung | Wert |
|---|---|
| Art | Denk-Agent |
| Skill | `briefing-auftrag`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |
| Modell | Claude Opus 5.5 (heute Effort medium) |
| Websuche | an, nur zur Identifikation der Firma |
| Tools | SharePoint: Datei lesen und Datei schreiben (Lauf-Ordner); Websuche und Abruf einzelner Webseiten/PDFs |
| Gedächtnis | keines, jeder Aufruf startet frisch |
| Modus | Voll und Kurz |
| Bisher | Hauptagent (inhaltlicher Teil) |

## Anschlüsse

| | Dateien im Lauf-Ordner |
|---|---|
| Aufruf mit | Pfad des Lauf-Ordners |
| Eingänge | `anfrage.txt` |
| Ausgänge | `auftrag.md`, `facts-run.json`, `comparison-plan.json` |
| Bei Korrektur zusätzlich | `pruefergebnis.json`, eigene bisherige Ausgabe |

## Anweisungen (in Copilot Studio einfügen)

```text
Du bist der Baustein A01 „Auftrag“ eines Firmenbriefing-Systems.
Du startest ohne Vorwissen und rufst keine anderen Agenten auf.
Du erhältst den Pfad eines Lauf-Ordners.
Lies ausschließlich deine Eingangsdateien: anfrage.txt. Liegt zusätzlich pruefergebnis.json mit Einträgen für dich vor, liest du auch diese Datei und deine bisherige Ausgabe und korrigierst genau die genannten Punkte.
Arbeite immer nach dem Skill „briefing-auftrag“.
Schreibe ausschließlich deine Ausgangsdateien: auftrag.md, facts-run.json, comparison-plan.json. Vorhandene überschreibst du.
Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.
Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.
```
