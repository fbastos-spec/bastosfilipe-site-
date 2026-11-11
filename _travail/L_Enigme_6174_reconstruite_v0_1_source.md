# L'Énigme 6174, reconstruite

**Le volet I du triptyque de Kaprekar, refait à partir de ce que le corpus en a gardé**

Corpus ARC · Filipe Bastos · pièce courte, version 0.1 · 11 novembre 2026 · CC BY 4.0. Auteur du modèle, des questions, des lectures et des règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

**Avis.** La pièce d'origine, *L'Énigme 6174*, volet I du cycle de la sédimentation arithmétique (juin 2026), est perdue. Ce texte n'est pas elle. Il rassemble ce que les autres pièces du corpus en rappellent, avec leurs adresses, et il refait chaque calcul. Aucune phrase n'y est prêtée à l'auteur qui ne soit déjà gravée ailleurs ; ce qui n'a pas pu être retrouvé est déclaré manquant en section 5.

Statuts : F, fait sourcé ou connu de l'hôte ; Th, calcul fini vérifié ou démonstration ; L, lecture, citée avec son adresse. Les contrôles sont au script `kaprekar_verif.py`.

## 0. Ce qui restait du volet I

Quatre endroits du corpus citent la pièce perdue. Le Volume 6 (chapitre 5, É 5.4 et É 5.5, cote P-25) en garde le lemme et sa lecture. Le Volume 4 (chapitre 17, V4.17.2 et V4.17.9 ; chapitre 18, V4.18.4, V4.18.11 à V4.18.13 ; chapitre 19, V4.19.31) en rappelle les constantes et les deux étages, et dit lui-même que le volet I n'est pas au nombre de ses sources. Le Volume 1 (É 9.1, É 9.3, É 16.26) en garde la convergence et les deux points fixes. Le Volume 0 (chapitre 3) en garde l'échelle.

## 1. La routine

**1.1 (F).** D. R. Kaprekar, « Another Solitaire Game », *Scripta Mathematica* 15, 1949. On écrit un nombre sur une largeur fixe, en complétant par des zéros à gauche ; on range ses chiffres du plus grand au plus petit, puis du plus petit au plus grand ; on soustrait le second du premier ; on recommence. Les nombres dont tous les chiffres sont égaux sont écartés. Ce que l'hôte sait depuis lors : à quatre chiffres, tout aboutit à 6174 en sept pas au plus ; à trois chiffres, tout aboutit à 495 ; à deux et à cinq chiffres il n'y a pas de point fixe, il y a des cycles. Ces faits sont refaits ci-dessous ; aucun n'est une découverte du corpus.

## 2. Le lemme : une secousse, et la racine est 9

**2.1 (Th, le lemme de Kaprekar ; Volume 6, É 5.4).** Un nombre et son réarrangement portent la même somme de chiffres ; leur différence est donc toujours un multiple de 9. Le premier pas met tout nombre sur le réseau du 9, et il n'en sort plus : sa racine est 9 dès le premier pas, et aucun résultat de la routine n'est premier. Vérifié pour tous les nombres de 1 à 9999. Les trois exemples du Volume 6 : de 2026 on passe à 5994, de 137 à 7173, de 8 à 7992.

**2.2 (L ; Volume 6, É 5.5 ; Volume 4, V4.18.4).** « Une seule secousse, et le nombre est expulsé du territoire des premiers, pour toujours, puisque tout itéré ultérieur reste multiple de 9. » Et : « ce que l'opération amnésique détruit n'est pas une décoration, c'est la fertilité même de l'arithmétique. » Le Volume 4 le dit de l'autre côté : Kaprekar effondre toute racine sur le 9 en un seul pas et l'y fixe.

## 3. Les largeurs, une à une

**3.1 (F, Th, deux chiffres).** Le pas vaut 9 × (grand chiffre − petit chiffre). Il n'y a pas de point fixe ; il y a un seul cycle, 09, 81, 63, 27, 45, et tout y tombe. Ce sont les cinq multiples impairs de 9. (Connu de l'hôte ; refait ; non attesté dans les rappels du volet I.)

**3.2 (Th, trois chiffres : l'échelle des barreaux ; Volume 4, V4.19.31 ; Volume 0, chapitre 3).** Le pas vaut 99 × (grand chiffre − petit chiffre) : chaque résultat est un barreau de l'échelle 99k, de 099 à 891. Les barreaux descendent d'un cran à la fois vers le milieu : 099, 891, 792, 693, 594, 495 ; et 189, 792, 693, 594, 495. Le barreau du milieu, 495 = 5 × 99 = 45 × 11, est fixe : 954 − 459 = 495, parce que 9 − 4 = 5. Les 990 écritures à trois chiffres non uniformes y aboutissent toutes, en six pas au plus.

**3.3 (F, Th, quatre chiffres ; Volume 1, É 16.26).** Si les chiffres rangés sont a, b, c, d du plus grand au plus petit, le pas vaut 999 × (a − d) + 90 × (b − c). Les 8 991 nombres de 1000 à 9999 dont les chiffres ne sont pas tous égaux aboutissent tous à 6174, en sept pas au plus (9 990 écritures en comptant les zéros à gauche). Et 6174 est fixe : 7641 − 1467 = 6174 = 999 × 6 + 90 × 2. Par nombre de pas, de zéro à sept : 1, 383, 576, 2400, 1272, 1518, 1656, 2184 écritures. (La formule du pas et le décompte sont connus de l'hôte ; refaits.)

**3.4 (Th ; Volume 1, É 9.3).** 6174 = 18 × 7³ = 2 × 3² × 7³. La somme de ses chiffres est 18, sa racine est 9.

**3.5 (F, Th, cinq chiffres).** Aucun point fixe. Trois cycles : 53955 et 59994 ; 61974, 82962, 75933, 63954 ; 62964, 71973, 83952, 74943. (Connu de l'hôte ; refait ; non attesté dans les rappels du volet I.)

## 4. Ce que le corpus en lit

Toutes les phrases de cette section sont citées, avec leur adresse.

**4.1 (L, le sédiment ; Volume 4, V4.17.9 ; Volume 8, 10.32).** Des trois régimes du triptyque, celui de la routine est dit ainsi : « ce qui descend se dépose sur le réseau du 9 ». La routine est une descente et une sédimentation ; son régime est la clôture. Le Volume 8 : « la machine de Kaprekar, qui broie les chiffres, converge vers un attracteur (6174), jamais vers un abîme ».

**4.2 (Th, L, les deux étages ; Volume 4, V4.17.2 et V4.19.31).** (Th) 1 + 2 + … + 31 = 496, le troisième nombre parfait ; 2 + … + 31 = 495. Un seul pas mène 496 sur 495 : 964 − 469 = 495. (L) Le réseau du 9, où vit 495, et le réseau plus un, où vit 496 : « La mémoire arithmétique n'a que deux adresses : le réseau, et le réseau plus le pas. » Le couple (495, 496) est, dit le Volume 4, l'emblème du triptyque : les deux adresses côte à côte.

**4.3 (Th, L, le demi porté ; Volume 4, V4.18.11 et V4.18.12).** (Th) 49 + 50 = 99, de milieu 49,5 ; 10 × 49,5 = 495 ; 4 × 49,5 = 198 ; 4 × 49 = 196. (L) « 495, le demi-point porté ; 196, le demi-point raté. » « Possession et privation du k_arc. »

**4.4 (L, le 7 ; Volume 1, É 9.3 et É 9.4).** Le 7 est au cube dans 6174, « au point de cristallisation de Kaprekar » ; c'est un des faits dont le Volume 1 dérive son sens : la connexion, l'inverse de ce qui sépare.

**4.5 (L, le tiroir des jouets ; Volume 3, R.11 ; Volume 4, V4.17.9).** 6174 a été rangé parmi les curiosités. « Le triptyque s'ouvre sur une question que personne ne posait, pourquoi 6174, et se ferme sur une réponse que personne n'attendait : les trois curiosités récréatives d'un calculateur indien de l'après-guerre sont trois lectures d'une même structure. Le comment des trois opérations contient intégralement leurs trois destins. Le comment contient le pourquoi. »

## 5. Ce qui manque

Le raisonnement propre du volet I n'a pas été retrouvé : l'ordre de ses énoncés et leurs numéros ; la façon dont il répondait à la question « pourquoi 6174 », que le Volume 4 lui attribue ; ses lectures qui n'ont pas été reprises ailleurs ; et ce qu'il disait, s'il en parlait, des largeurs autres que trois et quatre. Les énoncés 3.1 et 3.5 et la formule du pas de 3.3 sont ajoutés ici comme faits connus, pour que le tableau des largeurs soit complet ; rien n'atteste qu'ils étaient dans la pièce. Si le texte de juin 2026 reparaît, il remplace celui-ci.

## Annexe. Vérifications et sources

Script `kaprekar_verif.py` (Python 3, bibliothèque standard seule). Onze contrôles sur les calculs, tous conformes : le lemme sur 1 à 9999 et ses trois exemples ; le cycle à deux chiffres ; le pas, le point fixe et les six pas à trois chiffres ; l'échelle ; le pas, le point fixe, les 8 991 et les sept pas à quatre chiffres ; 6174 = 18 × 7³ ; les trois cycles à cinq chiffres ; 495 et 496 ; le demi-point. Un douzième contrôle porte sur la typographie de la source.

Sources : D. R. Kaprekar, « Another Solitaire Game », *Scripta Mathematica* 15, 1949. Corpus ARC : Volume 0, chapitre 3 ; Volume 1, É 9.1, É 9.3, É 9.4, É 16.26 ; Volume 3, R.10 et R.11 ; Volume 4, chapitres 17 à 19 ; Volume 6, É 5.4 et É 5.5 ; Volume 8, 10.32.
