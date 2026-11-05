---
name: werkzeug-bewertungskontext
description: Erzeugt für einen Firmenbriefing-Lauf den Kontext der Positionierung bzw. der SWOT aus den freigegebenen Fakten und prüft die Positionierung formal. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Bewertungskontext

Parameter: `schritt`: `positioning` vor A09, `swot` nach A09.

## So arbeitest du

1. **Lauf-Ordner aus SharePoint laden.** Ordner-ID mit „Get folder metadata
   using path“ holen, mit „List folder“ alle Dateien und Unterordner auflisten
   (auch `_pruefstand/` und tiefer) und jede Datei mit „Get file content using
   path“ in einen lokalen Ordner der Sandbox laden, mit gleicher Struktur.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w4_bewertungskontext.py --lauf <Lauf-Ordner> --schritt <positioning|swot>
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
| positioning | `facts-run.json`, `review-packet.json`, `review-basis.md` (freigegeben), `comparison-plan.json`, `market-facts.json`, `portfolio-facts.json` |
| swot | zusätzlich `positioning.json`, `positioning-context.json` |

## Ausgänge

| Phase | Dateien im Lauf-Ordner |
|---|---|
| positioning | `positioning-context.json`, `pruefergebnis.json` |
| swot | `positioning.json` mit Kopf und Prüfsummen, `swot-context.json`, `pruefergebnis.json`, `_pruefstand/` |

## Was das Skript tut

- **positioning:** nimmt alle A-geprüften Fakten der vier Kernmodule und
  erzeugt den Positionierungskontext mit Produktinventar, Modul-Insights und,
  falls vorhanden, regionaler Präsenz (`check-interpretation.py --prepare`).
- **swot:** vervollständigt `positioning.json`, prüft sie formal, meldet
  blockierende Rückfragen an die Faktenbausteine und erzeugt den SWOT-Kontext
  aus allen bewerteten Positionierungsaussagen. Unbewertete Matrixzellen,
  Produkte und Regionen sind keine SWOT-Grundlage.

Das Skript nutzt die vorhandenen Skripte unter `scripts/` in diesem Skill-Paket
unverändert. Es arbeitet intern unter einem festen Arbeitspfad, weil die
Prüfskripte Pfade in ihre Prüfsummen aufnehmen; so passt jeder Schritt zum
vorherigen, auch wenn der Lauf-Ordner in jeder Sandbox woanders liegt.
