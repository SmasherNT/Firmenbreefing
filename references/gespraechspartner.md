# Berufliches Gesprächspartnerprofil

Der bestehende company-context-Faktenagent liefert `profile` im context-facts.json.
Kein zusätzlicher Agent, keine HTML und keine strategische Personenbewertung.
Darstellung wie die freigegebene Profilvorlage: Name/Einleitung, Snapshot (bis zu
sechs Felder, drei Spalten), Werdegangstabelle, Fachprofil und Verantwortung
nebeneinander. Danach folgt die Medien-Timeline. Quellen und Evidenz stehen
ausschließlich im letzten Quellenreiter, erreichbar über Verweise auf der Profilseite.
Keinen Abschnitt „Regionaler Bezug“ darstellen.

## Datenvertrag

`profile.name` und `profile.claim_ids` bleiben Pflicht. Alle zugeordneten Fakten
sind berufliche H-Claims derselben Person. Kompakte Texte sind quellengedeckte
Paraphrasen; Einschränkungen wie „laut Fachmedium“, „angekündigt“ oder eine nur
historisch belegte Rolle bereits im sichtbaren Kurztext erhalten.

Neue Läufe liefern folgende Strukturen; leere Listen bei fehlender Evidenz:
- `intro`: optional `{text, claim_ids}` – kurze berufliche Einleitung.
- `snapshot`: maximal sechs `{label, value, claim_ids}`. Z. B. Rolle, Unternehmen,
  weitere belegte Verantwortung, Fachthema, prägende Erfahrung, internationaler Bezug.
  Nur sinnvolle belegte Felder; keine Felder künstlich auffüllen.
- `career`: `{period, organization, role, context, claim_ids}` pro Station in
  chronologischer Reihenfolge. context beschreibt den belegten Tätigkeitskontext,
  keine erfundene strategische Relevanz. Fehlendes Datum: „Zeitraum nicht belegt“.
  Nachweisdatum ausdrücklich vom Eintrittsdatum unterscheiden.
- `expertise`, `responsibilities`: jeweils `{label, text, claim_ids}`.
  Frühere Tätigkeiten nicht als aktuelle Verantwortung darstellen.
- `regional_context`: optional `{label, text, claim_ids}`. Nur den belegten
  persönlichen Bezug aus älteren Datenverträgen erhalten. Dieses Feld wird auf
  der Gesprächspartnerseite nicht als eigener Abschnitt dargestellt. Neue Läufe
  benötigen hierfür keine gesonderte Recherche.

Alle claim_ids müssen in profile.claim_ids stehen. Der Renderer verlangt aktuelle
A-Prüfungen; prepare-facts prüft Struktur und Verweise vor dem Basis-Review.
Auch name, Texte, Chronologie und Zuordnungen gehören zur semantischen Basisprüfung;
Änderungen am Profil entwerten den Paket-Fingerprint. Keine automatische Freigabe.
Nicht einsortierte H-Claims bleiben unter „Weitere belegte Profilangaben“ erreichbar.
Ältere Profile ohne neue Felder bleiben nutzbar, zeigen aber explizite Datenlücken.

## Darstellung und Quellen

Die lokale Komponente scripts/profile-html.py und profile.css erzeugt das Profil.
Nummerierte Belege springen zu direkten Originalquellen; vollständige Aussagen,
Unsicherheiten und Links ins gemeinsame Claimregister stehen im letzten Quellenreiter.
Der Profilteil enthält nur nummerierte Quellenverweise dorthin.
Nur Code und Layout wiederverwenden, nie Personendaten des vorigen Unternehmens.


## Aktuelle Äußerungen & Medienpräsenz der letzten vier Monate
Bei genannter Person zusätzlich im bestehenden context-Faktenauftrag recherchieren.
Das Viermonatsfenster endet am Auftragsstichtag, nicht an einem späteren Renderdatum.
Öffentliche Interviews, Reden/Stellungnahmen, offizielle Mitteilungen mit persönlichem
Zitat sowie relevante Artikel mit Namen der Person suchen; Gegenrecherche einschließen.
Keine privaten Inhalte. Alle verwendeten Quellen öffnen und lesen. Bezahlschranken
und verfügbare Auszüge ausdrücklich kennzeichnen; daraus keine Volltextthesen ableiten.
Gleiche Meldung, Übersetzung und Video desselben Interviews zu einem Eintrag bündeln.

`profile.media`: Liste von Einträgen mit folgenden Feldern:
- `id`: eindeutige interne ID; `published_date`: YYYY-MM-DD innerhalb des Fensters.
- `event_date`: optionales gesondertes Ereignisdatum, nicht nach Veröffentlichung.
- `category`: `own` (eigene Äußerung), `official` (offizielle Verlautbarung) oder
  `media` (Artikel über die Person). Medienkritik nicht als persönliche Aussage ausgeben.
- `format`, `title`, `preview`: kurze quellengedeckte Texte für die geschlossene Zeile.
- `claim_ids`: nichtleere Liste geprüfter beruflicher H-Claims aus profile.claim_ids.
  Deren Aussagen liefern die Zusammenfassung im Klickdetail. Vollständige Quellen,
  Abrufdaten, Ursprung und konkrete Belegstellen stehen im normalen Faktenvertrag.
- `access_note`: konkrete Zugriffslage und Aussagegrenze; Pläne als Erwartungen benennen.
- optional `quote`, `quote_source_id`, `quote_location`: kurzes exaktes belegtes Zitat.
  Quelle muss in den referenzierten Claims vorkommen. Urheberrechtliche Grenzen
  über alle Zitate und Paraphrasen derselben Quelle gemeinsam einhalten.

Alle Medienzuordnungen unterliegen demselben semantischen Basis-Review und dessen
Fingerprint; keine automatische Inhaltsfreigabe durch ein technisch gültiges Datum.
Auch Titel/Preview auf korrekte Zuschreibung prüfen. Fehlende öffentliche Treffer oder
Zugriffe in gaps/coverage dokumentieren; `media=[]` bleibt möglich und wird als
fehlende freigegebene Abdeckung angezeigt, nicht als Beweis fehlender Medienpräsenz.
Alte Profile ohne media bleiben technisch lesbar; neue Aufträge recherchieren den Block.

Darstellung: exakte Überschrift oben, kompakte chronologische Zeilen (neueste zuerst),
Datum links, drei farbige Kategorien samt Legende. Klick oder Tastatur öffnet
Zusammenfassung, optional Zitat, Kontext und Zugriffshinweis. Auf Seite 2 nur interne
Quellen-/Evidenzverweise; volle Belege im letzten Quellenreiter. Native details funktionieren auch
ohne JavaScript. Keine Personendaten vom vorigen Unternehmen übernehmen.


## Mehrere Gesprächspartner
Nennt der Auftrag mehrere Personen, ist `manifest.person` eine Liste (Text oder
`{name, role}` je Eintrag, Auftragsreihenfolge). Der context-Agent liefert dann
statt `profile` das Feld `profiles`: je belegter Person genau ein Profilobjekt mit
obiger Struktur, `name` exakt wie im Manifest. H-Claims gehören genau einem Profil;
`profile` und `profiles` schließen sich aus. Ohne öffentliche berufliche Evidenz
entfällt das Profilobjekt und die Lücke steht in gaps/coverage. Der Renderer zeigt
je angefragter Person eine eigene Seite („Gesprächspartner · Name“) mit getrennten
Quellenankern; nicht belegte Personen bleiben als „öffentlich nicht verifiziert“
sichtbar. Ein einzelner Gesprächspartner behält den bisherigen Pfad.
