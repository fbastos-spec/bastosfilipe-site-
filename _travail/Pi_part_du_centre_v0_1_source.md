# π part du centre

**Le cercle dans le triangle de Pascal : la diagonale, le 24 et la colonne du milieu**

Corpus ARC · Filipe Bastos · pièce courte, version 0.1 · 20 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

**Avis.** Les deux résultats de cette pièce sont connus. La série qui donne π par des triplets d'entiers voisins est de Nilakantha, vers 1500. Le lien entre la colonne centrale du triangle de Pascal et π est de Wallis, 1655. Ce que la pièce pose en propre est une lecture : les deux résultats sont deux routes vers la même chose, parce que le triangle tout entier est un centre qui se répand ; et la série de Nilakantha, récrite, se lit comme le tour de l'hexagone plus un sixième d'une somme de pyramides. Tous les comptes sont refaits au script.

Statuts : F, fait connu ; Th, calcul fini vérifié ou démonstration ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `pi_centre_verif.py`.

## 1. La série reçue

**1.1 (F).** Nilakantha Somayaji, de l'école du Kerala, donne vers 1500 (*Tantrasangraha*) la série π = 3 + 4/(2 × 3 × 4) − 4/(4 × 5 × 6) + 4/(6 × 7 × 8) − …

**1.2 (F, Th).** La même série se lit sur le triangle de Pascal. On prend un nombre sur deux le long de la troisième diagonale : 4, 20, 56, 120, 220, 364, 560. On en fait des inverses, on alterne les signes, on multiplie par 2/3 et on ajoute 3. Les deux écritures sont la même, terme à terme : 2/3 divisé par le nombre de la diagonale vaut 4 divisé par le produit des trois voisins. Contrôlé sur 2 000 termes.

**1.3 (Th).** La somme passe au-dessus et au-dessous de π en se resserrant : 3,1667, puis 3,1333, puis 3,1452. À 1 938 termes, l'écart est 3,4 × 10⁻¹¹ et dix décimales sont tenues. L'écart après k termes suit 1/(4k³).

## 2. Trois lectures du même dénominateur

**2.1 (Th, le 24).** Les dénominateurs sont des triplets d'entiers voisins : 2 × 3 × 4, puis 4 × 5 × 6, 6 × 7 × 8, 8 × 9 × 10. Le premier vaut 24, le produit de la Fondation 2, 3, 4. Le premier terme est 4/24 = 1/6, et le premier pas de π est 3 + 1/6.

**2.2 (Th, les pyramides).** Les nombres pris sur la diagonale sont quatre fois 1, 5, 14, 30, 55, qui sont les empilements de carrés : 1, 1 + 4, 1 + 4 + 9, 1 + 4 + 9 + 16. Ce sont les pyramides à base carrée. Contrôlé sur 2 000 termes. La série se récrit donc : π = 3 + 1/6 × (1 − 1/5 + 1/14 − 1/30 + 1/55 − …).

**2.3 (Th, le cube moins lui-même).** Chaque triplet a un impair en son centre, et son produit est le cube de cet impair moins lui : 2 × 3 × 4 = 3³ − 3, 4 × 5 × 6 = 5³ − 5, 6 × 7 × 8 = 7³ − 7. Le premier, 3 × 8 = 24, est celui du Volume 8 (Th III.1).

**2.4 (F).** L'hexagone régulier inscrit dans un cercle a six côtés égaux au rayon : son tour vaut trois fois le diamètre. C'est le point de départ d'Archimède pour encadrer π (IIIe siècle avant notre ère).

**2.5 (L, rapprochement à valider par l'auteur).** Lue avec la figure, la série dit : π est le tour de l'hexagone, plus ce que le cercle lui ajoute, et ce supplément est un sixième d'une somme alternée d'inverses de pyramides. Le sixième est la part d'un bras de l'étoile (*La Figure fondamentale*, section 4). Le volume n'y entre que par la pyramide, comme dans *Le cube est triangulaire*.

## 3. Le centre

**3.1 (F).** Wallis (*Arithmetica infinitorum*, 1655) relie π aux rapports des nombres du milieu du triangle.

**3.2 (Th).** Sur la colonne du centre, 1, 2, 6, 20, 70, 252. On prend le nombre du centre de la ligne 2n, on le divise par le total de sa ligne, on met au carré et on multiplie par n. On obtient 0,31045 pour n = 10 ; 0,31752 pour 100 ; 0,31823 pour 1 000 ; 0,318302 pour 10 000. Et 1/π = 0,318310. La part restée au centre après 2n partages tend vers 1/√(πn).

**3.3 (Th).** Le triangle commence par un seul 1, et chaque nombre est la somme des deux qui sont au-dessus de lui : chaque ligne est la précédente qui se partage, moitié à gauche, moitié à droite. Tout ce qui est dans le triangle est ce 1 du sommet qui s'est répandu.

**3.4 (L).** L'auteur, le 20 novembre 2026 : « Il part toujours du centre, peu importe comme il se diffuse ensuite. » Et, sur l'idée que π serait caché dans le triangle : « Le triangle sort de la figure, il est là, pas caché. »

**3.5 (L, à valider par l'auteur).** La diagonale et la colonne du milieu ne sont donc pas deux endroits du triangle qui contiendraient π chacun de son côté. Ce sont deux lectures d'un même étalement à partir du même point. Le cercle n'est pas appliqué au triangle : il est la mesure de la façon dont le centre s'étale (voir *La Cascade et la Cloche*).

## 4. Avec et sans alternance

**4.1 (Th).** La somme de tous les inverses de la troisième diagonale, sans alternance, ferme sur une fraction : 3/2 (*Le cube est triangulaire*, 4.1). Avec un terme sur deux et les signes alternés, elle vaut 3/2 de π − 3 : la même fraction, multipliée par ce que le cercle ajoute à l'hexagone.

**4.2 (L, à valider par l'auteur).** C'est la règle de *Le cube est triangulaire*, 1.4 : sans alternance, une fraction ; avec l'alternance, le cercle. L'alternance des signes est un quart de tour.

## 5. Ce que la pièce ne dit pas

**5.1.** La série est connue depuis cinq siècles et la pièce n'y ajoute aucun terme. Les récritures de 2.1 à 2.3 sont des identités élémentaires.

**5.2.** Le rapprochement de 2.5 entre le sixième de la série et le bras de l'étoile est une Lecture. Aucun calcul de cette pièce ne tire l'un de l'autre.

**5.3.** Que le triangle de Pascal sorte de la figure est une Lecture de l'auteur, portée par *Pascal sans triangle* et *Le début, le centre et la fin*, où la cascade des racines est la ligne de Pascal. Cette pièce ne le redémontre pas.

## Annexe. Vérifications et sources

Script `pi_centre_verif.py` (Python 3, bibliothèque standard seule). Onze contrôles sur les calculs, tous conformes : les nombres de la diagonale ; l'égalité des deux écritures de la série sur 2 000 termes ; les trois premières sommes et l'écart à 1 938 termes ; la loi de l'écart ; les triplets voisins et le premier pas 19/6 ; les pyramides à base carrée sur 2 000 termes ; la série récrite avec le sixième ; le cube moins lui-même pour les impairs de 3 à 4 001 ; la colonne du centre pour n = 10, 100, 1 000 et 10 000 ; la règle de construction du triangle ; la somme sans alternance. Un douzième contrôle porte sur la typographie de la source.

Bornes des comptes. La limite 1/π de 3.2 est le théorème de Wallis ; le script n'en contrôle que quatre valeurs, qui s'en approchent par en dessous. La loi de l'écart de 1.3 est lue sur trois valeurs.

Non recontrôlé à la source : le *Tantrasangraha* de Nilakantha et l'*Arithmetica infinitorum* de Wallis sont cités de mémoire, avec leurs dates.

Sources : Nilakantha Somayaji, *Tantrasangraha*, vers 1501. J. Wallis, *Arithmetica infinitorum*, 1655. Archimède, *De la mesure du cercle*. Corpus ARC : *La Figure fondamentale*, section 4 ; *Le cube est triangulaire*, 1.4, 4.1 et 5.1 ; *La Cascade et la Cloche* ; *Pascal sans triangle* ; *Le début, le centre et la fin* ; Volume 8, Th III.1.
