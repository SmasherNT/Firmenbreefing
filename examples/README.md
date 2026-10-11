# Fiktives HTML-Beispiel

briefing-demo.html zeigt die feste Ausgabe mit synthetischen Daten für
Example Inspection. 19 Fakten, 15 Interpretationen, fünf Netzwerkkanten,
vier auftragsbezogene Matrixzellen, Profil und Regionalansicht. Die Executive
Summary zeigt drei auftragsbezogene Highlights (Kapazität, Kundenländer,
Erprobungsstatus) und vier vertiefbare Kernaussagen; keine feste Finanzkennzahlenliste.
Alle Inhalte und Review-Entscheidungen sind erfunden; keine URL wurde geöffnet.
Die Beispiele sind keine Recherchevorlage für echte Firmen.

Reproduzieren (aus Repositorywurzel):

```bash
python3 examples/build-demo.py --out /tmp/briefing-demo-run
node tests/check_html_runtime.cjs /tmp/briefing-demo-run/briefing-demo.html
```

Der Generator erzeugt Fakten-/Interpretationspakete und ausdrücklich simulierte
Reviews nur für den Offline-Test. Nicht als tatsächliche Inhaltsfreigabe verwenden.
Die DOM-Laufzeitprüfung prüft JavaScript-Verhalten ohne CSS-Rendering.
Zusätzlich wurde die Executive Summary im echten Browser mit vier, fünf und
sechs Karten bei 1440, 1024 und 390 Pixeln geprüft, einschließlich Dialogen,
Quellenlinks, Druckzustand und Fallback ohne JavaScript. Das ersetzt keine
erneute Inhaltsprüfung oder Abnahme der übrigen Module nach späteren Änderungen.
Optional reproduzieren: playwright-core installieren und BRIEFING_CHROMIUM_PATH
auf ein Chromium-Executable setzen; dann tests/check_executive_browser.cjs mit
einem oder mehreren erzeugten HTML-Pfaden ausführen.
