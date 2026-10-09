# Schritt 2: gemeinsames Daten- und Übergabeformat
Status: Faktenrollen in Schritt 3 für den Modus facts-v2 angeschlossen.
Aufruf, isolierte Pfade und Validierung nach faktenphase.md; neue Faktenaufträge
nutzen facts-briefing. Interpretation/HTML und gemeinsamer Dokumentcache folgen
später. Bestehende HTML-Aufträge behalten vorerst die alten Modulpfade nach
uebergabe.md. Keine Mischläufe oder zwei konkurrierenden Faktenbestände.

## Zielstruktur und Rollen
Layoutreferenz: vom Nutzer bereitgestellte vollständige Briefing-HTML.
Inhalte pro Auftrag neu recherchieren. Keine Horváth-/Beratungsangebote-Kapitel,
kein eigenes Unternehmens-Deep-Dive-Kapitel wie QTI.
Relevante JV-/Tochterdaten bleiben als Fakten im Cluster/Portfolio erlaubt.
Abschnitte: Executive Summary, Timeline, Cluster Map, Portfolio/Produktreife,
Wettbewerbsvergleich, SWOT, optional berufliches Personenprofil, themenbezogene
regionale Marktanalyse, Quellenregister.
Faktenrollen: Unternehmens-/Kontextrecherche, Portfolio, Cluster, Markt.
Interpretationsrollen: Positionierung und SWOT. Hauptagent koordiniert und rendert.
Schlanke Quellenprüfung nach quellenpruefung.md zwischen den Phasen beibehalten.

## Vier getrennte Datenarten
1. Quellenregister: Metadaten und konkrete Dokumentidentität, keine Bewertung.
2. Fakten-Claims: Aussagen mit präziser Evidenz und Unsicherheit, keine Scores.
3. Review: tatsächlicher Prüfstatus je Claim/Version, getrennt von Analystenaussage.
4. Interpretationen: Aussage, Methode, Faktenbasis und Einschränkungen.
Ein Dokument einmal registrieren, mehrere Claims darauf referenzieren.
Jeder Fakt einmal maßgeblich speichern; andere Module nutzen Claim-ID statt
eine zweite abweichende Faktfassung anzulegen. Jede wesentliche Interpretation
muss auf geprüfte Fakten zurückführbar sein.

## Geplante Aufteilung und Schreibrechte
| Zielpfad (erst beim Anschluss aktivieren) | Inhalt | Schreiber |
|---|---|---|
| work/sources.json | konsolidiertes Quellenregister | Hauptagent |
| work/context-facts.json | Firmenbasis, Ereignisse, berufliches Profil | Kontextrecherche |
| work/portfolio-facts.json | Produkte, Eigenschaften, belegter Einsatzstatus | Portfolio-Agent |
| work/cluster-facts.json | Akteure, Beziehungen, Netzwerkdaten | Cluster-Agent |
| work/market-facts.json | Länder, Programme, Markt-/Wettbewerbsdaten | Markt-Agent |
| work/positioning.json | Reifegrad, Präsenzbewertung, Positionierung | Positionierungs-Agent |
| work/swot.json | begründete SWOT-Punkte | SWOT-Agent |
| work/review-basis.md, work/review-final.md | Prüfbefunde nach bestehender Methode | Quellenprüfer |

Jedes JSON-Modul: schema_version, run_id, company, as_of, scope, status, claims,
gaps; fachliche Produkt-/Akteurs-/Beziehungstabellen zusätzlich, wenn nötig.
status: vollständig / teilweise / blockiert. Nicht beauftragte Module entfallen.
Agenten schlagen neue Quellen in ihrem eigenen Modul unter source_proposals vor.
Nur Hauptagent konsolidiert das gemeinsame Register; keine parallelen Schreibzugriffe.
Quellen-IDs deterministisch aus der Dokument-URL, etwa S- plus SHA256-Präfix;
Kollisionen erkennen. Eindeutige Dokument-URL einschließlich bedeutungstragender
Query-Parameter erhalten; Belegseiten/Absätze als location, nicht als eigenes Dokument.
Verschiedene Veröffentlichungen mit identischem PM-Text getrennt registrieren,
aber mittels origin_source_id als gemeinsame Ursprungsevidenz kennzeichnen.
Fakten-IDs mit bestehendem P-/C-/M-/T-/H-Präfix erhalten; IDs im Lauf stabil.
Interpretationen I-Claims, SWOT S-Claims. Korrekturen ändern Version/Fingerprint,
nicht stillschweigend die Identität. Bei gleichem Fakt Zuständigkeit vereinbaren
und anderen Modulen diese Claim-ID übergeben; keine allein textbasierte Blind-Deduplikation.

## Quellenfelder
id, name, title, url, published_date, accessed_date, source_kind.
published_date: YYYY-MM-DD oder null; accessed_date: tatsächliches Abrufdatum.
source_kind nach cluster-quellenkatalog.md, etwa Herstellerangabe, Partnerangabe
oder Sekundärquelle. Optional report_year, page, section, origin_source_id.
Dokument-Version/Abrufzustand festhalten, sobald Quelleninhalte zwischengespeichert
werden. Kein Datum erfinden; geöffnete Quellen und reine Fundhinweise unterscheiden.
Nur tatsächlich gelesene Belegstellen als Evidenz verwenden.

## Faktenfelder
id, statement, kind, source_ids, evidence, location, uncertainty.
kind: Fakt / Herstellerangabe / Partnerangabe / Nutzerangabe.
Nutzerangabe ist keine geprüfte öffentliche Evidenz; vor Nutzung entsprechend behandeln.
evidence: kurzer gekennzeichneter Auszug oder genaue Paraphrase.
location: Seite/Abschnitt/Absatz; bei PDF abweichende Druck-/PDF-Seite kennzeichnen.
Bei mehreren Quellen zusätzlich evidence_items mit source_id, text, mode,
location; jeden Beleg der richtigen Quelle zuordnen. Nur nötige Auszüge speichern.
Optionale Felder: event_date, valid_from/valid_to, event_status, depends_on,
proposed_depth, depth_reason. Datums-/Statusangaben nur soweit belegbar.
Fact/Interpretation nicht anhand sprachlicher Sicherheit vermischen:
"Auftrag angekündigt", "Lieferung berichtet" sind belegbare Statusaussagen;
"starke Position" oder ein Reifegradscore gehören zu Interpretationen.
Rechercheabdeckung/Fundliste getrennt von belegten Claims speichern.
Lieferstatus beim ersten Quellenlesen erfassen, Aussageursprung sichtbar lassen.
Keine separate routinemäßige Bestätigungsrecherche oder Prüfschleife pro Lieferung.
Vollprüfung nur bei entscheidungstragender Verwendung oder Widersprüchen,
gebündelt mit der Quellenprüfung nach quellenpruefung.md; sonst B-Hintergrunddetail.
Bloß berichtete Lieferung nicht als unabhängig bestätigten Vollzug ausgeben.

## Interpretationsfelder und Freigabe
id, statement, section, depends_on, reasoning, method, uncertainty.
depends_on enthält bestehende Fakten- und ggf. bereits geprüfte I-Claim-IDs.
reasoning erklärt die Ableitung; method nennt vorab definierte Kriterien.
Bewertungen wie Produktreife oder regionale Präsenzskalen nur hier berechnen.
Ein Score braucht methodisch passende Evidenz; fehlende Belege nicht als
schlechte tatsächliche Leistung ausgeben.
Positionierung startet nach freigegebener Faktenbasis, SWOT danach mit geprüften
Fakten und nachvollziehbaren Positionierungsbefunden.
Jede wesentliche strategische Faktenbasis muss vollständig (A) geprüft sein.
B-Stichprobenclaims vor solcher Verwendung gezielt nach A hochstufen lassen.
Interpretationsrollen führen keine eigene allgemeine Recherche durch.
Konkrete Lücken an Faktenrolle zurückgeben; neue Fakten erneut prüfen.
Geänderte Fakten invalidieren betroffene Bewertungen/Schlussfolgerungen.
Quellenprüfer bewertet Ableitungen, nicht nur die Existenz ihrer Referenzen.

## Tokenbegrenzung bei Übergaben
- Metadaten einmal speichern, per Quellen-ID referenzieren.
- Hauptagent stellt pro Rolle nur passende Claim-/Quellenauszüge und benötigte
  Abdeckung bereit; niemand liest automatisch sämtliche JSON-Dateien.
- Kurzstatus an Hauptagent: Pfad, Status, zentrale Claim-IDs, offene Fragen.
  Keine vollständigen Berichte nochmals im Chat ausschreiben.
- Bereits im selben Lauf gelesene Dokumente/Belegstellen gemeinsam nutzen.
  Ein Cache muss beim Anschluss tatsächlich implementiert werden; ein JSON-
  Register allein verhindert noch keine doppelten Abrufe.
- Belege nach Bedarf öffnen; keine Volltexte sämtlicher Quellen in jeden Kontext laden.
  Bei neuen Abschnitten, Quellenänderungen oder Aktualitätsbedarf erneut abrufen.
- Vorhandene A-Prüfbefunde im selben Auftrag/Stichtag wiederverwenden.
  Hintergrunddetails nicht als vollständig geprüft deklarieren.
- Keine pauschale Suchobergrenze, die die vereinbarte breite Recherche beschneidet.
- Renderer erhält strukturierte Daten und geprüfte Kurztexte. Lange Markdown-
  Berichte UND JSON mit identischem Inhalt nicht dauerhaft parallel erzeugen.

## Anschluss an bestehende Komponenten
network-data bleibt Schema v1 nach netzwerk-html.md; kein inkompatibles neues
Graphschema erfinden. Fakten referenzieren vorhandene Knoten-/Kanten- und Claim-IDs.
Vorlagen rendern Tatsachen und Interpretationen mit sichtbarer Trennung.
Das bestehende scripts/check-review-data.py erwartet company/as_of, sources,
claims und optional network. Bei späterem Anschluss aus Fakten-/Quellenregistern
ein temporäres Paket erzeugen; evidence/location bleiben dort Strings, zusätzliche
evidence_items werden eindeutig als Quellenauszüge/Belegstellen zusammengeführt.
Interpretergebnisse separat gegen depends_on prüfen; das aktuelle Skript prüft
noch keine komplette Interpretation oder alle neuen Modulfelder.
Kein Prüfschritt als bestanden ausgeben, bevor Adapter/Validierung implementiert sind.

## Nächster Umsetzungsschritt
Faktenrollen/Skills sind für facts-v2 angeschlossen. Als Nächstes Interpretation,
Koordination/Cache und Renderer anschließen; begrenzte Konfigurations-/Fixturetests
ersetzen keinen tatsächlichen Recherchelauf. Reihenfolge mit Nutzer
schrittweise bearbeiten. Umstellung alter Pfade und Archivierung einmal konsistent
durchführen, keine Mischläufe. Tests müssen Scope-Ausschlüsse, Trennung der Phasen,
Claim-/Quellenintegrität und tatsächliche Token-/Aufwandsmessung berücksichtigen.
