---
name: portfolio
description: Recherchiert für ein Firmenbriefing das gesamte Portfolio des Zielunternehmens mit allen wesentlichen Geschäftsfeldern, Produkten, Software und Dienstleistungen, deren belegten Eigenschaften und Status. Liefert nur Fakten mit Quellen als Teil für briefing-daten.json, ohne Reifebewertung.
---

# Portfolio

Vorher briefing-standards laden. Ergebnis ist ein Teil mit `quellen`, `claims`
(P…), `inhalt.portfolio` und `phasen`.

## Umfang

- Im Vollbriefing das ganze Unternehmen: alle wesentlichen Geschäftsfelder,
  Produktfamilien, Software und Dienstleistungen, auch außerhalb der Fokusthemen.
  Ein Fokusthema ist nie das ganze Portfolio.
- Bei Modulauftrag nur den beauftragten Umfang.
- Aktuelle und eingestellte Aktivitäten aus Unternehmensquellen bestimmen und
  eingestellte kennzeichnen. Keine vollständige Artikelliste; Varianten getrennt
  führen, wenn Funktion oder Reife wesentlich abweichen.

## Recherche

1. Unternehmensseite, Produktseiten, Datenblätter, Geschäftsbericht
   (Segment- und Lagebericht), Investorenpräsentationen.
2. Nachrichten- und Fachmedien zu Produkten, Tests, Aufträgen, Lieferungen,
   Verzögerungen; Gegenrecherche bei Kunden und Behörden.
3. Je Angebot erfassen: Anwendung, zwei bis vier belegte Eigenschaften,
   belegter Status mit Datum.

## Status sauber trennen

Ankündigung, Prototyp, Test oder Demonstration, Kundenauftrag oder Pilot,
Betrieb beim Kunden, Serie oder wiederholte Auslieferung sind getrennte
Tatsachen und getrennte Claims. Nur erfassen, was die Quelle trägt.
„Lieferung laut Hersteller berichtet“ ist kein unabhängiger Liefernachweis.
Geplante Tests, Lieferziele und Kapazitäten sind kein erreichter Meilenstein.
Werbung belegt weder technische Überlegenheit noch Serienreife.
Eine Plattformreife gilt nicht automatisch für neue Sensoren oder Software.

## Keine Bewertung

Keine Scores, Reifegrade, Rankings oder Einschätzungen. Die Einordnung macht
später der Skill interpretation.

## Abgrenzung

Partner- und Kundenbeziehungen gehören ins Cluster, Wettbewerbsvergleich in
markt-wettbewerb. Dort wird auf deine P-Claims per ID verwiesen.

## Teil schreiben

- `inhalt.portfolio.felder`: je Geschäftsfeld `name` und `angebote` mit
  `name`, `anwendung`, `eigenschaften` (mit Ursprung, z. B. „laut Hersteller“),
  `status`, `claims`.
- Geschäftsfelder ohne ausreichende Belege als `luecken` führen.
- Datei `teil-portfolio.json`, `phasen: {"portfolio": "fertig"}`, zusammenführen,
  validieren.
