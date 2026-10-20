# Neutrale Themen- und Marktbriefings – Implementierungsabnahme 20.10.2026

Standard für neue Fokusaufträge: briefing_type=topic_market. Der kurze Nutzerprompt
bleibt unverändert. Die separate Fokusinstanz recherchiert das Thema selbst,
mit Marktdefinition, Kennzahlen, Segmenten, Wertschöpfungsfunktionen, Akteuren,
Erkenntnissen, Grafiken, Sechsmonats-Timeline und neutralen Meetingfragen.
Historische Seiten ohne Typ bleiben renderbar. Datenvertrag und Neutralitätsprüfung
sind in fokusseiten.md sowie Fokus-/Leitprüferanweisungen verankert.

Lokaler Renderer zeigt Typ, Definition, Einheit, Periode und Scope jeder Zahl;
unterschiedlich abgegrenzte Karten erzeugen keine automatische Summe oder Rangfolge.
Marktumsatz/Budget, Rahmenhöchstwert/Auftrag/Lieferung und Kapazitätsziel/Ist-Ausstoß
bleiben unterscheidbar. Fehlende Kennzahlen/Abdeckung verlangen sichtbare Grenzen.
Alle neuen Faktentexte und Zuordnungen sind A-Pflicht und snapshotgebunden.

Tatsächlich bestanden:
- 226 Python-Tests, einschließlich historischer Verträge, vollständiger neuer
  Feldstruktur, unzulässiger/fehlender Kennzahlentypen und Werte, transparenter
  Datenlücken, Quellenreferenzen, HTML-Escaping und veralteter Akteurszuordnung.
- Vollständiger synthetischer Renderer-Lauf mit zwei neutralen Fokusinstanzen,
  acht Zahlenkarten, Akteurstabellen, Meetingfragen und internen Evidenzlinks.
- Statische HTML-Prüfung der synthetischen Ausgabe: eindeutige IDs, vorhandene
  interne Linkziele; git diff --check.

Nicht ausgeführt: Desktop-Browser-/Interaktions-/Druckprüfung der neuen Ansicht.
In der ausführenden Umgebung fehlt die Browserlaufzeit; die alternative Cloud-
Vorschau erlaubt keinen lokalen file://-Zugriff. Der erweiterte reproduzierbare
Browsercheck liegt in tests/check_focus_browser.cjs vor, sein Vorhandensein ist
kein bestandener Browsertest.

Diese Implementierungsabnahme verwendet synthetische Daten, keine tatsächliche
Firmenrecherche oder inhaltliche Quellenfreigabe. Das erneut erstellte Rheinmetall-
Briefing erhält seine eigene Inhaltsprüfung und output/abnahme.md. Tatsächliche
Ausführung hier durch Codex; konfigurierte Claude-Modelle wurden nicht ausgeführt.

Reproduktion:
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tests/build_focus_fixture.py /tmp/topic-market.html
BRIEFING_CHROMIUM_PATH=<Chromium> node tests/check_focus_browser.cjs /tmp/topic-market.html
```
