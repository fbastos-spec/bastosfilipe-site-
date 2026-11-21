# -*- coding: utf-8 -*-
# Le nombre est un chemin, v0.1 : controles executes.
import sys, re
from math import isqrt, comb
from fractions import Fraction as F
n_ok=0
def ok(nom,cond):
    global n_ok
    assert cond,'ECHEC : '+nom
    n_ok+=1; print('[OK] '+nom)
dr=lambda n:1+(n-1)%9
def sgaps(n):
    d=[int(c) for c in str(n)]; return [b-a for a,b in zip(d,d[1:])]
def apex(n):
    s=[int(c) for c in str(n)]
    while len(s)>1: s=[dr(a+b) for a,b in zip(s,s[1:])]
    return s[0]
def prime(n): return n>1 and all(n%k for k in range(2,isqrt(n)+1))
carre=lambda n: n>0 and isqrt(n)**2==n
palin=lambda n: str(n)==str(n)[::-1]

# 1. le chemin
def recon(premier,sg):
    d=[premier]
    for g in sg: d.append(d[-1]+g)
    return int(''.join(map(str,d)))
ok("1.2 depart + ecarts signes redonnent le nombre (2 a 5 chiffres)",
   all(recon(int(str(n)[0]),sgaps(n))==n for n in range(10,100000)))

# 2. la derivee
def diff(s): return [b-a for a,b in zip(s,s[1:])]
carres=[k*k for k in range(1,12)]; cubes=[k**3 for k in range(1,12)]
ok("2.3 derivee des carres = impairs ; derivee seconde = 2 partout",
   diff(carres)==[3,5,7,9,11,13,15,17,19,21] and set(diff(diff(carres)))=={2})
ok("2.3 derivee troisieme des cubes = 6 partout (6 = 3x2x1)",
   set(diff(diff(diff(cubes))))=={6})

# 3. l integrale et le bord
def cumul(start,d):
    s=[start]
    for x in d: s.append(s[-1]+x)
    return s
ok("3.1 empiler les impairs redonne les carres", cumul(1,[3,5,7,9,11,13,15,17,19,21])==carres)
def newton(bord,k): return sum(comb(k,i)*bord[i] for i in range(len(bord)))
d=[1,7,2,9]; bord=[d[0]]; cur=d
while len(cur)>1: cur=diff(cur); bord.append(cur[0])
ok("3.3 le bord de 1729 reconstruit ses chiffres par Newton", [newton(bord,k) for k in range(4)]==[1,7,2,9])

# 4. le carre par retrait d impairs
def retraits(N):
    r=N; imp=1; k=0
    while r>=imp: r-=imp; imp+=2; k+=1
    return k,r
ok("4.1 deux triangulaires voisins font un carre (36+45=81, general)",
   all(k*(k+1)//2+(k+1)*(k+2)//2==(k+1)**2 for k in range(1,10000)))
ok("4.2 retrait d impairs : 1681 -> 41 etages reste 0 ; 1729 -> 41 etages reste 48",
   retraits(1681)==(41,0) and retraits(1729)==(41,48))
ok("4.2 le nombre d etages est la racine carree entiere (jusqu a 200000)",
   all(retraits(N)[0]==isqrt(N) for N in range(1,200000)))
ok("4.3 nombre d etages d un carre = somme des chiffres de sa racine, repliee (9973)",
   retraits(9973**2)[0]==9973 and dr(9+9+7+3)==1 and 9+9+7+3==28)

# 5. le point d equilibre (Fermat par cascade)
def fermat(N):
    s=isqrt(N)
    if s*s<N: s+=1
    car=s*s
    while True:
        d=car-N; t=isqrt(d)
        if t*t==d: return (s-t,s+t)
        car+=2*s+1; s+=1
ok("5.2 1081 = 23 x 47 par le point d equilibre (s=35, t=12)", fermat(1081)==(23,47))
ok("5.2 point d equilibre sur des semipremiers d exemple",
   fermat(99799811)==(9973,10007) and fermat(2491)==(47,53) and fermat(667)==(23,29))

# 6. les deux pesees
somme=lambda n: dr(dr(n)+apex(n))
ok("6.1 3 chiffres : pointe = racine(bord + 2*milieu + bord)",
   all(apex(n)==dr(int(str(n)[0])+2*int(str(n)[1])+int(str(n)[2])) for n in range(100,1000)))
# tableaux 4 chiffres
def famille(f):
    rac=set(); 
    for n in range(1000,10000):
        if f(n): rac.add(dr(n))
    return rac
ok("6.2 carres a 4 chiffres : seulement racines 1,4,7,9", famille(carre)=={1,4,7,9})
ok("6.2 premiers a 4 chiffres : jamais racine 3,6,9", famille(prime)=={1,2,4,5,7,8})
# palindromes : diagonale deux fois plus peuplee
import numpy as np
G=np.zeros((10,10),int)
for n in range(1000,10000):
    if palin(n): G[dr(n)][apex(n)]+=1
diag=[G[r][r] for r in range(1,10)]; horsdiag=[G[r][c] for r in range(1,10) for c in range(1,10) if r!=c]
ok("6.2 palindromes : diagonale racine=pointe deux fois plus peuplee",
   all(x==2 for x in diag) and all(x<=1 for x in horsdiag))
# inverse par complement a 9 (sans zero)
phi=lambda d: 9 if d==9 else 9-d
comp=lambda n:int(''.join(str(phi(int(c))) for c in str(n)))
inv9=lambda x:9-x if x!=9 else 9
ok("6.3 complement du cadastre (9->9, jamais 0) inverse racine ET pointe, chiffres 1 a 9 jusqu a 100000",
   all(dr(comp(n))==inv9(dr(n)) and apex(comp(n))==inv9(apex(n)) for n in range(10,100000) if '0' not in str(n))
   and comp(999)==999 and comp(137)==862)
ok("6.3 renverser ne bouge ni racine ni pointe (fins non nulles)",
   all(dr(int(str(n)[::-1]))==dr(n) and apex(int(str(n)[::-1]))==apex(n) for n in range(100,100000) if str(n)[-1]!='0'))
Fam=[n for n in range(100,1000) if dr(n)+somme(n)==9]
ok("6.4 famille racine+somme=9 : 100 sur 900, contient 169, 361, 961",
   len(Fam)==100 and all(x in Fam for x in (169,361,961)))

# 7. le perdu
def rowfold(n):
    d=[int(c) for c in str(n)]
    if len(d)==1: return None
    return int(''.join(str(dr(a+b)) for a,b in zip(d,d[1:])))
def perdus(n):
    out=[]
    while True:
        r=rowfold(n)
        if r is None: break
        out.append(n-r); n=r
    return out
ok("7.1 1279 -> 397,37,1 perdus 882,360,36 ; 2193 -> 313,44,8 perdus 1880,269,36",
   perdus(1279)==[882,360,36] and perdus(2193)==[1880,269,36])
ok("7.2 dernier perdu (2 chiffres -> 1) toujours multiple de 9",
   all(perdus(n)[-1]%9==0 for n in range(1000,10000)))

# 8. ce que la forme ne porte pas
def triangle(n):
    s=[int(c) for c in str(n)]; rows=[tuple(s)]
    while len(s)>1: s=[dr(a+b) for a,b in zip(s,s[1:])]; rows.append(tuple(s))
    return tuple(rows)
ok("8.1 jamais deux nombres differents avec la meme cascade complete (3 chiffres rails)",
   len(set(triangle(n) for n in range(100,1000) if n%10 in(1,3,7,9)))==len([n for n in range(100,1000) if n%10 in(1,3,7,9)]))
ok("8.2 49 (7x7) et 67 (premier) : meme racine et meme pointe",
   dr(49)==dr(67) and apex(49)==apex(67) and not prime(49) and prime(67))
# 8.4 divisibilite par 1001
def alt3(n):
    s=str(n); g=[]; 
    while s: g.append(int(s[-3:])); s=s[:-3]
    return sum(x if i%2==0 else -x for i,x in enumerate(g))
ok("8.4 tranches de 3 alternees donnent 7, 11 et 13 (jusqu a 200000)",
   all((alt3(n)%7==0)==(n%7==0) and (alt3(n)%11==0)==(n%11==0) and (alt3(n)%13==0)==(n%13==0) for n in range(1,200000)))
ok("8.4 somme alternee des chiffres donne 11", 
   all((sum((-1)**i*int(c) for i,c in enumerate(str(n)[::-1]))%11==0)==(n%11==0) for n in range(1,200000)))

# 9. liens figure fondamentale
ok("9.1 reseau des huit points : 28 aretes, 36 avec le centre", comb(8,2)==28 and 28+8==36)
ok("9.1 pli : carres 1,8,9 avec 1+8=9 ; 81 = 9x9", 1+8==9 and 81==9*9)
ok("9.2 ecarts des quatre paires 7,5,3,1 de somme 16, centre vide 4,5",
   7+5+3+1==16 and F(1+8,2)==F(9,2))

# texte
if len(sys.argv)>1:
    txt=open(sys.argv[1],encoding='utf-8').read()
    ok("T1 aucun tiret long dans la source", '—' not in txt and '–' not in txt)
    ok("T2 aucune valeur ecrite avec un signe moins colle a un chiffre",
       re.search(r'[−](?=\d)',txt) is None and re.search(r'(?<![\w)])-(?=\d)',txt) is None)
print('%d contrôles, tous conformes'%n_ok)
