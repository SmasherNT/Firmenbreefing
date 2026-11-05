---
name: werkzeug-freigabe
description: Führt Leitentscheid und Befunde eines Firmenbriefing-Laufs zusammen, wendet die Freigaberegeln an und schreibt Review und Prüfergebnis. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Freigabe

Parameter: `phase`: wie beim vorangegangenen W1.

## So arbeitest du

1. **Lauf-Ordner aus SharePoint laden.** Ordner-ID mit „Get folder metadata
   using path“ holen, mit „List folder“ alle Dateien und Unterordner auflisten
   (auch `_pruefstand/` und tiefer) und jede Datei mit „Get file content using
   path“ in einen lokalen Ordner der Sandbox laden, mit gleicher Struktur.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w3_freigabe.py --lauf <Lauf-Ordner> --phase <basis|final>
   ```

3. **Ergebnis nach SharePoint zurückschreiben.** Die letzte Zeile der Ausgabe
   beginnt mit `DATEIEN` und nennt `geaendert` und `geloescht` (Pfade relativ
   zum Lauf-Ordner). Jede Datei aus `geaendert` mit „Create file“ schreiben;
   existiert sie schon, ihre ID mit „Get file metadata using path“ holen und mit
   „Update file“ überschreiben. Jede Datei aus `geloescht` mit „Delete file“
   entfernen.
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
