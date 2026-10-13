# Regionale Präsenz auf einen Blick

Inhalt: Recherche · feste Skala · Faktenvertrag · Positionierung · Ausgabe/Review.

Auf Seite 1 als eigener Abschnitt nach Cluster und direkt vor Wettbewerb/Capability
Matrix. Stil der gelieferten Quantum-Systems-HTML: klickbare Regionszeilen, links
Region/Land, mittig Präsenzart und Produktumfang, rechts fünf ausgefüllte/leere
Kreise, n/5 und Pfeil. Auftragsfokus dezent gold hervorheben; übrige Zeilen dunkelblau.
Regionalklick öffnet darunter das passende Detailprofil mit Quellen. Firmen,
Regionen, Aktivitäten und Einstufungen entstehen je Auftrag neu.

## Recherche im Portfolio, vorhandene Cluster-Fakten wiederverwenden

Unternehmensweite geografische Aufstellung untersuchen, nicht nur den spezifischen
Industrie-Deep-Dive. Eigene Gesellschaften/Büros, Produktion, Entwicklung, Service,
Vertriebs-/Servicepartner, Auslandbetreuung und belegte Kundenaktivitäten erfassen.
Nachrichten und Fachmedien einbeziehen, konkrete öffentliche Quellen tatsächlich
öffnen. Vorhandene P-/C-/M-Claims über IDs wiederverwenden; kein zweiter Bericht.

Je Aktivität Rechtsträger/Akteur, Land, konkreter Standort, Funktion, Produkt- oder
Geschäftsbereich, Eigentums-/Kontrollbezug, Status und Statusdatum festhalten.
Hersteller-/Partnerangaben sichtbar zuschreiben. Eigene bzw. beherrschte Tochter-
Infrastruktur nur mit konkretem Beleg als own einordnen; fremde Werke, JV-/Partner-
Infrastruktur und Kundenanlagen nicht pauschal dem Zielunternehmen zurechnen.
Cluster liefert bei Bedarf Kontroll-/Beziehungsbelege. Kundennutzung allein belegt
keinen eigenen Standort oder lokalen Vertriebskanal.

Regionsraster aus globaler Firmenaufstellung und Auftrag ableiten. Belegte Länder
und regionale Reichweite ausdrücklich nennen: eine US-Präsenz belegt keine Kanada-
oder Mexiko-Präsenz, ein Dubai-Partner keine QS-Verträge in allen Golfstaaten.
Südafrika als Südafrika benennen. Wenn ein Land separat geführt wird (etwa Ukraine),
übriges Regionsaggregat entsprechend abgrenzen. Keine Weltkarte zur Grafikfüllung.
Produktbezug erhalten: Vermessungs-/Softwarevertrieb ist nicht das gesamte Defence-
Portfolio. Ohne Beleg offene Abdeckung, niemals fehlende tatsächliche Aktivität.

## Feste ordinale Skala

Methode regional-presence-v1; unabhängig von Produktreife und Wettbewerbsplan:

| Stufe | Konkreter Nachweis |
|---|---|
| 1 | Regionaler Zugang angekündigt oder dokumentierte Betreuung aus dem Ausland |
| 2 | Benannter operativer lokaler/regionaler Vertriebs- oder Servicepartner bzw. entsprechender JV-Zugang |
| 3 | Eigene operative Gesellschaft / eigenes Büro, auch eigenes Entwicklungsbüro |
| 4 | Eigene operative lokale Produktion oder eigene operative Serviceinfrastruktur |
| 5 | Eigene operative Produktion plus lokale Entwicklung oder mindestens zwei eigene operative Standorte in der betrachteten Region |

Höchste erfüllte Stufe anhand der vorhandenen A-Fakten wählen. Produktion und
Entwicklung am selben Standort reichen für 5; zwei Funktionsbezeichnungen am
gleichen Standort sind hingegen keine zwei Standorte. Mehrere Büros ohne Produktion
reichen nicht für 5. Partner-/JV-Werke sind ohne belegte eigene Kontrolle kein own.
Angekündigte Büros/Fabriken bleiben 1; eine Ankündigung ist kein laufender Betrieb.
Kundenaktivitäten werden qualitativ gezeigt und heben die Infrastrukturstufe allein
nicht an. Ohne passenden Nachweis auch für 1: null / nicht eindeutig bestimmbar.
Keine Null-/Ersatzstufe. Kein Umsatz-, Marktanteils-, Attraktivitäts- oder Leistungsindex.

## Faktenvertrag: portfolio-facts.json.regional_presence

Liste von Regionen, in der gewünschten Grafikreihenfolge. Jede Zeile:

| Feld | Inhalt |
|---|---|
| id, label | Eindeutige stabile ID, Regions-/Ländername (max. 80 Zeichen) |
| countries | Eindeutige Liste der hier bewerteten Länder; lokale Aktivitäten müssen darin liegen |
| presence_type | Quellengetragene Kurzbeschreibung (max. 100 Zeichen); ohne Fakten leer lassen |
| geographic_scope | Belegter Schwerpunkt, Abgrenzung und Grenzen des Regionsaggregats |
| product_scope | Tatsächlich betroffene Produkte/Geschäftsbereiche; keine unbelegte Portfolioausweitung |
| focus | Optionaler Boolean für den ausdrücklich beauftragten Regionsfokus |
| claim_ids | Vollständige eindeutige direkte Faktenreferenzen der Region, bei fehlendem Beleg leer |
| activities | Liste konkreter quellengedeckter Aktivitäten, bei fehlendem Beleg leer |
| coverage_note | Dokumentierte Such-/Beleggrenze; keine tatsächliche Schwäche behaupten |

Jede Aktivität enthält id, actor, country, location, product_scope, description,
kind, operator, status, status_date (YYYY-MM-DD oder null), claim_ids.
IDs: Buchstabe, danach Buchstaben/Ziffern/_/-. Keine Scores in Faktenphase.

- kind: access, foreign_support, partner, office, production, service,
  development oder customer_activity.
- operator: own, partner, jv, customer oder foreign. Partnerfunktionen/Standorte
  bleiben partner/jv; Kundennutzung bleibt customer_activity/customer.
- status: announced oder operational. operational bedeutet in der geöffneten
  Quelle operativ dokumentiert, nicht automatisch unabhängig bestätigt.
- access nur announced; foreign_support nur foreign; partner nur partner/jv;
  customer_activity nur customer. office/production/service/development mit
  own/partner/jv möglich. Lokale Aktivitäten liegen in countries, Auslandbetreuung
  kann außerhalb liegen. Statusdatum nicht neuer als Briefingstichtag.
- Bei eigenen office/production/service/development zusätzlich site_id und
  ownership_note mit belegter Eigen-/Kontrollzuordnung. Gleicher physischer
  Standort hat immer dieselbe ID und konsistente Land-/Standortangaben. Verschiedene
  Funktionen am selben Ort nicht als unterschiedliche eigene Standorte zählen.
- Aktivitäten referenzieren eine nicht leere Teilmenge der Region-claim_ids.
  Für eine Stufe erforderliche Kontroll-/Umsetzungsbelege in diese Referenzen
  aufnehmen. Neue Rollenklassifikation und Kurztexte semantisch im Basis-Review prüfen.

## Positionierung und Prüfbindung

Vollbriefing-Kontext mit --presence erzeugen, zusätzlich zu --portfolio und
--module-insights. Es enthält feste Skala und kompakte regionale Belegzuordnungen;
nur deren benötigte Fakten werden ergänzt, keine vollständigen Langberichte.
Die bestehende Positionierungsrolle liefert genau einen regulären I-Claim je Region:
type=regional_presence, section=regional_presence, region_id,
method_id=regional-presence-v1, assessment_status, score, statement, depends_on,
reasoning, method, uncertainty und next_stage_limit (bei bewerteter Stufe).
depends_on verwendet direkt Fakten dieser Region und muss die höchste Stufe tragen.
Bei nicht eindeutig bestimmbar score=null, coverage_note; leere depends_on zulässig.
Eine unbewertete Region trägt keine SWOT-Ableitung.

Der lokale Check prüft Vollständigkeit, höchsten erfüllten Anker, Standort-
Deduplikation und Abhängigkeiten. Er prüft keine Quellenwahrheit. Basis-Reviewer
prüft Quellen, Rollen-/Standort-/Status-/Scope-Zuordnung; alle referenzierten
Präsenzfakten stehen in required_full_review_ids. Ganze Faktzuordnung ist im
Paket-Fingerprint, feste Methodik/Region und I-Einordnung im I-Fingerprint.
Final-Reviewer prüft Ableitung und Reichweite in der bestehenden gemeinsamen Runde.
Änderungen gezielt erneut prüfen; keine weitere Recherche-/Prüfrolle.

## Ausgabe und Abgrenzung

Klick auf die ganze Zeile öffnet genau das Regionsprofil und scrollt dorthin.
Details: Wie vertreten? · Warum diese Stufe? · Reichweite des Nachweises ·
Originalquellen/Belegstellen. Hersteller-/Partnerursprung, Produktumfang und
Datums-/Umsetzungsgrenzen bleiben sichtbar. Methodik separat aufklappbar.
Unbestimmbare Regionen erhalten leere Kreise und „—“, Faktenansicht ohne I-Review
„Unbewertet“ ohne ersetzte Stufe. Keine Bewertung beim Rendern erzeugen.
Native Details bleiben ohne JavaScript und im Druck vollständig nutzbar;
anschließend vorherigen Druck-/Auswahlzustand wiederherstellen.

Unternehmenspräsenz hier auf Seite 1; der allgemeine regionale Markt-/Industrie-
Deep-Dive bleibt auf Seite 3. Alte zusätzliche portfolio.regions-Belege, die in
den neuen Profilen nicht enthalten sind, hier ergänzend erhalten. Ältere Pakete
ohne regional_presence bleiben kompatibel; keine Quantum-Systems-Daten kopieren.
