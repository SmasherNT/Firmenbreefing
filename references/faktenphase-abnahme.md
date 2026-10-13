# Faktenphase v2: Konfigurationsabnahme
Stand: 2026-10-09. Konfiguration und lokaler Dokumenttest, keine Firmenrecherche.
- Fünf Skill-Metadaten geprüft: portfolio-analysis, cluster-analysis,
  company-context, market-facts, facts-briefing.
- 12 automatisierte Tests für prepare-facts.py bestanden: Quellen-/Claimverweise,
  Firmen-/Laufidentität, Phasentrennung, dynamische Kriterien, Versionen, Quellen-
  Zuordnung, CLI-Ausgabe und Zurückweisung von Scores.
- market-facts mit zwei ausdrücklich fiktiven bereitgestellten Produktblättern
  ausgeführt: sechs Fakten und sechs Beobachtungen nach branchenspezifischem Plan.
  Keine Scores, keine externe Recherche; Herstellerangaben und abweichende
  Messbedingungen benannt. Formaler Prüflauf ohne Fehler, status=teilweise.
- Kein vollständiger Claude-Mehragentenlauf und keine öffentliche Quellenprüfung.
- Kontext/Portfolio/Cluster nicht einzeln in tatsächlicher Firmenrecherche getestet.
- Kein Token-/Kostenbenchmark; keine Aussage über gemessene Einsparungen.
- Faktenphase separat nutzbar; Interpretation, gemeinsamer Dokumentcache und
  HTML-Anschluss bleiben nächste Umsetzungsschritte. Bisherige HTML-Aufträge
  verwenden weiterhin den bisherigen Ablauf.

## Ergänzung 13.10.2026: Dokumentcache und gemeinsame Fakten

Laufbezogener Cache nach recherche-wiederverwendung.md, vollständige Original-
snapshots und mechanisch abgeleitete Texte, atomare Speicherung und Dokumentlocks.
Gemeinsamer Faktenindex mit unveränderten vollständigen Claims/Eigentümerrollen;
Duplikate nur als Kandidaten, Wiederverwendung über IDs ohne automatische Freigabe.
CLAUDE.md bündelt zentrale Regeln und verweist auf die bestehenden Fachverträge.
Fakten-/Positionierungs-/SWOT-Kontexte, Modellwahl, Rechercheumfang und Prüftiefe
bleiben erhalten. prepare-facts.py schreibt den Index als zusätzliche Suchhilfe.

- 142 Unit-Tests bestanden: unter anderem vier parallele Cacheabrufe mit genau
  einem Download, HTTP-304, neue Originalversion bei Inhaltsänderung, Erhalt alter
  Originale/Texte, Refresh-Fehler ohne Aktualitätsfreigabe, Hashfehler, Firmen-/Lauf-
  /Stichtagstrennung, Query-/Fragmentidentität, dynamische Seiten und PDF-Fallback.
- Faktenindex: vollständige Claims unverändert, Eigentümerrolle, mögliche
  Doppelungen, offene Rollen, Quellenkonflikte, keine Nutzerangaben/Scores als
  Fakten, aktualisierte Module und Änderungen während Indexbau blockieren Reuse.
  CLI-Konsolidierung ergänzt ausschließlich den Index; Paket/Fingerprints identisch.
- Bestehender vollständiger Offline-Beispiellauf erneut generiert: Faktenpaket,
  Positionierungs-/SWOT-Kontexte, Interpretationen, beide simulierten Reviews und
  HTML bytegleich zum vorherigen Stand. Keine neue Browserabnahme nötig, da keine
  HTML-/CSS-/JS-Änderung. Python-Syntax und geänderter facts-briefing-Skill gültig.
- Unabhängiger market-facts-Lauf mit anderen fiktiven Offline-Dokumenten und
  bestehendem Portfolio: Quelle aus gemeinsamem Cache tatsächlich gelesen,
  Produktionsclaim unter seiner P-ID wiederverwendet, nur neuer Programmclaim
  als M angelegt. Ankündigung bleibt ohne Auftrag/Auslieferung; Herstellerursprung,
  fehlende Behördenbestätigung und offene Programmwerte erhalten. Gemeinsames
  Paket mit zwei Claims/einer Quelle formal fehlerfrei, kein realer Quellenreview.

Cache-Zähler messen Dokumentoperationen, keine Modelltoken. Kein tatsächlicher
Token-/Kostenbenchmark oder Qualitätsvergleich realer Firmenrecherchen durchgeführt.
Alle Beispiel-/Forward-Quellen und Reviewer-Urteile bleiben fiktiv/simuliert.
