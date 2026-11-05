---
name: briefing-auftrag
description: Macht aus einer Firmenbriefing-Anfrage einen eindeutigen Auftrag (auftrag.md, facts-run.json) und legt vor jeder Recherche den Vergleichsplan (comparison-plan.json) fest. Recherchiert keine Inhalte.
---

# Auftrag

## Anschlüsse

| | Datei | Inhalt |
|---|---|---|
| Eingang | `anfrage.txt` | Originalnachricht; erste Zeile optional `modus: voll` oder `modus: kurz` |
| Ausgang | `auftrag.md` | Originalnachricht und normalisierte Felder |
| Ausgang | `facts-run.json` | Manifest des Laufs |
| Ausgang | `comparison-plan.json` | Vergleichsplan (nur Modus voll; bei kurz nicht schreiben) |
| Korrektur | `pruefergebnis.json` | Einträge mit owner `auftrag` |

## Arbeitsweise

Websuche nur, um die Firma eindeutig zu identifizieren: offizieller Name,
offizielle Website, Unternehmensgruppe. Keine inhaltliche Recherche.

1. Modus aus der ersten Zeile, sonst aus der Nachricht („kurz“, „Kurzbriefing“,
   „schnell“ = kurz), sonst voll.
2. Firma, Themen und genannte berufliche Gesprächspartner übernehmen. Themen in
   Nutzerreihenfolge. Nichts hinzuerfinden. Fehlende Themen oder Personen sind
   kein Grund zur Rückfrage.
3. Standardwerte: Sprache Deutsch; Zielgruppe Top-Management und
   Gesprächsvorbereitung; Grundblick global; Quellen öffentlich, möglichst primär,
   passend zum Stichtag; Stichtag = heutiges Datum (YYYY-MM-DD).
4. Allgemeine Unternehmensthemen → `topics` mit `page: "main"`.
   Separate Themen-, Länder- oder Marktüberblicke → `focus_pages`, je Thema
   `{id, label, briefing_type: "topic_market"}`; id nur A–Z, a–z, 0–9, _ und -.
   Ohne Fokusthema `focus_pages: []`.
5. Person nur, wenn genannt: als String „Name · Rolle laut Nutzer“, mehrere in
   Nutzerreihenfolge. Status: Nutzerangabe, noch nicht verifiziert.
6. Rollen: voll → `["context","portfolio","cluster","market"]`;
   kurz → `["context","portfolio"]`, `focus_pages: []`, kein Vergleichsplan.

## Vergleichsplan (nur voll)

Vor jeder Wettbewerbsrecherche aus der Fragestellung festlegen, nicht aus
gewünschten Ergebnissen:

- `comparison_unit`: konkretes Produkt, System oder Angebot mit Einsatzkontext,
  nicht pauschal der Konzern. Ohne Thema die Kerngeschäftseinheit begründet wählen.
- `purpose`, `peer_groups` (Gruppen nach vergleichbarer Rolle, keine Rangliste).
- `criteria`: etwa 5–7. Bei Produkt- und Systemvergleichen überwiegend technische
  Dimensionen, ergänzt um „Belegter Beschaffungs- und Einsatzstand“ und
  „Industrielle Fertigungs- und Lieferfähigkeit“. Keine branchenfremden Spalten.
  Je Kriterium `id, label, question, evidence_required, display_type`
  (Profil / Kennzahl / Evidenzstufe), `applicability, rationale`.
  Kennzahl zusätzlich `unit`, `conditions`. Evidenzstufe zusätzlich vorab
  definierte `anchors`, z. B. `{"1": "...", "2": "..."}`.
- `version: 1`, dazu `run_id`, `company`, `as_of` wie im Manifest.

## Dateiformate

`facts-run.json`:

```json
{
  "schema_version": 1, "mode": "facts-v2",
  "run_id": "<firma-kurz>-<YYYYMMDD>", "company": "...", "as_of": "YYYY-MM-DD",
  "scope": "Unternehmensgrenze und Umfang in einem Satz",
  "selected_roles": ["context", "portfolio", "cluster", "market"],
  "topics": [{"id": "...", "label": "...", "page": "main"}],
  "focus_pages": [{"id": "...", "label": "...", "briefing_type": "topic_market"}],
  "person": "Name · Rolle laut Nutzer"
}
```

`person` weglassen, wenn niemand genannt ist.

`auftrag.md`: Originalnachricht unverändert, darunter die Felder Unternehmen,
offizielle Website, Unternehmensgrenze, Stichtag, Sprache, Zielgruppe,
Grundregion, Themen, Fokusthemen, Gesprächspartner, Position laut Nutzer,
Verifizierungsstatus, Pflichtmodule, Ausgabeziel, Quellenstandard.

## Korrektur

Enthält `pruefergebnis.json` Einträge mit owner `auftrag`, die eigenen Dateien
lesen, genau diese Punkte beheben und alle drei Dateien vollständig neu schreiben.
