# Agent „Briefing-Prüfung“: Einstellungen

| Feld | Wert |
|---|---|
| Name | Briefing-Prüfung |
| Beschreibung | Prüft ein vorhandenes Firmenbriefing aus briefing.html oder briefing-daten.xlsx gegen seine Quellen und gibt eine geprüfte Fassung mit Prüfbericht aus. |
| Instructions | Inhalt von instructions.md vollständig einfügen |
| Websuche | an, „alle Websites durchsuchen“ |
| Code Interpreter | an (im Agent Builder immer an) |
| Wissen | keines nötig |
| Modell | Mandantenstandard |

## Skills (4 ZIP-Dateien aus dist/skills/)

1. briefing-standards.zip
2. briefing-ausgabe.zip
3. quellenpruefung.zip
4. ableitungspruefung.zip

briefing-standards.zip und briefing-ausgabe.zip sind dieselben Dateien wie
beim Agenten „Firmenbriefing“. Im Agent Builder werden sie in beide Agenten
hochgeladen. In Copilot Studio können sie geteilt werden.

## Gesprächsstarter

- Prüfe dieses Briefing (Datei anhängen)
- Prüfe nur das Portfolio (Datei anhängen)
- Prüfe nur die A-Fakten (Datei anhängen)
