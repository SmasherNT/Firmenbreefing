# Variante A: ein Agent in Copilot Studio, Datei im Chat

Ziel: Auftrag im Chat, briefing.html als Dateikarte zurück. Keine Flows, kein
SharePoint, keine weiteren Agenten. Voraussetzung: neue Copilot-Studio-
Agentenumgebung mit Dateierzeugung (Vorschau) und Maker-Lizenz.

## Dateien

| Datei | Verwendung in Copilot Studio |
|---|---|
| instructions.md | Inhalt vollständig in das Feld „Instructions“ einfügen (rund 5.000 Zeichen) |
| wissen/briefing-gliederung.md | als Wissensdatei hochladen |
| wissen/quellenregeln.md | als Wissensdatei hochladen |
| wissen/html-vorlage.html | als Wissensdatei hochladen; Vorlage für die Ausgabe |

## Einrichtung

1. Copilot Studio öffnen, neuen Agenten anlegen, Name „Firmenbriefing“.
   Beschreibung: „Erstellt aus einer kurzen Anfrage ein Firmenbriefing zur
   Gesprächsvorbereitung als HTML-Datei.“
2. Instructions: Inhalt von instructions.md einfügen. Falls das Feld die Länge
   nicht annimmt, den Abschnitt „Inhaltsregeln“ kürzen; die Details stehen in
   briefing-gliederung.md.
3. Wissen: die drei Dateien aus wissen/ hochladen. Allgemeines Wissen des Modells
   eingeschaltet lassen, sonst scheitert die Auftragserkennung.
4. Websuche einschalten. Keine SharePoint- oder Website-Wissensquellen nötig.
5. Modell: Standard des Mandanten belassen. Keine feste Vorgabe.
6. Orchestrierung: generativ. Keine Topics, keine Tools, keine Flows.
7. Im Test-Bereich den ersten Auftrag stellen, dann in Teams veröffentlichen.

## Erste Proben, Ergebnis in testprotokoll.md eintragen

| Probe | Auftrag | Bestanden wenn |
|---|---|---|
| 1 Dateikarte | „Erstelle eine Testdatei test.html mit einer Überschrift.“ | Dateikarte erscheint, Download öffnet im Browser |
| 2 Quellenlesen | „Nenne aus dem aktuellen Geschäftsbericht von [Firma] den Konzernumsatz mit Seitenangabe und Link.“ | Zahl, Seite und Link stimmen; sonst gilt PDF als nicht lesbar |
| 3 Modul | „Nur Portfolio zu [Firma].“ | Datei mit Kopf, Portfolio, Quellen, Abnahme; keine SWOT |
| 4 Vollbriefing | „Briefing zu [Firma], Fokus: [Thema], Gesprächspartner: [Name], [Position].“ | Alle Kapitel, Themen in Reihenfolge, Personenstatus sichtbar, Quellen anklickbar |
| 5 Länge | Probe 4 mit zwei Fokusthemen | Antwort vollständig oder sauber geteilt, kein stilles Kürzen |

Beobachtetes Modell, Dauer und Credits je Probe notieren, soweit sichtbar.

## Bekannte Grenzen

- Keine unabhängige Quellenprüfung; die HTML trägt den Hinweis im Kopf.
- HTML wird vom Modell aus der Vorlage geschrieben; kein interaktives Netz, keine Druckprüfung.
- Dateierzeugung ist Vorschau; ob .html als Karte erscheint, zeigt Probe 1.
  Fallback: PDF oder Word als Ausgabeformat, oder HTML als Codeblock.
- Nichts wird gespeichert; Dateien im Chat verfallen nach 28 Tagen ohne Aktivität.
- Websuche liest nicht sicher Volltexte und PDFs; Probe 2 entscheidet.

## Ausbau danach

Erst wenn Variante A stabil läuft: Rollen auf Connected Agents aufteilen
(Variante B), danach Reviews, Ablage und Renderer nach vorgehen.md.
