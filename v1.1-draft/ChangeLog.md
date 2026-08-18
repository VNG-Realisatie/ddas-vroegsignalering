# Wijzigingen v1.1-draft ten opzichte van v1.0

Deze versie beperkt de persoonsgegevens die over de inwoner worden uitgewisseld tot het
minimum dat nodig is om te kunnen matchen, en maakt het JSON-schema strikt zodat
onbedoelde velden worden afgekeurd in plaats van stilzwijgend geaccepteerd.

## Breaking changes

### Client: minder persoonsgegevens

Vijf velden zijn vervallen. Deze gegevens mogen niet meer worden meegeleverd; het
schema wijst ze af.

| Vervallen veld (v1.0) |
| :--- |
| `Voorletters` |
| `Voorvoegsel` |
| `Achternaam` |
| `Straatnaam` |
| `Plaatsnaam` |

De resterende velden zijn hernoemd van `Hoofdletter` naar `kleine letter`:

| Oude naam (v1.0) | Nieuwe naam (v1.1-draft) |
| :--- | :--- |
| `Burgerservicenummer` | `burgerservicenummer` |
| `Geboortedatum` | `geboortedatum` |
| `Postcode` | `postcode` |
| `Huisnummer` | `huisnummer` |
| `Huisnummertoevoeging` | `huisnummertoevoeging` |

### Nieuw veld: geslachtsaanduiding

Client krijgt het optionele veld `geslachtsaanduiding`, met de nieuwe enumeratie
`geslacht`: `Man`, `Vrouw`, `Onbekend`, `Leeg`.

### Identiteitsregel voor Client

Een Client moet vanaf deze versie op precies één van twee manieren worden
geïdentificeerd:

* **mét BSN** — `burgerservicenummer` is aanwezig en telt exact 9 tekens. Er mogen dan
  geen andere identificerende velden worden meegestuurd; of
* **zonder BSN** — `burgerservicenummer` ontbreekt, en zowel `postcode` als
  `huisnummer` zijn verplicht.

In v1.0 waren alle velden los optioneel en kon een Client zonder bruikbare identificatie
worden aangeleverd.

### Gesloten objecten

Vanaf deze versie zijn álle objecten in het schema gesloten met
`additionalProperties: false`. In v1.0 gold dat alleen voor Uitwisselmodel, Levering en
Vroegsignaal; nieuw gesloten zijn Client, Signaalpartner, AanleverendeOrganisatie,
Contactpersoon, Vroegsignaalzaak en Contactpoging. Velden die niet in de specificatie
staan, leiden vanaf nu tot afkeuring van het hele bestand.

## Ongewijzigd

* Objecttypen, relaties en multipliciteiten.
* De enumeraties `EnumSignaalpartner`, `EnumContactsoort`, `EnumEindresultaat`,
  `EnumSignaalstatus` en `EnumDagdeel`, inclusief alle waarden en definities.
* Alle definitieteksten van objecttypen en attributen.
* `DDAS-SHV.yaml` is inhoudelijk identiek aan v1.0; in `DDAS-VS.yaml` is alleen de
  verwijzing naar het JSON-schema naar deze versie bijgewerkt.

## Ondersteunende wijzigingen in de tooling

Twee controles zijn aan het bouwproces toegevoegd, zodat de bovenstaande regels
afdwingbaar zijn:

* `tools/postprocess_json_schema.py` — zet de identiteitsregel voor Client in het
  schema en sluit alle objecten af.
* `tools/validate_json_examples.js` — valideert de voorbeeldbestanden tegen het
  gegenereerde schema, zodat specificatie en voorbeelden niet uit elkaar kunnen lopen.

## Bestanden in deze versie

| Bestand | Inhoud |
| :--- | :--- |
| `json_schema_Uitwisselmodel.json` | Het normatieve JSON-schema |
| `enkelvoudigVoorbeeld.json` | Voorbeeld met één levering en één vroegsignaal |
| `meervoudigVoorbeeld.json` | Voorbeeld met meerdere leveringen |
| `uitgebreidVoorbeeld.json` | Voorbeeld met alle velden gevuld |
| `DDAS-VS.yaml` | OpenAPI-specificatie vroegsignalering |
| `DDAS-SHV.yaml` | OpenAPI-specificatie schuldhulpverlening |
