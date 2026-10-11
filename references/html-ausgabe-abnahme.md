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
Spezielle regionale Zeitreihen, Landkarten und frei entworfene Marktgrafiken sind
noch kein generischer Rendererbestandteil. Gemeinsamer Dokumentcache folgt.

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
