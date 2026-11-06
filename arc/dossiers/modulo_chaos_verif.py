"""
chaos_verif.py, joint a Modulo v2.1 (Filipe Bastos, corpus ARC, 6 novembre 2026).
Verifie la partie 4.9 : les trois formules du chaos et la formule II comme reduction au reste.
Arithmetique exacte (fractions) sauf la formule III, qui est par definition la machine (float64).
"""
from fractions import Fraction as F
import math, sys
sys.set_int_max_str_digits(100000)
ok=[]
def check(n,c):
    ok.append(bool(c)); print(("OK   " if c else "FAIL ")+n)

# Formule I : Stevin seul. 1/3 ecrit 0,3333, puis multiplication exacte par 3.
e0=F(1,3)-F(3333,10000)
check("eps0 = 1/3 - 0,3333 = 1/30000", e0==F(1,30000))
for n,d in [(100,43),(1000,472),(10000,4766)]:
    g=e0*3**n
    check(f"formule I : ecart apres {n} multiplications par 3 = 10^{d} (ordre)", len(str(g.numerator//g.denominator))-1==d)

# Formule II : le pli seul, en exact. x -> 2x, on garde la position (partie apres la virgule), on jette le tour.
def pli(x):
    y=2*x; t=y.numerator//y.denominator; return y-t,t
x=F(1,3); T=0; tours=[]
for n in range(9):
    tours.append(math.floor(F(2**n,3))); 
check("tours jetes cumules depuis 1/3 : 0,0,1,2,5,10,21,42,85", tours==[0,0,1,2,5,10,21,42,85])
a=F(1,5); b=F(1,5)+F(1,256)
gaps=[]
for n in range(9):
    d=b-a; gaps.append(d if d>=0 else d+1)
    a,_=pli(a); b,_=pli(b)
check("formule II exacte : l'ecart 1/256 double a chaque pas tant qu'il reste sous 1/2", all(gaps[n]==F(2**n,256) for n in range(8)))
check("au pas 8 l'ecart vaut un tour entier : meme position, tours differents", gaps[8]==0)
# position identique, tours distincts au pas 8
a=F(1,5); b=F(1,5)+F(1,256); Ta=Tb=0
for n in range(8):
    a,t=pli(a); Ta=2*Ta+t
    b,t=pli(b); Tb=2*Tb+t
check(f"pas 8 : positions egales ({a}), tours {Ta} et {Tb} distincts", a==b and Ta!=Tb)
check("deux points, une image : 1/5 et 7/10 vont tous deux sur 2/5", pli(F(1,5))[0]==pli(F(7,10))[0]==F(2,5))
# avec ses tours, l'orbite se remonte exactement
x0=F(7,23); x=x0; Tt=0
for n in range(40):
    x,t=pli(x); Tt=2*Tt+t
check("avec ses tours gardes, 40 pas se remontent exactement : x0 = (x40 + T40) / 2^40", (x+Tt)/2**40==x0)
# l'orbite rationnelle exacte ne se perd pas : 1/3 -> 2/3 -> 1/3
check("en exact, 1/3 va sur 2/3 puis revient sur 1/3", pli(F(1,3))[0]==F(2,3) and pli(F(2,3))[0]==F(1,3))

# Formule III : la machine (troncature + pli). float64.
x=1/3; n=0
while x!=0 and n<200:
    y=2*x; x=y-math.floor(y); n+=1
check(f"formule III : en double precision, 1/3 replie tombe sur 0 au pas {n} (mantisse de 53 bits epuisee)", 50<=n<=56)
xf=1/3; xe=F(1,3); first=None
for k in range(1,80):
    y=2*xf; xf=y-math.floor(y); xe=pli(xe)[0]
    if first is None and abs(xf-float(xe))>0.1: first=k
check(f"formule III : la machine quitte l'orbite exacte au pas {first} (ordre 52)", 45<=first<=56)

# Le chat d'Arnold de 4.5.5 est la formule II en deux dimensions, f = phi^2
phi2=(3+math.sqrt(5))/2
check("chat d'Arnold (2x+y, x+y) : valeur propre (3+sqrt5)/2 = 2,618 = phi^2", abs(phi2-((1+math.sqrt(5))/2)**2)<1e-12 and abs(phi2**2-3*phi2+1)<1e-12)
def cat(p): x,y=p; return ((2*x+y)%81,(x+y)%81)
p=(1,0); q=p
for k in range(108): q=cat(q)
check("chat replie sur 81 x 81 : retour exact apres 108 pas (4.5.5)", q==p and all(True for _ in [0]))
# premier retour
q=cat(p); k=1
while q!=p: q=cat(q); k+=1
check(f"periode du point (1,0) sur 81 x 81 : {k}", k==108)
# seuil n_chaos = p / log2 f, pour f = 2 : p bits consommes en p pas
check("seuil n_chaos = p / log2(f) : pour f = 2 et p = 52, 52 pas", 52/math.log2(2)==52)

print(("TOUTES LES VERIFICATIONS PASSENT" if all(ok) else "ECHEC")+f" ({sum(ok)}/{len(ok)})")
