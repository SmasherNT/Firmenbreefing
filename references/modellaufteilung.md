# Modellaufteilung für neue Claude-Code-Läufe

Stand: 19.10.2026. Diese Zuordnung ersetzt die frühere Gleichmodell-Regel.

| Aufgabe / Rolle | Modell-ID | Effort |
|---|---|---|
| Hauptagent: Koordination, Konsolidierung | claude-opus-5-5 | medium |
| Modulauftrag: module-contractor | claude-sonnet-5-5 | medium |
| Firmenkontext: company-context-analyst | claude-sonnet-5-5 | medium |
| Portfolio: portfolio-analyst | claude-sonnet-5-5 | medium |
| Cluster: cluster-analyst | claude-opus-5-5 | high |
| Markt: market-facts-analyst | claude-opus-5-5 | high |
| Positionierung / Matrix / Reife / Präsenz: positioning-analyst | claude-opus-5-5 | high |
| Je Fokusthema separat: focus-analyst | claude-sonnet-5-5 | medium |
| SWOT: swot-analyst | claude-sonnet-5-5 | medium |
| Dokumentprüfung: source-document-reviewer, bis zu drei Jobs | claude-sonnet-5-5 | medium |
| Leitprüfung Basis: source-reviewer, phase=basis | claude-sonnet-5-5 | medium |
| Leitprüfung Schlussreview: source-reviewer, phase=final | claude-sonnet-5-5 | medium |
| HTML-Erzeugung und mechanische Validierung | lokale Skripte | — |

Die maschinenlesbare Zuordnung steht in modellaufteilung.json. Ausführbare
Claude-Code-Konfiguration: .claude/settings.json für den Hauptagenten und
model/effort im YAML-Kopf jeder .claude/agents-Datei. Tests sichern die Konsistenz.
review-shards.py übernimmt Dokument- und Leitprüfermodell samt Effort in den
fingerprintgebundenen Plan; show liefert die jeweilige Dokumentjob-Konfiguration.
Änderungen verlangen neue Splitpläne. Keine automatische Hochstufung oder
Modellersetzung bei Konflikten; Fehler an zuständige Rolle zurückgeben und die
bestehenden Prüf-/Freigabebarrieren einhalten. Qualität und Tokenersparnis sind
mit dieser Konfiguration allein nicht gemessen.

Positioning bewertet die geprüften Fakten anhand der bestehenden Kriterien und
Skalen für Wettbewerbsposition, Capability-Matrix, Produktreife und regionale
Präsenz. Keine neue Webrecherche, keine Änderung an Skalen oder Kontextverträgen.
Die Dokumentprüfung prüft Belege; der Leitprüfer entscheidet über globale
Konsistenz, Abdeckung, Ableitungen und Freigabe. Beide Leitphasen bleiben Medium.

## Laufzeit und Kontrolle

Für Sonnet 5.5 ist mindestens Claude Code 2.1.284 erforderlich. Modellzugang und
organisatorische Vorgaben können die Ausführung begrenzen. Explizite Laufzeit-
Overrides (z. B. --model, ANTHROPIC_MODEL, CLAUDE_CODE_EFFORT_LEVEL oder
CLAUDE_CODE_SUBAGENT_MODEL_FORCE) können Projekt-/Agentenvorgaben übersteuern.
Bei Delegation die konfigurierten model-/effort-Werte erhalten und tatsächliche
Overrides transparent ausweisen. Keine stillschweigende Ersatzmodellwahl.
Eine bereits laufende Sitzung wird durch diese Repository-Dateien nicht umgestellt.
Die tatsächliche Ausführung soweit verfügbar über /model bzw. /tasks kontrollieren.
Konfigurationsmetadaten im Prüfplan belegen keine tatsächliche Modellausführung.

Offizielle Konfigurationsreferenzen:
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/settings

Fokusseiten nach fokusseiten.md: je Thema ein eigener focus-analyst-Aufruf mit
eigener Datei und eigenem Kontext. Forschung, Faktenverdichtung und Grafikinhalte
auf Sonnet 5.5 Medium; Prüfung ebenso. Kein Opus-/Positionierungs-/SWOT-Auftrag.
