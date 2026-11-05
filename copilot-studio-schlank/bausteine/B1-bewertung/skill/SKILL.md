---
name: schlank-bewertung
description: Leitet für ein Firmenbriefing aus den Fakten die Positionierung (schritt positioning) bzw. die SWOT (schritt swot) ab. Keine Recherche. Variante ohne Prüfagenten.
---

# Bewertung (Positionierung, SWOT)

## Parameter `schritt`

| schritt | liest | schreibt |
|---|---|---|
| `positioning` | `positioning-context.json` | `positioning.json` |
| `swot` | `swot-context.json` | `swot.json` |

In dieser Variante gibt es keine Schlussprüfung durch einen Prüfagenten.
Leite jede Aussage deshalb streng aus den Fakten im Kontext ab und nenne
Grenzen konkret. Das Briefing wird als ungeprüfter Entwurf gekennzeichnet.

## schritt `positioning`

### Anschlüsse

| | Datei |
|---|---|
| Eingang | `positioning-context.json` aus W1 (ausgewählte A-Fakten, Vergleichsplan, Produktinventar, Präsenzbelege, Modulauszüge) |
| Ausgang | `positioning.json` |
| Korrektur | `pruefergebnis.json` (owner `positioning`) und die eigene bisherige Ausgabe |

### Grundregeln

- Keine Recherche, keine neuen Fakten, Zahlen oder Quellen.
- Jede Aussage stützt sich über `depends_on` auf aktuelle, vollständig geprüfte
  Fakten aus dem Kontext. Fakten in `pending_checks` sind keine Grundlage.
- `statement` etwa ein Satz, `reasoning` meist 2–3 Sätze, `method` kurz,
  `uncertainty` nur konkrete Zusatzgrenze. Allgemeine Grenzen einmal in
  `shared_limitations`.

### Inhalte (`interpretations`, je `id` I…, `statement`, `section`, `depends_on`, `reasoning`, `method`, `uncertainty`)

1. **Executive Summary:** 4–6 Kernaussagen, `section: "executive_summary"`,
   mit `headline`, `preview`, `display_order`, nach Bedeutung geordnet.
2. **Highlights:** drei, `section: "executive_highlights"`,
   `type: "summary_highlight"`, `highlight_kind` metric oder status,
   `label` (max. 60), `value` (max. 40), `scope_label` (max. 80),
   `period` (max. 60), `display_order`. Zahl, Einheit, Bezug, Zeitraum aus den
   Fakten; Herstellerziel, Prognose, Obergrenze sichtbar kennzeichnen. Keine
   eigenen Zählungen. Fehlen Fakten: weniger Highlights, `status: teilweise`.
3. **Capability Matrix:** je Peer und Kriterium genau eine Zelle,
   `type: "matrix_cell"`, `peer_id`, `criterion_id`, `cell_status`
   (bewertet / nicht öffentlich belegt / nicht anwendbar / weitere Faktenprüfung
   nötig), `value`, `headline` (max. 48), `preview` (max. 80). Profil: Text;
   Kennzahl: belegter Wert; Evidenzstufe: genau ein `anchors`-Schlüssel. Höchste
   belegte Stufe begründen, `next_stage_limit` erklären. Nicht belegt ist keine
   fehlende Fähigkeit (`value: null`, `coverage_note`). Keine Gesamtrangliste.
4. **Produktreife:** je Produkt genau eine Einordnung,
   `type: "product_maturity"`, `product_id`, `method_id` aus dem Kontext,
   `section: "portfolio"`, `score` 1–6 (1 angekündigt, 2 Prototyp, 3 Test/Demo,
   4 Kundenprogramm, 5 im Betrieb, 6 Serie/Skala) oder `null` mit
   `assessment_status: "nicht eindeutig bestimmbar"` und `coverage_note`.
   Kapazitätsziel ist keine Serie.
5. **Regionale Präsenz:** je Region genau eine Einordnung,
   `type: "regional_presence"`, `region_id`, `method_id` und `section` aus dem
   Kontext, `score` 1–5 nach der Skala im Kontext oder `null`. Angekündigte
   Standorte und Kundenprogramme sind keine eigene operative Präsenz.
6. **Themen:** `section: "topic:<id>"` mit `headline` und `preview`.
7. **Modul-Insights:** je Modul Portfolio, Cluster, Markt 1–3 Karten,
   `type: "module_insight"`, `section: "module_insights"`, `module`,
   `display_order`, `headline`, `fact_text`, `fact_claim_ids`, `statement`.
   Ohne belastbaren Punkt `module_insight_gaps` mit Begründung.

Fehlende wesentliche Daten als `research_requests`
`[{id, target_role, question, related_claim_ids, blocking}]`; `target_role` ist
context, portfolio, cluster oder market.

### Ausgabedatei

Kopf: `schema_version: 1`, `mode: "interpret-v2"`, `role: "positioning"`,
`run_id`, `company`, `as_of`, `scope` aus dem Kontext. Prüfsummen ergänzt der Werkzeug-Agent.

```json
{"status": "vollständig | teilweise | blockiert", "interpretations": [],
 "research_requests": [], "shared_limitations": []}
```

### Korrektur

Enthält `pruefergebnis.json` Einträge mit owner `positioning`: genau diese
Punkte beheben, bestehende IDs behalten, Datei vollständig neu schreiben.

Regeln im Detail: `interpretationsphase.md`, `capability-matrix.md`,
`executive-summary.md`, `portfolio-darstellung.md`, `regionale-praesenz.md`,
`modul-keyfacts.md`, `themen-darstellung.md` (im Skill-Paket unter `references/`).

## schritt `swot`

### Anschlüsse

| | Datei |
|---|---|
| Eingang | `swot-context.json` aus W1 (Positionierungsaussagen und ihre Fakten) |
| Ausgang | `swot.json` |
| Korrektur | `pruefergebnis.json` (owner `swot`) und die eigene bisherige Ausgabe |

### Regeln

- Keine Recherche, keine neuen Fakten, Zahlen oder Quellen.
- Strengths und Weaknesses: bestehende interne Fähigkeiten und Grenzen.
  Opportunities und Threats: externe Chancen und Risiken.
- Standardmäßig drei eigenständige, belegte Punkte je Quadrant, höchstens drei.
  Weniger nur, wenn die Faktenbasis keinen sinnvollen Punkt trägt; die Grenze
  dann knapp in `shared_limitations`. Keine Füllpunkte, keine Aufteilung
  derselben Aussage.
- Eine Datenlücke ist keine Schwäche. Ein Produktmerkmal ohne begründeten
  Vorteil ist keine Stärke. Status, Konzern- oder Produktbezug und Zeitbezug
  erhalten. Unbewertete Matrix-Lücken und `pending_checks` tragen keine SWOT.
- Fehlende entscheidende Daten als `research_requests`
  `[{id, target_role, question, related_claim_ids, blocking}]`.

### Ausgabedatei

Kopf: `schema_version: 1`, `mode: "interpret-v2"`, `role: "swot"`, `run_id`,
`company`, `as_of`, `scope` aus dem Kontext. Prüfsummen ergänzt der Werkzeug-Agent.

Je Punkt in `interpretations`: `id` (S1, S2 …), `category` (Strengths /
Weaknesses / Opportunities / Threats), `statement` (etwa ein Satz),
`section: "swot"`, `depends_on` (Fakten- oder I-IDs aus dem Kontext),
`reasoning` (meist 2–3 Sätze), `method`, `uncertainty`.

```json
{"status": "vollständig | teilweise | blockiert", "interpretations": [],
 "research_requests": [], "shared_limitations": []}
```

### Korrektur

Enthält `pruefergebnis.json` Einträge mit owner `swot`: genau diese Punkte
beheben, bestehende IDs behalten, Datei vollständig neu schreiben.

Regeln im Detail: `interpretationsphase.md` (im Skill-Paket unter `references/`).
