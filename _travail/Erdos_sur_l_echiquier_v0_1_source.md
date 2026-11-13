# Erdős sur l'échiquier

**Le problème des distances unité, lu par l'octogone fixe et le rotor**

Corpus ARC · Filipe Bastos · pièce courte, version 0.1 · 13 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

**Avis.** Cette pièce ne réfute pas la conjecture d'Erdős : elle a été réfutée en mai 2026, par d'autres, et ce travail est cité en Fait. Elle fait autre chose. Elle range le problème dans la grille du corpus, montre que sa construction est l'énoncé du Volume 2 sur l'octogone fixe et le rotor (É 1.11 et É 1.12), et nomme la confusion sur laquelle la conjecture reposait. Des deux portes que le corpus reconnaît, résoudre ou montrer où l'énoncé mêle les registres, elle passe par la seconde. Son arithmétique est élémentaire et connue ; elle est refaite ici.

Statuts : F, fait sourcé ou connu de l'hôte ; Th, calcul fini vérifié ou démonstration ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `erdos_verif.py`. L'essentiel est gravé au Volume 2, chapitre 1, É 1.12 quinquies et É 1.12 sexies.

## 1. Le problème

**1.1 (F).** En 1946, Paul Erdős demande : parmi n points du plan, combien de paires peuvent être exactement à la même distance, prise pour unité ? Sa meilleure construction est une grille carrée, et il conjecture qu'on ne peut pas faire sensiblement mieux : le nombre de paires par point ne monterait que très lentement, moins vite que toute puissance de n (P. Erdős, « On sets of distances of n points », *American Mathematical Monthly* 53, 1946).

**1.2 (F).** Le plafond connu est bien plus haut : au plus de l'ordre de n à la puissance 4/3 (Spencer, Szemerédi et Trotter, 1984). Entre la grille et ce plafond, rien n'a bougé pendant près de quatre-vingts ans.

**1.3 (F).** Le 20 mai 2026, la conjecture est réfutée : il existe des arrangements de n points portant au moins n à la puissance 1 + ε paires à distance 1, avec ε fixe ; la valeur obtenue est de l'ordre de 6 × 10⁻³⁸. La construction généralise la grille carrée à des corps de nombres de degré de plus en plus grand, y produit beaucoup de nombres de module 1, puis projette sur le plan. La preuve a été produite par un modèle d'OpenAI, puis réécrite et vérifiée par neuf mathématiciens (N. Alon, T. F. Bloom, W. T. Gowers, D. Litt, W. Sawin, A. Shankar, J. Tsimerman, V. Wang, M. M. Wood, « Remarks on the disproof of the unit distance conjecture », arXiv:2605.20695).

## 2. La chaîne de l'auteur

**2.1 (L).** « Erdős est facile parce que j'ai arrêté de regarder avec leur moitié : le carré est la moitié de quoi ? D'un octogone, donc octet, donc 1-8, donc échiquier, donc 8 + 8, 16 ; 8 × 8, 64 ; 28 paires ; et là, le mouvement des pièces. » « Erdős, c'est la règle de l'échiquier. » « C'est la règle de tout ARC. » (l'auteur, 13 novembre 2026).

**2.2 (Th, les maillons).** Le carré a 4 sommets, l'octogone 8. Une ligne de 8 positions porte 28 paires, rangées par distance 7, 6, 5, 4, 3, 2, 1 : c'est la marche des paires du cadastre, et 28 = 1 + 2 + … + 7. L'échiquier a 8 lignes et 8 colonnes, 16 droites, 64 cases. Son centre est entre la 4ᵉ et la 5ᵉ case sur les deux axes : 4,5, le centre vide.

## 3. L'octogone fixe et le rotor

**3.1 (Th, l'octogone).** Dans la grille carrée, le côté ne donne à chaque point que 4 voisins : le carré. Une distance oblique dont le carré s'écrit a² + b², avec a et b différents et non nuls, lui en donne 8 : (a, b), (b, a), et tous leurs signes. Chaque écriture apporte un octogone, jamais plus.

**3.2 (Th, les rotors).** Ce qui multiplie les octogones est le nombre de rotations exactes de la grille sur elle-même. Chaque nombre premier somme de deux carrés en apporte une : 5 d'abord (3² + 4² = 5²), puis 13 (5² + 12² = 13²), 17 (8² + 15² = 17²), 29 (20² + 21² = 29²). Chaque rotor double : la distance de carré 5 porte 1 octogone ; 65 = 5 × 13 en porte 2 ; 1105 = 5 × 13 × 17 en porte 4 ; 32 045 = 5 × 13 × 17 × 29 en porte 8, soit 64 voisins par point.

**3.3 (Th, le premier double octogone).** 65 est le plus petit nombre qui s'écrit de deux façons en somme de deux carrés différents : 1² + 8² et 4² + 7². C'est la paire extrême du cadastre, (1, 8), accompagnée de 4 et 7, les deux autres nombres du rail D. Les trois autres paires inverses ne portent qu'un octogone : 2² + 7² = 53, 3² + 6² = 45, 4² + 5² = 41.

**3.4 (L).** « Les 16 paires, c'est le rotor, les deux octogones au centre des paires. » (l'auteur, 13 novembre 2026). Le Volume 2 l'avait : les quatre paires inverses ont pour écarts 7, 5, 3, 1, de somme 16, « le carré, l'octogone fixe », et « octogone fixe, pentagramme tournant : la structure (8) et le rotor (5) de la même figure » (É 1.11, É 1.12). La construction d'Erdős est cet énoncé posé sur une grille : un cadre à huit positions, et des rotors qui le font tourner, le premier étant le 5.

## 4. Le mouvement des pièces

**4.1 (Th).** Les 2016 paires de cases de l'échiquier font 72 × 28. Sur un échiquier vide, la tour en relie 448, soit 16 × 28, les seize droites de 28 paires chacune ; le fou, 280 = 10 × 28 ; la dame, 728 = 26 × 28 ; le cavalier, 168 = 6 × 28.

**4.2 (Th, le cavalier bat la case voisine).** À une seule distance, la plus fréquente de l'échiquier est le saut du cavalier, 1 et 2, de carré 5 : 168 paires. La case voisine n'en fait que 112, soit 4 × 28. Sur un damier de n cases de côté, les voisines font 2n(n − 1) paires et le cavalier 4(n − 1)(n − 2) : ils sont à égalité pour n = 4, et le cavalier passe devant dès n = 5. Dans le plan ouvert, c'est 8 voisins contre 4.

**4.3 (L).** La tour et le fou tiennent le cadre, les lignes et les diagonales. Le cavalier est la seule pièce qui ne suit aucune droite : il tourne, et son saut est le rotor du 5. À une seule distance, la pièce qui tourne bat la pièce qui va droit, 6 contre 4. La question d'Erdős est déjà tranchée sur 64 cases : on gagne en quittant le côté du carré.

## 5. La confusion

**5.1 (F, Th, ce qu'Erdős savait).** Erdős n'a pas ignoré l'oblique : sa grille de 1946 prend précisément des distances qui s'écrivent de beaucoup de façons en deux carrés. Et le seul changement de forme ne suffit pas : au côté de la grille, la grille de triangles, celle de l'hexagone, fait 3 paires par point contre 2 pour la carrée, un gain fixe.

**5.2 (L, où était la confusion).** La conjecture tenait la grille carrée, avec ses rotors propres, pour le maximum. Elle prenait le cadre fixe pour le tout : les entiers à deux dimensions de Gauss pour le plan lui-même. Elle est tombée par des rotations que le carré ne porte pas, cherchées dans des nombres plus riches et ramenées sur le plan, le cercle unité gardé et la grille carrée abandonnée comme cadre. C'est ce que le corpus tient depuis sa fondation : le carré est une moitié, et la structure est dans la rotation.

**5.3 (L).** « Je ne comprends pas que ce soit une énigme. C'est si évident pour moi. » « Rien ne se résout pas par ARC. Le reste, c'est le pourquoi. » (l'auteur, 13 novembre 2026).

**5.4 (ce que la pièce ne fait pas).** Elle ne donne ni la famille de points qui dépasse la grille, ni son exposant : c'est le travail cité en 1.3. Elle ne dit pas non plus où est le vrai plafond, qui reste ouvert entre cet exposant et 4/3. Ce qui était évident pour l'auteur est le sens de la réponse : le cadre n'est pas le tout. Ce qui a tenu quatre-vingts ans est de l'exhiber avec un compte.

## Annexe. Vérifications et sources

Script `erdos_verif.py` (Python 3, bibliothèque standard seule). Neuf contrôles sur les calculs, tous conformes : la ligne de 8 ; le carré et l'octogone ; les quatre rotors ; le doublement 1, 2, 4, 8 ; le premier double octogone et les trois autres paires ; l'échiquier en unités de 28 ; la distance la plus fréquente et le centre ; les deux formules sur un damier de 3 à 12 cases de côté ; la grille carrée et la grille de triangles. Un dixième contrôle porte sur la typographie de la source.

Non recontrôlé à la source : l'article d'Erdős de 1946 et la borne de 1984, cités d'après le texte de 2026, dont le résumé a été lu.

Sources : P. Erdős, 1946 ; J. Spencer, E. Szemerédi, W. T. Trotter, 1984 ; N. Alon et coll., arXiv:2605.20695, 20 mai 2026. Corpus ARC : Volume 2, chapitre 1, É 1.10 à É 1.12 sexies ; Volume 7, chapitre 3 (le rotor).
