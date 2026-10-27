# Faire tomber ARC, v2.0 : extraction des énoncés à statut P des douze volumes et génération de la table (markdown sur la sortie standard).
# Usage : python3 faire_tomber_extract.py <dossier arc/volumes> <arc/corpus.json> > Faire_tomber_ARC_v2_0.md
# Bibliothèque standard de Python seulement.
import re, glob, html, json, collections, sys
R=sys.argv[1]
corpus=json.load(open(sys.argv[2],encoding="utf-8"))
titres={v["slug"]:(v["numero"] if "numero" in v else int(v["slug"][1:3]), v["titre"]) for v in corpus["volumes"]}
# énoncé à statut P : formats du corpus
ENP=re.compile(r"^(?:(É\s?\d+\.\d+)\s*(?:\(P(?:[^)]*)\)|·\s*P\s*·)|(\[\d+\.\d+\])\s*P\.|(V\d+\.\d+\.\d+)\s*\(P[^)]*\)|(\d+\.\d+)\s*\[P[^\]]*\]|(P-[A-Z0-9]{1,5}-\d+)\s*\((?:Prédiction|P)[^)]*\)|(P\d|F-\d+|F\d)\s*[:(.]?\s*(?:\(P\)|Prédiction)?)")
CRIT=re.compile(r"réfut|ferait tomber|feraient tomber|tomberait|tombe si|Arbitre\s*:|Chute\s*:|Clause|critère|falsifi|Ce qui la fer|Ce qui le fer|mis en défaut|serait contredit", re.I)
out=[]
for f in sorted(glob.glob(f"{R}/v*/[0-9]*.html")):
    slug=f.split("/")[-2]
    t=open(f,encoding="utf-8").read()
    h=re.search(r"<title>(.*?)</title>", t, re.S); chapt=html.unescape(h.group(1)).split(" · ")[0].strip()
    body=re.search(r'<main class="chapter">(.*?)</main>', t, re.S).group(1)
    blocks=re.findall(r"<(p|li|tr|h3)[^>]*>(.*?)</\1>", body, re.S)
    prev=None
    for tag,blk in blocks:
        txt=html.unescape(re.sub(r"<[^>]+>"," ",blk)); txt=re.sub(r"\s+"," ",txt).strip()
        m=ENP.match(txt)
        if m and len(txt)>40:
            ident=next(g for g in m.groups() if g)
            lead = prev if (tag == "li" and prev and prev.rstrip().endswith(":") and len(prev) < 400 and (not out or out[-1].get("lead") != prev)) else None
            out.append(dict(vol=slug, chapitre=chapt, id=ident, texte=txt, critere=bool(CRIT.search(txt)), lead=lead))
        prev=txt

rows = out
vols = {v["slug"]: v for v in corpus["volumes"]}
par_vol = collections.OrderedDict()
for r in rows:
    par_vol.setdefault(r["vol"], collections.OrderedDict()).setdefault(r["chapitre"], []).append(r)
n = len(rows)
nv = len(par_vol)

def md(s):
    # protéger les caractères que pandoc lirait comme balisage
    s = s.replace("\\", "\\\\")
    s = re.sub(r"(?<!\w)([*_])", r"\\\1", s)
    s = s.replace("#", "\\#")
    return s

out = []
out.append("""---
title: "Faire tomber ARC"
subtitle: "La table complète des énoncés à statut Prédiction des douze volumes, recopiés avec leur adresse"
author: "Filipe Bastos"
date: "Corpus ARC, version 2.0, 26 octobre 2026"
lang: fr
mainfont: "DejaVu Serif"
monofont: "DejaVu Sans Mono"
fontsize: 10pt
geometry: margin=2.2cm
toc: true
toc-depth: 2
colorlinks: true
---

# Avant-propos

La version 1.0 de ce dossier (15 octobre 2026) retenait cinq prédictions et trois théorèmes. Elle donnait du corpus une image bien plus étroite que ce que les volumes exposent, et la responsabilité en est au scribe. Elle est retirée et remplacée par cette table.

La table recopie, sans modification, chaque énoncé des douze volumes dont le statut est P (Prédiction), avec son adresse : le volume, le chapitre, le numéro de l'énoncé. Le texte est celui des chapitres publiés sur bastosfilipe.com/arc le 26 octobre 2026, extrait par script (annexe) ; rien n'y est ajouté, rien n'en est retranché. Là où un énoncé renvoie à un critère écrit dans un autre énoncé ou dans une annexe du volume, l'adresse suffit pour l'y trouver.

Le compte est de %d énoncés à statut P, répartis sur %d volumes :

""" % (n, nv))
for slug, chaps in par_vol.items():
    v = vols[slug]; k = sum(len(x) for x in chaps.values())
    out.append(f"- Volume {int(slug[1:3])}, {md(v['titre'])} : {k} énoncés\n")
out.append("""
Les volumes 0 et 2 ne portent pas d'énoncé à statut P sous leur propre numérotation ; le Volume 0 (Le Seuil, chapitre 2) tient la table des huit reçus physiques, qui renvoie aux énoncés ci-dessous.

Ce que dit le statut P dans le corpus (Volume 0, chapitre 1) : « Un énoncé daté qui peut échouer, avec, le jour où il est inscrit, le reçu extérieur contre lequel il sera testé, la fenêtre et la méthode (règle R11). » Et la raison du statut, de l'auteur : « Tant mieux si les prédictions tombent : on apprendra et précisera plus. Elles nous donneront de l'information. »

""")
for slug, chaps in par_vol.items():
    v = vols[slug]
    out.append(f"\n# Volume {int(slug[1:3])}. {md(v['titre'])}\n\n*{md(v.get('sous_titre',''))}*\n\n")
    for chap, lst in chaps.items():
        out.append(f"\n## {md(chap)}\n\n")
        for r in lst:
            if r.get("lead"): out.append("*" + md(r["lead"]) + "*\n\n")
            out.append(md(r["texte"]) + "\n\n")
out.append("""
# Annexe. Le script

Le script lit les chapitres HTML des douze volumes du site, retient chaque bloc (paragraphe, item de liste, ligne de tableau) qui s'ouvre sur un numéro d'énoncé suivi du statut P, dans les quatre formes de numérotation du corpus (« É1.27 (P) », « É 5.10 · P · », « [7.28] P. », « V4.1.5 (P) », « 6.1 [P] »), ainsi que les prédictions nommées (« P-COL-1 (Prédiction, avec critère) », « F-1 » à « F-11 », « P1 » à « P4 »), et le recopie sans le modifier. Bibliothèque standard de Python seulement. Fichier `faire_tomber_extract.py`, déposé avec cette pièce ; usage : `python3 faire_tomber_extract.py <dossier arc/volumes> <arc/corpus.json>`.

**Colophon.** Modèle, questions, lectures et règles : Filipe Bastos. Scribe : Claude, sous la contradiction de l'auteur.

*Au 26 octobre 2026. Corpus ARC, Filipe Bastos, CC BY 4.0.*
""")
sys.stdout.write("".join(out))
