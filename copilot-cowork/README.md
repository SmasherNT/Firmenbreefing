# Firmenbriefing für Microsoft Copilot Cowork

Eigenständige Kopie der Firmenbriefing-Methodik für Microsoft Copilot Cowork.
Ausgangsbasis: Commit 37e562341e619b1587c03d749896b951184df26d.
Das bisherige Claude-Code-Projekt außerhalb dieses Ordners bleibt unverändert.

## Verwenden

1. Die benötigten Uploads mit `python3 scripts/build-cowork-skills.py --out dist/skills`
   aus diesem Ordner erzeugen. `company-briefing.skill` in Cowork unter
   Customize → Skills → Add → Upload skill importieren; weitere Methoden optional.
2. Im neuen Cowork-Chat einen tatsächlichen Firmenauftrag stellen. Der Einstieg
   entpackt die mitgelieferte Projektlaufzeit und liest AGENTS.md explizit.
3. Den Host-Pilot nach references/cowork-betrieb.md durchführen. Vorhandene
   Skill-Uploads stellen keine funktionsfähige Subagenten-Integration sicher.

Die Rollen bleiben unabhängig, auch wenn der Host sie seriell ausführt.
Fehlt diese Fähigkeit, muss der ausführende Host/Adapter sie zuerst bereitstellen.

Beispielauftrag: „Erstelle nach company-briefing ein vollständiges HTML-Briefing
zu [Firma]. Fokusthemen: [Thema 1], [Thema 2]. Sichere HTML und Prüfstatus.“

Alternativ vollständigen Projektordner im ausführbaren Arbeitsbereich verwenden,
AGENTS.md laden und von hier aus arbeiten. Kein automatischer GitHub-Zugriff nötig.

## Inhalt

| Pfad | Aufgabe |
|---|---|
| AGENTS.md | Plattformneutraler Einstieg und verbindliche Qualitätsregeln |
| roles/ | Zehn Rollenverträge ohne Claude-Tool-/Modell-YAML |
| skills/ | Zwölf übernommene und angepasste Methoden |
| references/ | Fachregeln, Datenverträge und identische HTML-Vorlagen |
| runtime/settings.json | Explizit zu lesender Hostvertrag; keine native Cowork-Konfiguration |
| scripts/ | Renderer, Validierung, Cache, Wiederaufnahme, Preflight und Upload-Build |
| tests/ | Kopierte Regressionstests und Migrationstests |

## Prüfen

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/cowork-preflight.py --out work/preflight.json --strict
python3 examples/build-demo.py --out work/demo
python3 scripts/build-cowork-skills.py --out dist/skills
```

Renderer/Vorlagen sind übernommen, Quellen-/Reviewbarrieren bleiben bestehen.
Die Wiederaufnahme berücksichtigt AGENTS.md, roles/, skills/, Modellpolicy und
Hostvertrag. auto-Modelle sind Anforderungen, keine Laufzeitnachweise.

Aktueller Prüfstatus: references/setup-check.md. Ein realer Cowork-Lauf und Import
im Zielmandanten sind separat nachzuweisen. Bei fehlenden unabhängigen Kontexten,
Webzugriffen oder Skriptlaufzeit stoppt der Workflow ohne finale Ausgabe.
Der strikte Preflight ist ohne echte Hostnachweise absichtlich blockiert. Nach
den Proben `--host-evidence <Nachweisdatei>` ergänzen; Format siehe
references/cowork-betrieb.md. Änderungen und Pfadzuordnung: MIGRATION.md.
