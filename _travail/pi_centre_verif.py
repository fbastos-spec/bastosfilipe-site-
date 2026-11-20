# -*- coding: utf-8 -*-
# π part du centre : le cercle dans le triangle de Pascal. Vérifications. Python 3, bibliothèque standard seule.
import sys
from math import comb, pi
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
getcontext().prec = 40
PI = D('3.14159265358979323846264338327950288')
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
den = [comb(2 * n + 2, 3) for n in range(1, 10)]
ok("V1 un nombre sur deux de la troisième diagonale : 4, 20, 56, 120, 220, 364, 560, 816, 1140", den == [4, 20, 56, 120, 220, 364, 560, 816, 1140])
ok("V2 les deux écritures sont la même : (2/3) / C(2n + 2, 3) = 4 / (2n (2n + 1)(2n + 2)), pour n de 1 à 2 000",
   all(F(2, 3) / comb(2 * n + 2, 3) == F(4, 2 * n * (2 * n + 1) * (2 * n + 2)) for n in range(1, 2001)))
s = D(3); S = {}
for k in range(1, 1939):
    s += D(2) / D(3) * D((-1) ** (k + 1)) / D(comb(2 * k + 2, 3))
    if k in (1, 2, 3, 100, 1000, 1938): S[k] = s
ok("V3 la somme : 3,1667 au premier terme, 3,1333 au deuxième, 3,1452 au troisième ; à 1 938 termes l'écart à π est 3,4 × 10^-11, dix décimales tenues",
   (round(float(S[1]), 4), round(float(S[2]), 4), round(float(S[3]), 4)) == (3.1667, 3.1333, 3.1452) and abs(float(abs(S[1938] - PI)) / 3.43e-11 - 1) < 0.01
   and str(S[1938])[:12] == '3.1415926535')
ok("V4 l'écart après k termes suit 1 / (4 k³) : écart × k³ = 0,243 à 100 termes, 0,2493 à 1 000, 0,2496 à 1 938",
   all(abs(float(abs(S[k] - PI)) * k ** 3 - v) < 0.0006 for k, v in ((100, 0.2426), (1000, 0.2493), (1938, 0.2496))))
ok("V5 les triplets voisins : 2 × 3 × 4 = 24, 4 × 5 × 6 = 120, 6 × 7 × 8 = 336, 8 × 9 × 10 = 720 ; premier terme 4/24 = 1/6, d'où 3 + 1/6 = 19/6",
   [2 * n * (2 * n + 1) * (2 * n + 2) for n in range(1, 5)] == [24, 120, 336, 720] and F(4, 24) == F(1, 6) and 3 + F(1, 6) == F(19, 6) and F(2, 3) * F(1, 4) == F(1, 6))
pyr = [sum(k * k for k in range(1, n + 1)) for n in range(1, 2001)]
ok("V6 les nombres dorés sont quatre fois les pyramides à base carrée 1, 5, 14, 30, 55 (sommes des carrés), pour n de 1 à 2 000",
   pyr[:5] == [1, 5, 14, 30, 55] and all(comb(2 * n + 2, 3) == 4 * pyr[n - 1] for n in range(1, 2001)))
t = sum(F((-1) ** (n + 1), pyr[n - 1]) for n in range(1, 2001))
ok("V7 π = 3 + 1/6 × (1 − 1/5 + 1/14 − 1/30 + 1/55 − …) : à 2 000 termes, l'écart est sous 10^-10 ; la parenthèse tend vers 6 (π − 3) = 0,84956",
   abs(float(3 + t / 6) - pi) < 1e-10 and round(6 * (pi - 3), 5) == 0.84956)
ok("V8 chaque triplet est un cube moins lui-même : 3³ − 3 = 24, 5³ − 5 = 120, 7³ − 7 = 336 ; pour tout impair m de 3 à 4 001, (m − 1) m (m + 1) = m³ − m",
   [m ** 3 - m for m in (3, 5, 7)] == [24, 120, 336] and all((m - 1) * m * (m + 1) == m ** 3 - m for m in range(3, 4002, 2)) and 3 * 8 == 24)
W = {n: n * (comb(2 * n, n) / 4 ** n) ** 2 for n in (10, 100, 1000, 10000)}
ok("V9 la colonne du centre : n × (part du centre de la ligne 2n)² = 0,31045 ; 0,31752 ; 0,31823 ; 0,318302 pour n = 10, 100, 1 000, 10 000, et 1/π = 0,318310",
   [round(W[n], 5) for n in (10, 100, 1000)] == [0.31045, 0.31752, 0.31823] and round(W[10000], 6) == 0.318302 and round(1 / pi, 6) == 0.31831
   and W[10] < W[100] < W[1000] < W[10000] < 1 / pi)
ok("V10 le centre des lignes paires : 1, 2, 6, 20, 70, 252 ; chaque nombre du triangle est la somme des deux au-dessus, à partir d'un seul 1",
   [comb(2 * n, n) for n in range(6)] == [1, 2, 6, 20, 70, 252] and all(comb(n, k) == comb(n - 1, k - 1) + comb(n - 1, k) for n in range(2, 60) for k in range(1, n)))
tet = sum(F(1, comb(k + 2, 3)) for k in range(1, 3000))
alt = sum(F((-1) ** (n + 1), comb(2 * n + 2, 3)) for n in range(1, 2001))
ok("V11 la somme de tous les inverses de la troisième diagonale, sans alternance, ferme sur 3/2 (écart sous 10^-6 à 3 000 termes) ; un terme sur deux, en alternance, vaut 3/2 × (π − 3) = 0,21239", abs(float(tet) - 1.5) < 1e-6 and abs(float(alt) - 1.5 * (pi - 3)) < 1e-9 and round(1.5 * (pi - 3), 5) == 0.21239)
if len(sys.argv) > 1:
    tx = open(sys.argv[1], encoding='utf-8').read()
    ok("V12 typographie de la source : aucun tiret long ni moyen", '—' not in tx and '–' not in tx)
for nom, c in R: print(("conforme : " if c else "ÉCHEC : ") + nom)
assert all(c for _, c in R); print(len(R), "contrôles, tous conformes")
