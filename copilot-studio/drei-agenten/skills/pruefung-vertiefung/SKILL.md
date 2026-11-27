---
name: pruefung-vertiefung
description: Prüft ein vorhandenes Firmenbriefing aus briefing-daten.xlsx unabhängig gegen seine Quellen, korrigiert belegte Abweichungen direkt mit Änderungsprotokoll, vertieft Lücken und gewünschte Kapitel und passt abhängige Interpretationen an. Ergebnis ist briefing-daten-geprueft.xlsx. Verwenden bei „prüfen“, „vertiefen“ oder „prüfen und vertiefen“.
---

# Prüfung und Vertiefung

Vorher briefing-grundlagen laden. Du arbeitest unabhängig vom Recherche-Agenten:
Du öffnest die Quellen selbst und bestätigst nie aus eigenem Wissen. Die HTML
erstellst du nicht; das macht der Agent „Firmenbriefing HTML“.

## Ablauf

1. **Einlesen:** Hochgeladene Excel mit `aus-excel`, eine Briefing-HTML mit
   `extrahieren`. Danach `validieren`.
2. **Umfang:** Aus der Nachricht: „prüfen“ heißt alle Kapitel; „nur Portfolio
   prüfen“ oder ein anderes Kapitel nur dieses; „nur A-Fakten“ nur Stufe A;
   „vertiefe …“ nennt zusätzliche Vertiefungsthemen. In `pruefung.umfang` eintragen.
3. **Quellenprüfung** nach references/quellenpruefung.md: Urteil je Claim,
   A vollständig, B als Stichprobe.
4. **Korrigieren** nach references/quellenpruefung.md, Abschnitt Korrigieren.
5. **Vertiefen** nach references/vertiefung.md.
6. **Ableitungen** nach references/ableitungspruefung.md prüfen und anpassen.
7. **Abschluss:** Prüfteil `{"pruefung": {…}}` mit Urteilen, Vertiefung,
   Stichprobe und Hinweisen zusammenführen (`--pruefer`), dann `auswerten`,
   `validieren` ohne Fehler, `excel` nach `briefing-daten-geprueft.xlsx`.

## Arbeit in Runden

Ist die Prüfung zu groß für eine Antwort, arbeite kapitelweise. Nach jedem
Kapitel Urteile zusammenführen, Excel als Zwischenstand ausgeben und um „weiter“
bitten. Urteile und Änderungen werden über die Runden ergänzt.

## Regeln

- „Im Original bestätigt“ und „korrigiert“ nur mit gelesener Belegstelle im
  geöffneten Original. Ein Suchsnippet ist keine Originalprüfung.
- „Durch Suche gestützt“ nur mit einer unabhängigen, gelesenen Quelle; kopierte
  Pressemitteilungen zählen nicht.
- Das Gesamtergebnis setzt nur das Skript mit `auswerten`. Ein abweichender oder
  nicht belegter A-Fakt, der nicht korrigiert ist, lässt die Prüfung scheitern;
  offene A-Fakten machen sie unvollständig.
- Jede Änderung bleibt nachvollziehbar: das Skript schreibt alt, neu und Grund
  ins Änderungsprotokoll, die HTML zeigt es im Prüfbericht.
