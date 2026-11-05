---
name: briefing-leitpruefung
description: Entscheidet für ein Firmenbriefing je Aussage über die Freigabe, in Phase basis über die Fakten und in Phase final über Positionierung und SWOT. Baut auf den Befunden der Dokumentprüfung auf.
---

# Leitprüfung

## Anschlüsse

| | Datei |
|---|---|
| Eingang | `leitpruefung-eingabe.json` aus W2: Phase, gebündelte Dokumentbefunde, Prüfpaket mit Aussagen, Quellen und Darstellungszuordnungen; in Phase final zusätzlich Positionierung, SWOT, ihre Kontexte und Übernahmekandidaten |
| Ausgang | `leitentscheid.json` |

## Phase basis

- Dokumentbefunde je Aussage zusammenführen. Ein positiver Befund zu einer
  Quelle genügt nicht für eine Aussage mit weiteren Quellen.
- Quellkonflikte, Abdeckung des Auftrags und alle Darstellungszuordnungen
  (`module_views`) fachlich prüfen: Labels, Kurztitel und Vorschauen, Produkt-,
  Akteurs-, Länder- und Themenzuordnung, Ereignisdatum und Vier-Monats-Fenster.
- Portfolio deckt alle wesentlichen Geschäftsfelder ab; Nutzerthemen dürfen die
  Breite nicht verengen.
- Person: Identität, aktuelle Rolle, Chronologie, Medien-Timeline; eine
  Ankündigung ist kein Amtsantritt.
- Netzwerk: Richtung, Kapitalanteil versus Kontrolle, aktueller versus
  historischer Status. Gemeinsame Kunden oder Verbände beweisen keine Kooperation.
- Fokusseiten: Neutralität, Kennzahlentyp und Scope, Vergleichbarkeit,
  Akteursauswahl, Meetingfragen.
- Nach vollständiger Prüfung `scope_and_mappings_checked: true`.

## Phase final

- Jede Positionierungs- und SWOT-Aussage (I-, S-IDs) vollständig prüfen:
  Ableitung aus aktuellen A-Fakten, passendes Kriterium und Skalenanker,
  Aussageursprung, Messbedingungen, Unsicherheit.
- Kurztitel und Vorschauen der Summary, Highlights (Einheit, Bezug, Zeitraum,
  Ziel versus Ist), Matrixzellen, Produktreife und Präsenzstufen mitprüfen.
  Eine Matrix-Lücke ist keine Schwäche; SWOT intern/extern richtig zuordnen.
- Unveränderte geprüfte Fakten aus den Übernahmekandidaten ausdrücklich in
  `reuse_fact_ids`; neu zu prüfende Fakten in `fact_groups` entscheiden.

## Für beide Phasen

- Keine pauschale erneute Quellenlektüre; nur bei unklaren Befunden gezielt
  die Quelle öffnen. Dokumentbefunde nicht still überschreiben.
- `status` je Aussage: geprüft / übernommen / nicht einzeln geprüft /
  Korrektur / offen. B-Details ohne Einzelprüfung: „nicht einzeln geprüft“.
- Bei Korrektur oder offen: `reason`, `action`, `owner`. Owner ist genau der
  zuständige Baustein: `context`, `portfolio`, `cluster`, `market`,
  `focus:<id>`, `positioning` oder `swot`. Daran geht die Aussage zurück.
- Gesamtstatus `freigegeben` nur ohne `material_errors` und ohne offene A-Aussage.

## Ausgabedatei

Kopf aus der Eingabe übernehmen: `schema_version: 1`, `run_id`, `company`,
`as_of`, `phase`. Prüfsummen ergänzt W3.

```json
{
  "status": "freigegeben | teilweise | blockiert",
  "review_scope": "tatsächlich geprüfter Umfang",
  "material_errors": [{"claim_ids": ["…"], "reason": "…", "action": "…", "owner": "…"}],
  "scope_and_mappings_checked": true,
  "review_groups": [{"claim_ids": ["…"], "depth": "A", "status": "geprüft", "note": "…"}],
  "reuse_fact_ids": [],
  "fact_groups": []
}
```

`reuse_fact_ids` und `fact_groups` nur in Phase final. In `review_groups` nur
wirklich gleichlautende Befunde bündeln und jede ID ausdrücklich nennen.

Regeln im Detail: `quellenpruefung.md`, `parallele-quellenpruefung.md`,
`pruefauftraege.md`, `interpretationsphase.md` und die Darstellungsregeln
(im Skill-Paket unter `references/`).
