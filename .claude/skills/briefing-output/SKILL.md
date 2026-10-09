---
name: briefing-output
description: Verdichtet geprüfte Firmen-, Themen- und Personenmodule zu einem HTML-Briefing.
---

Der Hauptagent verwendet diese Methode.
Lies input/auftrag.md, CLAUDE.md und alle references-Vorlagen sowie
work/portfolio.md, work/cluster.md, work/markt.md, work/kontext.md,
work/swot.md, work/review-basis.md und work/review-final.md.
Keine finale HTML bei offenen wesentlichen Fehlern erstellen.
Nur geprüfte Claims verwenden; keine neue Unternehmensbehauptung hinzufügen.
Erstelle output/briefing.html exakt nach references/briefing-struktur.md.
Priorisierte Nutzerthemen stehen vor der kompakten allgemeinen Firmenbasis.
Berufliches Personenprofil nur falls beauftragt; Nutzerrolle von verifizierter
Rolle trennen. Status, Datum und Unsicherheit auch beim Kürzen erhalten.
Jede Kernaussage auf Claim und Originalquelle verlinken. Lesbarkeit,
interne Links, mobile Darstellung und Druckansicht tatsächlich prüfen;
nicht ausführbare Kontrollen in der Abnahme als nicht geprüft kennzeichnen.
Erstelle output/abnahme.md gemäß Strukturvorlage. Dateipfade und Cloud-
Ausgabemöglichkeiten nennen. Keine öffentliche Veröffentlichung automatisch.

## Ausnahme für ausdrücklich beauftragte Modultests
Bei Modus modultest lies references/modultest.md. Die Delegation nennt
Testauftrag, Auswahl, Eingaben und Zielpfad. Diese Pfade ersetzen die festen
input/work/output-Pfade oben. Nicht gewählte Module sind keine Pflicht.
Im Standardlauf bleiben die obigen Regeln unverändert.

Im Modultest nur ausgewählte Kapitel rendern. Nach fehlerfreiem Basis-Review
ist kein SWOT-/Schluss-Review nötig. Ohne Basis-Review nur sichtbar ungeprüfter
Entwurf; bekannte wesentliche Fehler blockieren jede HTML-Ausgabe.
