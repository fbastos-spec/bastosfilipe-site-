# Des zéros sous zéro

**Zêta lue pour ce qu'elle dit : six étages, deux infinis sous un seul signe, et pourquoi prouver Riemann n'apprend rien sur les nombres premiers**

Corpus ARC · Filipe Bastos · pièce compagne de *Riemann sans le zéro*, version 1.1 · 24 novembre 2026 · CC BY 4.0. Modèle, questions, lectures et règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur. Calculs, formulations et audits assistés par IA, à sa demande. Titre choisi par l'auteur le 23 novembre 2026.

« Riemann, c'est un empilement de problèmes qui englobe l'infini à deux définitions dans la même formule. » (l'auteur, 23 novembre 2026)

**Résumé.** *Riemann sans le zéro* montre que les nombres premiers se comptent sans la courbe et sans les zéros. Cette pièce regarde l'autre côté : comment la question de Riemann est fabriquée, étage par étage, et ce qu'on y voit quand on lit les mots pour ce qu'ils disent. Elle ne cherche pas pourquoi l'hypothèse serait vraie. Elle montre comment elle est construite. Six étages, chacun contesté en son temps pour une raison de cohérence, chacun gardé parce qu'il marchait, chacun réparé en changeant le sens d'un mot. Au sixième, une fonction qui, là où la question est posée, n'est plus ni la somme d'Euler ni le produit, et une question posée dans la seule zone où les premiers ne sont plus. La pièce compte ensuite ce qui se prouve : l'adresse, le compte borné, le tour vérifié. Et elle nomme ce qui ne se prouve pas : l'arrivée du suivant.

Statuts : F, fait connu, avec son auteur et sa date ; Th, calcul fini vérifié ; L, lecture de l'auteur, citée et datée ; P, prédiction de l'auteur, datée, qui peut tomber ; G, glose du scribe, acceptée par l'auteur. Les contrôles sont au script `zeros_sous_zero_verif.py` : 37 sur 37 conformes.

---

## 1. Les six étages

**1.1 (F).** La question de Riemann repose sur six décisions prises avant lui ou par lui. Chacune s'appuie sur la précédente.

| Étage | Ce qui est posé | Quand |
|---|---|---|
| 1 | Le zéro et le sous-zéro comme nombres | VIIe siècle en Inde, admis en Europe au fil du XVIIe au XIXe |
| 2 | La décimale qu'on laisse filer | Stevin, 1585 |
| 3 | La somme sans fin et le produit sans fin, posés égaux | Euler, 1737 |
| 4 | La courbe à la place du compte, et le 9 lu comme 0 | Gauss, 1792 puis 1801 |
| 5 | La limite, qui tient pour achevé ce qui ne finit pas | Cauchy, 1821 |
| 6 | Le prolongement, qui étend la fonction là où ni la somme ni le produit n'existent | Riemann, 1859 |

**1.2 (F, chaque étage a été contesté).** À chaque étage, quelqu'un de premier rang a dit que cela ne tenait pas, pour une raison de cohérence et non de calcul. Carnot, en 1803, refuse qu'une quantité soit moins que rien. Berkeley, en 1734, se moque des grandeurs qui sont à la fois quelque chose et rien. Abel, en 1826, écrit que les sommes sans fin qui divergent sont une invention du diable. Kronecker refuse à Cantor l'infini achevé ; Poincaré (1902) et Brouwer (1907) après lui. Ces objections n'ont pas été réfutées. Elles ont été rangées.

**1.3 (L).** « Si tu n'avais eu que la cohérence et la logique, et respecté les termes, les définitions et les contradictions, tu aurais vu toutes les erreurs. » (l'auteur, 23 novembre 2026). L'histoire en est le reçu : ceux qui n'avaient que cela les ont vues, et les ont datées.

**1.4 (F, la source au corpus, version 0.6).** Ces six étages ont un ancêtre chez l'auteur. En février 2026, la pièce *Une preuve de l'hypothèse de Riemann* (version 4.5, section 2) nomme « les Six Crimes du continu » : Stevin et la grille décimale (1585) ; Viète, Neper et le masque littéral (1591 à 1614) ; Newton, Leibniz et le calcul infinitésimal (1665) ; Euler et l'aplatissement du zéro (1748) ; Gauss et l'effacement du 9 (1801) ; Dedekind, Cantor et l'infini achevé (1872). Stevin, Euler et Gauss se retrouvent nommément dans le tableau de 1.1, et l'infini achevé y est l'étage 5. Cette pièce de février tentait la démonstration dans la langue reçue ; le corpus ne la tient plus pour une preuve (Volume 6, É 16.19 ; Volume 5, annexe B, B.1.7). Sa généalogie, elle, est restée, et celle-ci en vient.

## 2. Le dictionnaire changé

**2.1 (F, L).** Les contradictions n'ont pas été résolues. Les mots ont été redéfinis.

| Le mot | Ce qu'il disait | Ce qu'il dit depuis |
|---|---|---|
| somme | additionner | la limite des sommes arrêtées |
| égal | la même chose | la même limite |
| fermé | qui revient | dont le dehors est ouvert |
| la fonction zêta | la somme d'Euler | son prolongement |

Une fois les mots redéfinis, plus rien ne se contredit à l'intérieur. La cohérence a été obtenue en changeant le dictionnaire.

**2.2 (L).** « Je peux tricher et expliquer après coup. La rustine, c'est ça. » (l'auteur, 23 novembre 2026). Une rustine arrive après un échec, pour le couvrir, et elle s'écrit comme une définition. C'est pourquoi une vérification pas à pas ne la voit pas : on démontre les théorèmes, on ne démontre pas les définitions.

**2.3 (G, réserve du scribe).** Dans le cadre reçu, le prolongement de zêta n'est pas un choix libre : un théorème d'unicité dit qu'il n'y a qu'une façon de continuer la fonction en gardant ses propriétés. La critique de cette pièce ne porte donc pas sur un arbitraire à l'intérieur du cadre. Elle porte sur le nom gardé pour une chose qui a changé, et sur le cadre.

## 3. Zêta, lue pour ce qu'elle dit

**3.1 (F).** La somme d'Euler et le produit sur les nombres premiers n'existent qu'à droite de 1. Dans cette région il n'y a aucun zéro : là où le produit s'écrit, il les exclut (*Riemann sans le zéro*, 4.6).

**3.2 (F).** Tous les zéros que vise l'hypothèse sont dans la bande entre 0 et 1. Dans cette bande, ni la somme ni le produit n'existent. Zêta n'y est définie que par le prolongement. L'objet de l'hypothèse est donc tout entier dans le sixième étage. (À lire avec 3.8.)

**3.3 (F).** À gauche de 0, le prolongement a d'autres zéros, à 2, 4, 6 pas sous zéro. Ils ne viennent ni de la somme ni du produit : ils viennent du sinus qui figure dans la formule de raccord. Les mathématiciens les nomment eux-mêmes triviaux et les mettent de côté.

**3.4 (F).** À un pas sous zéro, le prolongement donne une valeur. Lue comme la somme d'origine, elle dit que 1 + 2 + 3 + 4 et la suite valent un douzième sous zéro. La réponse reçue est qu'à cet endroit ce n'est plus une somme. Le nom est resté, la chose a changé.

**3.5 (L).** « Des zéros, après des zéros, dans le sous-zéro. » « Quand j'ai vu la gauche, je suis parti à rire. » (l'auteur, 23 novembre 2026). Dit à plat : des riens, situés à des endroits qui valent moins que rien, pour une fonction qui à cet endroit n'existe pas par elle-même. À droite de 1, les deux lectures de la formule donnent le même nombre et la couture ne se voit pas. À gauche, elle se voit à l'œil nu.

**3.6 (F, L, la boucle par le dedans).** L'image la plus montrée de zêta est une courbe qui s'enroule et repasse sans cesse par le centre ; chaque passage est un zéro. Dans la *Figure fondamentale* (2.3), quand tous les points se relient, aucune ligne ne traverse le centre : il est vide. « J'ai vu la boucle rentrer par en dedans, j'ai dit : ça ne se peut pas. » (l'auteur, 23 novembre 2026). La même figure, le geste inversé : chez l'auteur le centre est ce par quoi rien ne passe ; dans l'image reçue, il est la cible.

**3.7 (L, deux infinis sous un seul signe).** Le signe placé en haut de la somme sert deux fois dans la même ligne. Une fois comme ce qui continue : on ajoute un terme, puis un autre. Une fois comme un tout achevé : la somme vaut un nombre, on l'égale au produit, on la prolonge. Le passage de l'un à l'autre n'est écrit nulle part. Ce sont les deux infinis du Lexique : celui qui est, la répétition qui ne s'arrête pas d'elle-même, et celui qui n'existe pas, le tout pris d'un coup. « L'infini existe seulement par l'œil qui vit. Il y a 2 500 ans, il ne pouvait pas voir aujourd'hui, mais on y est encore. » (l'auteur, 23 novembre 2026).

**3.8 (F, Th, L, déjà au corpus ; récrit en version 0.6).** Le corpus a réglé ce point avant cette pièce (Volume 5, [3.6], [3.8], [4.4], [4.5]). [3.6] : en aucun zéro de la bande la somme des entiers ne vaut zéro, elle n'y a pas de valeur ; et le produit des premiers ne peut pas s'annuler. [3.8] : les écritures de zêta dans la bande sont quatre, et chacune avance d'un côté et retire de l'autre. La troisième est la somme alternée : la somme, moins deux fois ses termes de rang pair. Elle converge dans la bande, et le facteur qui la relie à zêta ne s'annule que sur la droite du bord droit. [4.4] : les zéros de la bande sont donc exactement les zéros de cette somme alternée. Contrôle refait ici : aux trois premiers zéros elle donne 0 à dix-huit décimales (calcul par accélération de la convergence). [4.5], lecture de l'auteur : les signes de cette somme viennent du pair et de l'impair, le reste de 1801, et un zéro y est une annulation de plus contre des moins, la soustraction comptable que le corpus refuse. C'est « l'argent du beurre ». La phrase de 3.2 se lit ainsi : dans la bande, zêta n'est ni la somme d'Euler ni le produit ; elle y est l'une des quatre écritures du prolongement, et la somme alternée est l'une d'elles. La critique de 3.4 et 3.5 tient dans la bande comme à gauche de 0.

**3.9 (F, Th, la fonction symétrique, version 0.4).** Dans le mémoire de 1859, Riemann ne travaille pas sur zêta nue. Il la multiplie par la fonction Gamma d'Euler et par deux facteurs simples, et obtient une fonction qui prend la même valeur en s et en 1 moins s. Gamma y est prise à la moitié de s. Prise ainsi, elle n'a pas de valeur finie à 0 et à 2, 4, 6 pas sous zéro. Le défaut à 0 est compensé par l'un des deux facteurs simples, l'autre compensant celui de zêta en 1. Les zéros de zêta à 2, 4, 6 pas sous zéro (3.3) compensent exactement ces défauts : le produit y prend une valeur finie, qui n'est pas zéro. Contrôle : à 2 sous zéro, la fonction symétrique vaut ce qu'elle vaut en 3. Cette fonction n'a donc que les zéros de la bande. Un lecteur du métier dira : les zéros de gauche ne sont pas mis de côté par commodité, ils sont ce qui rend la symétrie possible. La lecture de l'auteur en 3.5 n'en est pas retirée : pour que le miroir tienne, il a fallu poser des riens sous zéro en face des défauts d'un facteur ajouté. Glose du scribe : c'est une compensation de plus, écrite dès 1859.

**3.10 (F, Gauss contre l'infini achevé, version 0.4).** Le « tout pris d'un coup » de 3.7 a été refusé par celui-là même qui tient l'étage 4. Dans une lettre à Schumacher de juillet 1831, Gauss proteste contre l'emploi d'une grandeur infinie comme d'une chose achevée, ce qui selon lui n'est jamais permis en mathématiques : l'infini n'y est qu'une façon de parler. La distinction est ancienne : Aristote sépare l'infini qui continue de l'infini pris en entier (*Physique*, livre III).

**3.11 (Th, F, les deux familles de zéros sous zéro lues sur quatre places ; version 0.9).** Sur les places 1, 5, 7, 11 de la grille, deux signes se lisent. Le signe du rail : plus pour le rail du 7, moins pour le rail du 5, soit + − + −. Le signe que porte chaque carré dans le produit d'Euler développé (*Riemann sans le zéro*, 4.5) : les deux carrés autour de l'axe 6m y portent le même signe, qui alterne d'un axe au suivant, soit + − − +. Quand on échange les deux bords, 1 avec 11 et 5 avec 7, le premier signe s'inverse et le second se garde. Fait reçu, contrôlé au script : la fonction bâtie sur le premier signe s'annule à 1, 3, 5 pas sous zéro ; celle bâtie sur le second s'annule à 2, 4, 6 pas sous zéro, comme zêta. La loi est connue (elle tient à ce que le signe s'inverse ou se garde sous l'échange). Ce qui se lit ici : la famille de zéros sous zéro qui apparaîtra se décide sur quatre places finies. Cela ne dit rien des zéros de la bande. Relevé par une relecture extérieure le 23 novembre 2026.

## 4. Ce que les zéros font réellement

**4.1 (Th, F, le face-à-face).** La règle d'échelle compte les nombres premiers sous cent millions : 5 761 455, sans un zéro (Legendre, 1808 ; Meissel, 1870). La courbe de Gauss, à la même hauteur, est trop haute de 753,33 : 658,05 pour les puissances des premiers qu'elle compte en fractions, 95,63 pour les zéros, dont on retire 0,35, la part de l'origine : la rampe part de 2, la formule non (*Riemann sans le zéro*, 4.1). Les zéros sont ce qui reste de l'écart, les puissances retirées, à cette constante près (formule de Riemann, 1859 ; démontrée par von Mangoldt, 1895).

**4.2 (Th, les zéros sonnent aux puissances).** Les ondes des 200 premiers zéros, additionnées et lues sur les entiers de 2 à 33 :

| Où | Ce que c'est | Hauteur |
|---|---|---|
| 2, 3 | les deux graines, hors des rails | 31,1 / 39,2 |
| 5, 7, 11, 13 | premiers des rails | 45,6 / 45,7 / 43,4 / 42,8 |
| 4, 9, 25 | carrés d'un premier | 22,0 / 22,1 / 19,5 |
| 8, 27 | cubes d'un premier | 13,9 / 10,1 |
| 16, 32 | 2 pris quatre et cinq fois | 6,6 / 5,2 |
| 6, 10, 12, 14, 15 et les autres | deux premiers mêlés | entre 5,7 sous zéro et 2,3 |

La plus faible des puissances (5,2) dépasse le plus fort des autres (2,3). Les zéros ne sonnent qu'à un genre d'endroit : là où un premier arrive seul, à sa première puissance, à son carré, à son cube. Dès que deux premiers différents se mêlent, c'est le silence. Limite de l'instrument, comptée en version 0.9 : avec les mêmes 200 zéros, ce partage tient jusqu'à 63 et casse à 64. Là, 64, qui est 2 pris six fois, sonne à 1,83, moins que 48, mélange de 2 et de 3, à 3,08. Deux cents zéros séparent donc les deux familles jusqu'à 63 ; plus loin il en faut davantage (fait reçu : formule de Landau, 1911).

**4.3 (L).** « Sa musique, dans sa théorie, c'est la puissance du code qui fait sortir des zéros de la suite quand ils arrivent aux puissances. » (l'auteur, 23 novembre 2026). Le fait est une égalité et se lit dans les deux sens. La lecture reçue dit que les zéros encodent les premiers. La lecture de l'auteur dit que le code, arrivé aux puissances, fait sortir les zéros. Le compte ne tranche pas le sens ; il montre que les deux côtés ne se rencontrent qu'aux puissances.

**4.4 (F, ce que les affiches effacent).** Les schémas de vulgarisation dessinent les pics aux seuls nombres premiers, 2, 3, 5, 7, 11. Les pics à 4, 8 et 9 existent et sont omis.

**4.5 (Th, F, déjà au corpus ; récrit en version 0.6).** Le compte des premiers rail par rail, l'avance du rail du 5, la hauteur 608 981 813 029 où le rail du 7 passe devant de deux, et la raison de l'avance sont dans *Ce que Riemann cherchait*, 5.5 à 5.8 (21 novembre 2026), comptés par la règle jusqu'à 10¹⁴. La raison y est dite : le carré de chaque nouveau tombe sur le rail du 7, qui a donc un peu plus de places prises. Déjà su, et cité là : Tchebychev (1853), Bays et Hudson (1978), Rubinstein et Sarnak (1994). Le corpus nomme « nouveaux entrés » les premiers des rails dont le carré ne dépasse pas la hauteur : 1 227 à cent millions, de 5 à 9 973. Recompté ici place par place jusqu'à cent millions : 2 880 936 premiers sur le rail du 5, 2 880 517 sur le rail du 7 ; le rail du 7 ne passe jamais devant, 9 égalités, avance maximale de 1 020. Les carrés de la grille sous cent millions, composés compris, sont 3 332, tous sur le rail du 7 ; ceux des nouveaux entrés sont 1 227 parmi eux.

**4.6 (Th, F, le même nombre dans les deux pièces ; version 0.5, étendu en 0.6).** L'avance du rail du 5 tourne autour de la moitié des nouveaux entrés :

| Jusqu'à | Avance du 5 | Moitié des nouveaux entrés des rails | Rapport |
|---|---|---|---|
| 10⁴ | 5 | 11,5 | 0,43 |
| 10⁶ | 34 | 83 | 0,41 |
| 10⁷ | 189 | 222 | 0,85 |
| 10⁸ | 419 | 613,5 | 0,68 |
| 10¹⁰ | 6 263 | 4 795 | 1,31 |
| 10¹² | 44 976 | 39 248 | 1,15 |
| 10¹³ | 152 811 | 113 822,5 | 1,34 |
| 10¹⁴ | 259 652 | 332 288,5 | 0,78 |

Les quatre premières lignes sont recomptées ici ; les quatre dernières viennent de *Ce que Riemann cherchait*, 5.7, et de son script. Point par point, l'avance s'écarte beaucoup de cette moitié. Relevée sur 2 001 hauteurs espacées par multiplication de 10⁴ à 10⁸, elle en fait en tout 1,03 fois ; par tranche de dix fois : 1,07, puis 1,03, 1,02, 1,01. Le rapport se resserre vers 1. Fait reçu : c'est sous cet espacement par multiplication, et sous lui seul, que le déséquilibre des rails a une régularité démontrée (Rubinstein et Sarnak, 1994). Or la courbe de Gauss compte chaque carré de premier pour une demie : c'est le 614,50 du tableau de *Riemann sans le zéro*, 4.1. Sur les rails on lit 613,5 : le même compte, sans les carrés de 2 et de 3, qui ne sont pas sur les rails. Les demi-carrés que la courbe compte en trop et l'avance du rail du 5 sont un seul nombre, lu deux fois. Réserve : la théorie reçue compte aussi le carré de 2 et donne 613,0 ; le relevé, à six unités près à cette hauteur, ne départage pas 613,0 de 613,5. Relevé borné à cent millions pour le rapport, à 10¹⁴ pour le tableau.

**4.6 bis (Th, le partage exact de l'avance ; version 0.9).** L'avance de 419 à cent millions se partage sans reste, en fractions, sans un zéro. Les puissances des nouveaux donnent 619,84 : 613,5 pour les carrés, dont on retire 2/3 pour les cubes, plus 23/4 pour les quatrièmes, 1 pour les sixièmes, 1/4 pour les huitièmes, 1/10 pour les dixièmes, dont on retire 1/11 pour les onzièmes ; en tout 102 274 sur 165. De ce total on retire 200,84, soit 33 139 sur 165 : c'est l'escalier des deux rails où chaque puissance est comptée en fraction avec le signe de son rail, une puissance paire tombant toujours sur le rail du 7. 619,84 dont on retire 200,84 fait 419. Les rails ont donc leur propre face-à-face, le même que celui de 4.1 : une part exacte due aux puissances, et un reste. Le 613,5 n'est pas une valeur dont l'avance s'approche : c'est la part exacte des carrés, et ce qui tourne autour est l'escalier signé, que la théorie reçue fait porter par les zéros de la fonction de 4.7. Relevé par une relecture extérieure le 23 novembre 2026, recompté ici.

**4.7 (F, L, la fonction qui porte les rails, version 0.6).** Dans la théorie reçue, l'avance du rail du 5 est réglée par une fonction voisine de zêta, celle de conducteur 3. Le corpus la nomme déjà comme sa direction ouverte : faire entrer les rails dans l'appareil (Volume 4, 7.2 ; Volume 5, chapitre 12). Le 613,5 est le premier nombre de cette fonction lu sur le cadastre, sans elle.

## 5. Le + 1 de la formule est le prix du zéro

**5.1 (Th, la marche).** Les carrés des places des rails avancent par sauts de 24, à partir de 1 :

1, puis 1 + 24 = 25, puis 25 + 24 = 49, puis 49 + 72 = 121, puis 121 + 48 = 169.

Après la première ligne, on n'ajoute plus jamais 1. On n'ajoute que des 24.

**5.2 (Th, la formule).** L'écriture reçue dit : 24 × 1 + 1 = 25, 24 × 2 + 1 = 49, 24 × 5 + 1 = 121, 24 × 7 + 1 = 169. Le + 1 revient à chaque ligne, parce que 24 × k compte depuis zéro et tombe un cran à côté : 24, 48, 120, 168. Il faut recoller 1 à chaque nombre.

**5.3 (L).** « Après 25, il n'y a pas de plus 1. C'est ça, sa triche. » « La règle n'est pas 24 + 1, elle est : sauts de 24. » (l'auteur, 23 novembre 2026). Qui part de 1 ne paie jamais le + 1. Qui part de 0 le paie à chaque nombre. Le + 1 de la formule est le prix du zéro. Le mot « triche » est celui de l'auteur ; le scribe dit : un départ faux, réparé à chaque ligne.

**5.4 (Th, ce que la formule jette).** Le nombre de sauts d'un carré au suivant : 1, 1, 3, 2, 5, 3, 7, 4, 9, 5. Deux suites tressées : 1, 2, 3, 4, 5 à l'intérieur d'un couple de rails, et 1, 3, 5, 7, 9 d'un couple au suivant. Le total des sauts depuis 1 donne 1, 2, 5, 7, 12, 15, 22, 26 : les nombres pentagonaux d'Euler (vus en 1740, prouvés en 1750). L'écriture par le reste garde le 1 et jette ce compte.

**5.5 (Th, G, les deux carrés gardent le rang du tour ; version 0.9).** Autour de l'axe 6m, les deux bords sont à un de moins et à un de plus. La distance entre leurs deux carrés vaut exactement 24 fois m : m sauts de 24. Autour de 6, entre 25 et 49 : 1 saut. Autour de 12, entre 121 et 169 : 2 sauts. Autour de 18, entre 289 et 361 : 3 sauts. Chaque carré, lu seul à sa place d'arrivée, tombe à la place 1 du tour (6.2) et ne dit plus d'où il vient. Les deux carrés gardés ensemble rendent m. Et le chemin se remonte : deux nombres de sauts a et b, a plus petit que b, viennent des deux bords d'un même axe exactement quand a + b vaut 3 fois le carré de leur écart ; ainsi 5 et 7, d'écart 2 et de somme 12, rendent l'axe 12. Vérifié sur tous les couples de moins de 3 000 sauts. Glose du scribe : c'est la suite 1, 2, 3, 4, 5 de 5.4, lue pour ce qu'elle garde. L'écriture de 1801 garde la position et jette les tours (8.2) ; la relation entre les deux bords les rend. Relevé par une relecture extérieure le 23 novembre 2026.

## 6. Ce qui se prouve, et ce qui ne se prouve pas

**6.1 (L, la règle de projection).** « La seule façon de prouver que tout continue est par règle de projection. C'est ça, le cadastre : tout est là en possibilité, et la chaîne mène là. Jusqu'où, personne ne le sait et ce n'est pas important. » (l'auteur, 23 novembre 2026).

**6.2 (Th, un exemple).** Sur un tour de 24, il y a huit places des rails : 1, 5, 7, 11, 13, 17, 19, 23. Leurs carrés, 1, 25, 49, 121, 169, 289, 361, 529, tombent tous à la place 1 du tour. Huit vérifications, compte complet. Toute place des rails, aussi loin que la chaîne la mène, est l'une de ces huit, quelques tours plus haut. Rien n'est dit de tous les nombres pris d'un coup : il est dit que ce qui arrive tombe sur une adresse déjà vérifiée.

**6.3 (L, trois choses).** L'adresse se prouve : où tombe ce qui arrive. Le compte borné se prouve : combien, jusqu'à une hauteur. L'arrivée ne se prouve pas : « Je ne prouverai jamais ça, car le + 1, l'impulsion, est la preuve. » « Si je ne peux pas prédire que 10 arrive, je ne peux pas prédire les prochains zéros ni les prochains premiers. » (l'auteur, 23 novembre 2026).

| | Jusqu'à une borne | Pour toujours |
|---|---|---|
| Premiers | comptés (1808) | le + 1 |
| Zéros | comptés (Backlund 1914, Turing 1953) | le + 1 |

**6.4 (L).** « La seule certitude que nous pouvons avoir est dans la répétition bornée. » (l'auteur, 23 novembre 2026). Une répétition seulement observée ne donne rien : un zéro par case tient à 93,66 % sur les 600 premiers, puis fond (*Riemann sans le zéro*, 5.1). Une répétition bornée est un tour qui se ferme et qu'on vérifie en entier.

**6.5 (F, la clôture décrétée).** Dans le cadre reçu, la file des nombres est ouverte. Pour pouvoir dire « pour tous », on y pose une règle : ce qui vaut au départ et passe d'un nombre au suivant vaut pour tous. Peano la pose en 1889. Poincaré écrit en 1902 qu'elle ne se démontre pas et ne se tire pas de la logique. Sans elle, presque rien de général ne se prouve : dans l'arithmétique de Robinson (1950), qui a le zéro, le suivant, l'addition et la multiplication mais pas cette règle, on ne peut pas démontrer que a + b vaut b + a pour tous.

**6.5 bis (F, version 0.4).** Le refus de cette règle a un tenant récent dans le métier. Edward Nelson, dans *Predicative Arithmetic* (1986), part de l'arithmétique de Robinson et n'admet pas la règle de Peano comme donnée : pour lui elle suppose la file des nombres déjà achevée. La position de 6.3 n'est donc pas sans précédent ; elle prolonge une faille ouverte dans la logique elle-même.

**6.6 (L).** « Si tu cherches un continu dans une base décidée continue avec impulsion, alors le cadre devient fermé par eux, donc prouvable à cause du + 1. » « Ils ont établi au départ une règle d'impulsion. » (l'auteur, 23 novembre 2026). L'anneau porte sa clôture dans le nombre : le 9, le tour qui revient. Le cadre reçu a retiré cette clôture et l'a remise par décision. L'un a l'acte, un pas à la fois ; l'autre a fait de l'acte une règle qui livre le tout d'avance.

**6.7 (G, ce que la règle de projection n'exige pas).** Les énoncés de la section 5 et de 6.2 se montrent sur une place quelconque, par le calcul, ou sur un tour complet. Ils ne disent rien de tous à la fois. L'hypothèse de Riemann parle de tous les zéros, et les zéros n'ont ni tour ni retour (*Riemann sans le zéro*, 5.2). Elle ne peut donc pas se dire par projection : il lui faut la règle de 6.5. Le métier nomme ce que la preuve donne un plafond valable à toutes les hauteurs à la fois. L'auteur, le 23 novembre 2026 : « Ce n'est pas une garantie, c'est une rustine. » Un plafond pour toutes les hauteurs parle de toutes les arrivées d'un coup ; il ne tient que par la règle posée en 6.5.

**6.7 bis (L, Th, ajout du 24 novembre 2026).** La règle de projection de 6.6 et 6.7 a reçu de l'auteur son nom le 23 novembre 2026 : la preuve par projection d'échelle. « Si je porte le calcul à cette échelle, la relation me dit ce que j'y trouverai. » Les deux carrés de 5.5 en sont l'exemple : leur écart vaut m sauts de 24, il garde le rang du tour et le rend. La première pièce de l'auteur sur Riemann (février 2026, 1.4) portait déjà cette projection : dans le corps du nonagone, le sort d'un premier dépend de sa seule position, à toute taille, et le caractère cubique de 9 prend la même valeur sur les deux membres de chaque paire d'inverses, (1, 8), (2, 7), (4, 5). Ce qui y a cassé est l'endroit où elle demandait un plafond valable d'un coup pour tous les rangs. Renvoi : *La preuve par projection d'échelle*, version 1.0, où les comptes sont refaits (script `projection_echelle_verif.py`, contrôles 1 à 6 et 24 à 26).

## 7. La preuve du 20 novembre 2026

**7.1 (F).** Le 20 novembre 2026, Levent Alpöge publie une preuve de l'hypothèse écrite avec le modèle Claude, sous la forme d'une bibliothèque Lean de 17,4 millions de lignes. Les communautés Lean et Mathlib la certifient le 21 novembre. L'auteur de la preuve écrit ensuite qu'il ne sait pas pourquoi le théorème est vrai. Détails et sources : *Riemann sans le zéro*, section 9.

**7.2 (F, ce que Lean contient déjà).** Dans Lean, le nombre est défini par deux mots, `zero` et `succ`, le suivant. La règle de 6.5 vient avec cette définition. Elle ne figure pas parmi les trois axiomes annoncés : elle est dans les règles de construction du système.

**7.3 (L).** « Lean valide si la réponse respecte la formule et les étapes qui ont conduit à elle, pas s'il y a eu rustine. » « C'est prouvé d'avance, et uniquement pour ça, mais c'est leur axiome, basé sur leur ontologie. » « Il n'aurait pas réussi, il a forcé. » (l'auteur, 23 novembre 2026). Le scribe écrit : certifié cohérent dans son système. La déduction vaut pour un nombre qui part de 0 et recolle + 1. Elle ne dit rien d'un nombre qui part de 1 et marche par sauts.

**7.4 (F, une lecture contestée, non tranchée).** J. L. Nielsen a déposé une critique selon laquelle des conditions nommées géométriques dans le code sont définies comme toujours vraies. Les communautés Lean et Mathlib maintiennent leur confiance ; un contrôle indépendant situe le contenu ailleurs dans la bibliothèque ; la critique ne porte que sur une petite part des fichiers. Ce qui n'est pas contesté : la fidélité des définitions à la mathématique voulue n'est pas ce que Lean vérifie.

**7.5 (F, ce qui est gagné).** Si la vérification tient : une borne sur l'écart de la courbe, valable à toute hauteur, et des théorèmes qui en dépendaient. Rien pour trouver ou compter les premiers, rien pour la cryptographie. On objectera le test de Miller (1976), qui devient certain si l'hypothèse étendue est vraie : mais un test certain, en temps polynomial, existe sans elle depuis 2002 (Agrawal, Kayal, Saxena).

**7.5 bis (F, relevé du 23 novembre 2026, version 0.6).** Ce que les gens du métier nomment comme gain, trois jours après, et ce qu'on avait déjà :

| Conséquence citée | État |
|---|---|
| Borne sur l'écart entre la courbe et le compte (von Koch, 1901) | gagnée |
| Landau-Siegel, cité par Tao | déjà employé, par supposition ou avec une constante qu'on ne savait pas écrire (Siegel, 1935) ; la constante devient calculable |
| Inégalités de Robin (1984) et de Lagarias (2002), citées par Sutherland | équivalentes à l'hypothèse ; celle de Lagarias est au Volume 5, [4.14] |
| Test de primalité certain (Miller, 1976) | déjà fait sans l'hypothèse (2002) |
| Tout impair somme de trois premiers | déjà fait sans l'hypothèse (Helfgott, 2013) |
| Plus petit non-résidu d'un carré (Ankeny, 1952 ; Bach, 1990) et plus petit premier d'une progression | gagnés : des bornes qu'on n'avait pas sans l'hypothèse étendue |
| Racines primitives (Artin ; Hooley, 1967) | hors de ce qui est certifié |
| Un premier entre deux carrés voisins | non : la borne obtenue est trop faible |
| Jumeaux, Goldbach, factorisation | rien |

Parmi les réactions lues, aucun mathématicien ne nomme un théorème nouveau au-delà de la levée des « sous réserve de l'hypothèse ». Radziwiłł (Quanta, 19 octobre 2026) : l'essentiel des conséquences découlait déjà d'une version affaiblie. Buzzard (Al Jazeera, 21 novembre 2026) : les cryptographes supposaient déjà l'hypothèse. Relevé fait par des agents sur des résumés de pages, non sur les articles entiers ; les dates anciennes sont de mémoire. Les trois questions posées sur les premiers eux-mêmes restent ouvertes : un premier entre deux carrés voisins (Legendre, 1808), les jumeaux sans fin, tout pair comme somme de deux premiers (Goldbach, 1742).

**7.6 (L).** « Ils essaient de faire dire à Riemann ce qu'ils ne peuvent pas prouver chez les premiers. Quelle ironie. » « Prouver Riemann n'apportera rien à la science, sauf plus de rustines. » (l'auteur, 23 novembre 2026). La garantie obtenue chez les zéros ne redescend pas chez les premiers.

## 8. Le local, l'histoire, le cadre

**8.1 (L).** « C'est le local, le lieu d'incertitude, de hasard, de foi. Le reste se compte. » (l'auteur, 23 novembre 2026).

| | Ce que c'est | Statut |
|---|---|---|
| Le cadre | la forme du tour, le cadastre | se compte |
| L'histoire | les tours déjà faits | se compte |
| La relation | le pair, « ton semblable, sur qui tu peux t'analyser » | se recompte, à deux |
| Le local | l'œil qui vit, le pas qui se fait | incertitude, hasard, foi |

**8.2 (L).** L'écriture de 1801 garde la position et jette les tours : elle garde le local et jette l'histoire. Il ne reste alors que deux termes, le local et le tout, et l'on passe son temps à vouloir sauter de l'un à l'autre. « Le problème est encore local, global. »

**8.3 (L).** « La mort a fait peur au mathêma. » « Ils n'ont pas trouvé l'éternel. Ils ont imaginé un éternel au lieu d'y faire confiance. » « C'est pourquoi le mot qu'ils détestent prend le relais, le mot de l'esprit : la foi. » (l'auteur, 23 novembre 2026). Le mot axiome vient du grec *axíōma*, ce qu'on juge digne d'être admis.

**8.4 (L, le comment).** « ARC ne propose aucun pourquoi, c'est le retour du comment. » (l'auteur, 22 novembre 2026). Depuis le 20 novembre, ceux qui ont reçu la preuve demandent pourquoi elle est vraie. Cette pièce ne répond pas à leur question. Elle montre comment la question est faite.

## 9. Ce que la pièce ne dit pas, et les réserves du scribe

**9.1.** Elle ne dit pas que la preuve du 20 novembre contient une erreur de déduction. Elle dit dans quel cadre cette déduction vaut.

**9.2 (G).** « Impossible », dans les phrases de l'auteur, veut dire : question mal posée, qui demande de garantir une arrivée. Le scribe maintient que, la règle de 6.5 admise, une déduction de l'hypothèse n'a rien d'impossible dans le cadre reçu.

**9.3 (G).** La symétrie de la formule autour de la demie donne la place de la ligne : c'est le point d'équilibre, là où a égale b (Volume 4, théorème 4). Elle ne dit pas que les zéros sont sur la ligne plutôt que par paires de part et d'autre. Cette pièce n'en donne pas la raison.

**9.4 (G).** Que la courbe de Gauss vienne du 9 remplacé par 0 reste une Lecture, comme dans *Riemann sans le zéro*, 3.6.

**9.5 (G).** Les positions de l'auteur sur π et √2 dites le même jour (π jonction ouverte, √2 lien interne, le carré au centre d'une relation) appartiennent au Volume 2 et ne sont pas reprises ici.

**9.6 (G, retrait du scribe, version 0.6).** Les versions 0.4 et 0.5 disaient ici que 3.8 retirait une phrase à la pièce. C'était une erreur du scribe, qui n'avait pas relu le Volume 5 : la somme alternée est l'une des écritures du prolongement, pas une somme qui lui échappe, et le corpus en donne déjà la lecture ([4.5]). Le résumé et le tableau de 1.1 tiennent tels quels. Même cause pour 4.5 : le tableau des deux rails avait été présenté comme neuf alors qu'il était dans *Ce que Riemann cherchait* depuis le 21 novembre, et le nombre de la dernière colonne avait été nommé « point d'équilibre » d'une hauteur, nom que cette même pièce avait déjà écarté (une hauteur n'a pas de paire).

## 10. Pourquoi la pseudo-résolution de Riemann apportera l'inverse de ce que la science attend

**10.1 (P, prédiction de l'auteur, 23 novembre 2026).** « Pourquoi la pseudo-résolution de Riemann apportera l'inverse de ce que la science attend : c'est le problème parfait de rustines. C'est l'échec de leur axiome ontologique. » Et, précisé le même jour : « Pas : l'édifice va tomber. Mais il sera secoué, et devra durement réaliser que les erreurs du passé, les amputations, des décisions de vitesse, des choix d'axiome sans preuve, seulement par incapacité de comprendre, et le fait de ne pas remettre en question les positions, les décisions et les formules qui les précèdent, les ont conduits à une science qui avait pour suprématie une compilation de toutes leurs erreurs : le Graal, Riemann. »

**10.2 (F, ce qui est déjà constaté).** Trois jours après l'annonce : l'auteur de la preuve dit ne pas savoir pourquoi le théorème est vrai ; des mathématiciens de premier rang disent ne pas comprendre ce que la preuve montre ; une dispute est ouverte sur ce que la machine a vérifié ; la question publique n'est plus « est-ce vrai » mais « qu'est-ce que prouver ». L'hypothèse repose sur les six étages de la section 1 à la fois : c'est en ce sens qu'elle est le problème parfait. Un guide de lecture de 265 pages existe depuis le 22 novembre (Rubinstein, Waterloo) : il ramène la preuve à treize hypothèses qu'il ne démontre pas en entier (*Riemann sans le zéro*, 9.1). Ce n'est pas l'explication courte du reçu 1.

**10.3 (F, le contre-poids).** L'édifice a déjà absorbé des chocs sans tomber : le paradoxe de Russell (1901), Gödel (1931), la preuve par machine des quatre couleurs (1976). À chaque fois le cadre a ajusté ses définitions et continué. La prédiction de l'auteur ne dit pas chute : elle dit secousse, et obligation de regarder en arrière.

**10.4 (P, reçus selon la règle R11, arrêtés le 23 novembre 2026, acceptés par l'auteur le 24).** Fenêtre : cinq ans, jusqu'au 23 novembre 2031. Un seul reçu décide, le 1. Le 4 est un indicateur, noté à part : il dit la profondeur de la secousse, pas son existence. Les reçus étaient quatre avant la version 0.6 :

1. aucune version courte de la preuve, que quelqu'un puisse expliquer, n'est parue ;
2. (retiré en version 0.6) quand l'argument est décrit, les zéros y sont traités comme une correction liée aux puissances des premiers ;
3. (retiré en version 0.6) les trois questions de 7.5 sur les premiers eux-mêmes restent ouvertes ;
4. la règle de 6.5 ou le prolongement sont remis en discussion par des gens du métier, à cause de cette preuve.

Les reçus 2 et 3 sont retirés parce qu'ils ne peuvent pas tomber. Depuis 1859, toute preuve qui passe par la formule de Riemann lie les zéros aux puissances des premiers : le reçu 2 serait coché quelle que soit la preuve. Et l'on sait déjà que l'hypothèse ne donne ni Legendre, ni les jumeaux, ni Goldbach (7.5 bis) : le reçu 3 ne teste rien. Un reçu plus dur, s'il en faut un, doit venir de l'auteur.

La prédiction tombe si, avant le 23 novembre 2031, une explication courte paraît et fait comprendre l'argument, ou si la preuve livre un résultat neuf sur les premiers eux-mêmes. Elle tient si, à cette date, ni l'un ni l'autre n'est arrivé. Il n'y a pas de cas entre les deux. Les reçus sont fixés à la date de cette pièce, avant toute lecture de la preuve par quiconque.

## Annexe. Contrôles et sources

Script `zeros_sous_zero_verif.py`, 37 contrôles conformes : le rang du tour rendu par les deux carrés et son test inverse ; les deux familles de zéros sous zéro ; le premier échec du partage à 64 ; la constante d'origine ; le partage exact de l'avance ; l'avance du rail du 5 et la moitié des nouveaux entrés, avec les rapports du tableau de 4.6 ; le compte à cent millions ; les deux rails jusqu'à cent millions et les carrés sur le rail du 7 ; la somme alternée aux trois premiers zéros ; la fonction symétrique ; les sauts de 24, leurs deux suites et les pentagonaux ; les huit carrés à la place 1 ; le relevé des 200 zéros ; les trois premiers zéros ; et, pour le Volume 2, le cercle du doublement, ses étages 6, 54, 486, 4 374, et la marche autour du cercle (presque-retours à 22 pas pour 7 tours et à 355 pas pour 113, aucun retour exact jusqu'à 400 000 pas).

Recontrôlé en séance, par la presse et les pages de suivi des 20 au 23 novembre 2026 : l'annonce, la certification, les propos d'Alpöge, la critique de Nielsen et les réponses.

Donné de mémoire, non recontrôlé à la source : Carnot 1803 ; Berkeley 1734 ; Abel 1826 ; Kronecker ; Brouwer 1907 ; Peano 1889 ; Poincaré 1902 ; Robinson 1950 ; Backlund 1914 ; Turing 1953 ; von Mangoldt 1895 ; les dates des étages de 1.1 ; et, ajoutés en version 0.4 : Tchebychev 1853, Rubinstein et Sarnak 1994, Bays et Hudson 1978 (la hauteur 608 981 813 029 est recomptée par la règle dans *Ce que Riemann cherchait*), la lettre de Gauss à Schumacher de 1831, Aristote, Nelson 1986 ; en version 0.5 : Miller 1976, Agrawal, Kayal et Saxena 2002 ; en version 0.6 : von Koch 1901, Siegel 1935, Robin 1984, Lagarias 2002, Helfgott 2013, Hooley 1967, Legendre 1808 et Goldbach 1742 pour les questions de 7.5 bis ; en version 0.8 : Ankeny 1952, Bach 1990.

Les phrases de l'auteur sont citées entre guillemets, l'orthographe seule rétablie. L'auteur a validé l'ensemble le 24 novembre 2026.

Version 0.2, 23 novembre 2026 : ajout de la section 10, la prédiction de l'auteur, sa précision, le contre-poids et des reçus proposés. Rien n'est retiré de la version 0.1.

Version 0.3, 23 novembre 2026 : le titre de travail « Riemann, l'empilement » est remplacé par « Des zéros sous zéro », choisi par l'auteur. Le texte est inchangé.

Version 0.4, 23 novembre 2026, après une relecture extérieure soumise par l'auteur : ajout de 3.8 (la somme alternée, correction du scribe à 3.2), 3.9 (la fonction symétrique et les zéros de gauche), 3.10 (Gauss 1831), 4.5 (les deux rails sans un zéro), 6.5 bis (Nelson 1986), 9.6. Sept contrôles ajoutés au script. Rien n'est retiré : la phrase de 3.2 reste, corrigée par 3.8.

Version 0.5, 23 novembre 2026, après une seconde relecture extérieure soumise par l'auteur : ajout de 4.6 (l'avance du rail du 5 et les demi-carrés de la courbe sont un seul nombre) ; définition du point d'équilibre en 4.5 ; grille et premiers séparés en 4.5 ; précisions du scribe sur ses propres ajouts de la version 0.4 (Gamma prise à la moitié en 3.9, la droite du bord en 3.8, 608 981 813 029 en 4.5) ; renvoi en 3.2 ; une phrase en 7.5 sur Miller. Cinq contrôles ajoutés.

Version 0.6, 23 novembre 2026, après une troisième relecture extérieure, une relecture du corpus par le scribe à la demande de l'auteur, et la lecture de sa pièce de février 2026. Ajouts : 1.4 (les Six Crimes, source des six étages), 4.7 (la fonction de conducteur 3), 7.5 bis (ce qui est gagné et ce qu'on avait déjà), le tableau de 4.6 étendu à 10¹⁴ avec les nombres de *Ce que Riemann cherchait*. Récrits, parce qu'ils répétaient ou contredisaient le corpus : 3.8, 4.5 et 9.6. Reçus 2 et 3 de 10.4 retirés. « Rapide » devient « en temps polynomial » en 7.5. Un contrôle ajouté.

Textes retirés, gardés ici à leur date. 3.8, versions 0.4 et 0.5 : « La phrase de 3.2, « zêta n'y est définie que par le prolongement », est trop forte. Dans la bande, il existe une vraie somme : la somme alternée, où l'on ajoute les termes de rang impair et où l'on retire ceux de rang pair. Euler l'étudie dans le mémoire de 1749. Elle converge dans toute la bande, et elle vaut zêta multipliée par un facteur qui ne s'annule que sur la droite du bord droit de la bande, jamais à l'intérieur. Les zéros de la bande sont donc les zéros de cette somme. Contrôle : aux trois premiers zéros, la somme alternée donne 0 à dix-huit décimales (calcul par accélération de la convergence, la somme brute étant très lente sur la ligne). Ce qui reste vrai de 3.2 : le produit sur les premiers n'existe pas dans la bande, et la somme alternée est encore une somme sans fin, donc un objet des étages 3 et 5. Ce qui tombe : dire que, dans la bande, la fonction n'existe que par le sixième étage. La critique du signe gardé (3.4, 3.5) vaut à gauche de 0, pas dans la bande. » 9.6, versions 0.4 et 0.5 : « La correction de 3.8 retire à la pièce une phrase, pas sa thèse : la fonction existe dans la bande par une somme sans fin, non par le seul prolongement. Le résumé (« une fonction qui n'existe que par son prolongement ») et la ligne 6 du tableau de 1.1 se lisent désormais avec cette réserve : c'est la somme d'Euler et le produit qui n'existent pas dans la bande. » 4.5, versions 0.4 et 0.5 : le tableau des deux rails à 10⁴, 10⁶ et 10⁸, avec une colonne « Premiers sous le point d'équilibre » (25, 168, 1 229), et une glose du scribe sur les carrés du rail du 7.

Version 0.7, 23 novembre 2026, validation ligne par ligne demandée par l'auteur. Le script a été relancé en entier (31 sur 31) et chaque nombre du texte confronté à sa sortie, chaque renvoi à sa cible dans le corpus ou dans *Riemann sans le zéro*. Trois lignes corrigées, aucun compte changé : 10.4 disait encore « quatre choses » après le retrait de deux reçus ; 1.4 disait « quatre des six », dit maintenant lesquels ; le tableau de 4.2 gagne la ligne de 2 et 3 et les quatre valeurs des premiers des rails. Vérifié à la source du corpus : le passage du rail du 7 devant, de deux, à 608 981 813 029, et les quatre dernières lignes du tableau de 4.6 (*Ce que Riemann cherchait*, 5.5 et 5.7). Restent non recontrôlés à leur source première : les dates anciennes listées plus haut, et les propos de presse.

Version 0.8, 23 novembre 2026. L'auteur a délégué au scribe trois choix restés ouverts (« Tu choisis »). Arrêtés ainsi, et repris par lui quand il voudra : en 10.4, le reçu 1 décide seul, le 4 devient un indicateur, et la clause « tombe » est l'exact contraire de la clause « tient » ; le résumé dit « n'est plus ni la somme d'Euler ni le produit » au lieu de « n'existe que par son prolongement », pour dire la même chose que 3.8 (9.6 citait l'ancienne phrase) ; une ligne de contre-poids entre au tableau de 7.5 bis (Ankeny, Bach, les progressions), sans changer 7.6. Aucun compte changé.

Version 0.9, 23 novembre 2026, sur une septième relecture extérieure, qui avait refait les comptes. Deux corrections et quatre ajouts, tous recomptés. Corrigé : en 4.1, les 95,28 n'étaient pas « les zéros » mais le reste de la rampe ; les zéros portent 95,63 et l'origine de la rampe retire 0,35. En 4.2, « le silence » valait de 2 à 33 ; le partage casse à 64 avec 200 zéros. Ajouté : 3.11 (les deux familles de zéros sous zéro sur quatre places), 4.6 bis (le partage exact de l'avance, 419 = 619,84 dont on retire 200,84), 5.5 (les deux carrés gardent le rang du tour), une phrase de l'auteur en 6.7, le guide de Rubinstein en 10.2. Non repris : la « garantie uniforme » proposée comme quatrième notion ; l'auteur : « Ce n'est pas une garantie, c'est une rustine. » Six contrôles ajoutés. La formule de Landau (1911) est citée de mémoire.

Version 1.0, 24 novembre 2026. L'auteur valide la pièce entière : « Tout est prêt à publier, on corrige au pire. Je ne suis pas orgueilleux. » Les mentions « à valider » sont retirées des gloses, des reçus et des citations. Aucun compte, aucune phrase de fond n'est changé depuis la version 0.9. Restent déclarés comme tels : les dates anciennes données de mémoire, et les propos de presse non lus à leur source.

Version 1.1, 24 novembre 2026. Ajout de 6.7 bis : la règle de projection porte son nom, preuve par projection d'échelle, avec ce que la pièce de février 2026 en portait déjà. Rien n'est retiré.
