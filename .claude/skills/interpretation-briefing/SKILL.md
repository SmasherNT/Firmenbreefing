---
name: interpretation-briefing
description: Steuere ausdrücklich beauftragte Interpretation einer vorhandenen facts-v2-Basis mit Positionierung, SWOT und gezieltem Schluss-Review. Keine neue allgemeine Recherche oder HTML.
---

Lies references/interpretationsphase.md an der Repositorywurzel. Auftrag und vorhandenen Faktenlauf
identifizieren; ohne diesen keinen unabhängigen neuen Interpretationslauf erfinden.
1. Manifest, Faktenpaket und freigegebenes Basis-Review desselben Laufs prüfen.
   Nur beauftragte Interpretationsrollen ausführen; SWOT allein ist möglich.
2. Relevante Fakten-IDs für Positionierung wählen; bei Matrix Plan/Marktmodul
   bereitstellen. Selektiven Kontext per check-interpretation.py --prepare erzeugen.
3. positioning-analyst mit mode=interpret-v2, Auftrag, Kontext und Zielpfad
   delegieren. Ausgabe lokal mechanisch prüfen, keine Inhaltsfreigabe erfinden.
4. Für SWOT passenden Kontext mit ausgewählten A-Fakten und ggf. relevanten
   I-IDs erzeugen. Bereits vorhandene Positionierung vor Nutzung mechanisch
   prüfen; nicht alle Matrix-Deep-Dives als Standardkontext laden.
5. swot-analyst mit mode=interpret-v2, Kontext und Ziel delegieren; Schema prüfen.
   Bei I-Basis aktuelle Positionierung samt Kontext und Plan an den Check geben.
   Beide Validierungen per --merge-validation zusammenführen; Aufrufe in Referenz.
6. source-reviewer Phase final mit mode=interpret-v2, kompakten I-/S-Claims,
   Abhängigkeiten, Basis-Review und interpretation-validation.json delegieren.
   Ziel <Lauf>/work/review-final.md; JSON-Review nach Interpretationsvertrag.
   Unveränderte A-Fakten übernehmen, Ableitungen und Änderungen gezielt prüfen.
   Expliziten Reviewer-Entwurf per stamp-review.py mit lokalen Fingerprints ergänzen.
7. Fragen/Korrekturen nur zuständiger Rolle zuweisen; neue Fakten benötigen
   Basis-Review. Selektiven Kontext und betroffene Bewertungen erneuern.
   Nach zwei erfolglosen Korrekturrunden Materialfehler blockieren.
8. Abnahme aktualisieren: mechanischer Pass, Inhaltsreview und offene Fragen
   getrennt ausweisen. Keine finale HTML: Ausgabeanschluss folgt im nächsten Schritt.
Aufrufhilfe: python3 scripts/check-interpretation.py --help.
Vorgegebene Laufdateien erhalten; Korrekturen versionieren und überholte Reviews
nicht weiter als freigegeben behandeln. Nur kompakte Statusrückgabe.
