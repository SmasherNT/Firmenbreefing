---
name: werkzeug-freigabe
description: Führt Leitentscheid und Befunde eines Firmenbriefing-Laufs zusammen, wendet die Freigaberegeln an und schreibt Review und Prüfergebnis. Führt nur Skripte aus.
---

# Werkzeug: Freigabe

Führe nur die Befehle unten aus. Ändere keine Inhalte und bewerte nichts.
`L` ist der übergebene Lauf-Ordner, `P` ist `L/_pruefstand`, `<phase>` ist
`basis` oder `final`. `<validierung>` ist in basis `P/facts-validation.json`,
in final `P/interpretation-validation.json`.

1. Leitentscheid vervollständigen (Identität und aktuelle Prüfsummen):
   `python3 scripts/anpassen.py leitentscheid --lauf L --phase <phase>`
   Schreibt `P/leitentscheid-<phase>.json`.
2. Zusammenführen:
   `python3 scripts/review-shards.py merge --plan P/review-split-<phase>.json --work P/review-work-<phase>.json --facts L/review-packet.json --parts <alle L/befund-*.json> --lead P/leitentscheid-<phase>.json --validation <validierung> --out P/review-merged-<phase>.json`
3. Freigaberegeln anwenden und stempeln:
   `python3 scripts/stamp-review.py --draft P/review-merged-<phase>.json --validation <validierung> --work P/review-work-<phase>.json --out L/review-<phase>.md`
   (in basis entsteht `L/review-basis.md`, in final `L/review-final.md`)
4. Prüfergebnis schreiben:
   `python3 scripts/anpassen.py pruefergebnis --lauf L --schritt freigabe --phase <phase> [--fehler <Fehlerausgabe aus 2 oder 3>]`

`L/pruefergebnis.json` enthält `bestanden: true` nur, wenn Schritt 3 ohne Fehler
lief und der Status `freigegeben` ist. Sonst `bestanden: false` und eine
`rueckgabe` je zuständigem Baustein (`owner`) mit IDs, `reason` und `action`.
Ein abgelehnter Stempel wird nie als Freigabe gemeldet.
