import re, json, os, html
R='/home/claude/bastosfilipe-site-/'; V='/arc/volumes/'; D='https://bastosfilipe.com'
ch=dict(
 chaos=V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos",
 pnp=V+"v05-les-grands-problemes/09-chapitre-8-p-contre-np-ii-le-mur-le-compte-et-le-p",
 cloche=V+"v04-la-theorie-des-nombres/23-chapitre-16-la-cascade-et-la-cloche-huygens-le-cer",
 pascal=V+"v04-la-theorie-des-nombres/22-chapitre-15-la-cascade-cadastrale-et-la-spirale-du",
 un=V+"v01-la-fondation/03-chapitre-2-l-operation-minimale-1-1-3",
 trait=V+"v01-la-fondation/02-chapitre-1-le-trait-qui-est-deja-trois",
 figure=V+"v02-la-figure/05-chapitre-4-deux-cercles-et-un-carre-le-double-et-l",
 paires=V+"v01-la-fondation/08-chapitre-7-les-deux-zeros-et-le-centre-vide",
 matrio=V+"v07-la-physique-relue/11-chapitre-10-l-atome-n-est-pas-une-brique-la-matrio",
 ponts=V+"v03-le-code-et-le-registre/27-chapitre-23-le-pont-de-l-illusion-le-tiers-impose-et-la-table",
 sept=V+"v01-la-fondation/09-chapitre-8-le-7-ou-le-chemin-qui-n-a-pas-de-lieu",
 pi=V+"v03-le-code-et-le-registre/05-chapitre-3-les-gestes-historiques-et-leurs-resolut",
 formes=V+"v07-la-physique-relue/12-chapitre-11-les-cordes-sans-cordes",
 pourquoi=V+"v01-la-fondation/14-chapitre-13-le-comment-lisible-et-le-pourquoi-inde",
 hasard=V+"v00-le-seuil/05-chapitre-2-le-lexique",
 n35=V+"v02-la-figure/08-chapitre-7-le-carre-notifie")
S={'fr':dict(modulo='/sujets/modulo/',boeing='/sujets/boeing-787-248-jours/',pap='/sujets/effet-papillon/',hip='/sujets/hippase-racine-de-2/',tsi='/sujets/borne-de-tsirelson/',intr='/sujets/intrication-quantique/',khe='/sujets/pyramide-de-kheops-pi/',prem='/sujets/nombres-premiers/'),
   'en':dict(modulo='/en/topics/modulo/',boeing='/en/topics/boeing-787-248-days/',pap='/en/topics/butterfly-effect/',hip='/en/topics/hippasus-square-root-of-2/',tsi='/en/topics/tsirelson-bound/',intr='/en/topics/quantum-entanglement/',khe='/en/topics/khufu-pyramid-pi/',prem='/en/topics/prime-numbers/'),
   'pt':dict(modulo='/pt/temas/modulo/',boeing='/pt/temas/boeing-787-248-dias/',pap='/pt/temas/efeito-borboleta/',hip='/pt/temas/hipaso-raiz-de-2/',tsi='/en/topics/tsirelson-bound/',intr='/en/topics/quantum-entanglement/',khe='/pt/temas/piramide-de-queops-pi/',prem='/en/topics/prime-numbers/')}
K=[['modulo','boeing','pap','chaos','pnp','cloche','pascal'],['un','n35','trait','figure','paires','hip','tsi','intr','matrio','ponts'],['sept','pi','khe','formes','prem','pourquoi','hasard']]
L={}
L['fr']=dict(url='/carte/',title='La carte du corpus : trois gestes, lus cent fois',nav='La carte',eyebrow='La carte du corpus',h1='Trois gestes, lus cent fois',fr='',
 desc="La carte du corpus ARC : trois gestes, retrouvés dans l'arithmétique, la physique, l'histoire et le vivant. Ce que l'outil jette, le tiers, la forme ouverte, et où chacun réapparaît.",
 chapo="Le corpus ARC a douze volumes. Ce ne sont pas des centaines d'idées. Ce sont trois gestes, retrouvés dans l'arithmétique, la physique, l'histoire et le vivant. Cette page dit lesquels, et où chacun réapparaît.",
 alt="Deux cercles concentriques et un carré entre eux",
 fig=[("Les deux cercles","Ce qui ferme : le tour complet, et le compte des tours qu'il ne faut pas jeter."),("Le carré","Le tiers : ce qui tient les deux cercles ensemble sans qu'ils se touchent."),("Le centre vide","Ce qui reste ouvert : 4,5, la place que personne n'occupe et par où tout passe.")],
 tr=[("Ce que l'outil jette","On garde la position, on jette le compte. Ou bien on coupe la queue du nombre. Dans les deux cas, ce qui manque n'est écrit nulle part."),("Le tiers","Ce qui est entre deux choses compte pour une. Deux termes qui se rencontrent en font toujours trois."),("La forme ouverte","Ce qui ne ferme pas est ce qui laisse passer : le chemin, le temps, le nouveau.")],
 c=dict(modulo=("Le modulo","Tout nombre est des tours de 9, plus une position. Le modulo garde la position et jette les tours."),
  boeing=("Les compteurs qui reviennent à zéro","Therac-25, Boeing 787, GPS, 2038 : le reste pris pour le nombre, câblé dans la machine."),
  pap=("L'effet papillon","Deux coureurs au même endroit de la piste, à 51 et 52 tours. Le chaos du pli est un compte de tours jeté."),
  chaos=("La décimale coupée","Un tiers écrit 0,333, multiplié deux fois : il manque 444. C'est le geste voisin, celui de Stevin."),
  pnp=("P contre NP","Les bits qu'on dit « aléatoires » sont exactement l'écriture du compte des tours que le pli a jeté."),
  cloche=("La cloche","La courbe en cloche est d'abord un compte de chemins, la ligne 8 du triangle de Pascal. La cascade garde le rang que la somme jette."),
  pascal=("Le triangle de Pascal","Chaque case se souvient de ses deux parents : la cascade est ce triangle, lu avec ses tours."),
  un=("1 ⊕ 1 = 3","Une femme, un homme, un enfant. Un émetteur, un récepteur, un message. La relation est comptée."),
  n35=("35, le croisement premier","5 × 7 = 35 : la première fois que deux chemins distincts se nouent. Et 35 + 1 = 36, le carré du 6 qui les sépare."),
  trait=("Le trait","Deux bouts et ce qui les relie : le moindre trait est déjà trois."),
  figure=("La figure","Les deux cercles ne se touchent jamais. Ils se touchent par le carré."),
  paires=("Les paires et le centre vide","1 et 8, 2 et 7, 3 et 6, 4 et 5 : chaque paire fait 9, et leur centre, 4,5, n'est occupé par personne."),
  hip=("La diagonale de Hippase","Exacte comme relation : son carré vaut 2. Sans fin seulement comme quantité."),
  tsi=("La borne de Tsirelson","2√2 = 4 × ½ × √2 : sommets, pli, diagonale. La borne quantique mesure la diagonale du carré."),
  intr=("L'intrication","Une relation, pas un signal."),
  matrio=("La matriochka","Chaque couche porte le code complet du tout. Entre deux poupées, il y a toujours une forme entière."),
  ponts=("Les ponts qu'il a fallu inventer","Quand on coupe le lien, il faut fabriquer un tiers pour le remplacer."),
  sept=("Le 7","Le seul chiffre dont l'écho parcourt les deux rails sans jamais toucher l'axe : 1/7 = 0,142857… Il n'a pas de lieu parce qu'il est le chemin."),
  pi=("22/7 et π","22/7 est le cercle sans liaison, π le cercle lié. L'écart entre les deux se calcule exactement."),
  khe=("La pyramide de Khéops","Une pente de 14/11, et le tour de la base vaut 44/7 de la hauteur : deux fois 22/7."),
  formes=("Les formes entre deux cercles","Du triangle à l'octogone. L'heptagone est la seule qui ne se trace pas."),
  prem=("Les nombres premiers","Au-delà de 3, tous sont sur les rails, jamais sur l'axe : là où le nouveau entre."),
  pourquoi=("Le pourquoi et le comment","Le comment se lit ; le pourquoi premier ne se décide pas. La question reste ouverte, et c'est ce qui fait marcher."),
  hasard=("Le hasard","Toujours local. C'est lui qui crée la nouveauté.")),
 note="<b>Statut de cette page.</b> La carte est une Lecture : elle range, elle ne démontre pas. Chaque case renvoie à un chapitre où les énoncés portent leur propre statut, Fait, Théorème, Lecture ou Prédiction, et où les calculs se refont. Ce qui la ferait tomber : un résultat du corpus qui ne se range sous aucun des trois gestes.",
 home=("La carte du corpus","Trois gestes, lus cent fois : ce que l'outil jette, le tiers, la forme ouverte."))
L['en']=dict(url='/en/map/',title='The map of the corpus: three gestures, read a hundred times',nav='The map',eyebrow='The map of the corpus',h1='Three gestures, read a hundred times',fr=' <i>(chapter in French)</i>',
 desc="The map of the ARC corpus: three gestures, found again in arithmetic, physics, history and living things. What the tool throws away, the third, the open form, and where each one reappears.",
 chapo="The ARC corpus has twelve volumes. They are not hundreds of ideas. They are three gestures, found again in arithmetic, physics, history and living things. This page says which ones, and where each reappears.",
 alt="Two concentric circles and a square between them",
 fig=[("The two circles","What closes: the full turn, and the count of turns that must not be thrown away."),("The square","The third: what holds the two circles together without their touching."),("The empty centre","What stays open: 4.5, the place nobody occupies and through which everything passes.")],
 tr=[("What the tool throws away","We keep the position and throw away the count. Or we cut the tail of the number. Either way, what is missing is written nowhere."),("The third","What lies between two things counts as one. Two terms that meet always make three."),("The open form","What does not close is what lets things through: the path, time, the new.")],
 c=dict(modulo=("Modulo","Every number is turns of 9, plus a position. Modulo keeps the position and throws away the turns."),
  boeing=("Counters that return to zero","Therac-25, Boeing 787, GPS, 2038: the remainder taken for the number, wired into the machine."),
  pap=("The butterfly effect","Two runners at the same spot on the track, at 51 and 52 laps. The chaos of the fold is a thrown-away count of turns."),
  chaos=("The cut decimal","One third written 0.333, multiplied twice: 444 is missing. This is the neighbouring gesture, Stevin's."),
  pnp=("P versus NP","The bits called “random” are exactly the written count of the turns that the fold threw away."),
  cloche=("The bell curve","The bell curve is first a count of paths, row 8 of Pascal's triangle. The cascade keeps the rank that the sum throws away."),
  pascal=("Pascal's triangle","Each cell remembers its two parents: the cascade is this triangle, read with its turns."),
  un=("1 ⊕ 1 = 3","A woman, a man, a child. A sender, a receiver, a message. The relation is counted."),
  n35=("35, the first crossing","5 × 7 = 35: the first time two distinct paths tie a knot. And 35 + 1 = 36, the square of the 6 that stands between them."),
  trait=("The stroke","Two ends and what links them: the smallest stroke is already three."),
  figure=("The figure","The two circles never touch. They touch through the square."),
  paires=("The pairs and the empty centre","1 and 8, 2 and 7, 3 and 6, 4 and 5: each pair makes 9, and their centre, 4.5, is occupied by no one."),
  hip=("Hippasus's diagonal","Exact as a relation: its square is 2. Endless only as a quantity."),
  tsi=("The Tsirelson bound","2√2 = 4 × ½ × √2: vertices, fold, diagonal. The quantum bound measures the diagonal of the square."),
  intr=("Entanglement","A relation, not a signal."),
  matrio=("The matryoshka","Each layer carries the complete code of the whole. Between two dolls there is always an entire form."),
  ponts=("The bridges that had to be invented","When the link is cut, a third has to be manufactured to replace it."),
  sept=("The 7","The only digit whose echo runs along both rails without ever touching the axis: 1/7 = 0.142857… It has no place because it is the path."),
  pi=("22/7 and π","22/7 is the circle without the link, π the linked circle. The gap between the two is computed exactly."),
  khe=("The pyramid of Khufu","A slope of 14/11, and the perimeter of the base is 44/7 of the height: twice 22/7."),
  formes=("The forms between two circles","From the triangle to the octagon. The heptagon is the only one that cannot be drawn."),
  prem=("Prime numbers","Beyond 3, all are on the rails, never on the axis: where the new comes in."),
  pourquoi=("The why and the how","The how can be read; the first why cannot be decided. The question stays open, and that is what keeps us walking."),
  hasard=("Chance","Always local. It is what creates novelty.")),
 note="<b>Status of this page.</b> The map is a Reading: it sorts, it does not prove. Each card points to a chapter where the statements carry their own status, Fact, Theorem, Reading or Prediction, and where the calculations can be redone. What would bring it down: a result of the corpus that fits under none of the three gestures.",
 home=("The map of the corpus","Three gestures, read a hundred times: what the tool throws away, the third, the open form."))
L['pt']=dict(url='/pt/mapa/',title='O mapa do corpus: três gestos, lidos cem vezes',nav='O mapa',eyebrow='O mapa do corpus',h1='Três gestos, lidos cem vezes',fr=' <i>(capítulo em francês)</i>',
 desc="O mapa do corpus ARC: três gestos, reencontrados na aritmética, na física, na história e no vivo. O que a ferramenta deita fora, o terceiro, a forma aberta, e onde cada um reaparece.",
 chapo="O corpus ARC tem doze volumes. Não são centenas de ideias. São três gestos, reencontrados na aritmética, na física, na história e no vivo. Esta página diz quais, e onde cada um reaparece.",
 alt="Dois círculos concêntricos e um quadrado entre eles",
 fig=[("Os dois círculos","O que fecha: a volta completa, e a conta das voltas que não se deve deitar fora."),("O quadrado","O terceiro: o que mantém os dois círculos juntos sem que se toquem."),("O centro vazio","O que fica aberto: 4,5, o lugar que ninguém ocupa e por onde tudo passa.")],
 tr=[("O que a ferramenta deita fora","Guarda-se a posição, deita-se fora a conta. Ou então corta-se a cauda do número. Nos dois casos, o que falta não está escrito em lado nenhum."),("O terceiro","O que está entre duas coisas conta como uma. Dois termos que se encontram fazem sempre três."),("A forma aberta","O que não fecha é o que deixa passar: o caminho, o tempo, o novo.")],
 c=dict(modulo=("O módulo","Todo o número é voltas de 9, mais uma posição. O módulo guarda a posição e deita fora as voltas."),
  boeing=("Os contadores que voltam a zero","Therac-25, Boeing 787, GPS, 2038: o resto tomado pelo número, ligado dentro da máquina."),
  pap=("O efeito borboleta","Dois corredores no mesmo ponto da pista, com 51 e 52 voltas. O caos da dobra é uma conta de voltas deitada fora."),
  chaos=("A decimal cortada","Um terço escrito 0,333, multiplicado duas vezes: faltam 444. É o gesto vizinho, o de Stevin."),
  pnp=("P contra NP","Os bits a que se chama «aleatórios» são exatamente a escrita da conta das voltas que a dobra deitou fora."),
  cloche=("O sino","A curva em sino é primeiro uma conta de caminhos, a linha 8 do triângulo de Pascal. A cascata guarda a ordem que a soma deita fora."),
  pascal=("O triângulo de Pascal","Cada casa lembra-se dos seus dois pais: a cascata é este triângulo, lido com as suas voltas."),
  un=("1 ⊕ 1 = 3","Uma mulher, um homem, um filho. Um emissor, um recetor, uma mensagem. A relação é contada."),
  n35=("35, o primeiro cruzamento","5 × 7 = 35: a primeira vez que dois caminhos distintos se atam. E 35 + 1 = 36, o quadrado do 6 que os separa."),
  trait=("O traço","Duas pontas e o que as liga: o menor traço já é três."),
  figure=("A figura","Os dois círculos nunca se tocam. Tocam-se pelo quadrado."),
  paires=("Os pares e o centro vazio","1 e 8, 2 e 7, 3 e 6, 4 e 5: cada par faz 9, e o seu centro, 4,5, não é ocupado por ninguém."),
  hip=("A diagonal de Hipaso","Exata como relação: o seu quadrado vale 2. Sem fim apenas como quantidade."),
  tsi=("O limite de Tsirelson","2√2 = 4 × ½ × √2: vértices, dobra, diagonal. O limite quântico mede a diagonal do quadrado."),
  intr=("O entrelaçamento","Uma relação, não um sinal."),
  matrio=("A matriosca","Cada camada traz o código completo do todo. Entre duas bonecas há sempre uma forma inteira."),
  ponts=("As pontes que foi preciso inventar","Quando se corta a ligação, é preciso fabricar um terceiro para a substituir."),
  sept=("O 7","O único algarismo cujo eco percorre os dois carris sem nunca tocar o eixo: 1/7 = 0,142857… Não tem lugar porque é o caminho."),
  pi=("22/7 e π","22/7 é o círculo sem ligação, π o círculo ligado. A diferença entre os dois calcula-se exatamente."),
  khe=("A pirâmide de Quéops","Uma inclinação de 14/11, e o perímetro da base vale 44/7 da altura: duas vezes 22/7."),
  formes=("As formas entre dois círculos","Do triângulo ao octógono. O heptágono é a única que não se traça."),
  prem=("Os números primos","Depois do 3, todos estão nos carris, nunca no eixo: é por aí que entra o novo."),
  pourquoi=("O porquê e o como","O como lê-se; o primeiro porquê não se decide. A pergunta fica aberta, e é isso que faz andar."),
  hasard=("O acaso","Sempre local. É ele que cria a novidade.")),
 note="<b>Estatuto desta página.</b> O mapa é uma Leitura: arruma, não demonstra. Cada casa remete para um capítulo onde os enunciados trazem o seu próprio estatuto, Facto, Teorema, Leitura ou Predição, e onde os cálculos se refazem. O que o faria cair: um resultado do corpus que não cabe em nenhum dos três gestos.",
 home=("O mapa do corpus","Três gestos, lidos cem vezes: o que a ferramenta deita fora, o terceiro, a forma aberta."))
CSS='''<style>.carte{max-width:1080px}.carte h1{font-size:clamp(2rem,5vw,3rem);line-height:1.12;margin:10px 0 16px}.carte .chapo{font-size:1.12rem;line-height:1.6;max-width:62ch;color:rgb(58,65,75)}.fig-c{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:30px;align-items:center;margin:26px 0 10px}.fig-c img{max-width:300px;width:100%;height:auto;margin:auto;display:block}.fig-c ul{list-style:none;padding:0;margin:0}.fig-c li{padding:10px 0;border-bottom:1px solid var(--rule);font-size:1rem;line-height:1.5}.fig-c li b{font-family:"IBM Plex Mono",monospace;font-size:.72rem;letter-spacing:.14em;color:var(--or);text-transform:uppercase;display:block;font-weight:400}.tronc{margin:46px 0 0;border-top:3px solid var(--bleu);padding-top:18px}.tr-head{display:grid;grid-template-columns:auto 1fr;column-gap:16px;align-items:baseline}.tr-num{font-family:"Libre Caslon Display",serif;font-size:2.6rem;color:var(--or);line-height:1;grid-row:span 2}.tr-head h2{font-family:"Libre Caslon Display",serif;font-weight:400;font-size:1.9rem;margin:0}.tr-dev{font-style:italic;font-size:1.05rem;line-height:1.5;color:rgb(58,65,75);margin:6px 0 0;max-width:58ch}.tr-items{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-top:20px}.tr-items a{display:block;background:#fff;border:1px solid var(--rule);border-radius:3px;padding:14px 16px;text-decoration:none;color:var(--ink)}.tr-items a b{font-family:"Libre Caslon Display",serif;font-weight:400;font-size:1.14rem;display:block;margin-bottom:4px;color:var(--bleu)}.tr-items a span{font-size:.92rem;line-height:1.5;color:rgb(58,65,75)}.tr-items a i{font-size:.8rem;color:rgb(110,116,124)}.carte .note{font-size:.92rem;border:1px dashed var(--rule);background:#fff;padding:12px 16px;margin:44px 0 0;line-height:1.55;color:rgb(58,65,75)}</style>'''
def split(path):
    t=open(R+path,encoding='utf-8').read(); a=t.index('<body'); b=t.index('<main'); c=t.index('</main>')+7
    return t[:a],t[a:b],t[c:]
H_FR,N_FR,F_FR=split('sujets/borne-de-tsirelson/index.html')
H_EN,N_EN,F_EN=split('en/topics/tsirelson-bound/index.html')
_,N_PT,F_PT=split('pt/temas/modulo/index.html')
H_PT=H_FR.replace('<html lang="fr">','<html lang="pt">').replace('content="fr_CA"','content="pt_PT"')
T={'fr':(H_FR,N_FR,F_FR,'https://bastosfilipe.com/sujets/borne-de-tsirelson/'),'en':(H_EN,N_EN,F_EN,'https://bastosfilipe.com/en/topics/tsirelson-bound/'),'pt':(H_PT,N_PT,F_PT,'https://bastosfilipe.com/sujets/borne-de-tsirelson/')}
def ex(u):
    p=R+u.strip('/'); return any(os.path.exists(x) for x in (p+'.html',os.path.join(p,'index.html'),p))
e=lambda s:html.escape(s,quote=True)
alt=''.join(f'<link rel="alternate" hreflang="{x}" href="{D+L[x]["url"]}">' for x in L)+f'<link rel="alternate" hreflang="x-default" href="{D}/carte/">'
for l,c in L.items():
    h,n,f,tpl=T[l]; url=D+c['url']
    od=re.search(r'<meta name="description" content="([^"]*)"',h).group(1); h=h.replace(od,e(c['desc']))
    ot=re.search(r'<title>(.*?) · Filipe Bastos</title>',h).group(1)
    h=h.replace(f'<title>{ot} · Filipe Bastos</title>',f"<title>{e(c['title'])} · Filipe Bastos</title>").replace(f'content="{ot}"',f'content="{e(c["title"])}"')
    h=re.sub(r'(<link rel="alternate" hreflang="[^"]*" href="[^"]*">)+','',h).replace(tpl,url)
    a=h.index('<style>.q-page'); b=h.index('</style>',a)+8; h=h[:a]+alt+'\n'+CSS+h[b:]
    ld={"@context":"https://schema.org","@type":"CollectionPage","name":c['title'],"description":c['desc'],"inLanguage":l,"url":url,"author":{"@type":"Person","@id":D+"/#filipe-bastos","name":"Filipe Bastos","url":D+"/bio/"},"isPartOf":{"@id":D+"/#site"}}
    h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>',h,flags=re.S)
    assert 'sirelson' not in h, re.findall(r'.{60}sirelson.{30}',h)[:3]
    # switcher
    n=re.sub(r'data-l="(fr|en|pt)" href="[^"]*"',lambda m:f'data-l="{m.group(1)}" href="{L[m.group(1)]["url"]}"',n); assert n.count('data-l=')==3,n.count('data-l=')
    b=[f'<main id="content" data-pagefind-meta="title:{e(c["title"])}">','<div class="wrap page-shell carte">',f'<span class="sec-eyebrow">{c["eyebrow"]}</span>',f'<h1 class="entry-title">{c["h1"]}</h1>',f'<p class="chapo">{c["chapo"]}</p>',
       f'<div class="fig-c"><img src="/assets/figure_fondamentale.svg" alt="{e(c["alt"])}" width="300" height="300"><ul>'+''.join(f'<li><b>{x}</b>{y}</li>' for x,y in c['fig'])+'</ul></div>']
    for i,(nm,dev) in enumerate(c['tr']):
        its=''
        for k in K[i]:
            u=S[l].get(k) or ch[k]; assert ex(u),u
            tag=c['fr'] if (k in ch) else (' <i>(in English)</i>' if l=='pt' and u.startswith('/en/') else '')
            if l=='pt' and tag==' <i>(in English)</i>': tag=' <i>(em inglês)</i>'
            its+=f'<a href="{u}"><b>{c["c"][k][0]}</b><span>{c["c"][k][1]}</span>{tag}</a>'
        b.append(f'<section class="tronc"><div class="tr-head"><span class="tr-num">{"I"*(i+1)}</span><h2>{nm}</h2><p class="tr-dev">{dev}</p></div><div class="tr-items">{its}</div></section>')
    b+=[f'<p class="note">{c["note"]}</p>','</div>','</main>']
    body='\n'.join(b); assert '—' not in body and '–' not in body
    d=R+c['url'].strip('/'); os.makedirs(d,exist_ok=True); open(d+'/index.html','w',encoding='utf-8').write(h+n+body+f); print(l,c['url'])
    # accueil : quatrième porte
    hp=R+{'fr':'index.html','en':'en/index.html','pt':'pt/index.html'}[l]; t=open(hp,encoding='utf-8').read()
    if c['url'] not in t:
        i=t.index('<div class="portes">'); j=t.index('</div>',i)
        t=t[:j]+f'<a href="{c["url"]}"><b>{c["home"][0]}</b><span>{c["home"][1]}</span></a>\n'+t[j:]; open(hp,'w',encoding='utf-8').write(t)
# sitemap
sm=open(R+'sitemap.xml',encoding='utf-8').read()
if '/carte/' not in sm:
    add=''.join(f'  <url><loc>{D+L[x]["url"]}</loc><lastmod>2026-11-10</lastmod><priority>0.9</priority></url>\n' for x in L)
    sm=sm.replace('</urlset>',add+'</urlset>'); open(R+'sitemap.xml','w',encoding='utf-8').write(sm)
