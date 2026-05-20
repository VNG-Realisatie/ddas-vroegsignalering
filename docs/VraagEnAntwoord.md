# Vraag en Antwoord 

Hieronder vind je veelgestelde vragen met bijbehorende vragen over vroegsignalering in het kader van DDAS. 

??? question "Moet het aan CBS aan te leveren JSON-bestand worden versleuteld?"
    Nee, het aan CBS aan te leveren JSON-bestand hoeft niet te worden versleuteld. In een van de eerdere versie van de DPIA stond een zinsnede met de term '(versleuteld)' die tot verwarring leidde. Deze is in de DPIA aangepast. 

??? question "Wat moet worden opgegeven bij 'code gegevensleverancier'?"
    Dit is een code die het CBS nodig heeft om onderscheid te kunnen maken tussen de softwareleveranciers die de gegevens aanbieden. Ook wordt op basis van deze code bepaald welke versie van de software is gebruikt. De correcte vulling van dit veld is als volgt: 'naam softwareleverancier' + 'versienummer-software'.

??? question "Wat moet worden opgegeven bij 'geslachtsaanduiding' bij 'client'?"
    De geslachtsaanduiding hoort van het type 'geslacht' te zijn, en niet alleen een string. Dit staat nu niet goed in de uitwisselspecificatie. Bij geslachtsaanduiding moet dus een van de waarden uit 'geslacht' te staan: ['Man','Vrouw','Onbekend','Leeg']

??? question "Wat te doen als de gemeentecode onbekend is van de gemeente onder wiens verantwoordelijkheid schuldhulp wordt uitgevoerd."
    In uitzonderlijke gevallen is het mogelijk dat de gemeentecode onbekend is van de gemeente onder wiens verantwoordelijkheid schuldhulp wordt uitgevoerd. Bijvoorbeeld bij samenwerkingsorganisaties die deze gemeente niet administreren. 
    
    De verantwoordelijke gemeente is één van de belangrijke startpunten voor de statistiek die door CBS wordt opgesteld. Dus sporen aan dit wel in de systemen op te nemen. Wel zijn we erg blij met aan te leveren gegevens, en kunnen we die gebruiken voor diverse andere statistieken. In dergelijke gevallen kan bij de trajecten in het veld gemeentecode de waarde “Onbekend” worden opgenomen.

??? question "Waarom is het belangrijk dat contactpersonen bij aanleverende_organisatie contactpersonen goed wordt ingevuld?"
    Bij aanlevering van gegevens via API's worden de gegevens van contactpersonen gebruikt om het 'op-orde-rapport' naartoe te sturen. Hiermee kunnen organisaties controleren of er correcte gegevens aan CBS zijn aangeboden. Hiervoor gebruikt het CBS het emailadres.

??? question "Telefoonnummer hebben wij soms 2 telefoonnummers voor, hoe vul ik dit veld in?"
    Je kunt in het veld meerdere telefoonnummers kwijt. Graag gesplitst met een '/'

??? question "EnumSignaalstatus status "opgepakt" mist. Moeten wij deze invullen? Of gaan jullie ervan uit dat wanneer dit veld leeg is het signaal is opgepakt?"
    Als een signaal onderdeel is van een zaak, dan zien we het als opgepakt	

??? question "Wanneer geldt een dossier als 'opgepakt'? We hebben een aantal verschillende datums die we hiervoor kunnen hanteren, maar weten niet goed welke we hiervoor moeten gebruiken."
    Gebruik hiervoor het moment van aanmaken van het dossier.
