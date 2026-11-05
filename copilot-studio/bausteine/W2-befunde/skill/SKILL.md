---
name: werkzeug-befunde
description: Sammelt die Befunde der Dokumentprüfung eines Firmenbriefing-Laufs ein und erzeugt die Eingabe der Leitprüfung. Führt nur Skripte aus.
---

# Werkzeug: Befunde bündeln

Führe nur die Befehle unten aus. Ändere keine Inhalte und bewerte nichts.
`L` ist der übergebene Lauf-Ordner, `P` ist `L/_pruefstand`, `<phase>` ist
`basis` oder `final`.

1. Befunde vervollständigen (Format-Kennung, Prüfsummen aus dem Prüfstand):
   `python3 scripts/anpassen.py befunde --lauf L --phase <phase>`
2. Befunde einsammeln:
   `python3 scripts/review-shards.py collect --plan P/review-split-<phase>.json --work P/review-work-<phase>.json --facts L/review-packet.json --parts <alle L/befund-*.json> --out P/source-findings-<phase>.json`
   Gibt es keine Jobs, `--parts` ohne Dateien aufrufen.
3. Eingabe der Leitprüfung zusammenstellen:
   `python3 scripts/anpassen.py leitpruefung-eingabe --lauf L --phase <phase>`
   Schreibt `L/leitpruefung-eingabe.json` mit Phase, gebündelten Befunden,
   Prüfauftrag (`review-work.py show`), Aussagen, Quellen, Darstellungszuordnungen
   und in final zusätzlich Positionierung, SWOT und Kontexten.

Bei einem Fehler: die Fehlermeldung wörtlich zurückgeben und keine Datei schreiben.
