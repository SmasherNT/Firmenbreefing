---
name: facts-briefing
description: Steuere ausdrücklich beauftragte Faktenbasis- oder Faktenagenten-Tests mit bis zu vier Recherche-Rollen und schlankem Basis-Review in facts-v2. Keine vollständige HTML oder strategische Interpretation.
---

Lies references/faktenphase.md, defaults.md und bei Wettbewerb capability-matrix.md.
Einrichtung/Systemfragen sind keine Rechercheaufträge.
1. Delegierten Lauf verwenden; sonst isolierten Test tests/<run_id>/ mit Originalauftrag, Manifest und work/output
   anlegen. Firmenidentität/Stichtag normalisieren; nur beauftragte Rollen wählen.
   Dokumentcache nach references/recherche-wiederverwendung.md mit source-cache.py
   initialisieren; denselben laufbezogenen Pfad an Faktenrollen und Reviewer geben.
   Fehlenden Zustand nach references/lauf-wiederaufnahme.md initialisieren (isoliert
   --target facts); vorhandenen Zustand zuerst per resume prüfen. Nach fertigen Rollen,
   Plan, Paket und freigegebenem Basisreview lokale Checkpoints speichern.
2. Kontext, Portfolio und Cluster soweit ausgewählt delegieren, ggf. parallel.
   Eingaben, mode=facts-v2 und genau einen Ausgabeweg je Rolle nennen.
3. Vor Markt-/Wettbewerbsrecherche aus Auftrag und nötigen Identitäts-/Produktfakten
   comparison-plan.json festlegen. Kriterien/Skalen vor Bewertung definieren;
   keine festen Beispielspalten. Bei reinem Marktauftrag ohne Vergleich entfällt der Plan.
4. Markt-Agent mit Plan und nur relevanten vorhandenen Claim-Auszügen delegieren.
   Kontext/Portfolio/Cluster sind keine Pflicht für isolierten Marktauftrag.
   Nach fertigen Modulen und vor abhängigen Übergaben facts-index.json per
   fact-index.py bauen/erneuern; Rollen können vorhandene Claims über IDs nutzen.
   Bestehende Fakten-/Positionierungs-/SWOT-Kontexte unverändert übergeben.
5. sources/review-Paket lokal erzeugen:
   python3 scripts/prepare-facts.py --manifest <facts-run.json>
   --modules <ausgewählte Module...> --out <Lauf>/work
   Bei Vergleich zusätzlich --plan <comparison-plan.json> übergeben.
   Formale Fehler an zuständige Rollen; keine fremden Moduldateien umschreiben.
6. review-work.py prepare nach references/pruefauftraege.md ausführen.
   Quellenprüfung Phase basis nach references/parallele-quellenpruefung.md:
   review-shards.py split, Dokumentjobs parallel an source-document-reviewer
   mit model: inherit und getrennten Zielpfaden delegieren. Pro Job nur show-Ausgabe
   als Standardkontext; Auftrag und Originale bleiben erreichbar. Danach collect.
   source-reviewer desselben Modellstands als Leitprüfer mit Befunden, Abdeckung,
   gesamter module_views-/Netzwerkprüfung und exaktem Leitentwurfsziel delegieren.
   review-shards.py merge prüft Teilbefunde/Leitentscheidungen; Hauptagent erzeugt
   review-basis.md mit stamp-review.py --work aus dem zusammengeführten Entwurf.
   Keine eigene Gesamtfreigabe aus Dokumentbefunden ableiten. Wesentliche
   Korrekturen gezielt zurückgeben und betroffene Claims erneut prüfen.
7. Abnahme unter <Lauf>/output/abnahme.md: aufgerufene Rollen, Faktenabdeckung,
   Mechanik, Inhalt, offene Lücken und nicht geprüfte Punkte nennen.
   Keine Bewertung/HTML implizit starten; Interpretation ist separat beauftragbar.
Vorhandene Läufe nicht überschreiben; neuer Lauf hat neue ID. Rückgabe kurz.
Bei Änderungen Manifest/Plan beibehalten oder versionieren; keine Mischstände.

Für vollständige Briefings das unternehmensweite Portfolio und die spezifischen
Fach-/Markt-Deep-Dives nach references/themen-darstellung.md getrennt beauftragen.
Faktenrollen liefern topics.headline/preview als geprüfte Kurztexte.


Quellenprüfung verbindlich nach references/parallele-quellenpruefung.md:
Dokumentjobs (bis zu drei, gleiches Modell) → collect → Leitprüfung → merge →
bestehendes stamp-review.py --work. Keine reduzierte Prüftiefe oder Modellwechsel.
In final nur neu zu prüfende Faktenquellen verteilen, sonst ausschließlich Leitprüfung.
