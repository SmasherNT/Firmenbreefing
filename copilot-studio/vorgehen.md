# Firmenbriefing in Microsoft Copilot Studio: Vorgehensvorschlag

Stand: 13.11.2026. Grundlage: Nutzerantworten vom selben Tag und die am Ende
genannten Microsoft-Learn-Seiten. Die bestehende Kopie unter copilot-cowork/
wird ausdrücklich nicht weiterverwendet.

## Kurzfassung

Das Briefing-System lässt sich in Copilot Studio weitgehend ohne eigenen Code
abbilden: ein Orchestrator-Agent, zehn Rollen als eigenständige Connected Agents,
eine SharePoint-Bibliothek als gemeinsamer Laufordner und Agent Flows für
Dateizugriff und asynchrone Phasen. Zwei Stellen gehen nicht verlustfrei ohne Code:

1. **HTML-Rendering.** Der heutige Renderer ist Python (render-briefing.py und
   Modulrenderer). Der Code Interpreter in Copilot Studio führt nur selbst
   generierten Code aus, hat keinen Netzzugang, nimmt eine Datei je Prompt und
   muss vom Admin freigeschaltet werden. Er eignet sich nicht, um den Renderer
   auszuführen. Ohne Code bleibt nur ein Prompt-Tool, das die HTML-Vorlage mit
   den geprüften JSON-Daten füllt. Das verletzt die bisherige Regel "keine
   LLM-HTML" und wird in der Abnahme als solches gekennzeichnet. Stufe 2 mit
   echtem Renderer braucht eine Azure Function und damit IT-Beteiligung.
2. **Originalquellen lesen.** Websuche läuft über Bing-Grounding. Der volle
   Seitentext einer URL ist nur über den HTTP-Request-Knoten in einem Topic
   erreichbar, Standard-Timeout 30 Sekunden, PDF-Lesen dort nicht belegt. Ob die
   Rollen Geschäftsberichte als PDF tatsächlich öffnen können, muss die erste
   Hostprobe zeigen. Fällt sie negativ aus, gilt der Quellenstandard nur für
   HTML-Quellen, und PDF-Belege werden als "nicht geöffnet" markiert.

Empfehlung: zuerst drei Hostproben, dann die Modulvariante Portfolio als Pilot,
danach das Vollbriefing. Modelle werden nicht fest vorgegeben; jeder Agent nutzt
die im Mandanten eingestellte Standardwahl, und die Abnahme protokolliert nur,
was sichtbar ist.

## Zielarchitektur

| Heute (Claude Code) | Copilot Studio |
|---|---|
| CLAUDE.md, Hauptagent | Orchestrator-Agent "Firmenbriefing" mit Instructions aus CLAUDE.md-Kern |
| .claude/agents/*.md, zehn Rollen | zehn Connected Agents, Konversationsverlauf aus, eigene Instructions |
| .claude/skills/*/SKILL.md | Instructions des jeweiligen Rollen-Agents, gekürzt auf das Zeichenlimit |
| references/*.md | Wissensquellen je Agent: Dateien in einer SharePoint-Bibliothek "Briefing-Referenzen" |
| runs/<run_id>/input, work, output | SharePoint-Bibliothek "Briefing-Runs", ein Ordner je run_id mit denselben Unterordnern |
| Datei lesen/schreiben durch Agenten | Agent Flows "Datei lesen", "Datei schreiben", "Ordner anlegen" mit SharePoint-Aktionen |
| WebSearch, WebFetch | Websuche aktiviert; Topic "Quelle öffnen" mit HTTP-Request-Knoten für vollen Seitentext |
| source-cache.py | Agent Flow, der geöffnete Quellen als Textdatei unter work/cache/ ablegt |
| review-shards.py | Orchestrator teilt Quellenbündel per Instruction in bis zu drei Jobs; serielle Aufrufe |
| Python-Renderer | Stufe 1: Prompt-Tool "HTML rendern" mit Vorlage als Wissen; Stufe 2: Azure Function |
| Modellaufteilung Opus/Sonnet | keine Vorgabe; Modell je Agent in dessen Einstellungen, beobachtet protokollieren |
| Druck-/Browserprüfung | entfällt zunächst |

Begründung für Connected statt Child Agents: Child Agents teilen den Kontext mit
dem Hauptagenten und haben kein eigenes Modell. Der Vertrag verlangt getrennte
Kontexte, besonders zwischen Autoren und Prüfern. Connected Agents haben eigene
Orchestrierung, Tools, Wissen und Modell und einen Schalter für den Verlauf.
Parallelität ist nicht dokumentiert; serielle unabhängige Aufrufe sind erlaubt.

Begründung für asynchrone Phasen: synchrone Flows brechen nach 100 Sekunden
ab. Aktionen nach "Respond to Copilot" laufen bis zu 30 Tage. Ein Vollbriefing
läuft daher als autonomer Lauf: der Orchestrator legt input/auftrag.json an,
ein Ereignistrigger "Datei erstellt" startet die nächste Phase, der Zustand
steht in work/status.json. Am Ende kommt eine Teams-Nachricht mit dem Link.

## Ablauf im Vollbriefing

1. Nutzer schreibt dem Orchestrator Firma, Themen, optional Person.
2. Orchestrator erzeugt run_id, Ordner, auftrag.json, manifest.json; Antwort an den Nutzer mit Link.
3. Faktenphase: context, portfolio, cluster, market nacheinander; je Fokusthema ein focus-Aufruf. Jeder Agent schreibt nur seine Datei unter work/.
4. Basisreview: bis zu drei Dokumentprüfer-Aufrufe mit disjunkten Quellenbündeln, danach source-reviewer. Ergebnis work/review-basis.json. Bei Materialfehlern Rückgabe an die Rolle, höchstens zwei Runden, dann Stopp.
5. Interpretation: positioning, danach swot. Schlussreview durch source-reviewer.
6. Ausgabe: Prompt-Tool füllt die Vorlage; Flow schreibt output/briefing.html und output/abnahme.md mit tatsächlichen Prüfungen, offenen Grenzen und beobachteten Modellen.

## Modulvariante

Ein zweiter, kleinerer Orchestrator "Firmenbriefing-Modul" nutzt dieselben
Connected Agents: Auftrag, genau ein Faktenmodul, Dokumentprüfung,
source-reviewer, Modul-HTML. Keine SWOT, keine Positionierung. Er dient als
Pilot und bleibt danach als eigenständiges Angebot bestehen.

## Phasenplan

### Phase 0: Vorbereitung im Repo, ohne Mandant

- Ordner copilot-studio/ mit je einer Instruction-Datei pro Agent, erzeugt aus
  Rolle plus Skill plus Pflichtreferenzen durch ein Build-Skript. Das Skript
  prüft das Zeichenlimit der Instructions und schiebt Überhang in Wissensdateien.
- Liste der Wissensdateien je Agent und eine Ordnervorlage für die Bibliotheken.
- Prüfprotokolle für die Hostproben und eine Abnahmevorlage mit Feldern für
  beobachtetes Modell, Aufrufreihenfolge, geöffnete Quellen, offene Grenzen.

### Phase 1: Hostproben im Mandanten, Go oder No-Go

- Probe A Quellen: ein Testagent öffnet eine konkrete HTML-Seite und ein
  PDF eines Geschäftsberichts und zitiert eine Zahl mit Seitenangabe.
- Probe B Kontexte: zwei Connected Agents mit ausgeschaltetem Verlauf schreiben
  getrennte Dateien unter work/; der Orchestrator sieht beide, keiner sieht den anderen.
- Probe C Laufzeit: ein Flow mit asynchroner Antwort läuft länger als fünf
  Minuten und schreibt am Ende eine Datei; ein Ereignistrigger startet darauf einen Folgeagenten.
- Probe D Rendering: Prompt-Tool erzeugt aus einem kleinen JSON und der
  Portfolio-Vorlage eine HTML-Datei, die lokal mit den vorhandenen Tests verglichen wird.

Ergebnis je Probe wird in copilot-studio/hostproben.md festgehalten. Ohne
Probe A und B gibt es keinen Pilot; dann ist Code oder IT-Beteiligung nötig.

### Phase 2: Modulpilot Portfolio

- Agenten: Orchestrator-Modul, portfolio-analyst, source-document-reviewer,
  source-reviewer, Ausgabe.
- Abnahme: work/portfolio-facts.json entspricht dem Datenvertrag; Prüfung lokal
  mit scripts/prepare-facts.py und den vorhandenen Tests aus dem Repo. Diese
  lokale Prüfung ist Pilotwerkzeug, kein Teil der Mandantenlösung.
- Vergleich: dasselbe Portfolio-Modul einmal mit Claude Code, einmal in Copilot
  Studio; Unterschiede in Quellenabdeckung und Fehlerquote dokumentieren.

### Phase 3: Vollbriefing

- Restliche Rollen anlegen, Phasenkette mit Triggern, Fokusagenten, Reviews.
- Ein vollständiges Briefing mit zwei Fokusthemen und einer Person als Abnahmelauf.
- Kostenkontrolle: Nachrichten- und KI-Kreditverbrauch je Lauf messen.

### Phase 4: Härtung und Rollout

- Solution-Export der Agenten und Flows nach copilot-studio/solution/ im Repo;
  Instruction-Dateien bleiben Quelle, Export bleibt Nachweis.
- Freigabe im Unternehmen über den Admin: Veröffentlichung in Teams oder
  Microsoft 365 Copilot, Zugriff auf die Bibliotheken, Governance-Prüfung.
- Optional Stufe 2: Azure Function für den echten Renderer und die Druckprüfung.

## Risiken und Grenzen

- Instruction-Länge: Copilot-Studio-Instructions sind begrenzt; die heutigen
  Skills überschreiten das vermutlich. Lösung über Wissensdateien ist Pflicht,
  die genaue Grenze im Mandanten prüfen.
- PDF-Lesen: nicht belegt; kann den Quellenstandard einschränken.
- Keine Parallelität: ein Vollbriefing dauert seriell deutlich länger.
- Rendering-Treue: LLM-gefüllte Vorlage ist weniger stabil als der Renderer.
- Modell unbekannt: Qualität der Rollen hängt vom Mandantenmodell ab; nur
  beobachtete Werte protokollieren.
- DLP: Admin-Richtlinien können HTTP-Knoten, Websuche oder Trigger sperren.
  Mit Maker-Lizenz allein ist das nicht änderbar.
- Kosten: jede Trigger-Auslösung und jeder Agentenaufruf zählt als Nachricht.

## Nächste Schritte

1. Freigabe dieses Vorgehens.
2. Phase 0 im Repo umsetzen: Build-Skript, Instruction-Dateien, Protokollvorlagen.
3. Phase 1 im Mandanten durchführen, Ergebnisse eintragen.

## Quellen

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/multi-agent-patterns
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-child-agent
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-http-node
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-connectors
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/code-interpreter-for-prompts
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/faq-code-interpreter
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-modify-use-with-agent
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/error-codes
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas
