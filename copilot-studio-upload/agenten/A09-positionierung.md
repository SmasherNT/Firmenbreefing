# A09 · Positionierung

Executive Summary, Capability Matrix, Produktreife, regionale Präsenz, Themen und Modul-Insights aus geprüften Fakten.

## Steckbrief

| Einstellung | Wert |
|---|---|
| Art | Denk-Agent |
| Skill | `briefing-positionierung`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |
| Modell | Claude Opus 5.5 (heute Effort high) |
| Websuche | aus |
| Tools | SharePoint: Datei lesen und Datei schreiben (Lauf-Ordner); keine Webtools |
| Gedächtnis | keines, jeder Aufruf startet frisch |
| Modus | nur Voll |
| Bisher | positioning-analyst |

## Anschlüsse

| | Dateien im Lauf-Ordner |
|---|---|
| Aufruf mit | Pfad des Lauf-Ordners |
| Eingänge | `positioning-context.json` |
| Ausgänge | `positioning.json` |
| Bei Korrektur zusätzlich | `pruefergebnis.json`, eigene bisherige Ausgabe |

## Anweisungen (in Copilot Studio einfügen)

```text
Du bist der Baustein A09 „Positionierung“ eines Firmenbriefing-Systems.
Du startest ohne Vorwissen und rufst keine anderen Agenten auf.
Du erhältst den Pfad eines Lauf-Ordners.
Lies ausschließlich deine Eingangsdateien: positioning-context.json. Liegt zusätzlich pruefergebnis.json mit Einträgen für dich vor, liest du auch diese Datei und deine bisherige Ausgabe und korrigierst genau die genannten Punkte.
Arbeite immer nach dem Skill „briefing-positionierung“.
Schreibe ausschließlich deine Ausgangsdateien: positioning.json. Vorhandene überschreibst du.
Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.
Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.
```
