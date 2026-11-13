# -*- coding: utf-8 -*-
# Erdős sur l'échiquier : vérifications. Bibliothèque standard seule.
import sys
from math import isqrt
from itertools import combinations
from collections import Counter
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
def ecritures(k): return [(a, b) for a in range(0, isqrt(k) + 1) for b in range(a, isqrt(k) + 1) if a * a + b * b == k]
def octogones(k): return len([e for e in ecritures(k) if 0 < e[0] != e[1]])
def voisins(k): return sum(4 if (a == 0 or a == b) else 8 for a, b in ecritures(k))

ligne = Counter(abs(a - b) for a, b in combinations(range(1, 9), 2))
ok("V1 une ligne de 8 porte 28 paires, par distance 7, 6, 5, 4, 3, 2, 1 ; 28 = 1 + 2 + … + 7",
   sum(ligne.values()) == 28 == sum(range(1, 8)) and [ligne[d] for d in range(1, 8)] == [7, 6, 5, 4, 3, 2, 1])
ok("V2 le carré a 4 sommets, l'octogone 8 ; le côté de la grille donne 4 voisins, une écriture en deux carrés différents en donne 8",
   voisins(1) == 4 and voisins(5) == 8 and all(len({(s * x, t * y) for s in (1, -1) for t in (1, -1) for x, y in ((a, b), (b, a))}) == 8 for a in range(1, 30) for b in range(a + 1, 30)))
ok("V3 rotors : 5, 13, 17, 29 s'écrivent chacun d'une seule façon ; 3² + 4² = 5², 5² + 12² = 13², 8² + 15² = 17², 20² + 21² = 29²",
   all(octogones(p) == 1 for p in (5, 13, 17, 29)) and 9 + 16 == 25 and 25 + 144 == 169 and 64 + 225 == 289 and 400 + 441 == 841)
ok("V4 chaque rotor double : 1 octogone pour 5, 2 pour 65, 4 pour 1105, 8 pour 32045 ; voisins 8, 16, 32, 64",
   [octogones(k) for k in (5, 65, 1105, 32045)] == [1, 2, 4, 8] and [voisins(k) for k in (5, 65, 1105, 32045)] == [8, 16, 32, 64]
   and 65 == 5 * 13 and 1105 == 5 * 13 * 17 and 32045 == 5 * 13 * 17 * 29)
ok("V5 65 est le plus petit nombre à deux écritures en carrés différents : 1² + 8² et 4² + 7² ; les autres paires inverses donnent 53, 45, 41, à une seule écriture",
   min(k for k in range(1, 500) if octogones(k) >= 2) == 65 and ecritures(65) == [(1, 8), (4, 7)]
   and [(a * a + (9 - a) ** 2, octogones(a * a + (9 - a) ** 2)) for a in (2, 3, 4)] == [(53, 1), (45, 1), (41, 1)])
P = [(x, y) for x in range(1, 9) for y in range(1, 9)]
D = Counter((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 for a, b in combinations(P, 2))
t = sum(1 for a, b in combinations(P, 2) if a[0] == b[0] or a[1] == b[1])
f = sum(1 for a, b in combinations(P, 2) if abs(a[0] - b[0]) == abs(a[1] - b[1]))
ok("V6 l'échiquier : 64 cases, 2016 paires = 72 × 28 ; tour 448 = 16 × 28 ; fou 280 = 10 × 28 ; dame 728 = 26 × 28 ; cavalier 168 = 6 × 28 ; case voisine 112 = 4 × 28",
   len(P) == 64 and sum(D.values()) == 2016 == 72 * 28 and t == 448 == 16 * 28 and f == 280 == 10 * 28 and t + f == 728 == 26 * 28 and D[5] == 168 == 6 * 28 and D[1] == 112 == 4 * 28)
ok("V7 à une seule distance, le saut du cavalier est la plus fréquente de l'échiquier ; le centre est à 4,5 sur les deux axes",
   max(D, key=D.get) == 5 and sorted(D.values())[-2] < 168 and sum(range(1, 9)) * 2 == 9 * 8)
def comptes(n):
    Q = [(x, y) for x in range(n) for y in range(n)]
    C = Counter((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 for a, b in combinations(Q, 2)); return C[1], C[5]
ok("V8 sur un damier de n cases de côté : voisines 2n(n − 1), cavalier 4(n − 1)(n − 2) ; égalité à n = 4 (24 et 24), le cavalier devant dès n = 5",
   all(comptes(n) == (2 * n * (n - 1), 4 * (n - 1) * (n - 2)) for n in range(3, 13)) and comptes(4) == (24, 24) and comptes(5) == (40, 48))
def disque(R_, tri):
    if not tri:
        Q = [(x, y) for x in range(-R_, R_ + 1) for y in range(-R_, R_ + 1) if x * x + y * y <= R_ * R_]; S = set(Q)
        return len(Q), sum(((x + 1, y) in S) + ((x, y + 1) in S) for x, y in Q)
    Q = [(a, b) for a in range(-2 * R_, 2 * R_ + 1) for b in range(-2 * R_, 2 * R_ + 1) if a * a + a * b + b * b <= R_ * R_]; S = set(Q)
    return len(Q), sum(((a + 1, b) in S) + ((a, b + 1) in S) + ((a - 1, b + 1) in S) for a, b in Q)
n4, u4 = disque(60, False); n6, u6 = disque(60, True)
ok("V9 au côté de la grille : la grille carrée fait près de 2 paires par point, la grille de triangles près de 3 (disque de rayon 60)",
   1.95 < u4 / n4 < 2 and 2.93 < u6 / n6 < 3)
if len(sys.argv) > 1:
    src = open(sys.argv[1], encoding="utf-8").read()
    ok("V10 aucun tiret cadratin ni demi-cadratin dans la source", "—" not in src and "–" not in src)
for n, c in R: print(("OK   " if c else "FAUX ") + n)
print(f"{sum(c for _, c in R)} contrôles sur {len(R)} conformes")
sys.exit(0 if all(c for _, c in R) else 1)
