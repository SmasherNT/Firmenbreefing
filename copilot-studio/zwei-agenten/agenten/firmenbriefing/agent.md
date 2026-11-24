# Agent „Firmenbriefing“: Einstellungen

| Feld | Wert |
|---|---|
| Name | Firmenbriefing |
| Beschreibung | Erstellt aus einer kurzen Anfrage ein Firmenbriefing zur Gesprächsvorbereitung als HTML-Datei, ohne Prüfung. |
| Instructions | Inhalt von instructions.md vollständig einfügen |
| Websuche | an, „alle Websites durchsuchen“ |
| Code Interpreter | an (im Agent Builder immer an) |
| Wissen | keines nötig |
| Modell | Mandantenstandard |

## Skills (8 ZIP-Dateien aus dist/skills/)

1. briefing-standards.zip
2. briefing-ausgabe.zip
3. firmenbasis-person.zip
4. portfolio.zip
5. cluster.zip
6. markt-wettbewerb.zip
7. fokusthema.zip
8. interpretation.zip

## Gesprächsstarter

- Briefing zu [Firma], Fokus: [Thema], Gesprächspartner: [Name], [Position]
- Nur Portfolio zu [Firma]
- weiter
- Korrekturen aus dem Prüfbericht umsetzen

## Nur in Copilot Studio

Den Agenten „Briefing-Prüfung“ unter „Agenten“ als verbundenen Agenten
hinzufügen. Beschreibung für die Weiterleitung: „Prüft ein vorhandenes
Firmenbriefing gegen seine Quellen, wenn der Nutzer eine Prüfung wünscht.“
