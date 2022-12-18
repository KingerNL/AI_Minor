# Wiskunde les 1

1. Waarvoor lineaire algebra wordt gebruikt binnen de AI.
2. Weten wat een vector is, en vectoren kunnen optellen en vermenigvuldigen.
3. Weten wat een matrix is en matrices kunnen optellen en vermenigvuldigen.
4. Toelichten wat een getransporteerde matrix, de inverse matrix, de determinant van een matrix is en de indentiteitsmatrix is en deze ook allemaal kunnen bepalen.
5. Weten wat de euclidische- en manhatten afstand is en aantonen dat hoe je deze afstanden kan bepalen.

# Waarvoor lineaire algebra wordt gebruikt binnen de AI.
In verschillende machine learning-algoritmen zoals begeleid leren en niet-gesuperviseerd leren, om inputs te berekenen en de machines te trainen met de kenmerken en verwachte outputs.

Lineaire algebra wordt ook gebruikt voor verschillende andere algoritmen, waar berekeningen lineaire algebra vereisen……

Bij het implementeren van het lineaire regressie-, gradiëntafdalingsalgoritme en het implementeren van de kostenfunctie, speelt lineaire algebra een belangrijke rol.

Er zijn verschillende andere aspecten waar lineaire algebra wordt gebruikt. Zonder wiskundige concepten zijn kunstmatige intelligentie en machine learning niets.

# Weten wat een vector is, en vectoren kunnen optellen en vermenigvuldigen.

![image.png](attachment:image.png)

Vectoren zijn punten met een gerichte lijnstuk naar een ander punt.

Deze Vectoren kunnen erg makkelijk opgeteld worden door middel van de desbetreffende rij keer de andere desbetreffende lijn te doen, 
bijvoorbeeld: (3/1) + (2/2) = (5/3)

Vermenigvuldigen is hetzelfde principe: 3 * (2/4) = (6/12)

# Weten wat een matrix is en matrices kunnen optellen en vermenigvuldigen.

![image.png](attachment:image.png)

Matrixen zijn niks anders dan een Vector met meer dimensies. Deze Matrixen kan je + elkaar door als ze dezelfde afmetingen hebben, als dit het geval is kan je ze elkaar optellen als hetzelfde principe als een vector, bijvoorbeeld: (1/2/3) + (4/2/6) = (5/4/9)

Zoals je op de afbeelding hierboven kan zien kan je vectoren ook vermenigvuldigen, dat doe je doormiddel om te kijken naar welk punt in de matrix je wilt oplossen en daarna kijkt naar welke rijen/kolommen je moet hebt hebben in gegeven matrixes.

# Toelichten wat een getransporteerde matrix, de inverse matrix, de determinant van een matrix is en de indentiteitsmatrix is en deze ook allemaal kunnen bepalen.

![image.png](attachment:image.png)

Hier kan je een voorbeeld zien van een getransporteerde matrix, wat je hier kan zien is dat de matrix rij in een kolom verranderd en andersom.

Als je de inverse van een matrix genaamd (bijvoorbeeld) A de inverse gaat berekenen, betekend dat het volgende moet gelden:

![moi](https://www.hhofstede.nl/modules/inversematrix_bestanden/image004.gif)

Hoe je daaruit de inverse matrix kan halen is door middel van de determinant van A de halen, en dit doe je door middel van (in dit geval) a1 * a4 - a2 * a3.

Dus samengevat:

![](https://www.hhofstede.nl/modules/inversematrix_bestanden/image012.gif)

Het mooie is dat als je de daadwerkelijke matrix keer de inverse matrix doet, je uitkomt op een indentiteitsmatrix, die weer wordt gebruikt in AI voor *classification*. Zo ziet een indentiteitsmatrix er uit:
![](https://www.hhofstede.nl/modules/inversematrix_bestanden/image002.gif)

# Weten wat de euclidische- en manhatten afstand is en aantonen dat hoe je deze afstanden kan bepalen.

Hier zie je de Euclidische afstand berekent. Dit komt eigenlijk neer op de vergelijking van pythagoras.
![](http://www.wiskundemagie.be/wp-content/ql-cache/quicklatex.com-faa2b88465e298f292c920991fe81b18_l3.png)

Terwijl hier ziet dat bij de Manhatten afstand hij niet hemelsbreed naar het punt gaat, maar met de rasters mee beweegt.
![](http://www.wiskundemagie.be/wp-content/ql-cache/quicklatex.com-232c01ed40a4e290c69ecd7d621df601_l3.png)

Conclusie:

![image-2.png](attachment:image-2.png)

##### De afbeeldingen uit deze Notebook komen vanuit de volgende bronnen:

- https://www.hhofstede.nl/modules/inversematrix.htm
- https://nl.wikipedia.org/wiki/Getransponeerde_matrix
- http://www.wiskundemagie.be/tag/manhattan-metriek/