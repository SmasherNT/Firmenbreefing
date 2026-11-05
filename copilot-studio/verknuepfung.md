# Bausteine verknüpfen

Die Bausteine kennen sich nicht. Du legst fest, wer wann läuft. Jeder Baustein
bekommt nur den Pfad des Lauf-Ordners (und ggf. einen Parameter), liest seine
Eingangsdateien und schreibt seine Ausgangsdateien. Passen die Dateinamen,
passen die Bausteine zusammen.

## Lauf-Ordner anlegen

1. In SharePoint einen Ordner je Lauf anlegen, z. B. `Briefings/<firma>-<datum>/`.
2. Darin `anfrage.txt` mit der Nachricht ablegen. Erste Zeile optional
   `modus: voll` oder `modus: kurz`.

Alle weiteren Dateien entstehen durch die Bausteine. Jeder Baustein liest und
schreibt sie selbst über seine SharePoint-Aktionen; Einrichtung siehe
`README.md`, Abschnitt „SharePoint einrichten“. Welche das sind, steht in
[`dateien.md`](dateien.md).

## Aufruf eines Bausteins

Im Agent Flow: Aktion „Agent aufrufen“ mit dem Baustein und einer kurzen
Nachricht, zum Beispiel:

```text
Lauf-Ordner: Briefings/beispiel-ag-20261105
```

Mit Parameter:

```text
Lauf-Ordner: Briefings/beispiel-ag-20261105
focus_id: drohnen
```

Parameter: `focus_id` (A06), `job` (A07), `phase` (W1, W2, W3: basis oder final),
`schritt` (W4: positioning oder swot).

## Prüftore

Nach W1, W3 und W4 liegt `pruefergebnis.json` im Lauf-Ordner:

```json
{"schritt": "freigabe", "phase": "basis", "bestanden": false, "jobs": 0,
 "rueckgabe": {"portfolio": [{"ids": ["P7"], "reason": "…", "action": "…"}]}}
```

Im Flow: Datei lesen, als JSON auswerten, Bedingung auf `bestanden`.

- **bestanden = true:** weiter mit dem nächsten Schritt.
- **bestanden = false:** je Eintrag in `rueckgabe` den zuständigen Baustein
  erneut aufrufen. Er liest `pruefergebnis.json` selbst und korrigiert genau
  diese Punkte. Danach zurück zu W1 (Phase basis) bzw. zum genannten Schritt.

| owner in `rueckgabe` | Baustein | danach weiter mit |
|---|---|---|
| `auftrag` | A01 | A01-Folgeschritte neu |
| `context` | A02 | W1 basis |
| `portfolio` | A03 | W1 basis |
| `cluster` | A04 | W1 basis |
| `market` | A05 | W1 basis |
| `focus:<id>` | A06 mit `focus_id` | W1 basis |
| `positioning` | A09 | W4 swot (14), danach A10 und W1 final |
| `swot` | A10 | W1 final |
| `werkzeug` | keiner: technischer Fehler | Meldung in `fehler` lesen, Ursache beheben, Schritt wiederholen |

## Schaltplan

Alle Schritte mit sämtlichen Ein- und Ausgabedateien:
[`zielbild/schaltplan.html`](zielbild/schaltplan.html), als Bild
[`zielbild/schaltplan.png`](zielbild/schaltplan.png).

## Rezept Vollbriefing

| # | Agent | Parameter | liest | schreibt |
|---|---|---|---|---|
| 1 | A01 Auftrag | – | `anfrage.txt` | `auftrag.md`, `facts-run.json`, `comparison-plan.json` |
| 2 | A02 Kontext & Person | – | `auftrag.md`, `facts-run.json` | `context-facts.json` |
| 3 | A03 Portfolio & Präsenz | – | `auftrag.md`, `facts-run.json` | `portfolio-facts.json` |
| 4 | A04 Cluster & Netzwerk | – | `auftrag.md`, `facts-run.json` | `cluster-facts.json` |
| 5 | A05 Markt & Wettbewerb | – | `auftrag.md`, `facts-run.json`, `comparison-plan.json` | `market-facts.json` |
| 6 | A06 Fokusthema, je Eintrag in `facts-run.json → focus_pages` | `focus_id` | `auftrag.md`, `facts-run.json` | `focus-<id>-facts.json` |
| 7 | W1 Prüfpaket | `phase: basis` | `facts-run.json`, `comparison-plan.json`, alle `*-facts.json` | `pruefergebnis.json`, `review-packet.json`, `pruefjob-<n>.json`, `_pruefstand/` |
| | **Prüftor A** | | `pruefergebnis.json` | nein: Baustein aus `rueckgabe` korrigiert, dann ab 7 |
| 8 | A07 Dokumentprüfung, je Job (`jobs` aus Prüftor A) | `job: <n>` | `pruefjob-<n>.json` | `befund-<n>.json` |
| 9 | W2 Befunde bündeln | `phase: basis` | `befund-<n>.json`, `review-packet.json`, `auftrag.md`, `_pruefstand/` | `leitpruefung-eingabe.json` |
| 10 | A08 Leitprüfung | – | `leitpruefung-eingabe.json` | `leitentscheid.json` |
| 11 | W3 Freigabe | `phase: basis` | `leitentscheid.json`, `befund-<n>.json`, `review-packet.json`, `_pruefstand/` | `review-basis.md`, `pruefergebnis.json` |
| | **Prüftor 1** | | `pruefergebnis.json` | nein: Baustein aus `rueckgabe` korrigiert, dann ab 7 |
| 12 | W4 Bewertungskontext | `schritt: positioning` | `facts-run.json`, `review-packet.json`, `review-basis.md`, `comparison-plan.json`, `market-facts.json`, `portfolio-facts.json` | `positioning-context.json`, `pruefergebnis.json` |
| 13 | A09 Positionierung | – | `positioning-context.json` | `positioning.json` |
| 14 | W4 Bewertungskontext | `schritt: swot` | wie 12 plus `positioning.json`, `positioning-context.json` | `swot-context.json`, `pruefergebnis.json` |
| | **Prüftor B** | | `pruefergebnis.json` | nein: A09 korrigiert, dann ab 14; Rückfrage an A02–A05: diese korrigieren, dann ab 7 |
| 15 | A10 SWOT | – | `swot-context.json` | `swot.json` |
| 16 | W1 Prüfpaket | `phase: final` | Prüfpaket, Review, Positionierung, SWOT, Kontexte, `_pruefstand/` | `pruefergebnis.json`, `pruefjob-<n>.json` |
| | **Prüftor C** | | `pruefergebnis.json` | nein: A09 bzw. A10 korrigiert, dann ab 14 bzw. 16 |
| 17 | A07 Dokumentprüfung, je Job (oft keiner) | `job: <n>` | `pruefjob-<n>.json` | `befund-<n>.json` |
| 18 | W2 Befunde bündeln | `phase: final` | wie 9 plus Positionierung, SWOT, Kontexte | `leitpruefung-eingabe.json` |
| 19 | A08 Leitprüfung | – | `leitpruefung-eingabe.json` | `leitentscheid.json` |
| 20 | W3 Freigabe | `phase: final` | `leitentscheid.json`, `befund-<n>.json`, `review-packet.json`, `_pruefstand/` | `review-final.md`, `pruefergebnis.json` |
| | **Prüftor 2** | | `pruefergebnis.json` | nein: A09 → ab 14, A10 → ab 16, Faktenbaustein → ab 7 |
| 21 | W5 Briefing rendern | – | alle freigegebenen Dateien | `briefing.html` |

Danach im Flow: Link zu `briefing.html` per Teams oder E-Mail verschicken.

## Rezept Kurzbriefing

`anfrage.txt` beginnt mit `modus: kurz`. Dann nur die Schritte 1, 2, 3, 7 bis 11
und 21. A01 schreibt keinen Vergleichsplan, W5 erzeugt dieselbe Vorlage ohne
Bewertungsseiten.

## Von Hand statt im Flow

Jeder Baustein läuft auch einzeln im Chat: Agent öffnen, „Lauf-Ordner: …“
schreiben, Ergebnisdateien im Ordner ansehen. So lässt sich jeder Baustein
testen, bevor er in den Flow kommt.

## Vor dem Bau zu klären

| Nr. | Frage | Falls nein |
|---|---|---|
| T1 | Führt ein Agent (Copilot-Harness) das Python-Startskript aus seinem Skill in der Sandbox aus? | Werkzeug-Bausteine rufen dasselbe Startskript über einen Connector auf; Ein- und Ausgänge bleiben gleich |
| T2 | Hat die Sandbox Internetzugang (Quellen-Cache in W1)? | W1 lässt den Abruf aus; A07/A08 öffnen Quellen selbst; `review-work.py` muss ohne gespeicherte Originale laufen |
| T3 | Können Agenten Dateien im SharePoint-Lauf-Ordner lesen und schreiben? | Dateien als Anhang übergeben und als erzeugte Dateien zurückgeben |
| T4 | Wartet „Agent aufrufen“ im Flow auch bei mehreren Minuten Laufzeit? | Bausteine einzeln von Hand starten |
| T5 | Startet jeder Agentenaufruf ohne Verlauf? | Agent je Aufruf neu anlegen oder Verlauf ausdrücklich abschalten |
| T6 | Laufen parallele Zweige mit Agentenaufrufen? | nacheinander, dauert länger |
| T7 | Höchstzahl für Schleifen im Flow? | Rückläufe zählen und bei Bedarf manuell fortsetzen |
| T8 | Sind Claude Opus 5.5 und Sonnet 5.5 produktiv freigegeben? | Ersatzmodell je Baustein festlegen |
| T9 | Grenzen für Skill-Pakete (Dateien, Größe)? | Pakete aufteilen |
| T10 | Kosten eines Laufs in Copilot Credits? | Kurzbriefing als Standard |
