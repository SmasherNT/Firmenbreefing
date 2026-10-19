# Fokusseiten – technische Abnahme vom 19.10.2026

Umgesetzt: eigener focus-analyst auf Sonnet 5.5 Medium, je Thema eigener Aufruf,
Kontext, Datei und focus:<id>-Checkpoint. Kernaussagen, flexible Grafikanzahl und
Sechsmonats-Timeline statt neuer separater Markt-Deep-Dive-Seite. Quellen zuletzt.
Historische Läufe ohne focus_pages bleiben wiederholbar.

Prüfungen:
- 221 Python-Tests bestanden, einschließlich separater Job-Zuständigkeit,
  fehlender/doppelter/fremder Fokusmodule, obligatorischer A-Quellenprüfung,
  Grafik-/Datumsvalidierung, Quellenreferenzen und veralteter Paket-Snapshots.
- Vollständiges synthetisches Vier-Kernrollen-Briefing mit vorhandener
  Positionierung/SWOT und zwei zusätzlichen Fokusseiten erfolgreich gerendert.
- Je Fokus unabhängige Checkpoints: Änderung eines Fokus invalidiert dessen
  Folgeartefakte, während der andere Fokus wiederverwendbar bleibt.
- Fokus-Claims werden aus Positionierungs-/SWOT-Kontexten ausgeschlossen.
- Chromium offline: zwei Fokusreiter, drei Grafiktypen, acht Timeline-Ereignisse,
  native Details, interne Sprünge zum Quellenregister, Druckzustand und Rückkehr,
  Desktopbreiten 1440/1280/1024 sowie Lesbarkeit ohne JavaScript bestanden.
- Screenshot visuell kontrolliert; git diff --check bestanden.

Reproduzierbare Aufrufe:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tests/build_focus_fixture.py /tmp/focus-fixture.html
BRIEFING_CHROMIUM_PATH=<Chromium> node tests/check_focus_browser.cjs /tmp/focus-fixture.html
```

Testdaten, Quellensichtungen und Reviewer-Urteile ausschließlich synthetisch.
Kein realer Firmen-/Fokusrecherchelauf und keine Sonnet-/Opus-API-Ausführung für
diese Abnahme. Tatsächlicher Tokenverbrauch, Laufzeit und Recherchequalität mit
der neuen Aufteilung sind daher noch nicht gemessen.
