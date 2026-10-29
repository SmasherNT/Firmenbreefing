# Dokumentprüfung Phase basis, Runde 2 (nach Korrekturrunde 1)

Lauf: runs/knds-portfolio-status-2026-10-29 (Repositorywurzel /home/user/Firmenbreefing)
Splitplan: work/review-split-basis-r2.json · Arbeitsblatt: work/review-work-basis-r2.json
Paket: work/review-packet.json · Manifest: input/facts-run.json · Cache: work/document-cache
Konfiguration laut Plan: claude-sonnet-5-5, effort medium.
Änderungsübersicht (lokal erzeugt, keine Prüfentscheidung): work/r2-changes.json
(changed_claims, changed_source_snapshots, changed_product_rows, round1_open_or_correction).
Runde-1-Dokumentbefunde: work/review-basis-part-{1,2,3}.json (anderer Job-Zuschnitt;
Befund je source_id/claim_id dort nachschlagen). Runde-1-Leitbefunde: work/r1/review-basis-lead-draft.json.

Lies references/parallele-quellenpruefung.md und references/quellenpruefung.md.
Jobansicht: python3 scripts/review-shards.py show --plan work/review-split-basis-r2.json
--work work/review-work-basis-r2.json --facts work/review-packet.json --job <Job> (in Datei umleiten).

Regeln dieser Runde (CLAUDE.md: unveränderte bestätigte Fakten desselben Laufs/Stichtags
übernehmen; geänderte Claims, Belege und Abhängigkeiten gezielt erneut prüfen):
- Claim NICHT in changed_claims UND Quelle NICHT in changed_source_snapshots UND Runde-1-
  Befund für genau dieses Quelle/Claim-Paar = „geprüft“ (depth A): ausdrücklich als
  „geprüft“ übernehmen, note: „Unverändert seit Runde 1 (Claim und Snapshot identisch);
  Befund aus review-basis-part-N übernommen“. Keine erneute Lektüre nötig. Stichprobe:
  mindestens 3 solcher Paare je Job tatsächlich erneut im Original lesen und in note vermerken.
- Alle übrigen Paare (geänderter Claim, neuer Snapshot oder Runde-1-Befund Korrektur/offen):
  Original vollständig an der Belegstelle lesen und neu entscheiden (A-Prüfung).
- Für jedes zugewiesene Dokument/Claim-Paar genau ein expliziter Befund; Fingerprints aus show.
- Keine Freigabe. Bei Korrektur/offen reason, action, owner.
- gzip-/PDF-Cachetexte bei Bedarf aus gespeicherten Originalbytes dekodieren und dokumentieren.
