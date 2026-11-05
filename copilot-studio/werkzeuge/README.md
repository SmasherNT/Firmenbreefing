# Hilfsskript `anpassen.py` (noch zu bauen)

Die Werkzeug-Agenten W1–W4 rufen die vorhandenen Skripte aus `scripts/` auf.
Dazwischen sind ein paar kleine Anpassungen nötig, die heute der Hauptagent
erledigt. Sie kommen in ein einziges Hilfsskript `anpassen.py` in diesem Ordner.
`skills-bauen.py` legt es in jedes Werkzeug-Paket als `scripts/anpassen.py`.

Das Skript verändert keine Inhalte und trifft keine Prüfentscheidungen. Es
übernimmt nur, was Sprachmodelle schlecht können: Kennungen berechnen,
Prüfsummen exakt einsetzen, Dateien zusammenstellen.

## Befehle

| Befehl | Aufgerufen von | Aufgabe |
|---|---|---|
| `module --lauf L` | W1 basis | Kopffelder aus `facts-run.json` ergänzen; je Quelle `S-`-ID aus der URL berechnen (wie `prepare-facts.py --source-id`) und vorläufige IDs (Q1 …) in Aussagen, Belegen und Netzwerk ersetzen; einfache Formatfehler je Modul melden |
| `befunde --lauf L --phase X` | W2 | in `befund-*.json` Kopf, `format: review-source-part-v1`, `review_work_fingerprint` und `plan_fingerprint` aus dem Prüfstand einsetzen |
| `leitpruefung-eingabe --lauf L --phase X` | W2 | `leitpruefung-eingabe.json` bündeln: Phase, `source-findings`, Prüfauftrag (`review-work.py show`), Aussagen, Quellen, `module_views`, Netzwerk; in final Positionierung, SWOT und Kontexte |
| `leitentscheid --lauf L --phase X` | W3 | Identität und `review_work_fingerprint`, `plan_fingerprint`, `source_collection_fingerprint` in den Leitentscheid einsetzen → `_pruefstand/leitentscheid-X.json` |
| `bewertung --lauf L --rolle positioning\|swot` | W4, W1 final | Kopf, `input_fingerprint` und bei Positionierung `plan_fingerprint` aus dem jeweiligen Kontext einsetzen |
| `a-fakten --lauf L` | W4 | IDs aller A-geprüften Fakten der vier Kernmodule aus `review-basis.md` ausgeben |
| `pruefergebnis --lauf L --schritt S [--phase X] [--fehler …]` | W1, W3, W4 | `pruefergebnis.json` schreiben: `bestanden`, Anzahl `jobs`, `rueckgabe` je owner aus Fehlern, Korrektur/offen-Befunden, `material_errors` und blockierenden Rückfragen |

## Abnahme

Mit den Demodaten aus `examples/build-demo.py` einen Lauf-Ordner füllen, W1–W5
nacheinander ausführen (Agentenentscheidungen simuliert wie im Demo) und
prüfen, dass `briefing.html` dieselbe Struktur wie die Demo-HTML hat.
