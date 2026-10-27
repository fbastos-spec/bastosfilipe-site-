# Mise à jour du corpus ARC sur bastosfilipe.com, 26 octobre 2026

Ce paquet remplace le précédent (« Accueil et Bibliothèque »). Il contient le dossier `arc/` complet et corrigé, treize dossiers PDF, les deux blocs HTML à recoller, et les corrections de texte des pages. Même procédure que la dernière fois ; les différences sont listées à la section « Ce qui change ».

## Contenu

```
arc/                      le corpus complet, corrigé : 12 volumes (PDF + chapitres HTML), fiches, corpus.json, sitemap
dossiers/                 14 PDF à déposer dans /arc/dossiers/ (8 déjà en ligne, inchangés, + 6 nouveaux)
bloc_accueil.html         les 12 volumes et les 4 dossiers les plus récents (accueil)
bloc_bibliotheque.html    les 12 volumes et les 14 dossiers (Bibliothèque des documents)
bio_complete.html         la page Bio, avec les corrections de la section 4
ajouts_presentation.html  inchangé depuis le paquet précédent
```

## Ce qui change par rapport au paquet précédent

- Volumes 2, 3, 6 et 8 : PDF et chapitres HTML corrigés (règle du chaos, Registre v1.5, gravure G.70). Volume 7 : PDF et chapitres corrigés (gravure G.69 : inversion, chapitres 3, 9, 10, annexe B.13). Volume 0 rebâti pour la carte du corpus corrigée. `corpus.json`, les blocs et les pages d'index portent les nombres de pages des PDF déposés.
- Volumes 4 et 5 : PDF remplacés par les versions à jour de l'auteur (167 et 106 pages). Leurs chapitres HTML portent déjà le même texte (vérifié mot à mot le 26 octobre 2026) ; ils restent tels quels.
- Six nouveaux dossiers : Collatz v2.2, Le fini et l'infini mêlés v1.2, Ce qui vous manque v1.1, Le Zéro non construisible v0.2, Cosmic Dipole Resolution v1.5, Benford sans Neper v0.1 (26 octobre). Sur l'accueil, Benford remplace Heegner parmi les quatre dossiers récents.
- Deux fichiers retirés : `arc/Fiches_des_volumes.pdf` et `arc/pdf/Faire_tomber_ARC.pdf` (doublon ; le dossier reste sous `/arc/dossiers/`).
- Volume 3 : les ajouts v1.4 du Registre (R.161, R.162, G.69) sont fusionnés dans les chapitres 11 et 12.
- Sept pièces de l'auteur entrées mot pour mot comme nouveaux chapitres, avec leurs annexes A et C mises à jour, les fichiers d'annexes renumérotés et les PDF rebâtis : Volume 0, chapitre 8 (Le Figuier étrangleur) ; Volume 3, chapitres 22 et 23 (Le Chaos Fabriqué Partie I ; Le Pont de l'illusion) ; Volume 4, chapitre 22 (La congruence des paires) ; Volume 5, chapitre 12 (Trois questions non avenues) ; Volume 8, chapitre 16 (Là où la règle se trompe) ; Volume 9, chapitre 12 (Le Corps Comptable). Les anciens fichiers d'annexes de ces six volumes changent de nom (décalés d'un rang) : le remplacement du dossier `/arc/` en entier, étape 2, suffit ; `sitemap.xml` et `corpus.json` sont à jour.
- Dossier Faire tomber ARC : la v1.0 (10 p.) est remplacée par la v2.0 (38 p.), même nom de fichier, même adresse ; `dossiers/faire_tomber_extract.py` est le script qui l'a produite (à déposer à côté, dans `/arc/dossiers/`).
- Accueil : la page s'ouvre désormais sur la figure fondamentale (deux cercles et un carré) et sur trois paragraphes qui en partent ; le Volume 2 passe en tête des cartes. Bibliothèque : l'accroche part de la figure et de la constante ½.
- Résumés corrigés (Volumes 1 et 10) ; nombres de pages de tous les volumes réalignés sur les PDF déposés dans les blocs, `arc/index.html` et les pages de volume ; total 1714.

## Avant tout : ne rien perdre au déploiement

- **Garder l'en-tête actuel du site** (header WordPress : logo, menu, styles du thème) tel quel. Les blocs de ce paquet se collent *dans* les pages existantes ; ils ne remplacent ni le thème, ni l'en-tête, ni le pied de page.
- **Garder Google Analytics.** Le code de suivi en place (balise gtag ou Google Tag Manager, dans le thème ou dans une extension) doit rester actif sur toutes les pages après le déploiement, y compris sur les pages du dossier `/arc/` si elles le portaient avant : les fichiers de `arc/` dans ce paquet n'en contiennent pas. Si le suivi de `/arc/` se faisait par une injection côté serveur ou par le thème, ne pas la retirer ; s'il se faisait par une balise dans les fichiers HTML, me la transmettre (l'identifiant G-… suffit) et je l'ajoute dans le gabarit des 300 pages avant la prochaine livraison.
- Avant de remplacer `/arc/`, en faire une copie de sauvegarde sur le serveur (`arc_sauvegarde_2026-10-26/`), pour pouvoir comparer et revenir en arrière.
- Après le déploiement, vérifier dans Google Analytics (temps réel) qu'une visite sur l'accueil et une visite sur une page de `/arc/` sont bien comptées.

## Étapes

0. **PHP, si ce n'est pas déjà fait.** Même consigne que le paquet précédent : PHP2Shell (CVE-2026-109618 et CVE-2026-109619), passer à PHP 8.2.35, 8.3.36, 8.4.27 ou 8.5.12, redémarrer PHP-FPM ou Apache, confirmer la version à Filipe.

1. **HTTPS.** Vérifier que https://bastosfilipe.com/arc/ ne redirige plus vers http://.

2. **Remplacer le dossier `/arc/`** du serveur par le dossier `arc/` de ce paquet, en entier (FTP). Supprimer ensuite sur le serveur, s'ils y sont encore : `/arc/Fiches_des_volumes.pdf` et `/arc/pdf/Faire_tomber_ARC.pdf`. Si un lien externe pointe vers `/arc/pdf/Faire_tomber_ARC.pdf`, rediriger (301) vers `/arc/dossiers/Faire_tomber_ARC.pdf`.

3. **Dossiers.** Déposer les 14 PDF de `dossiers/` dans `/arc/dossiers/`, sans les renommer (`Faire_tomber_ARC.pdf` remplace celui en ligne), ainsi que `faire_tomber_extract.py`. `P-B-1_les_pingouins.pdf` ne doit pas être modifié ni recompressé : empreinte SHA-256 4079d4ae9533a35753c0343d2fb4de7791571264b784bc7e5459cfbb1caea686.

4. **Pages du site (WordPress), corrections de texte.** Chaque ligne donne le texte exact à trouver et celui qui le remplace. Ne rien reformuler.
   - Accueil, paragraphe de présentation : le remplacer en entier par les trois paragraphes suivants (ils sont aussi dans `bloc_accueil.html`, section « ouverture », avec la figure ; si le bloc HTML est placé en tête de la page, ne pas répéter le texte deux fois : garder la version du bloc et supprimer l'ancien paragraphe).
     `Tout le corpus ARC repose sur une seule image, que l'on peut tracer à la main en quelques secondes : deux cercles qui ont le même centre, un carré coincé entre eux (ses quatre coins touchent le grand cercle, ses quatre côtés touchent le petit), et la diagonale de ce carré, qui traverse le tout.`
     `Le rapport des deux rayons est √2/2, et son carré vaut ½ : c'est la constante k = 1/2, d'où tout le reste se déplie, l'arithmétique, la physique et l'épistémologie. Le cadastre des neuf positions en est la conséquence, pas le point de départ.`
     `Chaque énoncé porte son statut : Théorème (calcul vérifié), Fait (ce que la science tient), Lecture, Prédiction ou Chantier. Rien n'est demandé au lecteur sauf de vérifier.`
   - Accueil, figure : `figure_fondamentale.svg` (à la racine du paquet, et copié dans `arc/assets/`) est déjà incorporé dans `bloc_accueil.html` ; rien à téléverser à part. Le bloc place maintenant le Volume 2, La Figure, en tête, marqué « commencer ici ».
   - Accueil, bloc des volumes : remplacer le bloc « HTML personnalisé » actuel par `bloc_accueil.html` (les 12 volumes, et non plus seulement 6 à 11 ; les 4 dossiers récents).
   - Bibliothèque des documents : remplacer le bloc par `bloc_bibliotheque.html`. Dans la section « Articles » existante (fiches Zenodo), remplacer les tirets longs : `P ≠ NP — Structural Irreversibility` → `P ≠ NP : Structural Irreversibility` ; `sont amorphes — le tiers inabsorbable` → `sont amorphes : le tiers inabsorbable` ; `Navier-Stokes — Discrete Volumetric Projection` → `Navier-Stokes : Discrete Volumetric Projection` ; description de La Formule du Chaos, remplacer la description entière par : `Trois formules, trois moteurs : la troncature seule (Stevin), le pli seul (Gauss), les deux ensemble (la machine). Chacune fabrique le chaos ; la troisième au maximum. n_chaos = p / log10(f), prédiction P1 vérifiée par calcul.` ; `somme à 11 ≠ 9 — la non-clôture` → `somme à 11 ≠ 9 : la non-clôture` ; `sans espace de Hilbert — la corrélation` → `sans espace de Hilbert : la corrélation` ; `géométrie cadastrale — avec prédictions` → `géométrie cadastrale, avec prédictions`.
   - Bio : remplacer le texte par `bio_complete.html`. Il contient déjà : `puis on produit la pièce` à la place de `puis on écrit`, et la signature `Filipe Bastos · ARC` à la place de `Filipe Bastos — ARC`. Le prénom de sa fille s'écrit « Yanie », partout.
   - Ensuite, chercher dans toutes les pages WordPress le caractère `—` (tiret long) et le remplacer par une virgule (incise) ou un deux-points (pivot). Signaler à Filipe les cas douteux au lieu de choisir.

5. **Vérifier**, dans une fenêtre privée, sur téléphone et sur ordinateur :
   - chaque bouton « Lire » et « PDF » de l'accueil et de la bibliothèque répond (12 volumes, 14 dossiers) ;
   - les nombres de pages affichés sont ceux des PDF déposés (Volume 0 : 103, Volume 1 : 139, Volume 2 : 133, Volume 3 : 201, Volume 4 : 166, Volume 5 : 104, Volume 6 : 170, Volume 7 : 138, Volume 8 : 115, Volume 9 : 94, Volume 10 : 186, Volume 11 : 165 ; total 1714) ;
   - les deux fichiers retirés ne répondent plus (404 ou 301) ;
   - aucune page ne contient plus `tous les nombres premiers, un axe`, `le 19,`, `suspendue, elle est`, `puis on écrit`.

6. **Google.** Resoumettre https://bastosfilipe.com/arc/sitemap.xml dans Google Search Console (il contient les 14 dossiers). Le `robots.txt` reste celui du paquet précédent.

## Ce qui viendra dans un prochain paquet

- Rien n'est en attente à la date de ce paquet.

*Corpus ARC, Filipe Bastos, CC BY 4.0. Paquet préparé le 26 octobre 2026. Toute question va à Filipe.*
