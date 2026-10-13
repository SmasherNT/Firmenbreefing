# Keyfacts & Insights unter den Modulen

Auf Seite 1 direkt unter Portfolio, Cluster und Markt-/Wettbewerbsanalyse je
1–3 kompakte Karten im bestätigten Stil zeigen. Jede Karte enthält einen kurzen
Titel, einen belegten Fakt und einen daraus abgeleiteten Insight. Quellen,
Herleitung und Einschränkungen per Klick in nativen Details; auch ohne JavaScript
und vollständig im Druck. Keine zusätzlichen Scores oder eigene Recherche.

## Auswahl im bestehenden Positionierungsschritt

- Aus den vorhandenen A-Fakten die modulspezifischen, entscheidungsrelevanten
  Punkte wählen. Keine bloße Wiederholung der Executive Summary, keine drei
  Karten zur Rasterfüllung und keine allgemein gültigen Beratungssätze.
- Portfolio: unternehmensweite Produkt-/Geschäftsfeldstruktur, relevante
  Reifeunterschiede, industrielle Kapazitäten oder belegte Entwicklungsschritte.
  Den spezifischen Industrie-Deep-Dive nicht als gesamtes Portfolio behandeln.
- Cluster: konkrete Partnerrollen, industrielle Abhängigkeiten, Eigentum vs.
  Kontrolle, belegte Querverbindungen und Bedeutung für Integration/Marktzugang.
- Markt: konkrete Unterschiede im Wettbewerbsvergleich, dokumentierte
  Beschaffungs-/Nachfragesignale und Zugangsbedingungen im beauftragten Segment.
  Ein Kriteriumsvorsprung ist kein Gesamtvorsprung; Budgetkontext kein Segmentvolumen.
- Zuschreibung, Zeitraum und Bezug erhalten: „laut Hersteller“, geplant vs.
  umgesetzt, Produkt vs. Konzern, ein Kriterium vs. Gesamtangebot. Eine Datenlücke
  nur als wichtige Beleggrenze erwähnen, niemals als nachgewiesene Schwäche.
- Fakten und Analysteninterpretation sichtbar trennen. Keine neuen Kennzahlen,
  Unternehmensbehauptungen oder Prioritätsscores in Titel/Kurztext ergänzen.

Der Hauptagent wählt passende A-Claim-Auszüge für alle drei Module und ergänzt den
selektiven Positionierungskontext mit `--module-insights` (im Vollbriefing zusammen
mit `--portfolio`). Das Skript ergänzt nur die beauftragten Modulnamen in
context.module_insights; es lädt keine weiteren Fakten pauschal. Falls die
delegierten Auszüge nicht reichen, gezielt passende vorhandene A-Fakten anfordern.
Die bestehende Positionierungsrolle erstellt Karten innerhalb positioning.json;
SWOT erhält weiterhin nur tatsächlich benötigte I-IDs. Keine weitere Agentenrunde.

## Datenvertrag

Jede Karte ist ein regulärer, im Schluss-Review geprüfter I-Claim:

| Feld | Vorgabe |
|---|---|
| type / section | module_insight / module_insights |
| module | portfolio, cluster oder market; muss im Kontext beauftragt sein |
| display_order | 1 bis Anzahl der Karten, je Modul eindeutig und lückenlos |
| headline | Kurzer Titel, maximal 72 Zeichen |
| fact_text | Quellengedeckte Kurzfassung, maximal 180 Zeichen |
| fact_claim_ids | Nicht leere, eindeutige Liste direkt referenzierter Fakten |
| statement | Insight / Analysteninterpretation, maximal 180 Zeichen |
| depends_on | fact_claim_ids plus ggf. weitere relevante A-Fakten oder I-Claims |
| reasoning, method, uncertainty | Herleitung, Methode und konkrete Beleggrenze nach Interpretationsvertrag |

Die allgemeinen Felder id, Laufidentität und Input-Fingerprint bleiben bestehen.
fact_claim_ids müssen Teil von depends_on sein; sämtliche Abhängigkeiten müssen
im delegierten Kontext und aktuell vollständig geprüft sein. Keine score/value-
Felder. Maximal drei Karten je Modul; kein getrenntes ungeprüftes Layout-JSON.

Wenn für ein Modul kein zusätzlicher belastbarer Fakt/Insight ausgewählt werden
kann, statt einer Karte `module_insight_gaps:[{module,reason}]` im Positionierungs-
Output dokumentieren. reason beschreibt die Auswahl-/Beleggrenze für den Reviewer;
der Renderer zeigt nur die neutrale Systemmeldung „Für dieses Modul liegen keine
freigegebenen zusätzlichen Keyfacts & Insights vor.“ Keine freie ungeprüfte
Unternehmensbehauptung aus reason ausgeben. Karten und Gap für dasselbe Modul
sind unzulässig; jedes beauftragte Modul muss Karten oder einen Gap erhalten.

## Prüfung und Ausgabe

Im bestehenden Schluss-Review Titel, Faktverdichtung, Insight, Reihenfolge,
Modulzuordnung, Claim-Bezüge und Ableitung gemeinsam prüfen. Sämtliche sichtbaren
Kartenfelder sind Teil des I-Claim-Fingerprints. Nach Änderung der Texte/Zuordnung
betroffene I-Claims erneut prüfen; aktuelle A-Fakten bleiben wiederverwendbar.
Gap-Begründungen auf tatsächlichen Auswahl-/Belegumfang prüfen. Ein mechanischer
Pass ist keine Inhaltsfreigabe, der Renderer erzeugt keine Insights selbst.

Die Karten stehen innerhalb des jeweiligen Moduls hinter dessen Darstellung,
nicht erneut im allgemeinen Einordnungsabschnitt. Markt-Karten hinter der
Capability Matrix; bei einem Auftrag ohne Matrix als kompakte Markt-/Wettbewerbs-
Einordnung auf Seite 1. Der regionale Markt-Deep-Dive auf Seite 3 bleibt separat.
Ein bis drei Karten nutzen entsprechend eine bis drei Spalten am Desktop,
Kurztexte vollständig ohne Abschneiden. Öffnen zeigt sämtliche Fakten, direkte
Originalquellen, Belegstellen, Herleitung und Unsicherheit.
Alte Kontexte ohne module_insights bleiben nutzbar; keine Karten erfinden.
