# Zwei Agenten mit Skills in Microsoft 365 Copilot: Vorschlag

Stand: 23.11.2026. Ersetzt Variante A als Startpunkt. Grundlage sind die am Ende
genannten Microsoft-Seiten.

## Empfehlung in einem Satz

Zwei Agenten im **Agent Builder von Microsoft 365 Copilot**: „Firmenbriefing“
erstellt alles ohne Prüfung, „Briefing-Prüfung“ prüft auf Wunsch danach. Die
Fachlogik steckt in Skills, die Übergabe läuft über eine Excel-Datei, und ein
Python-Skript im Skill rendert die HTML immer gleich.

## Warum Agent Builder und nicht Copilot Studio

- **Skills sind dort allgemein verfügbar.** Ein Skill ist eine ZIP-Datei mit
  SKILL.md und Begleitdateien, also genau das Format der heutigen Claude-Skills.
- **Skripte laufen.** Python-Skripte im Skill werden in einer Sandbox ausgeführt,
  mit pandas, openpyxl, python-docx und LibreOffice, ohne Netz und ohne Nachinstallation.
  Damit wird die HTML von einem Skript gerendert, nicht frei vom Modell geschrieben.
- **Websuche** über „Search all websites“, **Code Interpreter** immer an,
  **Dateien zum Download** direkt im Chat.
- **Kein Copilot Studio nötig.** Kein Flow, kein SharePoint, keine Topics.

## Grenzen, die den Aufbau bestimmen

| Grenze | Folge |
|---|---|
| Agent-Instructions max. 8.000 Zeichen | Instructions nur für Ablauf und Regeln, Fachlogik in Skills |
| Max. 8 Skills je Agent | Ersteller bekommt genau 8, Prüfer 3 |
| SKILL.md max. 20.000 Zeichen, ZIP max. 50 MB | heutige references/*.md als Begleitdateien in den ZIP |
| Skills nicht über Agenten hinweg teilbar | gemeinsamer Ausgabe-Skill liegt in beiden Agenten als Kopie, Build-Skript im Repo hält sie gleich |
| Erzeugte Dateien nur während der Sitzung abrufbar | Dateien nach dem Lauf sofort speichern |
| Chat-Upload für Code Interpreter: Word, Excel, PowerPoint, PDF, CSV, TXT; HTML nicht gelistet | Übergabe an den Prüfer per Excel, nicht per HTML |
| Ein Agent kann keinen anderen aufrufen | Der Nutzer startet die Prüfung selbst mit der Excel-Datei |

## Agent 1: „Firmenbriefing“ (erstellt, prüft nicht)

Instructions: Auftragswahl, Defaults, Reihenfolge der Skills, Quellenregeln in
Kurzform, Hinweis „ungeprüft“, Ausgabe. Websuche an.

| Nr. | Skill | Inhalt | Herkunft im Repo |
|---|---|---|---|
| 1 | firmenbasis-person | Firmenbasis, Timeline vier Monate, berufliches Profil | company-context, gespraechspartner.md |
| 2 | portfolio | alle Geschäftsfelder, Eigenschaften, belegter Status | portfolio-analysis, portfolio-darstellung.md |
| 3 | cluster | Eigentum, Töchter, JV, Partner, Kunden, Beziehungen | cluster-analysis, cluster-recherche.md |
| 4 | markt-wettbewerb | Markt, Vergleichsplan, Vergleichstabelle, regionale Präsenz | market-facts, capability-matrix.md, regionale-praesenz.md |
| 5 | fokusthema | neutrales Themen- und Marktbriefing je Thema | fokusseiten.md |
| 6 | interpretation | Positionierung, SWOT, Executive Summary nur aus Fakten | positioning-analysis, swot-analysis, executive-summary.md |
| 7 | quellen-claims | Claim-IDs, Aussageursprung, Status, Quellenregister | datenvertrag.md, quellenpruefung.md (nur Erfassung) |
| 8 | briefing-ausgabe | Skript: Daten → briefing.html und briefing-daten.xlsx | neue schlanke Fassung von render-briefing.py |

Ergebnis im Chat: **briefing.html** zum Lesen und **briefing-daten.xlsx** als
Übergabe. Die HTML trägt im Kopf „Ungeprüfte Faktenbasis“.
„Nur Portfolio“ nutzt nur die Skills 2, 7 und 8.

## Agent 2: „Briefing-Prüfung“ (prüft auf Wunsch)

Start: Nutzer lädt briefing-daten.xlsx hoch und schreibt „prüfen“, optional
„nur Portfolio prüfen“ oder „nur A-Fakten“. Websuche an. Keine neue Recherche
über den Auftrag hinaus, keine neuen Fakten.

| Nr. | Skill | Inhalt | Herkunft im Repo |
|---|---|---|---|
| 1 | quellenpruefung | jede Quelle öffnen, Claim gegen Belegstelle prüfen, A-Fakten vollständig, B-Fakten Stichprobe; Urteil je Claim | quellenpruefung.md, pruefauftraege.md |
| 2 | ableitungspruefung | Summary, Positionierung, SWOT gegen die geprüften Fakten; fällt ein Fakt, fällt die Ableitung | interpretationsphase.md |
| 3 | briefing-ausgabe | dasselbe Skript wie in Agent 1, rendert mit Prüfstatus | Kopie von Skill 8 |

Urteile je Claim: bestätigt, abweichend, nicht belegt, Quelle nicht erreichbar.
Ergebnis im Chat: **briefing-geprueft.html** mit Prüfstatus an jeder Aussage,
**pruefbericht.html** mit Befunden und Korrekturvorschlägen, und die
aktualisierte Excel-Datei. Der Prüfer korrigiert keine Fakten selbst, er schlägt
vor. Bei wesentlichen Fehlern steht im Kopf „Prüfung nicht bestanden“.

## Übergabe: eine Excel-Datei als einzige Datenquelle

briefing-daten.xlsx enthält je Kapitel ein Blatt: Auftrag, Summary, Timeline,
Person, Portfolio, Cluster, Markt, Vergleich, Fokus, Positionierung, SWOT,
Quellen, Prüfung. Jede Zeile ist ein Claim mit ID, Aussage, Ursprung, Status,
Quelle und Belegstelle. Vorteile: der Prüfer kann sie lesen, der Mensch kann sie
in Excel öffnen und von Hand korrigieren, und das Ausgabeskript rendert aus
derselben Datei vor und nach der Prüfung die gleiche HTML.

## Pflege im Repo

copilot-studio/zwei-agenten/ hält Instructions und Skillordner als Quelle. Ein
Build-Skript packt die ZIPs, kopiert die gemeinsamen Begleitdateien in jeden
Skill, prüft die Zeichenlimits und testet das Ausgabeskript lokal mit
Beispieldaten. Hochgeladen werden nur die erzeugten ZIPs.

## Erste Proben im Mandanten

| Probe | Bestanden wenn |
|---|---|
| 1 Skill mit Skript | Testskill rendert aus einer Mini-Excel eine HTML, Datei ist im Chat herunterladbar |
| 2 HTML als Download | .html erscheint als Datei; sonst Ausgabe als PDF über LibreOffice im Skill |
| 3 Quellen lesen | Agent nennt aus einem Geschäftsbericht eine Zahl mit Seite und Link |
| 4 Excel-Übergabe | Prüfer liest die Excel eines Ersteller-Laufs vollständig ein |
| 5 Länge | Vollbriefing mit zwei Fokusthemen läuft in einer Sitzung durch |

## Offene Annahmen

- Für Skills in Agent Builder ist vermutlich eine Microsoft-365-Copilot-Lizenz
  oder nutzungsbasierte Abrechnung nötig; Copilot Chat Basic reicht laut
  Microsoft-Support nicht. Vor dem Bau im Mandanten prüfen.
- In Organisationen mit Information Barriers können Nutzer keine Skills
  hinzufügen; dann muss der Admin die Agenten bereitstellen.
- Ob Skill-Skripte und Code Interpreter dieselbe Sandbox nutzen, ist nicht
  dokumentiert; Probe 1 klärt das.

## Quellen

- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-skills
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites
- https://support.microsoft.com/en-us/microsoft-365-copilot/create-edit-skills-copilot
- https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/12-skills-da-agent-builder/
- https://mc.merill.net/message/MC1476977
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview
