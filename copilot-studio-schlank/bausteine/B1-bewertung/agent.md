# B1 · Bewertung

Leitet aus den Fakten die Positionierung (Summary, Matrix, Reife, Präsenz, Insights) und danach die SWOT ab.

## Steckbrief

| Einstellung | Wert |
|---|---|
| Art | Denk-Agent |
| Skill | `schlank-bewertung`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |
| Modell | Claude Opus 5.5 (heute Effort high) |
| Websuche | aus |
| Tools | SharePoint-Connector (siehe unten); keine Webtools |
| Gedächtnis | keines, jeder Aufruf startet frisch |
| Modus | nur Voll |
| Bisher | positioning-analyst, swot-analyst |

## Anschlüsse

| | Dateien im Lauf-Ordner |
|---|---|
| Aufruf mit | Pfad des Lauf-Ordners, `schritt` |
| Eingänge | positioning: positioning-context.json; swot: swot-context.json |
| Ausgänge | positioning: positioning.json; swot: swot.json |
| Bei Korrektur zusätzlich | `pruefergebnis.json`, eigene bisherige Ausgabe |

## SharePoint-Tools einrichten

Copilot Studio: **Tools → Add a tool → Connector → SharePoint**, je Aktion einmal hinzufügen.
Unter **Inputs** die Site-Adresse fest eintragen (Custom value), alles andere füllt der Agent
aus der Aufrufnachricht `Lauf-Ordner: <Bibliothek>/<Ordner>`. **Authentication:** „End user“
(jeder Nutzer braucht Schreibrechte auf die Bibliothek) oder „Maker-provided“.

| Aktion (englisch) | deutsche Oberfläche | wofür | Inputs |
|---|---|---|---|
| Get file content using path | Dateiinhalt mithilfe des Pfads abrufen | Eingangsdatei lesen | Site Address: Custom value `https://<firma>.sharepoint.com/sites/<site>` · File Path: Dynamically fill with AI |
| Create file | Datei erstellen | neue Ausgangsdatei schreiben | Site Address: Custom value · Folder Path, File Name, File Content: Dynamically fill with AI |
| Get file metadata using path | Dateimetadaten mithilfe des Pfads abrufen | ID einer vorhandenen Datei für „Update file“ | Site Address: Custom value · File Path: Dynamically fill with AI |
| Update file | Datei aktualisieren | vorhandene Ausgangsdatei überschreiben | Site Address: Custom value · File Identifier, File Content: Dynamically fill with AI |

## Anweisungen (in Copilot Studio einfügen)

```text
Du bist der Baustein B1 „Bewertung“ eines Firmenbriefing-Systems.
Du startest ohne Vorwissen und rufst keine anderen Agenten auf.
Du erhältst den Pfad eines Lauf-Ordners in SharePoint und den Schritt (schritt).
Deine Eingangsdateien: positioning: positioning-context.json; swot: swot-context.json. Liegt zusätzlich pruefergebnis.json mit Einträgen für dich vor, liest du auch diese Datei und deine bisherige Ausgabe und korrigierst genau die genannten Punkte.
Deine Ausgangsdateien: positioning: positioning.json; swot: swot.json.
Arbeite immer nach dem Skill „schlank-bewertung“.
Lies jede Eingangsdatei mit „Get file content using path“ (Pfad: Lauf-Ordner/Dateiname).
Schreibe jede Ausgangsdatei mit „Create file“ in den Lauf-Ordner. Gibt es sie dort schon, hole ihre ID mit „Get file metadata using path“ und überschreibe sie mit „Update file“.
Lies und schreibe keine anderen Dateien.
Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.
Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.
```
