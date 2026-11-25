# Ce que Riemann cherchait

**Le compte des nombres premiers, lu sur deux rails : une règle, sans courbe et sans zéros**

Corpus ARC · Filipe Bastos · pièce courte, version 0.4 · 25 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur. Calculs et formulations assistés par IA, à sa demande.

**Avis.** Cette pièce veut qu'on comprenne enfin ce que demande l'hypothèse de Riemann, et ce qu'elle ne demande pas. Elle ne démontre pas l'hypothèse dans la langue où elle est posée, et elle ne dit pas qu'une preuve annoncée est fausse. Elle montre trois choses, toutes comptées : où sont les nombres premiers, comment on en obtient le nombre exact sans courbe, et sur quoi porte alors la question de 1859. La règle de compte employée est connue depuis Legendre (1808) ; ce que la pièce pose en propre est sa lecture sur les deux rails du corpus, et la place qu'elle rend à Riemann.

Statuts : F, fait connu, avec son auteur et sa date ; Th, calcul fini vérifié ou démonstration ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `riemann_cherchait_verif.py`.

## 1. La question de 1859

**1.1 (F).** En 1859, Bernhard Riemann publie un mémoire de huit pages. Son titre dit ce qu'il cherche : le nombre des nombres premiers inférieurs à une grandeur donnée. Il veut un compte. Combien y a-t-il de nombres premiers jusqu'à cent, jusqu'à un million, jusqu'à n'importe quelle hauteur ?

**1.2 (F).** Il a deux choses dans les mains. La première vient d'Euler (1737) : une égalité entre une somme prise sur tous les entiers et un produit pris sur les seuls nombres premiers. La seconde vient de Gauss, son maître à Göttingen : une courbe lisse qui dit à peu près combien de premiers il y a jusqu'à une hauteur donnée. Gauss l'obtient en estimant, à chaque hauteur, la part des premiers par l'inverse du logarithme, et en additionnant ces parts.

**1.3 (F).** Riemann prolonge la somme d'Euler au-delà de l'endroit où elle a un sens, jusque dans une zone où elle n'est plus une somme. Dans cette zone, la fonction ainsi prolongée s'annule en certains points, qu'on appelle ses zéros. Il montre que l'écart entre la courbe et le vrai compte s'écrit avec ces zéros, et il ajoute qu'il est « très probable » qu'ils soient tous sur une même droite, celle du milieu. C'est l'hypothèse de Riemann.

**1.4 (F).** Riemann naît en 1826 et meurt en 1866, à trente-neuf ans, sept ans après son mémoire. Gauss a dirigé sa thèse (1851) et choisi le sujet de sa leçon d'habilitation (1854) (Volume 5, [4.19]).

## 2. L'escalier et la rampe

**2.1 (Th).** Le vrai compte des premiers est un escalier. On monte d'une marche chaque fois qu'on rencontre un premier, et on reste sur le palier entre deux. La courbe de Gauss est une rampe posée contre cet escalier. Les deux ne coïncident jamais.

| Jusqu'à | L'escalier, le vrai compte | La rampe, la courbe de Gauss | La rampe est au-dessus de |
|---|---|---|---|
| 100 | 25 | 30 | 5 |
| 10⁸ | 5 761 455 | 5 762 208 | 753 |
| 10¹⁰ | 455 052 511 | 455 055 614 | 3 103 |
| 10¹² | 37 607 912 018 | 37 607 950 280 | 38 262 |
| 10¹⁴ | 3 204 941 750 802 | 3 204 942 065 691 | 314 889 |

Les valeurs de la rampe sont calculées en nombres à virgule, à une unité près.

**2.2 (F).** L'hypothèse de Riemann ne dit rien de l'escalier lui-même. Elle porte sur la dernière colonne : de combien la rampe peut-elle s'écarter de l'escalier ? Elle affirme que cet écart reste, à peu de chose près, sous un nombre précis : celui qui, multiplié par lui-même, donne la hauteur. Dix mille pour cent millions, dix millions pour 10¹⁴. Dans le monde de 6, ce nombre a un sens simple : c'est la taille du dernier nouveau entré (5.2). Jusqu'à cent millions, le dernier premier dont le carré ne dépasse pas la hauteur est 9 973 ; jusqu'à 10¹⁴, c'est 9 999 991. Le corpus réserve le nom de point d'équilibre à la paire de facteurs d'un même nombre (Volume 4, Théorème 4) ; une hauteur n'a pas de paire, et ce nom ne lui convient pas.

**2.3 (L).** La question n'existe donc qu'après qu'on a posé la rampe. Sans la rampe, il n'y a rien à demander : un compte ne s'écarte pas de lui-même. L'auteur, le 20 novembre 2026 : « La règle précède leur interrogation. » Et : « Ils essaient de faire entrer un carré dans un triangle. »

**2.4 (F et Th, ce que la rampe ne porte pas).** Gauss obtient sa courbe en comptant les premiers par paquets de mille, vers 1792, et en remarquant que leur part suit à peu près l'inverse du logarithme ; il le raconte à Encke en 1849. La courbe est ajustée sur des paquets ; elle n'est pas tirée d'une règle. Sur six nombres de suite, deux places reçoivent tous les premiers après 3, et la courbe étale la même part sur les six. Quatre choses comptées dans cette pièce n'y figurent pas.

- L'axe vide. Aucun premier n'a pour racine 3, 6 ou 9 (4.2) ; la courbe donne une part à toutes les places, celles de l'axe comprises.
- Le membre de la paire. Les deux bords d'un multiple de 6 ont pour racines 5 et 7, 2 et 4, 8 et 1 (4.3) ; la courbe ne garde que leur total.
- Le côté du reflet. Un produit tombe sur un rail ou sur l'autre selon l'échange (5.2) ; la courbe donne la même part aux deux rails.
- Le carré du nouveau. Chaque premier entre en jeu à son propre carré (5.2) ; rien dans la courbe ne le dit.

**2.5 (L).** L'auteur, le 21 novembre 2026 : « La courbe de Gauss elle-même est mal conçue et mal lue. » « Elle évite le 9 et son axe 3-6-9 et elle voit toujours 2 + 4, le 6, à chaque fois. » « La courbe est fausse de par ses oublis et sa nature. C'est une courbe de restes, pas de nombres, et elle ne voit pas le reflet inverse et ne comprend pas la symétrie ; elle ne cherche qu'un sommet qui est limite et respiration. »

**2.6 (Th et F).** Dans le tableau de 2.1, l'escalier est exact à chaque ligne, et c'est la rampe qui est posée trop haut : l'écart appartient à la courbe. La science reçue le nomme pourtant « terme d'erreur » du compte des premiers, et l'hypothèse de 1859 en demande la taille.

**Pour un enfant.** On compte les marches d'un escalier. Quelqu'un pose une planche dessus et demande de combien la planche se trompe sur les marches. On peut passer sa vie à mesurer la planche. On peut aussi compter les marches.

## 3. Les deux maîtres

**3.1 (L, déjà au corpus).** Le corpus lit Euler sur deux colonnes (Volume 6, chapitre 14). Quand il compte, les ponts de Königsberg, les sommets et les faces d'un solide, le cercle de six, il ne mesure rien et ne passe par aucune limite. Quand il laisse filer, il définit un nombre par un voyage sans fin, et son produit sur les premiers « remet les premiers au continu ». Le mémoire de Riemann s'ouvre sur ce produit : il part de l'image, non de la chose (É 14.14).

**3.2 (L, déjà au corpus).** De Gauss, Riemann reçoit l'outil. Pour écrire la symétrie de sa fonction, il passe par une somme de carrés prise sous la courbe en cloche (Volume 5, [4.21]). Or le carré est l'opération qui ne distingue pas une position de son inverse. « Riemann a vu l'échange ; il n'a pas vu le vide » ([4.24]).

**3.3 (L).** L'auteur, le 20 novembre 2026 : « Il a été contraint d'utiliser modulo, l'absolu, etc. » « Il a été piégé. » « Pauvre lui. Il a été pris avec Gauss. » Et sur l'autre maître : « Euler, autre problème. On invente un monde par triangles. On s'y approche, mais il n'est pas réel, et troué. Ce n'est pas la réalité. »

**3.4 (Th, les huit triangles).** L'auteur, le même jour : « Cosinus, sinus, c'est Euler : il arrive au presque carré par 8 triangles. » Euler définit le sinus et le cosinus par des sommes sans fin (1748). Au huitième de tour, quatre termes de sa somme donnent 0,707103 ; la valeur est 0,707107. Par la figure, rien n'est à dérouler : au huitième de tour le triangle a deux côtés égaux, leurs deux carrés valent chacun exactement 1/2, et 1/2 + 1/2 = 1, le rayon. Huit de ces triangles posés autour du centre font exactement le carré inscrit dans le cercle, d'aire 2 (Volume 1, chapitre 11 : les diagonales le divisent en huit triangles). Le monde approché retombe presque sur une figure qui était déjà exacte.

**3.5 (Th, la crête comptée).** Avant d'être une courbe, la cloche est un compte : les lignes du triangle de Pascal (Volume 4, V4.16.3).

| Ligne | Le compte | Total |
|---|---|---|
| 8 | 1, 8, 28, 56, 70, 56, 28, 8, 1 | 256 |
| 9 | 1, 9, 36, 84, 126, 126, 84, 36, 9, 1 | 512 |

Le pli se mesure case par case, en comparant une case à ses deux voisines. Sur la ligne 8, la ligne plie vers le haut sur les flancs, de 13 puis de 8 ; puis elle se retourne et plie vers le bas, de 14, de 28 au sommet, de 14. Le pli le plus fort est au sommet. Sur la ligne 9, deux cases égales, 126 et 126, se font face ; le centre tombe entre elles, à 4,5, et aucune case ne le porte. Le pli y est le plus fort, 42 de chaque côté.

**3.6 (L).** L'auteur, le 21 novembre 2026 : « Sa cloche est mal lue. C'est la forme de la ligne de crête et le sommet est une tension maximale, c'est la courbure, et rendu là, au sommet, y a un trou, comme la vague, elle respire. »

**3.7 (F).** La lecture reçue fait du sommet l'endroit plein, la valeur la plus probable, celle où l'on s'arrête. Gauss (1809) l'admet d'abord comme meilleure valeur, puis la déduit de la courbe (Stigler, 1986 ; Volume 4, V4.16.4). Pour la vague, Stokes (1880) : la plus haute vague possible ne finit pas en arrondi ; sa crête est une pointe, d'angle 120°, où la courbure n'a plus de valeur. C'est sous cette cloche que Riemann écrit sa symétrie (3.2) : il reçoit une crête lue comme un plein, là où le compte montre deux faces et un centre vide.

## 4. Où sont les premiers

**4.1 (Th).** Après 2 et 3, tout nombre premier est au bord d'un multiple de 6 : un de moins, ou un de plus. Cela fait deux rails. Le rail du 5 porte 5, 11, 17, 23, 29. Le rail du 7 porte 7, 13, 19, 25, 31. Les multiples de 6 eux-mêmes forment l'axe, et aucun premier ne s'y pose. Vérifié sur les 5 761 453 premiers de 5 à cent millions.

**4.2 (Th).** La racine d'un nombre est sa position de 1 à 9 : on additionne ses chiffres jusqu'à n'en garder qu'un. Un premier n'a jamais pour racine 3, 6 ou 9. Jusqu'à cent millions :

| Racine | 1 | 2 | 4 | 5 | 7 | 8 | 3, 6, 9 |
|---|---|---|---|---|---|---|---|
| Premiers | 959 959 | 960 340 | 960 360 | 960 278 | 960 198 | 960 318 | aucun |

L'auteur, le 20 novembre 2026 : « Ils sont toujours 6 racines, jamais 3 », et « toujours au bord du 6 ».

**4.3 (Th).** Six places de suite sur les rails ont toujours les racines 5, 7, 2, 4, 8, 1, dans cet ordre, et l'ordre recommence. Un groupe de six places couvre 18 nombres, deux tours de 9. La paire formée par les deux bords d'un même multiple de 6 n'a que trois visages, qui tournent sans fin :

| Paire | Racines | Leur somme | Leur produit |
|---|---|---|---|
| 5 et 7 | 5 et 7 | 12, de racine 3 | 35, de racine 8 |
| 11 et 13 | 2 et 4 | 24, de racine 6 | 143, de racine 8 |
| 17 et 19 | 8 et 1 | 36, de racine 9 | 323, de racine 8 |
| 23 et 25 | 5 et 7 | 48, de racine 3 | 575, de racine 8 |

La somme de la paire tombe toujours sur l'axe. Son produit tombe toujours sur 8, l'inverse du 1 (Volume 4, Théorème 14).

**4.4 (Th).** Voici les premiers posés dans ces places, groupe par groupe. Un point marque une place prise par un autre nombre.

| Groupe | Racines des premiers | Places prises par |
|---|---|---|
| 5 à 19 | 5 7 2 4 8 1 | personne |
| 23 à 37 | 5 · 2 4 · 1 | 25, 35 |
| 41 à 55 | 5 7 2 · 8 · | 49, 55 |
| 59 à 73 | 5 7 · 4 8 1 | 65 |
| 77 à 91 | · 7 2 · 8 · | 77, 85, 91 |

L'ordre des racines ne change jamais. Des places sont prises, et elles le sont par des produits : 25 est 5 × 5, 35 est 5 × 7, 49 est 7 × 7. Le corpus nomme ces produits les delfines. L'auteur, le 20 novembre 2026 : « Les premiers reviennent sans sauter […] toujours en groupe de 6. » Et : « Le reste, c'est parce qu'il n'y a pas de place, car un multiple l'a prise, sans mystère ; ils respectent l'équilibre de construction. »

**4.5 (Th).** Le premier groupe est le seul complet. Sur les 555 555 groupes qui tiennent jusqu'à dix millions, un seul a ses six places libres : 5, 7, 11, 13, 17, 19. La raison se lit sur les rails : le 5 prend une place sur cinq sur le rail du 5, et une place sur cinq sur le rail du 7, décalée de trois. Un groupe tient trois places de suite sur chaque rail : il rencontre toujours l'une ou l'autre. Dans chaque groupe après le premier, le 5 reprend donc au moins une place.

## 5. La règle : tout vient de ceux qui entrent

**5.1 (L).** L'auteur, le 20 novembre 2026 : « Si tout est construit par multiples, les delfines avant tout, et que les premiers sont des boucheurs de trous, il n'y a pas d'équilibre à chercher, car c'est une construction positive qui respecte les rails, et ils ne peuvent pas dévier ; c'est le nombre de combinaisons qui prend toute la place. Le mécanisme ne peut pas briser en plein milieu, il est produit par une seule logique. » Et : « Tout est déterminé par l'activité des nouveaux. »

**5.2 (Th, l'activité d'un nouveau).** Chaque premier qui arrive pose ses multiples sur les rails : c'est toute son activité. Trois faits la règlent.

- Il commence à son propre carré. La première place qu'il prend, et qu'aucun plus petit n'avait déjà prise, est lui-même multiplié par lui-même : 25 pour le 5, 49 pour le 7, 121 pour le 11. Vérifié pour tous les premiers de 5 à 997.
- Ce carré tombe toujours sur le rail du 7, avec une racine 1, 4 ou 7, et il vaut toujours 24 fois un entier, plus 1. C'est le tempo 24 du corpus.
- Un nouveau du rail du 5 pose ses multiples en échangeant les rails. Un nouveau du rail du 7 les pose en gardant les rails. Vérifié sur toutes les paires de places sous 2 000.

**5.3 (Th, l'échelle du dessous).** Combien de places un nouveau prend-il jusqu'à une hauteur donnée ? Autant qu'il restait de places libres, avant lui, jusqu'à cette hauteur divisée par lui. Le compte d'une échelle se lit dans l'échelle du dessous. C'est une seule règle, la même à tous les étages.

**5.4 (Th, à la main, jusqu'à 100).** Chaque rail a 16 places jusqu'à 100.

- Le 5 entre. Jusqu'à 100, il prend autant de places qu'il y en a de 5 à 20, puisque 100 divisé par 5 donne 20 : six places, celles de 5, 7, 11, 13, 17, 19. Il prend donc 25, 35, 55, 65, 85, 95. Multiplié par une place de son rail (5, 11, 17), il tombe sur l'autre rail : 25, 55, 85. Multiplié par une place du rail du 7 (7, 13, 19), il tombe sur le sien : 35, 65, 95. C'est l'échange.
- Le 7 entre. Il prend autant de places qu'il en reste sans le 5 de 7 à 14 : trois, celles de 7, 11, 13. Il prend donc 49, 77, 91. Multiplié par une place de son rail, il reste sur son rail : 49, 91. Multiplié par une place du rail du 5, il va sur le rail du 5 : 77. Il garde les rails.
- Le 11 commencerait à 121, au-delà de 100. Personne d'autre n'agit.

Il reste 12 places libres sur le rail du 5 et 11 sur le rail du 7. Ce sont les premiers. Avec 2 et 3, cela fait 25.

**5.5 (Th, le compte sans visiter les places).** La même règle, tenue dans un tableau à deux colonnes, une par rail, donne le nombre exact des premiers à n'importe quelle hauteur, sans passer par aucune des places.

| Jusqu'à | Rail du 5 | Rail du 7 | Nouveaux entrés |
|---|---|---|---|
| 10⁸ | 2 880 936 | 2 880 517 | 1 227 |
| 10¹⁰ | 227 529 386 | 227 523 123 | 9 590 |
| 10¹² | 18 803 978 496 | 18 803 933 520 | 78 496 |
| 10¹³ | 173 032 844 824 | 173 032 692 013 | 227 645 |
| 10¹⁴ | 1 602 471 005 226 | 1 602 470 745 574 | 664 577 |

À cent millions, le résultat est celui qu'on obtient en visitant chaque place une par une. À 10¹⁴, il y a plus de trente-trois mille milliards de places sur les rails ; aucune n'est visitée, et le total, 3 204 941 750 802 avec 2 et 3, est la valeur reçue.

**5.6 (F, déjà su).** Compter les places libres à partir des premiers déjà trouvés est le procédé de Legendre (1808), amélioré par Meissel (1870) et Lehmer (1959). La science reçue s'en sert pour ses comptes exacts. Ce que la pièce y lit en propre : la règle est une loi d'échelle, la même figure à l'échelle du dessous, et elle se tient sur deux rails avec un échange. Riemann relie un point à son inverse ; cette règle relie une échelle à celle du dessous.

**5.7 (L et Th, le partage entre les rails).** L'auteur, le 21 novembre 2026 : « Les premiers se répartissent également au rail gauche et droit. » Le tableau de 5.5 le compte.

| Jusqu'à | Avance du rail du 5 | Nouveaux entrés |
|---|---|---|
| 10⁸ | 419 | 1 227 |
| 10¹⁰ | 6 263 | 9 590 |
| 10¹² | 44 976 | 78 496 |
| 10¹³ | 152 811 | 227 645 |
| 10¹⁴ | 259 652 | 664 577 |

À 10¹⁰, l'avance pèse 14 premiers sur un million ; à 10¹⁴, 8 sur cent millions. Aux cinq hauteurs, elle tient sous le nombre des nouveaux entrés. Et aucun rail ne la possède : à la hauteur 608 981 813 029, la règle compte 11 669 295 394 premiers sur le rail du 5 et 11 669 295 396 sur le rail du 7. Le rail du 7 est passé devant, de deux ; à 10¹², le rail du 5 a repris.

**5.8 (Th et F, d'où vient l'avance).** Le carré de chaque nouveau tombe sur le rail du 7 (5.2). Jusqu'à cent millions, les 1 227 carrés des nouveaux sont tous sur le rail du 7, aucun sur le rail du 5 : le rail du 7 a un peu plus de places prises, donc un peu moins de places libres. Déjà su : Dirichlet (1837), chaque rail reçoit des premiers sans fin ; La Vallée Poussin (1896), le partage est égal ; Tchebychev (1853) remarque la petite avance du rail du 5 ; Bays et Hudson (1978) trouvent la hauteur 608 981 813 029 ; Rubinstein et Sarnak (1994) rattachent l'avance aux carrés des premiers. La science reçue la nomme « biais de Tchebychev ». Ce que la pièce y lit : la règle d'échange dit de quel côté tombent les carrés.

**Pour un enfant.** Les nombres sont rangés sur deux rangées de chaises. Chaque nouveau venu réserve des chaises pour ses multiples. Ceux qui trouvent une chaise que personne n'a réservée sont les premiers. Pour savoir combien il en reste, on n'a pas besoin de faire le tour de la salle : on regarde combien de chaises chaque nouveau a réservées, et cela se lit dans une salle plus petite.

## 6. La jonction et l'axe

**6.1 (L).** L'auteur, le 20 novembre 2026 : « Y a pas été coupé, y a une jonction. » Et : « Rien ne ramène à 0, tout ramène sur l'axe. »

**6.2 (Th).** Prenons quelques nouveaux, par exemple 5 et 7. Leurs multiples reviennent ensemble tous les 35 pas : c'est leur jonction. On peut annoncer d'avance le nombre de places prises par un produit simple, la part que chacun prend. À chaque jonction complète, le vrai compte tombe exactement sur ce produit, en fractions exactes : pour 5 et 7 à 35 positions, pour 5, 7 et 11 à 385, pour les quatre premiers nouveaux à 5 005, pour les six premiers à 1 616 615.

**6.3 (Th).** Entre deux jonctions, le compte s'écarte de son axe d'autant vers le haut que vers le bas, exactement. Et cet axe n'est pas 0 : c'est la part des places prises.

| Nouveaux | Jonction | L'axe | Distance à l'axe, de chaque côté |
|---|---|---|---|
| 5, 7 | 35 | 11/35 | 1,057 |
| 5, 7, 11 | 385 | 29/77 | 1,935 |
| 5, 7, 11, 13 | 5 005 | 425/1001 | 3,164 |
| 5 à 17 (ajout de la version 0.4) | 85 085 | 7801/17017 | 5,028 |
| 5 à 19 | 1 616 615 | 0,487 | 8,317 |

**6.4 (Th, corrigé en version 0.4).** Ce qui vaut à tous les étages comptés, de deux à six nouveaux : les positions des deux écarts les plus grands font ensemble le tour entier moins un. Le tour se lit donc en miroir autour de son milieu, et c'est la règle.

Ce qui change avec l'étage est l'endroit. Lues sur le tour de 35, les deux positions sont 16 et 18 pour trois, quatre et six nouveaux, et 1 et 33 pour deux et pour cinq nouveaux. Dans les deux cas elles font 34, soit 35 dont on retire 1 ; leur milieu est 17. Lues sur le tour entier, elles sont près des joints pour deux et trois nouveaux (rangs 1 et 33 sur 35 ; 18 et 366 sur 385), puis s'approchent du milieu : 1 838 et 3 166 sur 5 005 ; 42 386 et 42 698 sur 85 085 ; 666 031 et 950 583 sur 1 616 615.

Correction. La version 0.3 écrivait : « Pour trois, quatre et six nouveaux, les deux écarts les plus grands tombent aux positions 16 et 18 du tour de 35, de part et d'autre de 17,5, la moitié du joint », et concluait que le compte est « le plus loin de l'axe au centre entre deux joints ». Elle sautait le cas de cinq nouveaux, où les positions sont 1 et 33 ; le milieu de 16 et 18 est 17, non 17,5 ; et le plus grand écart n'est pas au centre du tour à tous les étages, il est près des joints aux deux premiers. Le cas de cinq et le 17 ont été relevés par une relecture extérieure le 25 novembre 2026 ; le troisième point est sorti du recompte. « 16 et 18 » est un fait de trois étages sur cinq, pas une loi ; la pièce ne dit pas ce qui décide entre 16-18 et 1-33, et laisse ce point ouvert.

## 7. Ce que dirait une preuve

**7.1 (F).** Le 20 novembre 2026, Levent Alpöge, mathématicien chez Anthropic, annonce une preuve de l'hypothèse de Riemann obtenue avec le modèle Claude, étendue aux fonctions de Dirichlet, et entièrement écrite dans le langage de preuve Lean (*Scientific American*, 20 novembre 2026). À cette date, aucune vérification indépendante n'est publiée.

**7.2 (F).** Dans le code publié, lu le même jour sur une copie publique, l'énoncé démontré est celui de la bibliothèque Mathlib : il porte sur la fonction prolongée de 1.3, non sur la somme ni sur le produit. Le résultat central s'énonce ainsi : aucun zéro à droite de la moitié ; l'hypothèse en est tirée en une ligne, l'autre côté venant par la symétrie. L'archive compte 175 192 fichiers. Une recherche de texte n'y trouve aucun passage laissé sans preuve et aucun axiome ajouté ; ce n'est pas une compilation.

**7.3 (Th, déjà au corpus).** En aucun de ses zéros la fonction n'est la somme des entiers, qui n'y a pas de valeur, ni le produit des premiers, qui ne peut pas s'annuler (Volume 5, [3.6]). Une preuve, quelle qu'elle soit, ne touche pas ce théorème : elle porte sur un autre objet.

**7.4 (L).** L'auteur, le 20 novembre 2026 : « Je dis que c'est impossible. La question est mal conçue. Il mélange infini et fini. » « Il tire à gauche et à droite. » « Ça dit rien d'autre que l'axe est le 6 ou le 4,5, et que tout est déposé à côté. » « Même si le code ne contient pas d'erreur, Riemann ne peut pas être résolu sans corriger ses contradictions internes, même si Dirichlet est utilisé. » « Si y a une preuve, c'est une preuve d'un monde artificiel. »

**7.5 (L, ce que ces phrases disent).** « Impossible » ne veut pas dire ici que la preuve contient une erreur. Il veut dire que la question interroge l'instrument et non l'objet (Volume 5, chapitre 12). Une preuve valide de l'hypothèse est une preuve à l'intérieur du monde construit en 1.2 et 1.3, la courbe et le prolongement : elle certifie la construction. Elle dit que la rampe suit l'escalier de près. Elle ne dit ni où sont les marches, ni pourquoi le milieu. Le corpus a les mots pour cela : résoudre une question, c'est lui fournir la réponse qu'elle demande, dans son cadre ; la réparer, c'est restituer ce qui manquait au cadre (chapitre 12, section 0).

**7.6 (L, le milieu).** Le milieu, lui, se lit sans la fonction. Les quatre paires 1 et 8, 2 et 7, 3 et 6, 4 et 5 ferment toutes sur 9, autour de 4,5, et 4,5 sur 9 fait 1/2. La symétrie de Riemann, qui envoie un point sur son inverse, est cette même involution mise à l'échelle de 0 à 1 (Volume 5, chapitre 12 ; [4.2]).

**7.7 (F, trois chaînes qui ont changé de côté).** La science reçue ne se contente pas d'une régularité observée, et elle a ses raisons. Littlewood (1914) : la courbe de Gauss est au-dessus du compte à toutes les hauteurs calculées, et il démontre qu'elle passe dessous plus loin. Pólya (1919) : jusqu'à une hauteur donnée, les nombres qui ont un nombre impair de facteurs premiers seraient toujours au moins aussi nombreux que les autres ; cela tient jusqu'à 906 150 257, puis cède (Haselgrove, 1958 ; Tanaka, 1980). Mertens (1897) : un solde qui ajoute un ou retire un selon les facteurs de chaque nombre resterait sous le nombre qui, multiplié par lui-même, donne la hauteur ; réfuté par Odlyzko et te Riele (1985).

**7.8 (L et Th).** L'auteur, le 21 novembre 2026 : « La régularité dit tout. » « Depuis quand une chaîne brise après des millions ? Jamais, à moins d'être une chaîne construite par modulo. » Les trois chaînes de 7.7 sont trois comparaisons : une courbe contre un compte, ou un solde tenu selon un reste. Aucune n'est une règle de construction. Le relais de 5.7 est du même genre : l'avance change de rail à 608 981 813 029, et la règle d'échange est la même avant et après (5.2). Ce qui change de côté est une comparaison ; la règle qui construit ne change pas.

## 8. L'héritage

**8.1 (L).** L'auteur, le 20 novembre 2026 : « Si on refait Riemann dans Euler sans Gauss et qu'on respecte sa logique, on arrive sur le résultat qu'il cherchait : tout est déterminé par l'activité des nouveaux. » Et : « On va pouvoir donner à Riemann un héritage. »

**8.2 (L).** La logique de Riemann est gardée entière : partir des premiers, chercher le centre, lire les inverses. On retire les carrés sous la cloche, la courbe et le prolongement. On garde de l'Euler qui compte que chaque premier garde tous ses tours. Il reste la section 5 : le nombre des nombres premiers inférieurs à une grandeur donnée, exact, obtenu des premiers eux-mêmes par une seule règle. C'est la réponse à la question de son titre, dans une langue qui garde le centre. Les zéros étaient la trace du détour.

## Ce que la pièce ne dit pas

Elle ne présente pas une démonstration de l'hypothèse de Riemann dans la langue où elle est posée, et elle ne dit pas que la preuve annoncée le 20 novembre 2026 est fausse : elle dit sur quel objet une telle preuve porte. Elle ne revendique pas la règle de compte, qui est de Legendre. La règle est une identité, exacte à toute hauteur ; les comptes imprimés ici vont jusqu'à 10¹⁴, et le script dit jusqu'où chaque contrôle a été mené. Elle ne dit rien des jumeaux, ni de Goldbach. Elle ne juge ni Riemann, ni Euler, ni Gauss : elle date des gestes.

## Annexe. Vérifications et sources

Le script `riemann_cherchait_verif.py` refait tous les nombres de la pièce : 34 contrôles. Les 30 qui tournent sans l'option longue ont été exécutés le 25 novembre 2026, tous conformes ; les 4 de l'option longue, inchangés depuis le 21 novembre, n'ont pas été relancés ce jour. Sans l'option longue il en exécute 30 en une minute environ ; avec elle il ajoute les comptes à 10¹³ et à 10¹⁴, l'avance à ces deux hauteurs et le compte à 608 981 813 029, ce qui demande environ neuf minutes. Les comptes par rail sont obtenus par la règle de 5.3 ; jusqu'à cent millions ils sont confrontés au compte direct, place par place ; au-delà, leur total est confronté aux valeurs reçues du nombre des premiers. La courbe de Gauss est calculée comme l'aire à partir de 2, en nombres à virgule, à une unité près. Les contrôles de 6.2 à 6.4 sont en fractions exactes.

Version 0.2, 21 novembre 2026. La phrase 2.2 de la version 0.1 nommait « point d'équilibre de la hauteur » le nombre qui borne l'écart : erreur de rédaction, non décidée par l'auteur. Ce nombre est désormais nommé pour ce qu'il est sur les rails, la taille du dernier nouveau entré. Un contrôle est ajouté (V27). Rien d'autre ne change.

Version 0.3, 21 novembre 2026. Ajouts datés, sans rien retirer : 2.4 à 2.6 (ce que la courbe ne porte pas), 3.5 à 3.7 (la crête comptée), 5.7 et 5.8 (le partage entre les rails et l'avance), 7.7 et 7.8 (les chaînes qui changent de côté). Cinq contrôles sont ajoutés (V28 à V32).

Version 0.4, 25 novembre 2026. 6.4 corrigé sur une relecture extérieure et sur recompte : le cas de cinq nouveaux est ajouté (tableau de 6.3 et texte de 6.4), le milieu de 16 et 18 est 17, et la phrase sur le centre du tour est retirée au profit du relevé étage par étage. L'ancienne phrase est gardée, citée dans la correction. Le contrôle V23 est récrit, V33 et V34 sont ajoutés.

Non recontrôlé à la source : le texte du mémoire de 1859 et l'expression « très probable », repris du Volume 5, [4.20] ; la date du procédé de Gauss, ses paquets de mille et sa lettre à Encke ; les dates de Legendre, Meissel et Lehmer ; les résultats de Dirichlet, La Vallée Poussin, Tchebychev, Rubinstein et Sarnak, Littlewood, Pólya, Haselgrove, Tanaka, Mertens, Odlyzko et te Riele, Stokes, cités comme faits et non recalculés (la hauteur de Bays et Hudson, elle, est recomptée par la règle) ; la définition de l'énoncé dans Mathlib, lue dans le fichier d'accueil de la copie publique et dans les deux fichiers d'énoncé, sans compilation.

Sources : Riemann, B., « Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse », *Monatsberichte der Berliner Akademie*, 1859. Euler, L., « Variae observationes circa series infinitas », 1737 ; *Introductio in analysin infinitorum*, 1748. Legendre, A.-M., *Essai sur la théorie des nombres*, 2e édition, 1808. Meissel, E., *Mathematische Annalen* 2, 1870. Lehmer, D. H., *Illinois Journal of Mathematics* 3, 1959. Tchebychev, P., lettre à Fuss, 1853. Littlewood, J. E., *Comptes rendus* 158, 1914. Bays, C. et Hudson, R., *Mathematics of Computation* 32, 1978. Tanaka, M., *Tokyo Journal of Mathematics* 3, 1980. Odlyzko, A. et te Riele, H., *Journal für die reine und angewandte Mathematik* 357, 1985. Rubinstein, M. et Sarnak, P., « Chebyshev's bias », *Experimental Mathematics* 3, 1994. Stokes, G. G., *Mathematical and Physical Papers*, volume 1, 1880. Stigler, S., *The History of Statistics*, 1986. *Scientific American*, 20 novembre 2026, sur l'annonce de L. Alpöge. Corpus ARC : Volume 1, chapitre 11 ; Volume 4, chapitres 3, 6 et 16 ; Volume 5, chapitres 3, 4 et 12 ; Volume 6, chapitre 14.
