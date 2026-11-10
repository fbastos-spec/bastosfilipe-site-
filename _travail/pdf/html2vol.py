import sys, re, json, subprocess, ast
R="../../arc"  # lancer depuis _travail/pdf
num=int(sys.argv[1]); corpus=json.load(open(R+"/corpus.json",encoding="utf-8")); vol=[v for v in corpus["volumes"] if v["numero"]==num][0]
ch=vol["chapitres"]; ch=ast.literal_eval(ch) if isinstance(ch,str) else ch
parts=[]
PARTS=(num==3)  # Volume 3 : les Parties sont les chapitres du PDF, les chapitres et annexes en sont les sections
for c in ch:
    h=open(f"{R}/volumes/{vol['slug']}/{c['fichier']}",encoding="utf-8").read()
    m=re.search(r"<main[^>]*>(.*)</main>",h,flags=re.S); body=m.group(1) if m else h
    body=re.sub(r"<nav.*?</nav>","",body,flags=re.S)
    md=subprocess.run(["pandoc","-f","html","-t","markdown-smart-raw_html","--wrap=none"],input=body,capture_output=True,text=True).stdout
    md=re.sub(r" \{#[^}]*\}$","",md,flags=re.M)
    if PARTS and re.match(r"(Chapitre |Annexe |Colophon)",c["titre"]):
        md=re.sub(r"^(#+ )",r"#\1",md,flags=re.M)
    parts.append(md)
head=f'---\ntitle: "{vol["titre"]}"\nsubtitle: "{vol["sous_titre"]}"\nauthor: "Filipe Bastos"\ndate: "Corpus ARC, Volume {num}, version 1.1, octobre 2026"\nlang: fr\nmainfont: "DejaVu Serif"\nmonofont: "DejaVu Sans Mono"\nfontsize: 11pt\ngeometry: margin=2.5cm\ntoc: true\ntoc-depth: {3 if num==3 else 2}\ncolorlinks: true\n---\n\n'
open(f"build/V{num:02d}.md","w",encoding="utf-8").write(head+"\n\n".join(parts))
print(f"V{num:02d}: {len(ch)} fichiers, {sum(len(p) for p in parts)} caracteres, pdf actuel {vol['pages']} pages -> {vol['pdf']}")
