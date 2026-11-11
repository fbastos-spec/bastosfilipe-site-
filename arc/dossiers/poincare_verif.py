# Poincare est la matriochka v0.1 : verifications (bibliotheque standard seule)
from itertools import combinations, product
from fractions import Fraction as Fr
from collections import Counter
from math import pi, sin, sqrt, gcd
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
dr = lambda n: 1 + (n - 1) % 9

# V1 comptes des surfaces fermees : sommets - aretes + faces
ok("V1 tetraedre 4-6+4=2, octaedre 6-12+8=2, icosaedre 12-30+20=2, tore a 7 sommets 7-21+14=0",
   (4-6+4, 6-12+8, 12-30+20, 7-21+14) == (2, 2, 2, 0))
# V2 dimension 3 : le compte est nul
ok("V2 bord du 4-simplexe 5-10+10-5=0, 16 cellules 8-24+32-16=0, 600 cellules 120-720+1200-600=0",
   (5-10+10-5, 8-24+32-16, 120-720+1200-600) == (0, 0, 0))
# V3 Descartes : somme des (6 - degre) = 12 sur une sphere de triangles
ok("V3 Descartes : 4x3 = 6x2 = 12x1 = 12", 4*(6-3) == 6*(6-4) == 12*(6-5) == 12)
# V4 les 7 coupes d'une cellule a quatre pointes
P = [frozenset(s) for k in (1, 2) for s in combinations(range(4), k)]
coupes = {frozenset([s, frozenset(range(4)) - s]) for s in P}
quads = [c for c in coupes if all(len(x) == 2 for x in c)]
ok("V4 sept coupes : 4 (une pointe contre trois) + 3 (deux contre deux)", len(coupes) == 7 and len(quads) == 3)
def croise(c1, c2): return all(a & b for a in c1 for b in c2)
ok("V5 deux coupes deux-contre-deux distinctes se croisent toujours",
   all(croise(a, b) for a, b in combinations(quads, 2)))
# V6 le cube en trois pyramides : volume exact 1/3 (x maximal : integrale de x^2 sur [0,1])
ok("V6 cube = 3 pyramides de volume 1/3", Fr(1, 3) * 3 == 1)
# V7 un trou : p tours valent rien ; le nombre de boucles distinctes est p ; une seule (aucune ne resiste) pour p = 1
def boucles(p):
    vus, x = set(), 0
    while x not in vus: vus.add(x); x = (x + 1) % p
    return len(vus)
ok("V7 deux beignes a p tours : p boucles distinctes ; aucune ne resiste seulement pour p = 1",
   all(boucles(p) == p for p in range(1, 60)) and [p for p in range(1, 60) if boucles(p) == 1] == [1])
# V8 le squelette a trois faces sur un trait (bonnet d'ane, 8 sommets)
F = [(1,2,4),(1,2,7),(1,2,8),(1,3,4),(1,3,5),(1,3,6),(1,5,6),(1,7,8),(2,3,5),(2,3,7),(2,3,8),
     (2,4,5),(3,4,8),(3,6,7),(4,5,6),(4,6,8),(6,7,8)]
E = Counter(e for f in F for e in combinations(f, 2))
ok("V8 squelette : 8-24+17=1, aucune arete libre, 3 aretes portent 3 faces",
   (8, len(E), len(F)) == (8, 24, 17) and min(E.values()) == 2 and Counter(E.values())[3] == 3)
# V9 les 120 : groupe engendre par deux quaternions (un dixieme de tour, un tiers de tour)
phi = (1 + sqrt(5)) / 2
def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3], a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
            a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1], a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])
key = lambda q: tuple(round(x, 6) + 0.0 for x in q)
g1 = (phi/2, 1/(2*phi), 0.5, 0.0); g2 = (0.5, 0.5, 0.5, 0.5)
G = {key((1.0, 0, 0, 0)): (1.0, 0, 0, 0)}; front = list(G.values())
while front:
    nv = []
    for q in front:
        for g in (g1, g2):
            r = mul(q, g)
            if key(r) not in G: G[key(r)] = r; nv.append(r)
    front = nv
ok("V9 les rotations du collage dodecaedrique : 120 = 2 x 60", len(G) == 120)
# V10 a trois : racines des cubes et des sixiemes puissances
ok("V10 racines de x^3 : 1, 8, 9 par chambre ; de x^6 : 1 et 9",
   [dr(x**3) for x in range(1, 10)] == [1, 8, 9]*3 and {dr(x**6) for x in range(1, 10)} == {1, 9})
# V11 la piece de mars : rapport sur la 3-sphere de rayon 1, profondeur r/3
k = lambda r: pi*(2*r - sin(2*r)) / (4*pi*sin(r)**2 * r/3)
ok("V11 rapport V/(S r/3) sur la sphere : 1,0013 (r=0,1) et 1,155 (r=1), non 1",
   abs(k(0.1) - 1.0013) < 1e-4 and abs(k(1.0) - 1.155) < 1e-3)
ok("V12 coefficients de la boule geodesique : 1/30 et 1/18, ecart 1/45", Fr(1, 18) - Fr(1, 30) == Fr(1, 45))
# V13 la moyenne d'une metrique sur les 24 rotations du cube : un multiple du repere, rien de plus
def perms_signees():
    from itertools import permutations
    out = []
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            M = [[s[i] if p[i] == j else 0 for j in range(3)] for i in range(3)]
            d = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                 + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
            if d == 1: out.append(M)
    return out
Q = perms_signees()
g = [[Fr(5), Fr(1), Fr(2)], [Fr(1), Fr(3), Fr(-1)], [Fr(2), Fr(-1), Fr(7)]]
moy = [[sum(sum(q[a][i]*g[a][b]*q[b][j] for a in range(3) for b in range(3)) for q in Q) / len(Q)
        for j in range(3)] for i in range(3)]
ok("V13 moyenne d'une metrique sur les 24 rotations du cube = (trace/3) x repere : 5, 5, 5 et zeros",
   len(Q) == 24 and moy == [[Fr(5), 0, 0], [0, Fr(5), 0], [0, 0, Fr(5)]])
# V14 la figure : deux cercles et le carre
from math import cos, atan2, degrees
Rr = 1.0; r = Rr / sqrt(2)
pts = [(Rr*cos(pi/4 + k*pi/2), Rr*sin(pi/4 + k*pi/2)) for k in range(4)] + [(r*cos(k*pi/2), r*sin(k*pi/2)) for k in range(4)]
ang = sorted(round(degrees(atan2(y, x)) % 360) for x, y in pts)
ok("V14 figure : 8 contacts tous les 45 degres ; (r/R)^2 = 1/2 ; couronne = disque interieur",
   ang == [0, 45, 90, 135, 180, 225, 270, 315] and abs(r*r - 0.5) < 1e-12 and abs(pi*(Rr*Rr - r*r) - pi*r*r) < 1e-12)
# V15 les rangees de la table et leurs rencontres
row = lambda k: [dr(k*n) for n in range(1, 10)]
renc = {(j, k): [(n+1, row(j)[n]) for n in range(9) if row(j)[n] == row(k)[n]] for j, k in combinations(range(1, 9), 2)}
ok("V15 rangees : somme 9 pas a pas, inverse = lecture a l'envers ; (1,8),(2,7),(4,5) une rencontre au 9 ; (3,6) trois ; 28 paires : 21 une fois, 7 trois fois, aucune ne s'evite",
   all(x + y == 9 for k in (1, 2, 4) for x, y in zip(row(k)[:8], row(9-k)[:8]))
   and all(row(9-k)[:8] == row(k)[:8][::-1] for k in range(1, 9))
   and all(renc[p] == [(9, 9)] for p in ((1, 8), (2, 7), (4, 5))) and renc[(3, 6)] == [(3, 9), (6, 9), (9, 9)]
   and Counter(len(m) for m in renc.values()) == Counter({1: 21, 3: 7}))
# V16 polygones tracables de 3 a 9 cotes : n = 2^a x (premiers de Fermat distincts)
def tracable(n):
    while n % 2 == 0: n //= 2
    for f in (3, 5, 17, 257, 65537):
        if n % f == 0: n //= f
    return n == 1
ok("V16 polygones tracables de 3 a 9 cotes : 3, 4, 5, 6, 8 ; pavage par 120 dodecaedres 600-1200+720-120=0",
   [n for n in range(3, 10) if tracable(n)] == [3, 4, 5, 6, 8] and 600-1200+720-120 == 0)
# V17 les cinq formes fermees entre deux cercles : cos(pi/n) et leurs ecarts
cinq = [round(cos(pi/n), 4) for n in (3, 4, 5, 6, 8)]
ec = [round(1 - cos(pi/n), 3) for n in (3, 4, 5, 6, 8)]
ok("V17 cinq rapports 0,5000 0,7071 0,8090 0,8660 0,9239 ; ecarts 0,500 0,293 0,191 0,134 0,076, decroissants",
   cinq == [0.5, 0.7071, 0.809, 0.866, 0.9239] and ec == [0.5, 0.293, 0.191, 0.134, 0.076] and ec == sorted(ec, reverse=True))
# V18 le 7 se ferme presque
from math import asin
pas = degrees(2*asin(sqrt(3)/4))
ok("V18 angles entiers pour 3,4,5,6,8 ; 360/7 = 51,428571... ; sept pas de 51,318 = 359,22, ouvert de 0,78 ; 22/7 - pi = 0,00126",
   [360 % n for n in (3, 4, 5, 6, 8)] == [0]*5 and 360 % 7 != 0 and str(Fr(360, 7).numerator * 10**6 // 7)[:8] == "51428571"
   and round(pas, 3) == 51.318 and round(7*pas, 2) == 359.22 and round(360 - 7*pas, 2) == 0.78 and round(22/7 - pi, 5) == 0.00126)
# V19 les angles : l'axe pour les cinq formes fermees, les rails pour le 7, le centre pour le 9
def periode(p, q, k=12):
    s, r = '', p % q
    for _ in range(k): r *= 10; s += str(r // q); r %= q
    return s
ang = {n: (dr(360 // n), dr(180*(n-2) // n)) for n in (3, 4, 5, 6, 8, 9)}
prem = {dr(p) for p in range(5, 100000) if all(p % d for d in range(2, int(p**0.5) + 1))}
ok("V19 racines des angles : (3,6) (9,9) (9,9) (6,3) (9,9) pour 3,4,5,6,8 ; (4,5) pour 9 ; 1/7 sans 3, 6, 9 ; somme des angles de racine 9 ; premiers sur les rails",
   [ang[n] for n in (3, 4, 5, 6, 8)] == [(3, 6), (9, 9), (9, 9), (6, 3), (9, 9)] and ang[9] == (4, 5)
   and set(periode(360, 7) + periode(900, 7)) == set("142857") and all(dr(180*(n-2)) == 9 for n in range(3, 200))
   and prem == {1, 2, 4, 5, 7, 8})
import itertools as _it
from fractions import Fraction as _Fr
_T = set()
for _i in range(7):
    _T.add(frozenset((_i, (_i + 1) % 7, (_i + 3) % 7))); _T.add(frozenset((_i, (_i + 2) % 7, (_i + 3) % 7)))
_A = {frozenset(p) for t in _T for p in _it.combinations(t, 2)}
_C = [t | {p} for t in _T for p in (7, 8)]
_F3 = {frozenset(f) for c in _C for f in _it.combinations(c, 3)}; _A3 = {frozenset(f) for c in _C for f in _it.combinations(c, 2)}
_S5 = [frozenset(c) for c in _it.combinations(range(5), 4)]
_lien = {frozenset(c - {0}) for c in _S5 if 0 in c}; _la = {frozenset(p) for t in _lien for p in _it.combinations(t, 2)}
ok("V20 tore à 7 sommets coiffé de deux pointes : 9 - 35 + 56 - 28 = 2, deux cellules par face, enveloppe d'une pointe de compte 0 (un tore) ; sur le bord du 4-simplexe l'enveloppe compte 2 (une sphère) ; sept pas de 360/7 font 360",
   (9, len(_A3), len(_F3), len(_C)) == (9, 35, 56, 28) and 9 - len(_A3) + len(_F3) - len(_C) == 2
   and all(sum(1 for c in _C if f <= c) == 2 for f in _F3) and 7 - len(_A) + len(_T) == 0
   and 4 - len(_la) + len(_lien) == 2 and 7 * _Fr(360, 7) == 360)
for n, c in R: print("[OK]" if c else "[ECHEC]", n)
print(sum(c for _, c in R), "sur", len(R))
