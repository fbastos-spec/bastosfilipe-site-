# -*- coding: utf-8 -*-
# Ce que Riemann cherchait, v0.2 : controles executes.
# Usage : python3 riemann_cherchait_verif.py [source.md] [--long]
#   --long ajoute les comptes a 10^13 et 10^14 (environ sept minutes).
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
ok("V23 pour trois, quatre et six nouveaux, les deux extremes tombent aux positions 16 et 18 du tour de 35, de part et d'autre de 17,5, et leurs deux positions font ensemble le tour moins un",
   all((t[5]%35,t[6]%35)==(16,18) and t[5]+t[6]==t[0]-1 for G,t in T.items() if len(G)>=3))

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
print('%d contrôles, tous conformes'%n_ok)
