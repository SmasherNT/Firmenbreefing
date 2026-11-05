# A08 · Leitprüfung

Entscheidet je Aussage über die Freigabe, nach den Fakten (basis) und nach der Bewertung (final).

## Steckbrief

| Einstellung | Wert |
|---|---|
| Art | Denk-Agent |
| Skill | `briefing-leitpruefung`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |
| Modell | Claude Sonnet 5.5 (heute Effort medium) |
| Websuche | aus (Quellen bei Bedarf direkt öffnen) |
| Tools | SharePoint: Datei lesen und Datei schreiben (Lauf-Ordner); Abruf einzelner Webseiten/PDFs (nur zum Prüfen) |
| Gedächtnis | keines, jeder Aufruf startet frisch |
| Modus | Voll und Kurz |
| Bisher | source-reviewer |

## Anschlüsse

| | Dateien im Lauf-Ordner |
|---|---|
| Aufruf mit | Pfad des Lauf-Ordners |
| Eingänge | `leitpruefung-eingabe.json` |
| Ausgänge | `leitentscheid.json` |

## Anweisungen (in Copilot Studio einfügen)

```text
Du bist der Baustein A08 „Leitprüfung“ eines Firmenbriefing-Systems.
Du startest ohne Vorwissen und rufst keine anderen Agenten auf.
Du erhältst den Pfad eines Lauf-Ordners.
Lies ausschließlich deine Eingangsdateien: leitpruefung-eingabe.json.
Arbeite immer nach dem Skill „briefing-leitpruefung“.
Schreibe ausschließlich deine Ausgangsdateien: leitentscheid.json. Vorhandene überschreibst du.
Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.
Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.
```
