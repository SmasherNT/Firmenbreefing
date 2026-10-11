# Portfolio: Darstellung und Reifevertrag

Der Renderer nutzt die vereinbarte Portfolio-Matrix: Produktgruppen als farbige
Zeilen, sechs Reifestufen als Spalten, klickbare Produkte, Filter und alternative
Tabelle. Darunter Methodik und ein vollständig geschlossenes Detailmodul.
Nur „03 / DETAILPROFILE & EVIDENZ“ und „Von der Position zur Begründung.“ sind
zunächst sichtbar. Produktklick öffnet beide Disclosure-Ebenen; Druck alle Profile.
CSS/JS bleiben lokal. Keine neue Grafik-, Recherche- oder Bewertungsrolle.

## Faktenrolle
portfolio-facts.json.products: id (stabil, Buchstaben/Ziffern/_/-), label,
short_label (optional), domain (sachliche Produktgruppe), claim_ids.
IDs, Labels und Gruppen müssen von geprüften A-Fakten getragen sein.
Je Zeile nur Identifikation und entscheidende Statusbelege referenzieren;
weitere Merkmale optional in sections=[{label,claim_ids}] bündeln.
Kein score/grade/Reifeurteil im Faktenmodul. Ankündigung, Test, Auftrag,
Lieferung, Betrieb und Kapazitätsziel als getrennte Tatsachen erfassen.
Keine zusätzliche pauschale Lieferstatusrecherche.

## Vorab festgelegte Skala
Methode portfolio-maturity-v1, ordinale Meilensteine, kein Leistungsindex:

| Stufe | Öffentlicher Nachweis |
|---|---|
| 1 Angekündigt | Konkretes Produkt/Programm offiziell angekündigt |
| 2 Prototyp | Funktionsfähiger Prototyp; Konzeptbild/Messemodell reicht nicht |
| 3 Test / Demo | Tatsächlich durchgeführte Tests oder Demonstration |
| 4 Kundenprogramm | Konkreter Kundenauftrag, Pilot oder beauftragte Validierung |
| 5 Im Betrieb | Tatsächlicher Einsatz in einer relevanten Kundenaufgabe |
| 6 Serie / Skala | Laufende Serienproduktion, wiederholte Auslieferung oder tatsächlich gelieferte Skalierung |

Höchste konkret gestützte Stufe verwenden. Geplante Tests, Lieferziele,
Bestellungen und Produktionskapazität sind kein erreichten Meilenstein.
Demonstrator, künftiges Kundenprodukt, Konfigurationen und Varianten getrennt
bewerten; Reife einer Plattform nicht auf neue Sensoren/Software übertragen.
Eine Behauptung des Herstellers bleibt als solche sichtbar, auch in Medien.
Eine Beleglücke beschreibt Rechercheabdeckung, nicht tatsächliche Unreife.

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
  "method_id": "portfolio-maturity-v1",
  "assessment_status": "bewertet",
  "score": 3,
  "statement": "…",
  "depends_on": ["P1"],
  "reasoning": "…",
  "method": "Höchster konkret belegter Meilenstein",
  "uncertainty": "…",
  "next_stage_limit": "Ein konkretes Kundenprogramm ist nicht belegt."
}
```

Nur direkte geprüfte Fakten als depends_on, Begründung normalerweise 2–3 Sätze.
Unbestimmbar: assessment_status="nicht eindeutig bestimmbar", score=null,
coverage_note mit konkreter Beleggrenze. Keine Null-/Ersatzstufe. Solche Einträge
können leere depends_on haben und tragen keine SWOT-Ableitung.
Andere Zusatzscores bleiben an assessment_methods des Vergleichsplans gebunden;
Capability-Matrix-Kriterien ergeben sich weiterhin aus dem Prüfauftrag.

## Review und Ausgabe
Basis-Reviewer prüft Produktidentität, Gruppe, Statusdatum und Claim-Zuordnung.
Final-Reviewer prüft I-Reifezuordnung samt Varianten-/Zeitbezug und Evidenzgrenze
in der bestehenden gemeinsamen Prüfrunde. Kein zusätzlicher Quellenprüfer.
Inventaränderungen invalidieren den Positionierungskontext. Alle freigegebenen
Einordnungen und Abhängigkeiten behalten Fingerprints und Schluss-Review.
--full verlangt aktuelle Produktzuordnung und eine freigegebene Einordnung pro
Produkt. Reine Fakten-HTML zeigt Produkte ohne interpretierte Reifestufe.
Details enthalten Fakten, Einordnung, Grenzen und direkte Originalbelege.
Aussageursprungsfilter nutzt vorhandene Claim-Arten; „Fakt“ behauptet keine
unabhängige Bestätigung. Keine Quellenklassifikation allein aus dem Publishernamen.
