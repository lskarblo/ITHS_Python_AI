# Det egna projektet del 1

## Föutsättningar för data

För ett intressant projekt skulle jag ev kunna få tillgång till avidentifierad data från vårt vårddatasystem.

Vi har i vår databas ca 3 630 099 st vårdkontakter för 474 776 st unika patienter.

Datamängden har ju vissa egenskaper. Den sträcker sig från uppgifter om personer med namn och adress till vilka läkemedel som har distribuerats till patienten vid något visst tillfälle. Här finns förstås också koder för diagnoser och åtgärder, uppgifter om operationer, laboratoriesvar, mätvärden, tider för olika händelser mm.

## Förslag på AI projekt 

Förslagen är tänkta att kunna ge förutsägelser beroende av registrerade parametrar för vilka vi idag har resultat (supervised learning). Datamängden reduceras ju betänkligt när man fokuserar på någon viss diagnos eller motsvarande, men kan fortfarande vara tillräcklig för att träna en modell. Det betyder dock förmodligen att korrelationen mellan kombinationer av indata och utfall behöver vara bättre (tydligare) än vid en riktigt stor datamängd. 

- Förutse diagnoskoder utgående från skriven text. Svårigheter att åstadkomma datasetet med fritext. Ger många kombinationer av utfall (typ 2-10 st koder i många olika kombinationer). Intressant projekt! Det är oklart för mig hur det skulle gå att lösa. Det kommer ju att vara vissa textsnuttar som kommer att peka mot en diagnos, medan hela texten pekar på flera diagnoser. Möjligen går det att göra någon slags koppling genom att varje diagnoskod har en klartext som i sin tur har sannolikt har en motsvarighet - om än inte ordagrann - i texten. Om man betraktar varje kombination av koder som en vektor så kan det hända att datamängden helt enkelt är för liten för att träna en modell eftersom variationerna är för många med bara drygt 470 000 patienter. Klassificeringsproblem.

- Förutse någon viss diagnos utgående från vissa mätvärden eller kodade data. Intressant att titta på ur flera aspekter ungefär om i t-shirtfallet, där vissa data (givet att man har en mall för kroppsmått på t-shirts mappat till storlek) mer exakt skulle kunna prediktera resultatet och där det är intressant att reducera ner mängden inparametrar för att kolla om modellen fortfarande har goda möjligheter till korrekt prediktion. Det skulle ex kunna innebära att man med färre labdata för diagnostik skulle kunna göra en förutsägelse om något visst medicinskt utfall. Klassificeringsproblem.

- Förutse vistelsetid utgående från vissa diagnoser, mätvärden, persondata, el dyl. Vet inte om det kan vara så intressant som en faktisk tillämpning men skulle ev kunna ge en förutsägelse om platsläget eller vårdtyngden på avdelningar eller hela sjukhuset. Detta liknar i o f s triage-projektet till viss del. Regressionsproblem.

- Förutsägelser för operationstid eller dylikt utgående från olika waypoints i operationsprocessen. Regressionsproblem.

- Förutsägelser om behov av eftervård efter olika typer av åtgärder beroende på patientdata och rimligt berörda mätvärden. Klassificeringsproblem.

## Lär känna dina data

### Är det komplett?

Oklart just nu eftersom det så mycket beror på vilket spår som väljs MEN om det är samma sak som nästa fråga dvs finns det null-värden så tror jag att datasetet kommer att vara tvunget att väljas ut så att det inte har några null-värden om det alls ska gå att använda.

### Har du null-värden?

Se ovan

### Har du extrema värden?

Det kommer säkert att existera ”outliers” även bland de värden som vi hittar i vårddataunderlaget. Gäller det tider eller läkemedel så är det väl inte så vanligt – som att en operation skulle ha tagit 1000 timmar - men det kommer att finnas i flera andra sammanhang som t ex att en patient har väldigt många diagnoser vid ett tillfälle eller att en vistelsetid på sjukhuset ibland kan bli ovanligt lång.

### Vilka datatyper har datat?

Datatyperna kommer att vara mätvärden av flyttalstyp, mätvärden i klasser/intervaller, binära data (typ rökare ja/nej). Snodde följande ur någonstans på nätet och tänker att i stort sett alla sorterna finns men kan i många fall enkelt kodas om:

- Dikotoma data (binära data, två kategorier)\
- Kategoridata utan ordningsstruktur (nominaldata)\
- Kategoridata med ordningsstruktur (ordinaldata)\
- Kvantitativa antalsdata (diskreta data)\
- Kvantitativa kontinuerliga data, indelade i icke-negativa,intervallbegränsade eller obegränsade (intervall-, kvotdata)

Om man bortser från projektet med att från skriven text föreslå diagnoskoder så är skriven text inte ett viktigt inslag i datamängden. Det flesta data som vi i normalfallet hanterar som skriven text är fasta fraser som lätt kan kodas om till heltal.

### Vilka fält i ditt data vill du använda dig av?

Det här beror - som sagt – på vilket spår som väljs och det är i dagsläget svårt för mig att avgöra vilken nivå som är tillräcklig, lämplig och rimlig för ett sådant här projekt

### Hur kan du konvertera alla fält du vill använda till ett numeriskt format?

Det mesta kommer att vara tämligen enkelt att representera numeriskt. Jag vet dock inte hur det fungerar för ev nominaldata. Där är ju den numeriska representationen bara ett löpnummer – en etikett – där ordningen inte spelar någon roll. Jag vet inte hur – eller om – det behöver hanteras särskilt i modellerna. Det är bara för ett ev NLP-case som det behöver göras i flera steg. 

Finns det fall där det inte skulle att gå att koda indata numeriskt?
