# -*- coding: utf-8 -*-
# Ce que Riemann cherchait, v0.3 : controles executes.
# Usage : python3 riemann_cherchait_verif.py [source.md] [--long]
#   --long ajoute les comptes a 10^13 et 10^14 (environ neuf minutes).
import sys, re, math
from math import isqrt, prod
from fractions import Fraction as F
import numpy as np
LONG='--long' in sys.argv; SRC=[a for a in sys.argv[1:] if not a.startswith('--')]
n_ok=0
def ok(nom,cond):
    global n_ok
    assert cond, 'ECHEC : '+nom
    n_ok+=1; print('[OK] '+nom)
dr=lambda n:1+(n-1)%9

# ---------- crible, pour les controles directs
def crible(N):
    s=np.ones(N+1,dtype=bool); s[:2]=False
    for i in range(2,isqrt(N)+1):
        if s[i]: s[i*i::i]=False
    return s
N8=10**8; S=crible(N8); PR=np.nonzero(S)[0]

# ---------- 1. l'escalier
ok("V1 l'escalier : 25 premiers jusqu'a 100, 78 498 jusqu'a un million, 5 761 455 jusqu'a cent millions",
   int(S[:101].sum())==25 and int(S[:10**6+1].sum())==78498 and len(PR)==5761455)

# ---------- 2. le monde de 6
g=PR[PR>3]
ok("V2 tout premier apres 3 est au bord d'un multiple de 6 (verifie jusqu'a cent millions)", bool(np.all((g%6==1)|(g%6==5))))
rac=1+(g-1)%9; cnt={r:int((rac==r).sum()) for r in range(1,10)}
ok("V3 six racines, jamais trois : 959 959, 960 340, 960 360, 960 278, 960 198, 960 318 premiers de racine 1, 2, 4, 5, 7, 8 ; aucun de racine 3, 6 ou 9",
   [cnt[r] for r in (1,2,4,5,7,8)]==[959959,960340,960360,960278,960198,960318] and cnt[3]==cnt[6]==cnt[9]==0)
off=(0,2,6,8,12,14)
ok("V4 six places de suite sur la grille ont toujours les racines 5, 7, 2, 4, 8, 1 (cent mille groupes)",
   all(tuple(dr(18*m+5+o) for o in off)==(5,7,2,4,8,1) for m in range(100000)))
N7=10**7; occ=np.zeros(7,dtype=np.int64); m=np.arange(0,(N7-19)//18+1,dtype=np.int64)
tot=sum(S[18*m+5+o].astype(np.int64) for o in off)
for k in range(7): occ[k]=int((tot==k).sum())
ok("V5 groupes de six places jusqu'a dix millions : 555 555 groupes ; places libres 0 a 6 : 135 821, 228 029, 144 457, 41 619, 5 369, 259, 1 ; un seul groupe complet, le premier",
   len(m)==555555 and list(occ)==[135821,228029,144457,41619,5369,259,1] and tot[0]==6)
ok("V6 dans chaque groupe apres le premier, le 5 reprend au moins une place (deux cent mille groupes)",
   all(any((18*k+5+o)%5==0 for o in off) for k in range(1,200000)))
ok("V7 la paire (6k - 1, 6k + 1) : racines (5, 7), (2, 4), (8, 1) en cycle ; somme de racine 3, 6, 9 ; produit de racine 8 (k de 1 a 100 000)",
   all((dr(6*k-1),dr(6*k+1))==((5,7),(2,4),(8,1))[(k-1)%3] and dr(12*k)==(3,6,9)[(k-1)%3] and dr(36*k*k-1)==8 for k in range(1,100001)))

# ---------- 3. l'activite des nouveaux
def plus_petit_multiple_neuf(p,petits):
    q=p
    while True:
        if q%6 in (1,5) and all(q%r for r in petits): return p*q
        q+=1
P1000=[int(x) for x in PR[(PR>3)&(PR<1000)]]
ok("V8 chaque nouveau commence a son carre : la premiere place qu'il prend et qu'aucun plus petit n'avait prise est p x p (premiers de 5 a 997)",
   all(plus_petit_multiple_neuf(p,[r for r in P1000 if r<p])==p*p for p in P1000))
ok("V9 ce carre est toujours sur le rail du 7, de racine 1, 4 ou 7, et vaut 24 fois un entier plus 1 (premiers de 5 a 997)",
   all((p*p)%6==1 and dr(p*p) in (1,4,7) and (p*p-1)%24==0 for p in P1000))
gr=[n for n in range(5,2000) if n%6 in (1,5)]
ok("V10 l'echange : rail du 5 fois rail du 5 tombe sur le rail du 7 ; rail du 5 fois rail du 7 sur le rail du 5 ; rail du 7 fois rail du 7 sur le rail du 7 (toutes les paires de places sous 2 000)",
   all((a*b)%6==(1 if a%6==b%6 else 5) for a in gr for b in gr))
# l'exemple a la main, jusqu'a 100
r5=[n for n in range(5,101) if n%6==5]; r7=[n for n in range(7,101) if n%6==1]
pris5=sorted(n for n in r5+r7 if n%5==0 and n>5); pris7=sorted(n for n in r5+r7 if n%7==0 and n>7 and n%5)
libres5=[n for n in r5 if n not in pris5+pris7]; libres7=[n for n in r7 if n not in pris5+pris7]
ok("V11 jusqu'a 100 : 16 places par rail ; le 5 prend 25, 35, 55, 65, 85, 95 ; le 7 prend 49, 77, 91 ; restent 12 premiers sur le rail du 5 et 11 sur le rail du 7 ; avec 2 et 3, 25",
   len(r5)==16 and len(r7)==16 and pris5==[25,35,55,65,85,95] and pris7==[49,77,91] and len(libres5)==12 and len(libres7)==11
   and all(S[n] for n in libres5+libres7) and len(libres5)+len(libres7)+2==25)
ok("V12 l'echelle du dessous : le 5 prend jusqu'a 100 autant de places qu'il y a de places de 5 a 20 (six) ; le 7 autant qu'il y a de places sans 5 de 7 a 14 (trois)",
   len(pris5)==len([n for n in range(5,21) if n%6 in (1,5)])==6 and len(pris7)==len([n for n in range(7,15) if n%6 in (1,5) and n%5])==3)

# ---------- 4. le compte sans visiter les places
def compte(N):
    r=isqrt(N)
    s=np.arange(0,r+1,dtype=np.int64); L=N//np.arange(1,r+1,dtype=np.int64)
    s1=np.maximum((s-1)//6,0); s5=(s+1)//6
    L1=np.concatenate(([0],(L-1)//6)); L5=np.concatenate(([0],(L+1)//6))
    gens=0
    for p in range(5,r+1):
        mm=p%6
        if mm not in (1,5): continue
        if (s1[p]-s1[p-1] if mm==1 else s5[p]-s5[p-1])==0: continue
        gens+=1; a1,a5=s1[p-1],s5[p-1]; k=min(r,N//(p*p))
        if k>=1:
            i=np.arange(1,k+1,dtype=np.int64); d=i*p; inL=d<=r
            q1=np.where(inL,L1[np.minimum(d,r)],s1[np.where(inL,0,N//d)])
            q5=np.where(inL,L5[np.minimum(d,r)],s5[np.where(inL,0,N//d)])
            if mm==1: L1[1:k+1]-=q1-a1; L5[1:k+1]-=q5-a5
            else:     L1[1:k+1]-=q5-a5; L5[1:k+1]-=q1-a1
        if p*p<=r:
            w=np.arange(p*p,r+1,dtype=np.int64)//p; q1=s1[w].copy(); q5=s5[w].copy()
            if mm==1: s1[p*p:]-=q1-a1; s5[p*p:]-=q5-a5
            else:     s1[p*p:]-=q5-a5; s5[p*p:]-=q1-a1
    return int(L5[1]),int(L1[1]),gens
C={e:compte(10**e) for e in (3,8,10,11,12)}
ok("V13 le compte par la regle retrouve le compte direct jusqu'a cent millions : 2 880 936 sur le rail du 5, 2 880 517 sur le rail du 7",
   C[8][:2]==(int((g%6==5).sum()),int((g%6==1).sum()))==(2880936,2880517) and C[3][:2]==(86,80))
connu={10:455052511,11:4118054813,12:37607912018,13:346065536839,14:3204941750802}
ok("V14 a 10^10, 10^11 et 10^12 la regle donne 455 052 511, 4 118 054 813 et 37 607 912 018 premiers, les valeurs recues, avec 9 590, 27 291 et 78 496 nouveaux",
   all(C[e][0]+C[e][1]+2==connu[e] for e in (10,11,12)) and [C[e][2] for e in (10,11,12)]==[9590,27291,78496])
ok("V15 a 10^12 : 18 803 978 496 sur le rail du 5 et 18 803 933 520 sur le rail du 7", C[12][:2]==(18803978496,18803933520))
if LONG:
    C[13]=compte(10**13); C[14]=compte(10**14)
    ok("V16 a 10^13 : 173 032 844 824 et 173 032 692 013, total 346 065 536 839 ; 227 645 nouveaux",
       C[13]==(173032844824,173032692013,227645) and sum(C[13][:2])+2==connu[13])
    ok("V17 a 10^14 : 1 602 471 005 226 et 1 602 470 745 574, total 3 204 941 750 802 ; 664 577 nouveaux",
       C[14]==(1602471005226,1602470745574,664577) and sum(C[14][:2])+2==connu[14])

# ---------- 5. la courbe mesuree contre le compte
EG=0.57721566490153286
def li(x):
    Lx=math.log(x); s=0.0; t=1.0
    for k in range(1,400):
        t*=Lx/k; s+=t/k
        if t/k<1e-18*abs(s): break
    return EG+math.log(Lx)+s
aire=lambda x: li(x)-li(2)
trou={e:aire(10**e)-connu.get(e,5761455) for e in (8,10,12,13,14)}
att={8:753,10:3103,12:38262,13:108970,14:314889}
ok("V18 la courbe de Gauss (aire a partir de 2) est au-dessus du compte de 753 a 10^8, 3 103 a 10^10, 38 262 a 10^12, 108 970 a 10^13 et 314 889 a 10^14 (a une unite pres)",
   all(abs(trou[e]-att[e])<=1.0 for e in att))
ok("V19 la courbe annonce 30 premiers jusqu'a 100, ou il y en a 25", round(li(100))==30)

# ---------- 6. la jonction et l'axe
def tour(G):
    M=prod(G); R=prod(g_-1 for g_ in G)            # part libre = R/M
    Cc=0; hi=None; lo=None
    for k in range(1,M+1):
        a=6*k-1; b=6*k+1
        Cc+=any(a%g_==0 for g_ in G)+any(b%g_==0 for g_ in G)
        E=Cc*M-2*(M-R)*k                             # ecart au terme ferme, multiplie par M
        if hi is None or E>hi[0]: hi=(E,k)
        if lo is None or E<lo[0]: lo=(E,k)
    axe=F(M-R,M)
    return M,E,axe,F(hi[0],M)-axe,axe-F(lo[0],M),hi[1],lo[1]
T={tuple(G):tour(G) for G in ([5,7],[5,7,11],[5,7,11,13],[5,7,11,13,17,19])}
ok("V20 a chaque jonction complete (35, 385, 5 005, 1 616 615 positions), le compte est exactement sur son terme ferme", all(t[1]==0 for t in T.values()))
ok("V21 entre deux jonctions, le compte s'ecarte de son axe d'autant vers le haut que vers le bas, en fractions exactes ; l'axe est la part des places prises : 11/35, 29/77, 425/1001, puis 0,487 pour six nouveaux",
   all(t[3]==t[4] for t in T.values()) and [t[2] for t in T.values()][:3]==[F(11,35),F(29,77),F(425,1001)] and round(float(T[(5,7,11,13,17,19)][2]),3)==0.487)
ok("V22 la distance a l'axe vaut 1,057, 1,935, 3,164 et 8,317 pour deux, trois, quatre et six nouveaux",
   [round(float(t[3]),3) for t in T.values()]==[1.057,1.935,3.164,8.317])
T5=tour([5,7,11,13,17])
TT=dict(T); TT[(5,7,11,13,17)]=T5
ok("V23 (recrit en version 0.4) a tous les etages comptes, de deux a six nouveaux, les positions des deux extremes font ensemble le tour moins un ; sur le tour de 35 : 16 et 18 pour trois, quatre et six nouveaux, 1 et 33 pour deux et cinq ; milieu 17",
   all(t[5]+t[6]==t[0]-1 for t in TT.values())
   and all(sorted((t[5]%35,t[6]%35))==([16,18] if len(G) in (3,4,6) else [1,33]) for G,t in TT.items()) and (16+18)//2==17==(1+33)//2)
ok("V33 cinq nouveaux : jonction 85 085, axe 7801/17017, distance 5,028 de chaque cote, extremes aux rangs 42 386 et 42 698",
   T5[0]==85085 and T5[1]==0 and T5[2]==F(7801,17017) and T5[3]==T5[4] and round(float(T5[3]),3)==5.028 and sorted((T5[5],T5[6]))==[42386,42698])
ok("V34 rangs des extremes sur le tour entier : 1 et 33 sur 35 ; 18 et 366 sur 385 ; 1 838 et 3 166 sur 5 005 ; 666 031 et 950 583 sur 1 616 615",
   [sorted((t[5],t[6])) for t in T.values()]==[[1,33],[18,366],[1838,3166],[666031,950583]])

# etage de sept nouveaux (version 0.5) : compte vectoriel
import numpy as _np
_G=[5,7,11,13,17,19,23]; _M=prod(_G); _R=prod(g_-1 for g_ in _G)
_k=_np.arange(1,_M+1,dtype=_np.int64); _a=_np.zeros(_M,dtype=bool); _b=_np.zeros(_M,dtype=bool)
for g_ in _G:
    _a|=((6*_k-1)%g_==0); _b|=((6*_k+1)%g_==0)
_E=_np.cumsum(_a.astype(_np.int64)+_b.astype(_np.int64))*_M-2*(_M-_R)*_k
_i=int(_E.argmax())+1; _j=int(_E.argmin())+1; _axe=F(_M-_R,_M)
ok("V35 sept nouveaux : tour 37 182 145, axe 344263/676039 (au-dessus de la moitie), extremes aux rangs 15 705 670 et 21 476 474, distance 13,764 de chaque cote, somme = tour moins un, positions 15 et 19 sur 35 ; 94 234 019 pris par 11, 94 234 021 par 7, 94 234 025 par 5, 94 234 027 libre",
   _M==37182145 and _axe==F(344263,676039) and _axe>F(1,2) and (_i,_j)==(15705670,21476474) and _i+_j==_M-1 and (_i%35,_j%35)==(15,19)
   and round(float(F(int(_E[_i-1]),_M)-_axe),3)==13.764==round(float(_axe-F(int(_E[_j-1]),_M)),3) and int(_E[-1])==0
   and 94234019%11==0 and 94234021%7==0 and 94234025%5==0 and all(94234027%g_ for g_ in _G))
del _k,_a,_b,_E
def miroir(G):
    M=prod(G); t=[0]*(M+1)
    for k in range(1,M+1): t[k]=any((6*k-1)%g_==0 for g_ in G)+any((6*k+1)%g_==0 for g_ in G)
    if t[M]!=0 or any(t[k]!=t[M-k] for k in range(1,M)): return False
    C=[0]*(M+1)
    for k in range(1,M+1): C[k]=C[k-1]+t[k]
    T=C[M]
    return all((C[k]*M-T*k)+(C[M-1-k]*M-T*(M-1-k))==T for k in range(1,M-1))
ok("V36 le miroir par retournement : le rang k et le rang M - k portent le meme nombre de places prises, le rang M aucune, et l'ecart au rang M - 1 - k est l'oppose de l'ecart au rang k par rapport a l'axe, a tous les rangs, pour deux, trois, quatre et cinq nouveaux",
   all(miroir(G) for G in ([5,7],[5,7,11],[5,7,11,13],[5,7,11,13,17])))

# ---------- 7. les huit triangles
x=math.pi/4; c4=1-x**2/2+x**4/24-x**6/720
ok("V24 au huitieme de tour, quatre termes de la somme d'Euler donnent 0,707103 pour 0,707107 ; par la figure les deux carres valent 1/2 chacun, et huit triangles font le carre inscrit, d'aire 2",
   round(c4,6)==0.707103 and round(math.sqrt(2)/2,6)==0.707107 and F(1,2)+F(1,2)==1 and 8*F(1,2)*F(1,2)==2)

# ---------- 8. le texte
if SRC:
    txt=open(SRC[0],encoding='utf-8').read()
    ok("V25 typographie : aucun tiret long dans la source", '—' not in txt and '–' not in txt)
    ok("V26 aucune valeur ecrite avec un signe moins colle a un chiffre", re.search(r'[−](?=\d)',txt) is None and re.search(r'(?<![\w)])-(?=\d)',txt) is None)
ok("V27 le dernier nouveau entre : 9 973 jusqu'a cent millions (son carre 99 460 729 tient, celui de 10 007 non) ; 9 999 991 jusqu'a 10^14",
   int(PR[PR<=10**4][-1])==9973 and 9973**2==99460729<=10**8<10007**2 and bool(S[10007]) and int(PR[PR<=10**7][-1])==9999991 and 9999991**2<=10**14 and not S[9999992:10**7+1].any())

# ---------- 9. le partage entre les rails (v0.3)
av={e:C[e][0]-C[e][1] for e in C}
ok("V28 l'avance du rail du 5 : 419 a 10^8, 6 263 a 10^10, 44 976 a 10^12, chaque fois sous le nombre des nouveaux (1 227, 9 590, 78 496) ; 14 premiers sur un million a 10^10",
   [av[e] for e in (8,10,12)]==[419,6263,44976] and [C[e][2] for e in (8,10,12)]==[1227,9590,78496] and all(av[e]<C[e][2] for e in (8,10,12))
   and round(10**6*av[10]/(C[10][0]+C[10][1]))==14)
if LONG:
    ok("V29 l'avance a 10^13 et 10^14 : 152 811 et 259 652, sous 227 645 et 664 577 nouveaux ; 8 premiers sur cent millions a 10^14",
       [av[e] for e in (13,14)]==[152811,259652] and all(av[e]<C[e][2] for e in (13,14)) and round(10**8*av[14]/(C[14][0]+C[14][1]))==8)
    ok("V30 le relais : a 608 981 813 029 la regle compte 11 669 295 394 premiers sur le rail du 5 et 11 669 295 396 sur le rail du 7",
       compte(608981813029)[:2]==(11669295394,11669295396) and av[12]>0)
nv=[int(p) for p in PR[(PR>3)&(PR<=10**4)]]
ok("V31 jusqu'a cent millions, les 1 227 carres des nouveaux sont tous sur le rail du 7, aucun sur le rail du 5",
   len(nv)==1227 and all((p*p)%6==1 and p*p<=10**8 for p in nv))
from math import comb
l8=[comb(8,k) for k in range(9)]; l9=[comb(9,k) for k in range(10)]
pli=lambda r:[r[k-1]+r[k+1]-2*r[k] for k in range(1,len(r)-1)]
ok("V32 la crete : ligne 8 = 1, 8, 28, 56, 70, 56, 28, 8, 1 (total 256), pli 13 et 8 vers le haut puis 14, 28, 14 vers le bas, le plus fort au sommet ; ligne 9 : deux 126 face a face (total 512), centre a 4,5, pli 42 de chaque cote",
   l8==[1,8,28,56,70,56,28,8,1] and sum(l8)==256 and pli(l8)==[13,8,-14,-28,-14,8,13] and l9[4]==l9[5]==126 and sum(l9)==512
   and F(4+5,2)==F(9,2) and pli(l9)[3:5]==[-42,-42] and max(abs(x) for x in pli(l9))==42 and max(abs(x) for x in pli(l8))==28)
print('%d contrôles, tous conformes'%n_ok)
