---
name: werkzeug-befunde
description: Vervollständigt die Befunde der Dokumentprüfung eines Firmenbriefing-Laufs und erzeugt die Eingabe der Leitprüfung. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Befunde bündeln

Parameter: `phase`: wie beim vorangegangenen W1.

## So arbeitest du

1. **Lauf-Ordner aus SharePoint laden.** Ordner-ID mit „Get folder metadata
   using path“ holen, mit „List folder“ alle Dateien und Unterordner auflisten
   (auch `_pruefstand/` und tiefer) und jede Datei mit „Get file content using
   path“ in einen lokalen Ordner der Sandbox laden, mit gleicher Struktur.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w2_befunde.py --lauf <Lauf-Ordner> --phase <basis|final>
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
| beide | `befund-<n>.json` je Prüfjob, `review-packet.json`, `auftrag.md`, `_pruefstand/` |
| final | zusätzlich `positioning.json`, `positioning-context.json`, `swot.json`, `swot-context.json` |

## Ausgänge

| Phase | Dateien im Lauf-Ordner |
|---|---|
| beide | `leitpruefung-eingabe.json`, `befund-<n>.json` mit Kopf und Prüfsummen, `_pruefstand/` |

## Was das Skript tut

- ergänzt in jedem Befund Format-Kennung, Kopf und Prüfsummen,
- sammelt die Befunde ein (`review-shards.py collect`) und
- stellt `leitpruefung-eingabe.json` zusammen: Phase, Auftrag, Prüfauftrag,
  gebündelte Befunde, Aussagen, Quellen, Darstellungszuordnungen, Netzwerk; in
  final zusätzlich Positionierung, SWOT und ihre Kontexte.
- Fehlt ein Befund, schreibt das Skript nichts und nennt die fehlende Datei.

Das Skript nutzt die vorhandenen Skripte unter `scripts/` in diesem Skill-Paket
unverändert. Es arbeitet intern unter einem festen Arbeitspfad, weil die
Prüfskripte Pfade in ihre Prüfsummen aufnehmen; so passt jeder Schritt zum
vorherigen, auch wenn der Lauf-Ordner in jeder Sandbox woanders liegt.
