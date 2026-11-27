# Firmenbriefing mit drei Agenten in Copilot

| Agent | Aufgabe | Ergebnis |
|---|---|---|
| Firmenbriefing Recherche | recherchiert alle Fakten und Inhalte möglichst ausführlich, inklusive Summary, Reife, Präsenz, Positionierung und SWOT | briefing-daten.xlsx |
| Firmenbriefing Prüfung | prüft auf Wunsch gegen die Quellen, korrigiert belegte Abweichungen, vertieft Lücken und gewünschte Themen, passt Aussagen an | briefing-daten-geprueft.xlsx mit Änderungsprotokoll |
| Firmenbriefing HTML | erzeugt aus einer der beiden Excel-Dateien die HTML im festen Layout | briefing.html |

Die Agenten arbeiten unabhängig. Übergabe ist immer die Excel-Datei mit
lesbaren Blättern und dem vollständigen Datenstand. Die HTML entsteht nur durch
ein Skript mit fester Vorlage im Stil der Claude-Briefings: Reiter, Executive
Summary, Reifematrix, Unternehmensnetzwerk mit Tabellen- und Grafikansicht,
regionale Präsenz, Capability Matrix, Gesprächspartner- und Fokusseiten,
Quellenregister und nach einer Prüfung Prüfbericht mit Änderungsprotokoll.

Einrichtung Schritt für Schritt: ANLEITUNG.md. Grafik: architektur.png.

## Dateien

| Pfad | Inhalt |
|---|---|
| agenten/ | Instructions und Einstellungen je Agent |
| skills/ | Quellordner der neun Skills |
| skills/briefing-grundlagen/scripts/briefing.py | Zusammenführen, Validieren, Mindestregeln, Prüfung auswerten, Excel |
| skills/briefing-html/scripts/briefing_html.py | Seitenzusammenbau; nutzt die unveränderten Claude-Bausteine *-html.py und references/templates/ |
| machbarkeitstest/ | Test-Skill, Proben, Protokoll |
| beispiel/ | fiktive Beispieldaten in acht Teilen, inklusive Prüfung und Vertiefung |
| tests/ | automatische Tests |
| tools/build.py | synchronisiert die Skriptkopie, prüft Grenzen, führt Tests aus, baut dist/ |
| dist/ | ZIP-Dateien zum Hochladen und Gesamtpaket firmenbriefing-drei-agenten.zip |

## Pflege

```bash
python3 tools/build.py
```

Danach geänderte ZIP-Dateien in den Agenten ersetzen.
`python3 tools/build.py --pruefen` meldet, ob dist/ veraltet ist.

## Grenzen

- Im Agent Builder kann kein Agent einen anderen aufrufen; die Excel wird von
  Hand weitergegeben.
- Ob Agenten PDFs aus dem Web öffnen können, zeigt Probe 4 des Machbarkeitstests.
- Keine Druckprüfung im Mandanten; die Vorlage enthält Druckstile.
- Ein Agent recherchiert alle Kapitel; keine getrennten Kontexte je Faktenrolle
  wie im Claude-System.
