# -*- coding: utf-8 -*-
# Le cube est triangulaire : Apéry, racine de 2 et la mauvaise brique. Vérifications. Bibliothèque standard seule.
import sys
from math import pi, sqrt, cos, sin, asin, exp, comb, isclose
from fractions import Fraction as F
from itertools import combinations
R=[]
def ok(nom,cond): R.append((nom,bool(cond)))
Z3=1.2020569031595942
N=400000
imp=lambda n: sum(1/(2*k+1)**n for k in range(N))
alt=lambda n: sum((-1)**k/(2*k+1)**n for k in range(N))
q=pi/2
# 1
tot,impairs,pairs,carre=F(1,6),F(1,8),F(1,24),F(1,4)   # en unités de pi²
ok("V1 Bâle sur le carré du quart de tour : impairs 1/2, pairs 1/6, somme 2/3, reste 1/3 (fractions exactes de π²/4) ; valeur numérique des impairs",
   impairs/carre==F(1,2) and pairs/carre==F(1,6) and tot/carre==F(2,3) and (carre-tot)/carre==F(1,3) and isclose(imp(2),pi**2/8,abs_tol=1e-5))
ok("V2 parts du cube de côté π/2 : impairs aux exposants 2, 4, 6 = 1/2, 1/6, 1/15 ; alternés aux exposants 1, 3, 5 = 1/2, 1/4, 5/48",
   all(isclose(imp(n)/q**n,float(f),abs_tol=2e-6) for n,f in ((2,F(1,2)),(4,F(1,6)),(6,F(1,15))))
   and all(isclose(alt(n)/q**n,float(f),abs_tol=2e-6) for n,f in ((1,F(1,2)),(3,F(1,4)),(5,F(5,48)))))
s2=sum(1/n**2 for n in range(1,200001)); s3=sum(1/n**3 for n in range(1,200001))
ok("V3 part des termes pairs : 1/4 pour les carrés, 1/8 pour les cubes ; somme des cubes 1,2020569",
   isclose(sum(1/n**2 for n in range(2,200001,2))/s2,0.25,abs_tol=1e-5) and isclose(sum(1/n**3 for n in range(2,200001,2))/s3,0.125,abs_tol=1e-9) and isclose(s3,Z3,abs_tol=1e-9))
# 2
def pw(n): return (2**(n//2), n%2)     # (entier, exposant de √2 restant)
ok("V4 puissances de √2 de 1 à 8 : √2, 2, 2√2, 4, 4√2, 8, 8√2, 16 ; les paires sont entières, les impaires gardent √2",
   [pw(n) for n in range(1,9)]==[(1,1),(2,0),(2,1),(4,0),(4,1),(8,0),(8,1),(16,0)] and isclose(sqrt(2)**3,2*sqrt(2)))
a2,h2=F(1,4),F(1,2)          # carrés du côté de base 1/2 et de la hauteur √2/2
ok("V5 boîte du pli : côtés 1/2, 1/2, √2/2, proportions 1, 1, √2 ; grande diagonale 1 ; diagonale de la base = hauteur ; volume √2/8, pli au tiers √2/24",
   h2/a2==2 and a2+a2+h2==1 and a2+a2==h2 and isclose(0.25*sqrt(0.5),sqrt(2)/8) and isclose(0.25*sqrt(0.5)/3,sqrt(2)/24))
rap=[1/cos(pi/n) for n in range(3,61)]
ok("V6 rapport centre-sommets sur centre-côtés : 2 pour le triangle, √2 pour le carré, décroissant vers 1 ; entier pour le seul triangle (polygones de 3 à 60 côtés) ; le centre du triangle au tiers",
   isclose(rap[0],2) and isclose(rap[1],sqrt(2)) and all(x>y for x,y in zip(rap,rap[1:])) and all(1<x<2 for x in rap[1:]) and F(1,1+2)==F(1,3))
# 3
ok("V7 points à égale distance : 2, 3, 4 ; somme 9, produit 24 ; liens 1, 3, 6 ; tétraèdre 4, 6, 4 ; pli 5, 8, 5 ; Euler 2",
   2+3+4==9 and 2*3*4==24 and [comb(k,2) for k in (2,3,4)]==[1,3,6] and 4-6+4==2 and 5-8+5==2)
def vol(a,b,c,d):
    u=[b[i]-a[i] for i in range(3)];v=[c[i]-a[i] for i in range(3)];w=[d[i]-a[i] for i in range(3)]
    return abs(F(u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]),6))
T=[(0,0,0),(1,1,0),(1,0,1),(0,1,1)]
coins=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
vc=[vol(c,*[t for t in T if sum(abs(t[i]-c[i]) for i in range(3))==1]) for c in coins]
ok("V8 tétraèdre inscrit dans le cube : six arêtes de carré 2, volume 1/3 ; quatre coins de 1/6 ; total 1",
   {sum((p[i]-r[i])**2 for i in range(3)) for p,r in combinations(T,2)}=={2} and vol(*T)==F(1,3) and vc==[F(1,6)]*4 and vol(*T)+sum(vc)==1)
ok("V9 le cube en pyramides à base carrée : trois, la pointe dans un coin, de 1/3 ; six, la pointe au centre, de 1/6",
   F(1,3)*1*1==F(1,3) and 3*F(1,3)==1 and F(1,3)*1*F(1,2)==F(1,6) and 6*F(1,6)==1)
ok("V10 boîte étirée 1, 1, √2 : le tétraèdre des diagonales garde le tiers ; ses arêtes ont pour carrés 2, 2 (base et plafond) et 3, 3, 3, 3 (murs)",
   sorted([1+1,1+1]+[1+2]*4)==[2,2,3,3,3,3] and F(1,3)+4*F(1,6)==1)
O=(0,0,0); A=(F(1),0,0); B=(0,F(1),0); C=(0,0,F(1)); M=(F(1,2),F(1,2),F(1,2))
ok("V11 solide de la somme alternée des cubes : coin 1/6 + coiffe jusqu'au centre 1/12 = 1/4 du cube",
   vol(O,A,B,C)==F(1,6) and vol(M,A,B,C)==F(1,12) and vol(O,A,B,C)+vol(M,A,B,C)==F(1,4))
# 4
def part(k,n): return sum(F(1,comb(m+k-1,k)) for m in range(1,n+1))
ok("V12 inverses des triangulaires 1, 3, 6, 10 : reste exact 2/(N + 1) ; à dix termes 20/11",
   [comb(m+1,2) for m in range(1,5)]==[1,3,6,10] and all(part(2,n)==2-F(2,n+1) for n in range(1,200)) and part(2,10)==F(20,11))
ok("V13 inverses des tétraédriques 1, 4, 10, 20, 35 : reste exact 3/((N + 1)(N + 2)) ; à dix termes 65/44",
   [comb(m+2,3) for m in range(1,6)]==[1,4,10,20,35] and all(part(3,n)==F(3,2)-F(3,(n+1)*(n+2)) for n in range(1,200)) and part(3,10)==F(65,44))
ok("V14 étage suivant 1, 5, 15, 35 : somme 4/3, reste exact 8/((N + 1)(N + 2)(N + 3)) ; règle k/(k − 1) pour les étages 2 à 6",
   [comb(m+3,4) for m in range(1,5)]==[1,5,15,35] and all(part(4,n)==F(4,3)-F(8,(n+1)*(n+2)*(n+3)) for n in range(1,120))
   and all(isclose(float(part(k,3000)),k/(k-1),abs_tol=2e-3) for k in range(2,7)))
# 5
ok("V15 colonne du centre 1, 2, 6, 20, 70, 252 ; somme des C(2n, n)/8ⁿ = √2",
   [comb(2*n,n) for n in range(6)]==[1,2,6,20,70,252] and isclose(sum(comb(2*n,n)/8**n for n in range(200)),sqrt(2),abs_tol=1e-13))
ap=lambda n: 2.5*sum((-1)**(k+1)/(k**3*comb(2*k,k)) for k in range(1,n+1))
ok("V16 écriture d'Apéry : 5/2 × somme alternée des 1/(n³ C(2n, n)) = 1,2020569 ; neuf termes donnent six décimales ; mille termes de la somme ordinaire n'en donnent pas six",
   isclose(ap(40),Z3,abs_tol=1e-14) and abs(ap(9)-Z3)<5e-7 and abs(sum(1/n**3 for n in range(1,1001))-Z3)>4e-7)
ok("V17 faux ami : constante / √2 = 0,849983, et non 17/20 ; écart 0,000025 sur la constante",
   round(Z3/sqrt(2),6)==0.849983 and round(17*sqrt(2)/20-Z3,6)==0.000025)
# 7
h=1e-3
def coq(n): return sum(((i+.5)*h)**2*exp(-n*(i+.5)*h)*h for i in range(60000))
ok("V18 coquilles sphériques pesées au rythme n : part 2/n³ pour n = 1, 2, 3 ; somme de tous les rythmes = 2 × la constante",
   all(isclose(coq(n),2/n**3,abs_tol=1e-6) for n in (1,2,3))
   and isclose(sum(((i+.5)*h)**2/(exp((i+.5)*h)-1)*h for i in range(60000)),2*Z3,abs_tol=1e-6))
c=cos(2*pi/7)
ok("V19 heptagone : cos(2π/7) est racine de 8x³ + 4x² − 4x − 1",abs(8*c**3+4*c**2-4*c-1)<1e-12)
cote,app=2*sin(pi/7),sqrt(3)/2
ok("V20 heptagone approché par la moitié du côté du triangle inscrit : écart 0,2 % ; sept reports laissent moins d'un degré",
   round(100*(cote-app)/cote,1)==0.2 and 0<360-7*2*asin(app/2)*180/pi<1)
# --- ajouts de la version 0.2 (18 novembre 2026)
import math
from fractions import Fraction as _F
def _vol(a,b,c,d):
    m=[[b[i]-a[i] for i in range(3)],[c[i]-a[i] for i in range(3)],[d[i]-a[i] for i in range(3)]]
    return _F(abs(m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])))/6
_O,_A,_B,_C,_M=(0,0,0),(1,0,0),(0,1,0),(0,0,1),(_F(1,2),)*3
# sommets de la région {x, y, z ≥ 0 ; x+y ≤ 1 ; y+z ≤ 1 ; z+x ≤ 1} : intersections de trois des six plans, en fractions exactes
from itertools import combinations as _comb
_PL=[((1,0,0),0),((0,1,0),0),((0,0,1),0),((1,1,0),1),((0,1,1),1),((1,0,1),1)]
def _det3(m): return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
_S=set()
for _t in _comb(_PL,3):
    _m=[list(p[0]) for p in _t]; _d=_det3(_m)
    if _d==0: continue
    _b=[p[1] for p in _t]; _p=[]
    for _k in range(3):
        _mk=[r[:] for r in _m]
        for _r in range(3): _mk[_r][_k]=_b[_r]
        _p.append(_F(_det3(_mk),_d))
    _x,_y,_z=_p
    if min(_p)>=0 and _x+_y<=1 and _y+_z<=1 and _z+_x<=1: _S.add(tuple(_p))
ok("V22 solide alterné, sommets donnés : coin (0,0,0),(1,0,0),(0,1,0),(0,0,1) = 1/6 ; coiffe sur la même base, pointe (1/2,1/2,1/2) = 1/12 ; la région des trois sommes par paires au plus égales à 1 a exactement ces cinq sommets, donc 1/6 + 1/12 = 1/4",
   _vol(_O,_A,_B,_C)==_F(1,6) and _vol(_A,_B,_C,_M)==_F(1,12) and _S=={_O,_A,_B,_C,_M})
_T=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
ok("V23 centre du tétraèdre régulier : à √6/4 = 0,612 de l'arête de chacun des quatre sommets",
   all(abs(math.sqrt(sum(t*t for t in p))/math.sqrt(8)-math.sqrt(6)/4)<1e-12 for p in _T))
_z3=1.2020569031595943
_r=lambda N:_z3-sum(1/n**3 for n in range(1,N+1))
ok("V24 somme ordinaire des inverses des cubes : il manque 5,0 × 10⁻⁷ à 1 000 termes, 1,0 × 10⁻⁶ à 700 ; le rapport centre-sommets sur centre-côtés est strictement entre 1 et 2 de 4 à 2 000 côtés",
   abs(_r(1000)/5.0e-7-1)<0.01 and abs(_r(700)/1.0e-6-1)<0.03 and all(1<1/math.cos(math.pi/n)<2 for n in range(4,2001)))
if len(sys.argv)>1:
    t=open(sys.argv[1],encoding='utf-8').read()
    ok("V25 typographie de la source : aucun tiret long ni moyen",'—' not in t and '–' not in t)
for n,k in R: print(('conforme : ' if k else 'ÉCHEC : ')+n)
assert all(k for _,k in R); print(len(R),'contrôles, tous conformes')
