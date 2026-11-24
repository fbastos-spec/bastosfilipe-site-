# Riemann sans le zero, complement de la version 0.7 (23 novembre 2026)
import numpy as np, math
from fractions import Fraction as F
ok=[]
def chk(nom,cond,detail=''):
    ok.append(bool(cond)); print(('conforme  ' if cond else 'ECART     ')+nom+(' : '+detail if detail else ''))
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; lp=np.cumsum(np.log1p(-1.0/P))
recu={10**8:5761455,10**10:455052511,10**14:3204941750802}   # comptes recus
def prod(x):
    z=int(round(x**.5)); return math.exp(lp[np.searchsorted(P,z,side='right')-1]), z
m8,z8=prod(10**8); m14,z14=prod(10**14)
chk('Mertens : produit fois logarithme de la borne des nouveaux (10 000, dix millions) = 0,56077 a 10^8, 0,56145 a 10^14', (round(m8*math.log(z8),5),round(m14*math.log(z14),5))==(0.56077,0.56145))
ex=[round(100*(x*prod(x)[0]/recu[x]-1),2) for x in recu]
chk('exces du produit : 5,68 % / 7,14 % / 8,69 %', ex==[5.68,7.14,8.69], str(ex))
chk('limite recue de l exces : 12,29 %', round(100*(2*math.exp(-0.5772156649015329)-1),2)==12.29)
f=lambda x: math.log(x)/(8*math.pi)
chk('facteur de 9.2 : 0,733 a 10^8, 1 vers 82 milliards, 1,28 a 10^14', (round(f(1e8),3),round(math.exp(8*math.pi)/1e9),round(f(1e14),2))==(0.733,82,1.28))
pent=sorted({0}|{k*(3*k-1)//2 for k in range(1,60)}|{k*(3*k+1)//2 for k in range(1,60)})
t=[e for e in pent if e<=2000]
chk('73 termes jusqu a 2000 : le depart et 72 sauts', len(t)==73 and t[0]==0)
r=[n for n in range(1,1200) if n%6 in (1,5)]
chk('exposants de 4.5 bis : rang + 1/24 = carre d une place des rails / 24 ; 1/24 = moitie de 1/12', all(F(e)+F(1,24)==F(n*n,24) for e,n in zip(pent,r)) and F(1,12)/2==F(1,24))
Q=P[P>3]; v=[]
for X in (10**6,10**7,10**8):
    q=Q[Q<=X]; v.append(round(100*float(((q[1:]%6)!=(q[:-1]%6)).mean()),2))
chk('voisins sur des rails differents : 58,19 % / 56,96 % / 56,11 %', v==[58.19,56.96,56.11], str(v))
# ajouts v0.8
chk('exces sur les seules places des rails : 5,70 %', round(100*(6088469/5760226-1),2)==5.70)
chk('borne de Schoenfeld a 10^8 : environ 7 330, au-dessus de 753,33', round(1e4*math.log(1e8)/(8*math.pi),-1)==7330)
import cmath
def eta(tau,pre=True,n=400):
    q=cmath.exp(2j*cmath.pi*tau); p=1
    for k in range(1,n): p*=(1-q**k)
    return (cmath.exp(2j*cmath.pi*tau/24) if pre else 1)*p
tau=0.3+0.8j
avec=abs(eta(-1/tau)-cmath.sqrt(-1j*tau)*eta(tau)); sans=abs(eta(-1/tau,False)-cmath.sqrt(-1j*tau)*eta(tau,False))
chk('inversion : avec le 1/24 la fonction se retrouve, sans lui non', avec<1e-12 and sans>1e-3, 'ecart avec %.1e, sans %.3f'%(avec,sans))
# ajout v0.9 : le cote de l ecart de 4.4
nv=P[(P>3)&(P<=10**4)]
rl=np.zeros(N+1,dtype=bool); rl[5::6]=True; rl[7::6]=True; tot=int(rl.sum()); cote=[]
for k,g_ in enumerate(nv,1):
    rl[g_::g_]=False
    if k in (6,20,100,len(nv)):
        cote.append(round(tot*math.prod(1-1/float(h) for h in nv[:k])-int(rl.sum()),2))
chk('4.4 : produit moins compte = +1,56 / +984,03 / -56 790,24 / +328 243,00', cote==[1.56,984.03,-56790.24,328243.0], str(cote))
# ajouts v0.11
from mpmath import li as _li, log as _lg
c0=float(_li(2)-_lg(2))
chk('constante d origine 0,352 ; zeros = reste + 0,352 : 29,74 / 90,41 / 95,63', round(c0,3)==0.352 and [round(x+c0,2) for x in (29.39,90.06,95.28)]==[29.74,90.41,95.63])
Pq=P[P>3]; Av=int((Pq%6==5).sum()-(Pq%6==1).sum()); tt=F(0); k=2
while 5**k<=N:
    r=int(round(N**(1.0/k)))
    while (r+1)**k<=N: r+=1
    while r**k>N: r-=1
    q=Pq[Pq<=r]; tt+=F(int(sum((1 if int(p)%6==1 else -1)**k for p in q)),k); k+=1
chk('partage exact de l avance : 419 = 619,84 dont on retire 200,84', Av==419 and round(float(tt),2)==619.84 and round(float(tt-Av),2)==200.84)
print(sum(ok),'controles sur',len(ok),'conformes')
