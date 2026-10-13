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

## Ergänzung 13.10.2026: Dokumentbündel und kompakte Quellenprüfung

review-work.py bereitet zusätzlich zu unveränderten Fakten-/Bewertungskontexten
Dokumentbündel, aktuelle Originalbindungen und konservative Änderungsübersichten
vor. stamp-review.py --work expandiert ausschließlich explizite Gruppenentscheidungen
des Prüfers in vollständige Einzelreviews. Fehlende Befunde bleiben offen.
Basis prüft weiterhin Auftragsabdeckung/module_views und sämtliche erforderlichen
A-Fakten; Schlussreview prüft alle neuen Ableitungen. Übernahme verlangt geprüfte
unveränderte Aussage, Original, Zuordnung und Abhängigkeiten im selben Lauf/Stichtag.

- 160 Unit-Tests bestanden: Dokumentbündel/Mehrfachbelege, explizite Entscheidungen,
  fehlende erforderliche Befunde, unbekannte/doppelte IDs, B-/Teilfreigabegrenzen,
  Originaländerungen bei gleichem Claim-Hash, Produkt-/Regions-/Peerzuordnungen,
  Elternfakten, aktuelle Dateien/Arbeitsblätter/Validierungen, vollständige I-/S-
  und Faktenentscheidungen, falsche erklärte Snapshots sowie Legacy-Kompatibilität.
- Vollständiger synthetischer CLI-Lauf mit 71 Fakten, fünf Dokumentbündeln und
  29 Interpretationen: 20 benötigte A-Grundlagen aus gebundenem Basisreview im
  Schlussreview ausdrücklich übernommen, alle 29 Ableitungen geprüft. Beide
  Agentenkontexte nach neuer Basisfreigabe identisch und HTML bytegleich zum
  vorigen Stand. Keine HTML-/CSS-/JS-Änderung; keine erneute Browserabnahme.
- Unabhängiger source-reviewer-Lauf aus anderem fiktiven Offline-Original:
  vollständiges Dokument gemeinsam gelesen, zwei Aussagen und Produktzuordnung
  bestätigt, falschen Auftragsstatus als Korrektur erkannt. Kompakter Entwurf
  erfolgreich expandiert, Gesamtstatus blockiert; keine blanket Freigabe.
- Python-Syntax und zwei geänderte Skills per quick_validate bestanden.

Keine echte Unternehmensquelle geöffnet oder freigegeben. Integrationsergebnisse
und Reviews simuliert; kein gemessener Modelltoken-/Kostenbenchmark. Die vorherige
Stichproben-/Fehlereskalationsmethode, Recherchebreite und Agentenkontexte bleiben.

## Ergänzung 13.10.2026: sichere Wiederaufnahme unterbrochener Läufe

resume-run.py speichert nur ausdrücklich abgeschlossene und erneut formal geprüfte
Schritte. Originalauftrag, vollständiges Manifest, Eingaben/Ausgaben, Original-/
Text-Snapshots, aktuelle Verträge und Abhängigkeiten bleiben gebunden. Reviews
müssen weiterhin mit explizitem Entwurf, Arbeitsblatt und aktueller Validierung
übereinstimmen; der Helfer erzeugt keine Freigabe. Dateiexistenz ist kein Abschluss.
Änderungen sperren betroffene Schritte/Folgeschritte, unabhängige Teile bleiben
verwendbar. Neue Firma, Scope oder Stichtag wird kein Fortsetzungslauf.

- 187 Unit-Tests bestanden, darunter 27 neue Wiederaufnahmetests: Unterbrechung,
  fehlende/partielle Dateien, veränderter Auftrag/Stichtag, Originaländerung/-verlust,
  beschädigter Zustand, alte oder fehlgeschlagene Quellenkontrolle, explizite
  Freigabebindung, Kontextänderung, veraltete HTML, Pflichtplan, unabhängige Zweige,
  Abhängigkeitszyklen, spätere Revalidierung bei früheren Modulverweisen, parallele
  Dateiveränderung, atomarer Schreibabbruch und beendeter Prozesslock.
- Vollständiger synthetischer Lauf mit 71 Fakten, fünf Originalen, 29 Ableitungen
  und elf Checkpoints erfolgreich wiederaufgenommen und nach Helferänderung erneut
  validiert. Positionierungs-/SWOT-Kontexte und HTML bytegleich zum vorherigen Stand.
  Alle Rollendefinitionen, Selektions-/Kontextlogik und HTML/CSS/JS unverändert;
  bestehende Inhalts-/Quellenreviews und Browser-/Druckabnahme bleiben Pflicht.
- Unabhängiger delegierter Offline-Fortsetzungslauf: verändertes Original sperrt
  alten Portfolio-/Paketstand. Faktenrolle korrigiert vergebenen Auftrag auf keinen
  Auftrag und geplanten Pilot, entfernt unbelegte Produktzuordnung/Publikationsdatum.
  Quellenprüfer prüft alle drei Aussagen vollständig A und gesamte Modulabdeckung;
  Basis ausdrücklich freigegeben. Auftrag/Manifest erhalten, frühere Artefakte
  gesichert. Zwischenzeitliche Vertragsänderung sperrt alte Checkpoints ebenfalls;
  unveränderte Dateien anschließend gezielt revalidiert.
- Quellenaufnahmen älter als 24 Stunden benötigen tatsächlichen Refresh/Neueröffnung.
  HTTP-Abruf wird vor Netzoperation als laufend markiert; Abbruch/Fehler lässt die
  Sperre stehen, Cache-Hit löscht sie nicht. Unveränderter erfolgreicher Abruf/304
  bewahrt Datenbindung. Syntax, vier Skills und Diff-Whitespace geprüft.

Alle Quellen/Prüfentscheidungen dieser Tests fiktiv bzw. simuliert; keine reale
Firmenrecherche oder gemessene Token-/Kostenersparnis. Checkpoints führen keine
Agenten aus, kürzen keine Kontexte und ersetzen keine inhaltliche/visuelle Prüfung.
