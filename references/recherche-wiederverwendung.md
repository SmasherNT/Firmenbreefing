# Gemeinsame Dokumente und Fakten im aktuellen Lauf

Inhalt: Dokumentcache · Faktenindex · Zuständigkeit/Prüfung · Grenzen.

Verbindlich für neue facts-v2-Läufe; bestehende Läufe ohne Cache bleiben nutzbar.
Vollständige Fakten-/Quellen-/Bewertungskontexte und HTML-Inhalte erhalten.
Keine Projektion, Feldkürzung oder neue Auswahlregeln für positioning-/SWOT-Kontexte.
Modellwahl, Rechercheumfang, Gegenrecherche und Prüftiefen bleiben unverändert.

## Dokumentcache vor der Recherche initialisieren

Hauptagent führt einmal aus und nennt denselben Pfad in jeder Fakten-/Review-Delegation:

```bash
python3 scripts/source-cache.py --manifest <Lauf>/input/facts-run.json --cache <Lauf>/work/document-cache init
```

Cache gehört exakt zu run_id/company/as_of. Neuer Lauf verwendet einen neuen Cache;
alte Claims oder Quellenfreigaben nie aus früheren Firmen-/Stichtagsläufen übernehmen.
Je URL eigener Lock; atomare Dateien verhindern parallele Index-/Download-Verluste.
Kein gemeinsames sources.json durch Faktenagenten bearbeiten.

## Quellen öffnen, Original behalten

Vor erneutem Quellenabruf dieselbe Dokument-URL über den Cache aufrufen:

```bash
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> fetch --url '<Dokument-URL>'
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> show --source-id <S-ID>
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> read --source-id <S-ID>
```

`fetch` lädt eine öffentliche HTTP(S)-Quelle einmal herunter und gibt nur Metadaten
und lokale Pfade zurück. Weitere Aufrufe im selben Lauf verwenden den geprüften
Dateihash des gespeicherten Originals. Quelle per Read/Bash tatsächlich lesen;
ein erfolgreicher Download ist kein gelesener Beleg. Quelle bleibt Webseitendatum/
Ereignisdatum nach Auftrag, unabhängig vom technischen Download-Zeitpunkt.

Originalbytes unter documents/<S-ID>/versions/<Inhaltshash>/source.bin behalten.
HTML-Volltext ist eine mechanische Ableitung ohne script/style; ursprüngliche HTML
bleibt zugänglich. PDF mit lokalem pdftotext erschließen, PDF-Seiten markieren.
Bei fehlendem Extraktor, Scan, Encodingfehler, dynamischer Seite oder Zugriffsgrenze
Original-PDF/Browser/WebFetch nutzen; kein leerer Text als fehlende Aktivität werten.
Ableitung nicht als selbständige Quelle behandeln. Belegstelle nennt offizielle
Seite/Abschnitt/Absatz; Cache-Zeilen dienen nur der Navigation.

Bereits heruntergeladenes Original oder vollständig geöffneten Tool-Text speichern:

```bash
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> store --url '<Dokument-URL>' --input <lokale-Datei> --content-type text/html --capture-kind local-original --capture-note '<Abrufwerkzeug und Zeitpunkt>'
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> store --url '<Dokument-URL>' --input <vollständiger-geöffneter-Text.txt> --content-type text/plain --capture-kind opened-tool-text --capture-note '<Tool, Zeitpunkt, Zugriffsumfang und Grenzen>'
```

Keine Modellzusammenfassung oder Suchsnippet als Original speichern. opened-tool-text
ist ausdrücklich eine Tool-Textaufnahme, kein behauptetes Original-HTML/PDF.
Quelle/Beleg bei Zweifeln im Original unabhängig prüfen. Fragment bleibt
Belegstelle; S-ID entspricht prepare-facts.py, Query-Parameter bleiben erhalten.
Andere URLs/Kopien bleiben andere Dokumente; Ursprungsbeleg nach Quellenvertrag nennen.

Bei Änderungshinweis, widersprüchlichem Status oder begründetem Aktualitätszweifel:

```bash
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> fetch --url '<Dokument-URL>' --refresh
```

ETag/Last-Modified erlauben HTTP-304-Revalidierung. Veränderte Bytes erzeugen eine
neue Version (`content_changed=true`); alte Originale, Textableitungen und Abruf-
metadaten bleiben erhalten. Betroffene Claims/Zuordnungen erneut prüfen, Reviewer
Snapshot-Hash/Abrufzustand im vorhandenen Review dokumentieren lassen. Netzfehler
bei Refresh gibt einen Fehler, keine stillschweigende aktuelle Quellenfreigabe.
Ein Review bleibt eine unabhängige Inhaltsentscheidung; Cache ist kein Prüfurteil.

## Vorhandene Fakten finden und über IDs wiederverwenden

Nach fertig geschriebenen Modulen lokal einen Index bauen, vor weiterer Recherche
zu überlappenden Fragen prüfen. Nur bereits vorhandene Moduldateien übergeben:

```bash
python3 scripts/fact-index.py --manifest <Manifest> build --modules <fertige-Module...> --out <Lauf>/work/facts-index.json
python3 scripts/fact-index.py --manifest <Manifest> find --index <Lauf>/work/facts-index.json --query '<Akteur Produkt Standort>'
python3 scripts/fact-index.py --manifest <Manifest> find --index <Lauf>/work/facts-index.json --claim-ids <bekannte-IDs...>
```

Hauptagent baut nach dem ersten fertigen Modul und vor abhängigen Übergaben neu;
weitere fertige Module ergänzen. Faktenagenten verändern den gemeinsamen Index
nicht parallel. `prepare-facts.py --out` erzeugt den vollständigen Index zusätzlich
zu seinen bisherigen Dateien. Neue Datei ist eine Suchhilfe, kein Agentenkontext.
Index enthält vollständige Claims, Quelle, Eigentümerrolle und lokale Fingerprints;
Änderung einer Eingabedatei erzwingt Neubau. Fehlende Rollen sichtbar ausweisen.
Status immer unreviewed-index: vor strategischer Nutzung unverändert A-Prüfung nötig.

Passenden Claim mit seiner vorhandenen ID in `reuse_claim_ids` und fachlichen
Zuordnungen verwenden; Aussage/Quelle/Produkt-/Länder-/Zeitumfang zuerst prüfen.
Keine Kopie unter neuem Präfix erzeugen und keine Analystendatei einer anderen
Rolle bearbeiten. Neue sachlich andere Aussage erhält eigene ID. Nicht identische
Belege/Status oder widersprüchliche Angaben getrennt erhalten und prüfen.
Die kanonische Eigentümerrolle bleibt: P Portfolio, C Struktur/Beziehungen,
M Markt, T/H Themen/Person. Erforderliche Kantenclaims bleiben C-Claims.
Produkt-/Regionsansichten dürfen passende C-/P-/M-Fakten referenzieren.

`duplicate_candidates` markiert nur mögliche Doppelungen gleicher normalisierter
Aussage/Art/Quellen/Zeit. Kein automatisches Zusammenführen oder Entfernen.
Zuständige Rollen lösen echte Dubletten vor Review durch eine kanonische ID;
alle bisherigen Referenzen aktualisieren, lokale Validierung erneut ausführen.
Bereits parallel entstandene Fakten sind nicht stillschweigend löschbar.

## Abnahme

```bash
python3 scripts/source-cache.py --manifest <Manifest> --cache <Cache> stats
```

Downloads, Cache-Hits, Importe und Revalidierungen als Dokumentoperationen zählen.
Das sind keine gemessenen Modelltoken oder Kosten. Originalcache nicht committen;
Quellenmetadaten, Claims, Review-Befunde und Abnahme nach bisherigem Vertrag speichern.
