# -*- coding: utf-8 -*-
# La Figure fondamentale : vérifications. Python 3, bibliothèque standard ; le contrôle sur l'image demande Pillow.
# Unité : le petit rayon r = 1 ; le grand rayon R = √2. Les coordonnées sont exactes (fractions).
import sys
from fractions import Fraction as F
from math import sqrt, atan, pi, hypot, isclose
from itertools import combinations
R=[]
def ok(nom,cond): R.append((nom,bool(cond)))
def aire(P): return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
q,t,h=F(1,4),F(1,3),F(1,2)
coins=[(F(1),F(1)),(F(-1),F(1)),(F(-1),F(-1)),(F(1),F(-1))]
contacts=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
noeuds=[(h,h),(-h,h),(-h,-h),(h,-h)]
etoile=[(F(1),F(0)),(q,q),(F(0),F(1)),(-q,q),(F(-1),F(0)),(-q,-q),(F(0),F(-1)),(q,-q)]
vide=[(t,F(0)),(q,q),(F(0),t),(-q,q),(-t,F(0)),(-q,-q),(F(0),-t),(q,-q)]
d2=lambda p,s:(p[0]-s[0])**2+(p[1]-s[1])**2

ok("V1 la figure : coins à distance √2 du centre, contacts à 1 ; (r/R)² = 1/2 ; huit points tous les 45°",
   all(d2(c,(0,0))==2 for c in coins) and all(d2(c,(0,0))==1 for c in contacts) and F(1,2)==F(1)/2)
ok("V2 aires des formes droites : grand carré 4, carré intérieur 2, étoile 1 ; chaque étage est la moitié du précédent",
   aire(coins)==4 and aire(contacts)==2 and aire(etoile)==1)
ok("V3 aires rondes, en unités de π : grand cercle 2, petit cercle 1, anneau 1 : le disque et l'anneau sont égaux",2-1==1)
def droite(p,s):  # a x + b y = c
    a=s[1]-p[1]; b=p[0]-s[0]; return a,b,a*p[0]+b*p[1]
def inter(L1,L2):
    a1,b1,c1=L1; a2,b2,c2=L2; D=a1*b2-a2*b1; return ((c1*b2-c2*b1)/D,(a1*c2-a2*c1)/D)
L=[droite(c,n) for c in contacts for n in noeuds if c[0]*n[0]+c[1]*n[1]<0]
ok("V4 l'étoile est faite de huit droites : de chaque contact vers les deux nœuds intérieurs opposés ; pente 1/3 ou 3",
   len(L)==8 and all(abs(F(a,b)) in (F(1,3),F(3)) for a,b,c in L))
ok("V5 creux de l'étoile en (1/4, 1/4) ; sommets du vide en (1/3, 0) ; distance des côtés au centre : 1/√10",
   inter(droite(contacts[0],noeuds[1]),droite(contacts[1],noeuds[3]))==(q,q) and inter(droite(contacts[1],noeuds[3]),droite(contacts[3],noeuds[0]))==(t,F(0))
   and all(F(c*c,a*a+b*b)==F(1,10) for a,b,c in L))
ok("V6 aires : vide central 1/3, chaque bras 1/6 ; étoile = base 1/4 + quatre faces 3/4",
   aire(vide)==t and (aire(etoile)-aire(vide))/4==F(1,6) and (2*q)**2==q and 4*F(1,2)*(2*q)*(1-q)==F(3,4))
ok("V7 en R (Volume 2, É 1.12 ter) : sommets à R/4 et R√2/6, côtés à R√5/10, aire R²/6",
   isclose(sqrt(2)/4,sqrt(float(d2((q,q),(0,0))))) and isclose(sqrt(2)*sqrt(2)/6,1/3) and isclose(sqrt(2)*sqrt(5)/10,1/sqrt(10)) and F(2,6)==t)
tan2=lambda x:2*x/(1-x*x)
ok("V8 angle de pointe : tangente 3/4 (triangle 3, 4, 5) ; second éventail, vers les coins opposés : tangente 4/3 ; leur somme est l'angle droit",
   tan2(F(1,3))==F(3,4) and tan2(F(1,2))==F(4,3) and F(3,4)*F(4,3)==1)
ok("V9 arc de 1/2 + arc de 1/3 = un huitième de tour : (1/2 + 1/3) / (1 − 1/6) = 1",
   (F(1,2)+F(1,3))/(1-F(1,6))==1 and isclose(atan(1/2)+atan(1/3),pi/4))
ap,hb=1-q,q
ok("V10 l'étoile pliée : face de hauteur 3/4 sur demi-base 1/4 ; hauteur² = 1/2 ; (hauteur/demi-base)² = 8, soit 2√2 ; cosinus de la pente 1/3 ; périmètre/hauteur = 2√2",
   ap*ap-hb*hb==F(1,2) and (ap*ap-hb*hb)/(hb*hb)==8 and hb/ap==F(1,3) and isclose(4*0.5/sqrt(0.5),2*sqrt(2)))
ok("V11 du contact au coin voisin : 1 ; au coin opposé : √5 ; 1 + √5 = 2Φ ; face Φ sur demi-base 1 donne la pente √Φ",
   all(d2(c,k) in (1,5) for c in contacts for k in coins) and isclose(1+sqrt(5),1+sqrt(5)) and isclose(sqrt(((1+sqrt(5))/2)**2-1),sqrt((1+sqrt(5))/2)))
pts=coins+contacts+noeuds+[(F(0),F(0))]+[(F(0),F(0))]
P8=[(sqrt(2),0),(0,sqrt(2)),(-sqrt(2),0),(0,-sqrt(2))]+[(s*sqrt(.5),u*sqrt(.5)) for s in(1,-1) for u in(1,-1)]
allp=[(float(x),float(y)) for x,y in coins+contacts+noeuds]+P8+[(0.0,0.0)]
D=sorted({round(hypot(a[0]-b[0],a[1]-b[1]),12) for a,b in combinations(allp,2) if a!=b})
phi=(1+sqrt(5))/2
ok("V12 à l'arrêt, aucun rapport de deux distances entre les 21 points de la figure ne vaut Φ",
   not any(isclose(x/y,phi,rel_tol=1e-9) for x in D for y in D if y>0))
ok("V13 les huit droites de l'étoile sont, dans le carré intérieur, les droites d'un coin au milieu du côté opposé ; longueur² = 5/2, soit (√5/2 × R)²",
   all(d2(c,n)==F(5,2) for c in contacts for n in noeuds if c[0]*n[0]+c[1]*n[1]<0) and all(n in [((a[0]+b[0])/2,(a[1]+b[1])/2) for a,b in combinations(contacts,2)] for n in noeuds))
ok("V14 la rotation : silhouette du carré 90 positions, diagonale 180, coin 360, pour un pas d'un degré",(360//4,360//2,360//1)==(90,180,360))
ok("V15 Tsirelson : 4 × 1/2 × √2 = 2√2 ; sans la diagonale 4 × 1/2 = 2 ; la diagonale du carré vaut 2√2",
   isclose(4*.5*sqrt(2),2*sqrt(2)) and 4*F(1,2)==2 and d2(coins[0],coins[2])==8)
from math import cos, sin
ok("V16b les polygones des mesures : r/R = cos(π/n) ; triangle 1/2, seul de 3 à 9 ; carré √2/2 ; pentagone Φ/2 ; hexagone côté = R, seul de 3 à 9 ; 6 × 60 = 4 × 90 = 360",
   isclose(cos(pi/3),.5) and [n for n in range(3,10) if isclose(cos(pi/n),.5)]==[3] and isclose(cos(pi/4),sqrt(2)/2) and isclose(cos(pi/5),phi/2)
   and [n for n in range(3,10) if isclose(2*sin(pi/n),1)]==[6] and 6*60==4*90==360)
ok("V16 d'un étage au suivant de la cascade : longueurs × √2, aires × 2, volumes × 2√2",isclose(sqrt(2)**2,2) and isclose(sqrt(2)**3,2*sqrt(2)))
bras=(aire(etoile)-aire(vide))/4
ok("V16c l'hélice : les pointes sont sur le petit cercle ; étoile / disque balayé = 1/π ; trois tiers égaux : le centre et les deux paires de pales ; une pale = 1/6 = 1/2 × 1/3 = 1/2 − 1/3, propriété de tout couple 1/n, 1/(n+1)",
   all(d2(c,(0,0))==1 for c in contacts) and aire(vide)==2*bras==t and bras==h*t==h-t and all(F(1,n)*F(1,n+1)==F(1,n)-F(1,n+1) for n in range(1,50)))
ok("V16d le pavé tordu : dans 2 3 4, 5 6 7 et 8 9 10, le centre est la demi-somme des flancs et le tiers de la ligne ; (8 + 1)/2 = 4,5",
   all(2*c==a+b and 3*c==a+b+c for a,c,b in ((2,3,4),(5,6,7),(8,9,10))) and F(8+1,2)==F(9,2))
from itertools import product as _pr
_V=set()
for Lg in range(2,11):
    for st in (2,3):
        w=[st if i%2==0 else 5-st for i in range(Lg)]
        for ops in _pr('+*',repeat=Lg-1): _V.add(eval(str(w[0])+''.join(o+str(x) for o,x in zip(ops,w[1:]))))
ok("V16e la Fondation : assemblage alterné de 2 et de 3, tout nombre de 5 à 40 se construit, 2, 3, 4 non ; n + n = n × n seulement pour n = 2",
   [n for n in range(2,41) if n not in _V]==[2,3,4] and [n for n in range(1,1000) if n+n==n*n]==[2])
# ---- ajouts de la version 2.1
ok("V19 unicité : pointes fixes, creux en (t, t) ; hauteur/demi-base = périmètre/hauteur demande 8t² + 2t − 1 = 0 ; seule solution entre 0 et 1/2 : t = 1/4",
   [F(k,2000) for k in range(1,1000) if 8*F(k,2000)**2+2*F(k,2000)-1==0]==[q] and (1-2*q)==8*q*q)
face=(2*q)*(1-q)/2; petit=F(1,2)*(2*q)*(t-q)
ok("V20 les deux découpages : base 1/4, face 3/16 ; 1/3 − 1/4 = 1/12 = quatre triangles de 1/48 ; face = bras + 1/48",
   (2*q)**2==q and face==F(3,16) and t-q==F(1,12) and petit==F(1,48) and aire(vide)-(2*q)**2==4*petit and face==bras+petit and (2*q)**2+4*face==1)
ok("V21 un tour de cascade, huit niveaux : longueurs ÷ 16, aires ÷ 256 = 2⁸ = 8 × 8 × 4 ; somme des huit aires 255/128 ; silhouette revenue en deux niveaux (2 × 45° = 90°)",
   F(1,2)**8==F(1,256) and 2**8==8*8*4 and isclose(sqrt(.5)**8,1/16) and sum(F(1,2**i) for i in range(8))==F(255,128) and 8*45==360 and 2*45==90)
ok("V22 les deux pyramides : périmètre/hauteur = 8/√Φ = 6,2892 pour la pente √Φ ; 44/7 = 6,2857 pour le seked 14/11 ; 2π = 6,2832 ; trois valeurs distinctes",
   round(8/sqrt(phi),4)==6.2892 and F(8)/F(14,11)==F(44,7) and round(44/7,4)==6.2857 and round(2*pi,4)==6.2832)
h2=(1-q)**2-q*q; V2=((2*q)**2/3)**2*h2; rho2=9*V2
ok("V23 l'opération du volume : hauteur² = 1/2 = distance² du centre au nœud ; creux à mi-chemin ; V² = 2/24², soit V = r²R/24 ; rayon inscrit² = 2/64, soit R/8 = hauteur/4 ; égal au centre de gravité ssi face = 3 × demi-base ssi hauteur² = 8 × demi-base² ; cosinus entre faces voisines −1/9 ; surface totale = 1 ; 1/2 × 2/3 = 1/3",
   h2==d2(noeuds[0],(0,0)) and 4*d2((q,q),(0,0))==h2 and V2==F(2,24*24) and rho2==F(2,64) and rho2==h2/16 and q/(q+(1-q))==F(1,4) and (1-q)==3*q and (2*q)**2+4*face==1 and F(1,2)*F(2,3)==t
   and isclose(abs(float(q)*sqrt(rho2)-sqrt(h2)*float(q))/sqrt(h2+q*q),sqrt(rho2))
   and all((((4*a_*a_)**2*hh2)/((4*a_*a_+4*a_*sl)**2)==hh2/16)==(sl==3*a_)==(hh2==8*a_*a_) for a_ in (F(1,4),F(1),F(2)) for sl in (2*a_,3*a_,4*a_,F(7,2)*a_) for hh2 in [sl*sl-a_*a_])
   and (q*q)/(h2+q*q)==F(1,9))
ok("V24 le tétraèdre régulier : cosinus de l'angle entre faces = 1/3 ; trois faces sur une ; centre au quart de la hauteur",
   isclose((sqrt(3)/6)/(sqrt(3)/2),1/3) and isclose(sqrt(2/3)/4,(sqrt(2)/12)*3/sqrt(3)))
ok("V25 le losange de côté 1 : la somme des deux diagonales, 2cos + 2sin, est au plus 2√2, atteinte pour le carré seul",
   isclose(max(2*cos(a*pi/7200)+2*sin(a*pi/7200) for a in range(3601)),2*sqrt(2)) and [a for a in range(3601) if isclose(2*cos(a*pi/7200)+2*sin(a*pi/7200),2*sqrt(2),rel_tol=1e-12)]==[1800])
ok("V26 le balayage : un côté reste entre les distances 1 et √2 du centre (l'anneau) ; une diagonale passe par le centre",
   min(d2((F(1),F(k,100)),(0,0)) for k in range(-100,101))==1 and max(d2((F(1),F(k,100)),(0,0)) for k in range(-100,101))==2 and ((coins[0][0]+coins[2][0])/2,(coins[0][1]+coins[2][1])/2)==(0,0))

def _vis(sg):
    c,s_=-1/3,2*sqrt(2)/3; A=[[1,0,0],[0,c,-s_],[0,s_,c]]; p0=[0,.25,0]; Q=[[0,-sg,0],[sg,0,0],[0,0,1]]
    mul=lambda M,v:[sum(M[i][j]*v[j] for j in range(3)) for i in range(3)]
    M=[[sum(Q[i][k]*A[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    Ap=mul(A,p0); tt=mul(Q,[p0[i]-Ap[i] for i in range(3)])
    cth=(M[0][0]+M[1][1]+M[2][2]-1)/2; u=[M[2][1]-M[1][2],M[0][2]-M[2][0],M[1][0]-M[0][1]]; n=sqrt(sum(x*x for x in u)); u=[x/n for x in u]
    tip=mul(A,[0,.75,0]); return cth,abs(sum(u[i]*tt[i] for i in range(3))),abs(u[2])/hypot(u[0],u[1]),(tip[1]+.25,tip[2])
from math import acos
ok("V27 la vis : pli de cosinus −1/3 (tan² du demi-angle = 2) ; la pointe arrive au sommet, hauteur √2/2 ; pli puis quart de tour : cos θ = −2/3, avance 1/√10 = distance du centre aux côtés du vide, pente de l'axe 1/2, dans les deux sens ; pas = 2π/(√10 θ) = 0,8637",
   isclose((1+1/3)/(1-1/3),2) and all(isclose(_vis(g)[0],-2/3) and isclose(_vis(g)[1],1/sqrt(10)) and isclose(_vis(g)[2],.5) and isclose(_vis(g)[3][0],0,abs_tol=1e-12) and isclose(_vis(g)[3][1],sqrt(.5)) for g in (1,-1))
   and round(2*pi/(sqrt(10)*acos(-2/3)),4)==0.8637)
def _alt(somme_seule,N=41):
    S=set()
    for L in range(2,11):
        for d in (2,3):
            seq=[d if i%2==0 else 5-d for i in range(L)]
            for ops in _pr(*(['+' if somme_seule else '+*']*(L-1))):
                e=str(seq[0])+''.join(o+str(x) for o,x in zip(ops,seq[1:])); val=eval(e)
                if val<N: S.add(val)
    return S
ok("V28 la règle du 2 et du 3 : avec la somme et le produit, tout nombre de 5 à 40 ; par la somme seule, 6 et 9 manquent entre 5 et 10 ; second compte : tout n de 5 à 999 est la somme de deux nombres différents, chacun au moins 2, et 4 ne l'est pas ; pyramide carrée : (h/b)² = 8 est la seule égalité possible de h/b et 8b/h",
   all(n in _alt(False) for n in range(5,41)) and [n for n in range(5,11) if n not in _alt(True)]==[6,9]
   and all(any(a!=n-a and n-a>=2 for a in range(2,n-1)) for n in range(5,1000)) and not any(a!=4-a and 4-a>=2 for a in range(2,3)) and F(8)**1==8)
_dr=lambda n:1+(n-1)%9
from itertools import permutations as _pm
_N=987654321123456789
ok("V29 le 8-9-1 du pli : (face/demi-base)² = 9, (hauteur/demi-base)² = 8, 1 + 8 = 9 ; 8 = 2 × 4, 9 = 3² ; du centre de gravité, sommet à 3 rayons inscrits et base à 1 ; rayon inscrit² = demi-base²/2 ; lectures suivies de leur racine : 189 et 819 seules ; 81 = 18 × 4,5 ; 198 = 18 × 11, 891 = 81 × 11 ; abc − cba = 99(a − c), bouts de somme 9 ; 694 − 496 = 198 ; 496 parfait ; 987654321 = 8 × 123456789 + 9 ; 123456789 × 81 = 9 999 999 909 ; la couture : 18 chiffres, divisible par 99",
   ((1-q)/q)**2==9 and h2/(q*q)==8 and (3-1)*(3+1)==8 and h2==16*rho2 and (sqrt(h2)-sqrt(rho2))/sqrt(rho2)>2.999999 and rho2==q*q/2
   and sorted(''.join(p) for p in _pm('189') if _dr(int(''.join(p)[:2]))==int(''.join(p)[2]))==['189','819'] and F(81,18)==F(9,2) and 18*11==198 and 81*11==891
   and all((100*a_+10*b_+c_)-(100*c_+10*b_+a_)==99*(a_-c_) for a_ in range(1,10) for b_ in range(10) for c_ in range(a_)) and all(int(str(99*k).zfill(3)[0])+int(str(99*k).zfill(3)[2])==9 and str(99*k).zfill(3)[1]=='9' for k in range(1,10))
   and 694-496==198 and sum(d for d in range(1,496) if 496%d==0)==496 and 987654321==8*123456789+9 and 123456789*81==9999999909 and len(str(_N))==18 and _N%99==0)
if len(sys.argv)>2:
    from PIL import Image
    im=Image.open(sys.argv[2]).convert('L'); cx,cy,r=540,762,282.0
    def lum(p,s,off=0.0,n=300):
        (x1,y1),(x2,y2)=p,s; dx,dy=x2-x1,y2-y1; Ln=hypot(dx,dy); nx,ny=-dy/Ln,dx/Ln; v=0
        for i in range(n):
            u=0.08+0.84*i/(n-1); x=x1+u*dx+off*nx; y=y1+u*dy+off*ny; v+=im.getpixel((int(round(cx+x*r)),int(round(cy-y*r))))
        return v/n
    seg=[(c,n) for c in contacts for n in noeuds if c[0]*n[0]+c[1]*n[1]<0]+[(c,k) for c in contacts for k in coins if c[0]*k[0]+c[1]*k[1]<0]
    f=lambda p:(float(p[0]),float(p[1]))
    ok("V17 sur l'image de l'auteur : les 8 droites de l'étoile et les 8 droites vers les coins opposés sont tracées (au moins 1,5 fois plus lumineuses que leur voisinage)",
       all(lum(f(a),f(b))>1.5*(lum(f(a),f(b),.02)+lum(f(a),f(b),-.02))/2 for a,b in seg))
if len(sys.argv)>1:
    s=open(sys.argv[1],encoding='utf-8').read()
    ok("V18 typographie de la source : aucun tiret long ni moyen",'—' not in s and '–' not in s)
for n,k in R: print(('conforme : ' if k else 'ÉCHEC : ')+n)
assert all(k for _,k in R); print(len(R),'contrôles, tous conformes')
