# Plattformneutrale Rollen- und Modellzuordnung

Maschinenlesbar: references/modellaufteilung.json (schema_version=2).
Hostfähigkeiten: runtime/settings.json. Dies sind Projektverträge, keine nativen
Cowork-Einstellungsdateien. Der Host/Adapter muss sie explizit lesen und anwenden.

Alle Rollen verwenden model=auto: das im Mandanten zugelassene Modell wählen.
Keine vorausgesetzten Modellnamen oder Zugänge. Gewünschter Effort bleibt medium;
cluster-analyst, market-facts-analyst und positioning-analyst wünschen high.
Falls pro Rolle kein Modell/Effort einstellbar ist, die tatsächlich verfügbare
Einstellung und Abweichung protokollieren; nichts stillschweigend als erfüllt melden.

Die zehn Rollen sind fachliche Verträge in roles/*.md. Diese Dateien sind keine
installierbaren Cowork-Subagentendefinitionen. Getrennte Kontexte bleiben Pflicht.
Faktenrollen recherchieren; Positionierung und SWOT interpretieren geprüfte Fakten;
Dokumentprüfer und Leitprüfer entscheiden unabhängig von Autorenrollen.

review-shards.py bindet die angeforderten Reviewer-Profile an den Splitplan.
Geänderte Profile verlangen neue Pläne; resume-run.py bindet Profile, Laufzeit,
Rollenverträge und Methoden an Checkpoints. auto im Plan ist kein Modellnachweis.
Beobachtetes Modell/Effort, Rolle, Start/Ende, Ziel und Status in
<Lauf>/output/abnahme.md dokumentieren; nicht sichtbare Metadaten als unbekannt.
Keine reduzierte Quellenprüftiefe oder automatische Freigabe bei Modellwechsel.
