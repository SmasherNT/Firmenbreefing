# Betrieb in Microsoft Copilot Cowork

## Einstieg und Pfade

Der vollständige Projektstamm ist der Ordner copilot-cowork/. Bei importierten
Uploads ist es der von resources/bootstrap.py zurückgegebene project_root.
AGENTS.md ist ausdrücklich zu lesen; keine automatische Erkennung unterstellen.
Alle references/-, roles/-, skills/-, scripts/- und runs/-Pfade gelten darin.
Den alten Repository-Stamm weder als Quellenvertrag noch als Ausgabeziel verwenden.

## Import und Distribution

Die zwölf SKILL.md-Methoden verwenden name/description als Frontmatter.
roles/*.md sind fachliche Rollenverträge, keine importierbaren Agentenprofile.
Der Upload von Skills registriert weder diese Rollen noch Laufzeiteinstellungen.
Ein einzelner unverpackter Skillordner enthält absichtlich keine fremden Kopien
der gemeinsamen Referenzen. Für eigenständigen Import die Uploads erzeugen:

```bash
python3 scripts/build-cowork-skills.py --out dist/skills
```

Jede erzeugte .skill-Datei enthält SKILL.md und zwei Begleitdateien:
resources/bootstrap.py sowie resources/runtime.zip. Das Archiv ist eine
versionierte Projektlaufzeit, kein Plugin- oder Agenteninstaller. Der Bootstrap
prüft SHA-256 und sichere Pfade, entpackt im Arbeitsbereich und verweigert das
Überschreiben geänderter Runtime-Dateien. Alle Uploads derselben Version nutzen
denselben Projektstamm; Ergebnisse entstehen unter dessen runs/.
So bleiben gemeinsame Referenzen/Renderer vollständig, ohne je Methode Dutzende
lose Begleitdateien oder relative Pfade außerhalb des Skills vorauszusetzen.
Der Host muss Archive als Begleitdateien und Python-Ausführung zulassen; der
tatsächliche Import ist im Mandanten zu testen. Der lokale Pakettest ersetzt ihn nicht.

In Cowork: Customize → Skills → Add → Upload skill. Zuerst company-briefing,
weitere Methoden nach Bedarf importieren. Einen neuen Chat für neue Versionen
verwenden und alte gleichnamige Imports entfernen/gezielt deaktivieren.
Alternativ den vollständigen Projektordner als Arbeitsgrundlage bereitstellen und
AGENTS.md explizit laden. Ein GitHub-Link allein lädt keine Projektlaufzeit.

## Laufzeitprüfung

```bash
python3 scripts/cowork-preflight.py --out work/preflight.json --strict
```

Python, beschreibbares Arbeitsverzeichnis und POSIX-fcntl für Checkpoints sind
nötig. Node.js, playwright-core und Chromium werden für die vorhandenen Browser-
und Druckprüfungen benötigt. BRIEFING_CHROMIUM_PATH setzt den Browserpfad.
pdftotext unterstützt die PDF-Extraktion; ohne Extraktion Originale anders lesen.
Bei fehlender Laufzeit geeigneten externen Worker/Connector verwenden. Keine
Prüfung als bestanden melden, die dort nicht tatsächlich ausgeführt wurde.

Websuche/Originalaufruf und unabhängige Kontexte sind keine lokal messbaren
Hostfähigkeiten. Im tatsächlichen Mandanten einen Quellenaufruf und zwei
getrennte Rollenproben mit eigenen Dateizielen durchführen. Den beobachteten
Nachweis erst danach als JSON an --host-evidence übergeben, pro Fähigkeit:

```json
{
  "web_search_fetch": {"tested": true, "host": "tatsächlich verwendeter Host", "tested_at": "Zeitpunkt der Probe", "evidence": "konkreter Quellenaufruf mit Ergebnis"},
  "independent_contexts": {"tested": true, "host": "tatsächlich verwendeter Host", "tested_at": "Zeitpunkt der Probe", "evidence": "konkrete getrennte Aufruf-IDs und Dateiergebnisse"}
}
```

Dies ist eine externe Attestierung, keine automatische Verifikation des Hosts.
Ohne Nachweis meldet --strict blockiert (Exitcode 2). Der JSON-Beispieltext ist
keine echte Probe und darf nicht als Nachweis übernommen werden.

## Rollen und Modellwahl

Hauptagent: nur Auftrag, Koordination, mechanische Zusammenführung und Rendering.
Autoren- und Reviewer-Kontexte getrennt halten. Kontext/Portfolio/Cluster/Markt
jeweils delegieren; je Fokusthema genau ein focus-analyst-Aufruf mit eigener Datei.
Dokumentprüfung: bis zu drei disjunkte Jobs, danach separater source-reviewer.
Positionierung nach Basisfreigabe, danach SWOT und gemeinsames Schlussreview.
Serielle getrennte Kontexte sind erlaubt, falls keine Parallelität verfügbar ist.
Bei fehlender Delegation stoppen; keine Mehrrollen-Simulation in einem Chat.

Den Rollenvertrag und zugeordnete skills explizit in jede Übergabe aufnehmen;
kein automatisches Vorladen durch ein früheres skills-YAML-Feld voraussetzen.
Modell/Effort sind hostabhängige Wünsche gemäß modellaufteilung.json; auto ist
kein beobachteter Modellname. Sichtbare Aufrufmetadaten dokumentieren, sonst
unbekannt. Keine erfundene Modell- oder Effort-Zuordnung im Abnahmebericht.

## Speicherung und Wiederaufnahme

Neue run_id und eigenes runs/<run_id>/ je Auftrag. Den gesamten aktiven Lauf
einschließlich Manifest, Cache, Quellenbelegen, Reviews und Checkpoints im
beauftragten OneDrive-/SharePoint-Ziel sichern, nicht nur die HTML.
Absolute Checkpointpfade sind an den bisherigen Arbeitsbereich gebunden. Nach
Wechsel des Workspace keine Checkpoints blind übernehmen oder auf neuere Dateien
stempeln: Zustand und Pfade prüfen; bei ungültiger Bindung neuen Lauf beginnen.
Der Bootstrap versioniert nur Programmdateien, übernimmt keine alten Läufe.
GitHub-Schreibzugriffe nur bei ausdrücklichem Auftrag; kein automatisches Pushen
von recherchierten Firmenbriefings aus einem gewöhnlichen Cowork-Auftrag.

## Pilot-Abnahme

Ein vollständiges Briefing mit optionaler Person und zwei neutralen Fokusthemen
im echten Host testen. Aufrufprotokoll, echte Quellenlektüre, Basis-/Schlussreview,
getrennte Fokusdateien, Wiederaufnahme, Netzwerkfilter, Quellenlinks und Druck
nachweisen. Lokale synthetische Tests allein belegen diesen Pilot nicht.

Offizielle Referenzen, geprüft am 03.11.2026:
- https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize
- https://learn.microsoft.com/en-us/copilot/cowork/cowork-plugin-development
- https://learn.microsoft.com/en-us/copilot/cowork/use-cowork
