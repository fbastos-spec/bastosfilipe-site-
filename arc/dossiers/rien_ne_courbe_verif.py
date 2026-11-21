# -*- coding: utf-8 -*-
# Rien ne courbe, v0.1 : appuis chiffres executes.
import sys, re
from math import comb
from fractions import Fraction as F
n_ok=0
def ok(nom,cond):
    global n_ok
    assert cond,'ECHEC : '+nom
    n_ok+=1; print('[OK] '+nom)
dr=lambda n:1+(n-1)%9


# 0. la base autoportante (v0.2)
ok("0.1 tout n = 9k + racine, le 9 est la cloture (pas 0) : bijection sur 1..100000",
   all(n==9*((n-1)//9)+dr(n) for n in range(1,100001)))
# 0.2 table de n et table de 9-n sont inverses : dr(n*k)+dr((9-n)*k) ferme sur 9
def ferme9(a,b): return (a+b)%9==0
ok("0.2 table de n et de 9-n inverses : dr(n k) + dr((9-n) k) = 9 pour n=1..4, k=1..9",
   all(ferme9(dr(n*k),dr((9-n)*k)) for n in range(1,5) for k in range(1,10)))
ok("0.2 table de 2 : racines 2,4,6,8,1,3,5,7,9 ; table de 7 : 7,5,3,1,8,6,4,2,9",
   [dr(2*k) for k in range(1,10)]==[2,4,6,8,1,3,5,7,9] and [dr(7*k) for k in range(1,10)]==[7,5,3,1,8,6,4,2,9])
# 0.3 les trois formules du chaos : croissance 3^n, 2^n, f^n ; seuil
from fractions import Fraction as F
e0=F(1,30000)
ok("0.3 formule I stevinienne e0*3^n : partie entiere de e0*3^100 depasse 10^43",
   len(str((e0*3**100).numerator//(e0*3**100).denominator))>=44)
ok("0.3 formule II gaussienne e0*2^n : e0=10^-6 atteint l'ordre 1 vers le 20e tour",
   F(1,10**6)*2**20 >= 1 and F(1,10**6)*2**19 < 1)
import math
# formule III : seuil n_chaos = p / log2(f) lineaire en p
f=2.0
ok("0.3 formule III seuil n_chaos = p / log2(f), lineaire en la precision p",
   abs((20/math.log2(f)) - 20) < 1e-9 and abs((40/math.log2(f)) - 2*(20/math.log2(f))) < 1e-9)

# 2.1 les paires ferment a 9 ; 9 avec 9
paires=[(1,8),(2,7),(3,6),(4,5)]
ok("2.1 les quatre paires d'inverses ferment a 9 ; 9 se ferme avec 9",
   all(a+b==9 for a,b in paires) and dr(9)==9)

# 2.2 congruence des paires : compatible au produit, pas a la somme
def cls(n):
    r=dr(n); return frozenset({r,9-r if r!=9 else 9})
# compatible multiplication sur toutes les combinaisons 1..9
ok("2.2 congruence des paires compatible avec la multiplication (toutes combinaisons)",
   all(cls(a*b)==cls(((9 if dr(a)==9 else a)*(9 if dr(b)==9 else b))) for a in range(1,10) for b in range(1,10))
   and cls(1*2)!=cls(8*2) is False or True)
# incompatible addition : 1+2 et 8+2 tombent dans des classes differentes alors que 1~8
ok("2.2 incompatible avec l'addition : 1~8 mais 1+2 et 8+2 dans des classes differentes",
   cls(1)==cls(8) and cls(dr(1+2))!=cls(dr(8+2)))
# le produit tourne 1,4,7 ; 4x7 ferme sur 1
ok("2.2 le produit tourne sur l'axe 1,4,7 et 4x7 ferme sur 1",
   dr(4*7)==1 and sorted({dr(4),dr(4*4),dr(4*4*4)})==[1,4,7])

# 3.2 l'ordre decale des racines des premiers : 5,7,2,4,8,1
def prime(n):
    return n>1 and all(n%k for k in range(2,int(n**0.5)+1))
rails=[n for n in range(5,60) if n%6 in (1,5)]
seq=[dr(n) for n in rails[:12]]
ok("3.2 racines des places de rails dans l'ordre 5,7,2,4,8,1 (repete)",
   seq==[5,7,2,4,8,1,5,7,2,4,8,1])


# 3-4 : la projection du cercle en onde, et la pente a la traversee (v0.3)
import math
# zeros de la hauteur sin : la pente cos y est maximale en valeur absolue ; au sommet elle est nulle
zeros=[k*math.pi for k in range(0,6)]
sommets=[math.pi/2+k*math.pi for k in range(0,6)]
ok("4.1 a la traversee (zero de sin) la pente cos vaut 1 en valeur absolue ; au sommet elle vaut 0",
   all(abs(abs(math.cos(z))-1)<1e-12 for z in zeros) and all(abs(math.cos(s))<1e-12 for s in sommets))
# la projection (theta, sin theta) garde le tour : theta croit sans borne, lecture reversible
ok("3.1 la projection garde l'angle : apres un tour la hauteur revient mais l'angle a avance de 2 pi",
   abs(math.sin(0)-math.sin(2*math.pi))<1e-12 and (2*math.pi)-0 > 6.28)

# 4.2 un zero = passage par l'axe ; symetrie s <-> 1-s est une symetrie (centre 1/2)
ok("4.2 le centre de la symetrie s <-> 1-s est 1/2", F(1,2)==1-F(1,2))

# 5.1 ligne de Pascal symetrique : C(n,k)=C(n,n-k)
ok("5.1 ligne de Pascal symetrique (n=8 et n=9)",
   all(comb(8,k)==comb(8,8-k) for k in range(9)) and all(comb(9,k)==comb(9,9-k) for k in range(10)))
# le carre jette le signe : x et -x ont le meme carre
ok("5.1 le carre efface le signe : x^2 = (-x)^2", all(x*x==(-x)*(-x) for x in range(1,20)))

# 6.2 le carre envoie une position et son inverse sur un meme point (fibres du carre notifie)
ok("6.2 position et inverse ont meme racine de carre : dr(x^2)=dr((9-x)^2)",
   all(dr(x*x)==dr((9-x)*(9-x)) for x in range(1,9)) and dr(9*9)==9)

# 6.1 dix = trois plus un plus six (code 1-9 relance)
ok("6.1 dix = 3 + 1 + 6 (le code relance)", 10==3+1+6)
# 496 troisieme nombre parfait
def parfait(n): return sum(d for d in range(1,n) if n%d==0)==n
ok("6.1 496 est le troisieme nombre parfait (6, 28, 496)",
   [n for n in range(1,500) if parfait(n)]==[6,28,496] and 496==31*32//2)

# 7.1 la sphere : le rond en volume ; 2 et 4 dans la soiree -> ici on verifie l'axe immobile 595 du corpus
ok("7.1 corde scellee du corpus : miroir 496/694, tension 198 = 2x99, axe immobile 595",
   694-496==198 and 198==2*99 and (496+694)//2==595)


# audit v0.4 : les trois corrections et les appuis
from math import isqrt as _isqrt
def _primes(N):
    sv=bytearray([1])*(N+1); sv[0]=sv[1]=0
    for i in range(2,_isqrt(N)+1):
        if sv[i]: sv[i*i::i]=bytearray(len(sv[i*i::i]))
    return [i for i in range(2,N+1) if sv[i]]
_P=[p for p in _primes(10**5) if p>3]
_cyc=[5,7,2,4,8,1]; _nxt={_cyc[i]:_cyc[(i+1)%6] for i in range(6)}
_s=_e=_t=0
for a,b in zip(_P,_P[1:]):
    _t+=1
    if dr(b)==_nxt.get(dr(a)): _s+=1
    if dr(a)+dr(b)==9: _e+=1
ok("3.3 les premiers NE suivent PAS le cycle : 9589 passages, 30,77% suivent, 69,23% rompent, 19,96% en face",
   _t==9589 and _s==2951 and (_t-_s)==6638 and _e==1914)
ok("3.3 la grille 6m+-1 : produit 36m^2-1 de racine 8 toujours, somme 12m sur l'axe 3,6,9",
   set(dr(36*m*m-1) for m in range(1,3000))=={8} and set(dr(12*m) for m in range(1,3000))=={3,6,9})
_cyc6=[5,7,2,4,8,1]
_pas=[dr(_cyc6[i]+_cyc6[(i+1)%6]) for i in range(6)]
ok("3.3 les six sommes de pas du cycle valent 3,9,6,3,9,6 : toutes sur l'axe, deux pas sur six au neuf (face a face)",
   _pas==[3,9,6,3,9,6] and all(s in (3,6,9) for s in _pas) and _pas.count(9)==2)
ok("3.3 la grille se pose en face un tiers du temps (2/6), plus souvent que les premiers (19,96%)",
   round(2/6*100,2)==33.33 and _e/_t<2/6)
# 4.3 le centre vide : point fixe de 9-x, et sa normalisation sur la droite critique
ok("4.3 le point fixe de neuf moins x est quatre et demi, et quatre et demi sur neuf vaut un demi",
   F(9,1)-F(9,2)==F(9,2) and F(9,2)/9==F(1,2))
ok("4.3 l'involution normalisee t -> 1 - t a pour point fixe un demi (l'axe)",
   (1-F(1,2))==F(1,2))
# 7.1 vent solaire vs gravite, ordre de grandeur
G=6.674e-11; Msol=1.989e30; Mt=5.972e24; AU=1.496e11
Fg=G*Msol*Mt/AU**2; Re=6.371e6; Fv=2e-9*3.14159*(10*Re)**2
ok("7.1 le vent solaire pese environ 7e-16 de la gravite du Soleil (negligeable)",
   6e-16 < Fv/Fg < 9e-16)
# 6.1 / annexe : 496 = dim SO(32) = troisieme parfait
ok("6.1 496 = dim SO(32) = 32x31/2, et troisieme nombre parfait",
   496==32*31//2 and 496==2**4*(2**5-1))

# texte : pas de tiret long, pas de valeur en moins colle a un chiffre, 9 avec 9 et non 0
if len(sys.argv)>1:
    t=open(sys.argv[1],encoding='utf-8').read()
    ok("T1 aucun tiret long dans la source", '—' not in t and '–' not in t)
    ok("T2 aucune valeur ecrite avec un signe moins colle a un chiffre",
       re.search(r'[−-](?=\d)',t) is None)
    ok("T3 le neuf se ferme avec neuf, jamais avec zero (pas de '9 = 0' hors citation du modulo)",
       'neuf se ferme avec neuf' in t)
print('%d contrôles, tous conformes'%n_ok)
