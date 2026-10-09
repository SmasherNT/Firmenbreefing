---
name: cluster-analysis
description: Analysiert Unternehmensstruktur, Geschäftsberichte und belegte Querverbindungen im Unternehmensnetzwerk.
---

Lies input/auftrag.md, CLAUDE.md, references/uebergabe.md,
references/defaults.md, references/briefing-struktur.md und
references/cluster-recherche.md. Die Netzwerk- und Berichtsmethode dort
ist verbindlich. Ohne tatsächlichen Auftrag keine Firmenanalyse beginnen.

1. Zielunternehmen und relevante Akteure eindeutig identifizieren.
2. Direkte Beziehungen und Querverbindungen systematisch recherchieren:
   Eigentum/Kontrolle, JV, Kooperation, Lieferant/Kunde, Projekte/Konsortien,
   Technologie/Lizenzen, öffentliche berufliche Mandate und Historie.
3. Geschäftsberichte von Zielunternehmen und relevanten verbundenen Akteuren
   ausdrücklich suchen und einschlägige Abschnitte analysieren.
4. Akteursliste, Beziehungstabelle, indirekte Pfade, Querverbindungen,
   Bericht-Protokoll und Rechercheabdeckung nach cluster-recherche.md liefern.
5. C-Claims mit Originalbelegen, Bezugszeitpunkt, Status und Unsicherheit
   dokumentieren; Geschäftsberichte mit Geschäftsjahr und Seite/Abschnitt.
6. Quellen abgleichen; Überschneidung nicht als Zusammenarbeit ausgeben,
   Kapitalanteil/Stimmrechte/Kontrolle trennen, historische Status erhalten.

Schreibe ausschließlich work/cluster.md nach uebergabe.md.
Nutzerthemen priorisieren; Recherchegrenzen und Lücken transparent benennen.
Keine vollständige Konzernstruktur oder Lieferkette behaupten.
Keine Markt-/SWOT-Analyse als Ersatz für die Netzwerkprüfung.

## Ausnahme für ausdrücklich beauftragte Modultests
Bei Modus modultest lies references/modultest.md. Die Delegation nennt
Testauftrag, Auswahl, Eingaben und Zielpfad. Diese Pfade ersetzen die festen
input/work/output-Pfade oben. Nicht gewählte Module sind keine Pflicht.
Die gesamte Netzwerk-/Berichtsmethode gehört zu 2b; sie benötigt weder 2a
noch 3, 5 oder 6. Im Standardlauf bleiben die üblichen Abhängigkeiten bestehen.

## Übergabe an die HTML-Ausgabe
Lies references/netzwerk-html.md. Zusätzlich zu den lesbaren Tabellen das
network-data-JSON nach Schema v1 in work/cluster.md liefern. Es enthält genau
ein Zielunternehmen, eindeutig typisierte Knoten, belegte Kanten, Filterkategorien,
Produkt-IDs und Originalquellen mit Geschäftsbericht-Belegstellen.
Keine Beispiel-/Demo-Daten einsetzen; keine zusätzliche Pflichtdatei schreiben.

Jeder neue Firmenauftrag erhält einen vollständig neu recherchierten Datensatz.
company/as_of müssen zum Auftrag passen; keine inhaltliche Übernahme aus früheren
Firmenläufen. Das Schema enthält keine festen Firmen oder Verbindungen.


## Vertiefte Technologie- und Kundenrecherche
Lies references/cluster-quellenkatalog.md zusätzlich zu cluster-recherche.md.
Prüfe Technologie & Industrie sowie Kunden & Marktzugang in zwei Durchgängen,
mit Gegenrecherche bei Partnern, Auftraggebern, Projekten und öffentlichen
Vergabe-/Forschungsportalen. Quellenart, Beschaffungs-/Umsetzungsstatus und
Abdeckungsmatrix dokumentieren. Neue Beziehungen erst nach Quellenprüfung
in network-data übernehmen; keine Knoten oder Quoten zur Grafikfüllung erfinden.
