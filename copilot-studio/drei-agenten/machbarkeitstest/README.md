# Machbarkeitstest (etwa 30 Minuten)

Zweck: vor dem eigentlichen Einsatz klären, ob der Mandant kann, worauf das
Paket baut. Ergebnisse in testprotokoll.md eintragen.

## Vorbereitung

1. Im Agent Builder einen Testagenten „Briefing-Test“ anlegen. Websuche an,
   „alle Websites durchsuchen“.
2. Unter Skills `briefing-machbarkeit.zip` hochladen.
3. Instructions: „Du führst den Machbarkeitstest des Firmenbriefings mit dem
   Skill briefing-machbarkeit aus. Berichte Ergebnisse wörtlich und ehrlich.“

## Proben mit dem Testagenten

| Nr. | Nachricht | Bestanden, wenn | Wenn nicht |
|---|---|---|---|
| 1 | Machbarkeitstest Schritt 1 | Ausgabe zeigt Python-Version und „Kennung: machbarkeit-1“ | Skill-Skripte laufen nicht; mit der IT klären |
| 2 | Machbarkeitstest Schritt 2 | machbarkeit.html und machbarkeit.xlsx erscheinen als Dateien; die HTML öffnet im Browser | Kommt die Excel nicht, ist die Übergabe zwischen den Agenten nicht möglich |
| 3 | Neuer Chat: machbarkeit.xlsx hochladen, „Machbarkeitstest Schritt 3“; danach dasselbe mit machbarkeit.html | „Ergebnis: OK“ mindestens für die Excel | Ohne Excel-Upload keine Übergabe zwischen den Agenten |
| 4 | „Machbarkeitstest Schritt 4: Öffne [Link auf einen aktuellen Geschäftsbericht als PDF] und nenne den Konzernumsatz mit Seitenzahl.“ | Zahl und Seite stimmen, der Agent sagt, dass er das Dokument geöffnet hat | Der Prüf-Agent kann Originale nur eingeschränkt prüfen |

## Proben mit den drei Agenten

| Nr. | Schritt | Bestanden, wenn |
|---|---|---|
| 5 | „Firmenbriefing Recherche“: „Nur Portfolio zu [bekannte Firma]“ | briefing-daten.xlsx kommt, Validierung ohne Fehler, Portfolio auf Produktebene |
| 6 | „Firmenbriefing HTML“: diese Excel hochladen | briefing.html öffnet im Browser, Reifematrix und Quellen klickbar |
| 7 | „Firmenbriefing Prüfung“: dieselbe Excel hochladen, „prüfen“ | briefing-daten-geprueft.xlsx kommt mit Urteilen und, falls nötig, Änderungsprotokoll |
| 8 | „Firmenbriefing HTML“: die geprüfte Excel hochladen | HTML zeigt Prüfstatus, Prüfbericht und Änderungen |

Je Probe Dauer, sichtbares Modell und verbrauchte Credits notieren, soweit
angezeigt.
