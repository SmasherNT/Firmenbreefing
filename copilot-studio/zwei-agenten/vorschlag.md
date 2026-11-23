# Zwei Agenten mit Skills in Copilot: überarbeiteter Vorschlag

Stand: 23.11.2026, Version 2. Ersetzt Version 1 vom selben Tag, die Agent
Builder empfahl. Grundlage sind die am Ende genannten Microsoft-Seiten.
Nichts davon ist im Mandanten getestet.

## Empfehlung

Zwei Agenten in **Copilot Studio mit der Microsoft-Copilot-Laufzeit**
(Microsoft nennt sie „Microsoft Copilot harness“, früher „GitHub Copilot harness“;
allgemein verfügbar). Veröffentlicht in Teams und Microsoft 365 Copilot.

- **Agent 1 „Firmenbriefing“** erstellt das Briefing ohne Prüfung.
- **Agent 2 „Briefing-Prüfung“** prüft auf Wunsch danach, in eigenem Kontext.
- **Eine gemeinsame Skill-Bibliothek** statt Kopien: Standards und Ausgabe
  werden einmal gepflegt und beiden Agenten zugeordnet.
- **Eine einzige Übergabedatei:** briefing.html mit eingebetteten Daten.

## Warum diese Oberfläche

| Anforderung | Agent Builder (M365 Copilot) | Copilot Studio, Copilot-Laufzeit | Copilot Cowork |
|---|---|---|---|
| Zwei echte Agenten | ja | ja | nein, nur Skills und Plugins |
| Prüfer aus dem Chat des Erstellers aufrufbar | nein | ja, als verbundener Agent mit eigenem Kontext | entfällt |
| Skills zwischen Agenten teilen | nein | ja (Teilen ist Vorschau) | entfällt |
| Skill-Skripte werden ausgeführt | ja, dokumentiert | nicht dokumentiert; Python im Container ja | ja, dokumentiert |
| Websuche | Bing, alle Websites | Bing, alle Websites | Deep-Research-Skill |
| Bestimmte URL oder PDF öffnen | nicht dokumentiert | nicht dokumentiert; Browser-Bedienung geplant | ja, über den Edge-Browser des Nutzers |
| Datei im Chat ausgeben | ja, nur während der Sitzung | ja, 10 MB, 28 Tage, in Folgerunden wieder lesbar | ja, dauerhaft im OneDrive-Ordner „Cowork“ |
| HTML-Datei hochladen und lesen | nicht dokumentiert | ja, eingebauter HTML-Skill; Anhänge bearbeiten dokumentiert | ja |
| Lizenz | für Skills vermutlich M365-Copilot-Lizenz | Copilot Credits; keine persönliche Copilot-Studio-Lizenz nötig | M365-Copilot-Lizenz |

Copilot Studio erfüllt als einzige Oberfläche alle drei Wünsche zugleich:
zwei Agenten, Skills, und die Prüfung „im Nachhinein“ im selben Chat. Sie passt
außerdem zur vorhandenen Maker-Berechtigung, weil über Copilot Credits
abgerechnet wird.

## Aufbau

### Gemeinsame Skills (einmal gepflegt, beiden Agenten zugeordnet)

| Skill | Inhalt | Herkunft im Repo |
|---|---|---|
| briefing-standards | Quellenregeln, Aussageursprung, Claim-IDs, Datenformat, Kennzeichnung ungeprüft/geprüft | quellenpruefung.md, datenvertrag.md, CLAUDE.md |
| briefing-ausgabe | Python-Renderskript und HTML-Vorlage; rendert mit und ohne Prüfstatus, bettet die Daten ein | neue schlanke Fassung von render-briefing.py |

### Agent 1 „Firmenbriefing“

Instructions: Auftrag erkennen, Defaults, Reihenfolge der Skills, Arbeit in
Phasen, Hinweis „ungeprüft“. Websuche an. Verbundener Agent: „Briefing-Prüfung“.

| Skill | Inhalt | Herkunft |
|---|---|---|
| firmenbasis-person | Firmenbasis, Timeline vier Monate, berufliches Profil | company-context, gespraechspartner.md |
| portfolio | alle Geschäftsfelder, Eigenschaften, belegter Status | portfolio-analysis, portfolio-darstellung.md |
| cluster | Eigentum, Töchter, JV, Partner, Kunden, Beziehungsrichtung | cluster-analysis, cluster-recherche.md |
| markt-wettbewerb | Markt, Vergleichsplan, Vergleichstabelle, regionale Präsenz | market-facts, capability-matrix.md, regionale-praesenz.md |
| fokusthema | neutrales Themen- und Marktbriefing je Thema | fokusseiten.md |
| interpretation | Positionierung, SWOT, Executive Summary nur aus Fakten | positioning-, swot-analysis, executive-summary.md |
| + briefing-standards, briefing-ausgabe | gemeinsam | |

**Arbeit in Phasen.** Agent 1 legt nach jedem Kapitel die Daten in der
Arbeitsdatei briefing.html ab. Erzeugte Dateien bleiben im Chat und sind in
Folgerunden wieder lesbar. Bricht eine Antwort wegen Länge ab, genügt „weiter“,
und der Agent setzt an der letzten gespeicherten Phase fort.
„Nur Portfolio“ nutzt nur portfolio, standards und ausgabe.

### Agent 2 „Briefing-Prüfung“

Instructions: nur prüfen, keine neuen Fakten, Korrekturen nur vorschlagen,
Urteilsstufen, Freigaberegel. Websuche an.

| Skill | Inhalt | Herkunft |
|---|---|---|
| quellenpruefung | Prüftiefe A und B, Urteil je Claim, Netzwerkkanten, Personen, Kennzahlen | quellenpruefung.md, pruefauftraege.md |
| ableitungspruefung | Summary, Positionierung und SWOT gegen die geprüften Fakten; fällt ein Fakt, wird die Ableitung markiert | interpretationsphase.md |
| + briefing-standards, briefing-ausgabe | gemeinsam | |

**Urteile je Claim, ehrlich nach Prüfweg getrennt:**

| Urteil | Bedeutung |
|---|---|
| im Original bestätigt | Belegstelle im geöffneten Original gefunden |
| durch Suche gestützt | unabhängiges Suchergebnis stützt die Aussage, Original nicht geöffnet |
| abweichend | Quelle sagt etwas anderes; Korrekturvorschlag |
| nicht belegt | weder Original noch Suche stützen die Aussage |
| nicht erreichbar | Quelle nicht abrufbar |

**Prüftiefe:** A vollständig für Summary-Kennzahlen, Person und Rolle,
Eigentum und Kontrolle, jede Beziehung im Cluster, Vergleichswerte und jede
Grundlage der SWOT. B als dokumentierte Stichprobe für Hintergrunddetails.
**Freigaberegel:** Ein A-Claim „abweichend“ oder „nicht belegt“ ergibt
„Prüfung nicht bestanden“, sonst „bestanden“ oder „bestanden mit Einschränkungen“.

## Ablauf für den Nutzer

1. Im Chat mit „Firmenbriefing“: „Briefing zu [Firma], Fokus: [Thema],
   Gesprächspartner: [Name], [Position]“. Ergebnis: briefing.html mit
   Hinweis „Ungeprüfte Faktenbasis“.
2. Optional im selben Chat: „prüfen“, „nur Portfolio prüfen“ oder „nur
   A-Fakten prüfen“. Agent 1 übergibt an „Briefing-Prüfung“, der in eigenem
   Kontext arbeitet. Ergebnis: briefing-geprueft.html mit Status an jeder
   Aussage und einem Prüfbericht als letztem Kapitel.
3. Ausweg bei großen Dateien: Übergaben an verbundene Agenten haben eine
   Größengrenze. Dann „Briefing-Prüfung“ direkt öffnen und briefing.html hochladen.

## Übergabe: eine Datei

briefing.html enthält neben der lesbaren Seite einen unsichtbaren Datenblock
mit allen Claims, Quellen und Ableitungen. Der Prüfer liest diesen Block,
ergänzt die Urteile und rendert mit demselben Skript neu. Damit gibt es nur
eine Datei, und die geprüfte Fassung sieht genauso aus wie die ungeprüfte.
Ersatz, falls der Datenblock beim Hochladen nicht ankommt: zusätzlich
briefing-daten.xlsx ausgeben, denn Excel-Anhänge sind überall dokumentiert.

## Rendering ohne Rätselraten

Ob Skript-Dateien aus einem Skill in dieser Laufzeit ausgeführt werden, ist
nicht dokumentiert. Python im Container ist es. Deshalb steht das Renderskript
zweimal im Skill briefing-ausgabe: als Datei im Paket und als Codeblock in
SKILL.md. Kommt die Datei nicht im Container an, schreibt der Agent den
Codeblock unverändert in eine Datei und führt sie aus. Das Modell schreibt
die HTML in keinem Fall selbst.

## Was bewusst wegfällt gegenüber Claude Code

- Getrennte Kontexte je Faktenrolle: Agent 1 recherchiert alle Kapitel selbst.
- Bis zu drei parallele Dokumentprüfer: Agent 2 prüft seriell.
- Interaktives Cluster-Netz, Druckprüfung, Checkpoints mit Fingerprints.
Geblieben sind Claim-IDs, Aussageursprung, Quellenregister, Fakt-Interpretation-
Trennung und eine unabhängige Prüfung auf Wunsch.

## Hauptrisiko: Quellen wirklich öffnen

Keine der drei Oberflächen dokumentiert, dass ein Agent eine bestimmte URL oder
ein PDF aus dem Web öffnet; nur Cowork kann es über den Edge-Browser des
Nutzers. Folgen und Auswege:

1. Die Urteilsstufen oben machen den Prüfweg sichtbar, statt eine
   Originalprüfung vorzutäuschen.
2. Microsoft plant Browser-Bedienung für diese Laufzeit (Roadmap RM576272).
   Sobald verfügbar, nur Agent 2 damit ausstatten.
3. Falls eine Microsoft-365-Copilot-Lizenz vorhanden ist, kann der Skill
   quellenpruefung zusätzlich in Cowork laufen. Cowork öffnet Originale im
   Edge-Browser. Das ist der stärkste Prüfweg, aber kein eigener Agent.

## Machbarkeitstest vor dem Bau (etwa 30 Minuten)

Ein Testagent mit der Copilot-Laufzeit und einem Mini-Skill.

| Probe | Bestanden wenn | Wenn nicht |
|---|---|---|
| 1 Skript aus dem Skill | Skill-Skript rendert eine Mini-HTML, Datei erscheint im Chat | Codeblock-Ersatz aus SKILL.md nutzen |
| 2 HTML-Download | .html kommt als Dateikarte | Ausgabe als PDF über reportlab |
| 3 Datenblock lesen | hochgeladene HTML wird samt Datenblock gelesen | Excel-Übergabe |
| 4 URL und PDF | Agent nennt aus einem Geschäftsbericht Zahl, Seite, Link | Urteilsstufe „durch Suche gestützt“, Cowork-Ausweg |
| 5 Verbundener Agent | „prüfen“ im Chat von Agent 1 erreicht Agent 2 mit Datei | Agent 2 direkt nutzen |

Dazu je Probe Dauer und verbrauchte Copilot Credits notieren.

## Pflege im Repo

copilot-studio/zwei-agenten/ hält Instructions, Skillordner und Renderskript.
Ein Build-Skript prüft Zeichenlängen, testet das Renderskript lokal mit
Beispieldaten, setzt den Codeblock-Ersatz in SKILL.md ein und packt die ZIPs.
Hochgeladen werden nur die erzeugten Pakete.

## Ersatzwege

- **Agent Builder**, falls Copilot Studio im Mandanten nicht nutzbar ist,
  etwa in einer Dataverse-for-Teams-Umgebung: zwei Agenten, max. 8 Skills je
  Agent, Skills als Kopie in beiden, Übergabe per Excel, Prüfung per Agentwechsel.
- **Cowork**, falls M365-Copilot-Lizenzen vorhanden sind und Originalprüfung
  wichtiger ist als zwei echte Agenten: zwei Skills „briefing-erstellen“ und
  „briefing-pruefen“, Ergebnisse dauerhaft im OneDrive.

## Quellen

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-manage
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-add-other-agents
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/created-files-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use
- https://www.microsoft.com/en-us/copilot/blog/copilot-studio/new-and-improved-github-copilot-harness-agent-skills-and-richer-context/
- https://mc.merill.net/message/RM576272
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-skills
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills
- https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
- https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize
- https://learn.microsoft.com/en-us/copilot/cowork/use-cowork
- https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-plugin-development
