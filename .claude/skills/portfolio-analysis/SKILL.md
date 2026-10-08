---
name: portfolio-analysis
description: Analysiert Produktangebot und belegten Reifegrad für einen Firmenauftrag.
---

Lies input/auftrag.md, CLAUDE.md und references/uebergabe.md, references/defaults.md,
references/briefing-struktur.md und references/quellenzugang.md.
Fehlt der tatsächliche Auftrag, keine Analyse beginnen.
1. Vollständige Angebotsliste über alle Domänen (z. B. Luft, Land, See, Software,
   Nutzlasten/Sensorik, Services) aus Produktseiten und Newsroom der Firma
   (tools/quellenabruf.py); Zukäufe/Töchter mit eigenem Angebot einbeziehen.
2. Trenne Produkte, Software, Dienstleistungen und Ankündigungen.
3. Reifegrad je Angebot auf einheitlicher Skala, jeweils höchste öffentlich
   belegte Stufe:
   1 angekündigt/vorgestellt · 2 Demonstration/Erstflug/Prototyp ·
   3 Erprobung (Kunden-/Truppen-/Feldtest) · 4 Auftrag/Vertrag ·
   5 nachweislich ausgeliefert/im Einsatz · 6 Serie/Skala (wiederholte Lieferungen,
   mehrere Kunden oder Serienfertigung belegt).
   Kriterium und Beleg je Stufe nennen; Herstellerangabe (H) und unabhängige
   Quelle (U) getrennt kennzeichnen. Stufe 5–6 nur mit Liefer-/Einsatzbeleg.
   Technische TRL-Angaben des Herstellers ersetzen keine Stufe.
4. Produktwerbung belegt keine Serienreife oder Überlegenheit.
5. Tabelle: Domäne, Angebot, Anwendung, Reifestufe, Begründung, H/U, Claim-ID, Quelle.
   Zusätzlich Zählung: Anzahl Einträge je Stufe.
Nutze P-Claims. Markiere Herstellerangaben. Ergänze Unsicherheiten und Lücken.
Themenrelevante Angebote vertieft, übrige mindestens mit Stufe und Beleg.
Schreibe work/portfolio.md nach dem Übergabeschema inkl. Quellenregister.
Keinen Marktvergleich und keine SWOT als Ersatz für das Portfolio.
