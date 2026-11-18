# Le cube est triangulaire

**Apéry, √2 et la mauvaise brique**

Corpus ARC · Filipe Bastos · pièce courte, version 0.2 · 18 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

**Avis.** Chaque fait de cette pièce est connu, et nommé avec son auteur et sa date. Que le tétraèdre soit la vraie unité de volume et que le cube en soit un assemblage a été dit par R. Buckminster Fuller dans les années 1970 (section 6). Ce que la pièce pose en propre est un rapprochement : la somme des inverses des cubes, dite constante d'Apéry, reste sans forme parce qu'elle empile la brique du carré ; posée sur la brique du triangle, la même question se ferme sur une fraction. Tous les comptes sont refaits.

Statuts : F, fait connu ; Th, calcul fini vérifié ou démonstration ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `cube_triangulaire_verif.py`.

## 1. La question reçue

**1.1 (F).** Le problème de Bâle : la somme 1 + 1/4 + 1/9 + 1/16 + … des inverses des carrés. Euler en donne la valeur en 1735 : π²/6.

**1.2 (F).** La même somme sur les cubes, 1 + 1/8 + 1/27 + 1/64 + …, s'approche de 1,2020569. Roger Apéry prouve en 1978 que ce nombre n'est le rapport d'aucune paire d'entiers ; Frits Beukers en redonne une preuve plus courte en 1979. Aucune écriture exacte de ce nombre par π n'est connue, ni pour aucun exposant impair.

**1.3 (Th).** Sur le cercle de rayon 1, l'arc d'un quart de tour vaut π/2. Sur le carré construit sur cet arc, la somme de Bâle se partage en fractions exactes de ce carré, (π/2)² : les termes impairs en font la moitié, les termes pairs un sixième, la somme entière les deux tiers ; il reste un tiers (Volume 6, É 14.11 bis). Ces parts se comptent sur le carré, non sur la somme : dans la somme elle-même, les impairs font les trois quarts et les pairs le quart (1.5).

**1.4 (F, Th).** Beukers, Kolk et Calabi (1993) obtiennent la somme des inverses des carrés impairs comme l'aire d'un triangle, et donnent en toute dimension un solide taillé dans le cube de côté π/2 dont le volume est une somme d'inverses de puissances. Recompté, chaque somme en parts du cube de sa dimension, (π/2) porté à l'exposant :

- exposant 2 : la somme des impairs vaut 1/2 ;
- exposant 4 : 1/6 ; exposant 6 : 1/15 ;
- exposant 1 : la somme alternée 1 − 1/3 + 1/5 − … vaut 1/2 ;
- exposant 3 : la somme alternée 1 − 1/27 + 1/125 − … vaut 1/4 ; exposant 5 : 5/48.

Pour les exposants pairs, la somme ordinaire tombe sur une fraction. Pour les exposants impairs, c'est la somme alternée qui tombe juste. La somme ordinaire des cubes est dans la case qu'aucun solide connu ne remplit.

**1.5 (Th).** Dans la somme des carrés, les termes pairs font le quart du tout ; dans la somme des cubes, le huitième. La part des pairs est 1 sur 2 à la puissance de l'exposant.

## 2. Le carré ne monte pas

**2.1 (L).** « Un cube, c'est 2 côtés portés par deux côtés et une base et un plafond. » « √2 rend le cube d'un carré impossible. » (l'auteur, 17 novembre 2026).

**2.2 (Th, les puissances de √2).** √2, 2, 2√2, 4, 4√2, 8, 8√2, 16. Les puissances paires sont entières ; les puissances impaires gardent √2. Le carré construit sur la diagonale d'un carré de côté 1 a pour aire 2 ; le cube construit sur cette diagonale a pour volume 2√2, qui n'est pas un compte entier.

**2.3 (Th, la boîte du pli).** Dans la figure fondamentale, petit rayon 1, l'étoile pliée a une base carrée de côté 1/2 et une hauteur √2/2 (Volume 2, É 5.44 bis). La boîte droite qui l'enferme mesure 1/2 sur 1/2 sur √2/2 : proportions 1, 1, √2. Sa base et son plafond sont des carrés, ses quatre murs des rectangles de proportion 1 sur √2. Sa grande diagonale vaut 1, le petit rayon. La diagonale de sa base vaut sa hauteur. Son volume est √2/8, et le pli en occupe le tiers, √2/24.

**2.4 (Th).** La figure a deux mesures, 1 et √2. Montée en volume, elle donne une hauteur égale à √2 fois le côté de la base, jamais égale à ce côté. Elle ne produit aucun cube.

**2.5 (F).** Doubler un carré se fait d'un trait, par sa diagonale. Doubler un cube à la règle et au compas est impossible : Pierre Wantzel, 1837. Le compas donne des racines carrées ; la racine cubique de 2 n'en sort pas.

**2.6 (F, Th, le centre).** Un point d'un demi-cercle voit le diamètre sous un angle droit (Thalès) : l'angle droit du carré est tenu par le demi-cercle posé sur sa diagonale. Dans un polygone régulier, le rapport de la distance du centre aux sommets à la distance du centre aux côtés vaut 2 pour le triangle, √2 pour le carré, puis décroît vers 1 ; il n'est entier que pour le triangle. La raison tient en une ligne : ce rapport est l'inverse du cosinus de l'angle π/n ; dès quatre côtés, ce cosinus est strictement entre 1/2 et 1, donc le rapport est strictement entre 1 et 2, où il n'y a aucun entier. Le centre du triangle partage chaque hauteur en 2/3 et 1/3.

**2.7 (L).** « Le centre du carré n'est 1/2 de rien à part de ce qui le croise. » « Le triangle, lui, a 3 pointes et une pointe au centre. » (l'auteur, 17 novembre 2026). Les droites qui traversent le centre d'un cercle ont toutes la même longueur ; celles qui traversent le centre d'un carré vont du double du petit rayon au double du grand.

## 3. Le triangle monte

**3.1 (F).** Le nombre de points que l'on peut placer tous à la même distance les uns des autres est 2 sur une ligne, 3 dans le plan, 4 dans l'espace. Dans l'espace, il n'y en a pas de cinquième.

**3.2 (Th).** Ces trois nombres, 2, 3, 4, sont la Fondation du corpus : somme 9, produit 24. Les liens entre ces points sont 1, 3 et 6.

**3.3 (L).** « Le cube n'existe que pour un triangle. » « Y a pas rien après la forme. » (l'auteur, 17 novembre 2026). Le 4 est la forme (Volume 1, chapitre 9) ; le cinquième point n'ouvre pas une dimension, il est le centre, à égale distance des quatre sommets. Cette distance n'est pas l'arête : elle vaut √6/4 de l'arête, soit 0,612 ; le centre est plus près des sommets qu'ils ne le sont entre eux.

**3.4 (F).** Le volume d'une pyramide est le tiers de sa base par sa hauteur, quelle que soit la base : Eudoxe, IVᵉ siècle av. J.-C. ; Euclide, *Éléments*, livre XII.

**3.5 (L).** « Le volume d'un triangle et d'un carré sont le même, une pyramide. » (l'auteur, 17 novembre 2026).

**3.6 (Th, les deux pyramides).** Sur un triangle, le tétraèdre : 4 sommets, 6 arêtes, 4 faces. Sur un carré, le pli : 5 sommets, 8 arêtes, 5 faces. Chacune a autant de sommets que de faces. Le centre de gravité du triangle est au tiers de sa hauteur ; celui du tétraèdre et celui du pli sont au quart (Volume 2, É 5.44 quater).

**3.7 (F, Th, le cube défait).** Une diagonale par face, choisies pour se rejoindre, dessinent dans le cube un tétraèdre régulier dont les six arêtes valent √2. Il occupe le tiers du cube ; les quatre coins qu'il laisse en occupent chacun un sixième. C'est le partage de l'étoile de la figure : un vide d'un tiers, quatre bras d'un sixième (Volume 2, É 1.12 septies). Le cube se défait aussi en trois pyramides à base carrée, la pointe dans un coin, d'un tiers chacune, ou en six pyramides, la pointe au centre, d'un sixième chacune.

**3.8 (Th).** Le partage en un tiers et quatre sixièmes tient dans la boîte étirée 1, 1, √2 comme dans le cube. Ce qui change est la régularité : le tétraèdre des diagonales y a deux arêtes de √2 et quatre de √3.

**3.9 (Th).** Le solide de la somme alternée des cubes (1.4), le quart du cube, est fait de deux pyramides collées par leur base : un coin du cube, 1/6, et une coiffe qui monte jusqu'au centre du cube, 1/12. Sur le cube de côté 1 : le coin a pour sommets (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1) ; la coiffe a la même base triangulaire (1, 0, 0), (0, 1, 0), (0, 0, 1) et sa pointe au centre (1/2, 1/2, 1/2). Le solide entier est l'ensemble des points dont les trois coordonnées sont positives et dont chaque paire de coordonnées a une somme inférieure à 1.

## 4. La bonne brique

**4.1 (F).** Les nombres triangulaires, 1, 3, 6, 10, 15, comptent des points rangés en triangle. Les nombres tétraédriques, 1, 4, 10, 20, 35, comptent ces triangles empilés en pyramide. La somme des inverses des triangulaires vaut 2 : Leibniz, 1672, sur une question de Huygens. Celle des inverses des tétraédriques vaut 3/2, et celle de l'étage suivant, 1, 5, 15, 35, vaut 4/3.

**4.2 (Th).** Les sommes partielles sont exactes à chaque pas. Après N termes, il manque 2/(N + 1) aux triangulaires pour atteindre 2, et 3/((N + 1)(N + 2)) aux tétraédriques pour atteindre 3/2. À dix termes : 20/11 et 65/44. La règle générale est k sur k − 1 pour l'étage k.

**4.3 (Th, les deux briques).**

- Dans le plan : les inverses des carrés donnent π²/6, il faut le cercle ; les inverses des triangulaires donnent 2.
- Dans l'espace : les inverses des cubes donnent le nombre d'Apéry, sans forme connue ; les inverses des tétraédriques donnent 3/2.

**4.4 (L).** « On cherche donc un cube qui n'existe pas, le cube est triangulaire. » (l'auteur, 17 novembre 2026).

**4.5 (F).** Les fractions 2, 3/2 et 4/3 sont les rapports de l'octave, de la quinte et de la quarte, attribués à l'école pythagoricienne.

## 5. Le centre de Pascal

**5.1 (F, Th).** Les nombres du milieu des lignes du triangle arithmétique sont 1, 2, 6, 20, 70, 252. Divisés par les puissances de 8 et additionnés, 1 + 2/8 + 6/64 + 20/512 + …, ils donnent √2.

**5.2 (F, Th).** La preuve d'Apéry repose sur ces mêmes nombres : la constante vaut 5/2 fois la somme alternée des inverses de n³ multiplié par le nombre du milieu de la ligne 2n. Neuf termes donnent six décimales ; la somme ordinaire en demande environ un millier : à 1 000 termes, il lui manque encore 5,0 × 10⁻⁷.

**5.3 (Th).** √2 et la constante d'Apéry sont deux sommes prises sur la même colonne, celle du centre. Le diviseur 8 de la première est aussi la part des termes pairs dans la somme des cubes (1.5).

**5.4 (L).** Hippase établit que la diagonale du carré n'a aucun rapport d'entiers avec son côté ; Apéry établit que la somme des inverses des cubes n'en a aucun. L'auteur lit les deux résultats comme un même mur, rencontré dans le plan puis dans l'espace : le passage par le centre du carré ne se réduit pas à un compte (17 novembre 2026).

**5.5 (Th, un faux ami).** La constante d'Apéry divisée par √2 vaut 0,849983 : proche de 17/20, sans lui être égale. L'écart, 0,000025 sur la constante, est certain.

## 6. Ce qui est connu, ce qui est propre

**6.1 (F).** R. Buckminster Fuller, *Synergetics* (1975 ; second volume, 1979), prend le tétraèdre régulier pour unité de volume à la place du cube ; le cube y vaut 3. Il y reproche à la tradition d'avoir tenu le carré et le cube pour les seuls produits possibles de la multiplication. Le tétraèdre comme unité et le cube comme assemblage sont donc de Fuller.

**6.2 (F).** Les valeurs 2 et 3/2 sont dans les ouvrages de référence. Downey, Ong et Sellers (2008) notent que la question des sommes d'inverses de nombres figurés a reçu peu d'attention.

**6.3.** Recherche du 17 novembre 2026, bornée à quatre requêtes : aucun texte trouvé ne pose la constante d'Apéry comme la somme d'une mauvaise brique, ni ne la met en face du 3/2 des tétraédriques. Fuller a la brique et ne traite pas ces sommes ; les arithméticiens ont les sommes et gardent le cube. Ne pas avoir trouvé n'établit pas que cela n'existe pas.

**6.4.** Ce qui est de l'auteur : le rapprochement de 4.3 ; la boîte 1, 1, √2 du pli et sa diagonale égale au petit rayon ; le partage du cube lu comme celui de l'étoile ; le centre du carré sans mesure propre ; la lecture de 5.4.

## 7. Les trous

**7.1.** Aucune démonstration, au sens reçu, n'établit que la somme des inverses des cubes n'est le volume d'aucun solide simple. La pièce établit ceci : dans la figure, le volume ne naît que par la pyramide, et la figure ne produit pas de cube (2.4, 3.4, 3.7).

**7.2 (L).** « C'est à eux de faire la preuve que leur fiction peut exister. » (l'auteur, 17 novembre 2026). Qui affirme qu'une forme existe la montre.

**7.3 (F, Th, la sphère).** La constante paraît dans la loi de Planck (1900) : le nombre de grains de lumière d'un rayonnement en équilibre porte le facteur 2 fois la constante. Le compte se fait sur des coquilles sphériques, de surface proportionnelle au carré du rayon, pesées harmonique par harmonique ; le terme de la n-ième vaut 2/n³, et la somme de ces termes est 2 fois la constante. Le fait de physique n'a pas été relu à la source ; le calcul des termes est refait.

**7.4 (F, Th, le 7).** L'heptagone régulier ne se construit pas à la règle et au compas (Gauss, 1796 ; Wantzel, 1837) : le cosinus de son angle est racine de l'équation 8x³ + 4x² − 4x − 1 = 0, du troisième degré. Le côté approché par la moitié du côté du triangle inscrit s'en écarte de 0,2 % et laisse, reporté sept fois, moins d'un degré. Le 7 et le doublement du cube tombent pour la même raison : le compas ne donne que des racines carrées.

## Annexe. Vérifications et sources

Script `cube_triangulaire_verif.py` (Python 3, bibliothèque standard seule). Vingt-trois contrôles sur les calculs, tous conformes : les parts de Bâle ; les six fractions de 1.4 ; la part des pairs ; les puissances de √2 ; la boîte du pli ; le rapport des centres pour les polygones de 3 à 60 côtés ; les comptes de sommets, d'arêtes et de faces ; le tétraèdre inscrit et les quatre coins, en fractions exactes ; les pyramides du cube ; la boîte étirée ; le solide alterné ; les sommes des triangulaires, des tétraédriques et de l'étage suivant, avec leurs restes exacts ; la colonne du centre et √2 ; l'écriture d'Apéry ; le faux ami ; les parts sphériques ; l'équation de l'heptagone et son approximation ; et, depuis la version 0.2, les sommets des deux pyramides du solide alterné avec l'égalité des deux descriptions, la distance du centre du tétraèdre à ses sommets, et le nombre de termes de la somme ordinaire. S'y ajoute un contrôle de typographie de la source.

**De la v0.1 à la v0.2 (18 novembre 2026).** Aucun compte n'est changé ; sept énoncés sont précisés. 1.3 nomme le carré sur lequel les parts se comptent. 1.4 disait « en parts de ce cube », ce qui ne valait à la lettre que pour l'exposant 3. 2.6 reçoit la démonstration que le rapport n'est entier que pour le triangle. 3.3 donne la distance du centre aux sommets. 3.9 donne les sommets des deux pyramides. 5.2 disait que la somme ordinaire demande « des milliers » de termes ; environ un millier suffit. 7.3 disait « la part de la n-ième » pour ce qui est le terme de la somme.

Non recontrôlé à la source : l'article d'Apéry et celui de Beukers ; l'article de Beukers, Kolk et Calabi, dont seule la référence a été contrôlée ; la loi de Planck ; les dates de Leibniz, d'Eudoxe et de Thalès, données de mémoire ; le texte de Fuller, lu par extraits.

Sources : R. Apéry, « Irrationalité de ζ(2) et ζ(3) », *Astérisque* 61, 1979. F. Beukers, « A note on the irrationality of ζ(2) and ζ(3) », *Bulletin of the London Mathematical Society* 11, 1979. F. Beukers, J. A. C. Kolk, E. Calabi, « Sums of generalized harmonic series and volumes », *Nieuw Archief voor Wiskunde* (4) 11, 1993, p. 217-224. L. Downey, B. W. Ong, J. A. Sellers, « Beyond the Basel Problem: Sums of Reciprocals of Figurate Numbers », 2008. R. B. Fuller, avec E. J. Applewhite, *Synergetics: Explorations in the Geometry of Thinking*, 1975 et 1979, sections 620 et 986. P. Wantzel, 1837. Corpus ARC : Volume 1, chapitre 9 ; Volume 2, É 1.12 septies, É 5.44 bis, É 5.44 quater ; Volume 6, É 14.11 bis.
