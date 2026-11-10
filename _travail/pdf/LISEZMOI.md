# Fabrication des PDF des volumes

Les PDF de `arc/pdf/` se refont à partir des chapitres HTML de `arc/volumes/`, dans l'ordre de `arc/corpus.json`.

Outils : pandoc, xelatex, polices DejaVu Serif, DejaVu Sans Mono et FreeSerif (caractères absents de DejaVu).

    cd _travail/pdf && mkdir -p build
    python3 buildall.py            # les douze volumes
    python3 buildall.py 2 6        # seulement les volumes 2 et 6

Pour chaque volume, `buildall.py` écrit `build/VNN.pdf` et affiche : pages de l'ancien PDF et du nouveau, caractères manquants, erreurs, mots retirés et ajoutés par rapport au PDF en place. Ne copier un PDF dans `arc/pdf/` qu'après avoir lu cette ligne.

Réglages : classe report, 11 points, marges 2,5 cm, format lettre, table des matières à deux niveaux. Le Volume 3 fait exception : ses Parties sont les chapitres du PDF, ses chapitres et annexes en sont les sections, et sa table des matières a trois niveaux.

Si le nombre de pages change, le reporter dans `arc/corpus.json` (`pages`, `pages_total`), dans les pages d'index des volumes (fr, en, pt), les accueils, les bibliothèques et `arc/index.html`.

Les blocs préformatés trop larges pour la page (la table des ponts du Volume 3, par exemple) sont réduits juste assez pour tenir, sans rien couper : `buildall.py` le fait sur le fichier .tex avant la composition.

Contrôle à faire à chaque fois : aucun mot tronqué. Un mot nouveau qui est le début d'un mot disparu (« calc » pour « calcul ») signale un texte coupé au bord de la page.

État au 10 novembre 2026 : Volumes 0, 1, 2, 3, 4, 6 et 7 refaits avec ce script ; le Volume 9 ressort identique au PDF en place. Les Volumes 5, 8, 10 et 11 ne sont pas encore reproduits à l'identique : comparer avant de remplacer.
