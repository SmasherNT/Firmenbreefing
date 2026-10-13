# Markt-Deep-Dive: Vergleich und Vertiefung

Inhalt: Recherche und Aussagegrenzen · JSON-Vertrag · Prüfung und Darstellung.

Bei einem beauftragten regionalen Markt-Deep-Dive liefert market-facts zusätzlich
`market_dashboard` nach Schema 1. Region, Länder und Funktionen kommen aus dem
aktuellen Auftrag. Keine festen Golfstaaten-, Flugabwehr- oder Beispielwerte
übernehmen. Der Markt wird unabhängig von der Zielgesellschaft untersucht;
deren Präsenz steht auf Seite 1 nach references/regionale-praesenz.md. Der industrielle
Deep-Dive bleibt auf dem beauftragten Segment, das Portfolio deckt die Firma ab.
Ohne Regionenauftrag keine zusätzliche umfangreiche Länderanalyse.

## Recherche und Aussagegrenzen

- Fünf aufeinanderfolgende Kalenderjahre, möglichst die letzten verfügbaren
  abgeschlossenen Jahre. Quellen tatsächlich öffnen; jedes Land im selben
  Zeitraum, mit derselben Messgröße, Währung und Preis-/Umrechnungsbasis erfassen.
  Originalwert und belegte Normalisierung im M-Claim festhalten. Keine eigene
  Wechselkurs- oder Inflationsannahme. Ist, Plan und Prognose unterscheiden.
- Eine breite Budget-/Investitionsgröße ist Kontext, kein Marktvolumen des
  Zielsegments. Zusätzliches Segmentvolumen nur bei belastbaren, vergleichbaren
  Daten mit explizitem Marktumfang. Ohne Beleg keine Schätzung zur Grafikfüllung.
- Programme über stabile IDs deduplizieren. Nur die aktuell belegte Stufe zählen:
  Planung, angekündigt/genehmigt, beauftragt, in Auslieferung. Genehmigung oder
  Exportfreigabe ist kein Vertrag; Ankündigung ist kein Umsetzungsbeleg.
  Abgeschlossene/abgebrochene Programme nicht als laufende Auslieferung zählen.
  Länderübergreifende Gesamtprogramme nicht zusätzlich zu ihren Teilverträgen
  doppelt zählen. Abgrenzung, Auswahl und Suchabdeckung offen dokumentieren.
- Je Programm Auftraggeber, Anbieter, lokale Rolle, Statusdatum, geplante
  Zeitfenster, nächster belegter Schritt/offene Frage und Quellen. Werte separat
  als Vertragswert, Genehmigungsobergrenze oder Schätzung kennzeichnen; Einheit,
  Währung, Preisbasis und mehrjähriger Bezugszeitraum bleiben sichtbar.
  Unterschiedliche Programmwerte nicht zu einem jährlichen Marktvolumen addieren.
- Je Land und Funktion konkrete Akteure, Standort, Tätigkeit, belegte Rolle und
  Datum erfassen: Entwicklung, Lizenzfertigung, Integration, Wartung. Mehrere
  Rollen pro Zelle sind möglich. Keine Rolle allein aus Unternehmensnamen,
  Partnerschaft, Vertrieb oder nationalem Standort ableiten. Kein Reife-/Länderscore.
- Beschaffungsstelle, Vergabeverfahren, Registrierung, lokale Wertschöpfung,
  Partnerschaften und Zugangsbeschränkungen mit aktuellem Beleg recherchieren.
  Treiber/Rahmenbedingungen hier als Fakten; strategische Folgerungen bleiben
  geprüfte I-Claims im bestehenden Interpretationsschritt.
- Fehlende Finanzwerte als `value:null` plus `missing_reason`; Industrie ohne
  ausreichenden Beleg als leere `entries` plus `gap_reason`. Keine Nullwerte,
  interpolierten Werte, nationalen Fähigkeitslücken oder Markt-Vollständigkeit
  aus einer erfolglosen Suche ableiten. `gaps`/`coverage` weiterführen.

## JSON-Vertrag

`market_dashboard` enthält:

| Feld | Inhalt |
|---|---|
| schema_version | 1 |
| title, scope | Auftragsbezogener Titel und klare Abgrenzung |
| years | Genau fünf aufsteigende, aufeinanderfolgende Jahre |
| timeline_years | Aufsteigende, aufeinanderfolgende Kalenderjahre für Zeitfenster |
| programme_scope, programme_method | Segment, Auswahl, Deduplikation/Zählweise; keine Vollständigkeitsbehauptung |
| metrics | Nicht leere Liste: id, label, purpose (`context`/`segment`), unit, currency, price_basis, definition, claim_ids |
| functions | Nicht leere Liste: id, label; Funktionen aus dem aktuellen Auftrag |
| countries | Nicht leere Liste: id, label, coverage_note, series, programmes, roles, access, factors |

IDs beginnen mit einem Buchstaben und enthalten nur Buchstaben, Zahlen, `_`, `-`.
Länder-/Funktions-/Kennzahl-IDs sind jeweils eindeutig, Programm-IDs paketweit.
Alle Zahlen endlich und nicht negativ. Leere Programme/Access/Factors sind erlaubt.

`country.series` ordnet jeder Kennzahl-ID genau fünf Zeilen in Jahresreihenfolge zu:
`{year,value,status,comparable,claim_ids}`. status=`actual`/`plan`/`forecast`;
comparable ist ein Boolean. Bei false zusätzlich comparison_note, bei null-Wert
statt Status/Flag ein konkreter missing_reason (claim_ids darf dann leer sein).
Die Definition/Einheit/Währung/Preisbasis der Kennzahl gilt für jede Zeile;
inkompatible Werte nicht durch ein unzutreffendes comparable=true glätten.

`country.programmes[]`:
`id,label,status,status_date,customer,provider,local_role,next_step,claim_ids`.
status=`planning`/`announced`/`contracted`/`delivery`; status_date=YYYY-MM-DD,
nicht neuer als der Briefingstichtag. Unbekannte Details ausdrücklich im Text
benennen, keine Anbieter oder Meilensteine erfinden. Optional:

- value: `{amount,unit,currency,type,period,price_basis,claim_ids}`;
  type=`contract`/`ceiling`/`estimate`.
- window: `{start,end,label,claim_ids}`; start/end sind geordnete Kalenderjahre,
  label benennt die Art des Fensters, etwa „geplante Auslieferung“.

`country.roles` ordnet jeder Funktions-ID ein Objekt mit `entries` zu.
Jeder Eintrag: `{role,actor,location,activity,status_date,claim_ids}`;
role=`dev`/`license`/`integration`/`service`. Bei leerer Liste `gap_reason` ergänzen.
`country.access[]`: `{label,text,claim_ids}`.
`country.factors[]`: `{kind,label,text,claim_ids}`; kind=`driver`/`constraint`.

Jede faktische Kennzahl, Zahl, Programm-/Wert-/Zeitfensterzeile, Industrietätigkeit,
Zugangsangabe und Rahmenbedingung braucht konkrete Claim-Zuordnungen. Labels und
Kurztexte dürfen keine zusätzlichen Aussagen einführen. M-Claims bevorzugen;
vorhandene Fakten anderer Rollen über Claim-IDs wiederverwenden.

## Prüfung und Darstellung

prepare-facts validiert Struktur, IDs, Werte, Jahre und Referenzen und übernimmt
das gesamte Dashboard in den Paket-Fingerprint. Sämtliche referenzierten Fakten
stehen in required_full_review_ids für den bestehenden Basis-Reviewer. Die
Quellenprüfung umfasst Zahlen, Normierung, Status, Rollen und semantische
Zuordnungen; ein Schema-Pass ist keine Quellenfreigabe. Neue/geänderte Inhalte
und Mappings gezielt prüfen, Paket erneut stempeln. Keine zusätzliche Agenten-
oder Modellrunde für Grafikformatierung und lokale Rechenoperationen.

Seite 3 zeigt zuerst pro Kennzahl zwei Charts: letzter Jahreswert und CAGR mit
gemeinsamen Achsen je Vergleich. Nur vergleichbare Ist-Werte werden geplottet;
Plan/Prognose bleibt im Datenblatt. CAGR nur aus fünf vollständigen vergleichbaren
Ist-Jahren, mit positiver Ausgangsbasis und tatsächlicher Jahresdifferenz:
`(Endwert/Anfangswert)^(1/(Endjahr-Anfangsjahr))-1`. Negative Entwicklung steht
links der Nulllinie. Fehlende/inkompatible Daten werden sichtbar ausgelassen.
Programmzahlen entstehen lokal ausschließlich aus den deduplizierten Einträgen.
Industriefarben kodieren Kategorien, kein Ranking.

Länderbalken/Industriezelle öffnen die Vertiefung unterhalb: Programme und
Zeitfenster, Industrie und Marktzugang, Werte/Methode/Quellen. Auswahl über
Länderbuttons und Tastatur. Alle Fakten, Unsicherheiten, Originalquellen und
Belegstellen bleiben in nativen Details, ohne Dialog; vorhandene Themenkarten
und regionale Einordnungen folgen. Ohne JavaScript stehen sämtliche Länderprofile
bereit. Druck enthält alle Daten/Profile und stellt die vorherige Ansicht wieder her.
Ohne Dashboard bleiben vorhandene Faktenpakete mit Themen-/Regionenkarten nutzbar;
es werden keine Beispielwerte oder leeren Scheingrafiken eingesetzt.
