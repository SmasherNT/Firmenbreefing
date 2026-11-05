# Übergabedokumente

Jeder Agent startet ohne Vorwissen. Er weiß nur, was in seinem Eingabedokument
steht. Deshalb ist für jeden Schritt festgelegt, welches Dokument er bekommt und
welches er liefert. Die Formate sind die heutigen JSON-Formate des Repos. So
greifen Prüfskripte und Renderer unverändert.

## Warum JSON statt Fließtext

Fließtext verliert Aussage-IDs, Quellen-URLs, Belegstellen und den Prüfstatus.
Ohne diese Felder können die Prüfskripte nichts kontrollieren, und der Renderer
erzeugt keine klickbaren Belege. Für Menschen lesbar bleibt alles über das ZIP
des Laufs und die fertige HTML.

## Dokumente je Lauf

| Datei im Lauf | Erstellt von | Gelesen von |
|---|---|---|
| `input/auftrag.md` | 01 Auftrag (über Werkstatt) | alle Faktenagenten, Leitprüfung |
| `input/facts-run.json` (Manifest) | 01 Auftrag, Kopf durch Werkstatt | alle Agenten (als Teil des Eingabedokuments), Werkstatt |
| `work/comparison-plan.json` | 01 Auftrag (nur Voll) | 05 Markt, 09 Positionierung |
| `work/context-facts.json` | 02 Kontext & Person | Werkstatt → Prüfpaket |
| `work/portfolio-facts.json` | 03 Portfolio & Präsenz | Werkstatt → Prüfpaket |
| `work/cluster-facts.json` | 04 Cluster & Netzwerk | Werkstatt → Prüfpaket |
| `work/market-facts.json` | 05 Markt & Wettbewerb | Werkstatt → Prüfpaket, Matrix |
| `work/focus-<id>-facts.json` | 06 Fokusthema, je Thema | Werkstatt → Prüfpaket |
| `work/document-cache/` | Werkstatt über „Quelle abrufen“ | alle Recherche- und Prüfagenten über das Tool |
| `work/review-packet.json`, `sources.json`, `facts-validation.json` | Werkstatt (`prepare-facts.py`) | Prüfung |
| Jobansicht je Dokumentprüfung | Werkstatt (`review-shards.py show`) | 07 Dokumentprüfung |
| Dokumentbefunde je Job | 07 Dokumentprüfung | Werkstatt → Leitprüfung |
| gebündelte Befunde | Werkstatt (`review-shards.py collect`) | 08 Leitprüfung |
| `work/review-basis.md` | Werkstatt aus 08 (`merge` + `stamp-review.py`) | Werkstatt → Bewertungskontext, Renderer |
| `work/positioning-context.json` | Werkstatt (`check-interpretation.py --prepare`) | 09 Positionierung |
| `work/positioning.json` | 09 Positionierung, Kopf durch Werkstatt | SWOT-Kontext, Schlussprüfung, Renderer |
| `work/swot-context.json` | Werkstatt | 10 SWOT |
| `work/swot.json` | 10 SWOT, Kopf durch Werkstatt | Schlussprüfung, Renderer |
| `work/review-final.md` | Werkstatt aus 08 (Schluss) | Renderer |
| `output/briefing.html` | Werkstatt (`render-briefing.py`) | Flow → SharePoint → Nutzer |

## Rückgabe bei „nicht bestanden“

Bei einem Rücklauf bekommt der zuständige Agent ein neues Eingabedokument mit
drei Teilen:

1. dem ursprünglichen Auftrag,
2. seinem eigenen bisherigen Ergebnis,
3. der `rueckgabe`: betroffene IDs mit `reason` und `action` aus der Prüfung.

Er korrigiert genau diese Punkte und liefert sein vollständiges Ergebnis neu.
Alles andere bleibt unverändert. Danach wird nur das Geänderte erneut geprüft.

## Wo Token gespart werden

- Kein Chatverlauf: Jeder Aufruf beginnt leer.
- Jeder Agent hat nur seine eigenen Regeln, nicht das ganze Regelwerk.
- Dokumentprüfer sehen nur ihr Quellenbündel.
- Positionierung und SWOT sehen nur den ausgewählten Bewertungskontext.
- Bei Korrekturen läuft nur der betroffene Agent erneut.
