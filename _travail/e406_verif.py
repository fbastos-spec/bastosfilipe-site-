# -*- coding: utf-8 -*-
# Erdős 406 : la forme et le doublement : vérifications. Bibliothèque standard seule.
import sys, re
from itertools import product
R=[]
def ok(nom,cond): R.append((nom,bool(cond)))
def b3(x):
    d=[]
    while x: d.append(x%3); x//=3
    return d or [0]
def propre(x):
    while x:
        x,r=divmod(x,3)
        if r==2: return False
    return True
def racine(n): return 1+(n-1)%9
def coeur(n):
    d=[int(c) for c in str(n)]
    while len(d)>1: d=[racine(a+b) for a,b in zip(d,d[1:])]
    return d[0]

ok("V1 compte direct : pour l'exposant n de 0 à 20 000, 2^n s'écrit en 0 et 1 en base 3 seulement pour n = 0, 2, 8 (1, 4, 256)",
   [n for n in range(20001) if propre(2**n)]==[0,2,8])
ok("V2 écritures en base 3 : 1 = 1 ; 4 = 1 + 3 ; 256 = 1 + 3 + 9 + 243 ; 256 = 243 + 13 et 13 = 1 + 3 + 9",
   b3(1)==[1] and b3(4)==[1,1] and b3(256)==[1,1,1,0,0,1] and 256==243+13 and 13==1+3+9 and 243==3**5)
ok("V3 les racines des puissances de 2 tournent sur 1, 2, 4, 8, 7, 5 ; deux derniers chiffres en 0 et 1 : seules les racines 1 et 4 passent",
   [racine(2**n) for n in range(6)]==[1,2,4,8,7,5] and sorted({racine(2**n) for n in range(600) if all(x<2 for x in (b3(2**n)+[0])[:2])})==[1,4])
niv=[]
for k in range(1,13):
    per=2*3**(k-1); niv.append(sum(1 for n in range(per) if all((pow(2,n,3**k)//3**i)%3<2 for i in range(k))))
ok("V4 le dedans : sur les k derniers chiffres, 2 × 3^(k−1) adresses d'exposants, il en passe 2^(k−1), pour k de 1 à 12 (1, 2, 4, … 2048)",
   niv==[2**(k-1) for k in range(1,13)])
# assemblages alternés
def mots(Lmax):
    for L in range(2,Lmax+1):
        for st in (2,3): yield [st if i%2==0 else 5-st for i in range(L)]
S={sum(w) for w in mots(90)}
ok("V5 addition seule, pièces alternées : jusqu'à 200, manquent 1 et 4 à chaque tour de 5 (1, 4, 6, 9, 11, 14, …), plus les pièces 2 et 3",
   [n for n in range(1,201) if n not in S]==sorted([2,3]+[n for n in range(1,201) if n%5 in (1,4)]))
V=set()
for w in mots(12):
    for ops in product('+*',repeat=len(w)-1):
        V.add(eval(str(w[0])+''.join(o+str(x) for o,x in zip(ops,w[1:]))))
ok("V6 addition et produit, pièces alternées : jusqu'à 60, seuls 1, 2, 3, 4 ne sont pas construits ; 6 = 2 × 3, 9 = 3 + 2 × 3",
   [n for n in range(1,61) if n not in V]==[1,2,3,4] and 2*3==6 and 3+2*3==9)
def construit(n):       # règle générale, n >= 5
    k,r=divmod(n,5)
    if r==0: e='+'.join(['2+3']*k)
    elif r==2: e='+'.join(['2+3']*k+['2'])
    elif r==3: e='+'.join(['3+2']*k+['3'])
    elif r==1: e='+'.join(['2+3']*(k-1)+['2*3'])
    else:      e='+'.join(['3+2']*(k-1)+['3+2*3'])
    p=re.findall(r'\d',e)
    return eval(e)==n and all(a!=b for a,b in zip(p,p[1:])) and set(p)=={'2','3'}
ok("V7 règle générale : tout nombre de 5 à 5000 a un assemblage alterné explicite ; les exclus sont 1 et 4",
   all(construit(n) for n in range(5,5001)))
ok("V8 256 = 8 × 8 × 4 = 4 × 64 ; en doublements 3 + 2 + 3 = 8 ; 256 = 9 × 28 + 4 ; racine 4, somme des chiffres 13",
   256==8*8*4==4*64==2**(3+2+3) and 256==9*28+4 and racine(256)==4 and 2+5+6==13)
ok("V9 pyramide : 256, puis 7 2, puis 9 ; le cœur de 1 est 1, celui de 4 est 4",
   [racine(2+5),racine(5+6)]==[7,2] and coeur(256)==9 and coeur(1)==1 and coeur(4)==4)
ok("V10 huit doublements et cinq triplements se frôlent : 2^8 − 3^5 = 13",2**8-3**5==13)
if len(sys.argv)>1:
    t=open(sys.argv[1],encoding='utf-8').read()
    ok("V11 typographie de la source : aucun tiret long ni moyen",'—' not in t and '–' not in t)
for n,c in R: print(('conforme : ' if c else 'ÉCHEC : ')+n)
assert all(c for _,c in R); print(len(R),'contrôles, tous conformes')
