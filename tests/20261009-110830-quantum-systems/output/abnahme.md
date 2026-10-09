# Abnahme – Modultest Quantum Systems (2b -> 4 -> 7)

Testverzeichnis: tests/20261009-110830-quantum-systems/ · Stichtag 2026-10-09 · Modus modultest

## Ergebnis
**Geprüfter Modultest ausgegeben.** Das Basis-Review (Schritt 4) ist nach Korrekturrunde 1 von 2
„bestanden mit Hinweisen“; es gibt keine offenen wesentlichen Fehler.
Ausgabe: output/briefing.html (eigenständige HTML mit eingebetteter Netzwerkkomponente).

## Tatsächlich aufgerufene Rollen und Dateien
| Schritt | Rolle | Datei | Status |
|---|---|---|---|
| Auftrag | Hauptagent | input/auftrag.md | bestanden |
| Plan | module-contractor | plan.md | bestanden (2b -> 4 -> 7; 2a/3 nicht beauftragt, 5/6 nicht vorgesehen) |
| 2b | cluster-analyst (cluster-analysis) | work/cluster.md | bestanden: vollständig für 2b; Geschäftsbericht-Abdeckung teilweise |
| 4 | source-reviewer, Phase basis | work/review-basis.md | Erstprüfung nicht bestanden (W1–W3, K1–K2) → Korrektur durch cluster-analyst → Nachprüfung „bestanden mit Hinweisen“ |
| 4 (redaktionell) | cluster-analyst | work/cluster.md | N1–N3 umgesetzt. Hauptagent prüfte den Diff: nur die vom Review benannten Wortlaut-, Quellen- und Datumsangleichungen, keine neuen Claims |
| 7 | Hauptagent (briefing-output) | output/briefing.html, output/abnahme.md | bestanden, siehe Kontrollen |

Nicht beauftragt: 2a Portfolio, 3 Markt/Themen/Person. Im Modultest nicht vorgesehen: 5 SWOT, 6 Schluss-Review.

## Kontrollen
| Kontrolle | Status | Nachweis |
|---|---|---|
| Auftragsnormalisierung (Firma, Stichtag, Modulwahl) | bestanden | auftrag.md, plan.md |
| Themen / Person | nicht beauftragt | keine genannt |
| Reihenfolge 2b -> 4 -> 7 | bestanden | 7 erst nach bestandenem 4 |
| Geschlossene Fehler W1–W3, K1–K2 | bestanden | review-basis.md, „Nachprüfung Runde 1“ |
| company/as_of/Zielknoten = Auftrag | bestanden | Skriptprüfung: „Quantum Systems“, 2026-10-09, target_id qs, genau ein target |
| JSON/Claims/Quellen übereinstimmend | bestanden | Skriptprüfung: alle claim_ids existieren im C-Claim-Register, alle source_ids im Quellenregister, JSON-Quellen = Quellenregister (36) |
| Neues Netz, keine Altdaten | bestanden | kein Vorgängertest vorhanden; Vorlage enthält nur den Platzhalter |
| Platzhalter sicher ersetzt | bestanden | einmalig ersetzt; <, >, &, U+2028/U+2029 escaped; keine externen Skripte (`src=` 0) |
| Ziel zentral | bestanden | Browser: Zielknoten im Mittelpunkt der viewBox (Desktop 524/519 bei 1048×1038; Mobil 179/851 bei 358×1702) |
| Knotenfarben und Legende | bestanden | 8 Knotenarten mit Legende |
| Linien anfangs ohne Beschriftung, Details erst nach Auswahl | bestanden | Detailfeld anfangs verborgen; Texte nur Knotennamen |
| Jede Linie auswählbar | bestanden | 37/37 per Tastatur-Schaltfläche, 37/37 exakt per Mausklick (1200 px), 37/37 exakt per Touch (390 px) |
| Originalquellenlinks im Detail | bestanden | jede Kante zeigt ≥ 1 http(s)-Link; 27 eindeutige URLs abgerufen, alle HTTP 200 (2026-10-09) |
| Kategoriefilter (ODER), Produktfilter (UND) | bestanden | JV-Filter: 4 Kanten inkl. Kontext Porsche SE/DTCP; Eigentumsfilter enthält Frontline (W1); Produkt Vector: 1 Kante |
| Keine veralteten Details nach Filterwechsel | bestanden | ausgewählte Kante weggefiltert → Detail geschlossen |
| Mehrfachrollen ohne doppelte Firmen | bestanden | HENSOLDT, Airbus DS, Frontline je ein Knoten mit mehreren Kanten |
| Querverbindungen sichtbar | bestanden | Ebene-2-Kanten (Porsche SE–DTCP–Incharge, Airbus–HENSOLDT, Nordic Unmanned, Lockheed Martin UK–UK MoD, Frontline–QFI–Ukraine) |
| Keine Überlappung von Knoten/Labels | bestanden | 0 Überlappungen bei 320, 390, 768, 1200 px |
| Mobilansicht | bestanden | kein horizontales Scrollen bei 390 px; Touch-Auswahl s. o. |
| Druck | bestanden (emuliert) | Print-Media: Filter ausgeblendet, Beziehungstabelle mit Quellen sichtbar; PDF-Probedruck 44 S. Ein physischer Druck wurde nicht geprüft. |
| Interne Anker | bestanden | 0 tote #-Links |
| Pflichthinweise 1–10 aus review-basis.md sichtbar | bestanden | Hinweiskasten im Kopf; Detail- und Tabellenstatus |
| Geschäftsbericht-Belegstellen | bestanden (Review) | Protokoll im HTML; Seiten von source-reviewer geprüft |
| Dark Mode | nicht geprüft | CSS vorhanden, nicht visuell geprüft |
| Screenreader | nicht geprüft | nur aria-Labels und Tabellenalternative vorhanden |

## Layout-Anpassung der eingebetteten Komponente
Nach references/netzwerk-html.md („Layout anpassen, ohne Daten/Belege zu ändern“) wurde nur die
eingebettete Kopie angepasst. references/templates/cluster-network.html bleibt unverändert.
- Ein Ring mit gleichen Bogenabständen statt mehrerer Ringe, damit Linien vom Ziel keine Knoten kreuzen. Mobil zwei Spalten.
- Reihenfolge auf dem Ring: querverbundene Akteure liegen nebeneinander (aus den Kanten berechnet).
- Ziel-Label umbricht nach 9 Zeichen. Parallele Kanten haben 56 statt 24 Abstand.
- Knoten sind für Zeiger durchlässig. Die vorhandenen Tastatur-Schaltflächen in der Linienmitte sind auch per Klick/Touch auswählbar (24 px, unsichtbar, ohne Beschriftung).
- Druck: `::details-content` wird zusätzlich eingeblendet, damit die Tabelle auch ohne beforeprint erscheint.
Grenze: In der schmalen Zwei-Spalten-Ansicht laufen einige Linien vom Ziel nah an Knoten derselben Spalte vorbei.
Die Auswahl bleibt eindeutig (37/37). Die Beziehungstabelle ist die zugängliche Alternative.

## Offene Lücken (transparent, keine Fehler)
Cap Table/Kontrolle, Series-D-Closing, aktueller HENSOLDT-Anteil, Verkäufer von AirRobot/NU UK,
Produktionsstand QFI, Ausübung der Frontline-Option, Konzernabschluss 2025, HENSOLDT-/Airbus-
Geschäftsbericht 2025, Original im Unternehmensregister (nur Drittanbieter-Kopie gelesen), HTML-Seiten
quantum-systems.com (HTTP 403).

## Dateisicherung und Ausgabe
Alle Dateien liegen im Testverzeichnis und sind im Branch claude/sleepy-euler-bsbjbf committet und gepusht.
Root-Dateien input/, work/ und output/ blieben unverändert. Es gibt keine automatische öffentliche Veröffentlichung.

## Nächste mögliche Schritte
- 2a Portfolio und/oder 3 Markt für denselben Test (danach erneut 4).
- Gesellschafterliste und Konzernabschluss 2025 im Unternehmensregister direkt prüfen.
