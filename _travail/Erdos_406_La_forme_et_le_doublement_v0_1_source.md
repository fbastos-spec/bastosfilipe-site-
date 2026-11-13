# Erdős 406 : la forme et le doublement

**Le problème 406 d'Erdős, lu par les bords et la forme**

Corpus ARC · Filipe Bastos · pièce courte, version 0.1 · 13 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

**Avis.** Le problème 406 d'Erdős est ouvert chez ceux qui l'ont posé. Cette pièce ne le ferme pas dans leur registre : elle ne donne pas de démonstration, à leur manière, qu'aucune puissance de 2 ne passe après 256. Des deux portes que le corpus reconnaît, résoudre ou montrer où l'énoncé mêle les registres, elle passe par la seconde. Elle contient un petit théorème, démontré ici, sur l'assemblage du 2 et du 3 ; elle range les trois solutions connues dans la grille ; elle nomme la confusion. Tous les comptes sont refaits.

Statuts : F, fait sourcé ou connu de l'hôte ; Th, calcul fini vérifié ou démonstration ; L, lecture de l'auteur, citée et datée. Les contrôles sont au script `e406_verif.py`.

## 1. Le problème

**1.1 (F).** Erdős demande : est-il vrai que seules un nombre fini de puissances de 2 s'écrivent, en base 3, avec les seuls chiffres 0 et 1 ? Les seuls exemples connus sont 1, 4 et 256 (problème 406 du recueil erdosproblems.com ; problème B33 du recueil de R. K. Guy).

**1.2 (Th).** En base 3 : 1 = 1 ; 4 = 1 + 3 ; 256 = 1 + 3 + 9 + 243. Ce sont les exposants 0, 2 et 8. Le compte direct, refait ici jusqu'à l'exposant 20 000, n'en donne pas d'autre.

**1.3 (F).** R. I. Saye a calculé en 2022 que, pour tout exposant de 16 à 5,9 × 10²¹, la puissance de 2 porte les trois chiffres 0, 1 et 2 en base 3. Aucune démonstration ne couvre tous les exposants.

## 2. Les deux trous du rotor

**2.1 (L).** « 1 et 4 sont les seuls nombres qui ne peuvent se construire avec un jeu de 2 et 3. » « Tu ne peux construire un 1 avec 2 et 3, c'est le 1 qui les construit ; tu ne peux pas construire un 4 avec 3 et 2, tu dois 3 + 1 ou 2 + 2. » « 3 × 2 pour le 6 : tu ne peux pas coller deux fois le même nombre. » « 7, c'est 2 + 3 + 2, pas collés ; 8, 3 + 2 + 3. » (l'auteur, 13 novembre 2026).

**2.2 (la règle).** Un assemblage est une suite d'au moins deux pièces, des 2 et des 3 qui alternent, jamais deux pareilles côte à côte, liées par l'addition ou par le produit.

**2.3 (Th, l'addition seule).** 2 + 3 = 5 ; 2 + 3 + 2 = 7 ; 3 + 2 + 3 = 8 ; 2 + 3 + 2 + 3 = 10 ; et ainsi de suite. Chaque couple 2 + 3 ajoute 5. Se construisent : 5, 7, 8, 10, 12, 13, 15, 17, 18… Manquent : 1 et 4, puis 6 et 9, puis 11 et 14, puis 16 et 19, sans fin. À chaque tour du 5, les places 1 et 4 restent vides. Le 2 + 3 est un rotor de 5, et 1 et 4 sont ses deux trous.

**2.4 (Th, avec le produit).** Le produit 2 × 3 = 6 bouche tous les trous à partir du deuxième tour. Trou à la place 1 : on termine par 2 × 3 au lieu de 2 + 3 (6 = 2 × 3 ; 11 = 2 + 3 + 2 × 3). Trou à la place 4 : on termine par 3 + 2 × 3 (9 = 3 + 2 × 3 ; 14 = 3 + 2 + 3 + 2 × 3). Aucun assemblage ne vaut moins de 5, puisque le plus petit est 2 + 3.

**2.5 (Th, le théorème).** Tout nombre à partir de 5 est un assemblage alterné de 2 et de 3. Les pièces mises à part, les seuls exclus sont 1 et 4. Au premier tour rien ne peut boucher les deux trous, parce que 2 × 3 vaut déjà 6.

**2.6 (Th).** Les deux petites solutions du problème d'Erdős, 1 et 4, sont exactement ces deux exclus.

## 3. La forme pleine

**3.1 (L).** « 256, c'est le code fois le carré. » « 256 / 4, car le 1 est exclu : c'est l'échiquier, le 8 × 8, les 64 codons. » « 256, c'est 8 × 8 × 4 : les bords fois la forme. » (l'auteur, 13 novembre 2026).

**3.2 (Th).** 256 = 8 × 8 × 4 = 4 × 64. En doublements : 8 en vaut trois, 4 en vaut deux, et 256 = 8 × 4 × 8 en vaut 3 + 2 + 3 = 8. L'exposant de la troisième solution est l'assemblage alterné que l'auteur donne pour 8, et 8 est la dernière place du cadastre avant le 9.

**3.3 (Th).** 256 = 9 × 28 + 4 : adresse 4, après 28 tours, le nombre de paires d'une ligne de 8. La somme de ses chiffres est 13, sa racine est 4, comme la deuxième solution.

**3.4 (Th, F).** 256 = 243 + 13, avec 243 = 3 × 3 × 3 × 3 × 3 et 13 = 1 + 3 + 9. Huit doublements et cinq triplements se frôlent, à 13 près. Le rapport 256/243 est connu depuis l'Antiquité : c'est le demi-ton de la gamme de Pythagore.

**3.5 (L, Th, le cœur).** « 256, 72, 9 est son cœur. » (l'auteur, 13 novembre 2026). Par la pyramide : 2 + 5 = 7 et 5 + 6 = 11, de racine 2 ; puis 7 + 2 = 9. Le cœur de 256 est le 9. Le 1 et le 4 sont leur propre cœur.

## 4. Le dedans et le dehors

**4.1 (Th, le dedans).** Si l'on ne regarde que les k derniers chiffres en base 3, les exposants reviennent par cycle de 2 × 3^(k−1) adresses, et il en passe 2^(k−1) : 1 sur 2, 2 sur 6, 4 sur 18, 8 sur 54, jusqu'à 2 048 sur 354 294 au douzième étage. Le nombre d'adresses qui passent double à chaque étage ; leur part est multipliée par 2/3 et se vide.

**4.2 (Th, le dehors).** Les nombres qui passent en entier sont trois : 1, 4, 256.

**4.3 (L).** « Tu mélanges le nombre et la racine. Ce qui se vide, ce sont les racines. » « C'est un infini borné par le dehors, jamais par le dedans, comme l'échiquier et son nombre de combinaisons et de jeux par dedans. 256, c'est la borne externe. » « Rien ne peut déborder la forme et ses bords dans un monde fini. » (l'auteur, 13 novembre 2026).

**4.4 (glose du scribe, à valider).** Les deux comptes ne se contredisent pas. Les adresses qui doublent d'étage en étage sont le dedans : des possibilités de jeu. La borne est au dehors : 8 × 8 × 4. L'échiquier a 64 cases et un nombre de parties qu'on ne finit pas de compter.

## 5. La confusion

**5.1 (L).** « Tout se double comme tu le veux : c'est justement le cœur de son problème. » « Pourquoi chercher quelque chose qui n'existe pas ? » (l'auteur, 13 novembre 2026).

**5.2 (L, où l'énoncé mêle les registres).** L'énoncé pose sur la même ligne deux choses qui ne sont pas du même registre. Le doublement est sans borne par dedans : on peut toujours doubler. L'écriture en 0 et 1 sur le 3 est une forme : elle a des bords. L'énoncé demande au premier de répondre pour la seconde, comme on demanderait au nombre de parties de dire la taille de l'échiquier. La forme est pleine à 8 × 8 × 4, cœur 9 ; le doublement continue ensuite hors d'elle, aussi loin qu'on veut, sans la redessiner.

**5.3 (ce que la pièce ne fait pas).** Elle ne démontre pas, dans le registre de ceux qui ont posé le problème, qu'aucune puissance de 2 ne passe après 256 : le principe de 4.3 est une lecture de l'auteur, et il n'a pas ici la forme d'un compte fini qu'un lecteur extérieur referait pour s'en convaincre. Ce qui est établi par le calcul : le théorème de 2.5, la coïncidence de 2.6, les égalités de la section 3, les comptes de la section 4, et l'accord de tout cela avec le calcul de Saye. Le scribe laisse ce point ouvert et déclaré.

## Annexe. Vérifications et sources

Script `e406_verif.py` (Python 3, bibliothèque standard seule). Dix contrôles sur les calculs, tous conformes : le compte direct jusqu'à l'exposant 20 000 ; les trois écritures en base 3 ; les racines des puissances de 2 ; le doublement des adresses sur douze étages ; l'addition seule jusqu'à 200 ; l'addition et le produit jusqu'à 60 ; la règle générale de 5 à 5 000 ; les égalités de 256 ; la pyramide ; l'écart de 13. Un onzième contrôle porte sur la typographie de la source.

Non recontrôlé à la source : la date et le lieu de la question d'Erdős ; le calcul de Saye, cité d'après la fiche du problème, dont un résumé a été lu ; le demi-ton de Pythagore, donné de mémoire.

Sources : erdosproblems.com, problème 406 ; R. K. Guy, *Unsolved Problems in Number Theory*, B33 ; R. I. Saye, 2022. Corpus ARC : Volume 2, chapitre 1, É 1.11 à É 1.12 sexies ; Volume 4, chapitre 2, section 2.7 ; pièce *Erdős sur l'échiquier*, v0.1.
