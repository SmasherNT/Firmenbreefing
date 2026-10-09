---
name: company-briefing
description: Erstellt aus einer kurzen natürlichen Anfrage ein belegtes HTML-Firmenbriefing und steuert Auftrag, Agenten, Reviews und Ausgabe.
when_to_use: Bei jeder Anfrage nach einem Firmenbriefing, Unternehmensbriefing, Firmenprofil oder einer Gesprächsvorbereitung zu einem Unternehmen, auch ohne Slash-Befehl und ohne Formular, z. B. „Erstelle ein Briefing zu <Firma> mit Fokus <Themen>, Gesprächspartner <Name>, <Position>“ oder „Mach auch ein Briefing zu <Firma>“. Nicht bei Einrichtung oder Konfigurationsprüfung.
---

Bei ausdrücklich einzelnen Modulen oder Modultests stattdessen module-briefing
verwenden und references/modultest.md lesen; nicht diesen vollständigen Ablauf starten.

Der Hauptagent steuert den Ablauf. Einrichtung, Konfigurationsprüfung oder
Fragen zum System sind kein Auftrag: dann nichts recherchieren und
input/auftrag.md nicht anlegen.
Lies CLAUDE.md, references/defaults.md, references/briefing-struktur.md und
references/uebergabe.md; sie sind verbindlich.

## Ablauf (Reihenfolge einhalten)
1. Auftrag: Firma, Themen in Nutzerreihenfolge und Gesprächspartner/Position
   aus der aktuellen Nachricht übernehmen, übrige Werte aus defaults.md.
   Kein Formular, kein Slash-Befehl; nur bei blockierender Mehrdeutigkeit
   fragen. „auch“ setzt kein früheres Briefing voraus.
   Vorhandene input/auftrag.md, work/ und output/ nach defaults.md unter
   archive/<YYYYMMDD-HHMMSS>-<Firmenname>/ sichern, danach work/ und output/
   bis auf .gitkeep leeren. Stichtag mit `date +%F` ermitteln.
   input/auftrag.md nach defaults.md anlegen.
2. Portfolio und Struktur parallel delegieren: portfolio-analyst und
   cluster-analyst. Jede Delegation nennt Eingabedateien, Firma,
   Unternehmensgrenze, Stichtag, Nutzerthemen und Zielpfad.
3. Markt sowie Themen/Person: Hauptagent wendet briefing-context selbst an,
   nachdem work/portfolio.md und work/cluster.md vorliegen.
4. Basis-Review: source-reviewer mit Phase basis und den Dateien aus 2 und 3.
5. Korrekturen: wesentliche Fehler durch die zuständige Rolle beheben lassen
   (Analysten erneut delegieren, eigene Dateien selbst korrigieren), danach
   geänderte Claims erneut durch source-reviewer Phase basis prüfen lassen.
6. SWOT: swot-analyst erst, wenn review-basis keine offenen wesentlichen
   Fehler mehr meldet.
7. Schluss-Review: source-reviewer mit Phase final; Korrekturen wie in 5,
   abhängige Schlussfolgerungen erneut prüfen lassen.
8. Ausgabe: Hauptagent wendet briefing-output an.
Bleiben nach zwei Korrekturrunden wesentliche Fehler offen, keine finale
HTML erstellen; Status blockiert mit konkreten Punkten an den Nutzer melden.

## Zuständigkeiten (nur eigene Dateien schreiben)
| Datei | Rolle |
|---|---|
| archive/, input/auftrag.md | Hauptagent |
| work/portfolio.md | portfolio-analyst |
| work/cluster.md | cluster-analyst |
| work/markt.md, work/kontext.md | Hauptagent (briefing-context) |
| work/review-basis.md, work/review-final.md | source-reviewer |
| work/swot.md | swot-analyst |
| output/briefing.html, output/abnahme.md | Hauptagent (briefing-output) |
Die Methoden portfolio-analysis, cluster-analysis und swot-analysis führt
der Hauptagent nicht selbst aus, sondern delegiert an die Agenten.
Der Hauptagent ändert keine Analysten- oder Reviewdateien.
Tatsächlich aufgerufene Agenten, Phasen und Dateien für output/abnahme.md
protokollieren. Personenprofil nur, wenn ein Gesprächspartner genannt ist.

## Abschluss
Ergebnisse im Arbeitsbranch committen und pushen (Dateisicherung).
Keine öffentliche Veröffentlichung ohne ausdrücklichen Nutzerwunsch.
Dem Nutzer Pfade, Status, offene Lücken und Abnahmeergebnis nennen.
