# Portfolio: Darstellung und Statusvertrag

Der Renderer nutzt die vereinbarte Portfolio-Matrix: Produktgruppen als farbige
Zeilen, vier Statusstufen als Spalten plus abgesetzte Spalte „Nicht eindeutig
bestimmbar“, klickbare Produkte, Filter und alternative Tabelle. Jedes Produkt
steht in genau einer Spalte; ein „*“ hinter dem Namen markiert eine zusätzlich
noch aktive Vorstufe und wird im Detailprofil erklärt. Darunter Methodik und ein
vollständig geschlossenes Detailmodul.
Nur „03 / DETAILPROFILE & EVIDENZ“ und „Von der Position zur Begründung.“ sind
zunächst sichtbar. Produktklick öffnet beide Disclosure-Ebenen; Druck alle Profile.
CSS/JS bleiben lokal. Keine neue Grafik-, Recherche- oder Bewertungsrolle.

Die unternehmensweite geografische Aufstellung wird im Portfolio recherchiert und
als eigener Abschnitt vor Wettbewerb/Capability Matrix auf Seite 1 dargestellt;
Faktenvertrag und feste Präsenzskala siehe references/regionale-praesenz.md.

## Faktenrolle
portfolio-facts.json.products: id (stabil, Buchstaben/Ziffern/_/-), label,
short_label (optional), domain (sachliche Produktgruppe), claim_ids.
IDs, Labels und Gruppen müssen von geprüften A-Fakten getragen sein.
Je Zeile Identifikation und die entscheidenden aktuellen Statusbelege referenzieren
(Ankündigung, Prototyp/Test, laufende Serienfertigung/Auslieferung, Kundeneinsatz);
weitere Merkmale optional in sections=[{label,claim_ids}] bündeln.
Kein score/stage/Reifeurteil im Faktenmodul. Ankündigung, Test, Auftrag,
Lieferung, Betrieb und Kapazitätsziel als getrennte Tatsachen mit Datum erfassen.
Damit möglichst wenige Produkte unbestimmbar bleiben, je Produktzeile den aktuellen
Status gezielt belegen: Wird die Serie noch gefertigt/ausgeliefert? Ist das Produkt
bei einem benannten Kunden im Einsatz? Bündelzeilen mit unterschiedlichem Status
in Varianten-Zeilen aufteilen statt einen gemeinsamen Status zu behaupten.

## Vorab festgelegte Skala
Methode portfolio-status-v2, ordinale Statusstufen, kein Leistungsindex:

| Stufe (Schlüssel) | Öffentlicher Nachweis |
|---|---|
| Angekündigt (announced) | Konkretes Produkt/Programm offiziell angekündigt; kein funktionsfähiger Prototyp belegt |
| Prototyp (prototype) | Funktionsfähiger Prototyp/Demonstrator inkl. durchgeführter Tests/Qualifizierung; Konzeptbild/Messemodell reicht nicht |
| Serienproduktion (series) | Laufende Serienfertigung oder wiederholte Auslieferung |
| Im Betrieb (operation) | Tatsächlicher Einsatz bei mindestens einem Kunden in einer relevanten Aufgabe |
| Nicht eindeutig bestimmbar | Abgesetzte Sammelspalte, keine Stufe |

Spalte = höchste konkret gestützte Stufe. Geplante Tests, Lieferziele,
Bestellungen/Kundenaufträge und Produktionskapazität sind keine erreichte Stufe;
ein Auftrag bleibt als Fakt im Profil sichtbar.
Stern „*“: nur bei Serienproduktion und Im Betrieb, wenn die direkt vorherige
Stufe heute zusätzlich noch aktiv und eigens belegt ist (Im Betrieb* = weiterhin
laufende Serienfertigung/Auslieferung; Serienproduktion* = Prototypen-/
Qualifizierungsphase läuft parallel). Früheres Durchlaufen reicht nicht. Bei
Prototyp entfällt der Stern, weil die Ankündigung immer mit erfüllt ist.
Fehlender Stern behauptet nicht das Ende der Vorstufe.
Demonstrator, künftiges Kundenprodukt, Konfigurationen und Varianten getrennt
bewerten; Status einer Plattform nicht auf neue Sensoren/Software übertragen.
Bei Produktfamilien zählt der für die Zeile belegte Status; abweichende Varianten
in Unsicherheit/Grenze nennen statt den Status pauschal zu übertragen.
Eine Behauptung des Herstellers bleibt als solche sichtbar, auch in Medien.
Eine Beleglücke beschreibt Rechercheabdeckung, nicht tatsächliche Unreife.
Ältere Läufe mit portfolio-maturity-v1 (sechs Meilensteine) bleiben les- und
renderbar; neue Positionierungskontexte nutzen ausschließlich v2.

## Positionierungsrolle
Kontext mit check-interpretation.py --prepare --portfolio erzeugen. Er enthält
nur kompakte Produktzuordnung, feste Skala und relevante A-Fakten; keine HTML.
Im vollständigen Briefing genau eine I-Interpretation pro context.portfolio.products
liefern. Zusätzlich zum Standardvertrag:

```json
{
  "id": "I-PM-kit",
  "type": "product_maturity",
  "section": "portfolio",
  "product_id": "kit",
  "method_id": "portfolio-status-v2",
  "assessment_status": "bewertet",
  "stage": "operation",
  "stage_basis": ["P4"],
  "also_previous": {"stage": "series", "basis": ["P2"],
                    "note": "Serienfertigung läuft weiter; Stückzahl nicht veröffentlicht."},
  "statement": "…",
  "depends_on": ["P2", "P4"],
  "reasoning": "…",
  "method": "Höchste konkret belegte Statusstufe",
  "uncertainty": "…",
  "next_stage_limit": ""
}
```

stage_basis und also_previous.basis: nicht leere Teilmengen von depends_on mit
mindestens einem eigenen Produktfakt. also_previous nur bei stage=series/operation
und nur mit der direkt vorherigen Stufe; ohne Stern Feld weglassen.
next_stage_limit für alle Stufen unterhalb Im Betrieb (warum die nächste nicht belegt ist).
Nur direkte geprüfte Fakten als depends_on, Begründung normalerweise 2–3 Sätze.
Unbestimmbar: assessment_status="nicht eindeutig bestimmbar", stage=null, kein
also_previous, coverage_note mit konkreter Beleggrenze. Keine Ersatzstufe.
Solche Einträge können leere depends_on haben und tragen keine SWOT-Ableitung.
Fehlt für eine Einordnung ein konkreter aktueller Statusbeleg, research_request
an portfolio stellen, statt vorschnell „nicht eindeutig bestimmbar“ zu vergeben.
Andere Zusatzscores bleiben an assessment_methods des Vergleichsplans gebunden;
Capability-Matrix-Kriterien ergeben sich weiterhin aus dem Prüfauftrag.

## Review und Ausgabe
Basis-Reviewer prüft Produktidentität, Gruppe, Statusdatum und Claim-Zuordnung.
Final-Reviewer prüft I-Statuszuordnung, Stern samt eigenem aktuellen Beleg,
Varianten-/Zeitbezug und Evidenzgrenze
in der bestehenden gemeinsamen Prüfrunde. Kein zusätzlicher Quellenprüfer.
Inventaränderungen invalidieren den Positionierungskontext. Alle freigegebenen
Einordnungen und Abhängigkeiten behalten Fingerprints und Schluss-Review.
--full verlangt aktuelle Produktzuordnung und eine freigegebene Einordnung pro
Produkt. Reine Fakten-HTML zeigt Produkte ohne interpretierte Stufe („Noch nicht eingeordnet“).
Details enthalten Status mit Beleg, ggf. „* Zusätzlich: <Vorstufe>“ mit Hinweis
und Beleg, weitere Fakten, Einordnung, Grenzen und direkte Originalbelege.
Aussageursprungsfilter nutzt vorhandene Claim-Arten; „Fakt“ behauptet keine
unabhängige Bestätigung. Keine Quellenklassifikation allein aus dem Publishernamen.

Auftragsbezogene Themenkarten mit headline/preview sowie unternehmensweite
Portfolioabdeckung folgen themen-darstellung.md. SWOT-Kategorien farbig darstellen.
