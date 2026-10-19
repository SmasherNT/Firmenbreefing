# Quellenprüfung in Dokumentbündeln – gleiches Modell

Standard für neue v2-Prüfungen ab 19.10.2026. Keine Änderung an Rechercheumfang,
A/B-Prüftiefe, Fakten-/Interpretationskontexten oder Freigabebarrieren.
Alle Dokumentprüfer und der Leitprüfer nutzen dasselbe Modell wie der Hauptagent:
`model: inherit`, kein günstigeres Ersatzmodell und kein automatischer Modellwechsel.

## Zuständigkeit

- Hauptagent erzeugt wie bisher das validierte review-work-Arbeitsblatt.
- `source-document-reviewer` wird für bis zu drei Dokumentjobs instanziiert.
  Standard `--workers 3`; bei zwei Dokumenten zwei Jobs, bei einem ein Job.
  Kein Job ohne tatsächlich zu lesende Quellen; bei reinem Fakten-Reuse keine.
- Jede Quelle gehört exakt einem Job, einschließlich aller ihr zugeordneten
  derzeit zu prüfenden Claims über Modulgrenzen hinweg. Nicht nach Fachmodul teilen.
  Arbeitslast wird deterministisch nach Größe der Claim-Datensätze verteilt;
  `load_chars` ist ein Verteilungsindikator, keine gemessene Tokenzahl.
- Die Dokumentprüfer arbeiten parallel in getrennten Kontexten und Dateien.
  Sie prüfen Quelle → Aussage und melden eigene Befunde, erteilen keine Freigabe.
- Der bestehende `source-reviewer` übernimmt anschließend die Leitprüfung:
  Quervergleich mehrerer Quellen, gesamte module_views/Abdeckung und Zuordnungen,
  A/B-Auswahl, Fehlereskalation und finale Claim-/Freigabeentscheidungen.
  In Phase final zusätzlich sämtliche neuen/geänderten I-/S-Ableitungen prüfen.
  Keine vollständige erneute Quellenlektüre als Standard; Konflikte und nötigen
  Kontext gezielt öffnen. Quellenkorrekturen zuerst an zuständigen Dokumentjob
  bzw. Faktenrolle zurückgeben; keine widersprechenden Befunde still überschreiben.

## Vorbereitung und fokussierte Eingaben

Nach `review-work.py prepare`:

```bash
python3 scripts/review-shards.py split --work <review-work.json> --facts <review-packet.json> --workers 3 --out <review-split.json>
python3 scripts/review-shards.py show --plan <review-split.json> --work <review-work.json> --facts <review-packet.json> --job sources-1
```

Alle Jobs aus jobs[] delegieren, nicht pauschal drei leere Agenten starten.
Delegation nennt konkreten Auftrag/Phase, Plan-/Arbeitsblatt-/Paketpfade, Job-ID,
Cachepfad, denselben Modellstand und genau einen eigenen Ausgabepfad.
Dokumentprüfer lesen standardmäßig die Ausgabe von show, nicht das volle Paket.
Show enthält die eigenen Quellen, vollständige relevante Claims jeweils einmal,
A-Pflichten, passende Netzwerkkanten und Snapshotbindung. Andere Quellen eines
Mehrfachclaims bleiben in seinen Referenzen sichtbar, werden aber vom zugeordneten
Job geprüft. Ganze module_views bleiben erreichbar und werden vom Leitprüfer
semantisch geprüft; daraus entsteht keine Kürzung der globalen Prüfung.

Quellen an konkreten Belegstellen lesen, nötigen Kontext bei Zweifel erweitern.
Kein erfolgreiches Cache-fetch als gelesenen Beleg werten; vollständige Originale
bleiben zugänglich. Keine Modellzusammenfassung als Quellenoriginal verwenden.
Reine Download-, IDs-, Referenz- und Hashkontrollen bleiben lokale Skriptaufgaben.

## Dokumentbefunde

Je Job eine JSON-Datei, keine gemeinsamen Schreibzugriffe:

```json
{
  "schema_version": 1,
  "format": "review-source-part-v1",
  "run_id": "...", "company": "...", "as_of": "YYYY-MM-DD", "phase": "basis",
  "job_id": "sources-1",
  "review_work_fingerprint": "...", "plan_fingerprint": "...",
  "documents": [{
    "source_id": "S-...", "original_read": true,
    "note": "Tatsächlich gelesene Originalabschnitte und Zugriffsumfang.",
    "findings": [{
      "claim_id": "P1", "depth": "A", "status": "geprüft",
      "note": "Aussage samt Status/Zeitraum durch diese Quelle belegt."
    }]
  }]
}
```

Für jeden zugewiesenen Dokument/Claim-Paar genau einen ausdrücklichen Befund.
Status: geprüft / nicht einzeln geprüft / Korrektur / offen. Keine Übernahme oder
Gesamtfreigabe durch Dokumentprüfer. Bei Korrektur/offen zusätzlich reason, action,
owner nennen. Ohne gelesenen Originalbeleg keine geprüfte Entscheidung.
Nicht geprüfte B-Details ausdrücklich markieren; A-Pflichten bleiben vollständig.
Stichprobenfehler an Leitprüfer melden, Gruppeneskalation nach quellenpruefung.md.

## Einsammeln und Leitprüfung

```bash
python3 scripts/review-shards.py collect --plan <review-split.json> --work <review-work.json> --facts <review-packet.json> --parts <part-1.json> <part-2.json> <part-3.json> --out <source-findings.json>
```

Nur tatsächlich vorhandene Jobs/Dateien übergeben; ohne Jobs `--parts` leer lassen.
Collect prüft Besitz/Abdeckung, fehlende/doppelte Dokumente und Claimbefunde,
Identität und Snapshotbindungen. Es bündelt alle Quellenbefunde je Claim, ohne
Abstimmung, Mehrheitsentscheid oder automatische Freigabe. Ein positiver Befund
zu einer Quelle genügt niemals für einen Claim mit weiteren Quellen. Bei
mehrteiliger Belegführung prüft jeder Job den dieser Quelle zugeordneten
evidence_item/Teilbeitrag und benennt dessen Umfang. Nicht jede einzelne Quelle
muss alle Teilbehauptungen tragen; die gemeinsame Tragfähigkeit prüft der Leitprüfer.

Leitprüfer erhält kompakte source-findings.json, Auftrag, aktuelle Arbeitsblatt-
und Eingabepfade, bisherige Reviews sowie nötige Modul-/Interpretationskontexte.
Er bestätigt scope_and_mappings_checked in Phase basis selbst nach vollständiger
semantischer Abdeckungs-/Zuordnungsprüfung. Jeder Claim erhält einen expliziten
Befund im bisherigen review_groups-/fact_groups-Format. Unveränderte zulässige
Übernahmen weiterhin explizit nennen; keine doppelte Quellenprüfung für Reuse.
Zusätzlich im Leitentwurf plan_fingerprint und source_collection_fingerprint exakt
angeben. Keine eigenen source_checks über die Dokumentbefunde schreiben.

```bash
python3 scripts/review-shards.py merge --plan <review-split.json> --work <review-work.json> --facts <review-packet.json> --parts <part-1.json> <part-2.json> <part-3.json> --lead <review-lead-draft.json> --validation <validation.json> --out <review-merged-draft.json>
python3 scripts/stamp-review.py --draft <review-merged-draft.json> --validation <validation.json> --work <review-work.json> --out <review-basis.md>
```

Merge übernimmt ausschließlich explizite Leitentscheidungen. Eine A-Freigabe muss
von A-geprüften Befunden aller zugeordneten Quellen getragen sein. Fehlende Jobs,
veraltete Daten, unaufgelöste Quellenprobleme oder fehlende globale Prüfurteile
blockieren Freigabe. Neue/änderte Befunde erzeugen einen neuen Collection-Fingerprint;
der Leitprüfer muss diesen erneut ausdrücklich berücksichtigen. Keine Dateiexistenz-
oder Erfolgsannahme. Stempel/Snapshotkontrollen ersetzen kein inhaltliches Urteil.

## Phase final, Wiederaufnahme und Grenzen

Gleiche Aufteilung in basis und final: In final nur facts_to_verify auf Dokumentjobs
verteilen. Geprüfte unveränderte Fakten weiter ausdrücklich übernehmen; bei null
Quellenjobs prüft nur der Leitprüfer Ableitungen und Reuse. Kein zweiter vollständiger
Basislauf. Neue Fakten weiter an die zuständige Rolle, Basisprüfung und betroffene
Ableitungen erneuern. Bestehende Zwei-Korrekturrunden-Regel bleibt erhalten.
Alte monolithische Reviews bleiben lesbar; neue Läufe nutzen diese Aufteilung.
Geänderte Arbeitsblätter verlangen neue Splitpläne und zugehörige Befunde.

Dies begrenzt Kontext pro Dokumentprüfer und erlaubt Parallelität. Eine geringere
Gesamttokenmenge oder Laufzeit ist ohne Messlauf nicht zugesichert. Abnahme nennt
Jobs, dasselbe Modell, echte Quellensichtungen, Leitprüfung und offene Grenzen.
