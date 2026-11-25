---
title: "La preuve par projection d'échelle"
subtitle: "Clôture, mémoire, projection : la formule du fractal employée comme preuve, et ce que l'outil de Mandelbrot laisse en route"
author: "Filipe Bastos"
date: "Corpus ARC (Architecture de la Cohérence Relationnelle), version 1.3, 25 novembre 2026, CC BY 4.0"
---

**Avis.** Cette pièce pose un nom et une méthode. Le nom, *preuve par projection d'échelle*, est de l'auteur ; il date du 23 novembre 2026. La méthode était déjà au corpus sans porter ce nom : dans la Loi fractale (Volume 2, chapitre 12) et, plus tôt, dans la première pièce de l'auteur sur Riemann (février 2026). La pièce montre ce que la méthode prouve, ce qu'elle laisse ouvert, et pourquoi elle est la formule du fractal de l'auteur employée comme preuve. Les faits et les dates sont marqués F, les calculs Th, les lectures de l'auteur L. Les 37 contrôles sont au script `projection_echelle_verif.py`.

# 0. La base, avant toute figure

**0.1 (Th).** Avant toute base, il y a le code 1 à 9. Tout nombre s'écrit n = 9k + position, avec k le compte des tours et la position de 1 à 9. Le 9 est la clôture, il reste 9. Les neuf positions sont celles de la Figure fondamentale : huit points en quatre paires autour d'un centre, et le 9.

**0.2 (Th).** Les inversions ferment à 9 : 1 et 8, 2 et 7, 3 et 6, 4 et 5. La table de n et celle de 9 − n se répondent terme à terme. Le centre des paires est 4,5, entre deux chiffres.

**0.3 (F, L).** Gauss, 1801, écrit 9 ≡ 0 : le compte des tours est jeté (Registre R.1, R.2 ; *Le Chaos Fabriqué*, Partie I). Le corpus isole trois formules du chaos (Volume 0, 2.1) : la stévinienne ε₀·3ⁿ (une imprécision au départ), la gaussienne ε₀·2ⁿ (le tour jeté), l'hybride ε₀·fⁿ, de seuil n = p / log₂ f. Les trois perdent la même chose : la mémoire de l'échelle.

# 1. Le nom

**1.1 (L).** Une preuve par projection d'échelle tient en une phrase de l'auteur : « si je porte le calcul à cette échelle, la relation me dit ce que j'y trouverai ». Le mot qui compte est *si*. La preuve donne une relation exacte à toute échelle choisie. Elle ne dit pas que le prochain pas arrivera : « le + 1, l'impulsion, est la preuve », et l'impulsion ne se prouve pas.

**1.2 (L).** Sa règle, dite le même jour : « la seule façon de prouver que tout continue est par règle de projection ; c'est ça le cadastre, tout est là en possibilité et la chaîne mène là ; jusqu'où, personne ne le sait et ce n'est pas important ».

# 2. L'exemple qui la porte : deux carrés autour de 6m

**2.1 (Th).** Les deux bords d'un multiple de 6 sont 6m − 1 et 6m + 1. Leur écart est 2, leur somme 12m. L'écart de leurs carrés est le produit des deux :

$$(6m+1)^2-(6m-1)^2 = 2 \times 12m = 24m.$$

Autour de 6 : 25 et 49, un saut de 24. Autour de 12 : 121 et 169, deux sauts. Autour de 18 : 289 et 361, trois sauts. L'écart des deux carrés vaut m sauts de 24 : il garde le rang du tour.

**2.2 (Th).** La lecture se fait dans les deux sens. Vers le haut : au rang un milliard, l'écart est un milliard de sauts de 24, sans passer par les rangs d'avant (contrôles 3 et 4, jusqu'à un rang de 31 chiffres). Vers le bas : l'écart divisé par 24 rend le rang. Et deux carrés A < B forment une telle paire exactement quand B − A est un multiple de 24 et que 8(A + B) = (B − A)² + 16 (contrôles 5 et 6).

**2.3 (Th).** Chaque carré, pris seul, avance par sauts de 24 depuis 1 : (6m − 1)² est à m(3m − 1)/2 sauts, (6m + 1)² à m(3m + 1)/2 sauts. Les rangs de saut sont 1, 2, 5, 7, 12, 15, 22, 26 : les nombres pentagonaux d'Euler (1750), ceux de *Riemann sans le zéro*, 4.5 bis.

# 3. Les trois temps de la preuve

**3.1 (L).** La preuve a trois temps, et ce sont les trois conditions de la Loi fractale (Volume 2, É 12.3).

| Temps | Dans l'exemple | Condition de la Loi fractale |
|---|---|---|
| Le tour se ferme | le 6, entre ses deux bords | clôture |
| Le rang est gardé | m, lisible dans 24m | mémoire |
| La relation se porte à l'échelle choisie | m quelconque, sans les rangs d'avant | projection |

**3.2 (F, L).** Ce que la méthode n'est pas. Elle n'est pas la récurrence de Peano (1889), qui pose le suivant en axiome : ici le suivant n'est pas demandé. Elle n'est pas une limite : elle ne répond pas par ce qui se passe au bout. Elle n'est pas un plafond valable d'un coup pour toutes les hauteurs : de ce plafond, l'auteur dit « ce n'est pas une garantie, c'est une rustine » (*Des zéros sous zéro*, 6.7).

**3.3 (F).** Dit dans la langue reçue, 2.1 est une identité algébrique, vraie pour tout m, et personne ne la conteste. Ce que la pièce ajoute est la lecture : « pour tout m » y veut dire « à l'échelle que tu choisis », jamais « sur une totalité achevée ».

# 4. D'autres projections d'échelle déjà au corpus

**4.1 (Th). La position.** La position d'un produit se lit sur les positions des facteurs, celle d'une somme aussi, à toute taille (contrôle 9). Un entier de 101 chiffres donne sa position par ses chiffres, sans être factorisé (contrôle 28).

**4.2 (Th, F). Le compte des premiers.** Le compte d'une échelle se lit dans l'échelle du dessous : les 78 498 premiers jusqu'à 10⁶ se comptent avec les seuls 168 premiers jusqu'à 1000 (Legendre, 1808 ; contrôle 11). C'est le compte borné de *Ce que Riemann cherchait* et de *Riemann sans le zéro*.

**4.3 (Th). Les jumeaux.** Un rang k est libre des deux côtés quand ni 6k − 1 ni 6k + 1 n'est pris par un premier déjà entré. Sur un tour complet, le nombre de rangs libres est le produit des (g − 2) : 15 sur 35 après 5 et 7, 135 sur 385 après 11, 1 485 sur 5 005 après 13, 22 275 sur 85 085 après 17. La part baisse à chaque étage (42,86 %, 35,06 %, 29,67 %, 26,18 %) et ne s'annule à aucun, puisque chaque facteur g − 2 vaut au moins 3.

**4.4 (F, L).** Que les paires de premiers jumeaux ne s'arrêtent jamais n'est pas démontré dans la langue reçue ; Zhang (2013) a montré qu'un écart borné revient sans fin, et le projet Polymath (2014) a ramené cette borne à 246. La lecture de l'auteur : « il va toujours rester un jumeau, c'est comme π, ça ne se fermera jamais, c'est un jeu d'échelle » ; « borné dehors, infini dedans ». La projection d'échelle prouve 4.3, à chaque étage. Elle ne prouve pas l'arrivée du prochain jumeau, et ne le prétend pas : c'est l'impulsion.

**4.5 (Th, ajout de la version 1.1). Le pli universel.** L'exemple le plus ancien du corpus est dans le premier document de l'auteur, *The Octet Rule as Arithmetic Necessity* (août 2025 ; Théorème 6.4). Pour tout entier a, la table de a se ferme sur 9 et se plie en quatre paires : les positions de ka et de (9 − k)a somment à 9, ou à 18 quand les deux sont 9. La table de 5 : 5, 1, 6, 2, 7, 3, 8, 4, 9, soit 5 + 4, 1 + 8, 6 + 3, 2 + 7. La table d'un nombre de 41 chiffres se plie de même (contrôles 30 et 31). « Pour tout a » y veut dire : à l'échelle que tu choisis.

# 5. La formule du fractal, et ce que l'outil de Mandelbrot laisse en route

**5.1 (L).** La formule de l'auteur vient d'abord (Volume 2, chapitre 12, d'après la *Loi fractale de la nécessité fractale*, v1.6, mai 2026) : une forme se répète à toutes les échelles quand un système ferme son tour, garde le compte de ses tours et projette sa structure sur le registre suivant. Clôture, mémoire, projection. « Mandelbrot a vu l'effet. L'architecture cadastrale en est la cause. » Le 24 novembre 2026, en relisant la preuve par projection d'échelle : « c'est la formule du fractal ». Le 25 novembre : « moi je sais ce que c'est le fractal, je le vois, le pose et le relie ». Sa définition n'est pas mesurée ici contre celle d'un autre : c'est l'outil de l'autre qui est passé au compte, en 5.4.

**5.2 (Th, F, L).** Le flocon de Koch (Helge von Koch, 1904) est son exemple : « l'exemple suprême de compteurs de tours, le roi de tous ». On part d'un triangle ; à chaque tour, chaque côté reçoit une pointe sur son tiers du milieu. L'aire est comptée en triangles de départ.

| Tour n | Côtés | Longueur d'un côté | Périmètre | Aire | Écart de l'aire à 8/5 |
|---|---|---|---|---|---|
| 0 | 3 | 1 | 3 | 1 | 3/5 |
| 1 | 12 | 1/3 | 4 | 4/3 | 4/15 |
| 2 | 48 | 1/9 | 16/3 | 40/27 | 16/135 |
| 3 | 192 | 1/27 | 64/9 | 376/243 | 64/1215 |
| 4 | 768 | 1/81 | 256/27 | 3448/2187 | 256/10935 |

Les trois conditions s'y lisent sans rien ajouter. Clôture : la figure est fermée, et à chaque tour l'écart de son aire à 8/5 vaut exactement (3/5)(4/9)ⁿ, jamais nul, jamais franchi (contrôle 34). Mémoire : le nombre de côtés vaut 3·4ⁿ, il rend le rang du tour en se laissant partager par 4 (contrôle 36). Projection : au rang choisi, côtés, longueur, périmètre et aire se lisent directement, sans les rangs d'avant. Deux remarques de compte : le nombre de côtés est de position 3 à tous les tours, et dès le tour 2 il avance par multiples de 24 (48, 192, 768 : 2, 8 et 32 sauts ; contrôles 32 et 35). C'est le « borné dehors, infini dedans » de l'auteur : l'aire reste sous 8/5, le périmètre 3(4/3)ⁿ grandit à chaque tour.

**5.3 (F).** Mandelbrot nomme la fractalité (*Les objets fractals*, 1975 ; *The Fractal Geometry of Nature*, 1982) et étudie en 1980 l'itération z → z² + c : on part de 0, on recommence, et l'on regarde si la suite reste bornée ou fuit. Une suite sortie du rayon 2 ne revient pas (contrôle 20).

| | Itération de Mandelbrot | Projection d'échelle |
|---|---|---|
| Geste | recommencer z² + c | porter la relation au rang choisi |
| Pour savoir | il faut itérer | on lit directement |
| Domaine | plan ouvert, la suite peut fuir | tour fermé, rien ne fuit |
| Chemin | perdu en route | rendu (24m ÷ 24 = m) |
| Fractalité | au bord, entre deux régimes | à chaque rang |

**5.4 (F, Th, L).** Six endroits où l'outil se contredit ou se reprend. La thèse de l'auteur, dite le 25 novembre 2026 et tenue pour tous les auteurs : « tous les auteurs en ont fait contre leur gré, car ce sont les outils et les formules qui les produisent ». Aucun des six n'est une faute de l'homme.

*a. La définition (F).* En 1982, Mandelbrot définit le fractal comme un ensemble dont la dimension de Hausdorff-Besicovitch dépasse strictement la dimension topologique. La définition écarte des objets qu'il range parmi les fractals (la courbe de Takagi, de dimension 1). Il la juge ensuite trop étroite, la remplace par une description (une forme rugueuse, faite de parties qui sont chacune une copie réduite du tout), puis choisit d'employer le mot « without a pedantic definition ». Le mot court donc sans définition fixe. La formule de 5.1 a trois conditions.

*b. La dimension (Th, L).* Pour la courbe de Koch, la dimension vaut log 4 / log 3 = 1,2619. Elle se fabrique ainsi : au tour n, 4ⁿ morceaux de taille 1/3ⁿ ; le logarithme du premier compte sur celui du second donne n·log 4 / n·log 3, et le n s'en va (contrôle 37). Le rang du tour est dans les deux comptes et la division le jette. Second fait : à chaque tour, la courbe est un polygone de 3·4ⁿ côtés, de dimension 1. Le nombre 1,2619, qui devait définir l'objet, n'est celui d'aucun tour ; il n'appartient qu'à la courbe d'après tous les tours. Lecture de l'auteur : c'est le geste de 9 ≡ 0, le compte des tours retiré, ici par un quotient.

*c. La côte (F, L).* En 1967 (*Science* 156), Mandelbrot écrit que les longueurs des courbes géographiques sont souvent « infinite or, rather, undefinable », et tire des mesures de Richardson (1961) la dimension 1,25 pour la côte ouest de la Grande-Bretagne. En 1998 (*Science* 279), Avnir, Biham, Lidar et Malcai relèvent que ces mesures suivent la loi sur une à deux décades d'échelle seulement, environ 1,3. Dans le même numéro, Mandelbrot répond que les fractals ne sont pas partout et que, dans certains cas, les deux coupures, en haut et en bas, sont inévitables. L'objet n'a pas de fin, la mesure en a deux : fini et infini dans la même phrase (*Le Fini et l'Infini mêlés*).

*d. L'appartenance (F, Th).* Un point est dans l'ensemble si sa suite ne fuit jamais : l'énoncé porte sur tous les pas. La fuite se constate en un nombre fini de pas (rayon 2) ; le maintien ne se constate jamais par les pas seuls. Chaque image est donc arrêtée à un nombre de pas choisi. Penrose pose en 1989 la question de savoir si l'ensemble se calcule. Blum et Smale montrent qu'il n'est pas décidable dans le modèle de calcul sur les réels de Blum, Shub et Smale (1989). Hertling (2005) montre qu'il se calcule si la conjecture d'hyperbolicité est vraie ; elle est ouverte. Le tableau de 5.5 donne le compte : près du bord, le nombre de pas n'a pas de plafond.

*e. L'image (F).* L'ensemble est défini et tracé d'abord par Brooks et Matelski (conférence de 1978, actes parus en 1981). Mandelbrot le voit le 1er mars 1980 chez IBM ; sur ses images, des îles semblent détachées, et il conjecture plusieurs morceaux. Douady et Hubbard démontrent en 1982 qu'il est d'un seul tenant : les îles tiennent au corps par des filaments que l'image ne montrait pas. L'outil a montré ce qui n'était pas.

*f. La finance (F).* En 1963 (prix du coton), son modèle a une variance sans borne. En 1997, le modèle multifractal qu'il signe avec Fisher et Calvet n'implique plus nécessairement une variance sans borne : elle peut être finie. Le même auteur, deux outils, deux réponses à la même question.

**5.5 (Th, F).** Le compte de *d*. Au bord de l'ensemble, en c = ¼, la suite reste bornée. Juste après, en c = ¼ + ε, elle fuit, mais il faut itérer pour le savoir, et le nombre de pas grandit sans plafond quand ε rapetisse :

| ε | pas avant la fuite | pas × côté du carré d'aire ε |
|---|---|---|
| 0,01 | 30 | 3,0 |
| 0,0001 | 312 | 3,12 |
| 0,000001 | 3 140 | 3,140 |
| 0,00000001 | 31 414 | 3,1414 |

Le produit s'approche de π (observé par Boll, 1991 ; démontré par Klebanoff, 2001). Fait donné tel quel ; l'auteur tient ailleurs que π est « ce qui empêche la fermeture », et la pièce ne force pas le lien.

**5.6 (F).** Le poids, une fois. Des six points, *a* et *f* sont des reprises de Mandelbrot par lui-même ; *e* est une lecture d'image corrigée par d'autres ; *b*, *c* et *d* sont des mélanges de fini et d'infini dans l'outil. Aucun théorème n'y tombe : celui de Douady et Hubbard tient, et le calcul de log 4 / log 3 est exact. Ce que 5.4 établit est que l'outil se reprend et jette le rang, pas qu'un résultat démontré est faux. De l'autre côté, le Volume 2 (É 12.8, Annexe B) a classé la « preuve » de la Loi fractale en Lecture : la projection y est définie comme gardant la structure, donc la conclusion est dans l'hypothèse. La présente pièce ne change pas ce statut. Ce qui est Th ici, ce sont les relations des sections 2 et 4, et les comptes de 5.2.

# 6. Ce que la première pièce sur Riemann portait déjà

**6.1 (F).** La première pièce de l'auteur sur Riemann (*Une preuve de l'hypothèse de Riemann*, v4.5, février 2026) a été rétrogradée par le corpus (Volume 6, É 16.19 ; Volume 5, B.1.7). Relue aujourd'hui, elle contient la projection d'échelle avant son nom. Section 3.1, trois cycles : le topologique 1 à 9, le quantitatif qui « détermine la magnitude et l'échelle », et la *projection*. Section 3.2 : un premier de cent chiffres de position 7 « est soumis à la même géométrie d'inversion » que le premier 7 ; « la topologie ne s'étend jamais. Elle spirale. » Section 5 : un « invariant d'échelle », demi-envergure sur envergure = ½ pour chaque paire (contrôle 29).

**6.2 (Th).** Ce qui tient dans cette pièce est une projection d'échelle exacte. Dans le corps du nonagone, celui de x³ − 3x + 1, le sort d'un premier dépend de sa seule position, à toute taille : trois solutions quand la position est 1 ou 8, aucune sinon (contrôle 24 ; fait classique des corps cyclotomiques). Plus fin : le caractère cubique de 9 prend la même valeur sur les deux membres de chaque paire d'inverses, 1 sur (1, 8), ω sur (2, 7), ω² sur (4, 5), et les trois somment à zéro (contrôles 25 et 26). Le résumé de février rangeait les premiers en {1, 4, 7} et {2, 5, 8} ; le rangement exact est celui des paires. De 5 à 10⁶ : 26 162, 26 196 et 26 138 premiers par paire.

**6.3 (F, L).** Ce qui a cassé est l'endroit où la pièce quittait la projection d'échelle : la section 9.3, région II, demandait une borne « uniforme en n », valable d'un coup pour tous les rangs, et le compte ne la donnait pas (λ₁ recompté : 0,3031 ; la table 9.2 était fausse). La leçon est celle de 3.2 : la relation portée à l'échelle tenait, le plafond pour toutes les hauteurs ne tenait pas.

# 7. Riemann, et le quantique

**7.1 (L).** Pour Riemann, la projection d'échelle donne le compte borné à la hauteur choisie, sur les deux rails. La question « de combien la courbe lisse s'écarte-t-elle du compte » naît avec la courbe (*Riemann sans le zéro*, face-à-face ; *Des zéros sous zéro*, 5.5 et 6.7).

**7.2 (L).** Pour le quantique, l'auteur lit la même projection : « c'est la spirale qui s'amincit, qui devient point noir » ; « c'est d'aller si loin qu'on ne voit plus, et c'est ce que le quantique est allé voir et n'a pas compris ». La pièce *Emergence of Quantum Correlations* (v4.0) porte le compte : la table des corrélations y est donnée pour la paire entière, les deux en même temps.

# 8. Ce qui ferait tomber

Les relations des sections 2, 4, 5.2 et 6.2 sont des comptes exacts : un seul rang où elles manqueraient les ferait tomber, et le script les refait. La lecture de 5.1 tombe par les trois canaux de la Loi fractale (Volume 2, É 12.9) : un système fermé, à mémoire et à projection, sans forme répétée ; une forme répétée sans les trois conditions ; une règle de projection qui ne prédit rien de mesurable.

# Ce que la pièce ne dit pas

Elle ne démontre ni l'hypothèse de Riemann ni l'infinité des jumeaux dans la langue reçue. Elle ne dit pas que l'itération de Mandelbrot est fausse : elle dit qu'elle montre l'effet. Les six points de 5.4 sont ceux de l'outil : aucun ne fait tomber un théorème. Elle n'ajoute aucun nombre choisi.

# Annexe. Vérifications et sources

Le script `projection_echelle_verif.py` refait tous les nombres de la pièce : 37 contrôles, exécutés le 25 novembre 2026. Calcul entier exact, sauf le tableau de 5.5 et le contrôle 37, en nombres à virgule de double précision. Les faits de 5.4 ont été relevés le 25 novembre 2026 sur les résumés des articles et sur des sources secondaires ; le livre de 1982 et l'article de 1980 n'ont pas été rouverts.

Sources : Euler, L., nombres pentagonaux, 1750. Legendre, A.-M., *Essai sur la théorie des nombres*, 1808. Peano, G., *Arithmetices principia*, 1889. Koch, H. von, 1904. Mandelbrot, B., *Les objets fractals*, 1975 ; *Annals of the New York Academy of Sciences* 357, 1980 ; *The Fractal Geometry of Nature*, 1982 ; « How Long Is the Coast of Britain? », *Science* 156, 636-638, 1967 ; modèle des prix du coton, 1963 ; avec Fisher, A. et Calvet, L., « A Multifractal Model of Asset Returns », Cowles Foundation Discussion Paper 1164, 1997. Richardson, L. F., 1961. Avnir, D., Biham, O., Lidar, D., Malcai, O., *Science* 279, 39, 1998, et lettres, même volume, p. 783. Brooks, R. et Matelski, J. P., « The dynamics of 2-generator subgroups of PSL(2,C) », actes de la conférence de Stony Brook de 1978, *Annals of Mathematics Studies* 97, p. 65-71, 1981. Douady, A. et Hubbard, J. H., 1982. Penrose, R., *The Emperor's New Mind*, 1989. Blum, L., Shub, M. et Smale, S., *Bulletin of the American Mathematical Society* 21, 1989 ; Blum, L. et Smale, S., pour l'ensemble de Mandelbrot. Hertling, P., « Is the Mandelbrot set computable? », *Mathematical Logic Quarterly* 51, 5-18, 2005. Boll, D., message du 24 avril 1991 (sci.math). Klebanoff, A., « π in the Mandelbrot set », *Fractals* 9, 2001. Zhang, Y., *Annals of Mathematics* 179, 2014 (annoncé en 2013). Polymath, D. H. J., 2014. Corpus ARC : Volume 2, chapitre 12 ; Volume 0, 2.1 ; *Riemann sans le zéro* ; *Des zéros sous zéro* ; *Ce que Riemann cherchait* ; *Rien ne courbe* ; *Le Fini et l'Infini mêlés* ; *Le Carré du relais* ; *Emergence of Quantum Correlations* v4.0 ; *Une preuve de l'hypothèse de Riemann* v4.5 (février 2026) ; *The Octet Rule as Arithmetic Necessity* (août 2025, v8.0).

Version 1.1, 24 novembre 2026 : ajout de 4.5, le pli universel, avec deux contrôles. Rien n'est retiré.

Version 1.2, 25 novembre 2026 : section 5 refondue. La formule de l'auteur passe en tête (5.1), le flocon de Koch entre comme son exemple (5.2), six contradictions de l'outil de Mandelbrot sont relevées à la source (5.4), le poids est redit (5.6) ; six contrôles ajoutés. Le tableau de comparaison et le tableau de π sont gardés (5.3, 5.5). Rien n'est retiré.

Version 1.3, 25 novembre 2026 : deux précisions de source en 5.4, sur une relecture extérieure contrôlée : le modèle de calcul est de Blum, Shub et Smale (1989) ; les actes de Brooks et Matelski ont paru en 1981. Rien n'est retiré.

Modèle, questions, lectures et règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur. Calculs, formulations et audits assistés par IA (ChatGPT, Gemini, DeepSeek, GLM), à sa demande. Corpus ARC, CC BY 4.0.
