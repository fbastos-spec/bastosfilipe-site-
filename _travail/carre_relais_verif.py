# Le Carre du relais, v0.5 : assertions executees au build (R10). Bibliotheque standard seulement.
from fractions import Fraction as F
from itertools import permutations
from math import isqrt
D="0123456789ABCDEFGHIJ"
def ecrit(n,b):
    s=""
    while n: s=D[n%b]+s; n//=b
    return s
def adresse(n): return 9 if n%9==0 else n%9
out=[]
# 1. base
assert all(x+(9-x)==9 for x in range(1,9)); assert sum(range(1,10))==45 and F(45,10)==F(9,2)
for n in range(1,9):
    assert all(adresse(n*k)+adresse((9-n)*k)==9 or adresse(n*k)==9 for k in range(1,10))
out.append("Base : paires a 9, tables de n et de 9-n inverses, 45 / 10 = 4,5   OK")
# 2. deux plis
p9=[(x,9-x) for x in range(1,5)]; p10=[(x,10-x) for x in range(1,5)]; p11=[(x,11-x) for x in range(2,6)]
assert p9==[(1,8),(2,7),(3,6),(4,5)] and p10==[(1,9),(2,8),(3,7),(4,6)] and p11==[(2,9),(3,8),(4,7),(5,6)]
assert [x for x in range(1,10) if 2*x==9]==[] and [x for x in range(1,10) if 2*x==10]==[5] and [x for x in range(1,10) if 2*x==11]==[]
assert F(10,2)-F(9,2)==F(1,2)==F(11,2)-F(10,2)
out.append("Plis : centre 4,5 vide (9), 5 plein (10), 5,5 vide (11), ecart 1/2   OK")
# 3. le 5 premier sans double ; cycle du doublement
assert [x for x in range(1,10) if 2*x>9][0]==5 and all(2*x<=9 for x in range(1,5))
c=[1]
while adresse(2*c[-1])!=1: c.append(adresse(2*c[-1]))
assert c==[1,2,4,8,7,5] and adresse(2*5)==1
out.append("Relais : 5 premier chiffre dont le double sort ; cycle 1,2,4,8,7,5 ; 2 x 5 = 10, adresse 1   OK")
# 4-5. quatre demies, le carre
d=[F(1,2),F(9,2),F(10,2),F(11,2)]
assert d[1]*d[3]+d[0]**2==d[2]**2==25 and d[1]*d[3]==F(99,4) and 9*11+1==100
assert d[1]+d[2]+d[3]==15 and d[1]+d[3]==10
out.append("Carre : 4,5 x 5,5 + 0,5 x 0,5 = 24,75 + 0,25 = 25 ; 9 x 11 + 1 = 100   OK")
# 6. le mur
assert 5*7+1==36 and 35//5==7 and 35//7==5 and min(n for n in range(1,100) if n%5==0 and n%7==0)==35
assert all((a-e)*(a+e)+e*e==a*a for a in range(1,200) for e in range(0,a))
out.append("Mur : 5 x 7 + 1 = 36 ; rencontre a 35 (7 pas de 5, 5 pas de 7) ; forme generale sur 19 900 cas   OK")
# 7. le 49 et le 50
assert ecrit(49,9)=="54" and ecrit(49,11)=="45" and 49==7*7==100//2-1 and 50==2*5*5
sol=[(a,b) for a in range(1,9) for b in range(1,9) if 11*a+b==9*b+a]
assert sol==[(4,5)]
bases=[B for B in range(2,100001,2) if int((B*B//2-1)**0.5)**2==B*B//2-1 or (int((B*B//2-1)**0.5)+1)**2==B*B//2-1]
assert bases==[2,10,58,338,1970,11482,66922]
assert all(ecrit(B*B//2-1,B+1)==D[B//2-1]+D[B//2] and ecrit(B*B//2-1,B-1)==D[B//2]+D[B//2-1] for B in range(4,20,2))
out.append("49 : 54 en neuf, 45 en onze, unique (5a = 4b) ; 49 + 1 = 2 x 25 ; bases a carre jusqu'a 100 000 : 2, 10, 58, 338, 1970, 11482, 66922   OK")
# 8. carre de neuf cases
L=[[4,9,2],[3,5,7],[8,1,6]]
lignes=L+[list(c) for c in zip(*L)]+[[L[i][i] for i in range(3)],[L[i][2-i] for i in range(3)]]
assert all(sum(l)==15 for l in lignes) and all(L[i][j]+L[2-i][2-j]==10 for i in range(3) for j in range(3))
n=0
for p in permutations(range(1,10)):
    if p[4]!=5:
        if sum(p[0:3])==15 and sum(p[3:6])==15 and sum(p[6:9])==15 and p[0]+p[3]+p[6]==15 and p[1]+p[4]+p[7]==15 and p[2]+p[5]+p[8]==15 and p[0]+p[4]+p[8]==15 and p[2]+p[4]+p[6]==15: n+=10**6
        continue
    if all(sum(x)==15 for x in (p[0:3],p[3:6],p[6:9],p[0::3],p[1::3],p[2::3],p[0::4],p[2:7:2])): n+=1
assert n==8
P=[[2,3,4],[5,6,7],[8,9,1]]
opp=sorted(P[i][j]+P[2-i][2-j] for i in range(3) for j in range(3) if (i,j)<(2-i,2-j))
assert opp==[3,12,12,12]
out.append("Neuf cases : centre 5, lignes a 15, opposes a 10, 8 dispositions (une seule a rotation et miroir pres) ; pave 234/567/891 : opposes 12, 12, 12 et 3   OK")
# 8 bis. le pave lu de 2 a 10 (le 1 place apres le 9 est le 10)
Q=[[2,3,4],[5,6,7],[8,9,10]]
assert all(Q[i][j]+Q[2-i][2-j]==12 for i in range(3) for j in range(3)) and sum(map(sum,Q))==54 and sum(range(1,10))==45
assert [(x,11-x) for x in range(1,6)]==[(1,10),(2,9),(3,8),(4,7),(5,6)]
assert [F(k,2) for k in (9,10,11,12)]==[F(9,2),5,F(11,2),6]
out.append("Pave lu de 2 a 10 : opposes a 12, somme 54 (cadastre 45) ; centres 4,5 / 5 / 5,5 / 6   OK")
# 8 ter. les briques
nd=lambda n:sum(1 for d in range(1,n+1) if n%d==0)
assert nd(1)==1 and all(nd(p)==2 for p in (2,3,5,7)) and [n for n in range(1,10) if nd(n)==2]==[2,3,5,7]
assert 1+1==2 and 2+3==5 and 2*3==6==1+2+3==1*2*3 and 6+1==7 and (4,8,9)==(2*2,2*2*2,3*3) and 2*3-(2+3)==1
assert [n for n in range(1,100001) if n==sum(d for d in range(1,4)) and n==6]==[6]
out.append("Briques : 1 + 1 = 2, 2 + 3 = 5, 2 x 3 = 6, 6 + 1 = 7 ; un diviseur pour 1, deux pour un premier   OK")
# 5 bis. l'echelle des rectangles ; les pivots (v0.4)
assert [x*(10-x)+(5-x)**2 for x in range(1,5)]==[25,25,25,25] and [x*(10-x) for x in range(1,5)]==[9,16,21,24] and 3*3+4*4==5*5
assert all(F(x)*(9-x)+(F(9,2)-x)**2==F(81,4) for x in range(1,5)) and 1+24==25
assert [adresse(10*k+5) for k in range(10)]==[5,6,7,8,9,1,2,3,4,5] and [adresse(n) for n in (5,50,500)]==[5,5,5] and [F(n,2) for n in (1,10,100,1000)]==[F(1,2),5,50,500]
out.append("Echelle : 1 x 9 + 16 = 2 x 8 + 9 = 3 x 7 + 4 = 4 x 6 + 1 = 25 ; pli a 9 : 81/4 ; pivots   OK")
# 7 bis. la regle de la liste (v0.5) : six fois la precedente, dont on retire celle d'avant ; couples de Theon
assert all(bases[i+1]==6*bases[i]-bases[i-1] for i in range(1,len(bases)-1))
m,k=1,1; couples=[]
for _ in range(8):
    assert k*k+1==2*m*m; couples.append((m,k)); m,k=2*k+3*m,3*k+4*m
assert couples[:7]==[(1,1),(5,7),(29,41),(169,239),(985,1393),(5741,8119),(33461,47321)] and [2*c[0] for c in couples[:7]]==bases
B8=6*bases[-1]-bases[-2]
assert B8==390050==2*couples[7][0] and isqrt(B8*B8//2-1)**2==B8*B8//2-1 and isqrt(B8*B8//2-1)==275807==couples[7][1]
assert (1+2)**2-2*2**2==1 and 3*3-2*2*2==1 and 2*3==6   # (1 + V2)^2 = 3 + 2 V2 ; sa somme avec son conjugue vaut 6
out.append("Regle de la liste : six fois la precedente moins celle d'avant ; couples de Theon ; base suivante 390050   OK")
if __name__=="__main__": print("\n".join(out))
