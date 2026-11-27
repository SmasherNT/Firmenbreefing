---
name: interpretation
description: Leitet für ein Firmenbriefing aus den vorhandenen Fakten in briefing-daten.json die Executive Summary, Keyfacts je Modul, die Positionierung mit Produktreife, Wettbewerbseinordnung und regionaler Präsenz sowie eine themenbezogene SWOT ab. Keine Webrecherche, keine neuen Fakten.
---

# Interpretation

Vorher briefing-grundlagen laden; Skalen in references/skalen.md. Ergebnis ist
ein Teil `teil-interpretation.json` mit `interpretation`, `offen` und `phasen`.

## Regeln

- **Keine Websuche, keine neuen Fakten.** Grundlage sind nur Claims in
  `briefing-daten.json`. Fehlt ein Fakt, schreibe eine Lücke oder Frage in `offen`
  statt zu recherchieren.
- Jede Interpretation hat `basis` mit den tragenden Claim-IDs. Keine Zahl, die
  nicht in der Basis steht.
- Herstellerangaben bleiben Herstellerangaben; ein Kriteriumsvorsprung ist kein
  Gesamtvorsprung; eine Datenlücke ist keine Schwäche.
- Kurz schreiben: Aussage ein Satz, Begründung zwei bis drei Sätze, Unsicherheit
  nur die konkrete Grenze. Gemeinsame Grenzen einmal in `grenzen`.
- B-Fakten tragen keine Interpretation; nötige B-Fakten im Teil auf A hochstufen.
- Bei Modulauftrag nur, wenn Interpretation ausdrücklich beauftragt ist.

## Executive Summary

- **Drei Highlights:** auftragsbezogene Kennzahlen oder Status aus verschiedenen
  Perspektiven, nicht automatisch die größte Zahl. Label höchstens 60 Zeichen,
  Wert mit Einheit oder kurzer Status, Bezugsobjekt, Zeitraum. Ziel, Prognose
  oder Kapazität schon im Label kennzeichnen. Weniger als drei nur ohne Beleg.
- **Vier bis sechs Kernaussagen:** nach Bedeutung für den Auftrag sortiert.
  Titel höchstens 72 Zeichen, Vorschau höchstens 160 Zeichen, vollständige
  Aussage, Begründung, Unsicherheit. Keine generischen Füllpunkte.

## Keyfacts je Modul

Für Portfolio, Cluster und Markt je ein bis drei Karten: Titel, belegter Fakt,
daraus abgeleiteter Insight. Keine Wiederholung der Summary. Ohne belastbaren
Punkt keine Karte und eine Lücke in `offen`.

## Produktreife (`reife`)

Für **jedes** Angebot im Portfolio genau ein Eintrag: `angebot` (exakter Name),
`stufe` 1 bis 6 nach der Portfolio-Skala oder `null`, `aussage`, `begruendung`,
`unsicherheit`, `naechste_stufe` (warum die nächste Stufe nicht belegt ist),
`basis`. Die HTML zeigt daraus die Reifematrix. Herstellerangaben bleiben als
solche erkennbar; eine Beleglücke ist keine Unreife.

## Regionale Präsenz (`praesenz`)

Für jede Region aus `markt.praesenz` genau ein Eintrag: `region` (exakter Name),
`stufe` 1 bis 5 nach der Präsenzskala oder `null`, `status` (bewertet, geplant,
nicht eindeutig bestimmbar), `aussage`, `begruendung`, `naechste_stufe`, `basis`.
JV-Kontrollregeln beachten; nur Angekündigtes heißt „geplant“ ohne Stufe.

## Positionierung (`positionierung`)

Je Eintrag `dimension`, kurzes `urteil`, `aussage`, `methode`, `begruendung`,
`unsicherheit`, `basis`. Mindestens:

1. **Wettbewerb:** Einordnung entlang der Kriterien des Vergleichs. Ein
   Kriteriumsvorsprung ist kein Gesamtvorsprung; keine Summen aus Stufen.
2. **Netzwerk:** Bedeutung belegter Beziehungen für Zugang, Integration und
   Abhängigkeit als begründete Einschätzung, keine berechneten Kennzahlen.
3. Weitere auftragsbezogene Dimensionen, wenn die Fakten sie tragen.

## SWOT

- Stärken und Schwächen sind interne, bestehende Fähigkeiten und Grenzen;
  Chancen und Risiken sind externe Entwicklungen.
- Standardmäßig drei eigenständige belegte Punkte je Quadrant, höchstens drei.
  Weniger nur, wenn die Fakten keinen sinnvollen dritten Punkt tragen; dann die
  Grenze in `grenzen`. Dieselbe Aussage nicht aufteilen.
- Bezug zu den Fokusthemen des Auftrags. Produktmerkmal ohne begründeten Vorteil
  ist keine Stärke. Basis darf Positionierungs-IDs enthalten.

## Offen

Datenlücken, Widersprüche und neutrale Gesprächsfragen in `offen.luecken` und
`offen.fragen`, keine Behauptungen über die Firma.

`phasen: {"interpretation": "fertig"}`, zusammenführen, validieren.
