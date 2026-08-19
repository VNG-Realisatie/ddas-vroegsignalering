# Wijzigingen v1.2-draft ten opzichte van v1.1-draft

Deze versie bevat geen nieuwe objecttypen of relaties. De wijzigingen betreffen de
schrijfwijze van een aantal veldnamen, één hernoemde en drie nieuwe enumeratiewaarden,
de volgorde waarin enumeratiewaarden worden gepubliceerd, en een redactionele correctie
van de definitieteksten.

## Breaking changes

### Hernoemde velden

Aanleverende partijen moeten hun JSON-bestanden aanpassen: de onderstaande veldnamen
zijn hernoemd. Omdat het schema `additionalProperties: false` hanteert, wordt een
bestand met de oude namen afgekeurd.

| Oude naam (v1.1-draft) | Nieuwe naam (v1.2-draft) | Object |
| :--- | :--- | :--- |
| `aanleverende_organisatie` | `aanleverendeOrganisatie` | Levering |
| `contactpersoonen` | `contactpersonen` | AanleverendeOrganisatie |
| `startdatum_matchtingperiode` | `startdatumMatchingperiode` | Vroegsignaalzaak |
| `einddatum_matchingperiode` | `einddatumMatchingperiode` | Vroegsignaalzaak |
| `datum_opgepakt` | `datumOpgepakt` | Vroegsignaalzaak |

Aanleiding:

* `contactpersoonen` was een fout. De naam werd automatisch afgeleid uit de relatie
  tussen AanleverendeOrganisatie en Contactpersoon, waarbij de generator de
  Nederlandse regel voor open lettergrepen (persoon → personen) niet toepaste.
* De overige velden zijn van `snake_case` naar `lowerCamelCase` gebracht, zodat alle
  samengestelde veldnamen in de uitwisselspecificatie dezelfde schrijfwijze volgen.
  In `startdatumMatchingperiode` is meteen de schrijffout `Matchting` hersteld, zodat
  het veld weer overeenkomt met `einddatumMatchingperiode`.

### Hernoemde enumeratiewaarde

In **EnumEindresultaat** is één waarde vervangen:

| Oude waarde (v1.1-draft) | Nieuwe waarde (v1.2-draft) |
| :--- | :--- |
| `Verwijzing zonder toestemming` | `Verwijzing zonder tussenkomst inwoner` |

De oude waarde is niet langer toegestaan. Een Vroegsignaalzaak met
`"resultaat": "Verwijzing zonder toestemming"` wordt afgekeurd.

## Nieuwe enumeratiewaarden

**EnumContactsoort** — uitgebreid van 8 naar 10 waarden:

* `Onbekend`
* `Overige`

**EnumEindresultaat** — uitgebreid van 15 naar 16 waarden:

* `Vervolghulp en/of verwijzing`

**EnumSignaalstatus** — uitgebreid van 6 naar 7 waarden:

* `Inwoner al bekend bij schuldhulpverlening`

Op de hierboven genoemde hernoeming na zijn alle bestaande waarden ongewijzigd, zowel
qua schrijfwijze als qua definitie. Deze uitbreidingen zijn niet breaking: bestanden die
alleen bestaande waarden gebruiken blijven geldig.

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

## Tekstuele correcties

De definitieteksten zijn nagelopen op spel- en grammaticafouten. Het gaat om ongeveer
twintig correcties verspreid over objecttypen, attributen en enumeratiewaarden, zoals
ontbrekende woorden, een dubbel opgenomen zinsdeel en een enkelvoud/meervoud-fout. Ze
zijn hier niet stuk voor stuk opgesomd, omdat geen enkele correctie de betekenis van een
definitie verandert.

Twee correcties zijn wel het vermelden waard:

* In de definitie van het eindresultaat `Niet opgepakt: andere reden` stond een zin die
  halverwege afbrak en met de volgende zin was versmolten. Het onafgemaakte zinsdeel is
  verwijderd; de rest van de tekst is ongewijzigd.
* De term *matchingsperiode* is overal vervangen door *matchingperiode*, zodat de tekst
  overeenkomt met de veldnamen `startdatumMatchingperiode` en `einddatumMatchingperiode`.

## Diacritische tekens in het JSON-schema

Accenttekens in definitieteksten kwamen in het JSON-schema terecht als HTML-entiteit:
`&#233;` in plaats van `é`, `&#235;` in plaats van `ë`. In de gepubliceerde
detailspecificatie werden ze wel correct weergegeven, in het schema niet. Dat is
opgelost — de omschrijvingen in het JSON-schema bevatten nu de tekens zelf.

Merkbaar in bijvoorbeeld de definitie van Vroegsignaalzaak ("de behandeling van één of
meerdere vroegsignalen") en van `bereikt` ("contact met de cliënt gemaakt").

Dit raakt uitsluitend de omschrijvingen. **Veldnamen en enumeratiewaarden bevatten geen
diacritische tekens** en zijn hier niet door geraakt; aangeleverde bestanden hoeven dus
niet te worden aangepast.

## Ongewijzigd

* Objecttypen, relaties en multipliciteiten.
* De betekenis van alle definities: de tekstcorrecties hierboven zijn redactioneel.
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
