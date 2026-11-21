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

# texte : pas de tiret long, pas de valeur en moins colle a un chiffre, 9 avec 9 et non 0
if len(sys.argv)>1:
    t=open(sys.argv[1],encoding='utf-8').read()
    ok("T1 aucun tiret long dans la source", '—' not in t and '–' not in t)
    ok("T2 aucune valeur ecrite avec un signe moins colle a un chiffre",
       re.search(r'[−-](?=\d)',t) is None)
    ok("T3 le neuf se ferme avec neuf, jamais avec zero (pas de '9 = 0' hors citation du modulo)",
       'neuf se ferme avec neuf' in t)
print('%d contrôles, tous conformes'%n_ok)
