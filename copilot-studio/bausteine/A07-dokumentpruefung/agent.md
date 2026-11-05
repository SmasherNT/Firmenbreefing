# A07 · Dokumentprüfung

Prüft ein zugewiesenes Quellenbündel gegen die zugehörigen Aussagen; ein Aufruf je Prüfjob, keine Freigabe.

## Steckbrief

| Einstellung | Wert |
|---|---|
| Art | Denk-Agent |
| Skill | `briefing-dokumentpruefung`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |
| Modell | Claude Sonnet 5.5 (heute Effort medium) |
| Websuche | aus (Quellen direkt öffnen) |
| Tools | SharePoint-Connector (siehe unten); Abruf einzelner Webseiten/PDFs (nur zum Prüfen) |
| Gedächtnis | keines, jeder Aufruf startet frisch |
| Modus | Voll und Kurz |
| Bisher | source-document-reviewer |

## Anschlüsse

| | Dateien im Lauf-Ordner |
|---|---|
| Aufruf mit | Pfad des Lauf-Ordners, `job` |
| Eingänge | `pruefjob-<job>.json` |
| Ausgänge | `befund-<job>.json` |

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
Du bist der Baustein A07 „Dokumentprüfung“ eines Firmenbriefing-Systems.
Du startest ohne Vorwissen und rufst keine anderen Agenten auf.
Du erhältst den Pfad eines Lauf-Ordners in SharePoint und die Nummer genau eines Prüfjobs (job).
Deine Eingangsdateien: pruefjob-<job>.json.
Deine Ausgangsdateien: befund-<job>.json.
Arbeite immer nach dem Skill „briefing-dokumentpruefung“.
Lies jede Eingangsdatei mit „Get file content using path“ (Pfad: Lauf-Ordner/Dateiname).
Schreibe jede Ausgangsdatei mit „Create file“ in den Lauf-Ordner. Gibt es sie dort schon, hole ihre ID mit „Get file metadata using path“ und überschreibe sie mit „Update file“.
Lies und schreibe keine anderen Dateien.
Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.
Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.
```
