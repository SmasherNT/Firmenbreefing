---
name: briefing-swot
description: Leitet für ein Firmenbriefing eine konkrete SWOT aus geprüften Fakten und der aktuellen Positionierung ab. Keine Recherche.
---

# SWOT

## Anschlüsse

| | Datei |
|---|---|
| Eingang | `swot-context.json` aus W4 (Positionierungsaussagen und ihre Fakten) |
| Ausgang | `swot.json` |
| Korrektur | `pruefergebnis.json` (owner `swot`) und die eigene bisherige Ausgabe |

## Regeln

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

## Ausgabedatei

Kopf: `schema_version: 1`, `mode: "interpret-v2"`, `role: "swot"`, `run_id`,
`company`, `as_of`, `scope` aus dem Kontext. Prüfsummen ergänzt W1 (final).

Je Punkt in `interpretations`: `id` (S1, S2 …), `category` (Strengths /
Weaknesses / Opportunities / Threats), `statement` (etwa ein Satz),
`section: "swot"`, `depends_on` (Fakten- oder I-IDs aus dem Kontext),
`reasoning` (meist 2–3 Sätze), `method`, `uncertainty`.

```json
{"status": "vollständig | teilweise | blockiert", "interpretations": [],
 "research_requests": [], "shared_limitations": []}
```

## Korrektur

Enthält `pruefergebnis.json` Einträge mit owner `swot`: genau diese Punkte
beheben, bestehende IDs behalten, Datei vollständig neu schreiben.

Regeln im Detail: `interpretationsphase.md` (im Skill-Paket unter `references/`).
