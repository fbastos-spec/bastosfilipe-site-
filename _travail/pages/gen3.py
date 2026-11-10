import re, json, os, html, sys
sys.path.insert(0,'/home/claude/pages')
R='/home/claude/bastosfilipe-site-/'
src=open('/home/claude/pages/gen.py',encoding='utf-8').read()
ns={}; exec(src[:src.index("TIT={p['slug']")],ns)
FR=ns['PAGES']
KEY={'modulo':'modulo','boeing-787-248-jours':'boeing','pyramide-de-kheops-pi':'kheops','hippase-racine-de-2':'hippase','effet-papillon':'papillon'}
for p in FR:
    p['key']=KEY[p['slug']]; p['vois']=[KEY.get(s,'fr:'+s) for s in p['vois']]
st=lambda s:f'<span class="q-st">{s}</span>'
from pages_en import pages_en
from pages_pt import pages_pt
EN=pages_en(st('Fact'),st('Theorem'),st('Reading'),st('Prediction'))
PT=pages_pt(st('Facto'),st('Teorema'),st('Leitura'),st('Predição'))
def split(path):
    t=open(R+path,encoding='utf-8').read(); a=t.index('<body'); b=t.index('<main'); c=t.index('</main>')+7
    return t[:a],t[a:b],t[c:]
H_FR,N_FR,F_FR=split('sujets/borne-de-tsirelson/index.html')
H_EN,N_EN,F_EN=split('en/topics/tsirelson-bound/index.html')
_,N_PT,F_PT=split('pt/contradicoes/index.html')
N_PT=N_PT.replace(' aria-current="page"','').replace('href="/bio/#content"','href="#content"')
F_PT=re.sub(r'<script>\(function\(\)\{var f=document\.getElementById\("contra-form"\).*?</script>','',F_PT,flags=re.S)
assert 'contra-form' not in F_PT
H_PT=H_FR.replace('<html lang="fr">','<html lang="pt">').replace('content="fr_CA"','content="pt_PT"')
C={'fr':dict(pages=FR,H=H_FR,N=N_FR,F=F_FR,base='/sujets/',hub='Les grandes questions',short='La réponse courte',more='Pour aller plus loin',near='Questions voisines',site='Filipe Bastos · Corpus ARC',tpl_url='https://bastosfilipe.com/sujets/borne-de-tsirelson/',il='fr',
   meta='Chaque énoncé porte son statut : Fait (ce que la science tient), Théorème (calcul vérifié), Lecture (interprétation du corpus), Prédiction (ce qui la ferait tomber).<br>Filipe Bastos · Corpus ARC · CC BY 4.0 · <a href="/#methode">Méthode de lecture : l\'Empathie fractale, sociale et relationnelle</a> · <a href="/contradictions/">Une erreur ? Envoyez une contradiction</a>'),
 'en':dict(pages=EN,H=H_EN,N=N_EN,F=F_EN,base='/en/topics/',hub='The big questions',short='The short answer',more='Further reading',near='Related questions',site='Filipe Bastos · ARC Corpus',tpl_url='https://bastosfilipe.com/en/topics/tsirelson-bound/',il='en',
   meta='Every statement carries its status: Fact (what science holds), Theorem (verified computation), Reading (the corpus\'s interpretation), Prediction (what would bring it down).<br>Filipe Bastos · ARC Corpus · CC BY 4.0 · <a href="/en/#methode">Reading method: fractal, social and relational empathy</a> · <a href="/en/contradictions/">Found an error? Send a contradiction</a>'),
 'pt':dict(pages=PT,H=H_PT,N=N_PT,F=F_PT,base='/pt/temas/',hub='As grandes questões',short='A resposta curta',more='Para ir mais longe',near='Questões vizinhas',site='Filipe Bastos · Corpus ARC',tpl_url='https://bastosfilipe.com/sujets/borne-de-tsirelson/',il='pt',
   meta='Cada enunciado traz o seu estatuto: Facto (o que a ciência sustenta), Teorema (cálculo verificado), Leitura (interpretação do corpus), Predição (o que a faria cair).<br>Filipe Bastos · Corpus ARC · CC BY 4.0 · <a href="/pt/#methode">Método de leitura: a empatia fractal, social e relacional</a> · <a href="/pt/contradicoes/">Um erro? Envie uma contradição</a>')}
URL={l:{p['key']:C[l]['base']+p['slug']+'/' for p in C[l]['pages']} for l in C}
TIT={l:{p['key']:p['title'] for p in C[l]['pages']} for l in C}
def other_title(l,ref):
    lang,slug=ref.split(':'); path={'fr':'sujets/','en':'en/topics/'}[lang]+slug+'/index.html'
    t=open(R+path,encoding='utf-8').read()
    return ('/'+path[:-10], html.unescape(re.search(r'<h1 class="entry-title">(.*?)</h1>',t).group(1)))
def exists(u):
    p=R+u.strip('/'); return any(os.path.exists(x) for x in (p+'.html',os.path.join(p,'index.html'),p))
e=lambda s:html.escape(s,quote=True)
D='https://bastosfilipe.com'
for l,c in C.items():
    for p in c['pages']:
        k=p['key']; url=D+URL[l][k]; h=c['H']
        od=re.search(r'<meta name="description" content="([^"]*)"',h).group(1); h=h.replace(od,e(p['desc']))
        ot=re.search(r'<title>(.*?) · Filipe Bastos</title>',h).group(1)
        h=h.replace(f'<title>{ot} · Filipe Bastos</title>',f"<title>{e(p['title'])} · Filipe Bastos</title>").replace(f'content="{ot}"',f'content="{e(p["title"])}"')
        h=re.sub(r'(<link rel="alternate" hreflang="[^"]*" href="[^"]*">)+','',h)
        h=h.replace(c['tpl_url'],url)
        alt=''.join(f'<link rel="alternate" hreflang="{x}" href="{D+URL[x][k]}">' for x in ('fr','en','pt'))+f'<link rel="alternate" hreflang="x-default" href="{D+URL["fr"][k]}">'
        h=h.replace('<style>.q-page',alt+'\n<style>.q-page',1); assert alt in h
        ld={"@context":"https://schema.org","@graph":[{"@type":"Article","headline":p['title'],"description":p['desc'],"inLanguage":c['il'],"url":url,"author":{"@type":"Person","@id":D+"/#filipe-bastos","name":"Filipe Bastos","url":D+"/bio/"},"publisher":{"@id":D+"/#filipe-bastos"},"license":"https://creativecommons.org/licenses/by/4.0/","datePublished":"2026-11-10","dateModified":"2026-11-10","isPartOf":{"@id":D+"/#site"},"about":p['eyebrow']},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":p['title'],"acceptedAnswer":{"@type":"Answer","text":p['rep']}}]},{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Filipe Bastos","item":D+{'fr':'/','en':'/en/','pt':'/pt/'}[l]},{"@type":"ListItem","position":2,"name":c['hub'],"item":D+c['base']},{"@type":"ListItem","position":3,"name":p['eyebrow'],"item":url}]}]}
        h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>',h,flags=re.S)
        assert 'sirelson' not in h, re.findall(r'.{50}sirelson.{30}',h)[:2]
        n=c['N']
        for x,root in (('fr','/'),('en','/en/'),('pt','/pt/')):
            a=f'data-l="{x}" href="{root}"'; assert n.count(a)==1,(l,a); n=n.replace(a,f'data-l="{x}" href="{URL[x][k]}"')
        b=[f'<main id="content" data-pagefind-meta="title:{e(p["title"])}">','<div class="wrap page-shell q-page">',f'<p class="q-bc" style="font-size:.85rem;margin:0 0 6px"><a href="{c["base"]}">{c["hub"]}</a></p>',f'<span class="sec-eyebrow">{p["eyebrow"]}</span>',f'<h1 class="entry-title">{p["title"]}</h1>',f'<div class="q-rep"><span class="sec-eyebrow">{c["short"]}</span><p>{p["rep"]}</p></div>']
        for h2,ps in p['body']:
            b.append(f'<h2>{h2}</h2>'); b+=[f'<p>{x}</p>' for x in ps]
        for u,_ in p['links']: assert exists(u),u
        b.append(f'<h2>{c["more"]}</h2>'); b.append('<ul class="q-links">'+''.join(f'<li><a href="{u}">{t}</a></li>' for u,t in p['links'])+'</ul>')
        vs=[]
        for v in p['vois']:
            vs.append(other_title(l,v) if ':' in v else (URL[l][v],TIT[l][v]))
        b.append(f'<h2>{c["near"]}</h2>'); b.append('<ul class="q-links">'+''.join(f'<li><a href="{u}">{t}</a></li>' for u,t in vs)+f'<li><a href="{c["base"]}">{c["hub"]}</a></li></ul>')
        b.append(f'<p class="q-meta">{c["meta"]}</p>'); b+=['</div>','</main>']
        body='\n'.join(b); assert '—' not in body and '–' not in body
        for m in re.findall(r'href="(/[^"#]*)',body): assert exists(m) or m in URL[l].values() or m.rstrip('/')+'/' == c['base'], (l,m)
        out=h+n+body+c['F']
        d=R+URL[l][k].strip('/'); os.makedirs(d,exist_ok=True); open(d+'/index.html','w',encoding='utf-8').write(out)
        print(l,URL[l][k],len(out))
json.dump({l:[{'key':p['key'],'url':URL[l][p['key']],'title':p['title'],'desc':p['desc']} for p in C[l]['pages']] for l in C},open('/home/claude/pages/all.json','w'),ensure_ascii=False)
# hub pt
hub_h=H_PT; od=re.search(r'<meta name="description" content="([^"]*)"',hub_h).group(1)
dpt="As grandes questões da ciência e do pensamento, lidas pelo corpus ARC: cada página responde primeiro em duas frases e separa depois o que está estabelecido, o que está demonstrado e o que é lido."
hub_h=hub_h.replace(od,e(dpt)); ot=re.search(r'<title>(.*?) · Filipe Bastos</title>',hub_h).group(1)
hub_h=hub_h.replace(f'<title>{ot} · Filipe Bastos</title>','<title>As grandes questões · Filipe Bastos</title>').replace(f'content="{ot}"','content="As grandes questões"')
hub_h=re.sub(r'(<link rel="alternate" hreflang="[^"]*" href="[^"]*">)+','',hub_h).replace('https://bastosfilipe.com/sujets/borne-de-tsirelson/',D+'/pt/temas/')
hub_h=hub_h.replace('<style>.q-page',f'<link rel="alternate" hreflang="fr" href="{D}/sujets/"><link rel="alternate" hreflang="en" href="{D}/en/topics/"><link rel="alternate" hreflang="pt" href="{D}/pt/temas/"><link rel="alternate" hreflang="x-default" href="{D}/sujets/">\n<style>.q-page',1)
ld={"@context":"https://schema.org","@type":"CollectionPage","name":"As grandes questões","description":dpt,"inLanguage":"pt","url":D+"/pt/temas/","isPartOf":{"@id":D+"/#site"}}
hub_h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>',hub_h,flags=re.S)
n=N_PT.replace('data-l="fr" href="/"','data-l="fr" href="/sujets/"').replace('data-l="en" href="/en/"','data-l="en" href="/en/topics/"').replace('data-l="pt" href="/pt/"','data-l="pt" href="/pt/temas/"')
items=''.join(f'<li><a href="{URL["pt"][p["key"]]}"><strong>{p["title"]}</strong></a><br><span>{p["desc"]}</span></li>\n' for p in PT)
body=f'<main id="content" data-pagefind-meta="title:As grandes questões">\n<div class="wrap page-shell q-page">\n<span class="sec-eyebrow">Corpus ARC</span>\n<h1 class="entry-title">As grandes questões</h1>\n<p>{dpt}</p>\n<ul class="q-hub" style="list-style:none;padding:0">{items}</ul>\n<p>Outras questões estão disponíveis <a href="/en/topics/">em inglês</a> e <a href="/sujets/">em francês</a>.</p>\n<p class="q-meta">{C["pt"]["meta"]}</p>\n</div>\n</main>'
os.makedirs(R+'pt/temas',exist_ok=True); open(R+'pt/temas/index.html','w',encoding='utf-8').write(hub_h+n+body+F_PT); print('hub pt ok')
