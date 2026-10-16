# Netzwerkdaten und Übernahme in Schritt 7

## Zuständigkeiten
2b / cluster-analyst liefert Recherche, Knoten, Beziehungen und Originalquellen.
Zusätzlich in work/cluster.md den Abschnitt "## network-data" mit genau einem
JSON-Codeblock nach Schema v1 schreiben. Keine neue Ergebnisdatei nötig.
4 / source-reviewer prüft auch diese Daten gegen Claims und Originalquellen.
7 / Hauptagent mit briefing-output übernimmt die geprüften Daten in die
wiederverwendbare Komponente references/templates/cluster-network.html.
Das gilt sowohl im vollständigen Briefing als auch bei 2b -> 4 -> 7.
Der Cluster-Agent erstellt keine eigene finale HTML und überspringt keine Reviews.

## Verbindliches Erscheinungsbild
- Das Zielunternehmen bleibt zentral. Die übrigen Akteure bilden ein Netz
  darum herum; Querverbindungen verbinden auch umliegende Akteure miteinander.
- Alle Kreise haben denselben Radius; andere Formen verwenden dieselbe feste
  Größenbasis. Keine Größenstaffelung oder Zahlen-/Score-Badges in den Formen.
  Kurze Unternehmensnamen stehen unter den Formen, der Zielname im Zentrum.
  Jede Knotenart hat eine konsistente Farbe und Form samt gemeinsamer Legende.
  Größenbasis: Radius 22 SVG-Einheiten (Durchmesser 44), auch für das Ziel.
  Je Bereich fünf Akteure pro Reihe; Namen umbrechen statt Spaltenzahl reduzieren.
  Bei schmaler Fläche nur das Netz lokal horizontal scrollen. Die vier Bereiche
  bleiben im 2×2-Raster: gleiche Höhe je Bereichsreihe, Höhe nach benötigten
  Akteursreihen. Filter, Reihenfolge, Formen und rechte Detailspalte erhalten.
- Linien zeigen anfangs keine Beschriftung, Quote, Quellen oder Hover-Details.
  Verbindungen folgen dem bestätigten ursprünglichen Stil: leicht gebogene
  Linien mit Richtungspfeilen zwischen den Knotenrändern, ohne Endpunktkreise.
  Klick oder Tastaturauswahl zeigt Inhalte in der festen
  rechten Detailspalte, ohne Dialog oder Aufklappen. Nur Desktop-Darstellung.
  Mehrere Beziehungen desselben Paars teilen eine Linie; rechts bleiben alle
  Vorgänge einzeln auswählbar, einschließlich ihrer Richtung und Originalquellen.
- Details zeigen Von/Zu, Beziehungstyp, Gegenstand, Status, Datum, Quotenarten,
  Produktbezug, Unsicherheit und Claim-IDs sowie klickbare Originalquellen.
- Filter für Partner, Kunden, Joint Ventures, Eigentum, Zulieferer,
  Tochtergesellschaften, Projekte und weitere Beziehungen anbieten,
  soweit entsprechende Beziehungen vorliegen. Mehrere Filter kombinierbar.
- Produktfilter nur mit belegten Produktzuordnungen; keine erfundenen Produkte
  oder aus Portfolioähnlichkeit abgeleiteten Liefer-/Kundenbeziehungen.

Filter wirken auf Beziehungen: Kategorien untereinander ODER, ausgewählter
Produktbezug zusätzlich UND. Verbundene Akteure bleiben als Kontext sichtbar,
auch wenn ihre primäre Knotenart eine andere Kategorie hat.
Beispiel: JV-Filter zeigt auch seine Mitgesellschafter und alle passenden Kanten.
Eine Firma mit mehreren Rollen bleibt ein Knoten. Ihre primäre Knotenart bestimmt
Farbe und Form; Beziehungen können mehrere Filterkategorien tragen.
Das Zielunternehmen bleibt immer sichtbar. Knoten bleiben im zugewiesenen Cluster; bei Filtern darf das Layout kompakt
neu angeordnet werden, ohne die Clusterzuordnung zu verändern. Leere Ergebnisse verständlich anzeigen.
Unzugeordnete Produktbeziehungen nur unter "Alle Produkte", nicht künstlich
einem bestimmten Produkt zuschlagen.

## Neues Netz bei jedem Firmenauftrag
Jeder neue Auftrag erzeugt einen neuen network-data-Datensatz ausschließlich aus
der Recherche für die aktuelle Firma und den aktuellen Stichtag. Keine Knoten,
Kanten, Produkte, Claims oder Quellen aus dem vorigen Firmenlauf übernehmen.
Wiederverwendbar sind nur Code, Layout, Farben, Filter und Datenschema.
Die HTML-Vorlage enthält keine Firmen oder Beziehungen; der Platzhalter wird
bei jedem Lauf vollständig durch die neuen geprüften Firmendaten ersetzt.
Bestehende Ergebnisse werden nach den Archivierungsregeln gesichert, nicht
als Vorlage für Inhalte verwendet. Fortsetzungen desselben Modultests dürfen
seine eigenen Ergebnisse verwenden; ein Firmenwechsel ist immer ein neuer Test.
Vor Schritt 7 company/as_of und Zielknoten mit dem aktuellen Auftrag abgleichen.

## JSON-Schema v1
Top-Level:
- schema_version: 1
- company: eindeutig identifiziertes Zielunternehmen des aktuellen Auftrags
- as_of: Stichtag des aktuellen Auftrags (YYYY-MM-DD)
- target_id: ID des einzigen Zielknotens
- nodes: Akteursliste
- edges: einzelne belegte Beziehungen
- products: tatsächlich belegte Produkte/Produktgruppen
- sources: Originalquellenregister

Jede ID ist innerhalb ihrer Liste eindeutig und stabil.
Nodes: id, label (kurzer tatsächlicher Name, möglichst maximal 30 Zeichen),
kind. Optional legal_name für den vollständigen Namen, cluster für die Darstellungsgruppe
(capital, structure, technology, market) und focus (Boolean) für eine begründete
redaktionelle Erstansicht. cluster ist keine juristische Kategorie.
kind: target, partner, customer, jv, owner, supplier, subsidiary, project,
person, institution oder other. Genau ein target; target_id zeigt auf ihn.
kind wird aus belegten Rollen gewählt; keine zusätzlichen Firmen erfinden.

Products: id, label. Leere Liste erlaubt; dann keinen Produktfilter zeigen.
Edges (Pflicht): id, from, to, type, summary, categories, product_ids,
source_ids, claim_ids, status, as_of.
- from/to sind vorhandene Knoten-IDs und benennen die tatsächliche Richtung.
- type und summary erklären den konkreten belegten Vorgang; keine neue Behauptung.
- categories ist eine nichtleere Liste aus partner, customer, jv, owner,
  supplier, subsidiary, project, other.
- product_ids ist eine Liste vorhandener Produkt-IDs, leer wenn nicht belegt.
- source_ids ist eine nichtleere Liste vorhandener Originalquellen-IDs.
- claim_ids ist eine nichtleere Liste tatsächlich im Cluster-Modul dokumentierter C-Claims.
- status und as_of erhalten Ereignis-/Bezugsstatus; nicht nur das Abrufdatum.
Optional: capital_share, voting_share, control, interpretation, uncertainty,
historical (Boolean), overlap (Boolean).
Kapital/Stimmrechte/Kontrolle getrennt; Interpretation separat kennzeichnen.
Indirekte Pfade durch ihre tatsächlichen Teilkanten darstellen; keine künstliche
direkte Kante. Mehrere Vorgänge zwischen denselben Akteuren bleiben getrennte Kanten.

Sources: id, name, title, url, published_date, accessed_date.
published_date = Datum oder null bei o. D.; niemals ein Datum erfinden.
Optional report_year, page, section, source_kind (Originalbericht, amtlicher
Datensatz, Herstellerangabe, Partnerangabe, Sekundärquelle, Drittanbieter-Kopie
oder Wiedergabe). Quellenart auch im Review erfassen. Gedruckte/PDF-Seite in page ausdrücklich
unterscheiden, wenn abweichend. URLs nur tatsächlich geöffnete http(s)-Quellen; Primär-/Sekundärart und Kopien
nach references/cluster-quellenkatalog.md ausdrücklich klassifizieren.
Direkter Dokumentlink bleibt erhalten; bei PDF die Belegseite im Detail nennen.
Ein #page-Fragment kann zusätzlich angeboten werden, wenn der Viewer es unterstützt;
die ausgeschriebene Seitenangabe darf nicht davon abhängen.

Keine Recherche-Platzhalter, Testdaten oder Beispielquoten in echten Ausgabedaten.
Fehlende öffentliche Belege als Lücke dokumentieren und nicht als Kante zeichnen.

## Übernahme in die finale HTML
1. Auftrag/Plan, die neu recherchierten Cluster-Claims und den zugehörigen Review
   dieses Firmenlaufs lesen. company/as_of/Zielknoten mit dem Auftrag abgleichen.
2. network-data prüfen: eindeutige IDs, genau ein Ziel, gültige Referenzen,
   Kategorien, Produktbelege und Quellen sowie Übereinstimmung mit C-Claims.
3. Die reine Darstellungsvorlage references/templates/cluster-network.html lesen
   (ohne alte Firmen-/Netzdaten) und als Fragment in das
   Strukturkapitel bzw. den 2b-Modultest einbetten. CSS und JavaScript vollständig
   lokal übernehmen; keine externen Bibliotheken oder Laufzeit-Netzabfragen.
4. __CLUSTER_NETWORK_JSON__ einmalig durch sicher serialisiertes geprüftes JSON
   ersetzen: mindestens <, > und & sowie U+2028/U+2029 Unicode-escapen, damit
   Quelltexte kein script-Element beenden. Nicht HTML-escapen, sonst bricht JSON.
5. Text im Renderer nur per textContent, Links nur mit validiertem http(s)-href.
   Eigenes lokales JavaScript ist erlaubt; keine Skripte aus Quellen übernehmen.
6. Die Originalquellen erscheinen als direkte Links im Verbindungsdetail und
   in der Beziehungstabelle. Sie müssen auch im allgemeinen Quellenregister
   mit denselben Claim-/Quellenzuordnungen vorhanden sein.
7. Alle Beziehungen bleiben in einer zugänglichen Tabelle erhalten. Druck
   zeigt die Tabelle mit Quellen unabhängig vom aktuellen Bildschirmfilter.

Der Renderer ist eine Vorlage, keine Garantie für jede Netzgröße.
Bei vielen Akteuren oder langen Namen Layout anpassen, ohne Daten/Belege zu
ändern: aufklappbare Cluster, Teilnetze oder bewusste Begrenzung der
Erstansicht mit sichtbarer Erweiterungsmöglichkeit. Keine unsichtbare Datenkürzung.
Knoten dürfen sich nicht überlappen; bei schmalen Desktopfenstern bleibt die
Mindestbreite lokal horizontal verschiebbar. Die Seite muss normal vertikal
scrollen können; kein globales overflow:hidden und kein Scroll-Lock.
Farben und Formen zusätzlich durch Legende
und die im Detail erklärte Rolle erschließen. Keine Beschriftungen auf Linien
hinzufügen, um Platzprobleme zu umgehen.
Kein starres Bild, keine reine Mermaid-Grafik und keine externe Live-Datenquelle
als Ersatz für den geforderten interaktiven Bestandteil.
Bei fehlerhaften Übergabedaten Korrektur verlangen; Fehlermeldung der Vorlage
ist keine akzeptierte finale Ausgabe. Modultest ohne Review bleibt ungeprüft.

## Abnahme
Tatsächlich prüfen: Ziel zentral, Knotenfarben/Legende, jede Linie auswählbar,
Details erst nach Auswahl, Originalquellenlinks, Kategorie-/Produktfilter,
Kontextknoten bei JV, Mehrfachrollen ohne doppelte Firmen, Querverbindungen,
keine veralteten Details nach Filterwechsel, Tastatur, Seitenscrollen und Druck.
Technische Datenvalidierung ersetzt keinen inhaltlichen Quellencheck.
Nicht ausführbare Browserprüfungen als nicht geprüft melden.
Die installierte Vorlage wurde syntaktisch geprüft; ein tatsächlicher
Claude-Recherche- und Browserlauf mit echten Daten bleibt nachzuweisen.


## Vier-Cluster-Layout (verbindliche neue Standarddarstellung)
Zielunternehmen zentral zwischen vier rechteckigen Bereichen im 2×2-Raster:
Kapital & Investoren oben links, Konzern & Joint Ventures oben rechts,
Technologie & Industrie unten links, Kunden & Marktzugang unten rechts.
Je Zeile sind die beiden Bereiche gleich hoch; die Höhe folgt der Zahl der
sichtbaren Akteure. Innerhalb eines Bereichs stehen Knoten neben- und untereinander.
Die vorhandene Bereichszuordnung und Reihenfolge der Akteure bleiben erhalten.
Je Knoten eine Farbe und Form nach belegter Knotenart, eine eindeutige Identität,
kein Relevanzscore. Formen: Partner Kreis, Tochtergesellschaft Quadrat, JV Sechseck,
Eigentümer Achteck, Zulieferer Raute, Kunde Dreieck, Projekt Fünfeck,
Institution abgerundetes Quadrat, Person Stern, Sonstige Ellipse; Ziel Kreis.
Erstansicht bis zu sechs Akteure je Bereich; focus priorisiert die Auswahl,
begründet in der Cluster-Datei. Zusätzliche JV-/Tochter-Kontextknoten bleiben
sichtbar; andere Akteure sind per Cluster aufklappen erreichbar.
Querverbindungen zunächst eingeblendet und per Filter umschaltbar.
Auswahl listet alle Rollen eines Akteurs;
Linien bleiben unbeschriftet, Quellen und Unsicherheiten nur im Klickdetail.
Suche, Status-, Kategorie- und belegte Produktfilter verwenden.
Beziehungen der gleichen Akteurspaarung bündeln; jede bleibt rechts einzeln
auswählbar. Bei beiden Richtungen Pfeile an beiden Enden zeigen. Reduzierte Erstansicht
mit sichtbarem Gesamtzähler; die vollständige Tabelle enthält alle Beziehungen.
Im Desktopfenster Grafik lokal horizontal verschiebbar mit lesbarer Mindestbreite
760px, feste rechte Detailspalte und Tastatur-Beziehungsauswahl als Alternative.
Keine gesonderte Mobilansicht oder Mobilabnahme.
Keine Pflicht, leere Bereiche mit ungeprüften Akteuren zu füllen.
Lange Prüfhinweise, Abdeckungsmatrix und Register aufklappbar; wesentliche
Unsicherheiten trotzdem am betroffenen Claim/Verbindungsdetail sichtbar halten.
Abnahme zusätzlich: alle Cluster aufklappen, Querverbindungen, Suche/Status,
Knoten-/Linienklick, gleichzeitige Rollen, keine alten Details nach Filterwechsel.

JV-Kontextkanten haben Vorrang vor dem standardmäßig ausgeblendeten
Querverbindungsfilter: passende Gesellschafter-zu-JV-Kanten bleiben sichtbar.
Die vollständige Tabelle bewahrt auch Quoten, Kontrolle, Produktbezug,
Interpretationen und Unsicherheiten; Claim-IDs sind interne Sprunglinks.
Datumspräzision beibehalten: Kanten as_of YYYY-MM oder YYYY-MM-DD,
Top-Level-Stichtag und Quellendaten YYYY-MM-DD; unbekannte Veröffentlichung
explizit null. Pflichtmetadaten nicht mit fehlenden Feldern verwechseln.
