---
name: cluster-analysis
description: Kartiert Unternehmensstruktur, Beteiligungen und Partnerschaften.
---

Lies input/auftrag.md, CLAUDE.md und references/uebergabe.md, references/defaults.md,
references/briefing-struktur.md und references/quellenzugang.md.
Fehlt der tatsächliche Auftrag, keine Analyse beginnen.
1. Newsroom der Firma im Recherchezeitraum vollständig sichten
   (tools/quellenabruf.py news) sowie Standort-, Händler-, Partner- und
   Investorenseiten (seite). Für jeden Partner dessen eigene Mitteilung suchen.
2. Erfasse systematisch, je eigene Kategorie:
   Gesellschaften/Töchter · Zukäufe (unterzeichnet/vollzogen) · Standorte ·
   Joint Ventures · Finanzierungsrunden und Fremdfinanzierung mit Investoren ·
   Industrie-/Technologiepartner · Distributoren/Händler je Land (nur Firma,
   Land, Rolle) · Kunden/Verträge · Allianzen/Konsortien ·
   relevante Beziehungen zweiter Ordnung (Partner der Partner, Wettbewerbs-
   beziehungen, z. B. ein OEM mit mehreren Autonomiepartnern).
   Ziel: möglichst vollständige öffentliche Abdeckung (Richtwert ≥ 40 Beziehungen,
   sofern öffentlich belegbar); fehlende Kategorien als Lücke nennen.
3. Knotenliste: Name, Typ, belegte Funktion. Beziehungen: Von, Zu,
   Eigentum/JV/Kooperation/Kunde/Investor/Distributor, Quote falls belegt,
   Status und Datum, Quellentyp, Claim-ID, Originalquelle.
4. Trenne angekündigte und abgeschlossene Transaktionen.
5. Ein Standort ist keine Gesellschaft; ein Partner keine Beteiligung ohne Beleg;
   ein Distributor keine Niederlassung.
Nutze C-Claims und schreibe work/cluster.md nach dem Übergabeschema inkl.
Quellenregister. Grenzen öffentlicher Informationen markieren; keine
vollständige juristische Konzernstruktur behaupten.
Nutzerthemen priorisieren und je Thema eine kurze Einordnung liefern.
