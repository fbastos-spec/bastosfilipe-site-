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
def _chantiers():
    import itertools, random
    from fractions import Fraction as F_
    from collections import Counter as Cn
    Cb = itertools.combinations
    cle = lambda s: repr(sorted(s, key=repr))
    def bord4(): return [frozenset(c) for c in Cb(range(5), 4)]
    def c16(): return [frozenset((i, s) for i, s in enumerate(sg)) for sg in itertools.product((1, -1), repeat=4)]
    def pair(p): return sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0
    def icos_f():
        phi = (1 + 5 ** .5) / 2; V = set()
        for i in range(4):
            for s in (1, -1):
                w = [0, 0, 0, 0]; w[i] = s; V.add(tuple(w))
        for sg in itertools.product((.5, -.5), repeat=4): V.add(sg)
        base = (0, .5, phi / 2, 1 / (2 * phi))
        for p in itertools.permutations(range(4)):
            if not pair(p): continue
            for sg in itertools.product((1, -1), repeat=3):
                b = [base[0], base[1] * sg[0], base[2] * sg[1], base[3] * sg[2]]; w = [0] * 4
                for k in range(4): w[p[k]] = b[k]
                V.add(tuple(w))
        return sorted({tuple(round(x, 9) + 0.0 for x in w) for w in V})
    def c600():
        V = icos_f(); d = lambda a, b: sum((x - y) ** 2 for x, y in zip(a, b))
        m = min(d(V[0], w) for w in V[1:]); adj = {i: set() for i in range(len(V))}
        for i, j in Cb(range(len(V)), 2):
            if abs(d(V[i], V[j]) - m) < 1e-6: adj[i].add(j); adj[j].add(i)
        T = set()
        for i in adj:
            for j in adj[i]:
                if j < i: continue
                for k in adj[i] & adj[j]:
                    if k < j: continue
                    for l in adj[i] & adj[j] & adj[k]:
                        if l > k: T.add(frozenset((i, j, k, l)))
        return sorted(T, key=sorted), V
    def tore7():
        T = []
        for i in range(7): T.append((i, (i + 1) % 7, (i + 3) % 7)); T.append((i, (i + 2) % 7, (i + 3) % 7))
        return [tuple(sorted(t)) for t in T]
    def produit(surf, n=3):
        cells = []
        for (a, b, c) in surf:
            for i in range(n):
                j = (i + 1) % n
                cells += [frozenset(((a, i), (b, i), (c, i), (c, j))), frozenset(((a, i), (b, i), (b, j), (c, j))), frozenset(((a, i), (a, j), (b, j), (c, j)))]
        return cells
    def faces(cells, k): return {frozenset(f) for c in cells for f in Cb(sorted(c, key=repr), k)}
    def comptes(cells): return len(faces(cells, 1)), len(faces(cells, 2)), len(faces(cells, 3)), len(cells)
    def surface(tris):
        E = Cn(frozenset(e) for t in tris for e in Cb(sorted(t, key=repr), 2))
        if any(x != 2 for x in E.values()): return None
        adj = {}
        for t in tris:
            for e in Cb(sorted(t, key=repr), 2): adj.setdefault(frozenset(e), []).append(t)
        t0 = next(iter(tris)); seen = {t0}; q = [t0]
        while q:
            t = q.pop()
            for e in Cb(sorted(t, key=repr), 2):
                for u in adj[frozenset(e)]:
                    if u not in seen: seen.add(u); q.append(u)
        if len(seen) != len(tris): return None
        Vs = {x for t in tris for x in t}
        for x in Vs:
            nb = {}
            for t in tris:
                if x in t:
                    a, b = [y for y in t if y != x]; nb.setdefault(a, []).append(b); nb.setdefault(b, []).append(a)
            if any(len(z) != 2 for z in nb.values()): return None
            s0 = next(iter(nb)); s = {s0}; q = [s0]
            while q:
                y = q.pop()
                for z in nb[y]:
                    if z not in s: s.add(z); q.append(z)
            if len(s) != len(nb): return None
        return len(Vs) - len(E) + len(tris)
    def forme_reelle(cells):
        Fc = Cn(frozenset(f) for c in cells for f in Cb(sorted(c, key=repr), 3))
        if any(x != 2 for x in Fc.values()): return False
        return all(surface([frozenset(c - {x}) for c in cells if x in c]) == 2 for x in {y for c in cells for y in c})
    def rang(M):
        M = [[F_(x) for x in r] for r in M]; r = 0; nc = len(M[0]) if M else 0
        for col in range(nc):
            piv = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
            if piv is None: continue
            M[r], M[piv] = M[piv], M[r]; pr = M[r]; pv = pr[col]
            for i in range(r + 1, len(M)):
                if M[i][col] != 0:
                    f = M[i][col] / pv; ri = M[i]
                    for j in range(col, nc):
                        if pr[j] != 0: ri[j] -= f * pr[j]
            r += 1
            if r == len(M): break
        return r
    def boucles(cells):
        Vs = sorted(faces(cells, 1), key=cle); Es = sorted(faces(cells, 2), key=cle); Fs = sorted(faces(cells, 3), key=cle)
        ei = {e: i for i, e in enumerate(Es)}; M = [[0] * len(Fs) for _ in Es]
        for j, f in enumerate(Fs):
            a, b, c = sorted(f, key=repr)
            M[ei[frozenset((b, c))]][j] = 1; M[ei[frozenset((a, c))]][j] = -1; M[ei[frozenset((a, b))]][j] = 1
        return len(Es) - (len(Vs) - 1) - rang(M)
    def valide(P, Pv, Pe, Pf, c):
        sh = [frozenset(f) for f in Cb(sorted(c, key=repr), 3) if frozenset(f) in Pf]; k = len(sh)
        if k == 0: return 0 if not P else None
        if k == 1:
            (x,) = c - sh[0]; return 1 if x not in Pv else None
        if k == 2: return 2 if frozenset(c - (sh[0] & sh[1])) not in Pe else None
        return k
    def derouler(cells, ordre=None, seed=0, verif=True):
        rnd = random.Random(seed); P = []; Pv = set(); Pe = set(); Pf = Cn(); types = []; reste = set(cells); eu = []
        def ajoute(c, t):
            P.append(c); reste.discard(c); types.append(t); Pv.update(c)
            for e in Cb(sorted(c, key=repr), 2): Pe.add(frozenset(e))
            for f in Cb(sorted(c, key=repr), 3): Pf[frozenset(f)] += 1
            if verif and reste: eu.append(surface([f for f, x in Pf.items() if x == 1]))
        if ordre:
            for c in ordre:
                t = valide(P, Pv, Pe, Pf, c)
                if t is None: return P, types, eu, False
                ajoute(c, t)
            return P, types, eu, True
        ajoute(rnd.choice(sorted(cells, key=cle)), 0)
        while reste:
            front = {f for f, x in Pf.items() if x == 1}; cand = []
            for c in reste:
                if any(frozenset(f) in front for f in Cb(sorted(c, key=repr), 3)):
                    t = valide(P, Pv, Pe, Pf, c)
                    if t is not None: cand.append((c, t))
            if not cand: return P, types, eu, False
            cand.sort(key=lambda x: cle(x[0])); c, t = rnd.choice(cand); ajoute(c, t)
        return P, types, eu, True
    def ligne(cells, V):
        d = (0.31, 0.57, 0.73, 0.19); x0 = (0.001, 0.002, -0.003, 0.0015); L = []
        for c in cells:
            pts = [V[i] for i in sorted(c)]; n = [sum(p[k] for p in pts) / 4 for k in range(4)]
            h = sum(n[k] * pts[0][k] for k in range(4)); L.append(((h - sum(n[k] * x0[k] for k in range(4))) / sum(n[k] * d[k] for k in range(4)), c))
        return [c for t, c in sorted([x for x in L if x[0] > 0], key=lambda x: x[0])] + [c for t, c in sorted([x for x in L if x[0] < 0], key=lambda x: x[0])]
    def bilan(types): return tuple(Cn(types)[k] for k in range(5))
    T600, V600 = c600(); SxC = produit([tuple(sorted(c)) for c in Cb(range(4), 3)]); TxC = produit(tore7())
    ok("V21 sphère × cercle et tore × cercle : formes réelles, comptes 12 - 48 + 72 - 36 = 0 et 21 - 147 + 252 - 126 = 0, une boucle qui résiste et trois ; aucune sur le bord du 4-simplexe ni sur les 16 cellules",
       forme_reelle(SxC) and forme_reelle(TxC) and comptes(SxC) == (12, 48, 72, 36) and comptes(TxC) == (21, 147, 252, 126)
       and boucles(SxC) == 1 and boucles(TxC) == 3 and boucles(bord4()) == 0 and boucles(c16()) == 0)
    r4 = [derouler(bord4(), seed=s) for s in range(200)]; r16 = [derouler(c16(), seed=s) for s in range(200)]; r600 = derouler(T600, ordre=ligne(T600, V600))
    def attendu(cells):
        a, e, f, c = comptes(cells); return (1, a - 4, e - 3 * a + 6, a - 4, 1)
    ok("V22 déroulés complets : bilans 1,1,1,1,1 (4-simplexe), 1,4,6,4,1 (16 cellules), 1,116,366,116,1 (600 cellules) ; un seul bilan pour 200 ordres ; chaque enveloppe compte 2 ; bilan = (1, pointes - 4, arêtes - 3 × pointes + 6, pointes - 4, 1)",
       all(r[3] and bilan(r[1]) == (1, 1, 1, 1, 1) and set(r[2]) <= {2} for r in r4)
       and all(r[3] and bilan(r[1]) == (1, 4, 6, 4, 1) and set(r[2]) == {2} for r in r16)
       and r600[3] and bilan(r600[1]) == (1, 116, 366, 116, 1) and set(r600[2]) == {2}
       and attendu(bord4()) == (1, 1, 1, 1, 1) and attendu(c16()) == (1, 4, 6, 4, 1) and attendu(T600) == (1, 116, 366, 116, 1))
    rs = [derouler(SxC, seed=s) for s in range(300)]; rt = [derouler(TxC, seed=s) for s in range(300)]
    ms, mt = max(len(r[0]) for r in rs), max(len(r[0]) for r in rt)
    ok(f"V23 blocage : sur 300 déroulés tirés au sort, aucun n'aboutit sur la sphère × cercle (au plus loin {ms} cellules sur 36) ni sur le tore × cercle (au plus loin {mt} sur 126) ; jusqu'au blocage chaque enveloppe compte 2",
       not any(r[3] for r in rs + rt) and ms < 36 and mt < 126 and all(set(r[2]) <= {2} for r in rs + rt))
    class Q5:
        __slots__ = ('a', 'b')
        def __init__(s, a, b=0): s.a = F_(a); s.b = F_(b)
        def __add__(s, o): return Q5(s.a + o.a, s.b + o.b)
        def __sub__(s, o): return Q5(s.a - o.a, s.b - o.b)
        def __mul__(s, o): return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)
        def __neg__(s): return Q5(-s.a, -s.b)
        def __eq__(s, o): return s.a == o.a and s.b == o.b
        def __hash__(s): return hash((s.a, s.b))
        def f(s): return float(s.a) + float(s.b) * 5 ** .5
    Z = Q5(0); H = Q5(F_(1, 2)); PH = Q5(F_(1, 4), F_(1, 4)); IP = Q5(F_(-1, 4), F_(1, 4))
    def qm(p, q):
        a, b, c, d = p; e, f, g, h = q
        return (a*e - b*f - c*g - d*h, a*f + b*e + c*h - d*g, a*g - b*h + c*e + d*f, a*h + b*g - c*f + d*e)
    G = set()
    for i in range(4):
        for s in (Q5(1), Q5(-1)):
            w = [Z] * 4; w[i] = s; G.add(tuple(w))
    for sg in itertools.product((1, -1), repeat=4): G.add(tuple(H if x == 1 else -H for x in sg))
    base = (Z, H, PH, IP)
    for p in itertools.permutations(range(4)):
        if not pair(p): continue
        for sg in itertools.product((1, -1), repeat=3):
            b = [base[0]] + [base[k + 1] if sg[k] == 1 else -base[k + 1] for k in range(3)]; w = [None] * 4
            for k in range(4): w[p[k]] = b[k]
            G.add(tuple(w))
    G = list(G); S = set(G); UN = (Q5(1), Z, Z, Z); inv = lambda g: (g[0], -g[1], -g[2], -g[3])
    prod = {(a, b): qm(a, b) for a in G for b in G}
    ok("V24 les 120 tours, en écriture exacte : ils sont 120, de grandeur 1, se composent sans sortir des 120 ; aucun tour autre que le tour nul ne laisse une position à sa place ; d'une position on atteint les 120",
       len(G) == 120 and all(sum((x * x for x in g), Z) == Q5(1) for g in G) and all(p in S for p in prod.values())
       and all(prod[(g, x)] != x for g in G if g != UN for x in G) and len({prod[(g, UN)] for g in G}) == 120)
    accord = sum(1 for a in G for b in G if prod[(a, b)] == prod[(b, a)]); centre = [g for g in G if all(prod[(g, h)] == prod[(h, g)] for h in G)]
    K = {qm(prod[(a, b)], qm(inv(a), inv(b))) for a in G for b in G}; sub = set(K)
    while True:
        new = {prod[(a, b)] for a in sub for b in K} | sub
        if len(new) == len(sub): break
        sub = new
    ok(f"V25 le registre garde l'ordre : {accord} paires sur 14400 s'accordent dans les deux ordres (9 × 120) ; deux tours seulement s'accordent avec tous, les deux pôles ; les écarts d'ordre redonnent les 120 tours",
       accord == 1080 == 9 * 120 and len(centre) == 2 and UN in centre and tuple(-x for x in UN) in centre and len(sub) == 120)
    def retour(g):
        x = g; n = 1
        while x != UN: x = prod[(x, g)]; n += 1
        return n
    haut = sorted(Cn(g[0] for g in G).items(), key=lambda x: -x[0].f()); tailles = [n for h, n in haut]
    fam = [{g for g in G if g[0] == h} for h, n in haut]
    ok("V26 neuf enveloppes d'un pôle à l'autre : 1, 12, 20, 12, 30, 12, 20, 12, 1 ; chacune est une seule famille de tours (retours en 1, 10, 6, 5, 4, 10, 3, 5, 2 fois), stable quand on la lit depuis un autre tour",
       tailles == [1, 12, 20, 12, 30, 12, 20, 12, 1] and [sorted({retour(g) for g in f})[0] for f in fam] == [1, 10, 6, 5, 4, 10, 3, 5, 2]
       and all(len({retour(g) for g in f}) == 1 for f in fam)
       and all({prod[(prod[(x, g)], inv(x))] for x in G} == f for f in fam for g in [next(iter(f))]))
_chantiers()
for n, c in R: print("[OK]" if c else "[ECHEC]", n)
print(sum(c for _, c in R), "sur", len(R))
