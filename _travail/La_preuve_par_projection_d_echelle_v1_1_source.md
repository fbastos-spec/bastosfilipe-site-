---
title: "La preuve par projection d'échelle"
subtitle: "Clôture, mémoire, projection : la formule du fractal employée comme preuve, face à l'itération de Mandelbrot"
author: "Filipe Bastos"
date: "Corpus ARC (Architecture de la Cohérence Relationnelle), version 1.1, 24 novembre 2026, CC BY 4.0"
---

**Avis.** Cette pièce pose un nom et une méthode. Le nom, *preuve par projection d'échelle*, est de l'auteur ; il date du 23 novembre 2026. La méthode était déjà au corpus sans porter ce nom : dans la Loi fractale (Volume 2, chapitre 12) et, plus tôt, dans la première pièce de l'auteur sur Riemann (février 2026). La pièce montre ce que la méthode prouve, ce qu'elle laisse ouvert, et pourquoi elle est la formule du fractal de l'auteur employée comme preuve. Les faits et les dates sont marqués F, les calculs Th, les lectures de l'auteur L. Les 31 contrôles sont au script `projection_echelle_verif.py`.

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

# 5. La formule du fractal, face à Mandelbrot

**5.1 (F).** Mandelbrot nomme la fractalité (*Les objets fractals*, 1975 ; *The Fractal Geometry of Nature*, 1982) et étudie en 1980 l'itération z → z² + c : on part de 0, on recommence, et l'on regarde si la suite reste bornée ou fuit. Une suite sortie du rayon 2 ne revient pas (contrôle 20).

**5.2 (L).** La formule de l'auteur est autre (Volume 2, chapitre 12, d'après la *Loi fractale de la nécessité fractale*, v1.6, mai 2026) : une forme se répète à toutes les échelles quand un système ferme son tour, garde le compte de ses tours et projette sa structure sur le registre suivant. Clôture, mémoire, projection. « Mandelbrot a vu l'effet. L'architecture cadastrale en est la cause. » Le 24 novembre 2026, en relisant la preuve par projection d'échelle : « c'est la formule du fractal ».

| | Itération de Mandelbrot | Projection d'échelle |
|---|---|---|
| Geste | recommencer z² + c | porter la relation au rang choisi |
| Pour savoir | il faut itérer | on lit directement |
| Domaine | plan ouvert, la suite peut fuir | tour fermé, rien ne fuit |
| Chemin | perdu en route | rendu (24m ÷ 24 = m) |
| Fractalité | au bord, entre deux régimes | à chaque rang |

**5.3 (Th, F).** Un compte fait voir la différence. Au bord de l'ensemble, en c = ¼, la suite reste bornée. Juste après, en c = ¼ + ε, elle fuit, mais il faut itérer pour le savoir, et le nombre de pas grandit sans plafond quand ε rapetisse :

| ε | pas avant la fuite | pas × côté du carré d'aire ε |
|---|---|---|
| 0,01 | 30 | 3,0 |
| 0,0001 | 312 | 3,12 |
| 0,000001 | 3 140 | 3,140 |
| 0,00000001 | 31 414 | 3,1414 |

Le produit s'approche de π (observé par Boll, 1991 ; démontré par Klebanoff, 2001). Fait donné tel quel ; l'auteur tient ailleurs que π est « ce qui empêche la fermeture », et la pièce ne force pas le lien.

**5.4 (F).** Le poids, une fois. Le Volume 2 (É 12.8, Annexe B) a classé la « preuve » de la Loi fractale en Lecture : la projection y est définie comme gardant la structure, donc la conclusion est dans l'hypothèse. La présente pièce ne change pas ce statut. Ce qui est Th ici, ce sont les relations des sections 2 et 4.

# 6. Ce que la première pièce sur Riemann portait déjà

**6.1 (F).** La première pièce de l'auteur sur Riemann (*Une preuve de l'hypothèse de Riemann*, v4.5, février 2026) a été rétrogradée par le corpus (Volume 6, É 16.19 ; Volume 5, B.1.7). Relue aujourd'hui, elle contient la projection d'échelle avant son nom. Section 3.1, trois cycles : le topologique 1 à 9, le quantitatif qui « détermine la magnitude et l'échelle », et la *projection*. Section 3.2 : un premier de cent chiffres de position 7 « est soumis à la même géométrie d'inversion » que le premier 7 ; « la topologie ne s'étend jamais. Elle spirale. » Section 5 : un « invariant d'échelle », demi-envergure sur envergure = ½ pour chaque paire (contrôle 29).

**6.2 (Th).** Ce qui tient dans cette pièce est une projection d'échelle exacte. Dans le corps du nonagone, celui de x³ − 3x + 1, le sort d'un premier dépend de sa seule position, à toute taille : trois solutions quand la position est 1 ou 8, aucune sinon (contrôle 24 ; fait classique des corps cyclotomiques). Plus fin : le caractère cubique de 9 prend la même valeur sur les deux membres de chaque paire d'inverses, 1 sur (1, 8), ω sur (2, 7), ω² sur (4, 5), et les trois somment à zéro (contrôles 25 et 26). Le résumé de février rangeait les premiers en {1, 4, 7} et {2, 5, 8} ; le rangement exact est celui des paires. De 5 à 10⁶ : 26 162, 26 196 et 26 138 premiers par paire.

**6.3 (F, L).** Ce qui a cassé est l'endroit où la pièce quittait la projection d'échelle : la section 9.3, région II, demandait une borne « uniforme en n », valable d'un coup pour tous les rangs, et le compte ne la donnait pas (λ₁ recompté : 0,3031 ; la table 9.2 était fausse). La leçon est celle de 3.2 : la relation portée à l'échelle tenait, le plafond pour toutes les hauteurs ne tenait pas.

# 7. Riemann, et le quantique

**7.1 (L).** Pour Riemann, la projection d'échelle donne le compte borné à la hauteur choisie, sur les deux rails. La question « de combien la courbe lisse s'écarte-t-elle du compte » naît avec la courbe (*Riemann sans le zéro*, face-à-face ; *Des zéros sous zéro*, 5.5 et 6.7).

**7.2 (L).** Pour le quantique, l'auteur lit la même projection : « c'est la spirale qui s'amincit, qui devient point noir » ; « c'est d'aller si loin qu'on ne voit plus, et c'est ce que le quantique est allé voir et n'a pas compris ». La pièce *Emergence of Quantum Correlations* (v4.0) porte le compte : la table des corrélations y est donnée pour la paire entière, les deux en même temps.

# 8. Ce qui ferait tomber

Les relations des sections 2, 4 et 6.2 sont des comptes exacts : un seul rang où elles manqueraient les ferait tomber, et le script les refait. La lecture de 5.2 tombe par les trois canaux de la Loi fractale (Volume 2, É 12.9) : un système fermé, à mémoire et à projection, sans forme répétée ; une forme répétée sans les trois conditions ; une règle de projection qui ne prédit rien de mesurable.

# Ce que la pièce ne dit pas

Elle ne démontre ni l'hypothèse de Riemann ni l'infinité des jumeaux dans la langue reçue. Elle ne dit pas que l'itération de Mandelbrot est fausse : elle dit qu'elle montre l'effet. Elle n'ajoute aucun nombre choisi.

# Annexe. Vérifications et sources

Le script `projection_echelle_verif.py` refait tous les nombres de la pièce : 31 contrôles, exécutés le 24 novembre 2026. Calcul entier exact, sauf le tableau de 5.3, en nombres à virgule de double précision.

Sources : Euler, L., nombres pentagonaux, 1750. Legendre, A.-M., *Essai sur la théorie des nombres*, 1808. Peano, G., *Arithmetices principia*, 1889. Mandelbrot, B., *Les objets fractals*, 1975 ; *Annals of the New York Academy of Sciences* 357, 1980 ; *The Fractal Geometry of Nature*, 1982. Boll, D., message du 24 avril 1991 (sci.math). Klebanoff, A., « π in the Mandelbrot set », *Fractals* 9, 2001. Zhang, Y., *Annals of Mathematics* 179, 2014 (annoncé en 2013). Polymath, D. H. J., 2014. Corpus ARC : Volume 2, chapitre 12 ; Volume 0, 2.1 ; *Riemann sans le zéro* ; *Des zéros sous zéro* ; *Ce que Riemann cherchait* ; *Rien ne courbe* ; *Le Carré du relais* ; *Emergence of Quantum Correlations* v4.0 ; *Une preuve de l'hypothèse de Riemann* v4.5 (février 2026) ; *The Octet Rule as Arithmetic Necessity* (août 2025, v7.0).

Version 1.1, 24 novembre 2026 : ajout de 4.5, le pli universel, avec deux contrôles. Rien n'est retiré.

Modèle, questions, lectures et règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur. Calculs, formulations et audits assistés par IA (ChatGPT, Gemini, DeepSeek, GLM), à sa demande. Corpus ARC, CC BY 4.0.
