# Fiktives HTML-Beispiel

briefing-demo.html zeigt die feste Ausgabe mit synthetischen Daten für
Example Inspection. 23 Fakten, 17 Interpretationen, sechs Netzwerkkanten (fünf Akteurspaare),
vier auftragsbezogene Matrixzellen und feste vier Seiten. Die Executive
Summary zeigt drei auftragsbezogene Highlights (Kapazität, Kundenländer,
Erprobungsstatus) und vier vertiefbare Kernaussagen; keine feste Finanzkennzahlenliste.
Aktuelle Entwicklungen erscheinen als chronologische kompakte Ereigniskarten mit
Datum links und vollständigen Fakten/Originalquellen im gemeinsamen Detailfenster.
Alle Inhalte und Review-Entscheidungen sind erfunden; keine URL wurde geöffnet.
Die Beispiele sind keine Recherchevorlage für echte Firmen.
Portfolio: farbige Gruppen und sechs Reifestufen, zwei eingeordnete Produkte
und ein unbestimmbarer Service, Such-/Gruppen-/Stufen-/Ursprungsfilter und Tabelle.
Der gesamte Detailprofilbereich ist zunächst geschlossen. Produktklick öffnet
Block und Profil. Person, Markt-Deep-Dive Europa und Quellen stehen auf Seite 2–4.
Das Netzwerk zeigt vier Akteursgruppen, gerade Linien ohne Endpunkte und Quellen
in einer festen rechten Detailspalte. Das offene Personenprofil zeigt den Snapshot
und sichtbare Evidenz; unbelegte Werdegangsfelder bleiben als Datenlücke erkennbar.

Reproduzieren (aus Repositorywurzel):

```bash
python3 examples/build-demo.py --out /tmp/briefing-demo-run
python3 -m unittest discover -s tests -q
# Optional: playwright-core verfügbar machen und BRIEFING_CHROMIUM_PATH setzen.
node tests/check_design_browser.cjs /tmp/briefing-demo-run/briefing-demo.html
node tests/check_executive_browser.cjs /tmp/briefing-demo-run/briefing-demo.html
```

Der Generator erzeugt Fakten-/Interpretationspakete und ausdrücklich simulierte
Reviews nur für den Offline-Test. Nicht als tatsächliche Inhaltsfreigabe verwenden.
check_html_runtime.cjs nutzt nun ebenfalls die echte Browserprüfung; die vorherige
DOM-Nachbildung unterstützt native dialog/template nicht ausreichend.
Zusätzlich wurde die Executive Summary im echten Browser mit vier, fünf und
sechs Karten bei 1440, 1280 und 1024 Pixeln geprüft, einschließlich Ereigniskarten, Dialogen,
Quellenlinks, Druckzustand und Fallback ohne JavaScript. Das ersetzt keine
erneute Inhaltsprüfung oder Abnahme der übrigen Module nach späteren Änderungen.
Optional reproduzieren: playwright-core installieren und BRIEFING_CHROMIUM_PATH
auf ein Chromium-Executable setzen; dann tests/check_executive_browser.cjs mit
einem oder mehreren erzeugten HTML-Pfaden ausführen.
check_design_browser.cjs prüft zusätzlich Portfoliofilter, geschlossene Profile,
wiederholte Produktlinks, Netzwerkknoten/Kanten, Matrixdialoge, Seitenzuordnung,
Quellensuche, Tastaturnavigation, Druckzustand und native Fallbacks.
Alle Browserkontexte sind offline; nur Desktopbreiten werden geprüft.
