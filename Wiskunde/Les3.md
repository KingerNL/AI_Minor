# Wiskunde Les 3 - Mart Veldkamp

Bij mijn 3e wiskunde les ga ik uitleggen hoe je van verschillende functies de partiele afgeleide kan bepalen. Dit ga ik ter ondersteuning doen met Latex/Katex. Latex/Katex is een manier om wiskundige formules op te schrijven. Ik heb er nog nooit mee gewerkt, alleen ik dacht dat het een leuke uitdaging zou zijn naast het maken van de opgaves.

Afgeleides bepalen is erge belangrijk bij activatie functies, een voorbeeld waar afgeleides nodig zijn is bijvoorbeeld bij backpropegation. Hier gaan we terug het neurale net in om zo de error te verkleinen. Maar om dit te kunnen doen moeten we de activatie functies van elk neuroon kunne afleiden. Om zo de helling te bepalen, en daarmee te bepalen hoe groot te error is, dus hoe erg we hem moeten aanpassen.

Vraag: Bepaal de $\frac{\delta Z}{\delta x}$ & $\frac{\delta Z}{\delta y}$ voor de volgende functies:

1. $Z(X, y) = x^4+x^3y^2+y^5+8$
2. $Z(X, y) = x^3 + x^2y^4 -2y^5$
3. $Z(X, y) = -3x^3y^2 +5$

De uitwerkingen:

1.  $\frac{\delta Z}{\delta x}$ & $\frac{\delta Z}{\delta y} = 6x^2 . y$
2. $\frac{\delta Z}{\delta x}$ & $\frac{\delta Z}{\delta y} =8x . y^3$
3. $\frac{\delta Z}{\delta x}$ & $\frac{\delta Z}{\delta y} = -18x^2 . y$ 

## Bepaal de partieel afgeleide van verschillende kosten functies:

### Een voorbeeld met de Mean-Squarred error functie
Een kleine uitleg over De volgende afbeeldingen: Ik had eerst alles gemaakt in LaTeX, alleen toen ik erachter kwam dat dit niet samen gaat met gitlab. Was ik erg teleurgesteld. Om extra werk te voorkomen had ik foto's gemaakt van de uitgeschreven formules en deze hierin gezet. Zodat je nog steeds alles kan lezen, alleen het is iets minder scherp. Mijn excuses, ik had er hard aan gewerkt dus wou het niet helemaal over doen. De site die ik heb gebruikt om deze LaTeX te schrijven kan je vinden tussen mijn bronnen.

dit is de functie: $J(\theta) = \frac{1}{m} \sum_{i=1}^{m}(h_{\theta}(x^i)-y^i)^2$

$h_{\theta}(x^i)$ is linear, dus: $h_{\theta}(x^i) = \theta_{0} + \theta_{1}x^i$

Partieel differentiëren geeft:

$\frac{\delta}{\delta \theta_0}h_{\theta}(x^i) = \frac{\delta}{\delta \theta_0}(\theta_{0} + \theta_{1}x^i) = 1$

$\frac{\delta}{\delta \theta_1}h_{\theta}(x^i) = 
\frac{\delta}{\delta \theta_1}(\theta_{0} + \theta_{1}x^i) = x^i$

Nu terug naar de formule, de gegeven antwoorden uit de partieel gedifierentieerde functies moeten nu ingevuld worden in de functie van de Mean squarred error. Maar eerst moet deze ook gedifferentiëerd worden:
$$J(\theta) = (h_{\theta}(x^i)-y^i)^2 \Rightarrow J'(\theta) = 2(h_{\theta}(x^i)-y^i)$$

Nu we dit weten, kunnen we beide gedifferentieëerde uitkomsten in een matrix stoppen:

$$
\left[
    \begin{array}{ccc}
        2(h_{\theta}(x^i)-y^i) \cdot 1 \\
        2(h_{\theta}(x^i)-y^i) \cdot x^i \\
    \end{array}
\right] = 
\left[
    \begin{array}{ccc}
        \frac{2}{m} \sum_{i=1}^{m}2(h_{\theta}(x^i)-y^i) \\
        \frac{2}{m} \sum_{i=1}^{m}2(h_{\theta}(x^i)-y^i) \cdot x^i\\
    \end{array}
\right]
$$

Mooi! Nu kunnen we de lijn verbeteren, daar komt wat 'random' werk bij kijken. Stel we hebben een erg makkelijke functie: $y = x$. Nou willen we kijken als we random getallen invullen. of we deze zo kunnen verbeteren dat ze dichter bij onze target komen. Stel we nemen $y=2x+1$. Dit zit relatief erg ver weg van onze simpele formule. Je kan de $2x$ en 1 ook zien als $\theta (1,2)$.

### Kleine recap
We hebben nu de volgende gegevens:
- De orginele formule, en de gedifferentiëerde functie daarvan.
- De formule van $h_{\theta}(x^i)$. (Dit is die lineare functie)
- Zowel de daadwerkelijke functie, als de 'gegokte' functie.

Hiermee kunnen we de Mean squarred error bereken tussen beide functie:

$$ \frac{1}{3} \sum_{i=1}^{3}(1+2x^i-y^i)^2 = \frac{1}{3}((1+2-1)^2 + (1+4-2)^2 + (1+6-3)^2)^2 = \frac{1}{3}(4+9+16) = \frac{29}{30}$$

Wat we hier hebben gedaan is eerst gekeken naar de functie: $(1+2x^i-y^i)^2$ en daarna verschillende punten die op de grafiek zouden moeten liggen ingevuld. In mijn geval waren dit de coördinaten:
1. $(1,1)$
2. $(2,2)$
3. $(3,3)$

Nou liggen deze punten natuurlijk niet op de grafiek van $y = 2x+1$. Om onze grafiek beter de daadwerkelijk grafiek te beschrijven, gaan we de error berekenen en deze kwadrateren. 

Nu gaan we de $\Delta J$ berekenen. Dit doen we door middel van de volgende functie: $\frac{d}{d \theta}J(0,2)$.

$$
\left[
    \begin{array}{ccc}
        \frac{2}{3} \sum_{i=1}^{3}(1+2x^i-y^i) \\
        \frac{2}{3} \sum_{i=1}^{3}(1+2x^i-y^i) \cdot x^i\\
    \end{array}
\right] , (1,1) + (2,2) + (3,3) \Rightarrow
\left[
    \begin{array}{ccc}
        6\\
        \frac{29}{30}\\
    \end{array}
\right]
$$

Top, nu hebben we de $\Delta J$. We kunnen hiermee de volgende formule invullen om onze waardes aan te passen, om zo de formule dichter te krijgen bij onze daadwerkelijke formule:
1. $\theta_{new}=\theta_{old}- \alpha \cdot \Delta J$
2. $\theta_{old}=$ de oude gegevens van $\theta$ dus: $\theta(1,2)$
3. $\alpha = $ de learning rate, in ons geval 0,1.
4. $\Delta J = $ de error, gekwadrateerd.

Dit geeft ons de volgende formule:

$$\theta_{new} = 
\left[
    \begin{array}{ccc}
        1\\
        2\\
    \end{array}
\right] - 0,1 \cdot
\left[
    \begin{array}{ccc}
        6\\
        \frac{29}{30}\\
    \end{array}
\right] =
\left[
    \begin{array}{ccc}
        0,4\\
        0,67\\
    \end{array}
\right]
$$

Dus de nieuwe waardes van $\theta$ zijn: $\theta$(0,4; 0,67).

## Bronnen:

Voor de activatie functies:
- [Lijst met functies](https://en.wikipedia.org/wiki/Activation_function)
- [Lijst met afgeleide](https://dlo.mijnhva.nl/d2l/le/content/354957/viewContent/851240/View)
- [Site LaTeX](https://www.mathcha.io/editor/NvKDesYwiOph19NB2nFVZKQ9Bs072QlrivwD35o)