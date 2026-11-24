---
name: portfolio
description: Recherchiert für ein Firmenbriefing das gesamte Portfolio des Zielunternehmens auf Ebene einzelner Produktfamilien und Systeme, mit belegten Eigenschaften und belegter Statusstufe je Angebot, gestützt auf Geschäftsbericht, Produktseiten und Medien. Liefert nur Fakten mit Quellen als Teil für briefing-daten.json, ohne Bewertung.
---

# Portfolio

Vorher briefing-standards laden. Ergebnis sind Teile mit `quellen`, `claims`
(P…), `inhalt.portfolio` und `phasen`. Ziel ist ein Portfolio, mit dem man ein
Gespräch vorbereiten kann: konkrete Systeme, ihr belegter Stand, ihre Quellen.

## 1 Was ein Angebot ist

Ein **Angebot** ist eine konkrete Produktfamilie, ein System, eine Software
oder eine klar abgegrenzte Dienstleistung, die das Unternehmen unter eigenem
Namen anbietet. **Ein Geschäftsfeld oder eine Division ist nie ein Angebot.**

| Falsch | Richtig |
|---|---|
| Geschäftsfeld „Luftverteidigung“, Angebot „Luft- und Drohnenabwehr“ | Angebote „Flugabwehrkanone A“, „Flugabwehrsystem B“, „Radar C“, „Führungssystem D“ |
| Geschäftsfeld „Fahrzeuge“, Angebot „Militärfahrzeuge“ | Angebote „Radpanzer E“, „Schützenpanzer F“, „Logistik-Lkw G“ |
| Status „aktuelles Portfolio laut Hersteller“ | Stufe `serie`, Status „Serienfertigung laut Geschäftsbericht 2025, S. 34“ |

Je Geschäftsfeld die wichtigsten Angebote, in der Regel drei bis acht, mindestens
zwei. Wichtig heißt: im Geschäftsbericht oder auf der Website hervorgehoben, mit
Aufträgen oder Lieferungen in den Medien, oder für die Fokusthemen relevant.
Keine vollständige Artikelliste. Varianten getrennt führen, wenn Funktion oder
Stand wesentlich abweichen; eine Plattformreife gilt nicht für neue Varianten.

## 2 Statusstufe je Angebot (`status_stufe`)

Jedes Angebot bekommt genau eine Stufe, die höchste, die ein Beleg mit Datum trägt:

| Stufe | Nötiger Beleg |
|---|---|
| `angekuendigt` | konkretes Produkt offiziell angekündigt |
| `prototyp` | funktionsfähiger Prototyp; Konzeptbild oder Messemodell reicht nicht |
| `test` | tatsächlich durchgeführter Test oder Demonstration |
| `kundenauftrag` | konkreter Auftrag, Pilot oder beauftragte Validierung |
| `im_einsatz` | tatsächlicher Einsatz bei einem Kunden |
| `serie` | laufende Serienfertigung oder wiederholte Auslieferung |
| `eingestellt` | Angebot beendet |
| `nicht_belegt` | trotz Suche kein Statusbeleg; höchstens bei der Hälfte der Angebote |

Zusätzlich `status`: kurzer Text mit Ursprung und Quelle, z. B. „Auslieferung
laut Fachmedium, Juli 2026“. Ankündigung, Test, Auftrag, Lieferung, Betrieb und
Kapazitätsziel sind getrennte Claims mit eigenem Datum. „Lieferung laut Hersteller
berichtet“ ist kein unabhängiger Liefernachweis. Geplante Tests, Lieferziele,
Bestellungen und Kapazitäten sind kein erreichter Meilenstein. Werbung belegt
weder technische Überlegenheit noch Serienreife.

## 3 Pflichtquellen

1. **Geschäftsbericht** oder Investorenpräsentation des letzten Jahres, vor dem
   Stichtag veröffentlicht (`typ: geschaeftsbericht` oder `investor`). Daraus
   Geschäftsfelder, wichtige Produkte, Aufträge und Fertigungsstand. Ist das PDF
   nicht lesbar, Investorenpräsentation, Quartalsmitteilung oder Pressemitteilung
   zu den Zahlen suchen und die Grenze als Lücke nennen.
2. **Produktseiten oder Datenblätter** je wichtigem Angebot (`produktseite`,
   `datenblatt`), nicht nur die Divisionsübersicht.
3. **Mindestens zwei Nachrichten- oder Fachmedien** (`medien`, `fachmedien`) mit
   Aufträgen, Lieferungen, Tests, Verzögerungen. Suche je wichtigem Angebot nach
   Produktname plus contract, order, delivery, test, Auftrag, Lieferung.
4. Gegenrecherche bei Kunden, Behörden und Vergabeportalen für zentrale Aufträge.

## 4 Vorgehen in Runden

1. **Überblick:** Geschäftsbericht und Divisionsseiten öffnen, Geschäftsfelder
   festlegen. Unternehmensweite Breite, nicht nur Fokusthemen.
2. **Je Geschäftsfeld eine Runde:** wichtigste Angebote bestimmen, Produktseiten
   öffnen, Statusbelege und Medien suchen, Claims schreiben, Teil
   `teil-portfolio-<feld>.json` mit genau diesem Feld zusammenführen. Felder
   werden einzeln ergänzt, frühere Felder bleiben erhalten.
3. **Validieren nach jeder Runde.** Fehler zu Mindestregeln heißen: weiter
   recherchieren. Nur wenn nach gezielter Suche öffentlich nichts zu finden ist,
   eine Ausnahme mit Suchumfang eintragen (siehe briefing-standards).
4. Bei vielen Geschäftsfeldern nach zwei bis drei Feldern Zwischenstand ausgeben
   und um „weiter“ bitten. Lieber vollständig in mehreren Runden als flach in einer.

## 5 Claims

- Ein Claim, eine Aussage: eine Eigenschaft, ein Status, ein Auftrag. Keine
  Sammelclaims über mehrere Divisionen oder Ereignisse.
- Jede Tabellenzeile braucht mindestens einen A-Claim; B-Claims nur ergänzend.
- Eigenschaften mit Ursprung: „bis zu 150 °C (Herstellerangabe)“.

## 6 Keine Bewertung, klare Abgrenzung

Keine Scores, Rankings oder Einschätzungen; die Einordnung macht später der Skill
interpretation. Partner, Kunden und JVs als Beziehungen gehören ins Cluster,
Wettbewerbsvergleich in markt-wettbewerb; dort wird auf deine P-Claims verwiesen.

## 7 Teil schreiben

```json
{"inhalt": {"portfolio": {"felder": [{"name": "Luftverteidigung", "angebote": [
  {"name": "System B", "anwendung": "Nahbereichsschutz gegen Drohnen",
   "eigenschaften": "35-mm-Kanone, Radar integriert (Herstellerangabe)",
   "status_stufe": "kundenauftrag", "status": "Auftrag eines Landes laut Fachmedium, März 2026",
   "claims": ["P12", "P13"]}]}],
 "luecken": ["…"], "ausnahmen": []}},
 "phasen": {"portfolio": "teilweise"}}
```

Nach dem letzten Feld `phasen: {"portfolio": "fertig"}`.
