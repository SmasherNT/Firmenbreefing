---
name: interpretation-briefing
description: Steuere ausdrücklich beauftragte Interpretation einer vorhandenen facts-v2-Basis mit Positionierung, SWOT und gezieltem Schluss-Review. Keine neue allgemeine Recherche oder HTML.
---

Lies references/interpretationsphase.md an der Repositorywurzel. Auftrag und vorhandenen Faktenlauf
identifizieren; ohne diesen keinen unabhängigen neuen Interpretationslauf erfinden.
Bei vorhandenen Lauf-Checkpoints references/lauf-wiederaufnahme.md anwenden:
vor Delegation resume, nur reusable übernehmen; Positionierung, SWOT und
freigegebenes Schlussreview nach tatsächlichem Abschluss lokal speichern.
1. Manifest, Faktenpaket und freigegebenes Basis-Review desselben Laufs prüfen.
   Nur beauftragte Interpretationsrollen ausführen; SWOT allein ist möglich.
2. Relevante Fakten-IDs für Positionierung wählen; bei Matrix Plan/Marktmodul
   bereitstellen. Selektiven Kontext per check-interpretation.py --prepare erzeugen.
   Bei Summary auch relevante geprüfte Kennzahl-/Statuskandidaten aufnehmen;
   Darstellungsvertrag references/executive-summary.md an Positionierung geben.
   Bei vollständigem Briefing --portfolio und references/portfolio-darstellung.md
   mitgeben; Produktzuordnung/Skala bleiben selektiv, SWOT erhält nur relevante I-IDs.
   Zusätzlich --module-insights und references/modul-keyfacts.md mitgeben:
   passende vorhandene A-Auszüge aus Portfolio, Cluster und Markt selektiv wählen;
   Positionierung liefert je Modul 1–3 Fakt/Insight-Karten oder einen begründeten Gap.
   Im Vollbriefing zusätzlich --presence und references/regionale-praesenz.md;
   eigener kompakter Präsenzkontext mit fixer Skala 1–5, keine weitere Analyse-/Designrolle.
3. positioning-analyst mit mode=interpret-v2, Auftrag, Kontext und Zielpfad
   delegieren. Ausgabe lokal mechanisch prüfen, keine Inhaltsfreigabe erfinden.
4. Für SWOT passenden Kontext mit ausgewählten A-Fakten und ggf. relevanten
   I-IDs erzeugen. Bereits vorhandene Positionierung vor Nutzung mechanisch
   prüfen; nicht alle Matrix-Deep-Dives als Standardkontext laden.
5. swot-analyst mit mode=interpret-v2, Kontext und Ziel delegieren; Schema prüfen.
   Bei I-Basis aktuelle Positionierung samt Kontext und Plan an den Check geben.
   Beide Validierungen per --merge-validation zusammenführen; Aufrufe in Referenz.
6. Phase final: review-work.py prepare und nach parallele-quellenpruefung.md
   nur facts_to_verify auf Dokumentjobs desselben Modells verteilen. Danach
   source-reviewer als Leitprüfer mit mode=interpret-v2, Quellenbefunden, kompakten I-/S-Claims,
   Abhängigkeiten, Basis-Review und interpretation-validation.json delegieren.
   review-work.py prepare nach references/pruefauftraege.md: Originalbindung,
   Dokumentbündel und neue/geänderte Ableitungen vorbereiten; Kontexte nicht kürzen.
   Entwurfsziel <Lauf>/work/review-final-draft.json; Hauptagent erzeugt review-final.md.
   Unveränderte A-Fakten übernehmen, Ableitungen und Änderungen gezielt prüfen.
   Dokumentbefunde und Leitentwurf zuerst per review-shards.py merge abgleichen;
   den zusammengeführten Entwurf per stamp-review.py --work mit lokalen
   Einzelzeilen/Fingerprints ergänzen; fehlende Entscheidungen bleiben offen.
7. Fragen/Korrekturen nur zuständiger Rolle zuweisen; neue Fakten benötigen
   Basis-Review. Selektiven Kontext und betroffene Bewertungen erneuern.
   Nach zwei erfolglosen Korrekturrunden Materialfehler blockieren.
8. Abnahme aktualisieren: mechanischer Pass, Inhaltsreview und offene Fragen
   getrennt ausweisen. Keine HTML implizit starten; company-briefing beauftragt anschließend
   briefing-output nach references/ausgabe-html-v2.md.
Aufrufhilfe: python3 scripts/check-interpretation.py --help.
Vorgegebene Laufdateien erhalten; Korrekturen versionieren und überholte Reviews
nicht weiter als freigegeben behandeln. Nur kompakte Statusrückgabe.


Quellenprüfung verbindlich nach references/parallele-quellenpruefung.md:
Dokumentjobs (bis zu drei, gleiches Modell) → collect → Leitprüfung → merge →
bestehendes stamp-review.py --work. Keine reduzierte Prüftiefe oder Modellwechsel.
In final nur neu zu prüfende Faktenquellen verteilen, sonst ausschließlich Leitprüfung.
