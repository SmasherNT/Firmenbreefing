# Fiktives HTML-Beispiel

briefing-demo.html zeigt die feste Ausgabe mit synthetischen Daten für
Example Inspection. 17 Fakten, 12 Interpretationen, fünf Netzwerkkanten,
vier auftragsbezogene Matrixzellen, Profil und Regionalansicht.
Alle Inhalte und Review-Entscheidungen sind erfunden; keine URL wurde geöffnet.
Die Beispiele sind keine Recherchevorlage für echte Firmen.

Reproduzieren (aus Repositorywurzel):

```bash
python3 examples/build-demo.py --out /tmp/briefing-demo-run
node tests/check_html_runtime.cjs /tmp/briefing-demo-run/briefing-demo.html
```

Der Generator erzeugt Fakten-/Interpretationspakete und ausdrücklich simulierte
Reviews nur für den Offline-Test. Nicht als tatsächliche Inhaltsfreigabe verwenden.
Browser-/Mobil-/Drucklayout sind nicht visuell geprüft. Die Laufzeitprüfung nutzt
ein kleines DOM und prüft JavaScript-Verhalten ohne Browser/CSS-Rendering.
