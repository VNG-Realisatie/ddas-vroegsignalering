## Objecttypen Model Vroegsignalering


### AanleverendeOrganisatie
> **Definitie AanleverendeOrganisatie:** 
>
> Geen Definitie

??? info "Kenmerken Model AanleverendeOrganisatie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | AanleverendeOrganisatie |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    

Attributen van objecttype AanleverendeOrganisatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| kvk-nummer | AN80 |  |



### Contactpersoon
> **Definitie Contactpersoon:** 
>
> Contactpersoon van een organisatie

??? info "Kenmerken Model Contactpersoon"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Contactpersoon |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    

Attributen van objecttype Contactpersoon

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| telefoonnummer | AN200 |  |
| email | email |  |
| functietitel | AN200 |  |



### Contactpoging
> **Definitie Contactpoging:** 
>
> Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).

??? info "Kenmerken Model Contactpoging"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Contactpoging |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    

Attributen van objecttype Contactpoging

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| soort | Enumeratie: "EnumContactsoort" |  |
| bereikt | boolean | Er is succesvol contact met de client gemaakt. |
| datum | Date |  |
| dagdeel | Enumeratie: "EnumDagdeel" | Ochtend, middag of avond |



### Signaalpartner
> **Definitie Signaalpartner:** 
>
> Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.<br>Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.

??? info "Kenmerken Model Signaalpartner"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Signaalpartner |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    

Attributen van objecttype Signaalpartner

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| type | Enumeratie: "EnumSignaalpartner" |  |



### Vroegsignaal
> **Definitie Vroegsignaal:** 
>
> Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.<br>De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs). Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.

??? info "Kenmerken Model Vroegsignaal"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vroegsignaal |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    

Attributen van objecttype Vroegsignaal

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| crisissignaal | boolean | Betreft het een crisis? |
| warmeOverdracht | boolean | Er is al contact met persoon. Betreft verzoek deze persoon op te pakken in het kader van vroegsignalering. |
| bedrag | bedrag |  |
| ontstaansdatum | Date |  |
| signaaldatum | Date | Datum waarop de signaalpartner het signaal heeft verstuurd. |
| status | Enumeratie: "EnumSignaalstatus" |  |



### Vroegsignaalzaak
> **Definitie Vroegsignaalzaak:** 
>
> Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van &#233;&#233;n of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.

??? info "Kenmerken Model Vroegsignaalzaak"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vroegsignaalzaak |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    

Attributen van objecttype Vroegsignaalzaak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| resultaat | Enumeratie: "EnumEindresultaat" |  |
| matchingsdatum | Date |  |
| startdatum_matchtingperiode | Date |  |
| datum_opgepakt | Date |  |
| einddatum_matchingperiode | Date |  |



### Client
> **Definitie Client:** 
>
> Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente.

??? info "Kenmerken Model Client"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Client |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | aashkpour |
    | version | 1.5 |
    

Attributen van objecttype Client

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| Burgerservicenummer | AN9 |  |
| Voorletters | AN20 |  |
| Voorvoegsel | AN200 |  |
| Achternaam | AN200 |  |
| Geboortedatum | Datum | De datum waarop de persoon is geboren. |
| Straatnaam | AN200 |  |
| Postcode | AN6 |  |
| Huisnummer | AN5 |  |
| Huisnummertoevoeging | AN4 |  |
| Plaatsnaam | AN200 |  |






## Enumeraties Model Vroegsignalering


### EnumContactsoort
Enumeratie met daarin de soorten onderscheiden contactsoorten bij een contactpoging.

Het enumeratie EnumContactsoort kent de volgende waarden:

* **Mail**: Contact via e-mail, vaak gebruikt voor laagdrempelige informatievoorziening of opvolging.
* **Brief**: Een fysieke brief, vaak met uitleg over de achterstand en het hulpaanbod, verzonden per post.
* **SMS/Whatsapp**: Een tekstbericht verstuurd via sms, WhatsApp of andere digitale berichtendienst.
* **Telefoon**: Telefonisch contact, waarbij direct met de inwoner wordt gesproken of een voicemail wordt ingesproken.
* **Huisbezoek**: Een persoonlijke contactpoging aan huis, al dan niet aangekondigd, om direct met de inwoner in gesprek te gaan.
* **Kaartje**: Een informatief of uitnodigend kaartje dat bij de inwoner thuis wordt achtergelaten, bijvoorbeeld bij een gemist huisbezoek.
* **Overige**: Een andere vorm van contact dan de hier benoemde, bijvoorbeeld via een bemiddelaar, buurthulp of digitaal platform.


De enumeratie EnumContactsoort heeft de volgende kenmerken:

??? info "Kenmerken Model EnumContactsoort"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumContactsoort |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    


### EnumDagdeel
Geen Definitie

Het enumeratie EnumDagdeel kent de volgende waarden:

* **Ochtend**: Tot 12:00 uur
* **Middag**: Tussen 12:00 en 18:00
* **Avond**: 18:00 uur of later


De enumeratie EnumDagdeel heeft de volgende kenmerken:

??? info "Kenmerken Model EnumDagdeel"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumDagdeel |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    


### EnumEindresultaat
Enumeratie met de soorten Eindresultaten van een Vroegsignaalzaak.

Het enumeratie EnumEindresultaat kent de volgende waarden:

* **Niet opgepakt: inwoner wil geen contact**: <Geen Definities>
* **Niet opgepakt: geen capaciteit**: <Geen Definities>
* **Niet opgepakt**: [overig]
* **Inwoner al bekend bij schuldhulpverlening**: <Geen Definities>
* **Geen contact (meer) kunnen krijgen**: <Geen Definities>
* **Inwoner wil geen hulp**: <Geen Definities>
* **Inwoner probeert het zelf op te lossen**: <Geen Definities>
* **Inwoner heeft betaald/betalingsregeling getroffen voor oppakken melding**: <Geen Definities>
* **Inwoner heeft zelf betaald/betalingsregeling getroffen na oppakken melding**: <Geen Definities>
* **(Budget)advies en/of quick fix**: <Geen Definities>
* **Verwijzing financieel**: [bijv. naar schuldhulpverlening, budgetcoach, bewindvoerder]
* **Voorzien van informatie**: <Geen Definities>
* **Niet opgepakt: BRP-uitsluiting**: <Geen Definities>
* **Verwijzing niet-financieel**: [bijv. naar maatschappelijk werk, verslavingszorg, gezinszorg]
* **Inwoner heeft al een ander lopend traject**: [bijv. bij externe netwerkpartner, bij ander onderdeel sociaal domein, is onder bewind]


De enumeratie EnumEindresultaat heeft de volgende kenmerken:

??? info "Kenmerken Model EnumEindresultaat"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumEindresultaat |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    


### EnumSignaalpartner
Enumeratie met de soorten te onderscheiden Signaalpartners.

Het enumeratie EnumSignaalpartner kent de volgende waarden:

* **Energie**: Inzake de energierekening (elektriciteit, gas en/of warmte) vanaf 30 dagen
* **Huur**: Inzake de huur vanaf 30 dagen.
* **Hypotheek**: <Geen Definities>
* **CAK Zorgverzekeringen**: Als de zorgverzekering meer dan 6 maanden niet is betaald, wordt deze door CAK overgenomen.
* **Zorg**: Inzake de zorgverzekeringspremie inclusief premie voor aanvullende verzekering, eigen risico en eigen bijdragen van 30 tot 100 dagen.
* **Water**: Inzake de drinkwaterrekening vanaf 30 dagen
* **DUO**: <Geen Definities>
* **Belastingdienst**: Mensen die na een aanmaning hun belasting niet hebben betaald of terugbetaald.
* **CAK Eigen bijdrage**: Achterstand bij het betalen van de Eigen bijdrage in het kader van WLZ, en WMO. <font color="#0e0e0e">De doelgroep voldoet aan deze drie voorwaarden:</font><br><font color="#0e0e0e">1.Inwoners van de Gemeenten die het incassotraject hebben doorlopen (schriftelijke herinnering, aanmaning, minnelijk deurwaarders traject en telefonische poging tot persoonlijk contact). Het betreft hier achterstanden op gebied van eigen bijdrage Wmo of Wlz, ge&#239;ncasseerd door het CAK. Het gaat hierbij specifiek om de groep die terugkeert van een minnelijk deurwaarderstraject.</font><br><font color="#0e0e0e">2.Er is nog geen sprake van een gerechtelijke dwangmaatregel. De vroegsignalering gaat vooraf aan de inzet van een gerechtelijke procedure (doorgaans wordt die ingezet bij vorderingen &gt; € 100,= achterstand).</font><br><font color="#0e0e0e">3.Het lukt CAK niet om contact te krijgen of een betaalafspraak te maken met de klant.</font>
* **Overige**: <Geen Definities>
* **Dienst Toeslagen**: Mensen die na een aanmaning te veel ontvangen toeslag niet hebben betaald of terugbetaald.


De enumeratie EnumSignaalpartner heeft de volgende kenmerken:

??? info "Kenmerken Model EnumSignaalpartner"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumSignaalpartner |
    | toelichting | <memo> |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    


### EnumSignaalstatus
Geen Definitie

Het enumeratie EnumSignaalstatus kent de volgende waarden:

* **Nog niet opgepakt**: <Geen Definities>
* **Onterecht signaal**: <Geen Definities>
* **Overleden**: <Geen Definities>
* **Woont niet in gemeente**: <Geen Definities>
* **Herhaalde melding**: <Geen Definities>
* **Niet opgepakt**: <Geen Definities>
* **Opgepakt**: <Geen Definities>
* **Woont op een ander adres binnen gemeente**: <Geen Definities>


De enumeratie EnumSignaalstatus heeft de volgende kenmerken:

??? info "Kenmerken Model EnumSignaalstatus"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumSignaalstatus |
    | toelichting | #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.0 |
    



