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

 