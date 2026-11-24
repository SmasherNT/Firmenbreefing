---
name: briefing-machbarkeit
description: Nur für den Machbarkeitstest des Firmenbriefings. Prüft mit scripts/probe.py, ob Skill-Skripte laufen, welche Umgebung und welcher Netzzugang bestehen, ob HTML- und Excel-Dateien ausgegeben und hochgeladene Dateien wieder eingelesen werden können. Verwenden, wenn der Nutzer „Machbarkeitstest“ schreibt.
---

# Machbarkeitstest

Führe genau die Schritte aus, die der Nutzer nennt, und berichte die Ausgabe des
Skripts wörtlich in einem Codeblock. Erfinde keine Ergebnisse. Läuft ein Befehl
nicht, nenne die Fehlermeldung.

## Schritt 1: Umgebung

```bash
python3 scripts/probe.py umgebung
```

## Schritt 2: Dateien erzeugen

```bash
python3 scripts/probe.py html --out machbarkeit.html
python3 scripts/probe.py excel --out machbarkeit.xlsx
```

Gib beide Dateien als Datei im Chat aus.

## Schritt 3: Hochgeladene Datei lesen

Der Nutzer lädt machbarkeit.html oder machbarkeit.xlsx hoch.

```bash
python3 scripts/probe.py lesen --datei <hochgeladene Datei>
```

## Schritt 4: Quelle öffnen

Öffne die vom Nutzer genannte URL mit deinen eigenen Werkzeugen, nicht mit dem
Skript. Nenne die erfragte Angabe mit Seite oder Abschnitt und sage ehrlich, ob
du das Dokument selbst geöffnet hast oder nur Suchergebnisse gesehen hast.
