# Interpretationsphase v2
## Anschluss
Nur bei ausdrücklich beauftragter Interpretation einer bestehenden Faktenphase.
Keine Einrichtung als Firmenanalyse behandeln. Dieselbe run_id/company/as_of
wie facts-run.json und review-packet.json verwenden. Kein neuer Faktenauftrag.
Positionierung -> SWOT -> gemeinsamer Schluss-Review -> explizit beauftragte
Ausgabe nach ausgabe-html-v2.md. Neue vollständige HTML-Aufträge nutzen v2;
bestehende Legacy-Markdown-Läufe bleiben getrennt.
Keine Horváth-Angebotskapitel, keine separaten Firmen-Deep-Dives.

## Geprüfte Grundlage und kompakte Eingabe
Basis-Review muss für diesen Lauf freigegeben sein; Materialfehler blockieren.
Jede verwendete wesentliche Faktenaussage: depth=A, status=geprüft/übernommen
und Fingerprint identisch zum aktuellen Faktenpaket. B-Hintergrunddetails sind
keine bewertbare Faktenbasis. Vor Verwendung gezielt nach A hochstufen lassen.
Hauptagent bereitet selektive Eingabe mit scripts/check-interpretation.py vor.
Nur ausgewählte Claim-IDs/Interpretations-IDs plus Matrixbeobachtungen laden;
keine vollständigen Rechercheberichte, Quellen-Volltexte oder neuen Webabrufe.
Das Skript erhält Basis-Review, Faktenpaket und Manifest. Bei Matrix zusätzlich
Vergleichsplan und market-facts.json; Version/Identität müssen übereinstimmen.
Wegen weiterer Prüfbefunde ungeeignete Claims stehen in pending_checks.
Diese nicht für eine Bewertung verwenden; eine konkrete Prüf-/Recherchefrage stellen.
Allgemeine Grenzen einmal unter shared_limitations, nicht in jeder Zelle wiederholen.

## Ausgabeformat
schema_version=1, mode="interpret-v2", role=positioning/swot, run_id, company,
as_of, scope, status (vollständig/teilweise/blockiert), input_fingerprint,
interpretations (Liste), research_requests (Liste), shared_limitations (Liste).
input_fingerprint unverändert aus der delegierten context.json kopieren.
Je Interpretation: id (I- bzw. S-), statement, section, depends_on (Claim-IDs),
reasoning, method, uncertainty. Zahlen/Fakten nicht ohne Basis-IDs neu einführen.
Bei SWOT category=Strengths/Weaknesses/Opportunities/Threats.
depends_on führt zu aktuellen vollständig geprüften Fakten; bei SWOT dürfen
aktuelle I-Claims dazwischen liegen. Unbewertete Matrix-Lücken tragen keine SWOT.
Bei fehlender Basis weniger Aussagen liefern; keinen generischen Füllpunkt erzeugen.
Kurz schreiben: statement etwa ein Satz, reasoning normalerweise 2–3 Sätze,
method kurzer Methodenname/-hinweis, uncertainty nur konkrete zusätzliche Grenze.
Gemeinsame Quellen-/Scope-Grenzen ausschließlich in shared_limitations;
kein erneutes Ausschreiben der referenzierten Fakten oder globaler Disclaimer
je Punkt/Zelle. Bei komplexer Ableitung fachlich nötige Erklärung erhalten.

## Positionierung und Matrix
Qualitative Produkt-/Technologie-/Industrieposition, regionale Präsenz und
Netzwerkbedeutung nur soweit beauftragt aus geprüften Fakten ableiten.
Je Matrixzelle eine I-Interpretation mit type="matrix_cell", peer_id,
criterion_id, cell_status und value; kein zweiter identischer Claim in einer Tabelle.
cell_status: bewertet / nicht öffentlich belegt / nicht anwendbar /
weitere Faktenprüfung nötig.
bewertet: depends_on nicht leer. Profil -> beschreibender String ohne Score;
Kennzahl -> belegter Zahlenwert, Einheit/Bedingungen in reasoning nennen;
Evidenzstufe -> value entspricht einem vorher definierten anchors-Schlüssel.
nicht öffentlich belegt: value=null, Such-/Beleggrenze in coverage_note nennen;
keine Aussage, dass die Fähigkeit tatsächlich fehlt.
nicht anwendbar: value=null und begründete A-Faktenbasis für fehlende Anwendbarkeit.
weitere Faktenprüfung nötig: value=null; konkrete Frage in research_requests.
Jeder Peer/Kriterium-Paarung genau eine Zelle zuordnen, kein Auslassen schwacher
oder fehlender Evidenz. peer_ids, criteria und plan_fingerprint bleiben fest.
Höchste vollständig belegte Stufe begründen; auch erklären, warum die nächsthöhere
nicht belegt ist. Ordinale Scores nicht zu Gesamt-Ranglisten mitteln/addieren.
Andere numerische Bewertungen (Produktreife/regionale Präsenz) nur bei vorab
definierter assessment_methods im Vergleichsplan mit id, assessment_type,
anchors und applicability. Methode method_id und bewertetes subject nennen.
Ohne passende Methode qualitative Einordnung liefern, keinen Score erfinden.

## SWOT
Maximal drei konkrete Punkte je Quadrant, weniger bei begrenzter Evidenz.
S/W: bestehende interne Fähigkeiten/Grenzen, O/T: externe Chancen/Risiken.
Datenlücke ist keine betriebliche Schwäche. Herstellerproduktmerkmal ist ohne
begründeten Vorteil keine Stärke. Status, Konzern/Produkt und Zeitbezug erhalten.
Methodik/Interpretation von Fakten sichtbar unterscheiden. Keine neuen Fakten
selbst recherchieren; Fragen an die zuständige Fakten-/Prüfrolle zurückgeben.
Positionierungs-Claims nur mit aktuellem Input/Faktenbezug verwenden.

## Research requests und Änderungen
Frage: id, target_role (context/portfolio/cluster/market/source-reviewer),
question, related_claim_ids, blocking (Boolean).
Hauptagent behandelt nur entscheidungsrelevante Fragen. Kein allgemeiner
Recherche-Neustart und keine eigene Websuche der Interpretationsagenten.
Korrektur -> neue/aktualisierte Fakten -> gezieltes Basis-Review -> Kontext neu
erzeugen -> nur abhängige Bewertungen/Schlussfolgerungen erneuern.
Das Prüfskript vergleicht Snapshots/Fingerprints, kennt aber nicht die inhaltliche
Richtigkeit einer Bewertung. source-reviewer Phase final prüft Ableitungen.
Nicht verwendete geänderte Fakten müssen keine unveränderte Bewertung invalidieren.
Ohne aktuelle Grundlage bzw. bei Materialfehlern keine geprüfte Interpretation ausgeben.

## Maschinenlesbare Reviews
Für v2 in review-basis.md / review-final.md genau einen JSON-Codeblock führen
(kompakte Fehlertexte darin; keine duplizierte lange Statustabelle):
schema_version=1, run_id, company, as_of, phase=basis/final,
status=freigegeben/teilweise/blockiert, material_errors (Liste), claims (Liste).
Je Review-Claim: id, depth=A/B, status=geprüft/übernommen/nicht einzeln geprüft/
Korrektur/offen, fingerprint; bei Fehlern reason/action/owner.
Basis-Fingerprints aus facts-validation.json verwenden, nicht erfinden.
Final-Fingerprints aus interpretation-validation.json verwenden.
Reviewer schreibt review-basis-draft.json / review-final-draft.json mit expliziten
Entscheidungen, Prüfumfang, Belegstellen bzw. Review-Verweisen und Fehlern.
scripts/stamp-review.py fügt lokal die Fingerprints hinzu und schreibt das Review;
es erteilt keine Freigabe und ersetzt keine Quellen-/Ableitungsprüfung.
Der Entwurf braucht dieselbe run_id/company/as_of/phase wie die Validierung.
Ein mechanischer Pass darf nie als Inhaltsprüfung eingetragen werden.
Reine JSON-Reviewdateien sind ebenfalls lesbar; Legacy-Reviews bleiben unverändert.

## Lokale Aufrufe
Pfade liegen unter dem bereits vorhandenen Lauf. Alle references/-Pfade relativ
zur Repositorywurzel auflösen. --plan nennt stets die aktuelle Vergleichsplan-
Datei, damit Änderungen gegenüber dem delegierten Snapshot erkannt werden.

```bash
python3 scripts/stamp-review.py --draft <review-basis-draft.json> --validation <facts-validation.json> --out <review-basis.md>
python3 scripts/check-interpretation.py --prepare --manifest <facts-run.json> --facts <review-packet.json> --review <review-basis.md> --plan <comparison-plan.json> --market <market-facts.json> --out <positioning-context.json>
python3 scripts/check-interpretation.py --manifest <facts-run.json> --facts <review-packet.json> --review <review-basis.md> --context <positioning-context.json> --output <positioning.json> --plan <comparison-plan.json> --out <positioning-validation.json>
python3 scripts/check-interpretation.py --prepare --manifest <facts-run.json> --facts <review-packet.json> --review <review-basis.md> --positioning <positioning.json> --positioning-context <positioning-context.json> --plan <comparison-plan.json> --interpretation-ids <relevante I-IDs...> --claim-ids <weitere relevante Fakten-IDs...> --out <swot-context.json>
python3 scripts/check-interpretation.py --manifest <facts-run.json> --facts <review-packet.json> --review <review-basis.md> --context <swot-context.json> --output <swot.json> --positioning <positioning.json> --positioning-context <positioning-context.json> --plan <comparison-plan.json> --out <swot-validation.json>
python3 scripts/check-interpretation.py --merge-validation <positioning-validation.json> <swot-validation.json> --out <interpretation-validation.json>
python3 scripts/stamp-review.py --draft <review-final-draft.json> --validation <interpretation-validation.json> --out <review-final.md>
```
Ohne Vergleich --plan/--market weglassen; relevante Fakten mit --claim-ids wählen.
Bei SWOT allein ohne I-Basis entfallen --positioning/--positioning-context und
--interpretation-ids. Kein pauschales Laden aller Fakten als Standard.
Nach Änderungen Checks erneut auf aktuellen Dateien ausführen, Validierungs-
berichte nicht aus verschiedenen Dateiständen zusammenführen. Bei Fehlern
schreibt das Skript keine neue Validierung; alte Erfolgsdatei nicht weiterverwenden.
