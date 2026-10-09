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
Kein Chromium-Executable verfügbar; Browserstart nicht möglich. Deshalb keine
visuelle Browser-, Mobil- oder Drucklayout-Abnahme; kleine DOM-Prüfung ersetzt
keine echte Browser-/Touch-/CSS-Prüfung. Quellen-URLs des Beispiels nicht geöffnet.
Alle Beispieldaten und Reviewer-Urteile simuliert. Keine tatsächliche Firmen-
recherche oder Inhaltsfreigabe behaupten. Kein realer Token-/Kostenbenchmark.
Spezielle regionale Zeitreihen, Landkarten und frei entworfene Marktgrafiken sind
noch kein generischer Rendererbestandteil. Gemeinsamer Dokumentcache folgt.
