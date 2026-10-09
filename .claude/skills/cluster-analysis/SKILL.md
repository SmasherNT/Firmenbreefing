---
name: cluster-analysis
description: Kartiert Unternehmensstruktur, Beteiligungen und Partnerschaften.
---

Lies input/auftrag.md, CLAUDE.md und references/uebergabe.md, references/defaults.md und references/briefing-struktur.md.
Fehlt der tatsächliche Auftrag, keine Analyse beginnen.
1. Identifiziere belegte Gesellschaften, Joint Ventures und relevante Partner.
2. Erstelle eine Knotenliste mit Name, Typ und belegter Funktion.
3. Beziehungen: Von, Zu, Eigentum/JV/Kooperation/Kunde, Quote falls belegt,
   Status und Datum, Claim-ID, Originalquelle.
4. Trenne angekündigte und abgeschlossene Transaktionen.
5. Ein Standort ist keine Gesellschaft; ein Partner keine Beteiligung ohne Beleg.
Nutze C-Claims und schreibe work/cluster.md nach dem Übergabeschema.
Markiere Grenzen öffentlicher Informationen; keine vollständige juristische
Konzernstruktur behaupten, wenn relevante Daten fehlen.
Priorisiere die Nutzerthemen aus dem Auftrag; themenrelevante Angebote/Beziehungen belegen.

## Ausnahme für ausdrücklich beauftragte Modultests
Bei Modus modultest lies references/modultest.md. Die Delegation nennt
Testauftrag, Auswahl, Eingaben und Zielpfad. Diese Pfade ersetzen die festen
input/work/output-Pfade oben. Nicht gewählte Module sind keine Pflicht.
Im Standardlauf bleiben die obigen Regeln unverändert.
