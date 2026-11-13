# Pascal sans triangle

**La racine digitale et l'intérieur du nombre**

Corpus ARC · Filipe Bastos · pièce courte, version 0.1 · 13 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

**Avis.** Le triangle de Pascal et la racine digitale sont connus depuis des siècles. Cette pièce les pose l'un sur l'autre et lit ce que chaque position pèse. Elle en tire une règle qui donne la pointe de la pyramide sans monter la pyramide, et une lecture de la pointe 9. L'arithmétique est élémentaire ; il est possible que la règle figure ailleurs sous une autre forme, et le scribe ne l'a pas cherchée. Tous les comptes sont refaits.

Statuts : F, fait connu ; Th, calcul fini vérifié ou démonstration ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `pascal_verif.py`.

## 1. Les deux outils

**1.1 (F).** La racine digitale : on additionne les chiffres d'un nombre et l'on recommence jusqu'à un seul chiffre, de 1 à 9. C'est la preuve par 9 des écoles. Le triangle arithmétique, que Pascal décrit en 1654, donne les lignes 1 2 1, puis 1 3 3 1, puis 1 4 6 4 1.

**1.2 (la pyramide).** On écrit les chiffres d'un nombre sur une ligne. Sous chaque couple de voisins, on écrit leur somme réduite à sa racine. On recommence jusqu'à un seul chiffre : la pointe. Pour 256 : 2 5 6, puis 7 2, puis 9.

**1.3 (Th).** La pointe est la somme des chiffres pesés par la ligne de Pascal de même longueur, réduite. Pour trois chiffres : début + 2 × centre + fin. La racine, elle, pèse chaque chiffre une fois.

## 2. La règle

**2.1 (L).** « Donc avec la racine, tu peux presque déterminer le Pascal. » « Je suis sûr qu'on peut trouver la logique aussi pour 5 chiffres ; et pour les pairs, on prend les 2 du centre et on additionne. Fini le long triangle pour trouver la pointe. » (l'auteur, 13 novembre 2026).

**2.2 (Th, la règle).** Pointe = racine + supplément de l'intérieur. Les deux bords ne donnent jamais de supplément : Pascal et la racine les pèsent tous deux une fois.

**2.3 (Th, les suppléments).** Ce qu'on ajoute à la racine, position par position, les tours de 9 retirés :

- 2 chiffres : 0 0. La pointe est la racine.
- 3 chiffres : 0 1 0. Une fois le centre.
- 4 chiffres : 0 2 2 0. Deux fois les deux du centre.
- 5 chiffres : 0 3 5 3 0.
- 6 chiffres : 0 4 0 0 4 0.
- 7 chiffres : 0 5 5 1 5 5 0.
- 8 chiffres : 0 6 2 7 7 2 6 0.
- 9 chiffres : 0 7 0 1 6 1 0 7 0.
- 10 chiffres : 0 8 8 2 8 8 2 8 8 0.

**2.4 (Th, exemples).** 256 : racine 4, centre 5, pointe 9. 512 : racine 8, centre 1, pointe 9. 1024 : racine 7, milieu 0 + 2, doublé 4, pointe 2. 65 536 : racine 7 (somme 25), anneau 3 × (5 + 3) = 24, centre 5 × 5 = 25 ; 25 + 24 + 25 = 74, pointe 2. La pyramide complète donne les mêmes pointes.

**2.5 (Th, trois remarques).** Le voisin du bord pèse la longueur moins deux : 1, 2, 3, 4, 5. À six chiffres, les deux du centre ne comptent plus : leur poids de Pascal est 10, soit 9 + 1, un tour de plus que ce que la racine compte déjà. À dix chiffres, la pointe ne lit que quatre positions : la première, la dernière, et trois fois la quatrième et la septième ; les six autres ne pèsent que des tours.

**2.6 (L, Th, deux chiffres).** « Pascal sur un nombre à deux chiffres, c'est du délire de licornes. » (l'auteur, 13 novembre 2026). Le compte le dit : à deux chiffres la pointe est la racine, Pascal n'y ajoute rien. La pyramide commence au triplet : un début, un centre, une fin.

**2.7 (L).** « La racine, c'est le résultat une fois tout déballé. » (l'auteur, 13 novembre 2026). La racine lit le nombre à plat ; la pointe le lit avec le poids de son intérieur.

## 3. Les triplets

**3.1 (Th).** Sur un triplet : pointe = racine + centre. Les 900 nombres de trois chiffres se partagent également : 100 par pointe. Dans chaque pointe, 10 triplets par racine, et 20 pour la racine qui porte le nom de la pointe, parce qu'elle a deux centres, 0 et 9.

**3.2 (L).** « Donne-moi les 100 qui pointent à 9, tu vas voir ce que je vois. » « Maintenant regarde leurs racines et la proportion. » (l'auteur, 13 novembre 2026).

**3.3 (Th, les 100 qui pointent 9).** Rangés par racine, ils ont tous le même centre, et ce centre est l'inverse de la racine :

- racine 1, centre 8 : 181 280 289 388 487 586 685 784 883 982
- racine 2, centre 7 : 173 272 371 470 479 578 677 776 875 974
- racine 3, centre 6 : 165 264 363 462 561 660 669 768 867 966
- racine 4, centre 5 : 157 256 355 454 553 652 751 850 859 958
- racine 5, centre 4 : 140 149 248 347 446 545 644 743 842 941
- racine 6, centre 3 : 132 231 330 339 438 537 636 735 834 933
- racine 7, centre 2 : 124 223 322 421 520 529 628 727 826 925
- racine 8, centre 1 : 116 215 314 413 512 611 710 719 818 917
- racine 9, centre 0 ou 9 : 108 198 207 297 306 396 405 495 504 594 603 693 702 792 801 891 900 909 990 999

**3.4 (Th).** Un triplet pointe 9 si et seulement si sa racine et son centre sont inverses, ou si sa racine est 9 et son centre 0 ou 9. Chaque famille avance par 99, avec un seul pas de 9. La liste entière avance par pas de 8, de 9 et de 17 = 8 + 9 : 72, 18 et 9 fois.

**3.5 (Th, les rails).** Pour un triplet qui pointe 9, le centre et la somme des flancs sont sur le même rail. Centre 1, 4, 7 : flancs 7, 1, 4, le rail D qui tourne. Centre 2, 5, 8 : flancs 5, 8, 2, le rail G qui tourne. Centre 3, 6, 9 : flancs 3, 6, 9, l'axe qui se répond à lui-même.

**3.6 (Th, qui est dans la liste).** 256 et 512. 280 = 5 × 7 × 8 et 578. 495, la constante de Kaprekar à trois chiffres, avec 198, 297, 396, 594, 693, 792, 891. Cinq carrés : 256, 289, 529, 784 = 28 × 28, 900. Un seul cube : 512.

## 4. Ce que le 9 a de propre

**4.1 (L).** « Les paires du 9 sont des inverses. Obligées. Sa construction demande des inverses. » (l'auteur, 13 novembre 2026).

**4.2 (Th).** Toutes les pointes ont la même proportion : la fréquence ne distingue pas le 9. Ce qui le distingue est la nature du couple formé par la racine et le centre. Pour la pointe 9, ces couples sont les quatre paires inverses du cadastre, (1, 8), (2, 7), (3, 6), (4, 5), dans les deux sens, et le 9 avec lui-même. Pour la pointe 8, les couples sont (1, 7), (2, 6), (3, 5), qui ne sont pas des paires du cadastre, et (4, 4), un nombre collé à lui-même. Chaque pointe a une famille où la racine égale le centre ; pour le 9, cette famille est le 9 seul.

**4.3 (glose du scribe, à valider).** Pointer 9, c'est avoir le dehors et le dedans en paire : le nombre entier, lu par sa racine, et son milieu sont partenaires.

**4.4 (Th, les puissances de 2).** Les puissances de 2 à trois chiffres sont trois : 128, 256, 512. 128 pointe 4 ; 256 et 512 pointent 9. 256 est dans la famille de la paire centrale (4, 5) ; 512 dans celle de la paire extrême (1, 8).

**4.5 (Th, le témoin).** Un triplet pris sans raison pointe 9 une fois sur neuf. En avoir au moins deux sur trois sans raison arrive dans 3,4 % des cas, environ une fois sur 29. L'échantillon est de trois nombres : le chiffre est donné tel quel, sans plus.

## 5. Ce que la pièce ne fait pas

**5.1.** Elle ne prétend pas que la règle soit nouvelle : elle découle en une ligne de la ligne de Pascal et de la racine. Ce qui est de l'auteur est la lecture : le centre, les paires, les rails, et le triplet comme lieu où la pyramide commence. Elle ne dit rien de la pyramide en dehors de l'écriture décimale.

## Annexe. Vérifications et sources

Script `pascal_verif.py` (Python 3, bibliothèque standard seule). Treize contrôles sur les calculs, tous conformes : la pointe par la ligne de Pascal ; la règle et la table des suppléments, sur tous les nombres jusqu'à cinq chiffres et 4 000 tirages par longueur au-delà ; le cas des deux chiffres ; les 900 triplets ; la proportion 10 et 20 ; les couples de la pointe 9 ; la famille collée de chaque pointe ; les rails ; les pas de 99, 8, 9 et 17 ; les nombres présents dans la liste ; le témoin ; le cas des dix chiffres ; les exemples. Un quatorzième contrôle porte sur la typographie de la source.

Non recontrôlé à la source : la date du traité de Pascal, donnée de mémoire.

Sources : B. Pascal, *Traité du triangle arithmétique*, 1654. Corpus ARC : Volume 2, annexe D (cascade de Pascal) ; dossier *Le début, le centre et la fin* ; pièce *Erdős 406 : la forme et le doublement*, v0.1.
