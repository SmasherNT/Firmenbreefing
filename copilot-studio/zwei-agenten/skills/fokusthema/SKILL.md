---
name: fokusthema
description: Recherchiert für ein Firmenbriefing genau ein vom Nutzer genanntes Fokusthema als neutrales Themen- und Marktbriefing mit Definition, Kennzahlen, Segmenten, Akteuren, Kernaussagen, Entwicklungen der letzten sechs Monate und Gesprächsfragen. Je Thema ein eigener Durchgang und ein eigener Teil für briefing-daten.json.
---

# Fokusthema

Vorher briefing-standards laden. Je Fokusthema ein eigener Durchgang mit eigener
Datei `teil-fokus-<id>.json`. Claims mit Präfix `F_<id>_`, z. B. `F_lkw_1`.

## Haltung

Neutrales Meetingbriefing zum Thema selbst, verständlich ohne den Rest des
Briefings. Das Zielunternehmen ist kein Filter: Es erscheint wie andere Akteure
nach denselben Kriterien, sofern relevant. Keine Firmenstrategie unterstellen,
keine Vertriebsargumente, keine reine Firmen-Nachrichtenchronik, keine SWOT.

## Inhalt

1. **Definition:** ein bis zwei Sätze, geografische und sachliche Abgrenzung,
   Betrachtungszeitraum. Grundblick global, Vertiefung nach Auftrag.
2. **Kennzahlen:** Ziel vier bis sechs belastbare Zahlen, höchstens sechs. Je Zahl
   Typ (Marktgröße, Budget, Rahmenhöchstwert, fester Auftrag, Lieferungen,
   Kapazität, technisch, Industriestruktur), Zeitraum, Abgrenzung, Quelle.
   Keine Summe oder Rangfolge aus unvergleichbaren Zahlen. Unter vier Zahlen:
   Grund als Lücke.
3. **Segmente und Wertschöpfung:** Funktionen erklären, keine unbelegten Beziehungen.
4. **Akteure:** aus mindestens drei unabhängigen Akteursgruppen, je Rolle,
   belegtes Angebot, Segment. Auswahlkriterien als Lücke oder Hinweis nennen.
   Keine Marktanteile oder Vollständigkeit suggerieren.
5. **Kernaussagen:** drei bis fünf belegte Erkenntnisse; bei dünner Evidenz weniger
   mit Grund. Keine eigenen Schlussfolgerungen.
6. **Entwicklungen:** Stichtag minus sechs Kalendermonate bis Stichtag. Ankündigung,
   Auftrag, Pilot und Betrieb unterscheiden. Ereignisdatum, nicht Abrufdatum.
7. **Gesprächsfragen:** ein bis drei neutrale, offene Fragen aus belegten Themen.

## Quellen

Kennzahlen aus geöffneten Originaldaten von Auftraggebern, Behörden,
Organisationen, Verbänden und Unternehmen. Fach- und Wirtschaftsmedien für
Gegenprüfung und Entwicklungen. Alle sichtbaren Fokus-Fakten sind A.

## Teil schreiben

- `inhalt.fokus`: ein Eintrag mit derselben `id` und `titel` wie im Auftrag.
- `phasen: {"fokus:<id>": "fertig"}`, zusammenführen, validieren.
- Fokus-Fakten gehen nicht automatisch in Positionierung oder SWOT ein.
