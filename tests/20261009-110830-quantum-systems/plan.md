# Plan – Modultest Quantum Systems (2b -> 4 -> 7)

## Kopf
| Feld | Wert |
|---|---|
| Modus | modultest (references/modultest.md) |
| Testverzeichnis | /home/user/Firmenbreefing/tests/20261009-110830-quantum-systems/ (im Folgenden <Test>) |
| Unternehmen | Quantum Systems (Quantum-Systems GmbH, Raum München). In 2b eindeutig zuordnen und die offizielle Website https://quantum-systems.com prüfen |
| Unternehmensgrenze | Quantum-Systems-Gruppe einschließlich öffentlich belegter Tochtergesellschaften, Beteiligungen, Eigentümer, JV und Partner (Default) |
| Stichtag | 2026-10-09 |
| Sprache / Zielgruppe | Deutsch / Top-Management und Gesprächsvorbereitung |
| Nutzerthemen / Person | keine genannt; kein Personenprofil |
| Planstatus | geplant |
| Planer | module-contractor (schreibt nur diese Datei) |

## Originalanfrage (unverändert)
> Nutze die vorhandenen Repository-Anweisungen. Erstelle für Quantum Systems ausschließlich die Cluster-Analyse 2b, anschließend die Quellenprüfung 4 und direkt die HTML-Ausgabe 7. Recherchiere ein neues Unternehmensnetzwerk und stelle es mit der vorhandenen interaktiven Netzwerkkomponente inklusive Originalquellen dar.

## Modulauswahl und Begründung
| Schritt | Auswahl | Begründung |
|---|---|---|
| 2a Portfolio | nicht beauftragt | Ausschluss durch „ausschließlich die Cluster-Analyse 2b“ |
| 2b Struktur/Cluster | **ausgewählt** | ausdrücklich angefordert. Die Anfrage nennt das Unternehmensnetzwerk; dazu gehören die Geschäftsbericht- und Querverbindungsprüfung nach references/cluster-recherche.md sowie network-data-JSON nach references/netzwerk-html.md |
| 3 Kontext (Markt/Themen/Person) | nicht beauftragt | kein Teilumfang angefordert; keine Themen und keine Person genannt |
| 4 Basis-Review | **ausgewählt** | ausdrücklich angefordert („Quellenprüfung 4“); prüft nur work/cluster.md |
| 5 SWOT / 6 Schluss-Review | nicht vorgesehen | im Modultest ausgeschlossen; kein Wechsel zu company-briefing |
| 7 Ausgabe | **ausgewählt** | ausdrücklich angefordert („direkt die HTML-Ausgabe 7“), mit der Vorlage references/templates/cluster-network.html |

Der Umfang wird nicht erweitert. Fehlende Portfolio-, Markt- oder SWOT-Dateien
sind keine fehlenden Voraussetzungen (modultest.md, „Nur ausgewählte Module sind Pflicht“).

## Ausführungsliste (Nutzerreihenfolge, sequenziell)

### Schritt 1 – 2b Cluster-Analyse
- Rolle / Methode: cluster-analyst / cluster-analysis. Der Hauptagent ruft die Rolle auf; der Modultest-Pfad ersetzt die festen Pfade.
- Eingaben: <Test>/input/auftrag.md, <Test>/plan.md, references/cluster-recherche.md,
  references/netzwerk-html.md, references/uebergabe.md, CLAUDE.md.
- Zielpfad: <Test>/work/cluster.md (nur diese Datei).
- Pflichtinhalte:
  1. Kopf nach uebergabe.md mit Status vollständig/teilweise/blockiert. Die Firmenidentität und die offizielle Website eindeutig bestätigen.
  2. Kompakte Übersicht und 3 bis 5 belegte Kernaussagen.
  3. Akteursliste mit Knoten-IDs. Ebene 1 umfasst Töchter, Beteiligungen, Eigentümer/Investoren, JV, Kooperations-, Kunden-, Zuliefer- und Projektpartner. Ebene 2 umfasst die Querverbindungen zwischen diesen Akteuren und die Akteure, die eine Beziehung erklären. Die Recherchegrenze ist zu dokumentieren.
  4. Beziehungstabelle mit Kanten-IDs. Kapitalanteil, Stimmrechte und Kontrolle werden getrennt erfasst. Direkte Beziehungen, indirekte Pfade und Überschneidungen werden getrennt geführt, ebenso historische und aktuelle Beziehungen.
  5. Querverbindungen mit belegten Teilbeziehungen. Die Analysteninterpretation wird separat gekennzeichnet.
  6. Geschäftsbericht-Protokoll für das Zielunternehmen und die strukturtragenden Akteure (Eigentümer, JV-Mitgesellschafter, wesentliche Partner): Akteur | Bericht | GJ | Veröffentlichung | URL | Abschnitte/Seiten (PDF/gedruckt) | Claim-IDs | Zugriffsstatus. Liegt für die GmbH kein öffentlicher Bericht vor, wird das als Lücke dokumentiert, etwa ob ein Abschluss im Unternehmensregister zugänglich ist. Ohne Bericht bleibt eine Beziehung damit offen und gilt nicht als widerlegt.
  7. Ein C-Claim-Register nach uebergabe.md. Für Berichte kommen Geschäftsjahr, Seite/Abschnitt und Bezugszeitpunkt hinzu.
  8. Den Abschnitt „## network-data“ mit genau einem JSON-Codeblock nach Schema v1. Dabei gilt company = Quantum Systems und as_of = 2026-10-09, mit genau einem target. Zulässig sind nur tatsächlich geöffnete Quellen und dokumentierte C-Claims. Produkte nur bei belegter Zuordnung, sonst products = []. Keine Daten aus anderen Tests oder Läufen.
- Rückgabe an den Hauptagenten: Pfad, Status, Kernergebnisse, offene Punkte.

### Schritt 2 – 4 Basis-Review
- Rolle: source-reviewer, Phase basis.
- Eingaben: <Test>/input/auftrag.md, <Test>/plan.md, <Test>/work/cluster.md, references/cluster-recherche.md, references/netzwerk-html.md, references/uebergabe.md.
- Prüfgegenstand: nur work/cluster.md. Die Module 2a und 3 werden als „nicht beauftragt“ geführt, nicht als Fehler.
- Prüfpunkte: Firmenidentität und Stichtag; Quellen tatsächlich geöffnet und ursprünglich; Zweitbelege bei Eigentum und Kontrolle; Quotenarten und Zeitstatus; indirekte Teilpfade; die Trennung von Überschneidung und Kooperation; die Belegstellen in Geschäftsberichten (PDF- und gedruckte Seite); angekündigte gegenüber abgeschlossenen Vorgängen. Im network-data werden eindeutige IDs, genau ein Ziel, gültige Referenzen, Kategorien, Produktbelege sowie die Übereinstimmung von JSON, C-Claims und Quellen geprüft.
- Zielpfad: <Test>/work/review-basis.md.
- Korrekturschleife: Wesentliche Fehler korrigiert der cluster-analyst in work/cluster.md. Danach prüft der source-reviewer erneut und aktualisiert review-basis.md. Nach zwei erfolglosen Korrekturrunden gilt der Status blockiert, und Schritt 7 entfällt als geprüfte Ausgabe.

### Schritt 3 – 7 Ausgabe
- Rolle / Methode: Hauptagent / briefing-output.
- Voraussetzung: Schritt 4 ist bestanden und es gibt keine offenen wesentlichen Fehler.
- Eingaben (ausschließlich): <Test>/input/auftrag.md, <Test>/plan.md, <Test>/work/cluster.md (geprüfter Stand), <Test>/work/review-basis.md, references/templates/cluster-network.html, references/briefing-struktur.md, references/netzwerk-html.md.
- Zielpfade: <Test>/output/briefing.html und <Test>/output/abnahme.md.
- HTML:
  - Titel und Kopf als „Modultest 2b – Quantum Systems“ mit Stichtag und Prüfstatus.
  - Kurze Zusammenfassung, mit nur so vielen Punkten, wie belegt sind.
  - Kapitel 2b mit der eingebetteten Netzwerkkomponente. CSS und JS sind lokal eingebettet. __CLUSTER_NETWORK_JSON__ wird einmal durch sicher serialisiertes JSON ersetzt (<, >, &, U+2028/U+2029 Unicode-escapen).
  - Beziehungstabelle, Abdeckung der Geschäftsberichte, Lücken und Quellenregister mit Claim-Zuordnung.
  - Keine leeren Kapitel für 2a, 3 oder SWOT.
  - Neue Unternehmensbehauptungen in der HTML müssen vor einer geprüften Ausgabe zurück in Schritt 4.
- Abnahme: tatsächlich aufgerufene Rollen und Dateien, Reihenfolge, Review-Status und geschlossene Fehler. Weiter Quellenlinks, interne Links, Mobil- und Druckansicht. Für das Netz: Ziel zentral, Farben und Legende, Auswahl der Linien, Filter (Kategorie und Produkt), JV-Kontextknoten, Mehrfachrollen, kein veraltetes Detail nach Filterwechsel, Tastatur und Touch, Konsistenz von JSON, Claims und Quellen. Jeder Punkt wird als bestanden, offen, nicht geprüft oder nicht beauftragt geführt. Nicht ausführbare Browserprüfungen gelten als „nicht geprüft“.

## Nicht ausgewählte Schritte
2a (work/portfolio.md), 3 (work/markt.md, work/kontext.md), 5 SWOT (work/swot.md), 6 Schluss-Review: werden nicht ausgeführt und nicht angelegt. In der Abnahme stehen sie als „nicht beauftragt“ bzw. „im Modultest nicht vorgesehen“.

## Dateizuordnung innerhalb dieses Tests
| Pfad | Schreibende Rolle | Status |
|---|---|---|
| <Test>/input/auftrag.md | Hauptagent | vorhanden (angelegt) |
| <Test>/plan.md | module-contractor | dieser Plan |
| <Test>/work/cluster.md | cluster-analyst | geplant |
| <Test>/work/review-basis.md | source-reviewer (basis) | geplant |
| <Test>/output/briefing.html | Hauptagent | geplant |
| <Test>/output/abnahme.md | Hauptagent | geplant (auch bei Blockade mit bisherigem Status anlegen) |

Die Repository-Pfade input/auftrag.md, work/ und output/ des Standardlaufs werden nicht berührt.

## Fortsetzung / vorhandene Dateien
Es handelt sich um einen neuen Test. Verwendet wird nur <Test>/input/auftrag.md (Status vorhanden). Es gibt keine vorhandenen Ergebnisse. Dateien, Claims, Reviews oder Netzdaten aus anderen Tests oder dem Standardlauf werden nicht übernommen. Die Netzwerkvorlage liefert nur Code, Layout, Farben, Filter und Schema.

## Voraussetzungen und mögliche Blockaden
- Die Vorlage references/templates/cluster-network.html ist vorhanden; der Platzhalter __CLUSTER_NETWORK_JSON__ wurde gesichtet.
- Die Firmenidentität ist in 2b zu bestätigen. Bei einer relevanten Verwechslungsgefahr gezielt nachfragen; bisher ist keine bekannt.
- Bei einer GmbH liegen voraussichtlich keine Geschäftsberichte wie bei börsennotierten Firmen vor. Der Zugriff auf Abschlüsse im Unternehmensregister ist möglicherweise eingeschränkt. Das wird als Lücke dokumentiert und blockiert nicht.
- Für die Angaben zu Investoren und Finanzierungsrunden sind Kapital-, Stimmrechts- und Kontrollquoten öffentlich oft nicht belegt. Die Werte bleiben dann „unbekannt“; keine Schätzungen.
- Blockade für 7: nicht bestandenes 4 nach zwei Korrekturrunden oder fehlerhaftes network-data.
- Browserbasierte Interaktions-, Mobil- und Druckprüfungen sind möglicherweise nicht ausführbar. In diesem Fall gelten sie als „nicht geprüft“ und nicht als bestanden.

## Ergebnisstatus
geplant (2b, 4 und 7 noch nicht ausgeführt).
