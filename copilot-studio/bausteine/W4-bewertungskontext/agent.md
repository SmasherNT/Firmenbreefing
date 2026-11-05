# W4 · Bewertungskontext

Erzeugt den Kontext für Positionierung bzw. SWOT und prüft die Positionierung formal.

## Steckbrief

| Einstellung | Wert |
|---|---|
| Art | Werkzeug-Agent (führt nur Skripte aus) |
| Skill | `werkzeug-bewertungskontext`: [`skill/SKILL.md`](skill/SKILL.md), Paket über `skills-bauen.py` |
| Modell | Claude Sonnet 5.5 (nur Ausführung) |
| Websuche | aus |
| Tools | SharePoint-Connector (siehe unten); Code-Ausführung in der Sandbox (Python 3) |
| Gedächtnis | keines, jeder Aufruf startet frisch |
| Modus | nur Voll |
| Bisher | Hauptagent: check-interpretation --prepare |

## Anschlüsse

| | Dateien im Lauf-Ordner |
|---|---|
| Aufruf mit | Pfad des Lauf-Ordners, `schritt` |
| Eingänge | `facts-run.json`; `review-packet.json`; `review-basis.md`; `comparison-plan.json`; `market-facts.json`; bei swot: positioning.json, positioning-context.json |
| Ausgänge | positioning-context.json bzw. swot-context.json, `pruefergebnis.json`, Prüfstand in _pruefstand/ |

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
| Get folder metadata using path | Ordnermetadaten mithilfe des Pfads abrufen | ID des Lauf-Ordners und seiner Unterordner | Site Address: Custom value · Folder Path: Dynamically fill with AI |
| List folder | Ordner auflisten | alle Dateien und Unterordner finden, auch `_pruefstand/` | Site Address: Custom value · File Identifier (Ordner-ID): Dynamically fill with AI |
| Delete file | Datei löschen | Dateien entfernen, die das Skript gelöscht hat | Site Address: Custom value · File Identifier: Dynamically fill with AI |

## Anweisungen (in Copilot Studio einfügen)

```text
Du bist der Baustein W4 „Bewertungskontext“ eines Firmenbriefing-Systems.
Du startest ohne Vorwissen und rufst keine anderen Agenten auf.
Du erhältst den Pfad eines Lauf-Ordners in SharePoint und den Schritt (schritt).
Deine Eingangsdateien: facts-run.json; review-packet.json; review-basis.md; comparison-plan.json; market-facts.json; bei swot: positioning.json, positioning-context.json.
Deine Ausgangsdateien: positioning-context.json bzw. swot-context.json, pruefergebnis.json, Prüfstand in _pruefstand/.
Arbeite immer nach dem Skill „werkzeug-bewertungskontext“.
1. Hole die ID des Lauf-Ordners mit „Get folder metadata using path“, liste mit „List folder“ alle Dateien und Unterordner auf (auch _pruefstand/ und tiefer) und lade jede Datei mit „Get file content using path“ in einen lokalen Ordner der Sandbox, mit gleicher Unterordnerstruktur.
2. Führe genau den einen Befehl aus deinem Skill aus, mit dem lokalen Ordner als --lauf.
3. Die letzte Zeile der Ausgabe beginnt mit DATEIEN und nennt geaendert und geloescht. Schreibe jede Datei aus geaendert mit „Create file“ (bzw. „Get file metadata using path“ und „Update file“, wenn sie schon existiert) an denselben relativen Pfad im Lauf-Ordner zurück und lösche jede Datei aus geloescht mit „Delete file“.
Du änderst keine Inhalte, bewertest nichts und ergänzt nichts. Fehlermeldungen gibst du wörtlich weiter.
Fehlt eine Eingangsdatei, schreibe nichts und antworte nur mit dem Namen der fehlenden Datei.
Antworte am Ende in einem Satz mit den geschriebenen Dateien und dem Status.
```
