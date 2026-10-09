---
name: company-briefing
description: Erstelle aus einer kurzen Anfrage ein vollständiges HTML-Firmenbriefing mit vier Faktenrollen, zwei Interpretationsrollen, Reviews und fester HTML-Ausgabe. Nicht bei Einrichtung oder Systemfragen.
---

Lies CLAUDE.md, references/defaults.md und references/ausgabe-html-v2.md.
Einzelne Phasen/Modultests haben Vorrang. Bestehende Markdown-Läufe nur explizit
nach references/legacy-company-briefing.md; keine Legacy/v2-Mischläufe.
1. Firma, Themen in Nutzerreihenfolge, optionale berufliche Person/Rolle aus
   Nachricht übernehmen; Defaults ergänzen, kein Formular verlangen.
   Nur blockierende Mehrdeutigkeit klären. Unter runs/<neue_run_id>/input/
   Originalauftrag und facts-run.json erstellen. Alte Läufe erhalten.
   topics=[{id,label}], person als Nutzerangabe. Einrichtung ist kein Auftrag.
2. facts-briefing im delegierten Lauf mit context/portfolio/cluster/market
   ausführen. Alle vier Faktenagenten delegieren; Vergleichsplan vor
   Wettbewerbsrecherche aus Auftrag festlegen. Delegation nennt Identität,
   mode=facts-v2, Eingaben, Tabellenvertrag und exakten Zielpfad.
3. Paket lokal zusammenführen. source-reviewer prüft wesentliche Claims
   und module_views. Explizite Reviewer-Entscheidungen per stamp-review ergänzen.
4. interpretation-briefing mit Positionierung und SWOT ausführen. Positionierung
   liefert 4–6 executive_summary-I-Claims aus A-Fakten, die auftragsbezogene Matrix
   und Themen-/Produkt-/Industrie-/Regionaleinordnung. Nur selektive Kontexte.
   SWOT danach; ein gemeinsames Schluss-Review für beide Ableitungen.
5. briefing-output im selben Lauf mit --full ausführen. Hauptagent koordiniert
   und rendert; keine eigenen Fakten-/Interpretations-JSONs oder LLM-HTML.
6. output/abnahme.md mit tatsächlichen Agenten/Reviews/Prüfungen aktualisieren.
   Dateien im Arbeitsbranch committen/pushen; keine öffentliche Veröffentlichung.

Keine Horváth-Kapitel oder separaten Unternehmens-Deep-Dives; JV-Fakten bleiben
im Cluster. Neue Faktenfragen gezielt delegieren, erneut durch Basis-Review,
abhängige Interpretationen aktualisieren. Keine fremden Dateien umschreiben.
Nach zwei erfolglosen Korrekturrunden Materialfehler blockieren. Rückgabe kurz.
