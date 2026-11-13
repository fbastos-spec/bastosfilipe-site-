# -*- coding: utf-8 -*-
# La relation et le transport : vérifications. Bibliothèque standard seule.
import sys
from math import sqrt, pi, cos, sin
R=[]
def ok(nom,cond,val=''): R.append((nom,bool(cond),val))
c=299792458.0
# 1. GPS : décalage quotidien des horloges en orbite
GM=3.986004418e14; Rt=6.371e6; r=2.6561e7
grav=GM/c**2*(1/Rt-1/r)*86400e6          # microsecondes par jour, avance
vit=(GM/r)/(2*c**2)*86400e6               # microsecondes par jour, retard
ok("V1 GPS, formules de la relativité refaites : avance de gravité 45,7 µs par jour, retard de vitesse 7,2 µs, net 38 µs",
   abs(grav-45.7)<0.3 and abs(vit-7.2)<0.2 and abs(grav-vit-38.5)<0.6, f"{grav:.1f} - {vit:.1f} = {grav-vit:.1f}")
# 2. Mercure : avance du périhélie
GMs=1.32712440018e20; a=5.790905e10; e=0.20563; T=87.9691
dphi=6*pi*GMs/(c**2*a*(1-e*e))            # radians par orbite
sec=dphi*(36525/T)*(180/pi)*3600
ok("V2 Mercure, formule d'Einstein refaite : 43 secondes d'arc par siècle",abs(sec-43.0)<0.1,f"{sec:.2f}")
# 3. Bell : borne classique 2, borne quantique 2 racine de 2 = 4 x 1/2 x racine de 2
E=lambda x,y:-cos(x-y)
S=abs(E(0,pi/4)-E(0,3*pi/4)+E(pi/2,pi/4)+E(pi/2,3*pi/4))
best=max(abs(a1*b1-a1*b2+a2*b1+a2*b2) for a1 in(1,-1) for a2 in(1,-1) for b1 in(1,-1) for b2 in(1,-1))
ok("V3 corrélations : sans relation la borne est 2 ; avec la paire, 2√2 = 4 × 1/2 × √2, atteinte à 45°",
   best==2 and abs(S-2*sqrt(2))<1e-12 and abs(4*0.5*sqrt(2)-2*sqrt(2))<1e-12,f"{S:.4f}")
# 4. Pas de signal : ce que lit un côté ne dépend pas du réglage de l'autre
def p(sa,sb,x,y): return (1+sa*sb*E(x,y))/4
marg=[sum(p(1,sb,0.3,y) for sb in(1,-1)) for y in (0,0.7,1.9,3.0)]
ok("V4 la relation ne transporte rien : la lecture d'un côté vaut 1/2 quel que soit le réglage de l'autre",all(abs(m-0.5)<1e-12 for m in marg))
# 5. La paire : connaître x donne son inverse sans rien transporter
ok("V5 la paire : x + (9 − x) = 9 pour x de 1 à 8 ; le centre est 4,5 et k = 4,5 / 9 = 1/2",all(x+(9-x)==9 for x in range(1,9)) and 4.5/9==0.5)
# 6. La mesure de novembre 2026
ok("V6 mesure de Li et coll. : 1,01 dB sous la borne, soit 20,7 % en variance",abs((1-10**(-1.01/10))*100-20.7)<0.1,f"{(1-10**(-1.01/10))*100:.1f} %")
if len(sys.argv)>1:
    t=open(sys.argv[1],encoding='utf-8').read()
    ok("V7 typographie de la source : aucun tiret long ni moyen",'—' not in t and '–' not in t)
for n,k,v in R: print(('conforme : ' if k else 'ÉCHEC : ')+n+(' ['+v+']' if v else ''))
assert all(k for _,k,_ in R); print(len(R),'contrôles, tous conformes')
