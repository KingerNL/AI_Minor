# Wiskunde Les 4 - Mart Veldkamp

Mijn 4e wiskunde les was een inhaal les na de vakantie, dus deze zal niet heel veel informatie bevatten. Wat ik in dit document zal bespreken zijn de volgende dingen:
1. De twee kostenfuncties MSE (Mean Squarred Error) & Cross Entropy onderscheiden
2. Beschrijp wat beide functies doen en wanneer ze toegepast moeten worden
3. Kunnen uitleggen wat softmax is, en wanneer het toegepast kan worden.

Hoewel ik MSE (Mean Squarred Error) ook in mijn vorige Les al een klein beetje heb behandeld, zal ik hier wat meer ingaan in hoe het nou werkt, in plaats van de formules erachter. 

### MSE (Mean Squarred Error)

Laten we beginnen bij MSE, Wat deze kostenfunctie doet is kijkt naar een verschillende punten in een grafiek en kan zo bepalen wat de afwijking is ten opzichte van een functie, en kwadraateerd deze. Dit doet hij omdat je zo nog sneller grote uitwijking ziet, en drastischer kan aanpakken. Waar deze functie veel gebruikt wordt is tijdens het verbeteren van weights. Dit is nodig om zo een Neuraal netwerk optimaal te laten presteren. Om zo errors te verkleinen, dus een beter model te trainen. Een laatst belangrijk aspect is dat MSE eigenlijk uitsluitend wordt gebruikt bij Lineare regressie.


In MSE zit veel wiskundige formules, als je daar benieuwd naar bend kan je altijd kijken naar me vorige notebook waar ik wat dieper ben ingegaan om de wiskunde achter MSE.

### Cross entropy:
Bij Machine Learning / Deep Learning problemen worden kostenfuncties gebruikt om het model tijdens het trainen te optimaliseren. Het doel is bijna altijd om het verlies te verkleinen. Aangezien hoe lager het verlies, hoe beter het model. Cross entropy is een zeer belangrijke kostenfunctie. Het wordt gebruikt om classificatiemodellen te optimaliseren. In tegenstelling tot MSE, wat gebruikt wordt voor regressiemodellen. 

 
Zoals je hierboven kan zien kijkt het naar de kansen uit de S (Softmax) en zet het deze kansen om naar 1en en 0en. Dit wordt gedaan om een gewenste uitput te krijgen. Zodat de machine een conclusie kan trekken: plek 0 is 1 en de rest is 0. De afbeelding is een kat! (Bijvoorbeeld). 

### Softmax:

Wat de softmax functie is eigenlijk erg makkelijk, eerst leest het een input array (een lijst met 
getallen) uit. Daarna gebruik je de softmax functie om deze array om te zetten in kansen. Wat deze 
kansen meestal inhoudt is in geval van machine learning is 	**de kans dat een target correct 
geclassificeerd is**. Om hier een voorbeeld van te geven: stel je hebt een afbeelding waar je objecten 
in wil herkennen, in dit voorbeeld heb je een neuraal netwerk getraind om 5 objecten te herkennen, 
dit kan bijvoorbeeld de volgende targets zijn: stoel, lamp, kast, tafel, deur en waterflesje. Het idee is 
dat nadat je een foto met bijvoorbeeld alleen een lamp aan het model heb gegeven. Deze kan 
identificeren dat er een stoel in de foto staat. Na het bekijken van de foto zal de 2	e  target het meest 
omhoog schieten (lamp in dit geval). En kunnen we door middel van de Softmax functie bekijken hoe 
groot de kans is dat de machine zeker is dat het een lamp is. In ons geval is dit 0.9 oftewel 90%. 

### Conclusie

Zowel Cross entropy als MSE (Mean Squarred Error) zijn erg handige kostenfuncties die bijna niet te missen zijn binnen de regressie / classificatie modellen in machine learning. Wat je daadwerkelijk wil bereiken bij beide functies is het proberen om te error zo klein mogelijk te maken. In geval van MSE wil je de error zo klein mogelijk hebben, en met Cross entropy de verhouding tussen de targets zo groot mogelijk hebben.