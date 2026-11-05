---
name: werkzeug-bewertungskontext
description: Erzeugt für einen Firmenbriefing-Lauf den Kontext der Positionierung bzw. der SWOT aus den freigegebenen Fakten und prüft die Positionierung formal. Führt nur Skripte aus.
---

# Werkzeug: Bewertungskontext

Führe nur die Befehle unten aus. Ändere keine Inhalte und bewerte nichts.
`L` ist der übergebene Lauf-Ordner, `P` ist `L/_pruefstand`, `<schritt>` ist
`positioning` oder `swot`.

## Schritt positioning

1. Faktenauswahl: `python3 scripts/anpassen.py a-fakten --lauf L`
   liefert alle A-geprüften Fakten der vier Kernmodule (ohne Fokusseiten).
2. Kontext:
   `python3 scripts/check-interpretation.py --prepare --portfolio --module-insights --presence --manifest L/facts-run.json --facts L/review-packet.json --review L/review-basis.md --plan L/comparison-plan.json --market L/market-facts.json --claim-ids <IDs aus 1> --out L/positioning-context.json`
3. Ergebnis: `python3 scripts/anpassen.py pruefergebnis --lauf L --schritt bewertungskontext`

## Schritt swot

1. Positionierung vervollständigen: `python3 scripts/anpassen.py bewertung --lauf L --rolle positioning`
2. Positionierung prüfen:
   `python3 scripts/check-interpretation.py --manifest L/facts-run.json --facts L/review-packet.json --review L/review-basis.md --context L/positioning-context.json --output L/positioning.json --plan L/comparison-plan.json --out P/positioning-validation.json`
   Bei Fehlern: Prüfergebnis mit owner `positioning` melden (siehe unten) und aufhören.
3. Rückfragen: Enthält `positioning.json` blockierende `research_requests`,
   meldet `anpassen.py pruefergebnis` sie als Rückgabe an die Faktenbausteine.
4. Kontext:
   `python3 scripts/check-interpretation.py --prepare --manifest L/facts-run.json --facts L/review-packet.json --review L/review-basis.md --positioning L/positioning.json --positioning-context L/positioning-context.json --plan L/comparison-plan.json --interpretation-ids <alle I-IDs aus positioning.json> --out L/swot-context.json`
5. Ergebnis: `python3 scripts/anpassen.py pruefergebnis --lauf L --schritt bewertungskontext`

## Fehler melden

`python3 scripts/anpassen.py pruefergebnis --lauf L --schritt bewertungskontext --fehler <Fehlerausgabe>`
