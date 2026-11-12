# bastosfilipe.com

Site statique du corpus ARC (Architecture de la Cohérence Relationnelle), Filipe Bastos, CC BY 4.0.

Adresses du site :

- Accueil : https://bastosfilipe.com/
- Corpus ARC : https://bastosfilipe.com/arc/
- Bibliothèque des documents : https://bastosfilipe.com/bibliotheque-des-documents/
- English : https://bastosfilipe.com/en/
- Português : https://bastosfilipe.com/pt/
- Plan du site : https://bastosfilipe.com/sitemap.xml
- Guide pour les moteurs de réponse : https://bastosfilipe.com/llms.txt

- `index.html`, `bio/`, `bibliotheque-des-documents/` : les pages du site.
- `arc/` : le corpus en ligne (douze volumes en HTML et PDF, dossiers, fiches, `corpus.json`, `sitemap.xml`, `llms.txt`).
- `assets/` : feuilles de style du site et figure fondamentale.
- `_headers` : en-têtes servis par Cloudflare Pages.
- `_travail/` : blocs et consignes de la mise à jour du 26 octobre 2026 (archive).

Publication : Cloudflare Workers (fichiers statiques), relié à ce dépôt par l'intégration Git de Cloudflare ; configuration dans `wrangler.jsonc`, exclusions dans `.assetsignore`. Chaque commit sur `main` est mis en ligne.

En attente : l'identifiant Google Analytics (G-…) du site, à rétablir dans l'en-tête des trois pages et du gabarit de `/arc/`.
