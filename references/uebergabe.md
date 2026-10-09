# Gemeinsames Übergabeschema
## Kopf jeder Moduldatei
Unternehmen, Unternehmensgrenze, Stichtag, Region/Umfang.
Status: vollständig / teilweise / blockiert. Fehlende Eingaben konkret nennen.

## Ergebnisse
Kompakte Modultabelle und 3 bis 5 belegte Kernaussagen.
Jede wesentliche Aussage einzeln als Claim dokumentieren:
Claim-ID | Aussage | Fakt/Interpretation | belegte Faktenbasis
| Quellenname | Originaltitel | Veröffentlichungsdatum/o. D.
| Ereignisdatum sofern relevant | Direktlink | Abrufdatum
| Belegstelle als kurze Paraphrase | Unsicherheit.
Bei Interpretationen nachvollziehbar von Fakten zur Einordnung argumentieren.

## Abschluss
Offene Datenlücken, Widersprüche und ihre Auswirkung nennen.
Rückgabe an Hauptagent: Pfad, Bearbeitungsstatus, Kernergebnisse, offene Punkte.
Kein vollständiges Ergebnis behaupten, wenn Pflichtteile fehlen.

## Ergänzung für Cluster-Claims
Netzwerkdaten und Rechercheabdeckung folgen references/cluster-recherche.md.
Bei Geschäftsberichten zusätzlich Geschäftsjahr, Seite/Abschnitt und Bezugs-
zeitpunkt erfassen; PDF-Seite und gedruckte Seite bei Abweichung unterscheiden.
Direkte Beziehung, indirekter belegter Pfad und bloße Überschneidung trennen.
Gemeinsame Knoten-/Kanten-IDs ermöglichen nachvollziehbare Querverweise im HTML.

Für die automatische Netzwerkübernahme in Schritt 7 zusätzlich im Cluster-Modul
network-data-JSON nach references/netzwerk-html.md liefern. Seine Quellen-/Claim-
Referenzen müssen mit der lesbaren Recherche und dem Quellenregister übereinstimmen.

## Kompakte Übergabe an die Quellenprüfung
Jede Recherche-Rolle ergänzt pro Claim einen kurzen Belegauszug ODER eine
präzise Paraphrase (eindeutig kennzeichnen), mit Seite/Abschnitt/Absatz und
Quellen-ID. Nur die nötige Belegstelle, keine vollständigen Artikel kopieren.
Unsicherheit, abhängige Claim-IDs, vorgeschlagene Prüftiefe A/B und Grund
mitgeben. Der Prüfer legt die tatsächliche Prüftiefe fest.
Quellenmetadaten einmal in einem Register ablegen, im Claim per ID referenzieren.
Bestehende Claim-Pflichtfelder bleiben erhalten; Werte müssen nicht mehrfach
ausgeschrieben werden, wenn sie eindeutig über Quellen-ID auflösbar sind.
Hauptagent übergibt nur benötigte Claim-/Quellentabellen, Netzwerkdaten,
bisheriges Review und Änderungsübersicht. Nach Korrekturen: geänderte Claim-IDs,
geänderte Quellen und abhängige Aussagen nennen. Keine vollständige Neufassung
unveränderter Recherche an den Prüfer senden.
Arbeitsmethode und Freigaberegeln: references/quellenpruefung.md.

### Temporäres Prüfpaket für mechanische Kontrollen
Hauptagent stellt JSON im aktuellen work-/Modultest-Verzeichnis bereit:
company, as_of (YYYY-MM-DD), sources, claims und optional network.
sources: id, name, title, url, published_date (YYYY-MM-DD oder null),
accessed_date (YYYY-MM-DD); weitere Quellenmetadaten dürfen enthalten sein.
claims: id (bestehende Claim-ID), statement, evidence (gekennzeichneter kurzer
Auszug oder Paraphrase), location, uncertainty (auch leer), source_ids;
optional depends_on (Claim-IDs), proposed_depth und depth_reason.
network: bestehendes vollständiges network-data-JSON; Quellenmetadaten müssen
mit den gleichnamigen Einträgen im Prüfpaket übereinstimmen.
Claim-Fingerprints aus dem Prüfskript im Review festhalten; sie unterstützen
Änderungserkennung, ersetzen aber keine Inhaltsprüfung oder Aktualitätskontrolle.
Kein zusätzliches dauerhaftes Analysten-Ergebnis oder neues Pflichtmodul.

## Faktenphase v2
Bei ausdrücklichem mode=facts-v2 gilt references/faktenphase.md für Format/Pfade:
kompakte JSON-Fakten statt paralleler Markdown-Berichte. Quellenprüfung bleibt
quellenpruefung.md; Interpretation folgt erst nach geprüfter Faktenbasis.
Capability-Vergleichsplan und reine Beobachtungen nach capability-matrix.md.
