---
name: werkzeug-rendern
description: Erzeugt aus den freigegebenen Dateien eines Firmenbriefing-Laufs die HTML mit der bestehenden Vorlage. Führt nur Skripte aus.
---

# Werkzeug: Briefing rendern

Führe nur die Befehle unten aus. Ändere keine Inhalte und bewerte nichts.
`L` ist der übergebene Lauf-Ordner.

**Vollbriefing** (vier Rollen in `facts-run.json`):

`python3 scripts/render-briefing.py --manifest L/facts-run.json --facts L/review-packet.json --basis-review L/review-basis.md --positioning L/positioning.json --positioning-context L/positioning-context.json --swot L/swot.json --swot-context L/swot-context.json --final-review L/review-final.md --plan L/comparison-plan.json --full --out L/briefing.html`

**Kurzbriefing** (Rollen context und portfolio):

`python3 scripts/render-briefing.py --manifest L/facts-run.json --facts L/review-packet.json --basis-review L/review-basis.md --out L/briefing.html`

Der Renderer prüft selbst, dass alle Freigaben aktuell sind. Meldet er einen
Fehler, die Meldung wörtlich zurückgeben und keine HTML schreiben.
