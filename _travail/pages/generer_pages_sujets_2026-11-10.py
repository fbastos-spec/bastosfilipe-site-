import re, json, os, html
R='/home/claude/bastosfilipe-site-/'
tpl=open(R+'sujets/borne-de-tsirelson/index.html',encoding='utf-8').read()
head_end=tpl.index('<body'); main_a=tpl.index('<main'); main_b=tpl.index('</main>')+7
HEAD=tpl[:head_end]; NAV=tpl[head_end:main_a]; FOOT=tpl[main_b:]
st=lambda s:f'<span class="q-st">{s}</span>'
F,T,L,P=st('Fait'),st('Théorème'),st('Lecture'),st('Prédiction')
V='/arc/volumes/'
PAGES=[
dict(slug='modulo',eyebrow='Modulo',title="Le modulo expliqué simplement : ce qu'il garde, ce qu'il jette",
 desc="Le modulo, c'est le reste d'une division : l'heure sur une horloge, le compteur d'une voiture qui revient à zéro. Ce qu'il garde, ce qu'il jette, et ce qui arrive quand on prend ce reste pour le nombre.",
 rep="Le modulo garde le reste d'une division et jette le nombre de tours. Sur une horloge, 15 heures et 3 heures tombent au même endroit : l'aiguille dit où l'on est dans le tour, pas combien de tours ont été faits. C'est très utile, et ça devient dangereux dès qu'on prend ce reste pour le nombre entier.",
 body=[("Le modulo, c'est une horloge",[
  F+"Une horloge compte de 1 à 12, puis recommence. À 15 heures, l'aiguille montre le 3. Les mathématiciens écrivent : 15 modulo 12 égale 3. On a enlevé un tour de 12, et on a gardé ce qui dépasse.",
  F+"Le compteur d'une vieille voiture fait la même chose. Il a six chiffres : après 999 999 kilomètres, il affiche 000 000. La voiture n'est pas neuve. Le compteur a fait un tour complet, et ce tour n'est écrit nulle part.",
  "Le modulo n'est donc pas une erreur de calcul. Il répond juste à une question précise : <em>où en est-on dans le tour ?</em> Il ne répond pas à l'autre question : <em>combien de tours a-t-on faits ?</em>"]),
 ("Ce qu'il garde, ce qu'il jette",[
  T+"Tout nombre entier s'écrit d'une seule façon comme <em>des tours de 9, plus une position</em>. Par exemple 19 = 2 tours de 9, plus 1. Et 28 = 3 tours de 9, plus 1. Le corpus ARC compte les positions de 1 à 9 : 18, c'est un tour, et la position 9.",
  T+"10, 19, 28 et 1 000 000 ont tous la même position : 1. Si on ne garde que la position, ces quatre nombres deviennent le même. Et on ne peut pas revenir en arrière : à partir de « position 1 », personne ne peut dire de quel nombre on est parti.",
  T+"On peut mesurer la perte. Parmi le premier million de nombres, 111 112 ont la position 1. Dire seulement « position 1 », c'est donc laisser 111 112 candidats. En comptant l'information comme le font les ingénieurs (en bits), la position parmi neuf garde 3,17 bits sur 19,93 : 84 % de ce que le nombre portait est jeté."]),
 ("Quand la position suffit, et quand elle ne suffit pas",[
  T+"La position suffit pour certaines questions. Un nombre est divisible par 3 exactement quand sa position est 3, 6 ou 9 : on n'a pas besoin des tours.",
  T+"Elle ne suffit pas pour d'autres. 10 et 19 ont la même position : l'un est pair, l'autre impair. 19 et 28 ont la même position : l'un est premier, l'autre non. Chaque fois que la réponse dépend du tour, le modulo ne peut pas la donner."]),
 ("Quand on a pris le reste pour le nombre",[
  F+"Dans un ordinateur, un compteur a un nombre fixe de chiffres. Quand il est plein, il revient à zéro, comme le compteur de la voiture. Si le programme croit que ce zéro est le vrai nombre, il se trompe.",
  F+"C'est arrivé. En 1987, dans la machine de radiothérapie Therac-25, un compteur qui revenait à zéro au 256ᵉ passage a fait sauter une vérification, et un patient est mort d'une surdose. En 2015, les autorités ont imposé de redémarrer les Boeing 787 avant qu'un compteur n'arrive au bout, à 248 jours. En 1999 et en 2019, des récepteurs GPS se sont crus vingt ans plus tôt. <a href=\"/sujets/boeing-787-248-jours/\">Le cas du Boeing, avec son calcul.</a>"]),
 ("La lecture du corpus ARC",[
  L+"Le corpus ne reproche pas au modulo de mal calculer. Il lui reproche ce qu'on en a fait : prendre la position pour le nombre, et oublier que les tours existaient. Il date ce geste de Gauss, en 1801, quand le 9 a été écrit 0 : la fin du tour confondue avec le vide.",
  T+"Garder les tours, c'est tout garder. Si l'on note la position, puis la position du nombre de tours, et ainsi de suite, on retrouve le nombre entier sans rien perdre. 2026 s'écrit ainsi 2, 6, 9, 1, parce que 2 × 729 + 6 × 81 + 9 × 9 + 1 = 2026.",
  L+"« C'est l'outil qui est jugé, non ceux qui s'en sont servis. »"]),
 ("Ce que cette page ne dit pas",[
  "Elle ne dit pas que le modulo est faux, ni qu'il faut l'abandonner. Là où perdre est le but, il est à sa place : le chiffrement qui protège un mot de passe ou un paiement repose justement sur un chemin du retour qu'on a jeté.",
  "Elle ne lui impute pas tout. Le missile Patriot de 1991 a dérivé à cause d'une décimale coupée, pas d'un reste : c'est un autre geste, et le corpus les sépare."])],
 links=[("/arc/dossiers/lire/Modulo_v2_1/","Modulo : le dossier complet, avec ses théorèmes et ses sources"),("/arc/dossiers/Modulo_v2_1.pdf","Modulo (PDF)"),(V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos","Volume 3, chapitre 14 : la formule du chaos"),("/arc/dossiers/modulo_chaos_verif.py","Le script qui refait les calculs")],
 vois=["boeing-787-248-jours","effet-papillon","nombres-premiers"]),

dict(slug='boeing-787-248-jours',eyebrow='Boeing 787',title="Pourquoi le Boeing 787 devait être redémarré avant 248 jours",
 desc="En 2015, l'autorité américaine de l'aviation a imposé d'éteindre et de rallumer les Boeing 787 : un compteur interne débordait après 248 jours. Le fait, le calcul, et le geste qu'il y a derrière.",
 rep="Parce qu'un compteur interne, laissé sous tension sans arrêt, arrivait au bout de sa place après 248 jours et repartait de zéro. À cet instant, les boîtiers qui pilotent les générateurs électriques passaient en mode de sécurité, et l'avion pouvait perdre son courant. L'autorité américaine a imposé d'éteindre et de rallumer l'avion au moins tous les 120 jours, puis de corriger le logiciel.",
 body=[("Ce qui est établi",[
  F+"La directive AD 2015-09-07 de l'administration fédérale de l'aviation des États-Unis, en vigueur le 1ᵉʳ mai 2015, l'écrit : « un 787 alimenté sans interruption pendant 248 jours peut perdre toute son alimentation électrique en courant alternatif », à cause d'« un compteur logiciel interne aux unités de contrôle des générateurs, qui déborde après 248 jours d'alimentation continue ».",
  F+"Si les quatre unités principales ont été mises sous tension en même temps, elles basculent ensemble, « quelle que soit la phase de vol ». La directive mentionne une possible perte de contrôle de l'avion. Elle impose une mise hors tension au moins tous les 120 jours.",
  F+"Une seconde directive, AD 2018-20-15, en vigueur le 20 novembre 2018, exige un nouveau logiciel dans les six unités de l'avion."]),
 ("Le calcul, à refaire soi-même",[
  "Un compteur d'ordinateur ressemble au compteur kilométrique d'une voiture : il a un nombre fixe de chiffres, et quand il est plein, il revient à zéro.",
  T+"Un compteur de 31 chiffres binaires peut compter jusqu'à 2³¹, soit 2 147 483 648. S'il compte des centièmes de seconde, il est plein après 21 474 836 secondes. Une journée dure 86 400 secondes. Donc : 21 474 836 ÷ 86 400 = 248,55 jours.",
  F+"Honnêteté sur ce calcul : aucune des deux directives ne publie la taille du compteur ni son unité. Le compteur de 31 chiffres binaires en centièmes de seconde est une déduction, faite à partir de la concordance avec les 248 jours. Ce que l'autorité écrit, elle, noir sur blanc, c'est le geste : un compteur qui déborde."]),
 ("Le même geste, ailleurs",[
  F+"Therac-25, 1987 : dans une machine de radiothérapie, un compteur d'un seul octet revenait à zéro à son 256ᵉ passage. À zéro, une vérification était sautée. Un patient en est mort.",
  F+"GPS, 1999 et 2019 : le numéro de semaine tient sur dix chiffres binaires et revient à zéro toutes les 1024 semaines, soit 19,6 ans. Un récepteur qui prend ce reste pour la date se croit vingt ans plus tôt.",
  P+"2038 : beaucoup de systèmes comptent les secondes depuis le 1ᵉʳ janvier 1970 sur 32 chiffres binaires. Le compteur atteint sa limite le 19 janvier 2038 à 03 h 14 min 07 s. Tout système non corrigé qui revient au départ affichera alors le 13 décembre 1901."]),
 ("La lecture du corpus ARC",[
  L+"Les ingénieurs ont un nom pour le défaut : « débordement d'entier ». Ils n'ont pas de nom pour le geste qu'il y a dessous. Le corpus le nomme : <em>prendre le reste pour le nombre</em>. Le compteur garde la position dans le tour et jette le tour. C'est le <a href=\"/sujets/modulo/\">modulo</a>, câblé dans la machine.",
  L+"« Dans chaque cas, le remède a été de garder plus de tours » : des compteurs plus longs, des années sur quatre chiffres, des semaines sur treize chiffres binaires."]),
 ("Ce que cette page ne dit pas",[
  "Elle ne dit pas qu'un 787 est tombé à cause de ce compteur : la directive est une mesure de précaution, et le corpus ne rapporte aucun accident de cet avion lié à ce défaut.",
  "Elle ne met pas tout sur le compte du reste. Le missile Patriot de 1991 a dérivé de 0,34 seconde à cause d'une décimale coupée : c'est un autre geste, que le corpus traite à part."])],
 links=[("/arc/dossiers/lire/Modulo_v2_1/","Modulo, partie 5 : les morts et les pannes, avec les sources"),("/arc/dossiers/Modulo_v2_1.pdf","Modulo (PDF)"),("/arc/dossiers/modulo_chaos_verif.py","Le script qui refait les calculs")],
 vois=["modulo","effet-papillon"]),

dict(slug='pyramide-de-kheops-pi',eyebrow='Pyramide de Khéops',title="La pyramide de Khéops et π : ce que dit vraiment le seked",
 desc="La pyramide de Khéops cache-t-elle le nombre π ? Sa pente, le seked de 5 paumes et demie, donne exactement 44/7 : le calcul, les mesures, et ce qu'elles ne permettent pas de trancher.",
 rep="Les bâtisseurs de Khéops n'avaient pas besoin de connaître π. Ils ont choisi une pente simple, le seked : 5 paumes et demie de recul pour 7 paumes de montée. Avec cette pente, le tour de la base vaut exactement 44/7 fois la hauteur, soit deux fois 22/7, un nombre très proche de 2π. La ressemblance avec π vient de la pente, pas d'un secret.",
 body=[("Ce qui est établi",[
  F+"Les Égyptiens réglaient la pente d'une pyramide par le <em>seked</em> : de combien on recule à l'horizontale chaque fois qu'on monte d'une coudée. Une coudée vaut 7 paumes. Le seked de Khéops est de 5 paumes et demie.",
  F+"Les relevés donnent une hauteur d'environ 146,6 mètres et une demi-base de 115,2 mètres. La hauteur divisée par la demi-base vaut 1,2726."]),
 ("Le calcul, à refaire soi-même",[
  T+"Monter de 7 en reculant de 5,5, c'est une pente de 7 ÷ 5,5 = 14/11 = 1,2727. C'est le nombre mesuré, à un dix-millième près.",
  T+"Le tour de la base fait 8 demi-bases. Divisé par la hauteur, cela donne 8 × 11/14 = 44/7 = 6,2857. Or 2π vaut 6,2832. Voilà d'où vient la « pyramide de π » : de 22/7, la fraction simple que la pente fabrique toute seule.",
  T+"La figure du corpus ARC, deux cercles et un carré, repliée en pyramide, donne de son côté une pente de 1,2720, la racine du nombre d'or. Trois nombres se tiennent donc dans un mouchoir : 1,2720 par la figure, 1,2726 par la mesure, 1,2727 par le seked."]),
 ("Ce que les mesures ne tranchent pas",[
  F+"Le rapport mesuré est à 0,012 % de 44/7 et à 0,053 % de 2π. Mais les relevés de Petrie ont une marge d'erreur de 0,03 % à 0,21 %. Les deux écarts sont plus petits que cette marge : la mesure ne départage pas.",
  F+"Le corpus avait d'abord écrit « accord exact » avec le nombre d'or. Il a retiré cette formule en septembre 2026, pour la même raison : l'écart est dans la marge d'erreur. Le retrait est gardé, daté, dans le Registre."]),
 ("La lecture du corpus ARC",[
  L+"Khéops n'approxime pas π : elle inscrit un rapport fermé, 14/11, qui se construit avec une corde et des paumes. La « pyramide de π » des livres en est une conséquence, non une cause.",
  L+"Ce que la figure ajoute, c'est que la même pente sort d'un carré tenu entre deux cercles, sans aucune mesure. Que les bâtisseurs l'aient su ou non, le corpus ne le dit pas."]),
 ("Ce que cette page ne dit pas",[
  "Elle ne dit pas que les Égyptiens connaissaient π ou le nombre d'or. Elle ne dit pas qu'un message est caché dans la pyramide. Elle dit trois choses vérifiables : la pente est un rapport simple, ce rapport donne 44/7, et les mesures sont trop larges pour choisir entre les explications."])],
 links=[(V+"v02-la-figure/06-chapitre-5-le-carre-illusion-et-l-origine-geometri","Volume 2, chapitre 5 : le carré plié et la géométrie de Khéops"),(V+"v02-la-figure/05-chapitre-4-deux-cercles-et-un-carre-le-double-et-l","Volume 2, chapitre 4 : deux cercles et un carré"),(V+"v03-le-code-et-le-registre/05-chapitre-3-les-gestes-historiques-et-leurs-resolut","Volume 3, chapitre 3 : « Khéops ne départage pas »")],
 vois=["hippase-racine-de-2","borne-de-tsirelson"]),

dict(slug='hippase-racine-de-2',eyebrow='Hippase',title="Qu'a vraiment découvert Hippase ? La diagonale du carré et √2",
 desc="Hippase a montré que la diagonale d'un carré ne s'écrit pas comme une fraction de son côté. Crise des mathématiques, ou mauvaise question ? Le calcul du carré doublé, et la lecture du corpus ARC.",
 rep="Hippase a montré que la diagonale d'un carré ne s'écrit pas comme une fraction de son côté. La tradition en a fait une crise : un nombre « irrationnel », sans raison. Le corpus ARC lit autre chose. La diagonale se trace, se mesure et sert très bien ; ce qui a échoué, c'est la demande de l'écrire comme un rapport de deux nombres entiers.",
 body=[("Ce que la tradition établit",[
  F+"Vers 450 avant notre ère, Hippase de Métaponte, de l'école de Pythagore, étudie la diagonale d'un carré de côté 1. Il trouve qu'aucune fraction, aussi fine soit-elle, ne donne exactement sa longueur : la diagonale et le côté n'ont pas de mesure commune.",
  F+"On écrit aujourd'hui cette longueur √2 = 1,41421356…, avec des décimales qui ne finissent pas et ne se répètent pas. Ce résultat est démontré, et il reste vrai."]),
 ("Le calcul, à refaire avec un crayon",[
  T+"Trace un carré de côté 1, puis construis un second carré sur sa diagonale. Ce grand carré se découpe en quatre triangles, et chacun a une aire de 1/2. Son aire vaut donc 2 : il est exactement le double du premier.",
  T+"Autrement dit : la diagonale, multipliée par elle-même, donne 2. Pas à peu près, exactement. C'est le problème que Socrate fait résoudre à un jeune esclave dans le <em>Ménon</em> de Platon : pour doubler un carré, on le construit sur sa diagonale.",
  T+"Une queue de décimales sans fin n'est pas toujours la marque d'un mystère. Un tiers s'écrit 0,333… quand on compte par dix, et tout simplement 0,1 quand on compte par trois. La queue vient parfois de l'écriture, pas de la chose."]),
 ("La lecture du corpus ARC",[
  L+"Le mot grec <em>alogos</em>, qu'on traduit par « irrationnel », nomme l'échec d'une demande : exprimer la diagonale par un rapport de deux entiers. Il ne nomme pas un défaut de la diagonale, qui est construite, mesurable et qui marche.",
  L+"La diagonale est exacte comme relation : son carré vaut 2. Elle n'est sans fin que comme quantité écrite en décimales. La crise n'était pas dans la diagonale, mais dans la question qu'on lui a posée.",
  L+"Le corpus y voit un moule qui se répète ensuite, chez Stevin, chez Gauss, chez Riemann : on pose une demande de fondement à quelque chose qui fonctionnait, on obtient un objet impossible, et on lui donne le nom de l'impossibilité."]),
 ("Ce que cette page ne dit pas",[
  "Elle ne conteste pas la démonstration : √2 n'est une fraction dans aucune façon de compter, ni par dix, ni par trois, ni autrement. Le corpus le dit lui-même. Ce qu'il discute, c'est le mot « irrationnel » et la crise qu'on en a tirée, pas le théorème."]),
 ("Ce qui ferait tomber cette lecture",[
  P+"Le corpus avance que toute crise des fondements, dans l'histoire des mathématiques, vient d'une demande de justification posée à un calcul qui fonctionnait. Une crise née d'un calcul qui cesse de marcher tout seul, sans aucune demande de ce genre, la réfuterait."])],
 links=[(V+"v06-l-histoire-de-la-preuve/15-chapitre-12-le-probleme-qui-a-cree-le-probleme-hip","Volume 6, chapitre 12 : le problème qui a créé le problème, Hippase"),(V+"v06-l-histoire-de-la-preuve/14-chapitre-11-le-pourquoi-indecidable-anthologie-de","Volume 6, chapitre 11 : le pourquoi indécidable, avec le Ménon"),(V+"v02-la-figure/02-chapitre-1-la-figure-fondamentale","Volume 2, chapitre 1 : la figure fondamentale et √2")],
 vois=["pyramide-de-kheops-pi","borne-de-tsirelson","modulo"]),

dict(slug='effet-papillon',eyebrow='Effet papillon',title="L'effet papillon est-il dans la nature ou dans le calcul ?",
 desc="L'effet papillon et la théorie du chaos : d'où vient la divergence dans les calculs ? Une mesure coupée, un compteur de tours jeté, et un test qu'on refait en quelques lignes.",
 rep="Dans les calculs où on l'a découvert, l'effet papillon vient de deux gestes de l'outil : une mesure coupée au départ, et un compteur de tours jeté à chaque pas. Quand on garde le compte des tours, on remonte le calcul exactement. Le corpus ARC en conclut que ce chaos-là est fabriqué par le calcul. Pour la vraie atmosphère, la question reste ouverte, et le corpus le dit.",
 body=[("Ce qui est établi",[
  F+"En 1961, le météorologue Edward Lorenz relance une simulation en retapant un nombre à trois décimales, 0,506, au lieu des six que la machine gardait, 0,506127. Les deux calculs se séparent complètement. Il publie en 1963. On en a tiré l'image du papillon dont le battement d'aile changerait le temps à l'autre bout du monde.",
  F+"Le mécanisme est connu des mathématiciens : un calcul qui étire puis replie, et qui perd à chaque pas un peu de ce qu'il savait. Le corpus ne prétend pas l'avoir découvert. Ce qu'il propose, c'est une lecture."]),
 ("Deux coureurs sur une piste",[
  "Imagine deux coureurs sur une piste ronde. Tu les photographies : ils sont au même endroit. Tu en conclus qu'ils sont ensemble. Mais l'un a fait 51 tours et l'autre 52. La photo montre la position, pas le nombre de tours. C'est exactement ce que fait un calcul qui « replie ».",
  T+"Le calcul, à refaire : pars de 1/5, et d'un nombre tout proche, 1/5 + 1/256. À chaque pas, double le nombre et ne garde que ce qui vient après la virgule. L'écart double à chaque pas. Au huitième pas, les deux nombres ont la même position, 1/5. Leurs tours jetés, additionnés, valent 51 pour l'un et 52 pour l'autre. Aucune décimale n'a été coupée : tout est en fractions exactes."]),
 ("Les trois formules du chaos",[
  T+"Une seule écriture : l'écart après n pas vaut l'écart de départ multiplié n fois par un même facteur. Le corpus y distingue trois moteurs, et chacun suffit seul.",
  T+"<strong>La graine coupée.</strong> On écrit un tiers comme 0,3333. Il manque un trente-millième. Multiplié par 3 à chaque pas, sans rien replier, ce manque devient, en cent pas, un nombre de 44 chiffres.",
  T+"<strong>Le pli.</strong> La mesure est parfaite, mais à chaque pas on garde la position et on jette le tour. Ce sont les deux coureurs.",
  T+"<strong>La machine.</strong> Un ordinateur fait les deux à la fois. Il garde 52 chiffres binaires ; le doublement en demande un de plus à chaque pas ; au pas 53, il ne reste rien du départ."]),
 ("Ce qui se passe quand on garde les tours",[
  T+"Si l'on note le tour jeté à chaque pas, on remonte au point de départ sans aucune erreur, aussi loin qu'on veut. Dans les calculs étudiés, la confusion disparaît dès que le compte des tours est gardé.",
  F+"Vérification indépendante : en 2018, Saito et Yamaguchi simulent ce même calcul en arithmétique exacte, sans aucun arrondi. Il reste chaotique. Le chaos du pli ne vient donc pas de l'arrondi : il vient du tour jeté."]),
 ("La lecture du corpus ARC",[
  L+"« L'effet papillon n'est pas le battement d'une aile : c'est le sort d'un compteur de tours que le repliement jette. » On a confondu le système et la mesure du système. Ce que Lorenz a vu diverger, ce sont des nombres traités par un outil qui mesure, ce qui est légitime, puis qui replie en oubliant."]),
 ("Ce que cette page ne dit pas",[
  "Elle ne dit pas qu'on peut prévoir la météo indéfiniment. Toute mesure est finie, et le corpus tient cette limite pour légitime : ce n'est pas elle qu'il accuse.",
  "Elle ne tranche pas pour les équations de Lorenz elles-mêmes. Les refaire en arithmétique exacte est un chantier ouvert du corpus, déclaré comme tel."]),
 ("Ce qui ferait tomber cette lecture",[
  P+"Produire un système où deux départs différents deviennent impossibles à distinguer alors que l'opération garde le compte des tours. Le corpus affirme que cela n'arrive pas, et donne le test pour le vérifier."])],
 links=[(V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos","Volume 3, chapitre 14 : la formule du chaos"),("/arc/dossiers/lire/Les_trois_corps_n_ont_jamais_bouge/","Les trois corps n'ont jamais bougé"),("/arc/dossiers/lire/Modulo_v2_1/","Modulo : la formule II du chaos est son geste"),("/arc/dossiers/modulo_chaos_verif.py","Le script qui refait les calculs")],
 vois=["modulo","boeing-787-248-jours","physique-quantique"]),
]
TIT={p['slug']:p['title'] for p in PAGES}
for s in ['borne-de-tsirelson','intrication-quantique','physique-quantique','hypothese-de-riemann','nombres-premiers','probleme-difficile-de-la-conscience','crise-de-panique','gauche-droite']:
    t=open(R+f'sujets/{s}/index.html',encoding='utf-8').read()
    TIT[s]=html.unescape(re.search(r'<h1 class="entry-title">(.*?)</h1>',t).group(1))
def exists(u):
    p=R+u.strip('/')
    return any(os.path.exists(x) for x in (p+'.html',os.path.join(p,'index.html'),p))
e=lambda s:html.escape(s,quote=True)
for p in PAGES:
    url=f"https://bastosfilipe.com/sujets/{p['slug']}/"
    h=HEAD
    od=re.search(r'<meta name="description" content="([^"]*)"',h).group(1)
    h=h.replace(od,e(p['desc']))
    ot=re.search(r'<title>(.*?) · Filipe Bastos</title>',h).group(1)
    h=h.replace(f'<title>{ot} · Filipe Bastos</title>',f"<title>{e(p['title'])} · Filipe Bastos</title>")
    h=h.replace(f'content="{ot}"',f'content="{e(p["title"])}"')
    h=h.replace('https://bastosfilipe.com/sujets/borne-de-tsirelson/',url)
    h=re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">','',h)
    ld={"@context":"https://schema.org","@graph":[{"@type":"Article","headline":p['title'],"description":p['desc'],"inLanguage":"fr","url":url,"author":{"@type":"Person","@id":"https://bastosfilipe.com/#filipe-bastos","name":"Filipe Bastos","url":"https://bastosfilipe.com/bio/"},"publisher":{"@id":"https://bastosfilipe.com/#filipe-bastos"},"license":"https://creativecommons.org/licenses/by/4.0/","datePublished":"2026-11-10","dateModified":"2026-11-10","isPartOf":{"@id":"https://bastosfilipe.com/#site"},"about":p['eyebrow']},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":p['title'],"acceptedAnswer":{"@type":"Answer","text":p['rep']}}]},{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Filipe Bastos","item":"https://bastosfilipe.com/"},{"@type":"ListItem","position":2,"name":"Les grandes questions","item":"https://bastosfilipe.com/sujets/"},{"@type":"ListItem","position":3,"name":p['eyebrow'],"item":url}]}]}
    h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>',h,flags=re.S)
    assert 'Tsirelson' not in h and 'tsirelson' not in h, re.findall(r'.{40}sirelson.{40}',h)[:2]
    b=[f'<main id="content" data-pagefind-meta="title:{e(p["title"])}">','<div class="wrap page-shell q-page">','<p class="q-bc" style="font-size:.85rem;margin:0 0 6px"><a href="/sujets/">Les grandes questions</a></p>',f'<span class="sec-eyebrow">{p["eyebrow"]}</span>',f'<h1 class="entry-title">{p["title"]}</h1>',f'<div class="q-rep"><span class="sec-eyebrow">La réponse courte</span><p>{p["rep"]}</p></div>']
    for h2,ps in p['body']:
        b.append(f'<h2>{h2}</h2>'); b+= [f'<p>{x}</p>' for x in ps]
    for u,_ in p['links']: assert exists(u),u
    b.append('<h2>Pour aller plus loin</h2>'); b.append('<ul class="q-links">'+''.join(f'<li><a href="{u}">{t}</a></li>' for u,t in p['links'])+'</ul>')
    b.append('<h2>Questions voisines</h2>'); b.append('<ul class="q-links">'+''.join(f'<li><a href="/sujets/{s}/">{TIT[s]}</a></li>' for s in p['vois'])+'<li><a href="/sujets/">Les grandes questions</a></li></ul>')
    b.append('<p class="q-meta">Chaque énoncé porte son statut : Fait (ce que la science tient), Théorème (calcul vérifié), Lecture (interprétation du corpus), Prédiction (ce qui la ferait tomber).<br>Filipe Bastos · Corpus ARC · CC BY 4.0 · <a href="/#methode">Méthode de lecture : l\'Empathie fractale, sociale et relationnelle</a> · <a href="/contradictions/">Une erreur ? Envoyez une contradiction</a></p>')
    b+=['</div>','</main>']
    out=h+NAV+'\n'.join(b)+FOOT
    assert '—' not in out and '–' not in '\n'.join(b)
    os.makedirs(R+f"sujets/{p['slug']}",exist_ok=True)
    open(R+f"sujets/{p['slug']}/index.html",'w',encoding='utf-8').write(out)
    print(p['slug'],len(out))
json.dump([{k:p[k] for k in ('slug','title','desc')} for p in PAGES],open('/home/claude/pages/pages.json','w'),ensure_ascii=False)
