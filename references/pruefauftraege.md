# Dokumentbündel, Änderungsprüfung und kompakte Befunde

Inhalt: Vorbereitung · Reviewer · Rückgabe/Expansion · Wiederverwendung.
Neue v2-Prüfungen verwenden review-work.py und stamp-review.py --work.
Bestehende vollständige Review-Entwürfe bleiben kompatibel. Fakten-/Positionierungs-
und SWOT-Kontexte sowie Rechercheumfang, A/B-Regeln und zwei Prüfrunden unverändert.
Das Arbeitsblatt ist zusätzliche lokale Steuerung, keine gekürzte Faktenbasis.

## Dokumentjobs als Standard
Neue v2-Läufe verteilen die vorhandenen source_batches nach
[parallele-quellenpruefung.md](parallele-quellenpruefung.md) auf bis zu drei
Dokumentprüfer auf Sonnet 5.5 Medium. Der bestehende Quellenprüfer konsolidiert als
Leitprüfer. read/show-Kontexte der Dokumentprüfer sind auf eigene Quellen und
Claims begrenzt; volle Eingaben bleiben beim Leitprüfer erreichbar. Vor stamp-review
führt review-shards.py die expliziten Teilbefunde und Leitentscheidungen zusammen.
Alle unten beschriebenen Inhalts-, Reuse- und Freigaberegeln bleiben erhalten.

## Hauptagent: Prüfauftrag lokal vorbereiten

Nach erfolgreicher mechanischer Faktenvalidierung:

```bash
python3 scripts/review-work.py prepare --manifest <Manifest> --facts <review-packet.json> --validation <facts-validation.json> --cache <Dokumentcache> --out <review-work-basis.json>
```

Vor Schlussreview nach erfolgreicher Interpretationsvalidierung:

```bash
python3 scripts/review-work.py prepare --manifest <Manifest> --facts <review-packet.json> --validation <interpretation-validation.json> --cache <Dokumentcache> --basis-review <review-basis.md> --basis-work <review-work-basis.json> --positioning <positioning.json> --positioning-context <positioning-context.json> --swot <swot.json> --swot-context <swot-context.json> --plan <comparison-plan.json> --out <review-work-final.json>
```

Nur vorhandene/beauftragte Interpretationsdateien mitgeben; Plan nur bei Vergleich.
Aktuelle Ausgaben/Kontexte/Validierung werden erneut mechanisch abgeglichen.
Nach Korrekturen zusätzlich --previous-work <altes-Arbeitsblatt> und
--previous-review <zugehöriger-freigegebener-Review>. Versionen erhalten, alte
Arbeitsblätter nie überschreiben, wenn eine Übernahme darauf verweisen soll.
Originalcache vor Vorbereitung vollständig verfügbar machen; bei späterer Änderung
oder neuer Textaufnahme Arbeitsblatt neu bauen. Keine alten Freigaben umstempeln.

## Quellenprüfer: einmal je Dokument, Entscheidung je Aussage

Die folgenden vollständigen Eingaben gelten für den Leitprüfer. Dokumentjobs
erhalten die begrenzte Jobansicht nach parallele-quellenpruefung.md.

Alle bisherigen Auftrag-/Paket-/Kontext-/Abdeckungsdateien mitgeben. Zusätzlich
Arbeitsblattpfad; den Maschinen-Snapshot nicht als langen Hash-Bericht lesen:

```bash
python3 scripts/review-work.py show --work <Arbeitsblatt>
python3 scripts/review-work.py show --work <Arbeitsblatt> --source-id <S-ID>
python3 scripts/review-work.py show --work <Arbeitsblatt> --claim-ids <I-/S-IDs...>
```

source_batches bündelt alle Aussagen eines Dokuments. review_fact_ids nennt die
aktuell zu prüfenden Aussagen; vollständiges Paket bleibt erreichbar. Original-
abschnitte gemeinsam lesen, erforderlichen Kontext bei Zweifel erweitern. Für
Mehrfachbelege jede Quelle der betreffenden Aussage prüfen. Je Claim eigenen
Befund behalten; ein passender Absatz gibt nicht alle Dokumentclaims frei.
Labels/Zuordnungen/Status ebenso fachlich prüfen. Kein neuer Webabruf bei lesbarem,
passendem unverändertem Original; bei Widerspruch/Aktualitätszweifel gezielt refresh.
Die Ableitungsprüfung liest Kriterien/Skalen, Fakten und alle neuen I-/S-Aussagen.

## Kompakter JSON-Entwurf des Prüfers

Kopf wie bisher: schema_version, run_id, company, as_of, phase, status,
material_errors, review_scope. Zusätzlich review_work_fingerprint exakt aus show.
Bei freigegebener Basis scope_and_mappings_checked=true ausdrücklich bestätigen:
Auftragsabdeckung, offene Grenzen und gesamte module_views fachlich kontrollieren,
auch wenn einzelne Quellenbefunde übernommen werden. Kein automatischer Default.
Keine claims-Liste und keine selbst geschriebenen Fingerprints. Stattdessen:

```json
{
  "source_checks": [
    {"source_id": "S-ID", "claim_ids": ["P1", "P2"], "note": "Originalabschnitte und Zuordnungen einzeln abgeglichen."}
  ],
  "review_groups": [
    {"claim_ids": ["P1"], "depth": "A", "status": "geprüft", "note": "Aussage und Produktumfang belegt."},
    {"claim_ids": ["P2"], "depth": "A", "status": "Korrektur", "note": "Status widerspricht Original.", "reason": "Nur angekündigt.", "action": "Operativen Status korrigieren.", "owner": "portfolio"}
  ]
}
```

source_checks dokumentiert gelesene Originalbelege, keine pauschale Freigabe.
In review_groups nur tatsächlich gleichlautende Prüfbefunde bündeln; jede ID
ausdrücklich nennen. Gemeinsame Notiz einmal, individuelle Probleme separat.
Erlaubte Status wie bisher; B/Stichproben ausdrücklich klassifizieren und Auswahl/
Eskalation nach quellenpruefung.md dokumentieren. A-geprüft braucht die dokumentierte
Kontrolle sämtlicher referenzierter Quellen. Fehlender Befund bleibt offen.

Bei Phase final zusätzlich reuse_fact_ids mit ausdrücklich übernommenen IDs aus
fact_reuse_candidates. facts_to_verify durch fact_groups (gleiches Gruppenformat)
mit depth=A/status=geprüft und zugehörigen source_checks bestätigen; bei fehlendem
oder widersprüchlichem Original offen/Korrektur führen. Änderungen wesentlicher
Fakten weiterhin an Faktenrolle/Basis-Review zurückgeben, keine Analystendatei ändern.
review_groups enthält im Schlussreview die I-/S-IDs. Jede neue Ableitung vollständig
prüfen; unveränderte geprüfte I-/S-IDs nur als erlaubte Kandidaten übernehmen.

## Lokal expandieren und bestehende Prüfbarrieren anwenden

```bash
python3 scripts/stamp-review.py --draft <kompakter-Review.json> --validation <aktuelle-Validierung.json> --work <Arbeitsblatt> --out <review-basis.md-oder-review-final.md>
```

Das Skript erstellt einzelne Claim-Zeilen/Fingerprints aus ausdrücklich genannten
Prüferentscheidungen und hält gemeinsame Quellenbefunde einmal vor. Fehlende IDs
erhalten offen, keine Erfolgsannahme. Erforderliche fehlende/unvollständige A-Befunde,
unzulässige Übernahmen, doppelte/unknown IDs, veränderte Eingaben oder Originale
blockieren Freigabe. Mechanische Expansion erzeugt keine inhaltlichen Prüfurteile.

## Konservative Änderungsprüfung

Nur derselbe Lauf/Firmenauftrag/Stichtag und dieselbe Phase; vorheriger Review muss
freigegeben, fehlerfrei und an sein Arbeitsblatt gebunden sein. Übernahme verlangt
vorherige A-Entscheidung sowie unveränderte Aussage, Quellenmetadaten, Original-/
Tool-Snapshot, Produkt-/Länder-/Statuszuordnung und alle Faktenabhängigkeiten.
Fehlende Cachebindung/ältere Reviews ohne Arbeitsblatt liefern keine automatische
Übernahmekandidatur; dann regulär prüfen. source-cache-304 mit unverändertem Inhalt
erfordert keine Wiederholung, geänderte Bytes betreffen sämtliche Dokumentclaims.
Neue/änderte Quellen, Zuordnungen oder Elternfakten erneuern betroffene Prüfungen;
gelöschte IDs werden nicht übertragen. Der Prüfer entscheidet jede angebotene
Übernahme ausdrücklich. Keine blanket Freigabe und kein Reuse über Firmen/Stichtage.
