---
name: firmenbasis-person
description: Recherchiert für ein Firmenbriefing die Firmenbasis, die Entwicklungen der letzten vier Monate und, falls genannt, das berufliche Profil eines Gesprächspartners. Liefert nur Fakten mit Quellen als Teil für briefing-daten.json, keine Bewertung.
---

# Firmenbasis und Gesprächspartner

Vorher briefing-standards laden. Ergebnis ist ein Teil mit `quellen`, `claims`
(T… und H…), `inhalt.unternehmen`, `inhalt.personen` und `phasen`.

## 1 Unternehmen eindeutig zuordnen

- Offizielle Website, Rechtsform, Sitz, Konzernzugehörigkeit, Registereintrag.
- Gleichnamige Firmen ausschließen. Ist die Zuordnung nicht eindeutig, stoppe und
  frage nach; das ist die einzige blockierende Rückfrage.
- Unternehmensgrenze festlegen: identifizierte Gruppe und relevante öffentlich
  belegte Gesellschaften.

## 2 Profil

Zeilen für `inhalt.unternehmen.profil`, soweit belegt: Rechtsform und Sitz,
Eigentümer (Kurzform, Details im Cluster), Umsatz mit Jahr und Bezug
(Konzern oder Segment), Ergebnis falls relevant, Beschäftigte mit Stichtag,
Geschäftsfelder im Überblick, wichtige Standorte. Neuester veröffentlichter
Geschäftsbericht oder Abschluss vor dem Stichtag hat Vorrang. Keine Kennzahl
ohne Jahr und Bezugsobjekt.

## 3 Entwicklungen der letzten vier Monate

- Fenster: Stichtag minus vier Kalendermonate bis Stichtag, beide inklusive.
  Maßgeblich ist das Ereignisdatum, nicht das Abrufdatum.
- Suche gezielt: Newsroom, Investor Relations, Nachrichtenagenturen,
  Wirtschafts- und Fachmedien, lokale Medien an wichtigen Standorten, Behörden
  und Vergabeportale. Deutsch und Englisch, bei Auslandsbezug Landessprache.
- Je Ereignis: kurzer sachlicher Titel mit Einschränkung („angekündigt“,
  „laut Hersteller“, „laut Medien“), Datum, Status, Claim.
- Ältere, künftige oder undatierte Ereignisse nicht in die Timeline; ihre Fakten
  können in andere Kapitel.
- Keine Ereignisse gefunden: Lücke mit Suchumfang notieren.

## 4 Gesprächspartner (nur wenn im Auftrag genannt)

- Schreibweise, aktuelle Funktion und Unternehmenszugehörigkeit unabhängig
  prüfen. Die Nutzerangabe bleibt `position_laut_nutzer`. `verifizierung`:
  „bestätigt“, „abweichend: …“ oder „nicht verifiziert“.
- Belegter Werdegang chronologisch. Nachweisdatum ist nicht Eintrittsdatum;
  fehlt der Zeitraum, schreibe „Zeitraum nicht belegt“. Frühere Rollen nicht als
  aktuelle Verantwortung darstellen.
- Fachprofil und Verantwortung nur aus Belegen.
- Snapshot mit höchstens sechs sinnvollen Feldern, nichts auffüllen.
- Äußerungen und Medien der letzten vier Monate: eigene Interviews, Reden,
  Beiträge (`eigene`), offizielle Mitteilungen mit Zitat (`offiziell`), Artikel
  über die Person (`medien`). Gleiches Interview in mehreren Fassungen nur einmal.
  Bezahlschranke oder nur Auszug in der Unsicherheit nennen.
- Nur berufliche Informationen. Keine privaten Daten, keine regionalen oder
  persönlichen Bezüge herleiten.
- Mehrere Personen: je Person ein eigener Eintrag, keine vermischten Biografien.

## 5 Mindestumfang

- Profil mit mindestens vier belegten Zeilen, darunter Umsatz mit Jahr und Bezug.
- Mindestens zwei Nachrichten- oder Fachmedien (`typ: medien` oder `fachmedien`)
  für die Entwicklungen; Unternehmensmeldungen allein reichen nicht.
- Je Person mindestens zwei verschiedene Quellen, z. B. Unternehmensseite und
  Interview, Konferenzprogramm oder Registereintrag.
- Fehlt nach gezielter Suche etwas, Ausnahme mit Suchumfang statt Fülltext.

## 6 Teil schreiben

- Datei `teil-firmenbasis.json`, dann zusammenführen und validieren.
- `phasen`: `{"firmenbasis": "fertig", "person": "fertig"}`; ohne Person
  entfällt der Schlüssel `person`.
- Produkte, Beziehungen und Marktzahlen nicht hier anlegen; das machen die
  Skills portfolio, cluster und markt-wettbewerb.
