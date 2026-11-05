---
name: werkzeug-pruefpaket
description: Prüft die Ergebnisse eines Firmenbriefing-Laufs formal, baut das Prüfpaket und verteilt die Quellen auf bis zu drei Prüfjobs. Führt nur Skripte aus.
---

# Werkzeug: Prüfpaket

Führe nur die Befehle unten aus. Ändere keine Inhalte und bewerte nichts.
`L` ist der übergebene Lauf-Ordner, `P` ist `L/_pruefstand`. Die Skripte liegen
im Skill-Paket unter `scripts/`.

Bricht ein Befehl mit Fehlern ab: `scripts/anpassen.py pruefergebnis` mit der
Fehlerausgabe aufrufen (Schritt „Fehler melden“) und aufhören.

## Phase basis

1. Kopf und Quellen-IDs vereinheitlichen:
   `python3 scripts/anpassen.py module --lauf L`
   (ergänzt Kopffelder aus `facts-run.json`, berechnet `S-…`-IDs aus den URLs,
   passt alle Verweise an, meldet Formatfehler je Modul).
2. Quellen-Cache anlegen und Originale laden:
   `python3 scripts/source-cache.py --manifest L/facts-run.json --cache P/document-cache init`,
   danach für jede URL aus den `source_proposals`:
   `python3 scripts/source-cache.py --manifest L/facts-run.json --cache P/document-cache fetch --url <URL>`
   Nicht erreichbare Quellen nur notieren, nicht abbrechen.
3. Formale Gesamtprüfung und Prüfpaket:
   `python3 scripts/prepare-facts.py --manifest L/facts-run.json --modules <alle L/*-facts.json> [--plan L/comparison-plan.json] --out P`
   Danach `P/review-packet.json` nach `L/review-packet.json` kopieren.
4. Prüfauftrag:
   `python3 scripts/review-work.py prepare --manifest L/facts-run.json --facts L/review-packet.json --validation P/facts-validation.json --cache P/document-cache --out P/review-work-basis.json`
5. Quellen verteilen:
   `python3 scripts/review-shards.py split --work P/review-work-basis.json --facts L/review-packet.json --workers 3 --out P/review-split-basis.json`
6. Je Job `sources-<n>`:
   `python3 scripts/review-shards.py show --plan P/review-split-basis.json --work P/review-work-basis.json --facts L/review-packet.json --job sources-<n>`
   Ausgabe unverändert als `L/pruefjob-<n>.json` speichern. Alte `pruefjob-*.json`
   und `befund-*.json` vorher löschen.
7. Ergebnis: `python3 scripts/anpassen.py pruefergebnis --lauf L --schritt pruefpaket --phase basis`

## Phase final

1. SWOT vervollständigen: `python3 scripts/anpassen.py bewertung --lauf L --rolle swot`
2. Bewertungen prüfen:
   `python3 scripts/check-interpretation.py --manifest L/facts-run.json --facts L/review-packet.json --review L/review-basis.md --context L/positioning-context.json --output L/positioning.json --plan L/comparison-plan.json --out P/positioning-validation.json`
   `python3 scripts/check-interpretation.py --manifest L/facts-run.json --facts L/review-packet.json --review L/review-basis.md --context L/swot-context.json --output L/swot.json --positioning L/positioning.json --positioning-context L/positioning-context.json --plan L/comparison-plan.json --out P/swot-validation.json`
   `python3 scripts/check-interpretation.py --merge-validation P/positioning-validation.json P/swot-validation.json --out P/interpretation-validation.json`
3. Prüfauftrag:
   `python3 scripts/review-work.py prepare --manifest L/facts-run.json --facts L/review-packet.json --validation P/interpretation-validation.json --cache P/document-cache --basis-review L/review-basis.md --basis-work P/review-work-basis.json --positioning L/positioning.json --positioning-context L/positioning-context.json --swot L/swot.json --swot-context L/swot-context.json --plan L/comparison-plan.json --out P/review-work-final.json`
4. Schritte 5 und 6 wie in basis, mit `final` statt `basis` in den Dateinamen.
   Oft gibt es in final keinen Job.
5. Ergebnis: `python3 scripts/anpassen.py pruefergebnis --lauf L --schritt pruefpaket --phase final`

## Fehler melden

`python3 scripts/anpassen.py pruefergebnis --lauf L --schritt pruefpaket --phase <phase> --fehler <Fehlerausgabe>`

Schreibt `L/pruefergebnis.json` mit `bestanden: false` und den Fehlern je
zuständigem Baustein (`owner`).
