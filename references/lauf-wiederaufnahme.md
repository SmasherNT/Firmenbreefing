# Unterbrochene v2-Läufe sicher fortsetzen

Inhalt: Grenzen · Initialisierung · Checkpoints · Fortsetzung/Korrekturen.
Nur den konkret beauftragten laufenden/unterbrochenen Lauf fortsetzen. Neue Firma,
neuer Auftrag, anderer Themenumfang oder Stichtag erhalten weiterhin eine neue ID.
Keine Suche nach dem „neuesten“ ähnlichen Lauf und kein Reuse über Läufe hinweg.
Agentenkontexte, Rollen, Rechercheumfang, Modellwahl und Pflichtreviews unverändert.
resume-run.py koordiniert keine Agenten und erzeugt keine inhaltlichen Freigaben.

## Einmal initialisieren

Nach Originalauftrag/Manifest und Cacheinitialisierung, vor den Faktenrollen:

```bash
python3 scripts/resume-run.py --state <Lauf>/work/checkpoints.json init --manifest <Lauf>/input/facts-run.json --request <Lauf>/input/auftrag.md --cache <Lauf>/work/document-cache --full
```

Für beauftragte Faktenphasentests zusätzlich `--target facts` und ohne `--full`;
für reine Interpretation `--target interpretation`. Nur bei explizit alleiniger
SWOT/Positionierung `--interpretation-roles swot` bzw. `positioning` wählen.
Vollbriefings mit `--full` binden den Vergleichsplan automatisch. Bei anderen
Vergleichsaufträgen `comparison_plan_path` im Manifest oder `--with-plan` bei init:
damit ist der Plan zwingende Abhängigkeit vor Markt, Paket und Ableitungen.
Nach init Auftrag/Manifest nicht verändern; Themenreihenfolge, Person, Scope und
alle sonstigen Manifestfelder sind gebunden. Zustand nicht zurücksetzen.

## Nach tatsächlichem Abschluss lokal speichern

Nur der Hauptagent schreibt Checkpoints, nachdem die zuständige Rolle ihre Datei
fertiggestellt hat und vorhandene Validierung/Review erfolgt ist. Dateien existieren
reicht nicht. Keine laufenden, gescheiterten, blockierten oder ungeprüft freigegebenen
Schritte als fertig markieren. Faktenrollen-Checkpoints bedeuten nur fertiggestellte
formal gültige Recherchedatei; Inhaltsfreigabe erfolgt weiterhin im Basisreview.

```bash
python3 scripts/resume-run.py --state <Zustand> checkpoint --stage portfolio --output module=<portfolio-facts.json>
python3 scripts/resume-run.py --state <Zustand> checkpoint --stage plan --input context=<context-facts.json> portfolio=<portfolio-facts.json> --output plan=<comparison-plan.json>
python3 scripts/resume-run.py --state <Zustand> checkpoint --stage market --input plan=<comparison-plan.json> --output module=<market-facts.json>
```

Weitere tatsächlich verwendete Eingabedateien immer als `--input name=pfad`
angeben, auch Auftragsergänzungen, Agenten-/Tool-Rückgaben und wiederverwendete
Module. Für modulübergreifende Claim-IDs Schwesterdatei unter ihrem Rollennamen
mitgeben, etwa `--input cluster=<cluster-facts.json>` beim Portfolio. Unbekannte
Referenzen werden nicht übersprungen. Zusätzliche Abhängigkeiten bei Bedarf mit
`--depends-on context portfolio` erklären.
Wenn ein referenziertes Marktmodul Vergleichsbeobachtungen enthält, auch dessen
Plan als `--input plan=<comparison-plan.json>` zur formalen Prüfung mitgeben.
Referenzierte vorhandene Checkpoint-
Ausgaben werden automatisch als Abhängigkeit erkannt; Zyklen sind gesperrt.
Dateien, die vor dem Checkpoint ihrer Eigentümerrolle verwendet wurden, bleiben
an ihre vollständigen Bytes gebunden; beim erneuten Checkpointen keine nachträgliche
Reihenfolgekante hinzufügen. Pflichtabhängigkeiten wie Markt → Plan bleiben zwingend.
Planinputs nennen die tatsächlichen Identitäts-/Produktfakten, auf denen er beruht.

| Schritt (`--stage`) | Pflichtinputs (`--input`) | Outputs (`--output`) |
|---|---|---|
| context, portfolio, cluster | Alle tatsächlich verwendeten Zusatz-/Schwestermodule | module=Faktenmodul |
| plan | Tatsächliche Planbasis | plan=Vergleichsplan |
| market | plan bei Vergleich, weitere verwendete Module | module=Marktmodul |
| facts | context/portfolio/cluster/market jeweils soweit ausgewählt; plan bei Vergleich | facts=review-packet.json validation=facts-validation.json |
| basis-review | facts, validation, work=review-work-basis.json, draft=review-basis-draft.json; plan bei Vergleich | review=review-basis.md |
| positioning | facts, basis-review; plan bei Vergleich; weitere verwendete Eingaben | output=positioning.json context=positioning-context.json validation=positioning-validation.json |
| swot | facts, basis-review; positioning und positioning-context soweit beauftragt; plan bei Vergleich | output=swot.json context=swot-context.json validation=swot-validation.json |
| final-review | facts, basis-review, basis-work=review-work-basis.json, validation=interpretation-validation.json, work=review-work-final.json, draft=review-final-draft.json; positioning/positioning-context und swot/swot-context soweit beauftragt; plan bei Vergleich | review=review-final.md |
| html | facts, basis-review, final-review; positioning/positioning-context und swot/swot-context soweit beauftragt; plan bei Vergleich | html=Firmenbriefing.html |

Beispiel für die Basisfreigabe:

```bash
python3 scripts/resume-run.py --state <Zustand> checkpoint --stage basis-review --input facts=<review-packet.json> validation=<facts-validation.json> work=<review-work-basis.json> draft=<review-basis-draft.json> plan=<comparison-plan.json> --output review=<review-basis.md>
```

Planargumente bei Aufträgen ohne Vergleich weglassen. Kontext-/Validierungsdateien
und Inhalte durch die bestehenden Helfer unverändert erstellen. Kompakte Entwürfe
und Review-Arbeitsblätter bleiben Pflicht für wiederaufnehmbare Freigaben; alte
Legacy-Reviews ohne diese Bindung bleiben im regulären Ablauf verwendbar, werden
aber nicht automatisch zu wiederaufnehmbaren Freigaben erklärt.

## Fortsetzen und erneut prüfen

```bash
python3 scripts/resume-run.py --state <derselbe-Lauf>/work/checkpoints.json resume
```

Nur `reusable` übernehmen; `pending` fehlt und `invalid` benötigt Bearbeitung.
`next_stage` nennt den ersten offenen Schritt, unabhängige gültige Teilrecherchen
bleiben erhalten. Der Helfer prüft die Originalbytes des Auftrags/Manifests,
vollständige Ein-/Ausgabedateien, Rollenzuordnung, Quellenoriginale samt Textableitung,
Abhängigkeiten, aktuelle Verträge/Validatoren und für HTML die aktuelle Vorlage.
Bestehende Validierer und explizite Entwürfe werden erneut abgeglichen. Geänderter
Review, fehlende A-Entscheidung oder blockierende Frage bleibt gesperrt.

Quellenaufnahmen älter als 24 Stunden erfordern erneuten tatsächlichen Abruf:
HTTP-Original mit source-cache.py fetch --refresh revalidieren; Tool-/Browserquellen
neu öffnen und mit Herkunft aufnehmen. Keine bloße Neuablage eines alten Tooltexts
zum Erneuern des Zeitstempels. Abruffehler oder fehlende/korrupte Originale lassen
den Schritt gesperrt. HTTP-Abrufe werden vor dem Netzaufruf als laufend markiert;
nach Fehler/Abbruch blockiert auch ein vorher noch junger Cache den Checkpoint
bis zum echten Erfolg. Ein normaler Cache-Hit löscht diese Sperre nicht.
Unveränderter HTTP-304/Inhalt erhält seine Bindung; geänderte
Original-/Tool-Snapshots erneuern betroffene Fakten und Reviews. Ereignis-/Stichtags-
grenzen bleiben der ursprüngliche Auftrag, nicht das heutige Abrufdatum. Bei
Änderungshinweis auch vor Ablauf der 24 Stunden gezielt revalidieren.

Geänderte Artefakte/Belege machen den Schritt und seine abhängigen Folgeschritte
ungültig. Zuständige Rolle korrigiert bzw. überprüft den vorhandenen Stand; bei
reiner Validator-/Vertragsänderung vorhandene Datei zuerst erneut validieren.
Neue Fakten weiter durch Basisreview, betroffene Ableitungen durch Schlussreview.
Nach tatsächlicher Neubearbeitung Checkpoint erneut schreiben; alte Outputs nicht
löschen und alte Reviews nicht umstempeln. Inhaltliche Probleme ohne Dateidifferenz
ausdrücklich sperren:

```bash
python3 scripts/resume-run.py --state <Zustand> invalidate --stage portfolio --reason 'Neu erkannter fachlicher Widerspruch; zuständige Rolle prüft erneut.'
```

Zustandsdateien werden atomar unter Prozesslock geschrieben; abgebrochene Schreib-
vorgänge erzeugen keinen halben gültigen Checkpoint. Korrupter Zustand oder anderer
Auftrag blockiert Wiederaufnahme. Regulären Ablauf aus tatsächlichen Dateien und
neuen Prüfungen fortführen; Zustand nie von Hand als freigegeben reparieren.
Ohne Checkpoints weiterhin regulär arbeiten, keine Dateiexistenz als Abschluss
übernehmen. `ready_for_visual_qa` ist keine visuelle Abnahme: Browser-/Druckprüfung,
output/abnahme.md und Git-Übertragung bleiben nach bisherigem Vertrag erforderlich.
Helfer verwendet Python auf einer POSIX-Umgebung (Prozesslock per flock).
