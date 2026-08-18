# Wijzigingen v1.2-draft ten opzichte van v1.1-draft

Deze versie bevat geen nieuwe objecttypen of relaties. De wijzigingen betreffen de
schrijfwijze van een aantal veldnamen, drie nieuwe enumeratiewaarden en de volgorde
waarin enumeratiewaarden worden gepubliceerd.

## Breaking changes

Aanleverende partijen moeten hun JSON-bestanden aanpassen: de onderstaande veldnamen
zijn hernoemd. Omdat het schema `additionalProperties: false` hanteert, wordt een
bestand met de oude namen afgekeurd.

| Oude naam (v1.1-draft) | Nieuwe naam (v1.2-draft) | Object |
| :--- | :--- | :--- |
| `aanleverende_organisatie` | `aanleverendeOrganisatie` | Levering |
| `contactpersoonen` | `contactpersonen` | AanleverendeOrganisatie |
| `startdatum_matchtingperiode` | `startdatumMatchtingperiode` | Vroegsignaalzaak |
| `einddatum_matchingperiode` | `einddatumMatchingperiode` | Vroegsignaalzaak |
| `datum_opgepakt` | `datumOpgepakt` | Vroegsignaalzaak |

Aanleiding:

* `contactpersoonen` was een fout. De naam werd automatisch afgeleid uit de relatie
  tussen AanleverendeOrganisatie en Contactpersoon, waarbij de generator de
  Nederlandse regel voor open lettergrepen (persoon → personen) niet toepaste.
* De overige velden zijn van `snake_case` naar `lowerCamelCase` gebracht, zodat alle
  samengestelde veldnamen in de uitwisselspecificatie dezelfde schrijfwijze volgen.

## Nieuwe enumeratiewaarden

**EnumContactsoort** — uitgebreid van 8 naar 10 waarden:

* `Onbekend`
* `Overige`

**EnumSignaalstatus** — uitgebreid van 6 naar 7 waarden:

* `Inwoner al bekend bij schuldhulpverlening`

Bestaande waarden zijn ongewijzigd, zowel qua schrijfwijze als qua definitie. Deze
uitbreiding is niet breaking: bestanden die alleen bestaande waarden gebruiken blijven
geldig.

## Volgorde van enumeratiewaarden

De waarden van **EnumSignaalpartner**, **EnumContactsoort**, **EnumEindresultaat** en
**EnumSignaalstatus** worden vanaf deze versie alfabetisch gepubliceerd, zowel in het
JSON-schema als in de detailspecificatie. Dit maakt de lijsten beter doorzoekbaar.

Let op: `Overige` en `Onbekend` staan hierdoor niet meer achteraan, maar op hun
alfabetische plek. De volgorde in het JSON-schema is niet normatief — een `enum` is een
verzameling toegestane waarden, geen gesorteerde lijst — dus dit heeft geen gevolgen
voor de validatie van aangeleverde bestanden.

**EnumDagdeel** en **geslacht** houden hun oorspronkelijke volgorde, omdat die volgorde
inhoudelijk betekenis heeft.

## Ongewijzigd

* Objecttypen, relaties en multipliciteiten.
* Alle definitieteksten van objecttypen, attributen en enumeratiewaarden.
* De identiteitsregel voor Client: óf `burgerservicenummer` (exact 9 tekens), óf
  `postcode` + `huisnummer`.
* `additionalProperties: false` op alle objecten.
* De verplichte velden per object.

## Bestanden in deze versie

| Bestand | Inhoud |
| :--- | :--- |
| `json_schema_Uitwisselmodel.json` | Het normatieve JSON-schema |
| `enkelvoudigVoorbeeld.json` | Voorbeeld met één levering en één vroegsignaal |
| `meervoudigVoorbeeld.json` | Voorbeeld met meerdere leveringen |
| `uitgebreidVoorbeeld.json` | Voorbeeld met alle velden gevuld |
| `DDAS-VS.yaml` | OpenAPI-specificatie vroegsignalering |
| `DDAS-SHV.yaml` | OpenAPI-specificatie schuldhulpverlening |

Alle drie de voorbeeldbestanden zijn bijgewerkt naar de nieuwe veldnamen en
gevalideerd tegen het schema van deze versie.
