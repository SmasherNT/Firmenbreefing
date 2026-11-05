---
name: werkzeug-befunde
description: Vervollständigt die Befunde der Dokumentprüfung eines Firmenbriefing-Laufs und erzeugt die Eingabe der Leitprüfung. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Befunde bündeln

Parameter: `phase`: wie beim vorangegangenen W1.

## So arbeitest du

1. **Lauf-Ordner lokal bereitstellen.** Liegt der Lauf-Ordner in SharePoint,
   lade alle seine Dateien einschließlich des Unterordners `_pruefstand/` in
   einen lokalen Ordner der Sandbox. Liegt er schon lokal, nutze ihn direkt.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w2_befunde.py --lauf <Lauf-Ordner> --phase <basis|final>
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
