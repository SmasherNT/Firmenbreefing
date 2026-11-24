# Machbarkeitstest (etwa 30 Minuten)

Zweck: vor dem Einrichten der beiden Agenten klären, ob der Mandant das kann,
worauf das Paket baut. Ergebnisse in testprotokoll.md eintragen.

## Vorbereitung

1. Im Agent Builder einen Testagenten „Briefing-Test“ anlegen. Websuche an,
   „alle Websites durchsuchen“.
2. Unter Skills die Datei `dist/machbarkeitstest/briefing-machbarkeit.zip` hochladen.
3. Instructions: „Du führst den Machbarkeitstest des Firmenbriefings mit dem
   Skill briefing-machbarkeit aus. Berichte Ergebnisse wörtlich und ehrlich.“

## Proben

| Nr. | Nachricht an den Testagenten | Bestanden, wenn | Wenn nicht |
|---|---|---|---|
| 1 | Machbarkeitstest Schritt 1 | Ausgabe zeigt Python-Version und „Kennung: machbarkeit-1“ | Skill-Skripte laufen nicht; Paket nicht nutzbar, Hinweis an die IT |
| 2 | Machbarkeitstest Schritt 2 | machbarkeit.html und machbarkeit.xlsx erscheinen als Dateien; die HTML öffnet im Browser | Erscheint nur die Excel, im Skill briefing-ausgabe PDF statt HTML ergänzen |
| 3 | Neuer Chat: machbarkeit.html hochladen, „Machbarkeitstest Schritt 3“; danach dasselbe mit machbarkeit.xlsx | „Ergebnis: OK“ für mindestens eine der beiden Dateien | Prüfung nur mit der Datei, die funktioniert |
| 4 | „Machbarkeitstest Schritt 4: Öffne [Link auf einen aktuellen Geschäftsbericht als PDF] und nenne den Konzernumsatz mit Seitenzahl.“ | Zahl und Seite stimmen mit dem PDF überein, Agent sagt, dass er das Dokument geöffnet hat | Prüfagent kann nur „durch Suche gestützt“ vergeben; Originalprüfung bleibt manuell |
| 5 | Mit dem fertigen Agenten „Firmenbriefing“: „Nur Portfolio zu [bekannte Firma]“ | briefing.html und briefing-daten.xlsx kommen, Validierung ohne Fehler, Quellen klickbar | Fehlermeldung des Skripts notieren |

Zusätzlich je Probe Dauer, sichtbares Modell und verbrauchte Credits notieren,
soweit angezeigt. Probe 1 zeigt auch, ob das Skript selbst Netzzugang hat; das
Briefing braucht ihn nicht.

## Nur in Copilot Studio

| Nr. | Nachricht | Bestanden, wenn |
|---|---|---|
| 6 | Im Chat mit „Firmenbriefing“ nach Probe 5: „prüfen“ | „Briefing-Prüfung“ übernimmt und bekommt die Datei |
