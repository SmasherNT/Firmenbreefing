---
name: werkzeug-pruefpaket
description: Prüft die Ergebnisse eines Firmenbriefing-Laufs formal, baut das Prüfpaket und verteilt die Quellen auf bis zu drei Prüfjobs. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Prüfpaket

Parameter: `phase`: `basis` nach den Faktenbausteinen, `final` nach der SWOT.

## So arbeitest du

1. **Lauf-Ordner aus SharePoint laden.** Ordner-ID mit „Get folder metadata
   using path“ holen, mit „List folder“ alle Dateien und Unterordner auflisten
   (auch `_pruefstand/` und tiefer) und jede Datei mit „Get file content using
   path“ in einen lokalen Ordner der Sandbox laden, mit gleicher Struktur.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w1_pruefpaket.py --lauf <Lauf-Ordner> --phase <basis|final>
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
| basis | `facts-run.json`, `comparison-plan.json` (falls vorhanden), alle `*-facts.json` |
| final | zusätzlich `review-packet.json`, `review-basis.md`, `positioning.json`, `positioning-context.json`, `swot.json`, `swot-context.json`, `_pruefstand/` |

## Ausgänge

| Phase | Dateien im Lauf-Ordner |
|---|---|
| beide | `pruefergebnis.json` (Prüftor), `pruefjob-<n>.json` je Prüfjob, `_pruefstand/` |
| basis | zusätzlich `review-packet.json`; die `*-facts.json` mit einheitlichem Kopf und endgültigen Quellen-IDs |
| final | zusätzlich `swot.json` mit Kopf und Prüfsummen |

## Was das Skript tut

- **basis:** ergänzt in allen Faktenmodulen den Kopf aus `facts-run.json`,
  berechnet die Quellen-IDs (`S-…`) aus den URLs und passt alle Verweise an,
  lädt die Originale in den Quellen-Cache, prüft alle Module formal
  (`prepare-facts.py`), baut den Prüfauftrag (`review-work.py`) und verteilt die
  Quellen auf bis zu drei Prüfjobs (`review-shards.py`).
- **final:** vervollständigt `swot.json`, prüft Positionierung und SWOT formal
  (`check-interpretation.py`) und baut den Prüfauftrag für die Schlussprüfung.
- Formatfehler landen in `pruefergebnis.json` mit `bestanden: false` und einer
  `rueckgabe` an den zuständigen Baustein. `jobs` nennt die Zahl der Prüfjobs.

Das Skript nutzt die vorhandenen Skripte unter `scripts/` in diesem Skill-Paket
unverändert. Es arbeitet intern unter einem festen Arbeitspfad, weil die
Prüfskripte Pfade in ihre Prüfsummen aufnehmen; so passt jeder Schritt zum
vorherigen, auch wenn der Lauf-Ordner in jeder Sandbox woanders liegt.
