---
name: briefing-ausgabe
description: Führt Teilergebnisse eines Firmenbriefings mit dem Skript scripts/briefing.py zusammen, validiert sie, wertet eine Prüfung aus und rendert die Dateien briefing.html, briefing-geprueft.html und briefing-daten.xlsx. Liest Daten aus einer hochgeladenen Briefing-HTML oder Excel zurück. Immer verwenden, wenn Briefingdaten gespeichert, ausgegeben, fortgesetzt oder geprüft werden.
---

# Briefing-Ausgabe

Die HTML entsteht ausschließlich durch das Skript `scripts/briefing.py` in diesem
Skill. Schreibe oder ändere nie selbst HTML. Das Skript nutzt nur die
Python-Standardbibliothek; die Excel-Befehle brauchen openpyxl.

Rufe das Skript mit seinem vollständigen Pfad im Skillordner auf; die
Arbeitsdateien liegen im Arbeitsverzeichnis. Ist der Pfad unklar, suche die Datei
`briefing.py` im Dateisystem. Prüfe zu Beginn mit `version`, dass das Skript läuft
(erwartet: Schema firmenbriefing/1).

## Befehle

```bash
python3 scripts/briefing.py version
python3 scripts/briefing.py zusammenfuehren --daten briefing-daten.json --teil teil-portfolio.json
python3 scripts/briefing.py zusammenfuehren --daten briefing-daten.json --teil korrektur.json --ersetzen
python3 scripts/briefing.py validieren --daten briefing-daten.json
python3 scripts/briefing.py rendern --daten briefing-daten.json --out briefing.html
python3 scripts/briefing.py excel --daten briefing-daten.json --out briefing-daten.xlsx
python3 scripts/briefing.py extrahieren --html briefing.html --out briefing-daten.json
python3 scripts/briefing.py aus-excel --xlsx briefing-daten.xlsx --out briefing-daten.json
python3 scripts/briefing.py auswerten --daten briefing-daten.json
```

Gibt es `briefing-daten.json` noch nicht, legt der erste `zusammenfuehren` sie an;
der erste Teil muss dann den Block `auftrag` enthalten.

## Ablauf beim Erstellen

1. Nach jeder Phase den Teil schreiben und `zusammenfuehren` aufrufen.
2. `validieren` aufrufen. **Fehler** sofort im Teil beheben und den Teil erneut
   mit `--ersetzen` zusammenführen. **Hinweise** beheben, wenn sie einen echten
   Mangel zeigen; sonst bleiben sie in der Abnahme sichtbar.
3. `rendern` nach `briefing.html`. Das Skript verweigert die Ausgabe bei Fehlern.
4. Zwischenstand: Nach jeder abgeschlossenen Phase `briefing.html` als Datei
   ausgeben. Die Daten stecken in der HTML; damit lässt sich später fortsetzen.
5. Am Ende zusätzlich `excel` nach `briefing-daten.xlsx` für die Prüfung und zum
   Nachbearbeiten.

## Fortsetzen

Bei „weiter“ oder in einer neuen Runde: Fehlt `briefing-daten.json` im
Arbeitsverzeichnis, lies die zuletzt erzeugte oder hochgeladene `briefing.html`
mit `extrahieren` bzw. die Excel mit `aus-excel` zurück. `phasen` zeigt, wo es
weitergeht. Nie neu beginnen, wenn ein Zwischenstand vorhanden ist.

## Ablauf beim Prüfen

1. Hochgeladene Datei einlesen: `.html` mit `extrahieren`, `.xlsx` mit `aus-excel`.
2. Prüfergebnisse als Teil `{"pruefung": {…}}` schreiben und zusammenführen.
3. `auswerten` aufrufen; es setzt das Gesamtergebnis nach festen Regeln.
4. `validieren`, dann `rendern` nach `briefing-geprueft.html` und `excel` nach
   `briefing-daten.xlsx`.

## Ausgaberegeln

- Dateinamen: `briefing.html` ungeprüft, `briefing-geprueft.html` nach Prüfung,
  `briefing-daten.xlsx` als Übergabe.
- Keine Rohdaten oder langen JSON-Blöcke in den Chat schreiben.
- Läuft das Skript nicht, sag das klar, nenne die Fehlermeldung und gib keine
  selbst geschriebene HTML aus.
