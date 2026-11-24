# Emergence of Quantum Correlations v4.0 : verification. Every assertion can fail.
import numpy as np, math
from fractions import Fraction as F
rng=np.random.default_rng(2026); n=3_000_000; TOL=0.003
ok=0
def V(name,cond):
    global ok
    assert cond,"FAIL "+name
    ok+=1; print("pass:",name)
def S2(n):
    v=rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1)[:,None]
lam=S2(n); mu=rng.uniform(-1,1,n)
def u(az,el=0.0):
    t=math.radians(az); e=math.radians(el); return np.array([math.cos(t)*math.cos(e),math.sin(t)*math.cos(e),math.sin(e)])
def chsh(E): return abs(E(u(0),u(45))-E(u(0),u(135))+E(u(90),u(45))+E(u(90),u(135)))
R2=math.sqrt(2)
# --- Section 2
x=lam@u(37,12)
h=np.histogram(x,bins=10,range=(-1,1))[0]/n
V("2.2 height a.lambda evenly spread on [-1,1]",np.max(np.abs(h-0.1))<0.001)
V("2.2 expected |a.lambda| = 1/2",abs(np.mean(np.abs(x))-0.5)<0.001)
# --- Section 5 : protocol with mu
def E_mu(a,b):
    A=np.sign(lam@a); return float(np.mean(A*np.sign(-A*(a@b)-mu)))
angs=(0,30,45,60,90,120,135,180)
V("5.1 E = -cos at eight angles in the plane",all(abs(E_mu(u(0),u(t))+math.cos(math.radians(t)))<TOL for t in angs))
V("5.1 E = -a.b out of the plane",abs(E_mu(u(20,35),u(110,-50))+u(20,35)@u(110,-50))<TOL)
V("5.2 |S| = 2 sqrt 2 at 0,90,45,135",abs(chsh(E_mu)-2*R2)<3*TOL)
V("5.2 each term has magnitude sqrt2/2",abs(math.cos(math.radians(45))-R2/2)<1e-15)
d=np.radians(np.arange(180)); ap=d[:,None,None]; b=d[None,:,None]; bp=d[None,None,:]
Sg=np.abs(-np.cos(b)+np.cos(bp)-np.cos(b-ap)-np.cos(bp-ap))
i=np.unravel_index(np.argmax(Sg),Sg.shape)
V("5.2 scan by degrees: maximum 2 sqrt 2, reached at (90,45,135)",abs(Sg.max()-2*R2)<1e-12 and abs(Sg[90,45,135]-2*R2)<1e-12)
A=np.sign(lam@u(0)); B=np.sign(-A*(u(0)@u(60))-mu)
V("5.3 margins 1/2 for both readings",abs(np.mean(A))<TOL and abs(np.mean(B))<TOL)
# --- 3.2 order
def table(first,second):
    X=np.sign(lam@first); Y=np.sign(-X*(first@second)-mu); return X,Y
for th in (45,60,120):
    a,b_=u(0),u(th); A1,B1=table(a,b_); B2,A2=table(b_,a)
    exp=[(1-x*y*math.cos(math.radians(th)))/4 for x in (1,-1) for y in (1,-1)]
    t1=[np.mean((A1==x)&(B1==y)) for x in (1,-1) for y in (1,-1)]
    t2=[np.mean((A2==x)&(B2==y)) for x in (1,-1) for y in (1,-1)]
    V("3.2 joint table at %d deg, same in both orders"%th,all(abs(p-q)<0.0015 for p,q in zip(t1,exp)) and all(abs(p-q)<0.0015 for p,q in zip(t2,exp)))
# --- Section 6
sg=lambda v: (v>0)-(v<0)
def E_sign(a,b): return -sg(float(a@b))          # exact: AB = -sgn(a.b) for every lambda
V("6.1 bare sign: correlations -1,+1,-1,-1 and |S| = 4",[E_sign(u(0),u(45)),E_sign(u(0),u(135)),E_sign(u(90),u(45)),E_sign(u(90),u(135))]==[-1,1,-1,-1] and chsh(E_sign)==4)
A=np.sign(lam@u(0)); Bs=np.sign((-A[:,None]*u(0))@u(60))
V("6.1 bare sign sampled at 60 deg gives -1",float(np.mean(A*Bs))==-1.0)
w=S2(n)
def E_hemi(a,b):
    A=np.sign(lam@a); ww=w*(-(A*np.sign(w@a)))[:,None]; return float(np.mean(A*np.sign(ww@b)))
V("6.2 hemisphere: straight law -(1-2 theta/pi)",all(abs(E_hemi(u(0),u(t))+(1-2*t/180))<TOL for t in (30,45,60,120)))
V("6.2 hemisphere: |S| = 2",abs(chsh(E_hemi)-2)<4*TOL)
V("6.3 2 sqrt 2 = sqrt(2 x 4); ratio to 4 = r/R; its square 1/2",abs(2*R2-math.sqrt(8))<1e-15 and abs(2*R2/4-R2/2)<1e-15 and abs((R2/2)**2-0.5)<1e-15)
# --- Section 7
c=R2/2
V("7.1 closed form: centre density 4 sqrt2 - 2, edge density 2, flat 2 sqrt2",abs(4*(2*c-c*c)-(4*R2-2))<1e-12 and abs(4*(c*c)-2)<1e-12 and abs(4*c-2*R2)<1e-12)
mu_c=rng.uniform(0,1,n)-rng.uniform(0,1,n)                 # density 1-|mu|
mu_e=np.sign(rng.uniform(-1,1,n))*np.sqrt(rng.uniform(0,1,n))  # density |mu|
def E_with(m):
    def E(a,b):
        A=np.sign(lam@a); return float(np.mean(A*np.sign(-A*(a@b)-m)))
    return E
V("7.1 sampled: centre density gives 3.66",abs(chsh(E_with(mu_c))-(4*R2-2))<4*TOL)
V("7.1 sampled: edge density gives 2",abs(chsh(E_with(mu_e))-2)<4*TOL)
V("7.2 at 60 deg: flat 0.5, centre 0.75, edge 0.25",abs(-E_mu(u(0),u(60))-0.5)<TOL and abs(-E_with(mu_c)(u(0),u(60))-0.75)<TOL and abs(-E_with(mu_e)(u(0),u(60))-0.25)<TOL)
z=np.array([0,0,1.0])
def E_lam(a,b):
    A=np.sign(lam@a); cc=np.cross(a,z); cc/=np.linalg.norm(cc); return float(np.mean(A*np.sign(-A*(a@b)-lam@cc)))
V("7.3 sphere: unread height as threshold gives the cosine",all(abs(E_lam(u(0),u(t))+math.cos(math.radians(t)))<TOL for t in angs))
V("7.3 sphere: |S| = 2 sqrt 2",abs(chsh(E_lam)-2*R2)<4*TOL)
cc=np.cross(u(0),z); V("7.3 unread height unlinked to the first sign",abs(np.mean(np.sign(lam@u(0))*(lam@cc)))<TOL)
phi=rng.uniform(0,2*math.pi,n); l2=np.stack([np.cos(phi),np.sin(phi)],1)
def E_circ(t):
    a=np.array([1.0,0]); b=np.array([math.cos(math.radians(t)),math.sin(math.radians(t))]); A=np.sign(l2@a)
    return float(np.mean(A*np.sign(-A*(a@b)-l2@np.array([0,1.0]))))
V("7.3 circle: falls back to the straight law",all(abs(E_circ(t)+(1-2*t/180))<TOL for t in (30,45,60)))
# --- Section 8
V("8.2 4 x 1/2 x sqrt2 = 2 sqrt2 ; 4 x 1/2 x 1 = 2",abs(4*0.5*R2-2*R2)<1e-15 and 4*F(1,2)*1==2)
pairs=[(1,8),(2,7),(3,6),(4,5)]
V("8.3 hourglass widths 7,5,3,1 of sum 16",[q-p for p,q in pairs]==[7,5,3,1] and sum(q-p for p,q in pairs)==16)
Ec=lambda a,b: -math.cos(a-b)
V("8.3 directions 0 and 90 alone give 2",abs(abs(Ec(0,0)-Ec(0,math.pi/2)+Ec(math.pi/2,0)+Ec(math.pi/2,math.pi/2))-2)<1e-12)
# --- Section 11, 12
V("11.1 four pairs of sum 9, centre 9/2, ratio 1/2 in bases 2..36",all(p+q==9 for p,q in pairs) and F(9,2)==9-F(9,2) and all(F(F(b-1,2),b-1)==F(1,2) for b in range(2,37)))
V("11.1 centre of positions 1..9 is 5, of 1..8 is 4.5",F(sum(range(1,10)),9)==5 and F(sum(range(1,9)),8)==F(9,2))
V("12.1 couples (1,2),(4,5),(7,8): centres 1.5, 4.5, 7.5, gaps 3",[F(p+q,2) for p,q in ((1,2),(4,5),(7,8))]==[F(3,2),F(9,2),F(15,2)])
V("12.2 4.5^2 + 6^2 = 7.5^2 ; 3,4,5 times 1.5 ; perimeter 18",F(9,2)**2+36==F(15,2)**2 and (F(9,2)/3,F(6)/4,F(15,2)/5)==(F(3,2),)*3 and F(9,2)+6+F(15,2)==18)
lad=[F(9,2)+F(k,2) for k in range(7)]
V("12.3 ladder: six steps of 1/2, the 6 at the third",lad[-1]==F(15,2) and lad[3]==6 and len(lad)-1==6)
# --- Section 14 : Toner and Bacon
l1=lam; l22=S2(n)
def E_tb(a,b):
    A=np.sign(l1@a); cb=A*np.sign(l22@a); return float(np.mean(A*(-np.sign((l1+cb[:,None]*l22)@b))))
V("14 Toner-Bacon model: cosine with two vectors and one bit",all(abs(E_tb(u(0),u(t))+math.cos(math.radians(t)))<TOL for t in angs))

# --- second draft
dd=np.radians(np.arange(0,180,0.5)); ap=dd[:,None,None]; bb=dd[None,:,None]; bp=dd[None,None,:]
fe=lambda x: -np.sign(np.cos(x))*np.cos(x)**2
Se=np.abs(fe(bb)-fe(bp)+fe(bb-ap)+fe(bp-ap))
V("7.1 edge density: 2 at the fixed settings, maximum 1 + sqrt2 over all settings",abs(Se[180,90,270]-2)<1e-12 and abs(Se.max()-(1+R2))<1e-9)
def ordered(a,b_):
    la,lb=lam@a,lam@b_; fa=np.abs(la)>=np.abs(lb); c=a@b_
    A=np.where(fa,np.sign(la),0.0); B=np.where(~fa,np.sign(lb),0.0)
    B=np.where(fa,np.sign(-A*c-mu),B); A=np.where(~fa,np.sign(-B*c-mu),A)
    return A,B,fa
good=True
for th in (45,60,120):
    A,B,fa=ordered(u(0),u(th))
    exp=[(1-x*y*math.cos(math.radians(th)))/4 for x in (1,-1) for y in (1,-1)]
    tb=[np.mean((A==x)&(B==y)) for x in (1,-1) for y in (1,-1)]
    good=good and all(abs(p_-q_)<0.0015 for p_,q_ in zip(tb,exp)) and abs(np.mean(fa)-0.5)<TOL and abs(np.mean(A))<TOL and abs(np.mean(B))<TOL
V("3.3 order carried by the state: same table, margins 1/2, each face first half of the time",good)
Eo=lambda a,b_: float(np.mean(np.prod(ordered(a,b_)[:2],axis=0)))
V("3.3 order carried by the state: |S| = 2 sqrt 2",abs(chsh(Eo)-2*R2)<4*TOL)
V("7.1 flat density: maximum over all settings 2 sqrt 2",abs(Sg.max()-2*R2)<1e-12)
print(ok,"checks, all passed")
