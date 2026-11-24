# Riemann sans le zero, v0.2 : controles. Chaque assertion peut echouer.
import numpy as np, math, bisect
from fractions import Fraction as F
import mpmath as mp
ok=0
def V(nom,cond):
    global ok
    assert cond, "ECHEC "+nom
    ok+=1; print("conforme :",nom)
X=10**8
s=np.ones(X+1,dtype=bool); s[:2]=False
for p in range(2,10001):
    if s[p]: s[p*p::p]=False
P=np.flatnonzero(s)
pi=lambda y:int(np.searchsorted(P,y,side='right'))
V("0.3 pi(cent millions) = 5 761 455",pi(X)==5761455)
V("0.3 les 5 761 453 premiers apres 3 sont sur les rails",bool(np.all((P[2:]%6==1)|(P[2:]%6==5))) and len(P)-2==5761453)
V("0.3 aucune position 3, 6, 9",not np.any(P[2:]%3==0))
# 3.3 le carre
img={}
for x in range(1,9): img.setdefault((x*x-1)%9+1,[]).append(x)
V("3.3 le carre : 1,8->1 ; 2,7->4 ; 4,5->7 ; 3,6->9",img=={1:[1,8],4:[2,7],7:[4,5],9:[3,6]})
V("3.2 point fixe 4,5 et 4,5/9 = 1/2",F(9,2)==9-F(9,2) and F(9,2)/9==F(1,2))
# 4.1 la rampe
def li(x,n=2000000):
    a,b=math.log(2),math.log(x); h=(b-a)/n; f=lambda u: math.exp(u)/u
    return (f(a)+f(b)+4*sum(f(a+(2*i-1)*h) for i in range(1,n//2+1))+2*sum(f(a+2*i*h) for i in range(1,n//2)))*h/3
def iroot(x,k):
    y=int(round(x**(1/k)))
    while y**k>x: y-=1
    while (y+1)**k<=x: y+=1
    return y
att={10**6:(128.50,84.00,8.33,6.78,29.39),10**7:(338.36,223.00,15.67,9.63,90.06),10**8:(753.33,614.50,30.00,13.55,95.28)}
for x,a in att.items():
    e=li(x)-pi(x); parts=[]; k=2
    while 2**k<=x: parts.append(pi(iroot(x,k))/k); k+=1
    got=(e,parts[0],parts[1],sum(parts[2:]),e-sum(parts))
    V("4.1 rampe a %d : %s"%(x,a),all(abs(g-t)<0.006 for g,t in zip(got,a)))
V("9.2 dernier nouveau a cent millions = 9 973",int(P[pi(10**4)-1])==9973)
# 4.4 produit des parts
rail=np.zeros(X+1,dtype=bool); rail[5::6]=True; rail[7::6]=True
N=int(rail.sum()); V("4.4 places des rails = 33 333 332",N==33333332)
libre=rail.copy(); prodf=1.0
att={6:(19,17102400,17102401.56),20:(79,12444165,12445149.03),100:(557,8899649,8842858.76),1227:(9973,5760226,6088469.00)}
nouveaux=[int(p) for p in P[2:] if p<=10**4]
for j,p in enumerate(nouveaux,1):
    libre[p*p::p]=False; prodf*=(1-1/p)
    if j in att:
        free=int(libre.sum())-j
        V("4.4 %d nouveaux : libres %d, produit %.2f"%(j,att[j][1],att[j][2]),p==att[j][0] and free==att[j][1] and abs(N*prodf-att[j][2])<0.01)
V("4.4 nombre des nouveaux = 1 227",len(nouveaux)==1227)
m=1.0
for p in P: m*=(1-1/float(p))
mer=m*math.log(X); print("   produit du crible fois logarithme, a cent millions :",round(mer,6))
V("4.4 Mertens : vers 0,56146",abs(mer-0.561459)<0.0002)
K=10**6; G=[5,7,11,13,17,19]
a=np.arange(1,K+1); t=0
for sgn in (-1,1):
    n=6*a+sgn; hit=np.zeros(K,dtype=bool)
    for g in G: hit|=(n%g==0)
    t+=int(hit.sum())
pr=F(1)
for g in G: pr*=1-F(1,g)
V("4.4 formule pliee : 973 855,87 + 2,13 = 973 858",t==973858 and abs(float(2*K*(1-pr))-973855.87)<0.005)
# 4.5 produit d'Euler developpe
Nq=2000; c=[0]*(Nq+1); c[0]=1
for n in range(1,Nq+1):
    for e in range(Nq,n-1,-1): c[e]-=c[e-n]
deb=[e for e in range(Nq+1) if c[e]!=0]
rails=sorted({(q*q-1)//24 for q in range(1,400) if q%6 in (1,5) and (q*q-1)//24<=Nq})
V("4.5 73 exposants debout, 1 928 annules, tous des carres des rails",len(deb)==73 and deb==rails and all(abs(c[e])==1 for e in deb))
V("4.5 la liste 1, 25, 49, 121, 169, 289, 361, 529, 625",[24*e+1 for e in deb[:9]]==[1,25,49,121,169,289,361,529,625])
# 7.2
V("7.2 carre des rails = 24k+1, jusqu'a un million par rail",all(((6*q+sg)**2-1)%24==0 for q in range(1,10**6+1) for sg in (-1,1)))
# 6.6
pp=P[(P>=5)&(P<=10**6)]; sm=(pp[1:]+pp[:-1])%6==0
V("6.6 somme des voisins : 45 674 sur 78 495",len(sm)==78495 and int(sm.sum())==45674)
V("6.6 sur l'axe exactement quand les rails different",bool(np.all(sm==((pp[1:]%6)!=(pp[:-1]%6)))))
V("6.6 premiere rupture 23 + 29",next((int(x),int(y)) for x,y in zip(pp[:-1],pp[1:]) if (x+y)%6)==(23,29))
# 5 l'horloge
mp.mp.dps=18; M=600
z=[float(mp.zetazero(k).imag) for k in range(1,M+1)]
V("5 dernier zero a 939,02",abs(z[-1]-939.02)<0.01)
g=[float(mp.grampoint(k)) for k in range(-1,M+3)]
cnt=[0]*(len(g)-1)
for x in z: cnt[bisect.bisect_right(g,x)-1]+=1
full=[(i-1,n) for i,n in enumerate(cnt) if g[i+1]<=z[-1]]
cc=[n for _,n in full]
V("5.1 599 cases, 561 a un zero, 19 vides, 19 doubles",len(cc)==599 and cc.count(1)==561 and cc.count(0)==19 and cc.count(2)==19)
vid=[i for i,n in enumerate(cc) if n==0]
V("5.1 chaque case vide est collee a une case double",all((i>0 and cc[i-1]==2) or (i+1<len(cc) and cc[i+1]==2) for i in vid))
V("5.1 premiere rupture aux cases 125 et 126",[k for k,n in full if n!=1][:2]==[125,126])
th=lambda x: float(mp.siegeltheta(x))
S=[k-(th(x)/math.pi+1)-0.5 for k,x in enumerate(z,1)]
V("5.1 ecart du compte a l'horloge sous 0,672",max(max(S),-min(S))<0.6725 and max(S)>0.671)
d=[(th(b)-th(a))/math.pi for a,b in zip(z,z[1:])]
V("5.1 plus petit ecart entre voisins 0,236",abs(min(d)-0.236)<0.001)
b=[0]*6
for x in z: b[int((x%24)/24*6)]+=1
V("5.2 pas de 24 : 102, 99, 99, 103, 98, 99",b==[102,99,99,103,98,99])
t=z[0]; ex=th(t); base=t/2*math.log(t/(2*math.pi))-t/2-math.pi/8
e0,e1,e2=abs(ex-base),abs(ex-base-1/(48*t)),abs(ex-base-1/(48*t)-7/(5760*t**3))
V("5.3 les termes 1/48 et 7/5760 sont reels",1e-3<e0<2e-3 and 1e-7<e1<1e-6 and e2<1e-9)
V("5.3 48 = 2 x 24 et 5760 = 240 x 24",48==2*24 and 5760==240*24)
# 2.1, 5.4, 5.6
V("2.1 l'etoile : 1/3 + 4/6 = 1 et 1/4 + 12/16 = 1",F(1,3)+4*F(1,6)==1 and F(1,4)+4*F(3,16)==1)
V("2.1 ecart 1/12 = quatre triangles de 1/48 ; 3/16 = 1/6 + 1/48",F(1,3)-F(1,4)==F(1,12)==4*F(1,48) and F(3,16)==F(1,6)+F(1,48))
V("5.4 sur 48 : 9, 8, 1 ; et 3/16 = 1/8 + 1/16",F(3,16)*48==9 and F(1,6)*48==8 and F(1,8)+F(1,16)==F(3,16))
tt=mp.mpf(10000); zz=mp.mpf(1)/4+1j*tt/2
A=mp.im((zz-mp.mpf(1)/2)*mp.log(zz))-(tt/2*mp.log(tt/2)-mp.pi/8); B=mp.im(1/(12*zz))
V("5.4 dans l'horloge : part du quart 3/16, part du 1/12 d'Euler 1/6",abs(A*tt-mp.mpf(3)/16)<1e-6 and abs(-B*tt-mp.mpf(1)/6)<1e-6)
V("5.6 second etage : 1/24 moins 7/384 moins 1/45 = 7/5760",F(1,24)-F(7,384)-F(1,45)==F(7,5760))
V("2.2 le pli : 1 + 8 = 9",1+8==9)
print(ok,"controles, tous conformes")
