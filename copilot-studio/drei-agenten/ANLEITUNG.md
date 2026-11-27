# Schritt-für-Schritt-Anleitung: Firmenbriefing mit drei Agenten

Gilt für das Paket `firmenbriefing-drei-agenten.zip` im Agent Builder von
Microsoft 365 Copilot. Menünamen können je nach Version leicht abweichen.

## So arbeiten die drei Agenten zusammen

| Agent | Bekommt | Liefert |
|---|---|---|
| 1 Firmenbriefing Recherche | deinen Auftrag | briefing-daten.xlsx |
| 2 Firmenbriefing Prüfung (optional) | briefing-daten.xlsx | briefing-daten-geprueft.xlsx |
| 3 Firmenbriefing HTML | eine der beiden Excel-Dateien | briefing.html |

Jeder Agent arbeitet für sich. Du gibst die Excel-Datei von Hand weiter: herunterladen und beim nächsten Agenten hochladen.

## Teil 1: Vorbereitung (5 Minuten)

1. `firmenbriefing-drei-agenten.zip` entpacken. Es entsteht der Ordner
   `firmenbriefing-drei-agenten` mit `agenten`, `skills`, `machbarkeitstest`.
2. Die ZIP-Dateien in `skills` und `machbarkeitstest` **nicht** entpacken. Sie
   werden so hochgeladen, wie sie sind.
3. Die `.md`-Dateien mit einem einfachen Editor öffnen, nicht mit Word.
4. Falls die Agenten der Zwei-Agenten-Fassung schon existieren: nicht
   verändern, sondern die drei neuen Agenten zusätzlich anlegen. Die alten
   kannst du später löschen.

## Teil 2: Machbarkeitstest (etwa 30 Minuten)

5. Testagent anlegen nach `machbarkeitstest/README.md`, Proben 1 bis 4.
6. Wichtig sind vor allem Probe 2 und 3: Die Excel muss als Datei kommen und
   sich wieder hochladen lassen. Sonst funktioniert die Übergabe nicht.

## Teil 3: Agent „Firmenbriefing Recherche“ (10 Minuten)

7. Microsoft 365 Copilot öffnen, links „Agents“ bzw. „Agents & Skills“,
   „New agent“, „Configure“ bzw. „Skip to configure“.
8. Name `Firmenbriefing Recherche`, Beschreibung aus
   `agenten/recherche/recherche-einstellungen.md`.
9. Instructions: `agenten/recherche/recherche-instructions.md` vollständig einfügen.
10. Knowledge: „Search all websites“ einschalten.
11. Skills: sieben Dateien aus `skills` hochladen: briefing-grundlagen,
    firmenbasis-person, portfolio, cluster, markt-wettbewerb, fokusthema, interpretation.
12. Speichern.

## Teil 4: Agent „Firmenbriefing Prüfung“ (10 Minuten)

13. Neuer Agent `Firmenbriefing Prüfung`, Beschreibung und Instructions aus
    `agenten/pruefung/`.
14. „Search all websites“ einschalten.
15. Skills: acht Dateien hochladen: briefing-grundlagen, pruefung-vertiefung,
    firmenbasis-person, portfolio, cluster, markt-wettbewerb, fokusthema, interpretation.
16. Speichern.

## Teil 5: Agent „Firmenbriefing HTML“ (5 Minuten)

17. Neuer Agent `Firmenbriefing HTML`, Beschreibung und Instructions aus `agenten/html/`.
18. Websuche ausgeschaltet lassen.
19. Skill: `briefing-html.zip` hochladen. Speichern.

## Teil 6: Erster Durchlauf

20. Bei „Firmenbriefing Recherche“: `Nur Portfolio zu [bekannte Firma]`.
    Bei mehreren Runden jeweils `weiter`. Am Ende briefing-daten.xlsx herunterladen.
21. Bei „Firmenbriefing HTML“: briefing-daten.xlsx anhängen und
    `Erstelle die HTML` senden. briefing.html herunterladen und im Browser öffnen.
22. Optional bei „Firmenbriefing Prüfung“: briefing-daten.xlsx anhängen und
    `prüfen` senden, oder `prüfen und vertiefe [Thema]`. Am Ende
    briefing-daten-geprueft.xlsx herunterladen.
23. Die geprüfte Excel bei „Firmenbriefing HTML“ hochladen. Die neue HTML zeigt
    Prüfstatus, Prüfbericht und Änderungsprotokoll.
24. Danach das Vollbriefing:
    `Briefing zu [Firma], Fokus: [Thema], Gesprächspartner: [Name], [Position]`.
    Rechne mit 8 bis 12 Runden „weiter“.

## Häufige Probleme

| Problem | Lösung |
|---|---|
| Skill-Upload wird abgelehnt | ZIP-Datei hochladen, nicht den entpackten Ordner. Höchstens acht Skills je Agent. |
| Keine Skills-Option sichtbar | Lizenz oder Richtlinie fehlt; mit der IT klären. |
| Agent schreibt, das Skript laufe nicht | Machbarkeitstest Probe 1 wiederholen; Fehlermeldung an die IT. |
| Recherche beginnt nach „weiter“ von vorn | Die letzte briefing-daten.xlsx anhängen und erneut `weiter` schreiben. |
| HTML-Agent meldet Fehler | Die Fehler zeigen, welcher Agent nacharbeiten muss; Datei dort hochladen und die Fehler nennen. |
| Datei nach einiger Zeit weg | Dateien immer sofort herunterladen. |

## Variante Copilot Studio

Gleiche Instructions und ZIP-Dateien, Agenten mit der Microsoft-Copilot-Laufzeit.
Skills unter „Build“, „Skills“, „Upload a skill“. Gemeinsame Skills können
geteilt statt mehrfach hochgeladen werden.
