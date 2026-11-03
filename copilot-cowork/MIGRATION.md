# Migration nach Copilot Cowork

Die Kopie startet vom Commit 37e562341e619b1587c03d749896b951184df26d und
funktioniert als eigener Projektstamm. Fachliche Regeln bleiben in references/;
Layout, Datenverträge, Quellenstandards und Reviewbarrieren sind übernommen.

| Bisheriger Einstieg | Cowork-Kopie |
|---|---|
| CLAUDE.md | AGENTS.md, explizit zu laden |
| .claude/agents/*.md | roles/*.md: zehn fachliche Rollenverträge, ohne Anbieter-YAML |
| .claude/skills/*/SKILL.md | skills/*/SKILL.md: zwölf Methoden mit portablem Frontmatter |
| .claude/settings.json | runtime/settings.json: Hostvertrag, keine native Einstellung |
| Feste Opus-/Sonnet-Zuordnung | references/modellaufteilung.json: auto, gewünschter Effort je Rolle |
| Wiederaufnahme an alten Einstieg gebunden | scripts/resume-run.py mit neuen Verträgen und Pflichtdateiprüfung |
| Alter Konfigurationsbericht | references/setup-check.md mit tatsächlicher lokaler Abnahme |
| Einzelne Projekt-Skills mit externen Referenzen | scripts/build-cowork-skills.py erzeugt selbstständige Uploads |

## Übertragene Arbeitsweise

Vier Kern-Faktenrollen, je Fokusthema ein separater Kontext, Positionierung vor
SWOT, unabhängige Dokument- und Leitprüfung sowie lokale HTML-Erzeugung bleiben
verbindlich. Serielle unabhängige Kontexte sind bei fehlender Parallelität möglich.
Ohne echte Rollentrennung stoppt der entsprechende Lauf. Keine Rollen in einer
Antwort simulieren, kein Quellenreview durch einen rein mechanischen Prüfer ersetzen.

## Importweg

Diese Kopie liefert eigenständige Skill-Uploads. Dadurch ist kein M365-
Pluginmanifest mit erfundenen Herausgeber-, Datenschutz- oder Nutzungsbedingungen
nötig. Es ist kein automatisch konvertiertes Agenten-Plugin. Paketbau, Upload und
Hostproben stehen in references/cowork-betrieb.md und README.md. Die GitHub-
Methodenordner sind Quellcode; zum Upload die erzeugten .skill-Dateien verwenden.
Ein reales Cowork-Importresultat wird hier ausdrücklich nicht behauptet.

## Pflege

Änderungen im alten Projekt synchronisieren diese Kopie nicht automatisch. Vor
späteren Übernahmen Ausgangscommit vergleichen, fachliche Änderungen gezielt
übertragen, Tests und HTML-Vergleich wiederholen und Uploads neu bauen. Laufzeit-
oder Vertragsänderungen invalidieren betroffene Checkpoints. Kein Reuse alter
Claude-Code-Checkpoints in einem neuen Cowork-Lauf.

Aktuelle Ergebnisse und offene Hostprüfungen: references/setup-check.md.
