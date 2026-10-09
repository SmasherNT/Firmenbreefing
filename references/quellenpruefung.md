# Sparsame Quellenprüfung
## Ziel und Eingaben
Verbindlich für Schritt 4 (basis) und Schritt 6 (final), auch in Modultests.
Rechercheumfang bleibt unverändert; eingespart werden doppelte Quellenabrufe,
unnötige Kontextübergaben und wiederholte Prüfungen unveränderter Fakten.
Hauptagent übergibt Auftrag, kompakte Claim-/Quellentabellen nach uebergabe.md,
Netzwerkdaten soweit beauftragt, vorhandene Review-Datei und Änderungsübersicht.
Keine finale HTML und keine vollständigen Quelltexte als Standard-Prüfkontext.
Moduldateien/Originaldokumente nur für benötigte Details gezielt nachlesen.
Fehlende Eingaben konkret zurückgeben; keine vollständige Neurecherche durchführen.

## Prüftiefe durch den Prüfer bestimmen
Recherche-Rollen schlagen Prüftiefe und Grund vor; Prüfer entscheidet unabhängig.
A: Vollprüfung im geöffneten Beleg für jede entscheidungsrelevante Aussage:
Eigentum/Kontrolle, wesentliche Finanzierung oder Kundenaufträge, zentrale
Kooperationen, Personenidentität/aktuelle Rolle, Kennzahlen der Management-
Zusammenfassung, strittige oder widersprüchliche Angaben, nur sekundär belegte
wesentliche Beziehungen und Fakten, auf denen SWOT/strategische Empfehlungen beruhen.
Alle eingezeichneten Netzwerkkanten: Identitäten, Richtung, Beziehungstyp,
Status/Zeitraum, Produktbezug sowie dargestellte Quoten/Kontrolle im Beleg prüfen.
Indirekte Pfade: jede Teilkante. Mehrere Claims derselben Quelle gebündelt prüfen.
Ein relevanter Quellenbeleg genügt nicht automatisch für alle Claims derselben Quelle.

B: Stichprobe nur für nicht entscheidungstragende ergänzende Hintergrunddetails.
Gruppen nach Modul UND Quelle UND Aussageart bilden; unsichere Aussagen nach A.
Je Gruppe mindestens ein Claim; bei mehreren Claims etwa 20 Prozent aufgerundet,
einschließlich einer Zahl/Datumsangabe, falls vorhanden, und unterschiedlicher
Belegstellen soweit möglich. Auswahl und Grund dokumentieren.
Jeder inhaltliche Fehler in einer Stichprobe führt zur Vollprüfung der Gruppe
und Prüfung abhängiger Aussagen. Nicht geprüfte Claims ausdrücklich als
"nicht einzeln geprüft (Stichprobe)" markieren, niemals als geprüft ausgeben.
Aussagen, die später eine Schlussfolgerung tragen, vor Freigabe nach A hochstufen.
Reine Interpretationen auf belegte Fakten und nachvollziehbare Ableitung prüfen;
kein Originalbeleg kann die Analysteninterpretation selbst als Fakt bestätigen.

## Lieferstatus ohne separate Prüfschleife
Recherche-Rolle erfasst beim ersten Lesen den ausdrücklich genannten Status
und den Aussageursprung: angekündigt / beauftragt / Lieferung berichtet /
Auslieferung belegt, jeweils nur soweit die Quelle dies tatsächlich trägt.
Keine automatische Zusatzrecherche zur unabhängigen Bestätigung jeder Lieferangabe.
Bei Herstellerangabe sichtbar "Lieferung laut Hersteller berichtet" verwenden;
das bestätigt den Inhalt der Meldung, nicht unabhängig den tatsächlichen Vollzug.
Lieferstatus vollständig (A) im selben Quellenaufruf prüfen, wenn er Produktreife,
regionale Präsenz, eine zentrale Kundenbeziehung, einen Netzwerk-Beziehungsstatus
oder eine andere wesentliche Bewertung trägt, oder Angaben widersprüchlich sind.
Keine eigene Delegation, neue Prüfrunde oder breit angelegte Zweitrecherche allein
für diesen Status. Gezielt nachrecherchieren nur, wenn eine wesentliche Aussage
sonst unklar/falsch wäre; alternativ Unsicherheit zeigen und Bewertung begrenzen.
Nicht entscheidungstragende Lieferdetails nach B behandeln; erneute Prüfung nur
bei Änderung, Stichprobenfehler oder späterer Nutzung als wesentliche Faktenbasis.
Die Pflichtprüfung aller Netzwerkkanten bleibt bestehen, wird aber je Quelle
mit den übrigen Beziehungsmerkmalen gebündelt.

## Mechanische Prüfungen auslagern
scripts/check-review-data.py prüft ein temporäres JSON-Prüfpaket lokal mit Python 3:
Pflichtfelder, IDs, Quellen-/Claimreferenzen, Datumsformate, identisches company/as_of
im Netzwerk, Zielknoten und Endpunkte. Es erzeugt auch stabile Claim-Fingerprints.
Es prüft weder Erreichbarkeit noch Quelleninhalt, Unabhängigkeit oder Wahrheit.
Paket aus bestehenden Daten erzeugen, keine zusätzliche Recherche durchführen.
Aufruf: python3 scripts/check-review-data.py <pruefpaket.json>
Exit 0: formale Kontrollen bestanden; Exit 1: Fehler; Exit 2: ungültige Eingabe.
Ohne Python/Bash entsprechende formale Kontrollen manuell durchführen und benennen.
Bevor Inhalte geprüft werden, formale Fehler gebündelt an zuständige Rolle melden.
Temporäres Paket im vorhandenen work-/Modultest-Verzeichnis, keine neue Pflicht-
Ergebnisdatei; Analysten schreiben weiterhin nur zugewiesene Moduldateien.

## Quellen einmal lesen, Befunde mehrfach verwenden
Claims nach Quellen-ID gruppieren. Benötigte Abschnitte in einem Quellenabruf
prüfen; für jeden Claim dennoch eindeutige Belegstelle und Ergebnis speichern.
Vorhandene Auszüge und im aktuellen Lauf geöffnete Dokumente nutzen.
Für A Originaldokument oder redaktionellen Artikel selbst kontrollieren;
Analystenparaphrase und Suchsnippet ersetzen die Kontrolle nicht.
Neue Abrufe nur bei fehlendem Abschnitt, unlesbarem Dokument, Widerspruch,
geändertem Beleg oder Aktualitätsbedarf. Zugriffsgrenzen offen ausweisen.

## Änderungen und Schritt 6
Wiederverwendung ausschließlich innerhalb desselben Firmenauftrags und Stichtags.
Unveränderte bereits vollständig geprüfte Claims mit unveränderten Belegen
übernehmen; Fingerprint plus Quellen-/Belegzustand und Prüftiefe abgleichen.
Fingerprint allein beweist keinen unveränderten Webseiteninhalt.
Neue/geänderte Claims, Quellen, Zahlen, Status und Unsicherheiten erneut prüfen.
Änderung einer Quelle betrifft alle zugehörigen Claims; fachliche Änderungen
betreffen zusätzlich abhängige Interpretationen und SWOT-Punkte.
Schritt 6 liest Basis-Review, SWOT und Änderungsübersicht; keine Wiederholung
der gesamten Faktenprüfung. Jede SWOT-Ableitung auf ihre Claim-Abhängigkeiten
prüfen. B-Claims als Grundlage erst nach A-Prüfung freigeben.
Keine Wiederverwendung über neue Firmenaufträge oder neue Stichtage hinweg.

## Kompakter Review-Bericht
Kopf: Firma/Stichtag, Phase, Gesamtstatus und tatsächlich geprüfter Umfang.
Kompakte Statustabelle: Claim-ID | A/B | geprüft/Stichprobe/offen/Korrektur |
Fingerprint | Belegstelle/Quelle bzw. Verweis auf bisheriges Review.
Bei B die nicht einzeln geprüften IDs explizit nennen; keine blanket Freigabe.
Nur Fehler/offene Punkte ausführlich: Claim-ID, Grund, nötige Änderung, Rolle.
Keine Wiederholung aller Aussagen oder Quelltexte im Bericht.
Dokumentiere Stichprobengruppen/Auswahl und Erweiterungen, Quellenabrufgruppen,
wiederverwendete Prüfergebnisse und offene wesentliche Fehler.
Datenlücken und nicht geprüfte Hintergrunddetails sind keine bestätigten Fakten.
Keine finale Freigabe mit offenen wesentlichen Fehlern oder ungeprüften A-Claims.

## Maschinenlesbares Review im v2-Lauf
facts-v2/interpret-v2 verwenden einen kompakten JSON-Review-Entwurf mit
schema_version=1, run_id, company, as_of, phase=basis/final,
status=freigegeben/teilweise/blockiert, material_errors (Liste), claims (Liste).
Je Claim id, depth=A/B und expliziter status=geprüft/übernommen/
nicht einzeln geprüft/Korrektur/offen. Tatsächlichen Prüfumfang, Quellenabrufe,
Belegstellen oder Verweis auf vorherigen Befund und Stichproben dokumentieren.
Nur Fehler mit reason/action/owner ausführlich. Kein mechanischer Erfolg als
Inhaltsprüfung zählen. Jede finale I-/S-Ableitung benötigt Inhaltsprüfung A.
Hauptagent ergänzt mit scripts/stamp-review.py die Fingerprints aus
facts-validation.json (basis) oder interpretation-validation.json (final).
Das Skript bewahrt Entscheidungen; es prüft Identität/Referenzen und blockiert
fehlende Pflichtprüfungen, kann aber keine Wahrheit oder Ableitung freigeben.
Ausgabe review-basis.md / review-final.md mit genau einem JSON-Codeblock;
reines JSON zulässig. Bei Legacy-Modus bisherigen Bericht beibehalten.
Details und lokale Aufrufe in interpretationsphase.md; Fingerprints nicht
manuell erfinden oder im Agentenkontext als lange Erfolgsliste wiederholen.
