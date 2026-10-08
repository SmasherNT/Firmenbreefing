# Setup-Check Firmenbriefing-System
Prüfdatum: 2026-10-08. Art: reine Konfigurationsprüfung (Dateien, Metadaten,
Querverweise). Kein Agentenlauf, keine Firmenrecherche, kein Auftrag.
Ein bestandener Konfigurationstest ist kein durchgeführter Briefing-Lauf.

| # | Prüfpunkt | Ergebnis | Begründung |
|---|---|---|---|
| 1 | Vier Agent-Dateien, sechs SKILL.md | bestanden (nach Korrektur) | Agenten: portfolio-analyst, cluster-analyst, swot-analyst, source-reviewer. Skills: portfolio-analysis, cluster-analysis, briefing-context, swot-analysis, briefing-output, company-briefing. company-briefing fehlte und wurde angelegt (siehe Korrekturen). |
| 2 | Metadaten und Skill-Zuordnungen | bestanden | Alle YAML-Köpfe fehlerfrei einlesbar; `name` = Datei- bzw. Verzeichnisname. Agent-Feld `skills` verweist nur auf vorhandene Skills (portfolio-analyst→portfolio-analysis, cluster-analyst→cluster-analysis, swot-analyst→swot-analysis); source-reviewer ohne Skill, Methode im Agententext. Alle Agenten: `tools: Read, Write, WebSearch, WebFetch` (Komma-String laut Doku zulässig), `model: inherit`, kein `Agent`-Tool, also keine weitere Verschachtelung. Laut Doku wird der Skill-Inhalt per `skills` vorab geladen; das Skill-Tool ist dafür nicht nötig. |
| 3 | CLAUDE.md und drei references-Vorlagen lesbar/vollständig | bestanden | UTF-8, keine Ersatzzeichen; CLAUDE.md 31, defaults.md 29, briefing-struktur.md 30, uebergabe.md 18 Zeilen, jeweils byte-identisch mit den Nutzervorgaben. Alle referenzierten Pfade sind konsistent benannt. |
| 4 | Kurz-Anfrage aktiviert company-briefing ohne Slash-Befehl | bestanden (Konfiguration) | CLAUDE.md verlangt company-briefing bei HTML-Briefing-Anfragen. Der Skill hat `description` und `when_to_use` mit natürlichen Beispielanfragen (494 von max. 1.536 Zeichen) und kein `disable-model-invocation`, ist also automatisch aufrufbar. Claude Code führt ihn nach dem Anlegen samt Beispielanfragen in der Skill-Liste. Laufzeitnachweis erst mit echter Anfrage möglich. |
| 5 | Auftrag entsteht automatisch erst nach Briefing-Anfrage | bestanden | CLAUDE.md (Einrichtung, letzter Satz Kurz-Anfrage), defaults.md (Abschnitt „Aus kurzer Nachricht“) und company-briefing Schritt 1. Alle Analyse-Skills brechen ohne tatsächlichen Auftrag ab. |
| 6 | Nutzerthemen und Personenstatus in Analyse, Reviews, HTML | bestanden | Analyse: briefing-context (T-/H-Claims, Nutzerposition vs. bestätigte Rolle), portfolio-/cluster-analysis und swot-analysis priorisieren Nutzerthemen. Reviews: source-reviewer prüft alle Nutzerthemen, T-/H-Claims, Personenidentität und Rollenstatus. HTML: briefing-struktur.md Punkte 1, 3, 4; briefing-output trennt Nutzerrolle und verifizierte Rolle. |
| 7 | Alle Ergebnisdateien eindeutig zugewiesen | bestanden (nach Korrektur) | portfolio.md→portfolio-analyst; cluster.md→cluster-analyst; markt.md, kontext.md→Hauptagent (briefing-context); review-basis.md, review-final.md→source-reviewer; swot.md→swot-analyst; briefing.html, abnahme.md, auftrag.md, archive/→Hauptagent. Gesammelt als Tabelle in company-briefing; vorher fehlte eine zentrale Zuordnung für auftrag.md und archive/. |
| 8 | Keine feste Firma/kein festes Datum in Defaults | bestanden | Suche nach Jahreszahlen und Rechtsformen in CLAUDE.md, references/ und .claude/: kein Treffer. Stichtag = aktuelles Datum der Laufumgebung. Hinweis: briefing-context enthält themenspezifische Regeln (Fahrzeughersteller, Middle East); das ist keine Firma und kein Datum, für andere Themen greift die allgemeine Regel. |
| 9 | Reihenfolge Portfolio/Struktur → Markt+Themen/Person → Basis-Review → SWOT → Schluss-Review → HTML | bestanden (nach Korrektur) | Festgelegt in company-briefing Schritte 2–8. Abhängigkeiten passen: briefing-context liest portfolio.md/cluster.md, swot-analysis verlangt review-basis.md ohne offene wesentliche Fehler, briefing-output verlangt review-final.md. |
| 10 | Fehlende input/auftrag.md als beabsichtigt erkannt | bestanden | Datei existiert nicht. input/README.md, CLAUDE.md (Einrichtung) und company-briefing erklären dies als Sollzustand bis zur ersten Briefing-Anfrage. |

## Korrekturen in diesem Check
- .claude/skills/company-briefing/SKILL.md neu angelegt: Einstieg für
  Kurz-Anfragen, Ablaufreihenfolge, Korrekturschleife (höchstens zwei Runden,
  danach blockiert), Zuständigkeitstabelle, Protokoll für abnahme.md,
  Archivierung und Dateisicherung. Inhalt von Claude formuliert, nicht vom
  Nutzer vorgegeben; bei Bedarf durch Nutzervorlage ersetzen.
- Überflüssige .gitkeep in .claude/agents/, .claude/skills/ und references/
  entfernt, da die Verzeichnisse nun Dateien enthalten. work/ und output/
  behalten .gitkeep.

## Offene Einschränkungen
- Kein echter Agentenlauf: automatische Skill-Auswahl, Delegation,
  Web-Zugriff der Subagenten und HTML-Prüfungen sind erst beim ersten
  Briefing nachweisbar.
- Die Methoden-Skills portfolio-analysis, cluster-analysis und swot-analysis
  bleiben auch für den Hauptagenten automatisch aufrufbar; die Delegation an
  die Agenten ist nur per Anweisung in company-briefing abgesichert.
- Rollentrennung („nur eigene Dateien schreiben“) ist Anweisung, keine
  technische Sperre; alle Agenten haben das Write-Werkzeug.
- Mobil- und Druckansicht lassen sich in der Cloud-Umgebung nur per
  Headless-Browser prüfen; nicht ausführbare Kontrollen werden in
  output/abnahme.md als „nicht geprüft“ geführt.
