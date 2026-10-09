# Faktenphase v2: Vertrag und Durchführung
## Umfang
Aktiv nur bei ausdrücklich delegiertem mode=facts-v2 bzw. facts-briefing.
Die alten vollständigen HTML-/Modultestabläufe behalten ihre bisherigen Pfade.
Neue Faktenphase schreibt JSON statt paralleler Langberichte und produziert
keine finale HTML, Scores oder SWOT. Horváth-Kapitel und separate Firmen-
Deep-Dives entfallen. Fakten zu relevanten JV/Tochtergesellschaften bleiben erlaubt.
Faktenrecherche umfasst öffentliche Nachrichten/Fachmedien nach Quellenkatalog;
keine festen Beispielunternehmen, Daten oder Technologie-Kriterien übernehmen.

## Auftrag und Rollen
Hauptagent erstellt pro Lauf in tests/<run_id>/input/ den Originalauftrag und
facts-run.json. Kein input/auftrag.md des alten Ablaufs überschreiben.
Manifest: schema_version=1, mode="facts-v2", run_id, company, as_of (YYYY-MM-DD),
scope (nicht leer), selected_roles (nicht leere Liste aus context/portfolio/cluster/market).
Optional Person, Themen, Regionen und comparison_plan_path.
Ohne Firmen-/Teilauftrag keine Recherche beginnen. Nur ausgewählte Rollen starten.
Delegation nennt Auftrag, Manifest, erlaubte Eingaben und genau einen Zielpfad.
Nur eigenes Modul schreiben; gemeinsamen Quellenbestand nicht parallel ändern.

| Rolle | Agent / Skill | Ziel unter <Lauf>/work/ | Claim-Präfix |
|---|---|---|---|
| context | company-context-analyst / company-context | context-facts.json | T-/H- |
| portfolio | portfolio-analyst / portfolio-analysis | portfolio-facts.json | P- |
| cluster | cluster-analyst / cluster-analysis | cluster-facts.json | C- |
| market | market-facts-analyst / market-facts | market-facts.json | M- |

## JSON-Modul (verbindlich)
schema_version=1, mode="facts-v2", role, run_id, company, as_of, scope, status,
claims (Liste), source_proposals (Liste), gaps (Liste), coverage (Liste).
status: vollständig / teilweise / blockiert. Keine vollständige Arbeit behaupten
bei offenen Pflichtsuchwegen. Ein vollständig bearbeiteter Suchumfang kann
dokumentierte öffentliche Datenlücken enthalten.
Claims: id, statement, kind, source_ids, evidence, location, uncertainty.
kind: Fakt / Herstellerangabe / Partnerangabe / Nutzerangabe.
Gemeinsame Grenzen einmal unter shared_limitations/document_scope nennen.
Je Claim uncertainty nur auf konkrete zusätzliche Unsicherheit begrenzen;
allgemeine Quellen-/Scope-Hinweise nicht in jedem Claim/Beobachtung wiederholen.
prepare-facts übernimmt diese Modulhinweise in module_context des Prüfpakets.
Aussageursprung im Satz sichtbar machen; Zuschreibung ist kein unabhängiger Vollzugsbeleg.
Nutzerangaben ohne öffentlichen Beleg unter gaps/coverage führen, nicht als
öffentlich belegte Ergebnis-Claims übernehmen.
evidence: kurzer ausdrücklich als Auszug oder Paraphrase gekennzeichneter Text;
location: konkrete Seite/Abschnitt/Absatz. Mehrere Quellen: evidence_items
mit source_id, text, mode (Auszug/Paraphrase), location.
Optional depends_on, proposed_depth=A/B, depth_reason, event_date, event_status.
Keine I-/S-Claims, Bewertungsfelder, Rankings oder SWOT in Faktenmodulen.
Produkt-/Akteurs-/Länder-/Ereignistabellen dürfen bestehende Claim-IDs referenzieren.
reuse_claim_ids benennt Fakten anderer ausgewählter Module; nicht deren Text duplizieren.
Ein Link/Snippet allein ist keine Evidenz. Lieferstatus einmal beim Lesen erfassen;
Prüftiefe nach quellenpruefung.md, keine routinemäßige eigene Liefer-Prüfschleife.

source_proposals: id, name, title, url, published_date (Datum oder null),
accessed_date (Datum), source_kind; optional report_year/page/section/origin_source_id.
IDs erzeugen: python3 scripts/prepare-facts.py --source-id '<Dokument-URL>'.
S- + erste 16 SHA256-Zeichen der URL ohne Fragment; Query-Parameter erhalten.
Belegfragmente in location festhalten. Vorhandene gleiche Quelle wiederverwenden;
unterschiedliche PM-Kopien bleiben getrennte Dokumente mit gemeinsamer Ursprungsevidenz.
coverage je Suchweg: Thema/Akteur, Suchbegriffe, geöffnete Quellen-IDs, Befund,
Status (geprüft mit/ohne Beleg, nicht zugänglich, nicht geprüft mit Grund).
Fundhinweise und nicht gelesene Dokumente bleiben gaps/coverage, keine Quellenbelege.

## Technologie & Industrie: klare Zuständigkeit
Cluster: wer entwickelt/liefert/lizenziert/integriert/fertigt/serviceleistet mit wem?
Subsysteme, Plattformen, Software/KI, Schnittstellen, Produktions- und Projektpartner,
Länder, Rollenverteilung und belegte Umsetzung; Querverbindungen über JV hinaus.
Markt: vergleichbare technische/industrielle Angebote der Wettbewerber, Tests,
Integrationsmodelle, Einsatzbedingungen, Kundenprogramme und Fertigungsevidenz.
Portfolio: Eigenschaften/Status der Zielprodukte, ohne Reifegradeinordnung.
Gleiche Fakten über Claim-IDs weitergeben, nicht mehrfach neu recherchieren.
Gemeinsames Projekt/Kompatibilität ist kein unbelegter bilateraler Vertrag.

## Cluster-Daten
Cluster liefert zusätzlich actors, relationships, report_log und network
nach Schema v1 aus netzwerk-html.md; keine eigene HTML.
network enthält nur die dokumentierten C-Claims. Quellenmetadaten müssen mit
source_proposals bzw. mitgegebenem Quellenregister übereinstimmen.
Kanten-interpretation, Relevanzscores und analytische Gewichtung in dieser Phase
weglassen. cluster/focus sind nur belegte Hauptfunktion/redaktionelle Erstansicht,
keine strategische Bewertung. Noch nicht geprüftes Netzwerk nicht als freigegeben ausgeben.
Die Recherche-/Berichtspflichten aus cluster-recherche.md bleiben bestehen;
dessen Markdown-Ergebnisstruktur und Analysteninterpretation werden in diesem
Modus durch JSON/Faktenbegrenzung ersetzt.

## Zusammenführung und Prüfung
Hauptagent führt vorhandene Module mit scripts/prepare-facts.py zusammen.
Formale Fehler an verantwortliche Rolle zurückgeben; keine fremden Dateien umschreiben.
Nach fehlerfreiem Lauf: sources.json (gemeinsame Metadaten), review-packet.json
(temporäre Prüfeingabe) und facts-validation.json (mechanische Befunde).
Ein Paket enthält nur die ausgewählten Module dieses Laufes; kein Fremdfirmen-Reuse.
Es ersetzt weder Inhaltsprüfung noch Cache. Vorhandene Quellen/Belegstellen
gezielt wiederverwenden; vollständiger Dokumentcache folgt später.
source-reviewer Phase basis erhält Auftrag, Paket und nur nötige Abdeckung/Netzwerk.
Interpretation darf erst nach tatsächlicher Freigabe starten.
Für anschließende interpret-v2-Läufe maschinenlesbares Basis-Review nach
quellenpruefung.md schreiben. facts-validation.json enthält Laufidentität,
phase=basis und required_full_review_ids für eingezeichnete Netzwerkkanten.
Reviewer entscheidet inhaltlich; stamp-review.py übernimmt nur Fingerprints.
Nach zwei erfolglosen Korrekturrunden wesentlicher Fehler blockieren.
Abnahme unterscheidet formale Prüfung, Inhaltsprüfung, Abdeckung und nicht geprüft.

## Kompatibilität und Rückgabe
Keine JSON-Claims automatisch in alte .md-Pfade kopieren. Legacy-HTML/Skills
nicht mit v2-Dateien mischen; Anschluss der Ausgabe erfolgt im nächsten Schritt.
Rückgabe nur Pfad, Status, Kernergebnis-IDs und offene Fragen, keine Langberichtkopie.
Das Vorbereitungsskript meldet nur Fehler/Zähler; Fingerprints bleiben in der
facts-validation.json, damit lange Erfolgslisten keinen Toolkontext verbrauchen.
