---
name: portfolio-analysis
description: Analysiert Produktangebot und belegten Reifegrad für einen Firmenauftrag.
---

Lies input/auftrag.md, CLAUDE.md und references/uebergabe.md, references/defaults.md und references/briefing-struktur.md.
Fehlt der tatsächliche Auftrag, keine Analyse beginnen.
1. Recherchiere Produktgruppen und Anwendungen in Originalquellen.
2. Trenne Produkte, Software, Dienstleistungen und Ankündigungen.
3. Unterscheide vorgestellt, erprobt, bestellt und nachweislich ausgeliefert.
4. Produktwerbung belegt keine Serienreife oder Überlegenheit.
5. Erstelle eine Tabelle: Angebot, Anwendung, belegter Status, Claim-ID, Quelle.
Nutze P-Claims. Belege relevante Eigenschaften und markiere Herstellerangaben.
Ergänze Unsicherheiten und öffentliche Lücken.
Schreibe work/portfolio.md nach dem Übergabeschema.
Keinen Marktvergleich und keine vollständige SWOT als Ersatz für das Portfolio.
Priorisiere die Nutzerthemen aus dem Auftrag; themenrelevante Angebote/Beziehungen belegen.

## Ausnahme für ausdrücklich beauftragte Modultests
Bei Modus modultest lies references/modultest.md. Die Delegation nennt
Testauftrag, Auswahl, Eingaben und Zielpfad. Diese Pfade ersetzen die festen
input/work/output-Pfade oben. Nicht gewählte Module sind keine Pflicht.
Im Standardlauf bleiben die obigen Regeln unverändert.
