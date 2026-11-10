# Versões portuguesas das cinco páginas em linguagem simples
V = '/arc/volumes/'
def pages_pt(F, T, L, P):
    return [
dict(slug='modulo', key='modulo', eyebrow='Módulo', title="O módulo explicado de forma simples: o que guarda, o que deita fora",
 desc="O módulo é o resto de uma divisão: a hora num relógio, o conta-quilómetros de um carro que volta a zero. O que guarda, o que deita fora, e o que acontece quando se toma esse resto pelo número.",
 rep="O módulo guarda o resto de uma divisão e deita fora o número de voltas. Num relógio, as 15 horas e as 3 horas caem no mesmo sítio: o ponteiro diz onde estamos na volta, não quantas voltas já foram dadas. É muito útil, e torna-se perigoso logo que se toma esse resto pelo número inteiro.",
 body=[("O módulo é um relógio", [
  F+"Um relógio conta de 1 a 12 e depois recomeça. Às 15 horas, o ponteiro aponta para o 3. Os matemáticos escrevem: 15 módulo 12 é igual a 3. Tirou-se uma volta de 12 e guardou-se o que sobra.",
  F+"O conta-quilómetros de um carro antigo faz o mesmo. Tem seis algarismos: depois de 999 999 quilómetros, mostra 000 000. O carro não é novo. O contador deu uma volta completa, e essa volta não está escrita em lado nenhum.",
  "O módulo não é, portanto, um erro de cálculo. Responde bem a uma pergunta precisa: <em>onde estamos na volta?</em> Não responde à outra pergunta: <em>quantas voltas demos?</em>"]),
 ("O que guarda, o que deita fora", [
  T+"Todo o número inteiro se escreve de uma única maneira como <em>voltas de 9, mais uma posição</em>. Por exemplo, 19 = 2 voltas de 9, mais 1. E 28 = 3 voltas de 9, mais 1. O corpus ARC conta as posições de 1 a 9: 18 é uma volta, e a posição 9.",
  T+"10, 19, 28 e 1 000 000 têm todos a mesma posição: 1. Se só se guardar a posição, estes quatro números tornam-se o mesmo. E não há caminho de volta: a partir de «posição 1», ninguém consegue dizer de que número se partiu.",
  T+"A perda pode medir-se. Entre o primeiro milhão de números, 111 112 têm a posição 1. Dizer apenas «posição 1» é, pois, deixar 111 112 candidatos. Contando a informação como fazem os engenheiros (em bits), a posição entre nove guarda 3,17 bits em 19,93: 84 % do que o número trazia é deitado fora."]),
 ("Quando a posição chega, e quando não chega", [
  T+"A posição chega para certas perguntas. Um número é divisível por 3 exatamente quando a sua posição é 3, 6 ou 9: as voltas não fazem falta.",
  T+"Não chega para outras. 10 e 19 têm a mesma posição: um é par, o outro é ímpar. 19 e 28 têm a mesma posição: um é primo, o outro não. Sempre que a resposta depende da volta, o módulo não a pode dar."]),
 ("Quando se tomou o resto pelo número", [
  F+"Num computador, um contador tem um número fixo de algarismos. Quando está cheio, volta a zero, como o conta-quilómetros do carro. Se o programa acreditar que esse zero é o número verdadeiro, engana-se.",
  F+"Aconteceu. Em 1987, na máquina de radioterapia Therac-25, um contador que voltava a zero à 256.ª passagem fez saltar uma verificação, e um doente morreu de sobredosagem. Em 2015, as autoridades obrigaram a reiniciar os Boeing 787 antes de um contador chegar ao fim, aos 248 dias. Em 1999 e em 2019, recetores GPS julgaram estar vinte anos antes. <a href=\"/pt/temas/boeing-787-248-dias/\">O caso do Boeing, com o seu cálculo.</a>"]),
 ("A leitura do corpus ARC", [
  L+"O corpus não censura o módulo por calcular mal. Censura o que se fez com ele: tomar a posição pelo número e esquecer que as voltas existiam. Data esse gesto de Gauss, em 1801, quando o 9 foi escrito 0: o fim da volta confundido com o vazio.",
  T+"Guardar as voltas é guardar tudo. Se se anotar a posição, depois a posição do número de voltas, e assim por diante, recupera-se o número inteiro sem perder nada. 2026 escreve-se 2, 6, 9, 1, porque 2 × 729 + 6 × 81 + 9 × 9 + 1 = 2026.",
  L+"«É a ferramenta que é julgada, não quem dela se serviu.»"]),
 ("O que esta página não diz", [
  "Não diz que o módulo está errado, nem que deve ser abandonado. Onde perder é o objetivo, ele está no seu lugar: a cifra que protege uma palavra-passe ou um pagamento assenta precisamente num caminho de volta que se deitou fora.",
  "Não lhe atribui tudo. O míssil Patriot de 1991 derivou por causa de uma decimal cortada, não de um resto: é outro gesto, e o corpus separa-os."])],
 links=[("/arc/dossiers/lire/Modulo_v2_1/", "Modulo: o dossiê completo, com os seus teoremas e fontes (em francês)"), ("/arc/dossiers/Modulo_v2_1.pdf", "Modulo (PDF, em francês)"), (V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos", "Volume 3, capítulo 14: a fórmula do caos (em francês)"), ("/arc/dossiers/modulo_chaos_verif.py", "O script que refaz os cálculos")],
 vois=["boeing", "papillon"]),

dict(slug='boeing-787-248-dias', key='boeing', eyebrow='Boeing 787', title="Porque é que o Boeing 787 tinha de ser reiniciado antes de 248 dias",
 desc="Em 2015, a autoridade americana da aviação obrigou a desligar e voltar a ligar os Boeing 787: um contador interno transbordava ao fim de 248 dias. O facto, o cálculo, e o gesto que está por trás.",
 rep="Porque um contador interno, deixado sob tensão sem interrupção, chegava ao fim do seu espaço ao cabo de 248 dias e recomeçava do zero. Nesse instante, as unidades que comandam os geradores elétricos passavam a modo de segurança, e o avião podia perder a sua corrente. A autoridade americana obrigou a desligar e voltar a ligar o avião pelo menos de 120 em 120 dias, e depois a corrigir o software.",
 body=[("O que está estabelecido", [
  F+"A diretiva AD 2015-09-07 da administração federal de aviação dos Estados Unidos, em vigor a 1 de maio de 2015, escreve-o: um 787 alimentado sem interrupção durante 248 dias pode perder toda a alimentação elétrica em corrente alternada, por causa de um contador de software interno às unidades de controlo dos geradores, que transborda ao fim de 248 dias de alimentação contínua.",
  F+"Se as quatro unidades principais tiverem sido ligadas ao mesmo tempo, mudam todas juntas, seja qual for a fase do voo. A diretiva refere uma possível perda de controlo do avião. Impõe que se desligue a alimentação pelo menos de 120 em 120 dias.",
  F+"Uma segunda diretiva, AD 2018-20-15, em vigor a 20 de novembro de 2018, exige um novo software nas seis unidades do avião."]),
 ("O cálculo, para refazer", [
  "Um contador de computador é como o conta-quilómetros de um carro: tem um número fixo de algarismos e, quando está cheio, volta a zero.",
  T+"Um contador de 31 algarismos binários pode contar até 2³¹, ou seja, 2 147 483 648. Se contar centésimos de segundo, fica cheio ao fim de 21 474 836 segundos. Um dia dura 86 400 segundos. Logo: 21 474 836 ÷ 86 400 = 248,55 dias.",
  F+"Honestidade sobre este cálculo: nenhuma das duas diretivas publica o tamanho do contador nem a sua unidade. O contador de 31 algarismos binários em centésimos de segundo é uma dedução, feita a partir da concordância com os 248 dias. O que a autoridade escreve, preto no branco, é o gesto: um contador que transborda."]),
 ("O mesmo gesto, noutros lugares", [
  F+"Therac-25, 1987: numa máquina de radioterapia, um contador de um só octeto voltava a zero à 256.ª passagem. A zero, uma verificação era saltada. Um doente morreu por isso.",
  F+"GPS, 1999 e 2019: o número da semana cabe em dez algarismos binários e volta a zero de 1024 em 1024 semanas, ou seja, 19,6 anos. Um recetor que tome esse resto pela data julga estar vinte anos antes.",
  P+"2038: muitos sistemas contam os segundos desde 1 de janeiro de 1970 em 32 algarismos binários. O contador atinge o seu limite a 19 de janeiro de 2038, às 03 h 14 min 07 s. Qualquer sistema não corrigido que volte ao início mostrará então 13 de dezembro de 1901."]),
 ("A leitura do corpus ARC", [
  L+"Os engenheiros têm um nome para o defeito: «transbordo de inteiro». Não têm nome para o gesto que está por baixo. O corpus dá-lhe nome: <em>tomar o resto pelo número</em>. O contador guarda a posição na volta e deita fora a volta. É o <a href=\"/pt/temas/modulo/\">módulo</a>, montado dentro da máquina.",
  L+"«Em cada caso, o remédio foi guardar mais voltas»: contadores mais longos, anos com quatro algarismos, semanas em treze algarismos binários."]),
 ("O que esta página não diz", [
  "Não diz que um 787 caiu por causa deste contador: a diretiva é uma medida de precaução, e o corpus não refere nenhum acidente deste avião ligado a este defeito.",
  "Não atribui tudo ao resto. O míssil Patriot de 1991 derivou 0,34 segundos por causa de uma decimal cortada: é outro gesto, que o corpus trata à parte."])],
 links=[("/arc/dossiers/lire/Modulo_v2_1/", "Modulo, parte 5: as mortes e as avarias, com as fontes (em francês)"), ("/arc/dossiers/Modulo_v2_1.pdf", "Modulo (PDF, em francês)"), ("/arc/dossiers/modulo_chaos_verif.py", "O script que refaz os cálculos")],
 vois=["modulo", "papillon"]),

dict(slug='piramide-de-queops-pi', key='kheops', eyebrow='Pirâmide de Quéops', title="A pirâmide de Quéops e π: o que diz realmente o seked",
 desc="A pirâmide de Quéops esconde o número π? A sua inclinação, o seked de 5 palmos e meio, dá exatamente 44/7: o cálculo, as medidas, e o que elas não permitem decidir.",
 rep="Os construtores de Quéops não precisavam de conhecer π. Escolheram uma inclinação simples, o seked: 5 palmos e meio de recuo para 7 palmos de subida. Com essa inclinação, o contorno da base vale exatamente 44/7 vezes a altura, ou seja, duas vezes 22/7, um número muito próximo de 2π. A semelhança com π vem da inclinação, não de um segredo.",
 body=[("O que está estabelecido", [
  F+"Os egípcios regulavam a inclinação de uma pirâmide pelo <em>seked</em>: quanto se recua na horizontal de cada vez que se sobe um côvado. Um côvado vale 7 palmos. O seked de Quéops é de 5 palmos e meio.",
  F+"Os levantamentos dão uma altura de cerca de 146,6 metros e uma meia-base de 115,2 metros. A altura dividida pela meia-base vale 1,2726."]),
 ("O cálculo, para refazer", [
  T+"Subir 7 recuando 5,5 é uma inclinação de 7 ÷ 5,5 = 14/11 = 1,2727. É o número medido, com um erro de um décimo-milésimo.",
  T+"O contorno da base tem 8 meias-bases. Dividido pela altura, dá 8 × 11/14 = 44/7 = 6,2857. Ora 2π vale 6,2832. É daqui que vem a «pirâmide de π»: de 22/7, a fração simples que a inclinação fabrica sozinha.",
  T+"A figura do corpus ARC, dois círculos e um quadrado, dobrada em pirâmide, dá por seu lado uma inclinação de 1,2720, a raiz do número de ouro. Três números ficam, assim, a um fio uns dos outros: 1,2720 pela figura, 1,2726 pela medida, 1,2727 pelo seked."]),
 ("O que as medidas não decidem", [
  F+"A razão medida está a 0,012 % de 44/7 e a 0,053 % de 2π. Mas os levantamentos de Petrie têm uma margem de erro de 0,03 % a 0,21 %. Os dois desvios são menores do que essa margem: a medida não decide.",
  F+"O corpus tinha começado por escrever «acordo exato» com o número de ouro. Retirou essa fórmula em setembro de 2026, pela mesma razão: o desvio está dentro da margem de erro. A retirada está guardada, datada, no Registo."]),
 ("A leitura do corpus ARC", [
  L+"Quéops não aproxima π: inscreve uma razão fechada, 14/11, que se constrói com uma corda e palmos. A «pirâmide de π» dos livros é uma consequência disso, não uma causa.",
  L+"O que a figura acrescenta é que a mesma inclinação sai de um quadrado preso entre dois círculos, sem medida nenhuma. Se os construtores o sabiam ou não, o corpus não o diz."]),
 ("O que esta página não diz", [
  "Não diz que os egípcios conheciam π ou o número de ouro. Não diz que há uma mensagem escondida na pirâmide. Diz três coisas verificáveis: a inclinação é uma razão simples, essa razão dá 44/7, e as medidas são demasiado largas para escolher entre as explicações."])],
 links=[(V+"v02-la-figure/06-chapitre-5-le-carre-illusion-et-l-origine-geometri", "Volume 2, capítulo 5: o quadrado dobrado e a geometria de Quéops (em francês)"), (V+"v02-la-figure/05-chapitre-4-deux-cercles-et-un-carre-le-double-et-l", "Volume 2, capítulo 4: dois círculos e um quadrado (em francês)"), (V+"v03-le-code-et-le-registre/05-chapitre-3-les-gestes-historiques-et-leurs-resolut", "Volume 3, capítulo 3: «Quéops não decide» (em francês)")],
 vois=["hippase"]),

dict(slug='hipaso-raiz-de-2', key='hippase', eyebrow='Hipaso', title="O que descobriu realmente Hipaso? A diagonal do quadrado e √2",
 desc="Hipaso mostrou que a diagonal de um quadrado não se escreve como fração do seu lado. Crise da matemática, ou pergunta errada? O cálculo do quadrado duplicado, e a leitura do corpus ARC.",
 rep="Hipaso mostrou que a diagonal de um quadrado não se escreve como fração do seu lado. A tradição fez disso uma crise: um número «irracional», sem razão. O corpus ARC lê outra coisa. A diagonal traça-se, mede-se e serve muito bem; o que falhou foi a exigência de a escrever como razão de dois números inteiros.",
 body=[("O que a tradição estabelece", [
  F+"Por volta de 450 antes da nossa era, Hipaso de Metaponto, da escola de Pitágoras, estuda a diagonal de um quadrado de lado 1. Descobre que nenhuma fração, por mais fina que seja, dá exatamente o seu comprimento: a diagonal e o lado não têm medida comum.",
  F+"Hoje escreve-se esse comprimento √2 = 1,41421356…, com decimais que não acabam nem se repetem. Este resultado está demonstrado, e continua verdadeiro."]),
 ("O cálculo, para refazer com um lápis", [
  T+"Traça um quadrado de lado 1 e constrói depois um segundo quadrado sobre a sua diagonal. Esse quadrado grande divide-se em quatro triângulos, cada um com área 1/2. A sua área vale, pois, 2: é exatamente o dobro do primeiro.",
  T+"Por outras palavras: a diagonal, multiplicada por si mesma, dá 2. Não mais ou menos, exatamente. É o problema que Sócrates faz resolver a um jovem escravo no <em>Ménon</em> de Platão: para duplicar um quadrado, constrói-se sobre a sua diagonal.",
  T+"Uma cauda de decimais sem fim nem sempre é sinal de mistério. Um terço escreve-se 0,333… quando se conta de dez em dez, e simplesmente 0,1 quando se conta de três em três. A cauda vem, por vezes, da escrita, não da coisa."]),
 ("A leitura do corpus ARC", [
  L+"A palavra grega <em>alogos</em>, que se traduz por «irracional», dá nome ao fracasso de uma exigência: exprimir a diagonal por uma razão de dois inteiros. Não dá nome a um defeito da diagonal, que é construída, mensurável e funciona.",
  L+"A diagonal é exata como relação: o seu quadrado vale 2. Só não tem fim como quantidade escrita em decimais. A crise não estava na diagonal, mas na pergunta que lhe fizeram.",
  L+"O corpus vê aí um molde que se repete depois, em Stevin, em Gauss, em Riemann: faz-se uma exigência de fundamento a algo que funcionava, obtém-se um objeto impossível, e dá-se-lhe o nome da impossibilidade."]),
 ("O que esta página não diz", [
  "Não contesta a demonstração: √2 não é uma fração em nenhuma maneira de contar, nem de dez em dez, nem de três em três, nem de outra forma. O próprio corpus o diz. O que ele discute é a palavra «irracional» e a crise que dela se tirou, não o teorema."]),
 ("O que faria cair esta leitura", [
  P+"O corpus sustenta que toda a crise dos fundamentos, na história da matemática, vem de uma exigência de justificação feita a um cálculo que funcionava. Uma crise nascida de um cálculo que deixa de funcionar sozinho, sem nenhuma exigência desse género, refutá-la-ia."])],
 links=[(V+"v06-l-histoire-de-la-preuve/15-chapitre-12-le-probleme-qui-a-cree-le-probleme-hip", "Volume 6, capítulo 12: o problema que criou o problema, Hipaso (em francês)"), (V+"v06-l-histoire-de-la-preuve/14-chapitre-11-le-pourquoi-indecidable-anthologie-de", "Volume 6, capítulo 11: o porquê indecidível, com o Ménon (em francês)"), (V+"v02-la-figure/02-chapitre-1-la-figure-fondamentale", "Volume 2, capítulo 1: a figura fundamental e √2 (em francês)")],
 vois=["kheops", "modulo"]),

dict(slug='efeito-borboleta', key='papillon', eyebrow='Efeito borboleta', title="O efeito borboleta está na natureza ou no cálculo?",
 desc="O efeito borboleta e a teoria do caos: de onde vem a divergência nos cálculos? Uma medida cortada, uma contagem de voltas deitada fora, e um teste que se refaz em poucas linhas.",
 rep="Nos cálculos em que foi descoberto, o efeito borboleta vem de dois gestos da ferramenta: uma medida cortada à partida, e uma contagem de voltas deitada fora a cada passo. Quando se guarda a contagem das voltas, o cálculo refaz-se para trás exatamente. O corpus ARC conclui que este caos é fabricado pelo cálculo. O que divergiu em 1961 não foi o céu: foram três decimais redigitadas.",
 body=[("O que está estabelecido", [
  F+"Em 1961, o meteorologista Edward Lorenz relança uma simulação redigitando um número com três decimais, 0,506, em vez das seis que a máquina guardava, 0,506127. Os dois cálculos separam-se por completo. Publica em 1963. Daí veio a imagem da borboleta cujo bater de asas mudaria o tempo no outro lado do mundo.",
  F+"O mecanismo é conhecido dos matemáticos: um cálculo que estica e depois dobra, e que perde a cada passo um pouco do que sabia. O corpus não pretende tê-lo descoberto. O que propõe é uma leitura."]),
 ("Dois corredores numa pista", [
  "Imagina dois corredores numa pista redonda. Tiras uma fotografia: estão no mesmo sítio. Concluis que vão juntos. Mas um deu 51 voltas e o outro 52. A fotografia mostra a posição, não o número de voltas. É exatamente o que faz um cálculo que «dobra».",
  T+"O cálculo, para refazer: parte de 1/5 e de um número muito próximo, 1/5 + 1/256. A cada passo, duplica o número e guarda só o que vem depois da vírgula. A diferença duplica a cada passo. No oitavo passo, os dois números têm a mesma posição, 1/5. As voltas deitadas fora, somadas, valem 51 para um e 52 para o outro. Nenhuma decimal foi cortada: tudo está em frações exatas."]),
 ("As três fórmulas do caos", [
  T+"Uma só escrita: a diferença ao fim de n passos é a diferença de partida multiplicada n vezes pelo mesmo fator. O corpus distingue nela três motores, e cada um chega sozinho.",
  T+"<strong>A semente cortada.</strong> Faz tu mesmo. Escreve um terço como 0,333: falta um terço de milésimo, quase nada. Multiplica por 1000: obténs 333, quando o resultado verdadeiro é 333,333… Já falta um terço. Multiplica ainda por 1333: faltam 444. Duas multiplicações exatas, e o erro de partida tornou-se enorme. Em cem passos, multiplicando por 3 de cada vez, o que falta a um terço escrito 0,3333 torna-se um número de 44 algarismos. Foi o que aconteceu a Lorenz: a sua semente estava cortada, e o cálculo fê-la crescer.",
  T+"<strong>A dobra.</strong> A medida é perfeita, mas a cada passo guarda-se a posição e deita-se fora a volta. São os dois corredores.",
  T+"<strong>A máquina.</strong> Um computador faz as duas coisas ao mesmo tempo. Guarda 52 algarismos binários; a duplicação pede mais um a cada passo; ao passo 53, nada resta da partida."]),
 ("O que acontece quando se guardam as voltas", [
  T+"Se se anotar a volta deitada fora a cada passo, regressa-se ao ponto de partida sem erro nenhum, tão longe quanto se quiser. Nos cálculos estudados, a confusão desaparece logo que a contagem das voltas é guardada.",
  F+"Verificação independente: em 2018, Saito e Yamaguchi simulam este mesmo cálculo em aritmética exata, sem arredondamento nenhum. Continua caótico. O caos da dobra não vem, pois, do arredondamento: vem da volta deitada fora."]),
 ("A leitura do corpus ARC", [
  L+"«O efeito borboleta não é o bater de uma asa: é o destino de um contador de voltas que a dobra deita fora.» Confundiu-se o sistema com a medida do sistema. O que Lorenz viu divergir foram números tratados por uma ferramenta que mede, o que é legítimo, e que depois dobra esquecendo."]),
 ("O que esta página não diz", [
  "Não diz que se pode prever o tempo indefinidamente. Toda a medida é finita, e o corpus tem esse limite por legítimo: não é ele que acusa.",
  "Não diz que as equações de Lorenz estão erradas. Fazem crescer a diferença que se lhes dá, e fazem-no exatamente. Diz que a diferença de 1961 foi fabricada pela impressora, e que sem diferença à partida não há nada para crescer."]),
 ("O que faria cair esta leitura", [
  P+"Produzir um sistema em que dois pontos de partida diferentes se tornem impossíveis de distinguir embora a operação guarde a contagem das voltas. O corpus afirma que isso não acontece, e dá o teste para o verificar."])],
 links=[(V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos", "Volume 3, capítulo 14: a fórmula do caos (em francês)"), ("/arc/dossiers/lire/Les_trois_corps_n_ont_jamais_bouge/", "Os três corpos nunca se mexeram (em francês)"), ("/arc/dossiers/lire/Modulo_v2_1/", "Modulo: a fórmula II do caos é o seu gesto (em francês)"), ("/arc/dossiers/modulo_chaos_verif.py", "O script que refaz os cálculos")],
 vois=["modulo", "boeing"]),
]
