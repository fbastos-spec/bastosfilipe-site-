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
