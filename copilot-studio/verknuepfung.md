# Bausteine verknüpfen

Die Bausteine kennen sich nicht. Du legst fest, wer wann läuft. Jeder Baustein
bekommt nur den Pfad des Lauf-Ordners (und ggf. einen Parameter), liest seine
Eingangsdateien und schreibt seine Ausgangsdateien. Passen die Dateinamen,
passen die Bausteine zusammen.

## Lauf-Ordner anlegen

1. In SharePoint einen Ordner je Lauf anlegen, z. B. `Briefings/<firma>-<datum>/`.
2. Darin `anfrage.txt` mit der Nachricht ablegen. Erste Zeile optional
   `modus: voll` oder `modus: kurz`.

Alle weiteren Dateien entstehen durch die Bausteine. Welche das sind, steht in
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
| `positioning` | A09 | W4 swot |
| `swot` | A10 | W1 final |

## Rezept Vollbriefing

| # | Baustein | Parameter | Ergebnis |
|---|---|---|---|
| 1 | A01 Auftrag | – | `auftrag.md`, `facts-run.json`, `comparison-plan.json` |
| 2 | A02, A03, A04, A05 (parallel, falls möglich) | – | vier `*-facts.json` |
| 3 | A06 je Eintrag in `facts-run.json → focus_pages` | `focus_id` | `focus-<id>-facts.json` |
| 4 | W1 Prüfpaket | `phase: basis` | Prüftor; `pruefjob-<n>.json` |
| 5 | A07 je Job (Anzahl in `pruefergebnis.json → jobs`) | `job: <n>` | `befund-<n>.json` |
| 6 | W2 Befunde bündeln | `phase: basis` | `leitpruefung-eingabe.json` |
| 7 | A08 Leitprüfung | – | `leitentscheid.json` |
| 8 | W3 Freigabe | `phase: basis` | **Prüftor 1**; `review-basis.md` |
| 9 | W4 Bewertungskontext | `schritt: positioning` | `positioning-context.json` |
| 10 | A09 Positionierung | – | `positioning.json` |
| 11 | W4 Bewertungskontext | `schritt: swot` | Prüftor; `swot-context.json` |
| 12 | A10 SWOT | – | `swot.json` |
| 13 | W1 Prüfpaket | `phase: final` | Prüftor; ggf. `pruefjob-<n>.json` |
| 14 | A07 je Job, falls Jobs | `job: <n>` | `befund-<n>.json` |
| 15 | W2 Befunde bündeln | `phase: final` | `leitpruefung-eingabe.json` |
| 16 | A08 Leitprüfung | – | `leitentscheid.json` |
| 17 | W3 Freigabe | `phase: final` | **Prüftor 2**; `review-final.md` |
| 18 | W5 Briefing rendern | – | `briefing.html` |

Danach im Flow: Link zu `briefing.html` per Teams oder E-Mail verschicken.

## Rezept Kurzbriefing

`anfrage.txt` mit `modus: kurz`. Dann die Schritte 1, 2 (nur A02 und A03),
4 bis 8 und 18. A01 schreibt keinen Vergleichsplan, W5 erzeugt dieselbe Vorlage
ohne Bewertungsseiten.

## Von Hand statt im Flow

Jeder Baustein läuft auch einzeln im Chat: Agent öffnen, „Lauf-Ordner: …“
schreiben, Ergebnisdateien im Ordner ansehen. So lässt sich jeder Baustein
testen, bevor er in den Flow kommt.

## Vor dem Bau zu klären

| Nr. | Frage | Falls nein |
|---|---|---|
| T1 | Führt ein Agent (Copilot-Harness) die Python-Skripte aus seinem Skill in der Sandbox aus? | Werkzeug-Bausteine rufen dieselben Skripte über einen Connector auf; Ein- und Ausgänge bleiben gleich |
| T2 | Hat die Sandbox Internetzugang (Quellen-Cache in W1)? | W1 lässt den Abruf aus; A07/A08 öffnen Quellen selbst; `review-work.py` muss ohne gespeicherte Originale laufen |
| T3 | Können Agenten Dateien im SharePoint-Lauf-Ordner lesen und schreiben? | Dateien als Anhang übergeben und als erzeugte Dateien zurückgeben |
| T4 | Wartet „Agent aufrufen“ im Flow auch bei mehreren Minuten Laufzeit? | Bausteine einzeln von Hand starten |
| T5 | Startet jeder Agentenaufruf ohne Verlauf? | Agent je Aufruf neu anlegen oder Verlauf ausdrücklich abschalten |
| T6 | Laufen parallele Zweige mit Agentenaufrufen? | nacheinander, dauert länger |
| T7 | Höchstzahl für Schleifen im Flow? | Rückläufe zählen und bei Bedarf manuell fortsetzen |
| T8 | Sind Claude Opus 5.5 und Sonnet 5.5 produktiv freigegeben? | Ersatzmodell je Baustein festlegen |
| T9 | Grenzen für Skill-Pakete (Dateien, Größe)? | Pakete aufteilen |
| T10 | Kosten eines Laufs in Copilot Credits? | Kurzbriefing als Standard |
