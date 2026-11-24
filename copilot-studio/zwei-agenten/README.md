# Firmenbriefing mit zwei Agenten und Skills in Copilot

Zwei Agenten, zwölf Dateien zum Hochladen, keine Flows, kein SharePoint.

- **Firmenbriefing** erstellt das Briefing ohne Prüfung und gibt
  `briefing.html` und `briefing-daten.xlsx` aus.
- **Briefing-Prüfung** prüft auf Wunsch danach. Sie bekommt eine dieser Dateien
  und gibt `briefing-geprueft.html` mit Prüfbericht aus.

Die Skills sind ZIP-Pakete im Agent-Builder-Format: `SKILL.md` im Hauptordner,
daneben Skripte und Referenzen. Dasselbe Format nimmt auch Copilot Studio an.
Die HTML schreibt nie das Modell, sondern das Skript im Skill briefing-ausgabe.

## Was hochgeladen wird

Alle Dateien liegen fertig in `dist/`. Liste mit Größen: `dist/pakete.md`.

| Agent | Instructions | Skills aus dist/skills/ |
|---|---|---|
| Firmenbriefing | agenten/firmenbriefing/instructions.md | briefing-standards, briefing-ausgabe, firmenbasis-person, portfolio, cluster, markt-wettbewerb, fokusthema, interpretation |
| Briefing-Prüfung | agenten/briefing-pruefung/instructions.md | briefing-standards, briefing-ausgabe, quellenpruefung, ableitungspruefung |

## Reihenfolge

1. **Machbarkeitstest** nach `machbarkeitstest/README.md`, etwa 30 Minuten.
   Er zeigt, ob Skill-Skripte laufen, ob HTML und Excel als Datei kommen und ob
   Quellen-PDFs geöffnet werden können. Ergebnisse in `machbarkeitstest/testprotokoll.md`.
2. **Agent „Firmenbriefing“ anlegen** (unten).
3. **Agent „Briefing-Prüfung“ anlegen** (unten).
4. **Probelauf:** „Nur Portfolio zu [bekannte Firma]“, danach die Excel-Datei im
   Prüfagenten mit „prüfen“ hochladen.
5. **Vollbriefing:** „Briefing zu [Firma], Fokus: [Thema], Gesprächspartner:
   [Name], [Position]“.

## Einrichten im Agent Builder (Microsoft 365 Copilot)

Je Agent:

1. Microsoft 365 Copilot öffnen, links „Agents“, dann „New agent“ und
   „Configure“ bzw. „Skip to configure“.
2. Name und Beschreibung aus `agenten/<agent>/agent.md` übernehmen.
3. Instructions: Inhalt von `agenten/<agent>/instructions.md` vollständig einfügen.
4. Wissen: „Search all websites“ einschalten. Weitere Wissensquellen sind nicht nötig.
5. Skills: „Add“ und die ZIP-Dateien aus `dist/skills/` laut Tabelle hochladen.
   Höchstens acht Skills je Agent; Firmenbriefing nutzt genau acht.
6. Gesprächsstarter aus `agent.md` übernehmen, speichern, testen.

Grenzen im Agent Builder: Instructions bis 8.000 Zeichen, acht Skills je Agent,
SKILL.md unter 20.000 Zeichen, Skills nicht zwischen Agenten teilbar. Deshalb
werden briefing-standards und briefing-ausgabe in beide Agenten hochgeladen;
es sind dieselben Dateien. Erzeugte Dateien sind nur während der Sitzung
abrufbar und müssen danach gespeichert werden. Für Skills ist laut Microsoft
voraussichtlich eine Microsoft-365-Copilot-Lizenz oder nutzungsbasierte
Abrechnung nötig.

Prüfen im Agent Builder: Ein Agent kann den anderen nicht aufrufen. Der
Nutzer öffnet „Briefing-Prüfung“ und lädt `briefing-daten.xlsx` hoch, oder
`briefing.html`, falls der Machbarkeitstest gezeigt hat, dass HTML gelesen wird.

## Einrichten in Copilot Studio

Gleiche Instructions und ZIP-Dateien, mit der Microsoft-Copilot-Laufzeit:

1. Neuen Agenten mit der Microsoft-Copilot-Laufzeit anlegen, Instructions einfügen.
2. Websuche einschalten, Skills unter „Build“, „Skills“, „Upload a skill“ hochladen.
   Die beiden gemeinsamen Skills können geteilt statt doppelt hochgeladen werden.
3. „Briefing-Prüfung“ veröffentlichen und bei „Firmenbriefing“ als verbundenen
   Agenten hinzufügen. Dann genügt im selben Chat „prüfen“.
4. In Teams und Microsoft 365 Copilot veröffentlichen.

Abrechnung über Copilot Credits.

## Bedienung

| Nachricht | Agent | Ergebnis |
|---|---|---|
| Briefing zu [Firma], Fokus: [Thema], Gesprächspartner: [Name], [Position] | Firmenbriefing | Vollbriefing |
| Nur Portfolio zu [Firma] | Firmenbriefing | ein Kapitel, keine SWOT |
| weiter | Firmenbriefing | setzt nach einer abgebrochenen Runde fort |
| prüfen (mit Datei) | Briefing-Prüfung | alle Kapitel prüfen |
| nur Portfolio prüfen / nur A-Fakten prüfen | Briefing-Prüfung | Teilprüfung |
| Korrekturen umsetzen (mit geprüfter Datei) | Firmenbriefing | betroffene Fakten nachrecherchieren, neue Dateien |

Prüfergebnis: **bestanden**, **bestanden mit Einschränkungen** (z. B. nur durch
Suche gestützt oder Teilprüfung), **unvollständig** (A-Fakten offen oder nicht
erreichbar) oder **nicht bestanden** (ein A-Fakt abweichend oder nicht belegt,
oder eine Ableitung nicht gestützt). Das Ergebnis berechnet das Skript.

## Ordner

| Pfad | Inhalt |
|---|---|
| agenten/ | Instructions und Einstellungen je Agent |
| skills/ | Quellordner der zehn Skills |
| skills/briefing-ausgabe/scripts/briefing.py | Zusammenführen, Validieren, Rendern, Prüfung auswerten, Excel |
| machbarkeitstest/ | Test-Skill, Proben, Protokoll |
| beispiel/ | fiktive Beispieldaten in acht Teilen, für Tests |
| tests/ | automatische Tests des Skripts |
| tools/build.py | prüft Grenzen, führt Tests aus, baut dist/ |
| dist/ | fertige ZIP-Dateien zum Hochladen |
| vorschlag.md, architektur.png | Konzept und Grafik |

## Pflege

Nach jeder Änderung an Skills, Instructions oder Skript:

```bash
python3 tools/build.py
```

Das Skript prüft Zeichen- und Dateigrenzen, führt die Tests aus und schreibt
`dist/` neu. `python3 tools/build.py --pruefen` meldet, ob `dist/` veraltet ist.
Danach die geänderten ZIP-Dateien im Agenten ersetzen.

## Bewusste Vereinfachungen gegenüber Claude Code

- Ein Agent recherchiert alle Kapitel; keine getrennten Kontexte je Faktenrolle.
- Prüfung seriell in einem Agenten statt bis zu drei paralleler Dokumentprüfer.
- Kein interaktives Cluster-Netz, keine Druckprüfung, keine Fingerprints.
- Geblieben: Claim-IDs, Aussageursprung, Quellenregister, Trennung von Fakt und
  Interpretation, feste Skalen, unabhängige Prüfung auf Wunsch mit fester
  Freigaberegel.
