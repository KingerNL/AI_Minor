# Wiskunde les 1 - Mart Veldkamp

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

$$\vec{x} = \left[\begin{array}{ccc}
                    1\\
                    3
                    \end{array}\right]
                    $$ 
Vectoren zijn punten met een gerichte lijnstuk naar een ander punt.

Deze Vectoren kunnen erg makkelijk opgeteld worden door middel van de desbetreffende rij keer de andere desbetreffende lijn te doen, 
bijvoorbeeld: (3/1) + (2/2) = (5/3)

Vermenigvuldigen is hetzelfde principe: 3 * (2/4) = (6/12)

# Weten wat een matrix is en matrices kunnen optellen en vermenigvuldigen.

$$\left[\begin{array}{ccc}
        1 & 2 \\
        3 & 3 \\
        5 & 6 \\
        \end{array}\right] \cdot 
    \left[\begin{array}{ccc}
        1 & 2 & 3\\
        4 & 5 & 6 \\
        \end{array}\right] =
    \left[
        \begin{array}{ccc}
        9 & 12 & 15 \\
        19 & 26 & 33\\
        29 & 40 & 51
        \end{array}
        \right]
        $$ 

Matrixen zijn niks anders dan een Vector met meer dimensies. Deze Matrixen kan je + elkaar door als ze dezelfde afmetingen hebben, als dit het geval is kan je ze elkaar optellen als hetzelfde principe als een vector, bijvoorbeeld: (1/2/3) + (4/2/6) = (5/4/9)

Zoals je op de afbeelding hierboven kan zien kan je vectoren ook vermenigvuldigen, dat doe je doormiddel om te kijken naar welk punt in de matrix je wilt oplossen en daarna kijkt naar welke rijen/kolommen je moet hebt hebben in gegeven matrixes.

# Toelichten wat een getransporteerde matrix, de inverse matrix, de determinant van een matrix is en de indentiteitsmatrix is en deze ook allemaal kunnen bepalen.

$$ A = \left[
\begin{array}{ccc}
1-2a^2 & -2ab & -2ac \\
-2ab & 1-2b^2 & -2bc\\
-2ac & -2bc & 1-2c^2
\end{array}
\right]
$$

Hier kan je een voorbeeld zien van een getransporteerde matrix, wat je hier kan zien is dat de matrix rij in een kolom verranderd en andersom.

Als je de inverse van een matrix genaamd (bijvoorbeeld) A de inverse gaat berekenen, betekend dat het volgende moet gelden:

$$A \cdot B = E \Rightarrow 
\left[
    \begin{array}{ccc}
        a_1 & a_2 \\
        a_3 & a_4 \\
    \end{array}
\right] \cdot
\left[
    \begin{array}{ccc}
        b_1 & b_2 \\
        b_3 & b_4 \\
    \end{array}
\right] = 
\left[
\begin{array}{ccc}
a_1b_1+a_2b_3 & a_1b_2+a_2b_4 \\
a_3b_1+a_4b_3 & a_3b_2 + a_4b_4 \\
\end{array}
\right] = 
\left[
    \begin{array}{ccc}
        1 & 0 \\
        0 & 1 \\
    \end{array}
\right]
$$

Hoe je daaruit de inverse matrix kan halen is door middel van de determinant van A de halen, en dit doe je door middel van (in dit geval) a1 * a4 - a2 * a3.

Dus samengevat:
$$
\left[
    \begin{array}{ccc}
        a & b \\
        c & d \\
    \end{array}
\right]^{-1}= \frac{1}{\det(A)} \cdot
\left[
    \begin{array}{ccc}
        d & -b \\
        -c & a \\
    \end{array} 
\right] \Leftrightarrow \det(A) = ad - bc
$$

Het mooie is dat als je de daadwerkelijke matrix keer de inverse matrix doet, je uitkomt op een indentiteitsmatrix, die weer wordt gebruikt in AI voor *classification*. Zo ziet een indentiteitsmatrix er uit:

$$eenheidsmatrix: E=(1) \lor
\left[
    \begin{array}{ccc}
        1 & 0 \\
        0 & 1 \\
    \end{array} 
\right] \lor
\left[
    \begin{array}{ccc}
        1 & 0&0 \\
        0 & 1&0 \\
        0 & 0&1 \\
    \end{array} 
\right]...$$
# Weten wat de euclidische- en manhatten afstand is en aantonen dat hoe je deze afstanden kan bepalen.

Hier zie je de Euclidische afstand berekent. Dit komt eigenlijk neer op de vergelijking van pythagoras.

$$d(x,y) = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$

Terwijl hier ziet dat bij de Manhatten afstand hij niet hemelsbreed naar het punt gaat, maar met de rasters mee beweegt.

$$d(x,y) = |x_2-x_1|+|y_2-y_1|$$

##### De afbeeldingen uit deze Notebook komen vanuit de volgende bronnen:

- https://www.hhofstede.nl/modules/inversematrix.htm
- https://nl.wikipedia.org/wiki/Getransponeerde_matrix
- http://www.wiskundemagie.be/tag/manhattan-metriek/