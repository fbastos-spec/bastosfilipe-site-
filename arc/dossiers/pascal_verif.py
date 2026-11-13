# -*- coding: utf-8 -*-
# Pascal sans triangle : la racine digitale et l'intérieur du nombre. Vérifications. Bibliothèque standard seule.
import sys, random
from math import comb
from itertools import product
from collections import Counter
random.seed(9)
R=[]
def ok(nom,cond): R.append((nom,bool(cond)))
r=lambda n:1+(n-1)%9
def pointe(d):
    d=list(d)
    while len(d)>1: d=[r(a+b) for a,b in zip(d,d[1:])]
    return d[0]
def nombres(L,k=4000):
    if L<=5: return (d for d in product(range(10),repeat=L) if d[0]>0)
    return ([random.randint(1,9)]+[random.randint(0,9) for _ in range(L-1)] for _ in range(k))
SUP={2:[0,0],3:[0,1,0],4:[0,2,2,0],5:[0,3,5,3,0],6:[0,4,0,0,4,0],7:[0,5,5,1,5,5,0],8:[0,6,2,7,7,2,6,0],9:[0,7,0,1,6,1,0,7,0],10:[0,8,8,2,8,8,2,8,8,0]}
ok("V1 la pointe est la somme des chiffres pesés par la ligne de Pascal (1 2 1, 1 3 3 1, 1 4 6 4 1, …), réduite ; longueurs 2 à 10",
   all(pointe(d)==r(sum(comb(L-1,i)*x for i,x in enumerate(d))) for L in range(2,11) for d in nombres(L)))
ok("V2 pointe = racine + supplément de l'intérieur ; table des suppléments de 2 à 10 chiffres ; les bords ne pèsent jamais (tous les nombres jusqu'à 5 chiffres, 4000 tirages au-delà)",
   all(SUP[L]==[(comb(L-1,i)-1)%9 for i in range(L)] and SUP[L][0]==SUP[L][-1]==0 for L in SUP)
   and all(pointe(d)==r(sum(d)+sum(a*b for a,b in zip(SUP[L],d))) for L in SUP for d in nombres(L)))
ok("V3 à deux chiffres la pointe est la racine : Pascal n'y ajoute rien",all(pointe(d)==r(sum(d)) for d in nombres(2)))
T={t:[n for n in range(100,1000) if pointe(map(int,str(n)))==t] for t in range(1,10)}
c=lambda n:(n//10)%10
ok("V4 triplets : pointe = racine + centre, pour les 900 ; chaque pointe a exactement 100 triplets",
   all(pointe(map(int,str(n)))==r(r(n)+c(n)) for n in range(100,1000)) and all(len(T[t])==100 for t in T))
ok("V5 proportion : pour chaque pointe, 10 triplets par racine et 20 pour la racine du même nom que la pointe (centres 0 et 9)",
   all(Counter(r(n) for n in T[t])=={k:(20 if k==t else 10) for k in range(1,10)} and {c(n) for n in T[t] if r(n)==t}=={0,9} for t in T))
ok("V6 pointe 9 : la racine est l'inverse du centre (racine + centre = 9), sans exception ; seuls couples : les quatre paires inverses dans les deux sens, et le 9 avec 9 ou 0",
   all(r(n)+c(n)==9 or (r(n)==9 and c(n) in (0,9)) for n in T[9]) and {(r(n),c(n)) for n in T[9]}=={(k,9-k) for k in range(1,9)}|{(9,0),(9,9)})
ok("V7 pointe 8 : une famille où racine et centre sont le même nombre (4 et 4) ; chaque pointe en a une, et pour le 9 c'est le 9 lui-même",
   (4,4) in {(r(n),c(n)) for n in T[8]} and all(any(r(n)==c(n) for n in T[t]) for t in T) and {r(n) for n in T[9] if r(n)==c(n)}=={9})
rail=lambda x:{1:'D',4:'D',7:'D',2:'G',5:'G',8:'G',3:'A',6:'A',9:'A'}[x]
ok("V8 pointe 9 : centre et somme des flancs sur le même rail ; flancs 7, 1, 4 pour les centres 1, 4, 7 ; 5, 8, 2 pour 2, 5, 8 ; 3, 6, 9 pour 3, 6, 9",
   all(rail(c(n))==rail(r(n//100+n%10)) for n in T[9] if c(n)) and {b:r(n//100+n%10) for n in T[9] for b in [c(n)] if b}=={1:7,4:1,7:4,2:5,5:8,8:2,3:3,6:6,9:9})
fam=sorted(n for n in T[9] if r(n)==4)
ok("V9 les familles avancent par 99 avec un seul pas de 9 (racine 4 : 157, 256, … 850, 859, 958) ; la liste entière avance par pas de 8, de 9 et de 17 = 8 + 9 (72, 18 et 9 fois)",
   fam==[157,256,355,454,553,652,751,850,859,958] and Counter(b-a for a,b in zip(fam,fam[1:]))=={99:8,9:1} and Counter(b-a for a,b in zip(T[9],T[9][1:]))=={8:72,9:18,17:9})
ok("V10 dans les 100 : 256, 512, 280 = 5 × 7 × 8, 578, 495, 891 ; carrés 256, 289, 529, 784 = 28², 900 ; un seul cube, 512",
   all(x in T[9] for x in (256,512,280,578,495,891)) and 280==5*7*8 and [n for n in T[9] if round(n**.5)**2==n]==[256,289,529,784,900] and [n for n in T[9] if round(n**(1/3))**3==n]==[512])
p=1/9
ok("V11 témoin : un triplet sur neuf pointe 9 ; puissances de 2 à trois chiffres : 128 (pointe 4), 256 et 512 (pointe 9) ; au moins deux sur trois sans raison : 3,4 %",
   [pointe(map(int,str(n))) for n in (128,256,512)]==[4,9,9] and [2**k for k in range(20) if 100<=2**k<1000]==[128,256,512] and round(3*p*p*(1-p)+p**3,3)==0.034)
ok("V12 dix chiffres : la pointe ne lit que le premier, le dernier, et trois fois le quatrième et le septième",
   [comb(9,i)%9 for i in range(10)]==[1,0,0,3,0,0,3,0,0,1] and all(pointe(d)==r(d[0]+d[9]+3*(d[3]+d[6])) for d in nombres(10) if d[0]+d[9]+d[3]+d[6]>0))
ok("V13 exemples : 65 536, racine 7, anneau 3 × 8, centre 5 × 5, pointe 2 ; 1024, racine 7, milieu 2 × 2, pointe 2 ; 256 : 4 + 5 ; 512 : 8 + 1",
   pointe([6,5,5,3,6])==2==r(25+24+25) and r(25)==7 and pointe([1,0,2,4])==2==r(7+4) and r(256)==4 and r(512)==8)
if len(sys.argv)>1:
    t=open(sys.argv[1],encoding='utf-8').read()
    ok("V14 typographie de la source : aucun tiret long ni moyen",'—' not in t and '–' not in t)
for n,k in R: print(('conforme : ' if k else 'ÉCHEC : ')+n)
assert all(k for _,k in R); print(len(R),'contrôles, tous conformes')
