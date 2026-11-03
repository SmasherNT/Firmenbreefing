# Abnahme der Cowork-Kopie

Prüfdatum: 03.11.2026. Ausgangsstand:
37e562341e619b1587c03d749896b951184df26d.
Art: Migration, lokale Regression und synthetischer Offline-Vergleich.
Kein importierter Cowork-Workflow, keine echte Firmenrecherche.

| Prüfpunkt | Tatsächliches Ergebnis |
|---|---|
| Isolation | Ausschließlich neuer Unterordner copilot-cowork/; vorhandene Projektdateien unverändert. Keine alten Aufträge, Caches, Checkpoints oder Ergebnisdateien übernommen. |
| Rollen und Methoden | Zehn Rollenverträge in roles/, zwölf Methoden unter skills/. Keine nativen Agentenregistrierungen behauptet. |
| Anbieterabhängige Steuerung | AGENTS.md, runtime/settings.json und portable Modellpolicy ersetzen den alten Einstieg und feste Anbieter-Modelle. Effort ist Wunsch, Ausführung separat nachzuweisen. |
| Wiederaufnahme | Bindet AGENTS.md, Hostvertrag, Modellpolicy, zutreffende Rollen/Methoden und beide Reviewer-Verträge ein. Fehlende Pflichtdateien werden abgewiesen. |
| Python-Regression | 244 Tests erfolgreich: python3 -m unittest discover -s tests -p 'test_*.py'. Enthält acht neue Migrationstests sowie die angepassten bestehenden Tests. |
| Selbstständige Uploads | Zwölf reproduzierbare .skill-Uploads lokal gebaut und geprüft; je zwei Begleitdateien. SHA-256-Prüfung, Pfadschutz, Wiederverwendung derselben Runtime und Schutz geänderter Dateien getestet. |
| Extrahierte Laufzeit | prepare-facts.py, render-briefing.py und resume-run.py aus unabhängig entpackter Laufzeit ohne Repository-Elternpfade importiert. |
| HTML-Vergleich | Gleiche synthetische Daten erzeugen im Original und in der Kopie byte-identische HTML (357382 Bytes; SHA-256 bb20b8213b343673a9ceb2433dbc8d39f66bc815fa906fd40dec8fd83245119b). |
| Vorlagen | Alle zwölf HTML-, CSS- und JavaScript-Vorlagen byte-identisch zum Ausgangsstand. |
| Laufzeitprobe lokal | Python 3.12, Dateizugriff, fcntl, Node.js, playwright-core und pdftotext vorhanden. Chromium nicht verfügbar; deshalb Browser-/Drucktests nicht ausgeführt. |
| Grenzen korrekt blockiert | Strikter Preflight liefert Exitcode 2 ohne tatsächliche Hostnachweise für Quellenzugriff und unabhängige Kontexte; zusätzliche Browserlücke separat ausgewiesen. |

## Noch im tatsächlichen Cowork-Mandanten nachzuweisen

- Import einschließlich Zugriff auf Begleitarchive und Python-Ausführung.
- Quellenabruf, unabhängige Autoren-/Reviewer-Kontexte und eigener Kontext je Fokus.
- Vollständiger Firmenauftrag mit zwei neutralen Themen, Quellenfreigaben und Wiederaufnahme.
- Browserinteraktionen, Druckansicht und dauerhafte Sicherung im vorgesehenen Ziel.

Fehlende Hostfähigkeiten müssen bereitgestellt werden, gegebenenfalls über einen
externen Worker/Connector. Rollen-Dateien und Skill-Uploads ersetzen diese
Integration nicht. Der lokale Vergleich ist keine Cowork-End-to-End-Abnahme.
Historische *-abnahme.md-Berichte dokumentieren frühere Entwicklung; sie sind
keine aktuelle Laufzeitfreigabe.
