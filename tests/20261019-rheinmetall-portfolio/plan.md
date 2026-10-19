# Modultest: Rheinmetall – ausschließlich Portfolioanalyse

Originalanfrage: „erstelle nach dem auf github eine portfolioanalyse und nur diese. Möglichst ausführlich nach denKategorien die Rheinmetall auch auf seiner webseite hat“

Modus: `modultest`. Unternehmen: Rheinmetall AG und das öffentlich zuordenbare Produktportfolio der Gruppe. Stichtag: 2026-10-19. Sprache: Deutsch. Grundregion: global.

## Auswahl und Umfang

Ausgewählt ist ausschließlich **2a – Portfolio**. Diese kleinste passende Auswahl erfüllt die ausdrückliche Beschränkung auf eine Portfolioanalyse. Das Portfolio wird ausführlich entlang der Website-Oberkategorien **Land, Luft, See, Digitalisierung, Mobilität, Industrie, Ausbildung & Service** untersucht. Die tatsächliche Website-Struktur ist bei der Recherche zu prüfen und zu dokumentieren.

Je Kategorie werden wesentliche Unterkategorien, Produktfamilien, konkrete Systeme und Produkte, Anwendungen, technische Merkmale und öffentlich belegte Statusinformationen beschrieben. Herstellerangaben, belegte Tests, Aufträge, Lieferungen und Betrieb sind voneinander zu unterscheiden. Keine Reifegrad-Scores. Die Produktbreite ist transparent zu dokumentieren; eine unbelegte vollständige Erfassung sämtlicher Varianten darf nicht behauptet werden.

## Ausführungsliste

| Reihenfolge | Rolle | Eingaben | Zielpfad |
|---|---|---|---|
| 1 | Hauptagent, Auftragsnormalisierung | Originalanfrage und Delegation | `input/auftrag.md` – vorhanden |
| 2 | portfolio-analyst / portfolio-analysis, Schritt 2a | `input/auftrag.md`, dieser Plan, Repository-Verträge zur Portfolioanalyse, tatsächlich geöffnete öffentliche Originalseiten | `work/portfolio.md` |
| 3 | Hauptagent, Bereitstellung des einzigen Analysemoduls | `work/portfolio.md`; unveränderte analytische Aussagen und Quellen | `output/Rheinmetall_Portfolioanalyse.md` |
| 4 | Hauptagent, tatsächlichen Bearbeitungsstatus dokumentieren | Auftrag, Plan, Portfolio und durchgeführte Kontrollen | `output/abnahme.md` |

Die Bereitstellung als Markdown-Datei ist kein zusätzliches Recherchemodul und keine HTML-Ausgabephase 7. Keine inhaltliche Erweiterung durch den Hauptagenten.

## Nicht ausgewählte Schritte

**2b Struktur/Cluster, 3 Markt/Themen/Person, 4 Basis-Review und 7 HTML-Ausgabe sind nicht beauftragt.** Ebenso entfallen 5 SWOT und 6 Schluss-Review, die im Modultest ohnehin nicht vorgesehen sind. Kein Wettbewerbskapitel, keine Marktanalyse und kein Personenprofil ergänzen. Ein formales Review darf weder durchgeführt noch als bestanden ausgewiesen werden; Ergebnis als Recherche ohne gesondertes Basis-Review kennzeichnen. Die Quellenpflicht und Verantwortung für erkennbare Fehler bleiben bestehen.

## Dateizuordnung und Isolation

Delegiertes Testverzeichnis: `/workspace/scratch/ce13351cb638/rheinmetall-portfolio/`. Dieser ausdrücklich delegierte Pfad ersetzt für diesen Lauf die sonstigen Standardpfade. Alle Laufdateien bleiben innerhalb dieses Verzeichnisses.

- `input/auftrag.md`: vorhandener, für diesen Test erstellter Auftrag; verbindliche Normalisierung der Nutzeranfrage.
- `plan.md`: dieser Ablaufplan; einzige Datei des module-contractor.
- `work/portfolio.md`: ausschließlich Ergebnis des Portfolio-Spezialisten einschließlich Claim-Nachweisen, Quellenregister und Datenlücken.
- `output/Rheinmetall_Portfolioanalyse.md`: Nutzerfassung ausschließlich dieser Portfolioanalyse.
- `output/abnahme.md`: tatsächlicher Status; Review und HTML-Kontrollen als nicht beauftragt führen.

Kein Fortsetzungslauf und keine Übernahme älterer Unternehmensclaims. Vorhandene Repository-Anweisungen dienen als Arbeitsvertrag, nicht als Quelle für Unternehmensfakten.

## Voraussetzungen und Ergebnisstatus

Status: **geplant**. Auftrag und erforderliche Planungsreferenzen wurden gelesen. Keine bekannte blockierende Mehrdeutigkeit.

Vor der Analyse sind die Portfolio-Fachverträge zu lesen. Recherche beginnt bei `https://www.rheinmetall.com/de/produkte/uebersicht`; relevante Originalseiten müssen tatsächlich geöffnet werden. Wesentliche Claims erhalten Claim-ID, Aussageursprung, direkten Beleg, Quellen-/Veröffentlichungsdatum oder „o. D.“, Abrufdatum, konkrete Belegstelle und Unsicherheit. Quellenmetadaten können über eindeutige Quellen-IDs im Register aufgelöst werden. Quellenzugriffslücken und Unterschiede zwischen Produktbeschreibung und nachgewiesenem Realisierungsstatus offen ausweisen.

Die im Repository genannten Claude-Modelle sind hier nicht verfügbar. Ausführung mit verfügbarem Modell gemäß Hauptdelegation; keine Sonnet-Ausführung behaupten. Weitere Agentenaufrufe durch den module-contractor sind ausgeschlossen.

Offene Punkte: tatsächliche Website-Kategorien und Unterstruktur bestätigen, Quellenzugänglichkeit und erreichbare Produktabdeckung während 2a feststellen. Falls Pflichtkategorien nicht recherchierbar sind, Status teilweise bzw. blockiert mit konkreter Lücke ausweisen.
