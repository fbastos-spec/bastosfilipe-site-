import re, json, html, os
R='/home/claude/bastosfilipe-site-/'
ALL=json.load(open('/home/claude/pages/all.json',encoding='utf-8'))
U={l:{p['key']:p['url'] for p in ALL[l]} for l in ALL}
fr=open(R+'index.html',encoding='utf-8').read()
CSS=re.search(r'<style id="accueil-2026-11">.*?</style>',fr,flags=re.S).group(0)
mots=re.findall(r'<p class="mots">(.*?)</p>',fr,flags=re.S); assert len(mots)==2
A_FR=re.findall(r'<a href="([^"]*)">([^<]*)</a>',mots[0]); N_FR=re.findall(r'<a href="([^"]*)">([^<]*)</a>',mots[1])
V='/arc/volumes/'
S={
'en':dict(root='/en/',eyebrow='ARC Corpus · Architecture of Relational Coherence · Québec, Canada',h1='The remainder taken for <em>the number</em>',
 sub="A counter that rolls back to zero keeps the position and throws away the turns. An airliner, satellites and a radiotherapy machine have taken that remainder for the number. The ARC corpus starts from there: it names the gesture, gives the formulas for what it costs, and shows the writing that throws nothing away.",
 stat=['Fact','Theorem','Reading','Prediction'],statlab="The corpus's statuses",
 f_eye='The facts, dated and sourced',f_h='What the tool threw away',f_intro='Every calculation can be redone by hand. Every source is public.',
 faits=[('1987 · Yakima','The one-byte counter',"In the Therac-25 radiotherapy machine, a one-byte variable rolls back to zero on its 256th pass. At zero, a check is skipped. A patient receives an overdose and dies of it.",'255 + 1 → 0: the turn is thrown away','Leveson and Turner, Computer, 1993.',None),
  ('2015 · Boeing 787','The airliner that shuts down after 248 days',"An internal counter overflows after 248 days under power, and the aircraft can lose all its electrical power, whatever the phase of flight.",'2³¹ hundredths of a second = 248.55 days','FAA, directive AD 2015-09-07.','boeing'),
  ('1999 and 2019 · GPS','Twenty years back',"The week number is held on ten binary digits and rolls back to zero every 1,024 weeks. A receiver that takes this remainder for the date believes it is 19.6 years earlier.",'1,024 weeks = 19.6 years','GPS interface specification, IS-GPS-200.',None),
  ('1991 · Dhahran','0.34 second',"One tenth of a second, whose binary writing never ends, is cut at 24 digits. After a hundred hours, the Patriot missile's clock has drifted by 0.34 s. The interception misses: 28 dead. This is the other gesture, the truncated decimal.",'0.000000095 × 10 × 3600 × 100 = 0.34 s','GAO, IMTEC-92-26, 1992.',None),
  ('1961 · Lorenz','0.506 for 0.506127',"Lorenz restarts his calculation by retyping three decimals instead of six. The simulated weather diverges. It was made into a property of nature; it was a truncated seed.",'starting gap: 0.000127','Lorenz, The Essence of Chaos, 1993.',None),
  ('2038 · Dated prediction','19 January, 03:14:07',"Seconds counted on 32 binary digits reach their limit. Any uncorrected system that rolls back will show 13 December 1901 at that second.",'2³¹ − 1 seconds after 1 January 1970','Fall criterion: a system of this kind that does not jump.',None)],
 c_eye='What it costs',c_h='The three formulas of chaos',
 trois=[('I. The truncated seed',"Stevin, 1585. One third is written 0.3333: 1/30,000 is missing. Multiplied by 3 at each step, with nothing folded, the gap reaches 10⁴³ in a hundred steps."),('II. The fold',"The remainder, Gauss, 1801. The measurement is exact, but at each step the position is kept and the turn thrown away. Two starts, 1/5 and 1/5 + 1/256: at step 8, same position, and turns that differ by one, 51 and 52."),('III. The machine',"It truncates and folds at each step. This is the chaos we measure, and it is the one we manufactured.")],
 conf="Independent confirmation: in exact arithmetic, with no numerical drift at all, the orbit remains chaotic (Saito and Yamaguchi, Chaos, 2018). The chaos of the fold does not come from rounding: it comes from the thrown-away turn.",
 b_mod='Modulo explained simply',b_pap='The butterfly effect',b_dos='The Modulo dossier (in French)',b_for='The formula of chaos (in French)',b_calc='Redo the calculations',
 o_eye='Where this work comes from',quote="“It all started from zero. Zero led me to Gauss, and Gauss to modulo. I had never heard of modulo before February 2025. On first reading, it did not work in my head: total incoherence. It took me two months to prove it.”",
 p_eye='The figure, seen from the front',p_h='The Great Pyramid of Khufu',
 p1="The slope is given by the builders themselves: a seked of 5½ palms for a cubit of 7 palms. The height is therefore 14/11 of the half-base, and the perimeter is 44/7 of the height, exactly.",p2="The figure of the corpus, two circles and a square, folded into a pyramid, gives the same slope to within a few ten-thousandths.",
 pcalc='14/11 = 1.2727 · folded figure: 1.2720 · measured: 146.6 / 115.2 = 1.2726',
 phon="<b>What this does not establish.</b> Petrie's measured dimensions do not decide between 44/7 and 2π: the gap is below his margin of uncertainty. The corpus does not say the Egyptians “knew π”. It says that their slope is a closed ratio, 14/11, and that the figure gives it back.",pbtn='Read: Khufu and π, what the seked says',
 t_eye='The figure, laid flat',t_h='√2 and the Tsirelson bound',figalt='Two concentric circles and a square between them',
 t1="Two circles with the same centre, a square between them. It can be drawn by hand in ten seconds.",t2="The diagonal of the square gives √2. The ratio of the two circles, squared, gives ½. And the bound that quantum mechanics sets on the correlations between two entangled particles can be read on those three strokes:",
 tcalc='2√2 = 4 × ½ × √2 · corners × fold × diagonal',thon="<b>Without Hilbert space. Bell's theorem is not disputed.</b> The classical bound measures the sides of the square; the quantum bound measures its diagonal.",tbtn='Read: Tsirelson without Hilbert',turl='/en/topics/tsirelson-bound/',
 l_eye='Dated gestures, not men judged',l_h='The lineage',l_intro='Each name leads to the chapter of the corpus that reads its gesture: the date, what was thrown away, what replaces it. (Chapters in French.)',
 lig=[('c. −450','Hippasus','The crisis was not in the diagonal','hippase'),('c. −380','Plato','The doubled square of the Meno',V+'v06-l-histoire-de-la-preuve/14-chapitre-11-le-pourquoi-indecidable-anthologie-de'),('c. −350','Aristotle','The question of why',V+'v01-la-fondation/14-chapitre-13-le-comment-lisible-et-le-pourquoi-inde'),('1585','Stevin','The truncated decimal: the seed',V+'v03-le-code-et-le-registre/26-chapitre-22-le-chaos-fabrique-partie-i-la-lignee-des-amputatio'),('1637','Descartes','The separation, and the bridges that had to be invented','/deux-exceptions/'),('1677','Spinoza','Hope and fear, twins',V+'v10-la-conscience-et-la-peine/25-chapitre-21-la-peine-appartient-au-registre-de-la'),('1801','Gauss','9 written as 0: the remainder','modulo'),('1926','Born','The square christened probability',V+'v03-le-code-et-le-registre/12-chapitre-9-le-quantum-la-matiere-et-le-cosmos-fami')],
 d_eye='Choose your level of risk',d_h='Three doors',
 portes=[('/en/arc/volumes/v03-le-code-et-le-registre/','The Register of Errors','The errors found in established science: a gesture, a date, a calculation, and what replaces it.'),('/en/contradictions/','Contradictions','Send an error, an inconsistency, a prediction that falls. Everything is published with its answer; nothing is erased.'),('/arc/dossiers/Faire_tomber_ARC.pdf','The predictions','179 dated statements, each with what would bring it down. (In French.)')],
 b_vol='The twelve volumes',b_meth='The reading method',b_ia='Check with an AI',arc='/en/arc/',contra='/en/contradictions/#ia',
 m_eye='Enter by a word',m_h='Names and notions',m_intro='Each word leads to the chapter of the corpus that deals with it most directly. (Chapters in French.)',m_a='The authors reread',m_n='The notions',
 desc="Filipe Bastos's ARC corpus: the remainder taken for the number. Modulo and the three formulas of chaos, with their dated accidents (Therac-25, Boeing 787, GPS, Patriot); the Great Pyramid of Khufu; √2 and the Tsirelson bound without Hilbert space; Hippasus, Plato, Aristotle, Descartes, Spinoza, Stevin, Gauss, Born reread. Twelve volumes, every statement with its status.",
 names={'Hippase':'Hippasus','Pythagore':'Pythagoras','Platon':'Plato','Aristote':'Aristotle','Euclide':'Euclid','Archimède':'Archimedes','Galilée':'Galileo'},
 notions={'modulo':'modulo','théorie du chaos':'chaos theory','effet papillon':'butterfly effect','trois corps':'three-body problem','zéro':'zero','infini':'infinity','décimales':'decimals','racine de 2':'square root of 2','nombre π':'the number π','nombre d\'or':'golden ratio','pyramide de Khéops':'Great Pyramid of Khufu','racine digitale':'digital root','nombres premiers':'prime numbers','hypothèse de Riemann':'Riemann hypothesis','conjecture de Collatz':'Collatz conjecture','conjecture de Goldbach':'Goldbach conjecture','P contre NP':'P versus NP','Navier-Stokes':'Navier-Stokes','Yang-Mills':'Yang-Mills','triangle de Pascal':"Pascal's triangle",'suite de Fibonacci':'Fibonacci sequence','nombres parfaits':'perfect numbers','1729':'1729','constante de Kaprekar':"Kaprekar's constant",'loi de Benford':"Benford's law",'loi des grands nombres':'law of large numbers','probabilité':'probability','courbe en cloche':'bell curve','calcul intégral':'integral calculus','physique quantique':'quantum physics','borne de Tsirelson':'Tsirelson bound','intrication quantique':'quantum entanglement','théorème de Bell':"Bell's theorem",'principe d\'incertitude':'uncertainty principle','chat de Schrödinger':"Schrödinger's cat",'effet tunnel':'quantum tunnelling','théorie des cordes':'string theory','boson de Higgs':'Higgs boson','entropie':'entropy','matière noire':'dark matter','tableau périodique':'periodic table','code génétique':'genetic code','évolution':'evolution','conscience':'consciousness','crise de panique':'panic attack','honte':'shame','deuil':'grief','gauche et droite':'left and right','démocratie':'democracy'},
 topics={'/sujets/hypothese-de-riemann/':'/en/topics/riemann-hypothesis/','/sujets/nombres-premiers/':'/en/topics/prime-numbers/','/sujets/intrication-quantique/':'/en/topics/quantum-entanglement/','/sujets/probleme-difficile-de-la-conscience/':'/en/topics/hard-problem-of-consciousness/','/sujets/borne-de-tsirelson/':'/en/topics/tsirelson-bound/','/sujets/crise-de-panique/':'/en/topics/panic-attack/','/sujets/gauche-droite/':'/en/topics/left-right-politics/','/sujets/physique-quantique/':'/en/topics/quantum-physics/'}),
'pt':dict(root='/pt/',eyebrow='Corpus ARC · Arquitetura da Coerência Relacional · Quebeque, Canadá',h1='O resto tomado pelo <em>número</em>',
 sub="Um contador que volta a zero guarda a posição e deita fora as voltas. Um avião, satélites e uma máquina de radioterapia tomaram esse resto pelo número. O corpus ARC parte daí: dá nome ao gesto, dá as fórmulas do que ele custa, e mostra a escrita que não deita nada fora.",
 stat=['Facto','Teorema','Leitura','Predição'],statlab='Estatutos do corpus',
 f_eye='Os factos, datados e com fonte',f_h='O que a ferramenta deitou fora',f_intro='Cada cálculo refaz-se à mão. Cada fonte é pública.',
 faits=[('1987 · Yakima','O contador de um octeto',"Na máquina de radioterapia Therac-25, uma variável de um octeto volta a zero à 256.ª passagem. A zero, uma verificação é saltada. Um doente recebe uma sobredosagem e morre.",'255 + 1 → 0: a volta é deitada fora','Leveson e Turner, Computer, 1993.',None),
  ('2015 · Boeing 787','O avião que se apaga ao fim de 248 dias',"Um contador interno transborda ao fim de 248 dias sob tensão, e o avião pode perder toda a alimentação elétrica, seja qual for a fase do voo.",'2³¹ centésimos de segundo = 248,55 dias','FAA, diretiva AD 2015-09-07.','boeing'),
  ('1999 e 2019 · GPS','Vinte anos para trás',"O número da semana cabe em dez algarismos binários e volta a zero de 1024 em 1024 semanas. Um recetor que tome esse resto pela data julga estar 19,6 anos antes.",'1024 semanas = 19,6 anos','Especificação de interface GPS, IS-GPS-200.',None),
  ('1991 · Dhahran','0,34 segundo',"O décimo de segundo, cuja escrita binária não acaba, é cortado em 24 algarismos. Ao fim de cem horas, o relógio do míssil Patriot derivou 0,34 s. A interceção falha: 28 mortos. É o outro gesto, a decimal cortada.",'0,000000095 × 10 × 3600 × 100 = 0,34 s','GAO, IMTEC-92-26, 1992.',None),
  ('1961 · Lorenz','0,506 por 0,506127',"Lorenz relança o seu cálculo redigitando três decimais em vez de seis. O tempo simulado diverge. Fez-se disso uma propriedade da natureza; era uma semente cortada.",'diferença de partida: 0,000127','Lorenz, The Essence of Chaos, 1993.',None),
  ('2038 · Predição datada','19 de janeiro, 03 h 14 min 07 s',"Os segundos contados em 32 algarismos binários atingem o seu limite. Qualquer sistema não corrigido que volte ao início mostrará 13 de dezembro de 1901 nesse segundo.",'2³¹ − 1 segundos depois de 1 de janeiro de 1970','Critério de queda: um sistema deste tipo que não salte.',None)],
 c_eye='O que isso custa',c_h='As três fórmulas do caos',
 trois=[('I. A semente cortada',"Stevin, 1585. Escreve-se 1/3 como 0,3333: falta 1/30 000. Multiplicada por 3 a cada passo, sem dobrar nada, a diferença atinge 10⁴³ em cem passos."),('II. A dobra',"O resto, Gauss, 1801. A medida é exata, mas a cada passo guarda-se a posição e deita-se fora a volta. Duas partidas, 1/5 e 1/5 + 1/256: ao passo 8, a mesma posição, e voltas que diferem de uma, 51 e 52."),('III. A máquina',"Corta e dobra a cada passo. É o caos que se mede, e é o que fabricámos.")],
 conf="Confirmação independente: em cálculo exato, sem nenhuma deriva numérica, a órbita continua caótica (Saito e Yamaguchi, Chaos, 2018). O caos da dobra não vem do arredondamento: vem da volta deitada fora.",
 b_mod='O módulo explicado de forma simples',b_pap='O efeito borboleta',b_dos='O dossiê Modulo (em francês)',b_for='A fórmula do caos (em francês)',b_calc='Refazer os cálculos',
 o_eye='De onde vem este trabalho',quote="«Tudo partiu do zero. O zero levou-me a Gauss, e Gauss ao módulo. Nunca tinha ouvido falar do módulo antes de fevereiro de 2025. À primeira leitura, aquilo não funcionava na minha cabeça: incoerência total. Precisei de dois meses para o provar.»",
 p_eye='A figura, vista de frente',p_h='A pirâmide de Quéops',
 p1="A inclinação é dada pelos próprios construtores: um seked de 5 palmos e meio para um côvado de 7 palmos. A altura vale, pois, 14/11 da meia-base, e o contorno vale 44/7 da altura, exatamente.",p2="A figura do corpus, dois círculos e um quadrado, dobrada em pirâmide, dá a mesma inclinação com um erro de alguns décimos-milésimos.",
 pcalc='14/11 = 1,2727 · figura dobrada: 1,2720 · medido: 146,6 / 115,2 = 1,2726',
 phon="<b>O que isto não estabelece.</b> As cotas medidas por Petrie não decidem entre 44/7 e 2π: o desvio está abaixo da sua margem de incerteza. O corpus não diz que os egípcios «conheciam π». Diz que a sua inclinação é uma razão fechada, 14/11, e que a figura a devolve.",pbtn='Ler: Quéops e π, o que diz o seked',
 t_eye='A figura, no plano',t_h='√2 e o limite de Tsirelson',figalt='Dois círculos concêntricos e um quadrado entre eles',
 t1="Dois círculos com o mesmo centro, um quadrado entre eles. Traça-se à mão em dez segundos.",t2="A diagonal do quadrado dá √2. A razão dos dois círculos, ao quadrado, dá ½. E o limite que a mecânica quântica fixa às correlações entre duas partículas entrelaçadas lê-se nestes três traços:",
 tcalc='2√2 = 4 × ½ × √2 · vértices × dobra × diagonal',thon="<b>Sem espaço de Hilbert. O teorema de Bell não é contestado.</b> O limite clássico mede os lados do quadrado; o limite quântico mede a sua diagonal.",tbtn='Ler: Tsirelson sem Hilbert (em inglês)',turl='/en/topics/tsirelson-bound/',
 l_eye='Gestos datados, não homens julgados',l_h='A linhagem',l_intro='Cada nome leva ao capítulo do corpus que lê o seu gesto: a data, o que foi deitado fora, o que o substitui. (Capítulos em francês.)',
 lig=[('c. −450','Hipaso','A crise não estava na diagonal','hippase'),('c. −380','Platão','O quadrado duplicado do Ménon',V+'v06-l-histoire-de-la-preuve/14-chapitre-11-le-pourquoi-indecidable-anthologie-de'),('c. −350','Aristóteles','A questão do porquê',V+'v01-la-fondation/14-chapitre-13-le-comment-lisible-et-le-pourquoi-inde'),('1585','Stevin','A decimal cortada: a semente',V+'v03-le-code-et-le-registre/26-chapitre-22-le-chaos-fabrique-partie-i-la-lignee-des-amputatio'),('1637','Descartes','A separação, e as pontes que foi preciso inventar','/deux-exceptions/'),('1677','Espinosa','A esperança e o medo, gémeos',V+'v10-la-conscience-et-la-peine/25-chapitre-21-la-peine-appartient-au-registre-de-la'),('1801','Gauss','O 9 escrito 0: o resto','modulo'),('1926','Born','O quadrado batizado de probabilidade',V+'v03-le-code-et-le-registre/12-chapitre-9-le-quantum-la-matiere-et-le-cosmos-fami')],
 d_eye='Escolher o seu nível de risco',d_h='Três portas',
 portes=[('/pt/arc/volumes/v03-le-code-et-le-registre/','O Registo dos Erros','Os erros apontados na ciência estabelecida: um gesto, uma data, um cálculo, e o que o substitui.'),('/pt/contradicoes/','Contradições','Envie um erro, uma incoerência, uma predição que cai. Tudo é publicado com a sua resposta; nada é apagado.'),('/arc/dossiers/Faire_tomber_ARC.pdf','As predições','179 enunciados datados, cada um com o que o faria cair. (Em francês.)')],
 b_vol='Os doze volumes',b_meth='O método de leitura',b_ia='Verificar com uma IA',arc='/pt/arc/',contra='/pt/contradicoes/#ia',
 m_eye='Entrar por uma palavra',m_h='Nomes e noções',m_intro='Cada palavra leva ao capítulo do corpus que a trata mais diretamente. (Capítulos em francês.)',m_a='Os autores relidos',m_n='As noções',
 desc="Corpus ARC de Filipe Bastos: o resto tomado pelo número. O módulo e as três fórmulas do caos, com os seus acidentes datados (Therac-25, Boeing 787, GPS, Patriot); a pirâmide de Quéops; √2 e o limite de Tsirelson sem espaço de Hilbert; Hipaso, Platão, Aristóteles, Descartes, Espinosa, Stevin, Gauss, Born relidos. Doze volumes, cada enunciado com o seu estatuto.",
 names={'Hippase':'Hipaso','Pythagore':'Pitágoras','Platon':'Platão','Aristote':'Aristóteles','Euclide':'Euclides','Archimède':'Arquimedes','Spinoza':'Espinosa'},
 notions={'modulo':'módulo','théorie du chaos':'teoria do caos','effet papillon':'efeito borboleta','trois corps':'três corpos','zéro':'zero','infini':'infinito','décimales':'decimais','racine de 2':'raiz de 2','nombre π':'número π','nombre d\'or':'número de ouro','pyramide de Khéops':'pirâmide de Quéops','racine digitale':'raiz digital','nombres premiers':'números primos','hypothèse de Riemann':'hipótese de Riemann','conjecture de Collatz':'conjetura de Collatz','conjecture de Goldbach':'conjetura de Goldbach','P contre NP':'P versus NP','Navier-Stokes':'Navier-Stokes','Yang-Mills':'Yang-Mills','triangle de Pascal':'triângulo de Pascal','suite de Fibonacci':'sucessão de Fibonacci','nombres parfaits':'números perfeitos','1729':'1729','constante de Kaprekar':'constante de Kaprekar','loi de Benford':'lei de Benford','loi des grands nombres':'lei dos grandes números','probabilité':'probabilidade','courbe en cloche':'curva em sino','calcul intégral':'cálculo integral','physique quantique':'física quântica','borne de Tsirelson':'limite de Tsirelson','intrication quantique':'entrelaçamento quântico','théorème de Bell':'teorema de Bell','principe d\'incertitude':'princípio da incerteza','chat de Schrödinger':'gato de Schrödinger','effet tunnel':'efeito túnel','théorie des cordes':'teoria das cordas','boson de Higgs':'bosão de Higgs','entropie':'entropia','matière noire':'matéria escura','tableau périodique':'tabela periódica','code génétique':'código genético','évolution':'evolução','conscience':'consciência','crise de panique':'ataque de pânico','honte':'vergonha','deuil':'luto','gauche et droite':'esquerda e direita','démocratie':'democracia'},
 topics={'/sujets/hypothese-de-riemann/':'/en/topics/riemann-hypothesis/','/sujets/nombres-premiers/':'/en/topics/prime-numbers/','/sujets/intrication-quantique/':'/en/topics/quantum-entanglement/','/sujets/probleme-difficile-de-la-conscience/':'/en/topics/hard-problem-of-consciousness/','/sujets/borne-de-tsirelson/':'/en/topics/tsirelson-bound/','/sujets/crise-de-panique/':'/en/topics/panic-attack/','/sujets/gauche-droite/':'/en/topics/left-right-politics/','/sujets/physique-quantique/':'/en/topics/quantum-physics/'}),
}
FRNEW={'/sujets/modulo/':'modulo','/sujets/effet-papillon/':'papillon','/sujets/pyramide-de-kheops-pi/':'kheops','/sujets/hippase-racine-de-2/':'hippase','/sujets/boeing-787-248-jours/':'boeing'}
def exists(u):
    p=R+u.split('#')[0].strip('/'); return any(os.path.exists(x) for x in (p+'.html',os.path.join(p,'index.html'),p))
for l,s in S.items():
    f=R+l+'/index.html'; t=open(f,encoding='utf-8').read()
    if 'id="accueil-2026-11"' in t: print(l,'déjà fait'); continue
    i=t.index('<div class="wrap hero">'); j=t.index('<section class="wrap" id="methode"'); old=t[i:j]
    ded=re.search(r'<p class="dedicace".*?</p>',old,flags=re.S).group(0); meth=re.search(r'<p class="methode-sub".*?</p>',old,flags=re.S).group(0)
    u=lambda k:U[l][k]
    def mapurl(x):
        if x in FRNEW: return u(FRNEW[x])
        return s['topics'].get(x,x)
    faits=''.join(f'<div class="fait"><span class="an">{a}</span><h3>'+(f'<a href="{u(k)}" style="color:inherit">{h}</a>' if k else h)+f'</h3><p>{p}</p><span class="calc">{c}</span><p class="src">{src}</p></div>\n' for a,h,p,c,src,k in s['faits'])
    trois=''.join(f'<div><h3>{a}</h3><p>{b}</p></div>\n' for a,b in s['trois'])
    lig=''.join(f'<a href="{u(x) if x in U[l] else x}"><span>{d}</span><b>{n}</b><em>{sub}</em></a>\n' for d,n,sub,x in s['lig'])
    portes=''.join(f'<a href="{a}"><b>{b}</b><span>{c}</span></a>\n' for a,b,c in s['portes'])
    au=' '.join(f'<a href="{mapurl(a)}">{s["names"].get(n,n)}</a>' for a,n in A_FR)
    no=' '.join(f'<a href="{mapurl(a)}">{s["notions"].get(html.unescape(n),n)}</a>' for a,n in N_FR)
    calc='style="font-family:\'IBM Plex Mono\',monospace;color:var(--bleu);background:var(--wash);padding:8px 10px;display:block;font-size:.9rem;margin:10px 0"'
    new=f'''<div class="wrap hero">
{ded}
<p class="eyebrow">{s['eyebrow']}</p>
<h1>{s['h1']}</h1>
<p class="sub">{s['sub']}</p>
{meth}
<div aria-label="{s['statlab']}" class="trichotomie" role="list">{''.join(f'<span role="listitem">{x}</span>' for x in s['stat'])}</div>
</div>

<section class="wrap sect" style="padding-top:20px;padding-bottom:54px">
<span class="sec-eyebrow">{s['f_eye']}</span>
<h2 class="sec">{s['f_h']}</h2>
<p class="sec-intro">{s['f_intro']}</p>
<div class="faits">
{faits}</div>
</section>

<section class="band"><div class="wrap sect">
<span class="sec-eyebrow">{s['c_eye']}</span>
<h2 class="sec">{s['c_h']}</h2>
<p class="formule">ε(n) = ε₀ · fⁿ</p>
<div class="trois">
{trois}</div>
<p class="txt" style="margin-top:22px">{s['conf']}</p>
<p><a class="btn" href="{u('modulo')}">{s['b_mod']}</a> <a class="btn ghost" href="{u('papillon')}">{s['b_pap']}</a> <a class="btn ghost" href="/arc/dossiers/lire/Modulo_v2_1/">{s['b_dos']}</a> <a class="btn ghost" href="/arc/volumes/v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos">{s['b_for']}</a> <a class="btn ghost" href="/arc/dossiers/modulo_chaos_verif.py">{s['b_calc']}</a></p>
</div></section>

<section class="wrap sect">
<span class="sec-eyebrow">{s['o_eye']}</span>
<blockquote class="orig">{s['quote']}<cite>Filipe Bastos</cite></blockquote>
</section>

<section class="band"><div class="wrap sect">
<span class="sec-eyebrow">{s['p_eye']}</span>
<h2 class="sec">{s['p_h']}</h2>
<div class="deux">
<div>
<p class="txt">{s['p1']}</p>
<p class="txt">{s['p2']}</p>
<span class="calc" {calc}>{s['pcalc']}</span>
</div>
<div>
<p class="honn">{s['phon']}</p>
<p><a class="btn ghost" href="{u('kheops')}">{s['pbtn']}</a></p>
</div>
</div>
</div></section>

<section class="wrap sect">
<span class="sec-eyebrow">{s['t_eye']}</span>
<h2 class="sec">{s['t_h']}</h2>
<div class="deux">
<div><img src="/assets/figure_fondamentale.svg" alt="{s['figalt']}"></div>
<div>
<p class="txt">{s['t1']}</p>
<p class="txt">{s['t2']}</p>
<span class="calc" {calc}>{s['tcalc']}</span>
<p class="honn">{s['thon']}</p>
<p><a class="btn ghost" href="{s['turl']}">{s['tbtn']}</a></p>
</div>
</div>
</section>

<section class="band"><div class="wrap sect">
<span class="sec-eyebrow">{s['l_eye']}</span>
<h2 class="sec">{s['l_h']}</h2>
<p class="sec-intro">{s['l_intro']}</p>
<div class="lignee">
{lig}</div>
</div></section>

<section class="wrap sect">
<span class="sec-eyebrow">{s['d_eye']}</span>
<h2 class="sec">{s['d_h']}</h2>
<div class="portes">
{portes}</div>
<p style="margin-top:26px"><a class="btn" href="{s['arc']}">{s['b_vol']}</a> <a class="btn ghost" href="#methode">{s['b_meth']}</a> <a class="btn ghost" href="{s['contra']}">{s['b_ia']}</a></p>
</section>
<section class="wrap sect" id="mots" aria-label="{s['m_h']}">
<span class="sec-eyebrow">{s['m_eye']}</span>
<h2 class="sec">{s['m_h']}</h2>
<p class="sec-intro">{s['m_intro']}</p>
<h3 class="mots-t">{s['m_a']}</h3>
<p class="mots">{au}</p>
<h3 class="mots-t">{s['m_n']}</h3>
<p class="mots">{no}</p>
</section>
'''
    assert '—' not in new and '–' not in new
    bad=[m for m in re.findall(r'href="(/[^"]*)"',new) if not exists(m)]; assert not bad,bad
    os.makedirs(R+'_travail',exist_ok=True); open(R+f'_travail/accueil_ancien_{l}_2026-11-10.html','w',encoding='utf-8').write(old)
    t=t[:i]+new+t[j:]
    assert t.count('</head>')==1; t=t.replace('</head>',CSS+'\n</head>')
    d=re.search(r'<meta name="description" content="([^"]*)"',t).group(1); t=t.replace('<meta name="description" content="'+d+'"','<meta name="description" content="'+html.escape(s['desc'],quote=True)+'"')
    a='<ul style="columns:2 320px;column-gap:40px;padding-left:1.2em;max-width:980px">'; assert t.count(a)==1
    t=t.replace(a,a+''.join(f'<li style="margin:6px 0"><a href="{p["url"]}">{p["title"]}</a></li>' for p in ALL[l]))
    if l=='pt': t=t.replace(' (Em francês e em inglês.)',' (As outras em francês e em inglês.)')
    open(f,'w',encoding='utf-8').write(t); print(l,'accueil ok',len(new))
# hub en
h=open(R+'en/topics/index.html',encoding='utf-8').read(); a='<ul class="q-hub" style="list-style:none;padding:0">'
if ALL['en'][0]['url'] not in h:
    h=h.replace(a,a+''.join(f'<li><a href="{p["url"]}"><strong>{html.escape(p["title"])}</strong></a><br><span>{html.escape(p["desc"])}</span></li>\n' for p in ALL['en'])); open(R+'en/topics/index.html','w',encoding='utf-8').write(h)
# sitemap
sm=open(R+'sitemap.xml',encoding='utf-8').read(); a='  <url><loc>https://bastosfilipe.com/sujets/borne-de-tsirelson/</loc>'
add=''.join(f'  <url><loc>https://bastosfilipe.com{p["url"]}</loc><lastmod>2026-11-10</lastmod><priority>0.8</priority></url>\n' for l in ('en','pt') for p in ALL[l] if p['url'] not in sm)
if '/pt/temas/</loc>' not in sm: add+='  <url><loc>https://bastosfilipe.com/pt/temas/</loc><lastmod>2026-11-10</lastmod><priority>0.7</priority></url>\n'
open(R+'sitemap.xml','w',encoding='utf-8').write(sm.replace(a,add+a)); print('plan ok')
