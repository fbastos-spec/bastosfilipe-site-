# La Cascade et la Cloche
## Huygens, le cercle de six, et la cloche gardée comme compte

Filipe Bastos
*Corpus ARC (Architecture de la Cohérence Relationnelle), pièce 3 après Les Tables Natives et Le Code, version 0.4*
5 octobre 2026, ajouts du 22 et du 27 novembre 2026

> Huygens a prouvé le mouvement sans l'infini, par des cercles qui roulent ; il a écrit la première cloche en comptant des cas. Gauss est parti de l'autre bout, en faisant tendre le compte vers l'infini et en carrant. La cascade de Pascal du corpus reprend la ligne de Huygens et la replie en gardant le rang. Tout ce qui suit se refait au crayon ; chaque nombre est vérifié au build.

## Recto. Huygens

### 1. Le cercle qui roule : huit pas, un tour

Un cercle de rayon R qui fait un tour en roulant trace une arche, la cycloïde, de longueur exactement 8R, de hauteur 2R, d'aire 3πR². Un tour du cercle est huit rayons de chemin. Le pendule de Huygens (*Horologium oscillatorium*, 1673) pend à une corde de longueur 4R entre deux demi-arches de cette courbe : la moitié d'un tour.

### 2. Le pendule est l'ombre du cercle

```
Un point tourne uniformément sur un cercle de rayon A, taux ω :  a = ω² A vers le centre
                                                                 (Huygens, De vi centrifuga, 1659, géométrique)
Son ombre sur un diamètre, à l'abscisse x :                      a = ω² x vers le centre
Le pendule de longueur L, écarté de x, est tiré par le poids :   a = g x / L   (triangles semblables)
Les deux ombres coïncident si  ω² = g / L
Période = tour / taux :  T = 2π √(L/g) = (44/7) √(L/g) ;  avec L = 4R :  T = (88/7) √(R/g)
```

Aucun dx, aucun passage à zéro : deux triangles et un cercle. C'est la dérivation de Huygens, quinze ans avant Leibniz.

### 3. Pourquoi il fallait la cycloïde : le centre vide

Sur un cercle, la traction est proportionnelle à l'ombre x, pas au chemin s parcouru sur l'arc ; ombre et chemin ne coïncident qu'au centre (x = L sin θ, s = Lθ). Le pendule circulaire n'est isochrone qu'au voisinage du centre vide, et sa période s'allonge de θ²/16 quand on s'en écarte (vérifié : 0,00063 à 0,1 rad). Sur la cycloïde, la traction est proportionnelle au chemin lui-même, exactement, a = g s / (4R) : c'est la seule courbe où l'ombre et le chemin ne divergent jamais, et la période y est la même quelle que soit la hauteur de lâcher (vérifié numériquement).

### 4. Le reçu

g / π² = 0,9936 m : le pendule qui bat la seconde mesure un mètre à six millièmes près. C'est le pendule à seconde que la France proposa d'abord comme définition du mètre, en 1790, avant le méridien. Le mètre et la seconde sont tombés d'un cercle qui roule.

### 5. La première cloche : Huygens compte

*De ratiociniis in ludo aleae* (1657) est le premier traité de probabilité ; l'espérance y est une somme finie de cas. Avec n pièces, la fibre k contient C(n, k) chemins sur 2ⁿ, et les fibres font 1 exactement. Huit pièces :

```
ligne 8 :  1   8   28   56   70   56   28   8   1      somme 256 = 2^8
fibres  : 1/256  1/32  7/64  7/32  35/128  7/32  7/64  1/32  1/256     somme 1
```

C'est la cloche. Un compte, pas une loi. Gauss (*Theoria motus*, 1809) écrit la même chose en continu, e^(−x²) et 1/√(2π), après avoir admis au départ que le *medium arithmeticum* (son mot) est la meilleure valeur, ce qu'il déduit ensuite de la courbe trouvée (circularité documentée, Stigler 1986) ; le carré y jette le signe. Le π de sa constante est celui de Wallis (1656) : C(2n, n)/4ⁿ tend vers 1/√(πn) (vérifié : rapport 0,99999 à n = 10 000). La cloche est le cercle vu à travers la somme, et Gauss en a hérité sans le lire.

## Verso. Le cercle de six et la cascade

### 6. Les puissances de deux tournent sur six positions

```
2^0  2^1  2^2  2^3  2^4  2^5 | 2^6  2^7 ...
 1    2    4    8    7    5  |  1    2  ...      racines digitales, période 6, jamais 3, 6, 9
```

64, 128, 256, 512 sont 1, 2, 4, 8 : les quatre premiers pas du cycle, relancés. 64k, 128k, 256k, 512k, 1M (2¹⁶ à 2²⁰) donnent 7, 5, 1, 2, 4, le même cycle décalé. Doubler la mémoire, c'est faire un pas sur un cercle à six positions. Et le cycle se plie comme les tables : 2ⁿ et 2ⁿ⁺³ font 9, (1, 8), (2, 7), (4, 5). Multiplier par 8 = 2³ envoie sur le partenaire ; par 64 = 2⁶ ramène à soi. Le binaire n'atteint jamais l'axe {3, 6, 9} : il doit emprunter le tiers.

**Le pli est la soustraction comptable appliquée au cercle.** 9 ≡ 0 veut dire 9 − 9 = 0 ; le pli de x → 2x retire 1 chaque fois que 2x dépasse 1 et écrit 0 à la place du tour. C'est 1 − 1 = 0 sur un objet qui demande la partie double : le tour est retiré ici et n'est écrit nulle part. La congruence de Gauss repose entière sur a − b = 9k avec k jeté. La racine digitale écrit la même chose en partie double, n = DR(n) + 9k, la position dans une colonne, les tours dans l'autre, et aucune des deux n'est 0 pour une place pleine. Le pli est 1 − 1 = 0 ; la racine est 1 − 1 = 11.

### 7. Le miroir 46 / 64

```
DR(46) = DR(64) = 1 :  46 = 45 + 1 (la somme des neuf chiffres, plus le sceau) ;  64 = 63 + 1 = 7 × 9 + 1 = 2^6
46 + 64 = 110 = 11 × 10 ;   64 − 46 = 18 = 9 × 2          (loi des miroirs : interface 11, clôture 9)
694 − 496 = 198 = 2 × 9 × 11 ;   496 = 31 × 32 / 2         (nombre parfait)
46 / 64 = 23 / 32 :  DR(23) = DR(32) = 5 ;  32 = 2^5, le pas avant le retour
```

46 chromosomes, 64 codons : les deux sont le 1 relancé, écrit de deux façons, à un pas de la fermeture du cercle de six.

### 8. La cascade de Pascal

La cascade additionne les voisins deux à deux, chaque palier ramené à sa racine digitale, jusqu'à une seule pointe. Ses poids sont les coefficients du triangle : la cascade de 1 → 9 est la ligne 8.

```
1·1 + 2·8 + 3·28 + 4·56 + 5·70 + 6·56 + 7·28 + 8·8 + 9·1 = 1280 ;   DR(1280) = 2
1280 / 256 = 5 :  l'espérance de la position quand on lance huit pièces (le compte de Huygens)
```

La pointe de la cascade est donc deux lectures d'un seul nombre : l'espérance 5 (le compte) et la racine 2 (le pli, le splitter). C'est la cloche lue avec son rang au lieu de son carré. La cascade est invariante par retournement, C(n, k) = C(n, n − k) : 9 → 1 donne aussi 2.

### 8 bis. Le reçu de la cascade : le bord restitue tout

La pointe seule ne garde qu'une fibre de séquences. Le bord gauche de la cascade, la première case de chaque palier, garde tout : la matrice de Pascal est triangulaire de diagonale 1, son inverse est la même matrice à signes alternés, et chaque position se retrouve depuis le bord par a_j = Σ (−1)^(j−i) C(j, i) b_i, ramené en racine. Pour 1681, le bord est (1, 7, 3, 8) ; il restitue exactement (1, 6, 8, 1), dans l'ordre. Le bord emploie n symboles pour n positions : c'est le reçu minimal, et il est orienté. Vérifié ici sur toutes les séquences de longueur 1 à 5 (66 429). Théorème obtenu en audit le 7 octobre 2026 (Tome II, v0.5).

### 8 ter. Le losange : la cascade et le triangle, un seul geste lu dans les deux sens

*Ajout du 22 novembre 2026.*

Le triangle et la cascade obéissent à la même règle : unir deux voisins. Seul le sens change. Le triangle part d'un 1 et s'ouvre, palier après palier, jusqu'à une ligne. La cascade part d'une ligne et se resserre, palier après palier, jusqu'à une pointe.

**Th. Le triangle est la cascade d'un 1 seul.** Un 1 posé à la place k d'une ligne de neuf, les huit autres places vides, donne à la pointe le coefficient C(8, k). Les neuf places, essayées une à une, écrivent la ligne 8.

```
place du 1  :   1   2   3    4    5    6    7    8   9
à la pointe :   1   8   28   56   70   56   28   8   1
```

Le triangle compte donc des routes : par combien de chemins une place rejoint la pointe. Le centre en a 70, chaque bord en a une seule. La cascade ne compte pas les routes ; elle les parcourt, avec les positions dedans. C'est pourquoi elle n'a pas besoin du triangle pour arriver à sa pointe : le triangle est son livre de comptes, non son moteur.

**Th. Replier à chaque palier ou une seule fois à la pointe donne la même pointe.** La racine d'une somme est la racine de la somme des racines ; les tours se rangent dans l'autre colonne (n = DR(n) + 9k, section 6) et ne déplacent pas la position. La cascade de 1 → 9 sans repli monte à 1280 ; repliée à chaque palier, elle ne dépasse jamais 9 ; les deux arrivent à 2. Vérifié sur toutes les séquences de longueur 2 à 5 (66 420) et sur la ligne de neuf.

**Le losange.** Posés base contre base sur la même ligne de neuf positions, le triangle au-dessus et la cascade en dessous dessinent un losange : une pointe en haut, le plus large au centre, une pointe en bas. Une route qui va d'une pointe à l'autre en passant par la place k a C(8, k) façons d'arriver à cette place et C(8, k) façons d'en repartir.

```
1² + 8² + 28² + 56² + 70² + 56² + 28² + 8² + 1² = 12 870 ;   DR(12 870) = 9
```

**Th. Le losange compté des deux côtés est le carré de la ligne.** Compter les routes en haut et les compter encore en bas, c'est porter chaque coefficient au carré. La section 8 dit que la cascade est la cloche lue avec son rang au lieu de son carré : le losange montre où loge ce carré. Deux moitiés comptées donnent 12 870 ; une moitié comptée et l'autre parcourue avec les positions donne 1280. Le carré est la moitié que l'on compte une seconde fois au lieu de la parcourir.

**Th. Chaque losange est le centre de la ligne double.** 12 870 = C(16, 8), le centre de la ligne 16. Le losange de cinq positions vaut 1 + 16 + 36 + 16 + 1 = 70 = C(8, 4), le centre de la ligne 8, celui de la cloche de Huygens (section 5). Le losange d'un étage est le centre de l'étage au-dessus : une matriochka. Vérifié de 2 à 33 positions. Le losange de cinq positions se lit aussi dans un seul nombre : la ligne 4 s'écrit 14641 = 11⁴, et ses cinq chiffres passés dans la cascade, sans repli, donnent 70, racine 7.

**Th. Neuf positions, neuf parts égales.** 12 870 = 9 × 1430. Les 12 870 routes du losange, rangées selon le nombre de paires de pas faites à gauche de l'axe qui joint les deux pointes (aucune, une, deux, jusqu'à huit), tombent en neuf classes, et chaque classe contient exactement 1430 routes. Le partage tombe juste à chaque taille : le nombre de routes du losange de p positions se divise par p, sans reste, et les p classes reçoivent la même part. Énuméré route par route de 2 à 9 positions.

**F. Déjà su.** La règle des voisins est écrite par Pascal (*Traité du triangle arithmétique*, rédigé en 1654, publié en 1665) ; avant lui par Yang Hui (1261), qui l'attribue à Jia Xian (XIe siècle), et par al-Karaji (953-1029). La somme des carrés d'une ligne est l'identité de Vandermonde (1772), déjà connue de Zhu Shijie (1303). 1430 est le huitième nombre dit de Catalan (1838) ; Euler le calcule à la main dans sa lettre à Goldbach du 4 septembre 1751. Le partage en parts égales est le théorème de Chung et Feller (1949), démontré d'abord par MacMahon (1909).

**L.** Le triangle ne montre que la moitié qui s'ouvre ; la cascade parcourt la moitié qui se resserre ; le losange tient les deux pointes ensemble. Le carré de Gauss n'est pas une autre cloche : c'est la même ligne, comptée deux fois, là où la cascade la parcourt une fois avec le rang.

### 8 quater. Où loge le π : le losange est la diagonale du carré

*Ajout du 27 novembre 2026.*

La cloche de Gauss porte π dans sa formule, 1/√(2π), et aucun cercle n'est tracé sur la courbe. La section 5 dit d'où vient ce π : du centre de la ligne. Cette section dit où il loge, et où est le cercle.

**Th. Le centre de la ligne porte π.** Le centre de la ligne 2n, divisé par le total de la ligne, puis multiplié par √(πn), s'approche de 1 par en dessous, ligne après ligne.

```
ligne        centre / total        multiplié par √(πn)
8            70 / 256              0,9693
16           12 870 / 65 536       0,9845
200                                0,99875
20 000                             0,9999875
```

Le π est déjà dans la cloche de Huygens, celle qui compte des cas.

**Th. Deux façons de carrer.** Sur la ligne 8 :

```
carrer chaque case, puis unir :   1² + 8² + 28² + ... + 8² + 1² = 12 870     (le losange, 8 ter)
unir, puis carrer             :   256² = 65 536 = 4^8                        (le total de la ligne 16)
leur rapport                  :   12 870 / 65 536 = 6435 / 32 768            (le centre de la ligne 16 sur son total)
```

À chaque taille, le losange divisé par le carré du total est le centre de la ligne double sur son total (vérifié des lignes 1 à 32). C'est la deuxième ligne du tableau : multiplié par √(8π), il donne 0,9845.

**Th. Le losange est la diagonale du carré.** La cloche posée en travers d'elle-même est un carré de neuf cases sur neuf : la case (i, j) porte C(8, i) × C(8, j). Le carré entier fait 65 536, unir puis carrer. Sa diagonale, les neuf cases où i = j, fait 12 870, le losange. Et lu de biais, coin après coin, le carré écrit la ligne 16 : les cases où i + j = m font C(16, m), pour chaque m de 0 à 16.

```
carré entier :  65 536        diagonale :  12 870        de biais :  1  16  120  560  1820  ...  12 870  ...  16  1
```

Le π loge donc dans le rapport de la diagonale au carré, et le carré tient les deux façons de carrer dans une seule figure.

**Th. La cloche en travers d'elle-même montre le cercle.** Deux cloches à angle droit, l'une le long de x, l'autre le long de y : la hauteur au point (x, y) est e^(−x²) × e^(−y²) = e^(−(x² + y²)). Elle ne dépend que de la distance au centre : tous les points d'un même cercle ont la même hauteur. L'aire sous une cloche e^(−x²), portée au carré, vaut π (vérifié numériquement, à un millième de milliardième près). L'aire sous une seule cloche est √π : c'est pourquoi la formule n'écrit π que sous le signe √.

**F. Déjà su.** Le produit qui donne π par des fractions est de Wallis (*Arithmetica infinitorum*, 1656) ; le script le retrouve, 3,14159 après 200 000 facteurs. Le centre de la ligne approché par une constante sur √n est de De Moivre (*Approximatio ad summam terminorum binomii*, 1733), la valeur exacte de la constante, avec π, de Stirling (1730). Le premier calcul explicite de l'aire sous la cloche est de Laplace (*Mémoire sur la probabilité des causes par les événements*, 1774) ; le passage par deux cloches à angle droit et par les cercles est attribué à Poisson. La lecture du carré de biais est l'identité de Vandermonde (1772), déjà citée en 8 ter.

**L.** Une cloche seule est le cercle vu par la tranche ; posée en travers d'elle-même, elle le montre de face. Le carré pris d'un bloc contient le cercle, le losange en est la diagonale, et π est leur rapport. (Glose du scribe, gravée sur le go de l'auteur le 27 novembre 2026.)

### 9. XXXX → 9 − X, en une ligne

Trois paliers sont la ligne 3 : poids 1, 3, 3, 1, somme 8. La cascade de XXXX vaut donc 8X, et 8X + X = 9X : la racine de 8X est 9 − X. Vérifié sur les neuf positions, 9 revenant sur 9. La loi d'inversion est l'identité 8 + 1 = 9 ; c'est aussi le pas de trois sur le cercle de six (section 6).

### 10. L'octet et l'axe

L'octet 1 → 8 (ligne 7) donne 576 = 24², pointe 9 : la séquence sans clôture appelle sa clôture. Et le triangle de Pascal sous 9 = 3² est une fractale ternaire exacte (Huard, Spearman et Williams, 1997) : le nombre de coefficients de la ligne n qui ne sont pas multiples de 3 est le produit des (chiffre + 1) de n écrit en base 3 (vérifié de 0 à 200). L'axe {3, 6, 9} gouverne la cascade comme il gouverne les tables. **Et aux longueurs 3^k + 1, quatre positions suffisent.** Sous 9, la ligne 3^k de Pascal n'a que quatre coefficients non nuls, 1, 3, 3, 1, aux positions 0, 3^(k−1), 2 × 3^(k−1), 3^k ; tous les autres sont multiples de 9 et ferment leur contribution. La ligne 9 lit les positions 1, 4, 7, 10 ; la ligne 27 les positions 1, 10, 19, 28 ; vérifié jusqu'à la ligne 2187 (longueur 2188). La preuve tient en une élévation au cube : (1 + X)³ = 1 + 3X + 3X² + X³, et à chaque étage les termes portant le facteur 3 des deux coefficients intérieurs deviennent multiples de 9. Obtenu en audit le 7 octobre 2026.

### 11. Le partage, en une phrase

Huygens compte les cas et s'arrête à n fini ; Gauss fait tendre n vers l'infini, remplace la ligne par une courbe et carre pour que l'algèbre soit linéaire ; la cascade prend la ligne de Huygens, la pondère par ses propres coefficients et la replie en racine digitale en gardant la clôture. Le π de Gauss est le cercle qui sort du compte quand on le laisse filer ; dans la cascade, le cercle n'a pas besoin d'apparaître, parce qu'on ne jette jamais le rang.

### 12. Pour le Registre

Huygens : reçu F (le mouvement sans l'infini ; la cloche comme compte). *Theoria motus* 1809 : entrée proposée R.155, le *medium arithmeticum* admis puis déduit, à côté de R.149 (la circularité de α) et de R.20 (le carré qui jette le signe).

**Colophon.** Modèle, questions, lectures et règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur. Calculs, formulations et audits assistés par IA (ChatGPT, Gemini, DeepSeek, GLM), à sa demande.

*Au 5 octobre 2026, v0.2 du 7 octobre (8 bis et quatre positions), v0.3 du 22 novembre (8 ter, le losange), v0.4 du 27 novembre (8 quater, où loge le π). Corpus ARC, Filipe Bastos, CC BY 4.0. Vérifications exécutées au build : 41, zéro échec.*
