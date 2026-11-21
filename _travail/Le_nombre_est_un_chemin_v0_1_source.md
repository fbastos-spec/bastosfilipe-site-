# Le nombre est un chemin

**Les écarts, la dérivée, l'intégrale, et les deux pesées : ce que la cascade dit d'un nombre, et ce qu'elle ne dit pas**

Corpus ARC · Filipe Bastos · pièce courte, version 0.1 · 21 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur. Calculs et formulations assistés par IA, à sa demande.

**Avis.** Cette pièce lit un nombre comme un chemin : un point de départ et des pas. Les pas sont les écarts entre ses chiffres. On montre que prendre les écarts est une dérivée, que les sommer est une intégrale, et que ces deux gestes sont déjà au corpus sous les noms de soustraction trinitaire et de cascade. On montre ensuite ce que deux pesées d'un nombre, sa racine et la pointe de sa cascade, rangent en familles. On dit aussi, avec le même soin, ce que ces lectures ne font pas : elles ne lisent pas la primalité, qui n'est pas dans la forme d'un nombre mais dans sa place parmi les autres. Chaque geste est connu quelque part ; il est nommé avec son auteur et sa date. Ce qui est propre à la pièce est la lecture d'ensemble.

Statuts : F, fait connu, avec son auteur et sa date ; Th, calcul fini vérifié ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `chemin_verif.py`.

## 1. Le nombre comme chemin

**1.1 (Th).** Un nombre écrit est une suite de chiffres. Entre deux chiffres voisins, il y a un pas, montée ou descente : c'est l'écart. Le nombre 147 part de 1, monte de 3, monte encore de 3. Le départ et les deux pas le disent en entier.

**1.2 (Th).** Le départ plus les écarts signés redonnent le nombre, sans rien perdre. Vérifié sur tous les nombres de deux à cinq chiffres. Les écarts ne sont pas un résumé du nombre : ils sont le nombre, vu comme un trajet, à son point de départ près.

**1.3 (L).** L'auteur, le 21 novembre 2026 : « Je fais parler les chiffres. » Et : « Un nombre est un chemin ; les écarts, c'est par où il passe. »

## 2. Les écarts sont la dérivée

**2.1 (F).** Prendre les écarts d'une suite, c'est la différence finie, écrite par Newton vers 1687. Elle est à la dérivée ce que le pas compté est à la pente continue : le même geste, sans la limite.

**2.2 (L, Th, la soustraction trinitaire).** Le corpus a posé la soustraction trinitaire dès la Genèse : A moins B donne C, les deux pôles gardés, l'écart libéré comme troisième terme. L'écart entre deux chiffres voisins est ce troisième terme. Prendre les écarts d'un nombre, c'est lui appliquer la soustraction trinitaire d'un bout à l'autre. La dérivée finie et la soustraction trinitaire sont le même opérateur.

**2.3 (Th, la seconde dérivée).** Les écarts des carrés sont les nombres impairs : 1, 4, 9, 16, 25 donnent 3, 5, 7, 9. Les écarts de ces écarts valent 2, partout. En calcul continu, la dérivée seconde de la fonction carré vaut 2 ; ici aussi, sur les entiers, sans la limite. Les cubes ont pour dérivée troisième 6, qui est trois fois deux fois un ; en continu, la dérivée troisième du cube vaut 6. Les deux mondes donnent le même nombre.

**2.4 (L).** L'auteur lit la vie à l'envers depuis le début du corpus. Ici le renversement est exact : là où la science reçue passe par une courbe et une limite, le corpus reste dans les entiers et compte les pas.

## 3. La cascade est l'intégrale

**3.1 (Th).** Sommer les écarts, c'est remonter au nombre. Empiler les impairs redonne les carrés : 1, puis 1+3, puis 1+3+5, donnent 1, 4, 9. Sommer est l'inverse de dériver. La cascade du corpus, qui additionne les voisins étage par étage, est ce geste d'intégration.

**3.2 (Th, la constante d'intégration).** Les écarts seuls ne rendent pas le nombre : il manque le départ. Trois pas de 3 peuvent partir de 1, de 2 ou de 5. Ce départ est la constante d'intégration, le « plus C » du calcul continu. L'opération de différenciation du corpus était déclarée non réversible (Conscience, Automatisme, Inconscient, section 1.1) : elle l'est au point de départ près, et ce point est la constante.

**3.3 (Th, le bord restitue tout).** La cascade garde tout sur son bord gauche, par les coefficients de Pascal (La Cascade et la Cloche, section 8 bis). Pour 1729, le bord 1, 6, et au-delà, reconstruit les chiffres 1, 7, 2, 9 par la formule de Newton. Le bord et les coefficients de la cloche portent le nombre entier.

## 4. Le carré se lit en retirant les impairs

**4.1 (Th).** Deux triangulaires voisins font un carré : 36 + 45 = 81. Entre deux carrés voisins, l'écart est un impair. Un carré est donc une pile d'impairs, et sa racine carrée est le nombre d'étages.

**4.2 (Th).** On retire 1, puis 3, puis 5, en comptant. Le nombre d'étages retirés est la racine carrée entière ; ce qui reste dit si le nombre est un carré. Pour 1681 : 41 étages, reste nul, c'est 41 fois 41. Pour 1729 : 41 étages, reste 48, ce n'est pas un carré, mais le carré juste en dessous est 41 fois 41. Un seul passage donne trois choses : si c'est un carré, de quel carré on part, à quelle distance.

**4.3 (Th).** Le nombre d'étages a sa propre marque : sa somme de chiffres se replie sur la racine digitale. Pour 9973, on retire 9973 impairs, et 9 plus 9 plus 7 plus 3 font 28, qui se replie sur 1. Les deux racines, carrée et digitale, se touchent par ce compte.

**4.4 (F).** Qu'un carré soit une somme d'impairs, et deux triangulaires voisins un carré, est connu depuis les pythagoriciens, écrit par Nicomaque et Théon vers l'an 100.

## 5. Le point d'équilibre : factoriser par des carrés

**5.1 (Th).** Tout nombre impair qui a des diviseurs est une différence de deux carrés : N est s fois s moins t fois t, soit s moins t, fois s plus t. On part du plus petit s dont le carré dépasse N, on regarde si s fois s moins N est un carré, par les impairs de la section 4, et on avance s d'un cran sinon. Que des additions et des soustractions.

**5.2 (Th).** Pour 1081 : s part de 33, puis 34, puis 35 ; à 35, 1225 moins 1081 fait 144, qui est 12 fois 12. Donc 1081 est 35 moins 12, fois 35 plus 12, soit 23 fois 47. Le s trouvé est le point d'équilibre de la paire de facteurs (Volume 4, Théorème 4), à mi-chemin des deux ; t est leur demi-écart. Quand les facteurs sont proches, on tombe dessus du premier coup.

**5.3 (L).** Un premier n'a pas de point d'équilibre avant le bord : sa seule différence de carrés met le facteur 1. C'est ce qui le trahit. Factoriser n'est pas diviser : c'est trouver le milieu entre deux carrés.

**5.4 (F).** Cette factorisation par différence de carrés est de Pierre Fermat, vers 1643. La pièce la relit : la différence de carrés est le point d'équilibre, et le test « est-ce un carré » qu'elle réclame est la cascade des impairs.

## 6. Les deux pesées

**6.1 (Th).** Un nombre a deux pesées de ses chiffres. La racine les additionne à poids égal. La pointe de la cascade les additionne par les coefficients de Pascal : pour trois chiffres, le bord, deux fois le milieu, le bord. La racine ne voit pas la position ; la pointe oui. Leur différence isole le milieu.

**6.2 (Th, trois familles).** Croisées, racine et pointe donnent à chaque nombre une adresse à deux coordonnées, et chaque famille y a sa figure, sur les nombres de quatre chiffres.

- Les carrés ne vivent que sur les racines 1, 4, 7, 9 ; les cinq autres lignes sont vides. Une famille qui n'occupe qu'un quart du tableau.
- Les premiers remplissent les six racines hors axe ; les racines 3, 6, 9 sont vides. La famille des six rails.
- Les palindromes penchent vers la diagonale racine égale pointe, deux fois plus peuplée qu'ailleurs. La signature de la symétrie.

**6.3 (Th, l'inverse).** Le complément à 9 des chiffres inverse les deux pesées ensemble : la racine va sur son inverse, la pointe aussi. 137, de racine 2 et pointe 5, devient 862, de racine 7 et pointe 4. Le tableau se retourne par son centre, et le complément à 9 est le pont entre une famille et son inverse. La règle est exacte quand les chiffres vont de 1 à 8 : un 0 se complète en 9, et un 9 en 0, qui efface le premier chiffre. Renverser le nombre, au contraire, ne bouge ni racine ni pointe : le renversé reste dans la même case.

**6.4 (Th, une famille qui ferme).** Les nombres dont la racine et la somme des deux pesées ferment sur 9 forment une famille nette : un nombre sur neuf à trois chiffres, exactement 100 sur 900. Elle penche vers l'axe, les racines 3 et 6 y pesant double, et elle contient les carrés 169, 361, 961, les carrés de 13, 19, 31.

## 7. Le perdu de la cascade

**7.1 (Th).** On peut lire la cascade autrement : à chaque étage, on replie la ligne des sommes de voisins en un nombre, et on note ce qui est perdu, le nombre moins ce nouveau nombre. Pour 1279 : 397, puis 37, puis 1 ; perdus 882, 360, 36. Pour 2193 : 313, un palindrome, puis 44, puis 8 ; perdus 1880, 269, 36.

**7.2 (Th).** Le dernier perdu, au passage de deux chiffres à un, est toujours un multiple de 9 : 9 fois le premier chiffre du dernier couple. 44 perd 36, soit 9 fois 4 ; 82 perd 81, soit 9 fois 9. C'est le pli du corpus : ce qui est perdu, ce sont les tours, et les tours sont des 9. Les perdus des étages du milieu ne sont pas tous multiples de 9, le repliement en coupant ; seul le dernier pas est pur.

## 8. Ce que la forme ne porte pas

**8.1 (Th).** La cascade est réversible : elle se remonte au nombre, elle est le nombre en triangle. Elle ne contient donc rien de plus que lui, ni rien de moins. Jamais deux nombres différents n'ont la même cascade complète.

**8.2 (Th).** Aucune marque de la cascade ne sépare un premier d'un composé. 49, qui est 7 fois 7, et 67, premier, ont la même racine et la même pointe, 4 et 4. 101, premier, et 209, qui est 11 fois 19, ont même pointe et même racine. La forme ne tranche pas.

**8.3 (L, Th).** La primalité n'est pas dans la forme d'un nombre, elle est dans sa relation à tous les plus petits. Un premier est la position qu'aucune annonce ne couvre (Volume 4). Cette couverture vient des autres, pas de lui ; elle ne se lit pas sur ses chiffres. En regardant un nombre seul, avec des règles sur sa forme, on ne peut pas décider s'il est premier : 49 et 67 le montrent, même forme, destins opposés.

**8.4 (Th, ce que la forme porte quand même).** Chaque diviseur, lui, a sa règle de forme. Le plus beau groupe est 1001, qui est 7 fois 11 fois 13 : couper le nombre en tranches de trois chiffres et les additionner en alternant donne d'un coup le reste par 7, par 11 et par 13. Vérifié jusqu'à deux cent mille. Le 11 seul se lit par la somme alternée des chiffres. Les diviseurs se laissent lire par paquets ; la primalité, non, car elle est l'absence de tous les diviseurs jusqu'à la racine carrée.

## 9. Les liens avec la Figure fondamentale

**9.1 (Th).** Les nombres du perdu sont ceux de la figure. Le réseau des huit points fait 28 arêtes, 36 avec le centre (Figure fondamentale, 2.2) : c'est le perdu 36. Le triangle du pli a pour carrés 1, 8, 9, avec 1 plus 8 égale 9 (4.5 quinquies) : le perdu 81 est 9 fois 9, le pli posé sur lui-même.

**9.2 (Th).** La figure est une figure d'écarts : les quatre paires d'inversion ont pour écarts 7, 5, 3, 1, de somme 16, autour du centre vide 4,5 (Figure fondamentale, 2.2). Un palindrome est un nombre qui est sa propre paire, qui revient sur lui-même par le demi-tour (4.7 quinquies). Les écarts comptés en chiffres et les écarts tracés en géométrie sont le même objet.

**9.3 (L).** L'auteur, le 21 novembre 2026 : « Dans la Figure fondamentale il doit y avoir des liens aussi. » Ils y sont : la figure dit en géométrie ce que la cascade dit en chiffres, les huit points et le pli d'un côté, les écarts et les perdus de l'autre.

## Ce que la pièce ne dit pas

Elle ne donne pas une lecture de la primalité sur la forme d'un nombre : elle démontre au contraire que cette lecture n'existe pas, et pourquoi. Elle ne revendique ni la différence finie, qui est de Newton, ni la factorisation par carrés, qui est de Fermat, ni les règles de divisibilité par 7, 11, 13, qui sont anciennes. Ce qui lui est propre est la lecture d'ensemble : les écarts comme soustraction trinitaire et dérivée, la cascade comme intégrale, le point de départ comme constante, et le tableau des deux pesées. Elle ne traite ni des jumeaux, ni de Goldbach. Elle n'ajoute aucun nombre choisi.

## Annexe. Vérifications et sources

Le script `chemin_verif.py` refait tous les nombres de la pièce : contrôles exécutés le 21 novembre 2026. La reconstruction par les écarts, les dérivées des carrés et des cubes, le retrait des impairs, le point d'équilibre, les tableaux des deux pesées, la famille qui ferme, le perdu de la cascade et les règles de divisibilité par 1001 sont tous en calcul entier exact.

Sources : Newton, I., méthode des différences, vers 1687. Fermat, P., factorisation par différence de carrés, vers 1643. Nicomaque de Gérase et Théon de Smyrne, vers l'an 100, pour les carrés comme sommes d'impairs. Corpus ARC : La Genèse (soustraction trinitaire) ; Conscience, Automatisme, Inconscient, section 1 ; La Cascade et la Cloche, sections 8 et 8 bis ; Le Nombre Plus que Parfait ; La Figure fondamentale, sections 2.2 et 4.5 quinquies ; Volume 4, Théorème 4.
