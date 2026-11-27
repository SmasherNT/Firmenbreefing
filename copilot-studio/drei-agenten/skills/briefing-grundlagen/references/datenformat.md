# Datenformat briefing-daten.json (Schema firmenbriefing/2)

Alle Texte auf Deutsch. Felder, die es nicht gibt, weglassen. Jede Zeile mit
`claims` braucht mindestens einen A-Claim; eine Zeile ohne Beleg gehört als Text
in `luecken`. Das Skript `validieren` prüft alle hier genannten Pflichtfelder,
erlaubten Werte und Mindestregeln.

## Oberste Ebene

```json
{
 "schema": "firmenbriefing/2",
 "auftrag": {},
 "phasen": {"auftrag": "fertig", "firmenbasis": "fertig", "portfolio": "teilweise"},
 "quellen": [],
 "claims": [],
 "inhalt": {"unternehmen": {}, "personen": [], "portfolio": {}, "cluster": {}, "markt": {}, "fokus": []},
 "interpretation": {},
 "offen": {"luecken": [], "fragen": []},
 "pruefung": {}
}
```

`pruefung` schreibt nur der Prüf-Agent. `phasen`: `fertig`, `teilweise`, `offen`.

## auftrag

```json
{"firma": "Firma AG", "kurzname": "Firma", "website": "https://…", "stichtag": "2026-11-27",
 "nachricht": "Originalnachricht unverändert", "modus": "voll", "module": ["portfolio"],
 "fokus": [{"id": "lkw", "titel": "Europäische Lkw-OEMs"}],
 "personen": [{"name": "…", "position_laut_nutzer": "…"}]}
```

`modus`: `voll` oder `modul`. `kurzname` ist der Name, mit dem das Zielunternehmen
in Beziehungen und Vergleichen geschrieben wird. Fokus-IDs nur aus Buchstaben,
Ziffern, `_` und `-`.

## quellen

```json
{"id": "Q1", "titel": "Geschäftsbericht 2025", "herausgeber": "Firma AG", "datum": "2026-03-20",
 "url": "https://…", "abruf": "2026-11-27", "art": "original", "typ": "geschaeftsbericht",
 "geoeffnet": true, "geschaeftsjahr": "2025", "seite": "34", "abschnitt": "Segmentbericht"}
```

`typ` (Pflicht): `geschaeftsbericht`, `investor`, `produktseite`, `datenblatt`,
`pressemitteilung`, `register`, `behoerde`, `vergabe`, `verband`, `statistik`,
`medien`, `fachmedien`, `sonstiges`. `art`: `original`, `medien`, `register`,
`datenbank`, `sonstige`. `geoeffnet: false` heißt nur Suchtreffer.

## claims

```json
{"id": "P3", "aussage": "Ein Satz mit Bezugsobjekt und Zeitraum.", "ursprung": "hersteller",
 "status": "Serie laut Hersteller", "datum": "2026-05-02", "quellen": ["Q1"],
 "belegstelle": "S. 22, Abschnitt Produkte", "unsicherheit": "Nur Herstellerangabe.", "stufe": "A"}
```

Pflicht: `id`, `aussage`, `ursprung` (`fakt`, `hersteller`, `partner`, `medien`,
`nutzer`), `quellen`, `stufe` (`A` oder `B`). Bei A immer `belegstelle`. Der
Prüf-Agent setzt bei neuen Claims `herkunft: "vertiefung"` automatisch und bei
Korrekturen optional `korrekturgrund`.

## inhalt.unternehmen

```json
{"profil": [{"feld": "Umsatz 2025", "wert": "412 Mio. EUR (Konzern)", "claims": ["T1"]}],
 "timeline": [{"datum": "2026-09-02", "ereignis": "… (laut Fachmedium)", "status": "eröffnet", "claims": ["T3"]}],
 "luecken": ["…"], "ausnahmen": []}
```

Timeline nur Stichtag minus vier Kalendermonate bis Stichtag, Ereignisdatum.

## inhalt.personen (je Person ein Eintrag)

```json
{"name": "…", "position_laut_nutzer": "…", "verifizierung": "bestätigt | abweichend: … | nicht verifiziert",
 "einleitung": {"text": "…", "claims": ["H1"]},
 "snapshot": [{"feld": "Rolle", "wert": "…", "claims": ["H1"]}],
 "werdegang": [{"zeitraum": "2019–2023 oder Zeitraum nicht belegt", "organisation": "…", "rolle": "…", "kontext": "…", "claims": ["H2"]}],
 "fachprofil": [{"titel": "…", "text": "…", "claims": ["H3"]}],
 "verantwortung": [{"titel": "…", "text": "…", "claims": ["H1"]}],
 "medien": [{"datum": "2026-10-05", "ereignisdatum": "2026-10-04", "kategorie": "eigene | offiziell | medien",
             "format": "Interview", "titel": "…", "vorschau": "…", "zugriff": "frei, vollständig gelesen",
             "zitat": "optional, kurz und wörtlich", "claims": ["H4"]}],
 "luecken": ["…"], "ausnahmen": []}
```

Snapshot höchstens sechs Felder. Medien: Veröffentlichungen der letzten vier Monate.

## inhalt.portfolio

```json
{"felder": [{"name": "Luftverteidigung", "angebote": [
   {"name": "System B", "kurzname": "Sys B", "anwendung": "…", "eigenschaften": "… (Herstellerangabe)",
    "status_stufe": "kundenauftrag", "status": "Auftrag laut Fachmedium, März 2026",
    "claims": ["P12", "P13"], "abschnitte": [{"titel": "Technik", "claims": ["P14"]}]}]}],
 "luecken": ["…"], "ausnahmen": []}
```

Ein Angebot ist eine Produktfamilie oder ein System, nie die Division. Namen
eindeutig. `status_stufe`: `angekuendigt`, `prototyp`, `test`, `kundenauftrag`,
`im_einsatz`, `serie`, `eingestellt`, `nicht_belegt`. Geschäftsfelder werden
beim Zusammenführen einzeln über `name` ersetzt.

## inhalt.cluster

```json
{"akteure": [{"name": "Beispiel Kälte AG", "langname": "…", "art": "jv", "bereich": "konzern", "fokus": false}],
 "beziehungen": [{"von": "Firma", "zu": "Beispiel Kälte AG", "typ": "Joint Venture", "gegenstand": "Großanlagen",
   "anteil_rolle": "50 % Kapital", "kapitalanteil": "50 %", "stimmrechte": "…", "kontrolle": "nicht belegt",
   "art": "direkt", "status": "laufend", "datum": "2025-12", "produkte": ["System B"],
   "unsicherheit": "…", "claims": ["C2"]}],
 "berichte": [{"akteur": "…", "bericht": "Geschäftsbericht 2025", "jahr": "2025", "abschnitte": "S. 80–84", "status": "analysiert"}],
 "luecken": ["…"], "ausnahmen": []}
```

- Das Zielunternehmen heißt in `von`/`zu` genau wie `auftrag.firma` oder `auftrag.kurzname`.
- `typ` genau einer von: Eigentum, Tochtergesellschaft, Joint Venture, Kooperation,
  Kunde, Lieferant, Projekt, Lizenz, Mandat, historisch. Bei Eigentum zeigt `von`
  auf den Eigentümer, `zu` auf die gehaltene Gesellschaft.
- `art`: direkt, indirekt, Überschneidung. `datum`: JJJJ-MM oder JJJJ-MM-TT.
- `produkte`: nur Angebotsnamen aus dem Portfolio.
- `akteure` ist optional, aber empfohlen: `art` (eigentuemer, tochter, jv, partner,
  kunde, zulieferer, projekt, institution, person, sonstige) und `bereich`
  (kapital, konzern, technologie, markt) bestimmen Farbe und Gruppe im Netzwerk.
- `berichte.status`: analysiert, nicht gefunden, nicht zugänglich, teilweise lesbar.

## inhalt.markt

```json
{"kennzahlen": [{"kennzahl": "…", "wert": "1.200 Stück", "definition": "Region, Jahr, Abgrenzung", "claims": ["M1"]}],
 "vergleich": {"einheit": "verglichene Angebotsart",
  "kriterien": [
   {"id": "temp", "name": "Max. Vorlauftemperatur", "typ": "kennzahl", "einheit": "°C",
    "frage": "Welche Höchsttemperatur nennt der Hersteller?", "beleganforderung": "Datenblatt", "bedingungen": "Maximalwert"},
   {"id": "einsatz", "name": "Belegter Einsatzstand", "typ": "evidenzstufe", "frage": "…", "beleganforderung": "…",
    "stufen": {"1": "angekündigt", "2": "Pilot oder Test", "3": "in Betrieb", "4": "Serie mit wiederholten Lieferungen"}},
   {"id": "fertigung", "name": "Fertigungs- und Lieferfähigkeit", "typ": "profil", "frage": "…", "beleganforderung": "…"}],
  "zeilen": [{"akteur": "Firma", "angebot": "System B", "referenz": true, "zellen": {
    "temp": {"wert": 150, "text": "bis zu 150 °C (Herstellerangabe)", "claims": ["P1"]},
    "einsatz": {"stufe": 3, "text": "in Betrieb laut Medien", "titel": "optional kurz", "vorschau": "optional",
                "aussage": "…", "einordnung": "Warum diese Stufe", "grenze": "…", "claims": ["P5"]},
    "fertigung": {"text": "Pilotserie laut Geschäftsbericht", "claims": ["P2"]}}}]},
 "praesenz": [{"region": "Deutschland", "laender": ["Deutschland"], "schwerpunkt": "…", "produktbezug": "…",
   "praesenzart": "optionale Kurzbeschreibung", "fokus": true, "abdeckung": "Such- und Beleggrenze",
   "aktivitaeten": [{"akteur": "Rechtsträger", "land": "Deutschland", "ort": "Hamburg", "funktion": "Service",
     "betreiber": "eigen", "status": "operativ", "statusdatum": "2026-09-02", "produktbezug": "…",
     "beschreibung": "…", "eigentum": "eigene Gesellschaft", "claims": ["M6"],
     "kontrolle": "nur bei jv: alleinig | gemeinsam | keine | unbekannt", "kontrollbeleg": ["C2"], "kontrollnotiz": "…"}]}],
 "luecken": ["…"], "ausnahmen": []}
```

- Kriterium `typ`: `kennzahl` (Zelle braucht Zahl in `wert`, Kriterium braucht
  `einheit`), `evidenzstufe` (Kriterium braucht `stufen`, Zelle eine dieser
  Stufen in `stufe`) oder `profil` (Text).
- Fehlt eine Zelle, zeigt die HTML „nicht öffentlich belegt“. Nicht anwendbar:
  `{"nicht_anwendbar": true, "text": "Grund", "claims": [...]}`.
- Präsenz `funktion`: Büro, Produktion, Integration, Service, Entwicklung,
  Partner, Kundenaktivität, Zugang, Auslandsbetreuung. `betreiber`: eigen,
  partner, jv, kunde, ausland. `status`: operativ, angekündigt. Belegte
  JV-Kontrolle (`alleinig`, `gemeinsam`) braucht `kontrollbeleg`.

## inhalt.fokus (je Fokusthema ein Eintrag)

```json
{"id": "lkw", "titel": "Europäische Lkw-OEMs",
 "ueberblick": {"text": "Ein Orientierungssatz.", "claims": ["F_lkw_1"]},
 "definition": {"text": "…", "region": "Europa", "zeitraum": "2025–2026", "abgrenzung": "…", "claims": ["F_lkw_1"]},
 "kennzahlen": [{"kennzahl": "Neuzulassungen schwerer Lkw", "wert": 312000, "einheit": "Stück", "zusatz": "rund",
                 "zeitraum": "2025", "abgrenzung": "EU", "definition": "…", "typ": "lieferung", "claims": ["F_lkw_2"]}],
 "segmente": [{"titel": "…", "text": "…", "claims": ["F_lkw_3"]}],
 "wertschoepfung": [{"titel": "…", "text": "…", "claims": ["F_lkw_4"]}],
 "akteure": [{"akteur": "…", "rolle": "…", "angebot": "…", "segment": "…", "stand": "…", "claims": ["F_lkw_5"]}],
 "auswahl": "Kriterien der Akteursauswahl",
 "kernaussagen": [{"titel": "Belegte Kernaussage in einem Satz", "claims": ["F_lkw_6"]}],
 "entwicklungen": [{"datum": "2026-08-15", "ereignis": "…", "status": "…", "claims": ["F_lkw_7"]}],
 "fragen": [{"frage": "Neutrale Frage für das Meeting?", "claims": ["F_lkw_7"]}],
 "glossar": [{"begriff": "…", "definition": "…", "claims": ["F_lkw_1"]}],
 "luecken": ["…"], "ausnahmen": []}
```

Kennzahl `wert` ist eine Zahl ab 0, `typ`: marktvolumen, budget,
rahmenhoechstwert, auftrag, lieferung, kapazitaet, technisch, struktur, sonstige.
Entwicklungen: Stichtag minus sechs Monate bis Stichtag. Claims mit Präfix `F_<id>_`.

## interpretation

Jedes Objekt hat eine eindeutige `id` (I… oder S…) und `basis` mit Claim- oder
Interpretations-IDs. Keine Zahl oder Tatsache, die nicht in der Basis steht.

```json
{
 "summary": {
  "highlights": [{"id": "I1", "label": "max. 60 Zeichen", "wert": "412 Mio. EUR", "art": "kennzahl | status",
                  "bezug": "Konzern, Segment, Produkt oder Region", "zeitraum": "…", "basis": ["T1"]}],
  "kernaussagen": [{"id": "I4", "titel": "max. 72 Zeichen", "vorschau": "max. 160 Zeichen", "aussage": "…",
                    "begruendung": "…", "methode": "…", "unsicherheit": "…", "basis": ["P1", "M2"]}]},
 "keyfacts": [{"id": "I8", "modul": "portfolio | cluster | markt", "titel": "…", "fakt": "…", "insight": "…",
               "begruendung": "…", "unsicherheit": "…", "basis": ["P2"]}],
 "reife": [{"id": "I11", "angebot": "System B", "stufe": 4, "aussage": "…", "begruendung": "…",
            "unsicherheit": "…", "naechste_stufe": "Warum die nächste Stufe nicht belegt ist", "abdeckung": "…", "basis": ["P12"]}],
 "praesenz": [{"id": "I15", "region": "Deutschland", "stufe": 4, "status": "bewertet | geplant | nicht eindeutig bestimmbar",
               "aussage": "…", "begruendung": "…", "methode": "regional-presence-v2", "unsicherheit": "…",
               "naechste_stufe": "…", "abdeckung": "…", "basis": ["M6"]}],
 "positionierung": [{"id": "I16", "dimension": "Netzwerkposition", "urteil": "kurz", "aussage": "…", "methode": "…",
                     "begruendung": "…", "unsicherheit": "…", "basis": ["C2"]}],
 "swot": {"staerken": [{"id": "S1", "titel": "…", "aussage": "…", "begruendung": "…", "einschraenkung": "…", "basis": ["I4"]}],
          "schwaechen": [], "chancen": [], "risiken": []},
 "grenzen": ["gemeinsame Grenze einmal nennen"]
}
```

- `reife`: je Portfolio-Angebot genau ein Eintrag, `angebot` = Angebotsname,
  `stufe` 1 bis 6 oder `null` (nicht eindeutig bestimmbar). Ohne Eintrag leitet
  die HTML die Stufe aus `status_stufe` ab und kennzeichnet das.
- `praesenz`: je Region genau ein Eintrag, `stufe` 1 bis 5 oder `null`.
- Keyfacts höchstens drei je Modul, SWOT höchstens drei je Quadrant.

## offen

`luecken`: wichtige Datenlücken und Widersprüche. `fragen`: neutrale
Gesprächsfragen, keine Behauptungen über die Firma.

## Mindestregeln

Fehler, wenn nicht erfüllt und im Kapitel keine Ausnahme mit derselben Regel-ID
steht. Ausnahme: `{"regel": "<id>", "grund": "Suchwege und Ergebnis, mindestens 40 Zeichen"}`.

| Regel-ID | Anforderung |
|---|---|
| unternehmen.profil | Profil mit mindestens vier belegten Zeilen |
| unternehmen.medien | mindestens zwei Nachrichten- oder Fachmedien |
| personen.quellen | je Person mindestens zwei verschiedene Quellen |
| portfolio.angebote_je_feld | je Geschäftsfeld mindestens zwei Angebote |
| portfolio.geschaeftsbericht | mindestens ein Geschäftsbericht oder eine Investorenunterlage |
| portfolio.medien | mindestens zwei Nachrichten- oder Fachmedien |
| portfolio.status | höchstens die Hälfte der Angebote `nicht_belegt` |
| cluster.beziehungen | mindestens drei Beziehungen |
| cluster.bericht | mindestens ein Bericht mit Status „analysiert“ |
| cluster.medien | mindestens zwei Nachrichten- oder Fachmedien |
| markt.kennzahlen | mindestens zwei Kennzahlen mit Definition |
| markt.vergleich | mindestens drei Zeilen und drei Kriterien |
| markt.medien | mindestens zwei Nachrichten- oder Fachmedien |
| fokus.kennzahlen | je Fokus mindestens vier Kennzahlen |
| fokus.akteure | je Fokus mindestens drei Akteure |
| fokus.kernaussagen | je Fokus drei bis fünf Kernaussagen |

## pruefung (nur Prüf-Agent)

```json
{
 "stand": "2026-11-28",
 "umfang": {"kapitel": "alle", "nur_a": false},
 "zusammenfassung": "Ein bis zwei Sätze.",
 "claims": [{"id": "P2", "urteil": "korrigiert", "stufe": "A", "beleg": "URL und Stelle", "begruendung": "…", "korrektur": "…"}],
 "ableitungen": [{"id": "I11", "urteil": "angepasst", "begruendung": "…"}],
 "vertiefung": [{"bereich": "Portfolio Luftverteidigung", "ergebnis": "drei weitere Systeme ergänzt"}],
 "stichprobe": [{"gruppe": "Kapitel, Quelle, Aussageart", "auswahl": "IDs", "ergebnis": "…"}],
 "hinweise": ["…"]
}
```

`umfang.kapitel`: `"alle"` oder Liste aus unternehmen, personen, portfolio,
cluster, markt, fokus, interpretation.

| Urteil Fakt | Bedeutung |
|---|---|
| im_original_bestaetigt | Belegstelle im geöffneten Original gelesen |
| durch_suche_gestuetzt | Original nicht geöffnet, unabhängige gelesene Quelle stützt |
| abweichend | Quelle sagt etwas anderes, noch nicht korrigiert |
| nicht_belegt | weder Original noch unabhängige Quelle stützen |
| nicht_erreichbar | Quelle nicht abrufbar, keine Alternative |
| nicht_einzeln_geprueft | B-Claim außerhalb der Stichprobe |
| korrigiert | vom Prüf-Agenten nach geöffnetem Original korrigiert |
| neu_aus_vertiefung | vom Prüf-Agenten neu recherchiert |

| Urteil Ableitung | Bedeutung |
|---|---|
| gestuetzt | Basis trägt die Aussage |
| eingeschraenkt | trägt sie nur teilweise |
| nicht_gestuetzt | Basis fehlt oder trägt sie nicht |
| angepasst | vom Prüf-Agenten an korrigierte Fakten angepasst |

`aenderungen`, `ergebnis` und `auswertung` setzt das Skript, nie von Hand.
