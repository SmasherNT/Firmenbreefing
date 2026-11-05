# Briefing-Werkstatt (Tool-Backend)

Die Werkstatt übernimmt die mechanische Arbeit des bisherigen Hauptagenten:
Dateien ablegen, Formate prüfen, Prüfpakete bauen, Freigaben stempeln und die
HTML rendern. Sie denkt nicht und bewertet nichts. Sie ruft die **vorhandenen
Skripte unter `scripts/` direkt auf**, ohne sie zu kopieren oder umzuschreiben.
Deshalb entsteht aus denselben Daten dieselbe HTML wie heute.

In Copilot Studio erscheint die Werkstatt als **Custom Connector** mit den
Aktionen unten. Die Definition steht in `openapi.yaml`.

## Ablage je Lauf

Die Werkstatt verwaltet je Lauf genau die heutige Ordnerstruktur:

```
runs/<run_id>/
  input/   auftrag.md, facts-run.json
  work/    comparison-plan.json, *-facts.json, document-cache/,
           review-*.json, positioning*.json, swot*.json
  output/  briefing.html
```

Der Flow legt am Ende HTML und optional ein ZIP des Laufs in SharePoint ab.

## Aktionen

| Aktion | Eingabe | Ausgabe | Nutzt vorhandene Skripte |
|---|---|---|---|
| `laufAnlegen` | anfrage, modus | run_id, stichtag | – |
| `auftragSpeichern` | run_id, Ergebnis Agent 01 | ok, fehler, rollen, fokus | `source-cache.py init` |
| `eingabeHolen` | run_id, rolle, optional rueckgabe | dokument | `fact-index.py` (Auszüge) |
| `quelleAbrufen` | run_id, url, optional seite | source_id, Metadaten, Textausschnitt mit Seitenmarkern | `source-cache.py fetch/show/read`, `prepare-facts.py --source-id` |
| `modulSpeichern` | run_id, rolle, Ergebnis Agent 02–06 | ok, fehler | Formatprüfung je Modul |
| `pruefungVorbereiten` | run_id, phase | formatfehler je Modul **oder** jobs | `prepare-facts.py`, `check-interpretation.py --merge-validation`, `review-work.py prepare`, `review-shards.py split/show` |
| `befundSpeichern` | run_id, phase, job_id, Ergebnis Agent 07 | ok, fehler | – |
| `leitpruefungEingabe` | run_id, phase | dokument | `review-shards.py collect` |
| `pruefungAbschliessen` | run_id, phase, Ergebnis Agent 08 | bestanden, rueckgabe je Modul, fehler | `review-shards.py merge`, `stamp-review.py --work` |
| `bewertungEingabe` | run_id, schritt | dokument | `check-interpretation.py --prepare` |
| `bewertungSpeichern` | run_id, schritt, Ergebnis Agent 09/10 | ok, fehler, rueckfragen | `check-interpretation.py` (Validierung) |
| `briefingRendern` | run_id, modus | dateiname, html | `render-briefing.py` (`--full` bei Voll) |
| `laufArchiv` | run_id | ZIP | – |

## Was die Werkstatt den Agenten abnimmt

Agenten sind gut im Recherchieren und Prüfen, aber schlecht im Abschreiben
langer Prüfsummen. Deshalb ergänzt die Werkstatt in jedem gespeicherten
Ergebnis:

- **Kopffelder:** `schema_version`, `mode`, `role`, `run_id`, `company`, `as_of`,
  `scope`, bei Fokus `focus_id`.
- **Quellen-IDs:** aus der URL neu berechnet (`S-` plus SHA-256), Verweise in
  Aussagen und Netzwerk werden angepasst.
- **Prüfsummen:** `input_fingerprint`, `plan_fingerprint`,
  `review_work_fingerprint`, `source_collection_fingerprint` aus dem aktuellen
  Stand. Der Flow stellt sicher, dass jeder Agent genau diesen Stand gesehen hat.

## Rückgabe an die Module

`pruefungAbschliessen` liefert bei „nicht bestanden“ eine `rueckgabe`,
gruppiert nach `owner` aus der Leitprüfung: `context`, `portfolio`,
`cluster`, `market`, `focus:<id>`, `positioning`, `swot`. Je Eintrag die
betroffenen IDs mit `reason` und `action`. Der Flow schickt jede Gruppe an
genau den zuständigen Agenten.

## Auswahl für die Bewertung (erste Version)

Bisher wählte der Hauptagent die relevanten Fakten für Positionierung und SWOT
aus. In der ersten Version übernimmt die Werkstatt **alle A-geprüften Fakten
der vier Kernmodule** in den Positionierungskontext. Fokusseiten bleiben
draußen, wie heute. Für die SWOT kommen alle Positionierungsaussagen mit ihren
Fakten hinzu. Das ist vollständig, kostet aber mehr Token. Eine engere Auswahl
ist ein späterer Optimierungsschritt.

## Betrieb

| Thema | Vorschlag | Offen |
|---|---|---|
| Hosting | Azure Functions (Python 3.12) als Container | Freigabe durch IT |
| Ablage `runs/` | dauerhafter Dateispeicher (z. B. Azure Files) | Dateisperren für den Quellen-Cache testen |
| PDF-Text | `pdftotext` im Container | – |
| Netzwerk | ausgehender Zugriff auf öffentliche Webseiten | Proxy-Regeln |
| Anmeldung | Schlüssel oder Entra ID für den Connector | Vorgabe der IT |
| Code | dünne Hülle um `scripts/`, keine Kopie der Fachlogik | noch zu bauen |
