# Abnahme Schritt 5: feste HTML-Ausgabe

## Umgesetzt
Facts-v2 und interpret-v2 werden nach Basis- und Schlussfreigabe lokal gerendert.
Aktuelle Paket-/Claim-/Interpretationssnapshots, Kernansichts-A-Claims und aktuelle
Matrixzuordnungen sind erforderlich. Keine finale HTML bei Materialfehlern oder
blockierenden Fragen. Keine zusätzlichen LLM-Aufrufe für Darstellung.
Spalten/Skalen aus Vergleichsplan, Vier-Cluster-Netz aus aktuellen Firmendaten,
Quellen mit Belegstellen, aufklappbare Karten und optionale Person-/Regionalansicht.
Keine Horváth-Kapitel oder gesonderten Unternehmens-Deep-Dives.

## Tatsächlich geprüft
- 50 unittest-Tests: bestehende Fakten-/Interpretationskontrollen plus Renderer-
  Gates, Zuordnungssnapshots, Quellen/Links, Datumsfehler, sichere Serialisierung,
  Netzwerk-Fallback, optionale Person und CLI-Dateischutz.
- Python-Kompilierung der Skripte; neun geänderte Skills per quick_validate gültig.
- Reproduzierbarer vollständiger Offline-Beispiellauf mit 17 synthetischen Fakten,
  12 Interpretationen, vier Matrixzellen und fünf Netzwerkkanten.
- Inline-Skripte in kleinem DOM tatsächlich ausgeführt: Netzwerkaufklappen,
  Querverbindungen, Kantenauswahl/Quellendetails, Suche/Reset, Tastatur-Knotenauswahl,
  Quellen-Seitenwechsel/Details und Öffnen/Wiederherstellen des Druckzustands.
- Statische Tabelle enthält alle Beziehungen und optionale Quoten/Produktbezüge;
  JavaScript erzeugt keine doppelten Tabellenzeilen.

Zusätzlich: unabhängiger Skill-Forward-Lauf mit aktuellem Vollrenderer, 13 Renderer-
Tests, zehn statischen Ausgabechecks und dem begrenzten DOM-Laufzeittest bestanden.
Keine echten Firmeninhalte, Webabrufe oder Live-Systemänderungen im Test.

## Nicht geprüft / Grenzen
Beim ursprünglichen Schritt-5-Stand war kein Chromium-Executable verfügbar. Deshalb damals keine
visuelle Browser-, Mobil- oder Drucklayout-Abnahme; kleine DOM-Prüfung ersetzt
keine echte Browser-/Touch-/CSS-Prüfung. Quellen-URLs des Beispiels nicht geöffnet.
Alle Beispieldaten und Reviewer-Urteile simuliert. Keine tatsächliche Firmen-
recherche oder Inhaltsfreigabe behaupten. Kein realer Token-/Kostenbenchmark.
Zum damaligen Stand waren spezielle regionale Zeitreihen, Landkarten und frei
entworfene Marktgrafiken noch kein generischer Rendererbestandteil; aktuelle
Markt-Zeitreihen siehe Ergänzung vom 12.10.2026 unten. Dokumentcache folgt.

## Ergänzung 11.10.2026: Executive Summary
Der Positionierungsagent wählt drei Highlights aus der vorhandenen A-Faktenbasis;
weiterhin 4–6 Kernaussagen, kurze Titel/Vorschausätze und vertiefbare Details.
Zahl/Status, Einheit, Zeitraum, Bezugsobjekt und Reihenfolge werden im regulären
I-Claim geprüft und fingerprintgebunden. Keine zusätzliche Recherche-/Prüfrolle.

- 59 unittest-Tests bestanden; neue Tests prüfen 4/5/6 Karten, Grenzen der
  Vollausgabe, Faktenbasis A, Kurzfelder, Darstellungsänderungen/Review-Barrieren,
  Reihenfolge, Quellenlinks und HTML-Escaping.
- Die drei geänderten Skills sind per quick_validate gültig; Python-Syntax gültig.
- Echter Offline-Chromium-Test: 4/5/6 Karten bei 1440/1024/390 Pixeln, Dialoge
  per Klick/Tastatur, Escape/Schließen/Hintergrund, direkte Originalquellen,
  Claim-Navigation, ausgeklappter/wiederhergestellter Druckzustand und native
  details ohne JavaScript. Keine Browser-JavaScript-Fehler.
- Desktop-Summarys visuell kontrolliert. Unabhängiger Positionierungs-Forward-Lauf
  aus synthetischen Fakten: passende Kapazitäts-/Markt-/Status-Highlights,
  korrekte Einschränkungen und vier Kernaussagen; formal gültiges JSON.

Alle Beispielinhalte und Review-Urteile bleiben simuliert; keine echten
Unternehmensquellen geprüft und kein Token-/Kostenbenchmark durchgeführt.
Die neue Browserabnahme betrifft die Executive Summary, nicht ein vollständiges
Redesign oder eine erneute visuelle Abnahme sämtlicher übriger Module.

## Ergänzung 11.10.2026: Aktuelle Entwicklungen
Kompakte vertikale Zeitachse mit Datum links, kurzer klickbarer Ereigniskarte
rechts und gemeinsamem Detailfenster. Vollständige A-Fakten, Aussageursprung,
Unsicherheiten, direkte Originalquellen und Belegstellen bleiben erhalten.
Bekannte Ereignisse chronologisch, unbekannte Datumsangaben sichtbar zuletzt;
keine neuen Interpretationen oder zusätzliche Modellrunde. Bestehender events-
Vertrag bleibt nutzbar. Aktuelle Abnahme und künftige Ausgabeprüfungen richten
sich auf die Desktop-Webansicht.

- 63 unittest-Tests bestanden, einschließlich Ereignisreihenfolge, offenen Daten,
  Mehrfachbelegen/Unterabschnitten, Mapping-Review, Escaping und leerer Timeline.
- Desktop-Chromium bei 1440/1280/1024 Pixeln: Datum/Karte, kompakte Zeilen,
  Öffnen per Tastatur, vollständige Aussagen, direkte Quellen und Claim-Navigation.
  Summary mit 4/5/6 Karten, Schließen/Escape/Hintergrund, Druckzustand sowie native
  Details ohne JavaScript weiterhin gültig; keine Browser-JavaScript-Fehler.
- Ereignismodul visuell am Desktop kontrolliert; DOM-Laufzeittest, Python-Syntax
  und quick_validate der beiden geänderten Skills bestanden.
- Reproduzierbares Beispiel: 21 synthetische Fakten, 15 Interpretationen,
  drei Ereignisse. Keine echten Quellen geöffnet oder Inhaltsfreigabe behauptet.

## Cluster und Gesprächspartner
- Vier Bereichsfelder in fester 2×2-Reihenfolge; gleiche Höhen innerhalb einer Zeile,
  dynamische Höhe bei mehr Akteuren. Namen unter den Formen, keine Score-Badges.
- Alle Kreise gleich groß, feste Größenbasis und passende Farbe/Form je Knotenart.
- Gebogene Kanten mit Richtungspfeilen ohne Endpunktkreise; Mehrfachbeziehungen
  bleiben einzeln erreichbar, gegenläufige Beziehungen haben beide Pfeile.
- Normales vertikales Seitenscrollen, nur lokales horizontales Scrollen der Grafik.
- Auswahl aktualisiert die feste rechte Spalte ohne Dialog, Filter löschen veraltete Details.
- Profile zeigen Snapshot, chronologische Stationen, Fachprofil, Verantwortung und
  belegten regionalen Kontext; leere Felder erhalten eine neutrale Lückenanzeige.
- Öffentliche Rollen-/Datumsunsicherheiten und direkte Quellen bleiben sichtbar.

Themenkarten: Kurz­titel und Vorschau, vollständige Inhalte/Originalquellen per Klick,
keine neuen Behauptungen in Vorschauen. SWOT: Kategorienamen und vier unterscheidbare
Farben prüfen (Stärken grün, Schwächen rot, Chancen blau, Risiken orange).

Clusterstandard 2026-10-12: Template und Ausgabevorgaben auf den bestätigten
Originalstil umgestellt. 81 Unit-Tests und Desktop-Browserprüfung bei 1440, 1280
und 1024 Pixeln bestanden, einschließlich Seitenscrollen, rechter Detailspalte,
Filter, Quellen, Druckzustand und Fallback ohne JavaScript. Zusätzlich das bereits
vorhandene Rheinmetall-Netz mit 43 Knoten und 54 Beziehungen visuell geprüft:
alle Akteure erreichbar, keine Symbolüberlappung, Bereichshöhen wachsen je Zeile.
Das ist eine Darstellungsprüfung vorhandener Daten, keine neue Inhaltsfreigabe.

## Capability Matrix 12.10.2026
Bestätigter Quantum-Systems-Stil: gleich hohe Kurztextzellen, große Evidenzstufen
mit tatsächlichem Kriterienmaximum, sichtbare Referenz und neutrale Profile/
Kennzahlen. Einzelbewertung unter der Matrix; Spaltenkopf öffnet alle Wettbewerber
nach identischem Kriterium. Alle Einordnungen, Beleggrenzen, A-Fakten und Quellen
bleiben erhalten. headline/preview sind Teil des geprüften I-Claims/Fingerprints.

- 86 Unit-Tests bestanden: u. a. freie Skalenanker, Profil/Kennzahl ohne
  künstlichen Evidenzscore, fehlende Evidenz vs. Nichtanwendbarkeit, vollständige
  statische Inhalte, HTML-Escaping und Review-Bindung der Kurztexte.
- Desktop-Browser bei 1440/1280/1024 Pixeln: gleich hohe Zellen ohne Textverlust,
  Auswahl mit Maus/Enter/Leertaste, Kriterienvergleich, direkte Originalquellen,
  Quellen-Seitenwechsel, Druck mit allen Bewertungen und wiederhergestellter
  Ansicht, native Details ohne JavaScript; keine JavaScript-Fehler.
- Bereits vorhandene Rheinmetall-Inhalte zusätzlich als Darstellungsprüfung:
  sieben Angebote, 35 Bewertungen, 90 Faktenblöcke und fünf Kriterienvergleiche
  vollständig erreichbar. Keine neue Recherche oder Inhaltsfreigabe behauptet.

## Markt-Deep-Dive 12.10.2026
Generische Vergleichsoberfläche nach markt-deepdive.md: Kontext-/Segmentkennzahl
und Wachstum, deduplizierte Programme nach Status, industrielle Rollen je Funktion
und Länderdetails mit Programmfenstern, Marktzugang, Zeitreihen/Methode/Quellen.
Gemeinsame Achsen, negative Entwicklung links der Null, keine erfundenen Werte.
Plan/Prognose und inkompatible Daten bleiben außerhalb des Ist-Vergleichs.
Alle Dashboard-Zuordnungen sind an den Paket-Snapshot und aktuelle A-Reviews
gebunden; required_full_review_ids umfasst sämtliche verwendeten Fakten.

- 98 Unit-Tests bestanden: Jahre/Einheiten/IDs/Referenzen, endliche Werte,
  Nullwert vs. Datenlücke, CAGR/negative Entwicklung, Plan/Prognose, Deduplikation,
  Status-/Zeitfensterdaten, Mehrfachrollen, optionale Segmentkennzahl, Escaping,
  vollständige statische Inhalte und Review-/Zuordnungsbarrieren.
- Offline-Desktop-Chromium bei 1440/1280/1024 Pixeln: nebeneinanderliegende
  Größen-/Wachstumscharts, vollständige Rollentexte, Balken-/Zellklick,
  Länderauswahl, drei Detailreiter, Tastatur, Programmfenster, direkte Quellen,
  Claim-Seitenwechsel, alle Länder im Druck und wiederhergestellter Zustand,
  vollständiger Fallback ohne JavaScript. Keine JavaScript-Fehler.
- Bestehende Desktopprüfung für Portfolio, Cluster, Capability Matrix, Profile,
  Seitenwechsel und Druck weiterhin bestanden. Marktübersicht und Programm-
  Vertiefung visuell kontrolliert; Python-Syntax und zwei geänderte Skills gültig.
- Reproduzierbares Beispiel: 65 synthetische Fakten, 17 Interpretationen,
  drei Testländer, sechs Programme und drei Industriefunktionen. Zahlen und
  Reviewer-Urteile ausschließlich simuliert, keine echten Quellen geöffnet.
- Unabhängiger market-facts-Lauf aus anderen fiktiven Dokumenten: 13 M-Claims,
  zwei Länder/zwei Programme, formal gültiges Dashboard. Historische Genehmigung
  von aktuellem Vertrag getrennt, keine doppelte Programmzählung, geplante
  Auslieferung nicht als begonnen gewertet; fehlende Werte/Rollen/Zugangsregeln
  offengehalten. Kein reales Inhaltsreview oder Quellenfreigabe behauptet.

Künftige regionale Aufträge verwenden recherchierte Daten ihres aktuellen Laufs;
keine firmenspezifischen Testwerte oder festen Länder/Funktionen im Renderer.
Alte Faktenpakete ohne Dashboard bleiben mit Themen-/Regionenkarten nutzbar.

## Modulspezifische Keyfacts & Insights 13.10.2026
Bestätigte kompakte Karten direkt unter Portfolio, Cluster und Markt-/Wettbewerbs-
darstellung auf Seite 1. Je Modul 1–3 Punkte mit Titel, belegtem fact_text und
statement als Insight. Herleitung, Unsicherheit, vollständige A-Fakten, direkte
Originalquellen und Belegstellen in nativen Details. Auswahl im bestehenden
Positionierungsschritt, alle sichtbaren Felder/Zuordnungen im I-Fingerprint;
keine zusätzliche Recherche-/Agenten-/Designrunde für reale Briefings.

- 112 Unit-Tests bestanden, einschließlich 1/2/3 Karten ohne Auffüllen,
  Obergrenze/Reihenfolge, direkte eindeutige Faktenreferenzen, A-/Quellenbindung,
  Änderungen von Titel/Fakt/Insight/Modul/Referenzen, explizite Gaps, sichere
  Ausgabe, keine doppelten Einordnungskarten, alte Kontexte und Markt ohne Matrix.
- Offline-Desktop-Chromium bei 1440/1280/1024 Pixeln: richtige Modul-/Seitenposition,
  gleich hohe Karten ohne Textverlust, geschlossene Details, Öffnen per Tastatur,
  Herleitung/Unsicherheit/Originalquellen, Claim-Navigation, Druck mit allen Karten
  und Fakten sowie wiederhergestellter Zustand, vollständig ohne JavaScript.
- Bestehende Desktopprüfung für Portfolio, Cluster, Capability Matrix, Profile,
  Seitenwechsel und Druck weiterhin bestanden; keine JavaScript-Fehler.
- Karten aller drei Module visuell kontrolliert, Python-Syntax gültig und vier
  geänderte Skills per quick_validate bestanden.
- Beispiel jetzt 65 synthetische Fakten und 24 Interpretationen, darunter sieben
  modulspezifische Karten (Portfolio 3, Cluster 2, Markt 2). Alle Daten/Reviews
  bleiben erfunden; keine echten Unternehmensquellen geöffnet oder freigegeben.
- Unabhängiger positioning-analysis-Lauf aus anderen bereitgestellten fiktiven
  A-Fakten: fünf formal gültige Karten (1/2/2), passende Produkt-/Partner-/Markt-
  Bezüge, Zuschreibungen und Grenzen erhalten, keine künstlichen Scores, keine
  Rasterfüllung. Dies ist eine Workflowprüfung, kein reales Inhaltsreview.

Kontexte ohne module_insights bleiben kompatibel. Neue Vollbriefings beauftragen
--module-insights mit selektiven A-Auszügen und folgen references/modul-keyfacts.md.
Explizite Gaps zeigen nur eine neutrale Systemmeldung, keine freie ungeprüfte
Unternehmensbehauptung. Der regionale Markt-Deep-Dive auf Seite 3 bleibt separat.

## Regionale Präsenz 13.10.2026
Bestätigter Stil der gelieferten Quantum-Systems-HTML: Regionszeilen unmittelbar
vor Wettbewerb/Capability Matrix auf Seite 1, fünf gleich große Kreise und n/5,
Fokusregion gold, konkrete Präsenzart und Produktumfang. Klick öffnet darunter das
Regionsprofil mit Aktivitäten, Stufenbegründung, Reichweite, Originalquellen und
Belegstellen. Unternehmensweite Recherche im bestehenden Portfolio-Schritt;
Positionierung und beide Reviews prüfen die feste Skala regional-presence-v1.
Alle Zuordnungen, Status-/Kontrollbelege, Stufen und Kurztexte sind snapshotgebunden.

- 126 Unit-Tests bestanden: fünf Stufen und null, operative vs. angekündigte
  Aktivitäten, eigene/Partner-/JV-/Kundenrollen, Standort-Deduplikation,
  Produktionsanker für Stufe 5, direkte Abhängigkeiten, Quellen-/Review-Bindung,
  aktuelle Zuordnung/Methodik, SWOT-Grenzen, alte Kontexte und sichere Ausgabe.
- Offline-Desktop-Chromium bei 1440/1280/1024 Pixeln: korrekte Modulposition,
  vollständige Zeilen ohne Überlauf, identische Kreise, Fokusfarbe, Regionsauswahl
  per Maus/Enter, Begründung/Methodik, direkte Quellen und Claim-Navigation.
  Druck mit allen Profilen/Quellen und wiederhergestellter Ansicht, vollständiger
  Fallback ohne JavaScript; keine Browser-JavaScript-Fehler.
- Bestehende Desktopprüfung für Portfolio, Cluster, Capability Matrix, Profile,
  Seitenwechsel und Druck weiterhin bestanden. Übersicht und Regionsprofil
  visuell kontrolliert; Python-Syntax und fünf geänderte Skills gültig.
- Beispiel jetzt 71 synthetische Fakten und 29 Interpretationen; sechs Testregionen
  zeigen 5/4/3/2/1/null. Alte zusätzliche Portfolio-Regionsbelege bleiben auf Seite 1
  erhalten, ohne vollständig abgedeckte Inhalte doppelt darzustellen.
- Unabhängiger Portfolio- und anschließender Positionierungs-Forward-Lauf aus
  anderen fiktiven Dokumenten: fünf P-Fakten und vier Regionen formal gültig;
  Produktion/Entwicklung am selben Standort korrekt als ein Standort, geplantes
  Werk nicht operativ, ziviler Vertriebspartner ohne Defence-Ausweitung,
  Kundenverkauf ohne Infrastrukturstufe, unbelegte Region offen. Positionierung
  liefert vier formal gültige Einordnungen mit 5/2/null/null und passenden Grenzen.

Sämtliche Testquellen und Reviewer-Urteile sind fiktiv/simuliert. Keine echten
Unternehmensquellen geöffnet und keine tatsächliche Inhaltsfreigabe behauptet.
Künftige Vollbriefings recherchieren die aktuellen Firmen-/Regionsdaten neu und
beauftragen --presence; der allgemeine Markt-/Industrie-Deep-Dive bleibt auf Seite 3.

## Cluster und technischer Vergleich 16.10.2026
Die bereitgestellte Rheinmetall-HTML wurde ausschließlich aus ihrem vorhandenen
Inhalt neu dargestellt; ihr fachlicher Stichtag bleibt 13.10.2026. Keine neue
Recherche oder Quellenfreigabe. Generische Vorgaben stehen in
`netzwerk-html.md` und `capability-matrix.md`, nicht in Agentenkontexten.

- Cluster: Radius 22, fünf Akteure je voller Bereichsreihe, vier Kategorien im
  bisherigen 2×2-Raster mit gleicher Höhe je Bereichsreihe. 39 Knoten und 51
  Kanten unverändert; Formen, Farben, Filter und rechte Detailansicht erhalten.
- Vergleich: fünf technische Kriterien mit 45 Faktenprofilen für neun Angebote;
  18 bisherige Beschaffungs-/Industriebewertungen unverändert. 36 zusätzliche
  Markt-/Integrationsprofile bleiben separat zugänglich. Technische Angaben
  bekommen keinen künstlichen Leistungsscore. Fehlende Angaben beziehen sich
  ausdrücklich auf die vorliegende HTML, nicht auf die gesamte öffentliche Lage.
- Alle 360 Quellenregister-Claims sowie übrige Module unverändert; keine
  doppelten IDs oder ungültigen internen Links. JavaScript-Syntax geprüft.
- Offline-Chromium mit der überarbeiteten HTML bei 1440/1280/1024 Pixeln:
  fünf Symbole je voller Reihe, alle Knoten/Kanten und Details bedienbar, keine
  globale horizontale Überbreite. Matrix mit sieben Spalten, technischem
  Erstprofil, vollständigen Zell-/Spaltendetails und sichtbaren Datenlücken.
  Druck und Fallback ohne JavaScript vollständig; keine JavaScript-Fehler.
  Netzwerk und Matrix zusätzlich visuell kontrolliert.
- Alle 187 Python-Tests bestanden. Dies prüft Darstellung und Bestandserhalt,
  ersetzt keine erneute fachliche Prüfung der ursprünglichen Recherche.
