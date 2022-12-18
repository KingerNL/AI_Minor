# Wiskunde les 2 - Mart Veldkamp

1. Bewijzen dat je diverse activatiefuncties kan differentiëren.
2. Vertellen wat activatiefuncties zijn.
3. Vertellen waartoe afgeleide van functies dienen mbt AI.

# Bewijzen dat je diverse activatiefuncties kan differentiëren.

### De sommen die we hadden gekregen:

$$1. \; f(x) = 3x^3+2x^4+3x^{\frac{1}{2}} + 3x^4 + 3x + 2$$
$$2. \; f(x) = (-5x+3x^2) \cdot (5-2x)$$
$$3. \; f(x) = \frac{5x+3}{3+2x}$$
$$4. \; f(x) = (x^2+2)^4 $$
$$5. \; f(x) = 3e^{-x}$$

### De uitwerkingen

$$1. \; f'(x) = 21x^3+9x^2+ \frac{3}{2}x^{-\frac{1}{2}}+3$$
$$2. \; f'(x) = -6x^2+25$$
$$3. \; f'(x) = \frac{21}{9+12x+4x^2}$$
$$4. \; f'(x) = 4(x^2+4)^3 \cdot 2x$$
$$5. \; f'(x) = -3e^{-x}$$


# Vertellen wat activatiefuncties zijn.

activatiefuncties zijn functies die helpen bij omzetten van een Input naar een gewenste Output. Deze Input zijn meestal getallen die je wilt omzetten naar desbetreffende ouput. (bijvoorbeeld hoe dicht een getal bij 1 of 0 ligt)

# Vertellen waartoe afgeleide van functies dienen met betrekking tot AI.

Afgeleide functies (ook wel gedifferentieerde functies genoemd) zijn erg handig met betrekking tot AI bij bijvoorbeeld Gradient descent, dit is een techniek voor het oplossen van optimalisatieproblemen waar het minimum van een functie van continue parameters wordt gezocht. Dit betekend dat het minimum te vinden is door de afgeleide gelijk te stellen aan 0.

#### bronnen:
1. https://dlo.mijnhva.nl/d2l/le/content/354957/viewContent/851260/View
2. http://www.cs.uu.nl/docs/vakken/ias/HANDOUTS/07._(24)_NEURAL_NETWORKS_HANDOUTS.pdf
3. https://libstore.ugent.be/fulltxt/RUG01/001/312/561/RUG01-001312561_2010_0001_AC.pdf