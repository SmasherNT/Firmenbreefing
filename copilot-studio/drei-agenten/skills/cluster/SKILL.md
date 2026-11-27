---
name: cluster
description: Recherchiert für ein Firmenbriefing Eigentum, Kontrolle, Töchter, Joint Ventures, Partner, Kunden, Zulieferer, Projekte und Querverbindungen mit Geschäftsberichtsanalyse und Gegenrecherche. Liefert nur belegte Beziehungen als Teil für briefing-daten.json, ohne Bewertung.
---

# Struktur, Partner und Kunden (Cluster)

Vorher briefing-grundlagen laden; für Suchwege references/quellenwege.md lesen.
Ergebnis ist ein Teil mit `quellen`, `claims` (C…), `inhalt.cluster`, `phasen`.

## Umfang

- **Ebene 1:** Mutter, Töchter, Beteiligungen, Joint Ventures, Kooperations-
  partner, Kunden, Zulieferer, Projektpartner des Zielunternehmens.
- **Ebene 2:** Beziehungen zwischen diesen Akteuren und Akteure, die eine direkte
  Beziehung erklären, z. B. weitere JV-Gesellschafter oder Eigentümer eines Partners.
- Weitere Ebenen nur, wenn sie Eigentum, Kontrolle oder ein Fokusthema erklären.
  Keine unbegrenzte Netzwerkrecherche. Kein Anspruch auf vollständige Konzernstruktur.
- Vier Bereiche immer prüfen: Kapital und Konzern, Technologie und Industrie,
  Kunden und Aufträge, Marktzugang und Vertrieb. Leere Bereiche als Lücke führen.

## Beziehungstypen und Grenzen

| Typ | Grenze |
|---|---|
| Eigentum / Kontrolle | Kapitalanteil ist nicht Stimmrecht und nicht Kontrolle; getrennt erfassen |
| Joint Venture | alle Gesellschafter, Quoten, Zweck, Rolle; 50/50 beweist keine gemeinsame Kontrolle |
| Kooperation | konkreter Gegenstand und Status; Kompatibilität ist keine Kooperation |
| Kunde / Lieferant | Richtung, Gegenstand, Zeitraum; Ausschreibung, Zuschlag, Lieferung trennen |
| Projekt / Konsortium | gemeinsame Teilnahme ist kein bilateraler Vertrag |
| Lizenz / Technologie | Integration nur mit Beleg |
| Berufliches Mandat | öffentlich dokumentierte Organfunktionen mit Zeitraum |
| Historisch | beendete Beziehungen getrennt von aktuellen |

Gemeinsamer Kunde oder Lieferant ist eine **Überschneidung**, keine
Zusammenarbeit. Indirekte Verbindungen als Pfad aus einzeln belegten Teilbeziehungen.
Angekündigte Transaktionen sind nicht abgeschlossen. Keine Beziehung aus
Produktähnlichkeit ableiten.

## Geschäftsberichte

Pflicht für Zielunternehmen und strukturtragende Akteure: neuester vor dem
Stichtag veröffentlichter Geschäfts- oder Konzernbericht. Lies Anhang
(Anteilsbesitz, Konsolidierungskreis, Gemeinschaftsunternehmen, assoziierte
Unternehmen), Erwerbe und Veräußerungen, Ereignisse nach dem Stichtag, Segment-
und Lagebericht, Corporate Governance. Bei relevanten Änderungen das Vorjahr
vergleichen. Je Bericht eine Zeile in `inhalt.cluster.berichte` mit Status
„analysiert“, „nicht gefunden“, „nicht zugänglich“ oder „teilweise lesbar“.
Nur Snippets gelesen heißt nicht analysiert.

## Gegenrecherche

Jeden relevanten Partner, Kunden und Gesellschafter auch von dessen Seite
suchen. Aus Artikeln neu gefundene Akteure erneut suchen. Wichtige Eigentums-,
Kontroll- und Kundenbeziehungen möglichst mit unabhängigem Original bestätigen.
Widersprüche zu Quote, Datum oder Status offen benennen.

## Mindestumfang

- Mindestens drei belegte Beziehungen; bei Konzernen deutlich mehr: Mutter,
  wichtige Töchter, jedes JV, zentrale Kunden und Partner der Fokusthemen.
- Mindestens ein Geschäftsbericht mit Status „analysiert“ in `berichte`.
- Mindestens zwei Nachrichten- oder Fachmedien zur Entdeckung und Gegenprüfung.
- `typ` genau einer von: Eigentum, Joint Venture, Kooperation, Kunde, Lieferant,
  Projekt, Lizenz, Mandat, historisch. `art` genau einer von: direkt, indirekt,
  Überschneidung.
- Fehlt nach gezielter Suche etwas, Ausnahme mit Suchumfang statt Fülltext.

## Teil schreiben

Die HTML zeigt daraus ein Unternehmensnetzwerk mit Tabellen- und Grafikansicht.
Deshalb sind diese Felder wichtig:

- `inhalt.cluster.akteure`: je Akteur `name`, optional `langname`, `art`
  (eigentuemer, tochter, jv, partner, kunde, zulieferer, projekt, institution,
  person, sonstige) und `bereich` (kapital, konzern, technologie, markt). Daraus
  entstehen Farbe und Gruppe im Netzwerk. `fokus: true` für Akteure der Fokusthemen.
- `inhalt.cluster.beziehungen`: `von`, `zu`, `typ`, `gegenstand`, `anteil_rolle`,
  optional `kapitalanteil`, `stimmrechte`, `kontrolle`, `art` (direkt, indirekt,
  Überschneidung), `status`, `datum` (JJJJ-MM oder JJJJ-MM-TT), optional
  `produkte` (Angebotsnamen aus dem Portfolio), `unsicherheit`, `claims`.
  Jede Beziehung ist A.
- Das Zielunternehmen heißt in `von`/`zu` genau wie `auftrag.kurzname`.
  Bei Eigentum zeigt `von` auf den Eigentümer.
- Auch Querverbindungen zwischen anderen Akteuren als Beziehung eintragen,
  zum Beispiel weitere JV-Gesellschafter oder Eigentümer eines Partners.
- `berichte` und `luecken` wie oben.
- Datei `teil-cluster.json`, `phasen: {"cluster": "fertig"}`, zusammenführen, validieren.
- Keine Bewertung von Abhängigkeit oder Einfluss; das macht interpretation.
