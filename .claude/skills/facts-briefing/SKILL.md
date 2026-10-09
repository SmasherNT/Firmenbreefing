---
name: facts-briefing
description: Steuere ausdrücklich beauftragte Faktenbasis- oder Faktenagenten-Tests mit bis zu vier Recherche-Rollen und schlankem Basis-Review in facts-v2. Keine vollständige HTML oder strategische Interpretation.
---

Lies references/faktenphase.md, defaults.md und bei Wettbewerb capability-matrix.md.
Einrichtung/Systemfragen sind keine Rechercheaufträge.
1. Delegierten Lauf verwenden; sonst isolierten Test tests/<run_id>/ mit Originalauftrag, Manifest und work/output
   anlegen. Firmenidentität/Stichtag normalisieren; nur beauftragte Rollen wählen.
2. Kontext, Portfolio und Cluster soweit ausgewählt delegieren, ggf. parallel.
   Eingaben, mode=facts-v2 und genau einen Ausgabeweg je Rolle nennen.
3. Vor Markt-/Wettbewerbsrecherche aus Auftrag und nötigen Identitäts-/Produktfakten
   comparison-plan.json festlegen. Kriterien/Skalen vor Bewertung definieren;
   keine festen Beispielspalten. Bei reinem Marktauftrag ohne Vergleich entfällt der Plan.
4. Markt-Agent mit Plan und nur relevanten vorhandenen Claim-Auszügen delegieren.
   Kontext/Portfolio/Cluster sind keine Pflicht für isolierten Marktauftrag.
5. sources/review-Paket lokal erzeugen:
   python3 scripts/prepare-facts.py --manifest <facts-run.json>
   --modules <ausgewählte Module...> --out <Lauf>/work
   Bei Vergleich zusätzlich --plan <comparison-plan.json> übergeben.
   Formale Fehler an zuständige Rollen; keine fremden Moduldateien umschreiben.
6. source-reviewer Phase basis mit Auftrag, review-packet.json, Abdeckung
   und ggf. Netzwerk delegieren. quellenpruefung.md beachten.
   mode=facts-v2 und Ziel <Lauf>/work/review-basis.md explizit nennen.
   Bei v2 maschinenlesbaren Reviewer-Entwurf nach quellenpruefung.md verlangen;
   Fingerprints mit stamp-review.py --draft <review-basis-draft.json>
   --validation <facts-validation.json> --out <review-basis.md> lokal ergänzen.
   Wesentliche Korrekturen gezielt zurückgeben und betroffene Claims erneut prüfen.
7. Abnahme unter <Lauf>/output/abnahme.md: aufgerufene Rollen, Faktenabdeckung,
   Mechanik, Inhalt, offene Lücken und nicht geprüfte Punkte nennen.
   Keine Bewertung/HTML implizit starten; Interpretation ist separat beauftragbar.
Vorhandene Läufe nicht überschreiben; neuer Lauf hat neue ID. Rückgabe kurz.
Bei Änderungen Manifest/Plan beibehalten oder versionieren; keine Mischstände.
