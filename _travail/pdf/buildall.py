import subprocess,re,difflib,json,sys,os
R="../../arc"  # lancer depuis _travail/pdf; corpus=json.load(open(R+"/corpus.json",encoding="utf-8"))
def txt(p):
    t=subprocess.run(['pdftotext',p,'-'],capture_output=True,text=True).stdout
    return re.sub(r'\s+',' ',re.sub(r'-\n','',t))
def pages(p): return int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',p],capture_output=True,text=True).stdout).group(1))
for v in corpus["volumes"]:
    n=v["numero"]
    if len(sys.argv)>1 and str(n) not in sys.argv[1:]: continue
    subprocess.run([sys.executable,"-I","html2vol.py",str(n)],capture_output=True)
    b=f"build/V{n:02d}"
    subprocess.run(["pandoc",b+".md","-s","--pdf-engine=xelatex","-V","documentclass=report","-V","classoption=oneside","-H","build/fallback.tex","-o",b+".tex"],capture_output=True)
    for i in range(3): subprocess.run(["xelatex","-interaction=nonstopmode",f"V{n:02d}.tex"],cwd="build",capture_output=True)
    log=open(b+".log",errors="replace").read()
    old=R+"/"+v["pdf"]; wa,wb=txt(old).split(),txt(b+".pdf").split()
    ops=[o for o in difflib.SequenceMatcher(None,wa,wb,autojunk=False).get_opcodes() if o[0]!='equal']
    dele=sum(o[2]-o[1] for o in ops); ins=sum(o[4]-o[3] for o in ops)
    print(f"V{n:02d} pages site {pages(old)} (json {v['pages']}) -> {pages(b+'.pdf')} | manquants {log.count('Missing character')} | erreurs {len(re.findall(r'^!',log,flags=re.M))} | mots retires {dele}, ajoutes {ins}, blocs {len(ops)}")
    json.dump([(o[0],' '.join(wa[o[1]:o[2]])[:300],' '.join(wb[o[3]:o[4]])[:300]) for o in ops],open(b+"_diff.json","w"),ensure_ascii=False,indent=0)
