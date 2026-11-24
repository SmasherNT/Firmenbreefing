---
name: markt-wettbewerb
description: Recherchiert für ein Firmenbriefing Markt, Nachfrage und Programme, legt vor der Wettbewerbsrecherche einen Vergleichsplan fest, sammelt vergleichbare Wettbewerbsfakten und die regionale Präsenz des Zielunternehmens. Liefert nur Fakten als Teil für briefing-daten.json, ohne Scores oder Positionsurteile.
---

# Markt, Wettbewerb und regionale Präsenz

Vorher briefing-standards laden; Suchwege in references/vergleich-und-praesenz.md.
Ergebnis ist ein Teil mit `quellen`, `claims` (M…), `inhalt.markt`, `phasen`.

## 1 Markt

- Größe, Wachstum, Treiber, Programme, Beschaffung, Regulierung im für den
  Auftrag relevanten Segment und in den relevanten Regionen.
- Je Kennzahl Definition, Region, Zeitraum, Einheit, Währung, Preisbasis.
- Daten von Behörden, Verbänden, Auftraggebern und Unternehmen bevorzugen.
  Keine Prognosen aus Snippets, keine ungelesenen kommerziellen Studien.
- Verteidigungsbudget ist kein Segmentvolumen, Rahmenhöchstwert kein Auftrag,
  Bestellung keine Lieferung, Zielkapazität kein Ist-Ausstoß.
- Fehlt ein Gesamtvolumen, belegte Programm- und Strukturdaten statt Schätzung.

## 2 Vergleichsplan zuerst

Bevor Wettbewerber recherchiert werden, festlegen und im Teil speichern:

1. **Vergleichseinheit:** konkrete Angebote mit vergleichbarer Rolle, nicht ganze
   Konzerne. Varianten und Ausbaustufen unterscheiden.
2. **Drei bis fünf Wettbewerber** nach vergleichbarer Rolle, keine Rangliste.
3. **Drei bis fünf fachliche Kriterien**, bei Produktvergleichen überwiegend
   technisch, je mit Definition, Einheit und Bedingungen. Dazu immer
   „Belegter Einsatzstand“ und „Fertigungs- und Lieferfähigkeit“.

## 3 Wettbewerbsfakten

- Je Angebot und Kriterium die belegte Angabe mit Ursprung. „Bis zu“, Herstellerangabe,
  Medienangabe, Test und Einsatznachweis unterscheiden.
- Werte anderer Varianten nie übertragen. Radarreichweite ist keine
  Wirkungsreichweite. Geplante Integration ist kein Serienstand.
- Für das Zielunternehmen vorhandene P- und C-Claims per ID verwenden, nicht neu anlegen.
- Nichts gefunden: Zelle weglassen, sie erscheint als „nicht öffentlich belegt“.
  Nicht anwendbar als Text „nicht anwendbar: Grund“ mit Beleg.
- Keine Scores, keine Sieger, keine Summen.

## 4 Regionale Präsenz des Zielunternehmens

- Unternehmensweit, nicht nur im Fokusthema. Je Aktivität: Rechtsträger, Land und
  Ort, Funktion (Büro, Produktion, Integration, Service, Entwicklung, Partner,
  Kundenaktivität), Betreiber (eigen, partner, jv, kunde, ausland), Status
  (operativ oder angekündigt), Produktbezug.
- Eigene Infrastruktur nur mit Beleg als `eigen`. Partner-, JV- und Kundenanlagen
  nicht dem Zielunternehmen zurechnen. Kundenbelieferung belegt keinen Standort.
- Bei JV die Kontrolle getrennt belegen; Quote allein reicht nicht.
- Länder genau benennen: eine US-Präsenz belegt keine Präsenz in Kanada.
- Keine Stufen vergeben; das macht interpretation.

## 5 Mindestumfang

- Mindestens zwei Marktkennzahlen mit Definition, Region, Zeitraum und Quelle.
- Vergleich mit mindestens drei Zeilen (Zielunternehmen und zwei Wettbewerber)
  und mindestens drei Kriterien.
- Mindestens zwei Nachrichten- oder Fachmedien.
- Präsenz: `betreiber` genau einer von eigen, partner, jv, kunde, ausland;
  `status` genau einer von operativ, angekündigt. Details in den Text, nicht in
  diese Felder.
- Fehlt nach gezielter Suche etwas, Ausnahme mit Suchumfang statt Fülltext.

## 6 Teil schreiben

- `inhalt.markt`: `kennzahlen`, `vergleich` (einheit, kriterien, zeilen),
  `praesenz`, `luecken`. Alle sichtbaren Angaben sind A.
- Datei `teil-markt.json`, `phasen: {"markt": "fertig"}`, zusammenführen, validieren.
- Eigene Fokusthemen gehören in den Skill fokusthema, nicht hierher.
