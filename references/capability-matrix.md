# Capability Matrix: Vergleichsplan aus dem Auftrag
Darstellung wie Referenz-HTML: Unternehmen/konkretes Angebot in Zeilen, Kriterien
in Spalten, jede Zelle mit späterem Deep Dive zu Begründung, Evidenz und Quellen.
Scores zeigen öffentliche Evidenzreife, keine gemessene technische Überlegenheit.

## Vor der Wettbewerbsrecherche
Hauptagent erstellt comparison-plan.json mit company, as_of, run_id,
comparison_unit, purpose, peer_groups, criteria und version.
Vergleichseinheit aus Nutzerthemen bestimmen: Produkt/System/Dienstleistung
und Einsatzkontext, nicht pauschal gesamter Konzern. Frühe Firmen-/Produktfakten
dürfen die Identität klären; Kriterien nicht nach gewünschten Ergebnissen wählen.
Bei allgemeinem Auftrag passende Kerngeschäftseinheit begründet wählen.
Etwa 5–7 Kriterien als Richtwert; weniger oder mehr nur bei fachlichem Bedarf.
Keine feste Bodenautonomie-Matrix für andere Firmen/Branchen übernehmen.

Je Kriterium: id, label, question, evidence_required, display_type,
applicability, rationale. display_type: Profil / Kennzahl / Evidenzstufe.
Evidenzstufe: zusätzlich vorab definierte anchors (z. B. 1–5); gleiche
Stufen und Bezugsgrößen für alle vergleichbaren Angebote. Noch keine Scores vergeben.
Kennzahl: gemeinsame Einheit und Einsatz-/Messbedingungen definieren.
Im JSON dafür unit und conditions angeben.
Profil: qualitative Beschreibung ohne Rangfolge, z. B. Integrationsmodell.
peer_groups: Gruppen nach vergleichbarer Rolle, keine Rangliste und keine
vorgegebene Anzahl. Markt-Agent schlägt konkrete Peers mit nachvollziehbarem
Produkt-/Funktionsbezug vor; Hauptagent bestätigt Scope und Gruppen.

Kriterien aus Fragestellung ableiten und kurz begründen:
OEM-Integration -> Integrationsmodell/Schnittstellen;
industrielle Skalierung -> relevante Fertigung/Lieferfähigkeit;
Marktzugang -> Kundenprogramme/regionale Partner/Zulassungen;
missionskritische Autonomie -> passende Tests/Einsatz/Resilienz.
Diese Beispiele sind keine Pflichtspalten. Branchenfremde Kriterien weglassen.
Markt-Agent sammelt Beobachtungen und Claim-IDs je peer_id/criterion_id.
Markt-Modul nennt comparison_plan_version; geänderte Kriterien nicht mit alten
Beobachtungen mischen.
Peer- und Produktidentität, Kriterienversion und Beleggrenzen erhalten.
Portfolio-/Cluster-Fakten der Zielgruppe referenzieren; keine parallele Zweitrecherche.

## Nach der Faktenprüfung
Positionierung vergibt erst dann Bewertungen nach anchors/Methode.
Nicht öffentlich belegt und nicht anwendbar getrennt kennzeichnen.
Herstellerangaben ausdrücklich ausweisen; höchster vollständig belegter
Evidenzstand, keine vermutete technische Schwäche bei fehlender Veröffentlichung.
Ordinale Scores nicht automatisch addieren/mitteln oder als Gesamt-Ranking ausgeben.
Kriterienänderung: Auftrag/Scope-Grund, neue version und alle betroffenen
Beobachtungen/Bewertungen aktualisieren; keine selektive Anpassung eines Peers.
Die vollständige Bewertung und Zell-Deep-Dives werden in der Interpretationsphase
implementiert. Markt-Fakten allein sind noch keine bewertete Capability Matrix.
