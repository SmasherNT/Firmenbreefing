---
name: werkzeug-rendern
description: Erzeugt aus den freigegebenen Dateien eines Firmenbriefing-Laufs die HTML mit der bestehenden Vorlage. Führt nur das Startskript des Skills aus.
---

# Werkzeug: Briefing rendern

Parameter: keiner; Voll- oder Kurzbriefing ergibt sich aus `facts-run.json`.

## So arbeitest du

1. **Lauf-Ordner lokal bereitstellen.** Liegt der Lauf-Ordner in SharePoint,
   lade alle seine Dateien einschließlich des Unterordners `_pruefstand/` in
   einen lokalen Ordner der Sandbox. Liegt er schon lokal, nutze ihn direkt.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 w5_rendern.py --lauf <Lauf-Ordner>
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
| Kurz | `facts-run.json`, `review-packet.json`, `review-basis.md` |
| Voll | zusätzlich `positioning.json`, `positioning-context.json`, `swot.json`, `swot-context.json`, `review-final.md`, `comparison-plan.json` |

## Ausgänge

| Phase | Dateien im Lauf-Ordner |
|---|---|
| beide | `briefing.html` |

## Was das Skript tut

- ruft `render-briefing.py` mit der bestehenden HTML-Vorlage auf; im
  Vollbriefing mit allen Bewertungsseiten (`--full`).
- Der Renderer prüft selbst, dass alle Freigaben aktuell sind. Fehlt eine,
  entsteht keine HTML, und das Skript nennt den Grund.

Das Skript nutzt die vorhandenen Skripte unter `scripts/` in diesem Skill-Paket
unverändert. Es arbeitet intern unter einem festen Arbeitspfad, weil die
Prüfskripte Pfade in ihre Prüfsummen aufnehmen; so passt jeder Schritt zum
vorherigen, auch wenn der Lauf-Ordner in jeder Sandbox woanders liegt.
