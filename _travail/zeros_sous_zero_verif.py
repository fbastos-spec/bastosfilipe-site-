# Des zeros sous zero : controles refaits (23 novembre 2026)
import math
from mpmath import mp, mpf, pi as MPI, nint, zetazero
ok=[]
def chk(nom,cond,detail=''):
    ok.append(bool(cond)); print(('conforme  ' if cond else 'ECART     ')+nom+(' : '+detail if detail else ''))
# 1. compte exact a 10^8 par le crible des deux rails
import numpy as np
N=10**8; s=np.ones(N+1,bool); s[:2]=False
for p in range(2,int(N**.5)+1):
    if s[p]: s[p*p::p]=False
chk('compte des premiers sous 10^8', int(s.sum())==5761455, str(int(s.sum())))
chk('rampe trop haute de 753,33 = 658,05 + 95,28', abs(658.05+95.28-753.33)<1e-9)
# 1 bis. les deux rails, sans un zero (ajout v0.4)
P=np.nonzero(s)[0]; P=P[P>3]
c5=np.cumsum(P%6==5); c7=np.cumsum(P%6==1); av=c5-c7
at=lambda x:int(np.searchsorted(P,x,side='right'))-1
chk('rails a 10^8 : 2 880 936 sur le 5, 2 880 517 sur le 7, avance 419', (int(c5[at(N)]),int(c7[at(N)]))==(2880936,2880517))
chk('rails a 10^4 et 10^6 : 616/611 et 39 265/39 231', (int(c5[at(10**4)]),int(c7[at(10**4)]),int(c5[at(10**6)]),int(c7[at(10**6)]))==(616,611,39265,39231))
chk('le rail du 7 ne passe jamais devant jusqu a 10^8', int(av.min())==0, 'egalites %d, avance maximale %d'%(int((av==0).sum()),int(av.max())))
mm=[n for n in range(5,10001) if n%6 in (1,5)]
chk('les carres des places des rails sous 10^8 tombent tous sur le rail du 7', all((n*n)%6==1 for n in mm), '%d carres'%len(mm))
# 1 ter. l avance du rail du 5 et la moitie des nouveaux entres (ajout v0.5, mots corriges v0.6)
AP=np.nonzero(s)[0]
half=lambda x:(int(np.searchsorted(AP,int(x**.5),side='right'))-2)/2
chk('moitie des nouveaux entres des rails : 11,5 / 83 / 222 / 613,5', [half(10**k) for k in (4,6,7,8)]==[11.5,83.0,222.0,613.5])
chk('avance du 5 : 5 / 34 / 189 / 419', [int(av[at(10**k)]) for k in (4,6,7,8)]==[5,34,189,419])
xs=np.exp(np.linspace(np.log(1e4),np.log(1e8),2001))
rp=np.array([av[at(x)]/half(x) for x in xs])
dec=[round(float(rp[(xs>=10**k)&(xs<10**(k+1))].mean()),2) for k in (4,5,6,7)]
chk('rapport moyen avance / moitie de 10^4 a 10^8 : 1,03 ; par decade 1,07 1,03 1,02 1,01', round(float(rp.mean()),2)==1.03 and dec==[1.07,1.03,1.02,1.01], '%.3f %s'%(rp.mean(),dec))
chk('1 227 carres de premiers sur les rails sous 10^8, de 5 a 9 973', int(np.searchsorted(AP,10**4))-2==1227 and int(AP[np.searchsorted(AP,10**4)-1])==9973)
chk('614,50 de la rampe = 613,5 + les carres de 2 et de 3', 613.5+1==614.5)
# tableau 4.6 etendu : avances et nouveaux entres repris de Ce que Riemann cherchait 5.7 (non recomptes ici)
T46=[(5,23),(34,166),(189,444),(419,1227),(6263,9590),(44976,78496),(152811,227645),(259652,664577)]
chk('rapports du tableau 4.6 : 0,43 0,41 0,85 0,68 1,31 1,15 1,34 0,78', [round(a/(b/2),2) for a,b in T46]==[0.43,0.41,0.85,0.68,1.31,1.15,1.34,0.78] and [int(av[at(10**k)]) for k in (4,6,7,8)]==[x for x,_ in T46[:4]])
del AP
del P,c5,c7,av
# 2. sauts de 24
r=[n for n in range(1,2000) if n%6 in (1,5)]; q=[n*n for n in r]
d=[b-a for a,b in zip(q,q[1:])]
chk('tout ecart entre carres voisins des rails est un nombre entier de sauts de 24', all(x%24==0 for x in d))
j=[x//24 for x in d]
chk('sauts dans le couple : 1,2,3,4...', j[1::2][:300]==list(range(1,301)))
chk('sauts entre couples : 1,3,5,7...', j[0::2][:300]==list(range(1,601,2)))
pent=sorted({k*(3*k-1)//2 for k in range(1,400)}|{k*(3*k+1)//2 for k in range(1,400)})
chk('total des sauts = pentagonaux 1,2,5,7,12,15', [(x-1)//24 for x in q[1:201]]==pent[:200])
chk('5 lignes : 1,25,49,121,169 = 1 puis +24,+24,+72,+48', q[:5]==[1,25,49,121,169] and d[:4]==[24,24,72,48])
chk('24k part de 0 : 24,48,120,168 tombe un cran a cote', [24*k+1 for k in (1,2,5,7)]==q[1:5])
# 3. regle de projection : huit places, un tour de 24
h=[n for n in range(1,24) if n%6 in (1,5)]
chk('huit places des rails sur un tour de 24', h==[1,5,7,11,13,17,19,23])
chk('leurs huit carres tombent tous a la place 1 du tour', all((n*n)%24==1 for n in h), str([n*n for n in h]))
# 4. cercle du doublement
dr=lambda n:(n-1)%9+1
chk('positions des puissances de 2 : 1,2,4,8,7,5', [dr(2**k) for k in range(6)]==[1,2,4,8,7,5])
chk('demi-tour = paire a 9', all(dr(2**k)+dr(2**(k+3))==9 for k in range(6)))
chk('position de 2^1000 lue sur l exposant = 7', dr(2**1000)==7 and 1000%6==4)
def tour(m):
    k=1;x=2
    while x!=1: x=x*2%m;k+=1
    return k
chk('tour du doublement par etage : 6, 54, 486, 4374', [tour(9**k) for k in (1,2,3,4)]==[6,54,486,4374])
# 5. marche autour du cercle : jamais de retour exact
mp.dps=40; best=mpf(10); rec=[]
for n in range(1,400000):
    t=nint(n/MPI); e=abs(n-t*MPI)
    if e<best: best=e; rec.append((n,int(t),float(e)))
chk('presque-retours a 22 pas (7 tours) et 355 pas (113 tours)', (22,7) in [(a,b) for a,b,c in rec] and (355,113) in [(a,b) for a,b,c in rec])
chk('aucun retour exact jusqu a 400 000 pas', best>0, 'plus petit ecart %.7f'%float(best))
# 6. les zeros sonnent aux puissances d un seul premier
g=[float(zetazero(k).imag) for k in range(1,201)]
S=lambda x:-sum(math.cos(t*math.log(x)) for t in g)
pp={2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32}
v={n:S(n) for n in range(2,34)}
a=min(v[n] for n in v if n in pp); b=max(v[n] for n in v if n not in pp)
chk('200 zeros : la plus faible des puissances depasse le plus fort des autres', a>b, 'min puissances %.1f, max autres %.1f'%(a,b))
print('   releve :',{n:round(v[n],1) for n in (2,3,4,5,7,8,9,16,25,27,32,6,10,12,15)})
chk('trois premiers zeros : 14,13 / 21,02 / 25,01', [round(x,2) for x in g[:3]]==[14.13,21.02,25.01])
# 7. la somme alternee dans la bande, et la fonction symetrique (ajout v0.4)
from mpmath import altzeta, zeta, gamma, mpc
mp.dps=25
chk('la somme alternee s annule aux trois premiers zeros', all(abs(altzeta(zetazero(k)))<mpf(10)**-18 for k in (1,2,3)))
xi=lambda z: z*(z-1)/2*MPI**(-z/2)*gamma(z/2)*zeta(z)
z0=mpc('0.3','5')
chk('fonction symetrique : meme valeur en s et en 1 - s', abs(xi(z0)-xi(1-z0))<mpf(10)**-18)
chk('a 2 sous zero la fonction symetrique ne s annule pas (vaut sa valeur en 3)', abs(xi(mpf(-2)+mpf(10)**-12)-xi(3))<mpf(10)**-9 and abs(xi(3))>0.5, 'valeur %.4f'%float(xi(3)))
# ---- ajouts v0.9
chk('les deux carres autour de 6m sont a m sauts de 24 l un de l autre', all(((6*m+1)**2-(6*m-1)**2)==24*m for m in range(1,5000)))
cp={((3*m*m-m)//2,(3*m*m+m)//2) for m in range(1,45)}
fd={(x,y) for x in range(1,3000) for y in range(x+1,x+70) if x+y==3*(y-x)**2}
chk('test inverse : a + b = 3 fois le carre de l ecart, exactement les couples d un meme axe', fd=={c for c in cp if c[0]<3000}, '%d couples'%len(fd))
from mpmath import zeta as _z
Lf=lambda k,chi,q: q**(mpf(k))*sum(c*_z(-k,mpf(x)/q) for x,c in chi.items())
r1=[abs(Lf(k,{1:1,5:-1},6))<mpf(10)**-15 for k in range(1,7)]; r2=[abs(Lf(k,{1:1,5:-1,7:-1,11:1},12))<mpf(10)**-15 for k in range(1,7)]
chk('signe du rail : zeros a 1, 3, 5 pas sous zero ; signe du produit : a 2, 4, 6', r1==[True,False]*3 and r2==[False,True]*3)
def pur(n):
    for p in range(2,n+1):
        if n%p==0:
            while n%p==0: n//=p
            return n==1
vv={n:S(n) for n in range(2,65)}
t63=min(vv[n] for n in range(2,64) if pur(n))>max(vv[n] for n in range(2,64) if not pur(n))
chk('200 zeros : le partage tient jusqu a 63 et casse a 64 (64 : 1,83 ; 48 : 3,08)', t63 and (round(vv[64],2),round(vv[48],2))==(1.83,3.08))
from mpmath import li as _li, log as _lg
chk('constante d origine : 0,352 ; zeros = 95,28 + 0,35 = 95,63', round(float(_li(2)-_lg(2)),3)==0.352 and round(95.277242+float(_li(2)-_lg(2)),2)==95.63)
from fractions import Fraction as Fr
Pq=np.nonzero(s)[0]; Pq=Pq[Pq>3]; Av=int((Pq%6==5).sum()-(Pq%6==1).sum()); tt=Fr(0); k=2
while 5**k<=N:
    r=int(round(N**(1.0/k)))
    while (r+1)**k<=N: r+=1
    while r**k>N: r-=1
    q=Pq[Pq<=r]; tt+=Fr(int(sum((1 if int(p)%6==1 else -1)**k for p in q)),k); k+=1
chk('partage exact : 419 = 102274/165 dont on retire 33139/165', Av==419 and tt==Fr(102274,165) and tt-Av==Fr(33139,165), '%.2f et %.2f'%(float(tt),float(tt-Av)))
print(sum(ok),'controles sur',len(ok),'conformes')
