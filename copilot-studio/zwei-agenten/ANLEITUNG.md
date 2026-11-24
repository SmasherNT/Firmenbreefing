# Schritt-für-Schritt-Anleitung: Firmenbriefing in Microsoft 365 Copilot

Gilt für das heruntergeladene Paket `firmenbriefing-copilot-paket.zip`.
Menünamen können je nach Copilot-Version leicht abweichen.

## Teil 1: Vorbereitung (5 Minuten)

1. `firmenbriefing-copilot-paket.zip` entpacken. Es entsteht der Ordner
   `firmenbriefing-copilot` mit `agenten`, `skills`, `machbarkeitstest`.
2. Die ZIP-Dateien in `skills` und `machbarkeitstest` **nicht** entpacken. Sie
   werden so hochgeladen, wie sie sind.
3. Die Textdateien (`.md`) mit einem einfachen Editor öffnen, z. B. Notepad
   oder VS Code, nicht mit Word. So bleibt der Text beim Kopieren sauber.

## Teil 2: Machbarkeitstest (etwa 30 Minuten)

4. Microsoft 365 Copilot öffnen. Links „Agents“ bzw. „Agents & Skills“, dann
   „New agent“ und „Configure“ bzw. „Skip to configure“.
5. Name: `Briefing-Test`.
6. Instructions einfügen:
   `Du führst den Machbarkeitstest des Firmenbriefings mit dem Skill briefing-machbarkeit aus. Berichte Ergebnisse wörtlich und ehrlich.`
7. Unter Knowledge „Search all websites“ einschalten.
8. Unter Skills „Add“ und `machbarkeitstest/briefing-machbarkeit.zip` hochladen.
9. Speichern bzw. „Create“ und den Agenten im Chat öffnen.
10. Nacheinander senden und die Ergebnisse in `machbarkeitstest/testprotokoll.md` eintragen:
    - `Machbarkeitstest Schritt 1` → erwartet: Python-Version und „Kennung: machbarkeit-1“.
    - `Machbarkeitstest Schritt 2` → erwartet: zwei Dateien, machbarkeit.html und machbarkeit.xlsx. Die HTML herunterladen und im Browser öffnen.
    - Neuer Chat, machbarkeit.html anhängen, `Machbarkeitstest Schritt 3` → erwartet: „Ergebnis: OK“. Dasselbe mit machbarkeit.xlsx.
    - `Machbarkeitstest Schritt 4: Öffne [Link auf einen aktuellen Geschäftsbericht als PDF] und nenne den Konzernumsatz mit Seitenzahl.` → Zahl und Seite selbst im PDF nachprüfen.
11. Auswerten:
    - Schritt 1 nicht bestanden: Skill-Skripte laufen nicht. Hier aufhören und mit der IT klären.
    - Schritt 3 nur mit Excel bestanden: später immer die Excel-Datei zur Prüfung hochladen.
    - Schritt 4 nicht bestanden: Der Prüfagent kann Quellen nur über die Suche bestätigen, nicht im Original.

## Teil 3: Agent „Firmenbriefing“ anlegen (10 Minuten)

12. „New agent“, „Configure“.
13. Name `Firmenbriefing`, Beschreibung aus `agenten/firmenbriefing/agent.md`.
14. Instructions: `agenten/firmenbriefing/instructions.md` öffnen, alles markieren,
    kopieren und vollständig einfügen.
15. Knowledge: „Search all websites“ einschalten.
16. Skills: diese acht Dateien aus `skills` hochladen:
    briefing-standards.zip, briefing-ausgabe.zip, firmenbasis-person.zip,
    portfolio.zip, cluster.zip, markt-wettbewerb.zip, fokusthema.zip, interpretation.zip.
17. Gesprächsstarter aus `agent.md` übernehmen, falls angeboten.
18. Speichern bzw. „Create“.

## Teil 4: Agent „Briefing-Prüfung“ anlegen (5 Minuten)

19. „New agent“, „Configure“.
20. Name `Briefing-Prüfung`, Beschreibung aus `agenten/briefing-pruefung/agent.md`.
21. Instructions aus `agenten/briefing-pruefung/instructions.md` vollständig einfügen.
22. Knowledge: „Search all websites“ einschalten.
23. Skills: diese vier Dateien hochladen:
    briefing-standards.zip, briefing-ausgabe.zip, quellenpruefung.zip, ableitungspruefung.zip.
24. Speichern bzw. „Create“.

## Teil 5: Erster Lauf

25. Im Agenten „Firmenbriefing“: `Nur Portfolio zu [bekannte Firma]`.
26. Erwartet: briefing.html und briefing-daten.xlsx. **Beide sofort
    herunterladen**, Dateien bleiben nur während der Sitzung abrufbar.
27. briefing.html im Browser öffnen: oben steht „Ungeprüfte Faktenbasis“,
    unten Faktenregister und Quellenregister mit klickbaren Links.
28. Im Agenten „Briefing-Prüfung“: briefing-daten.xlsx anhängen und `prüfen` senden.
29. Erwartet: briefing-geprueft.html mit Prüfstatus an jeder Aussage und
    Prüfbericht. Ebenfalls herunterladen.
30. Danach das Vollbriefing:
    `Briefing zu [Firma], Fokus: [Thema], Gesprächspartner: [Name], [Position]`.
    Bricht die Antwort ab, `weiter` schreiben.
31. Korrekturen: geprüfte Datei bei „Firmenbriefing“ anhängen und
    `Korrekturen umsetzen` schreiben. Danach erneut prüfen lassen.

## Häufige Probleme

| Problem | Lösung |
|---|---|
| Skill-Upload wird abgelehnt | Die ZIP-Datei hochladen, nicht den entpackten Ordner. Höchstens acht Skills je Agent. |
| Keine Skills-Option sichtbar | Lizenz oder Richtlinie fehlt; mit der IT klären. |
| Agent schreibt, das Skript laufe nicht | Machbarkeitstest Schritt 1 wiederholen; Fehlermeldung an die IT. |
| Agent beginnt nach „weiter“ von vorn | Die zuletzt erhaltene briefing.html anhängen und `weiter` schreiben. |
| Datei nach einiger Zeit weg | Dateien immer sofort herunterladen. |
| Neue Version des Pakets | In beiden Agenten die geänderten ZIP-Dateien entfernen und neu hochladen. |

## Variante Copilot Studio

Gleiche Instructions und ZIP-Dateien. Agent mit der Microsoft-Copilot-Laufzeit
anlegen, Skills unter „Build“, „Skills“, „Upload a skill“ hochladen, Websuche
einschalten. „Briefing-Prüfung“ veröffentlichen und bei „Firmenbriefing“ als
verbundenen Agenten hinzufügen. Dann genügt in Schritt 28 `prüfen` im selben Chat.
