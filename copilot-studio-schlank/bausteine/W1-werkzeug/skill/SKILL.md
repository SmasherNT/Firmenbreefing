---
name: schlank-werkzeug
description: Prüft in einem Firmenbriefing-Lauf die Formate, baut Prüfpaket und Bewertungskontexte, vermerkt die fehlende unabhängige Prüfung und rendert die HTML als ungeprüften Entwurf. Führt nur das Startskript des Skills aus.
---

# Werkzeug (schlanke Variante)

Parameter `schritt`: `fakten`, `swot` oder `abschluss`.

## So arbeitest du

1. **Lauf-Ordner lokal bereitstellen.** Liegt der Lauf-Ordner in SharePoint,
   lade alle seine Dateien einschließlich des Unterordners `_pruefstand/` in
   einen lokalen Ordner der Sandbox. Liegt er schon lokal, nutze ihn direkt.
2. **Genau diesen einen Befehl ausführen** (aus dem Wurzelordner dieses Skills):

   ```bash
   python3 werkzeug.py --lauf <Lauf-Ordner> --schritt <fakten|swot|abschluss>
   ```

3. **Ergebnis zurückschreiben.** Alle neuen und geänderten Dateien
   (einschließlich `_pruefstand/`) zurück in den Lauf-Ordner schreiben.
4. **Antworten** mit der letzten Ausgabe des Skripts in einem Satz.

Du änderst keine Inhalte, bewertest nichts und rufst keine anderen Befehle auf.
Bricht das Skript ab, gibst du die Fehlermeldung wörtlich zurück.

## Schritte

| schritt | liest | schreibt |
|---|---|---|
| `fakten` | `facts-run.json`, `comparison-plan.json` (Voll), alle `*-facts.json` | `review-packet.json`, `review-basis.md`, `positioning-context.json` (nur Voll), `pruefergebnis.json`, die `*-facts.json` vereinheitlicht, `_pruefstand/` |
| `swot` | `positioning.json`, `positioning-context.json`, `review-packet.json`, `review-basis.md`, `comparison-plan.json` | `swot-context.json`, `positioning.json` ergänzt, `pruefergebnis.json`, `_pruefstand/` |
| `abschluss` | Kurz: `facts-run.json`, `review-packet.json`, `review-basis.md`; Voll zusätzlich `positioning*.json`, `swot.json`, `swot-context.json`, `comparison-plan.json` | `briefing.html`, `review-final.md` (Voll), `pruefergebnis.json`, `_pruefstand/` |

## Was das Skript tut

- **fakten:** ergänzt in allen Faktenmodulen den Kopf, berechnet die
  Quellen-IDs aus den URLs, prüft alle Module formal (`prepare-facts.py`), baut
  das Prüfpaket und schreibt `review-basis.md` mit dem Vermerk „ohne
  unabhängige Quellenprüfung übernommen“. Im Vollbriefing erzeugt es danach den
  Positionierungskontext (`check-interpretation.py --prepare`).
- **swot:** vervollständigt und prüft `positioning.json` formal, meldet
  blockierende Rückfragen an die Recherche und erzeugt den SWOT-Kontext.
- **abschluss:** prüft im Vollbriefing Positionierung und SWOT formal, schreibt
  `review-final.md` mit demselben Vermerk und rendert die HTML mit der
  bestehenden Vorlage (`render-briefing.py`). Die HTML wird sichtbar als
  **ungeprüfter Entwurf** gekennzeichnet: Hinweis oben, Kennzeichen im Kopf,
  „nicht unabhängig geprüft“ im Quellenverzeichnis.

`pruefergebnis.json` meldet nur **Formatfehler** und Rückfragen, keine
inhaltliche Prüfung. Bei `bestanden: false` nennt `rueckgabe` das zuständige
Modul (`context`, `portfolio`, `cluster`, `market`, `focus:<id>`,
`positioning`, `swot` oder `auftrag`).

Das Skript arbeitet intern unter einem festen Arbeitspfad, damit die
Prüfsummen von Aufruf zu Aufruf gültig bleiben.
