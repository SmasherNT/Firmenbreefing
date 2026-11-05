---
name: werkzeug-freigabe
description: Führt Leitentscheid und Befunde eines Firmenbriefing-Laufs zusammen, wendet die Freigaberegeln an und schreibt Review und Prüfergebnis. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Freigabe

Parameter: `phase`: wie beim vorangegangenen W1.

## So arbeitest du

1. **Lauf-Ordner lokal bereitstellen.** Liegt der Lauf-Ordner in SharePoint,
   lade alle seine Dateien einschließlich des Unterordners `_pruefstand/` in
   einen lokalen Ordner der Sandbox. Liegt er schon lokal, nutze ihn direkt.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w3_freigabe.py --lauf <Lauf-Ordner> --phase <basis|final>
   ```

3. **Ergebnis zurückschreiben.** Alle neuen und geänderten Dateien
   (einschließlich `_pruefstand/`) zurück in den Lauf-Ordner schreiben. Dateien,
   die das Skript gelöscht hat, dort ebenfalls löschen.
4. **Antworten** mit der letzten Ausgabe des Skripts in einem Satz.

Du änderst keine Inhalte, bewertest nichts und rufst keine anderen Befehle auf.
Bricht das Skript ab, gibst du die Fehlermeldung wörtlich zurück.

## Eingänge

| Phase | Dateien im Lauf-Ordner |
|---|---|
| beide | `leitentscheid.json`, `befund-<n>.json`, `review-packet.json`, `_pruefstand/` |

## Ausgänge

| Phase | Dateien im Lauf-Ordner |
|---|---|
| basis | `review-basis.md`, `pruefergebnis.json` (Prüftor 1), `_pruefstand/` |
| final | `review-final.md`, `pruefergebnis.json` (Prüftor 2), `_pruefstand/` |

## Was das Skript tut

- ergänzt im Leitentscheid Kopf und aktuelle Prüfsummen,
- führt Leitentscheid und Befunde zusammen (`review-shards.py merge`) und
- wendet die Freigaberegeln an (`stamp-review.py`).
- `bestanden: true` nur bei Status `freigegeben` ohne offene Punkte. Sonst
  `rueckgabe` je zuständigem Baustein aus den Korrektur- und offen-Befunden,
  den `material_errors` und den Fehlern der Skripte. Ein abgelehnter Stempel
  wird nie als Freigabe gemeldet.

Das Skript nutzt die vorhandenen Skripte unter `scripts/` in diesem Skill-Paket
unverändert. Es arbeitet intern unter einem festen Arbeitspfad, weil die
Prüfskripte Pfade in ihre Prüfsummen aufnehmen; so passt jeder Schritt zum
vorherigen, auch wenn der Lauf-Ordner in jeder Sandbox woanders liegt.
