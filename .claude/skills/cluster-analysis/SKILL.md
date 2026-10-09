---
name: cluster-analysis
description: Recherchiere Unternehmensstruktur, Technologie und Industrie, Kunden und Querverbindungen mit Geschäftsberichten für Firmenbriefings. Kein strategisches Scoring.
---

Lies tatsächlichen Auftrag, references/cluster-recherche.md,
references/cluster-quellenkatalog.md und references/netzwerk-html.md.
1. Firma/Akteure identifizieren; direkte und indirekte Teilbeziehungen prüfen:
   Eigentum/Kontrolle, JV, Entwicklung, Lizenz, Integration, Lieferant/Kunde,
   Produktion, Service, Konsortien, berufliche Mandate und Historie.
2. Technologie & Industrie gleichwertig zu Kapital/Konzern/Kunden recherchieren:
   Software/KI, Sensorik, Kommunikation, Plattform-/Fahrzeugintegration,
   Fertigungspartner und Aufgabenverteilung nur soweit auftragsrelevant.
3. Geschäftsberichte relevanter Akteure suchen; Abschnitt/Seite, Zeitbezug
   und Bericht-Abdeckung erfassen. Nachrichten/Fachmedien und Gegenparteien
   aktiv einbeziehen; relevante Hinweise und Querverbindungen weiterverfolgen.
4. C-Claims, Akteure, Kanten, Teilpfade, Bericht-Protokoll, Fundliste, Quellen
   und Lücken liefern. Gemeinsame Mitgliedschaft/Kompatibilität ist kein Vertrag.
5. Netzwerk aus belegt recherchierten Claims nach Schema v1 erzeugen;
   neuer Auftrag -> neuer Datensatz. Nicht vor Quellenprüfung als freigegeben ausgeben.

Bei mode=facts-v2 references/faktenphase.md lesen und ausschließlich delegiertes
cluster-facts.json mit network/actors/relationships/report_log schreiben.
Die JSON- und Faktenbegrenzung ersetzt Markdown-/Interpretationsanforderungen
in den Referenzen. Kein edge.interpretation, Gewichtung oder Score.
Sonst CLAUDE.md, uebergabe.md, defaults.md und briefing-struktur.md lesen;
work/cluster.md inkl. network-data nach bisherigem Schema schreiben.
Modultest: delegierte Pfade und Auswahl nach references/modultest.md haben Vorrang;
2b verlangt keine weiteren Module. Hauptfunktion/focus sind redaktionell, keine Bewertung.
Keine Markt-/SWOT-Analyse oder eigene finale HTML erstellen.
