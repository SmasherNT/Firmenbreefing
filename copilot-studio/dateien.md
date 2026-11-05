# Dateien im Lauf-Ordner

Ein Lauf-Ordner je Briefing. Jeder Baustein liest und schreibt nur die Dateien
in seiner Zeile. Die Formate sind die heutigen JSON-Formate des Repositorys.
Deshalb funktionieren Prüfskripte und Renderer unverändert.

## Warum JSON statt Fließtext

Fließtext verliert Aussage-IDs, Quellen-URLs, Belegstellen und den Prüfstatus.
Ohne diese Felder können die Skripte nichts prüfen, und der Renderer erzeugt
keine klickbaren Belege. Lesbar für Menschen ist das Ergebnis `briefing.html`.

## Übersicht

| Datei | Schreibt | Liest |
|---|---|---|
| `anfrage.txt` | du (bzw. der Flow) | A01 |
| `auftrag.md` | A01 | A02–A06 |
| `facts-run.json` | A01 | alle |
| `comparison-plan.json` | A01 (nur Voll) | A05, W1, W4, W5 |
| `context-facts.json` | A02 (W1 vereinheitlicht Kopf und Quellen-IDs) | W1 |
| `portfolio-facts.json` | A03 (dito) | W1 |
| `cluster-facts.json` | A04 (dito) | W1 |
| `market-facts.json` | A05 (dito) | W1, W4 |
| `focus-<id>-facts.json` | A06, je Fokusthema (dito) | W1 |
| `review-packet.json` | W1 | W2, W3, W4, W5 |
| `pruefjob-<n>.json` | W1, bis zu 3 | A07 |
| `befund-<n>.json` | A07 (W2 ergänzt Kopf und Prüfsummen) | W2, W3 |
| `leitpruefung-eingabe.json` | W2 | A08 |
| `leitentscheid.json` | A08 | W3 |
| `review-basis.md` | W3 (Phase basis) | W1 final, W4, W5 |
| `positioning-context.json` | W4 | A09, W1 final, W5 |
| `positioning.json` | A09 (W4 ergänzt Prüfsummen) | W4, W1 final, W5 |
| `swot-context.json` | W4 | A10, W1 final, W5 |
| `swot.json` | A10 (W1 final ergänzt Prüfsummen) | W1 final, W5 |
| `review-final.md` | W3 (Phase final) | W5 |
| `pruefergebnis.json` | W1, W3, W4 | du (Prüftor) und der Baustein mit Rückgabe |
| `briefing.html` | W5 | Nutzer |
| `_pruefstand/` | W1–W4 | nur W1–W5 |

## pruefergebnis.json

```json
{
  "schritt": "pruefpaket | freigabe | bewertungskontext",
  "phase": "basis | final",
  "bestanden": true,
  "jobs": 2,
  "rueckgabe": {
    "<owner>": [{"ids": ["…"], "reason": "…", "action": "…", "frage": "…"}]
  },
  "fehler": []
}
```

`frage` steht nur bei Rückfragen aus Positionierung oder SWOT an die
Faktenbausteine.

## _pruefstand/

Zwischenstände der Skripte: Quellen-Cache, `facts-validation.json`,
`sources.json`, `review-work-*.json`, `review-split-*.json`,
`source-findings-*.json`, `leitentscheid-*.json`, `review-merged-*.json`,
Validierungen. Kein Denk-Agent liest oder schreibt hier.

## Rückgabe bei „nicht bestanden“

Der zuständige Baustein liest `pruefergebnis.json` und seine eigene bisherige
Datei, korrigiert genau die genannten Punkte und schreibt seine Datei neu. Alles
andere bleibt unverändert, und nur das Geänderte wird erneut geprüft.

## Wo Token gespart werden

- Kein Chatverlauf: jeder Aufruf beginnt leer.
- Jeder Baustein hat nur seinen eigenen Skill und seine eigenen Regeln.
- Dokumentprüfer sehen nur ihr Quellenbündel.
- Positionierung und SWOT sehen nur ihren Bewertungskontext.
- Bei Korrekturen läuft nur der betroffene Baustein erneut.
- Die Werkzeug-Bausteine denken nicht; sie rufen nur Skripte auf.
