# Vérifications de « La Cascade et la Cloche » v0.4 (R10 : assertions exécutées au build)
from math import comb, pi, sqrt, sin, cos, lgamma, log, exp
from fractions import Fraction
from itertools import product, combinations
from collections import Counter

N = 0
def ok(cond, nom):
    global N
    assert cond, nom
    N += 1

def dr(n):
    return 9 if (n % 9 == 0 and n) else n % 9

def cascade(s, pli=True):
    s = list(s)
    while len(s) > 1:
        s = [(dr(a + b) if pli else a + b) for a, b in zip(s, s[1:])]
    return s[0]

# 1. Cycloïde : longueur 8R, hauteur 2R, aire 3 pi R^2 (R = 1)
M = 200000
h = 2 * pi / M
L = sum(2 * abs(sin((i + 0.5) * h / 2)) * h for i in range(M))
A = sum((1 - cos((i + 0.5) * h)) ** 2 * h for i in range(M))
ok(abs(L - 8) < 1e-6, "arche 8R")
ok(abs(A - 3 * pi) < 1e-6, "aire 3 pi R2")

# 3. Pendule circulaire : allongement theta^2/16 (moyenne arithmético-géométrique)
def agm(a, b):
    for _ in range(40):
        a, b = (a + b) / 2, sqrt(a * b)
    return a
th = 0.1
ok(abs((1 / agm(1, cos(th / 2)) - 1) - 0.00063) < 0.00001, "theta2/16 a 0,1 rad")

# 3. Cycloïde isochrone : a = g s / 4R, même période pour deux hauteurs de lâcher
def periode(s0, g=9.80665, R=1.0, dt=1e-5):
    s, v, t = s0, 0.0, 0.0
    w2 = g / (4 * R)
    while True:
        v2 = v - w2 * s * dt
        s2 = s + v2 * dt
        t += dt
        if s > 0 >= s2:
            return 4 * (t - dt * s2 / (s2 - s))
        s, v = s2, v2
ok(abs(periode(0.2) - periode(3.5)) < 1e-4, "isochronie")

# 4. Le reçu : g / pi^2
ok(abs(9.80665 / pi ** 2 - 0.9936) < 0.0001, "g/pi2")

# 5. Ligne 8 et fibres
l8 = [comb(8, k) for k in range(9)]
ok(l8 == [1, 8, 28, 56, 70, 56, 28, 8, 1] and sum(l8) == 256, "ligne 8")
ok(sum(Fraction(c, 256) for c in l8) == 1, "fibres somme 1")
n = 10000
r = exp(lgamma(2 * n + 1) - 2 * lgamma(n + 1) - 2 * n * log(2)) * sqrt(pi * n)
ok(abs(r - 0.99999) < 0.00001, "Wallis")

# 6. Cercle de six
cyc = [dr(2 ** k) for k in range(60)]
ok(cyc[:6] == [1, 2, 4, 8, 7, 5] and all(cyc[k] == cyc[k % 6] for k in range(60)), "periode 6")
ok(not set(cyc) & {3, 6, 9}, "jamais l'axe")
ok([dr(2 ** k) for k in range(16, 21)] == [7, 5, 1, 2, 4], "64k a 1M")
ok(all(dr(2 ** k) + dr(2 ** (k + 3)) == 9 for k in range(60)), "pli par 8")

# 7. Miroir 46 / 64
ok(dr(46) == dr(64) == 1 and 46 == 45 + 1 and 64 == 7 * 9 + 1 == 2 ** 6, "46 et 64")
ok(46 + 64 == 11 * 10 and 64 - 46 == 9 * 2, "loi des miroirs")
ok(694 - 496 == 2 * 9 * 11 and 496 == 31 * 32 // 2, "496")
ok(Fraction(46, 64) == Fraction(23, 32) and dr(23) == dr(32) == 5, "23/32")

# 8. Cascade 1 -> 9
ok(sum((k + 1) * l8[k] for k in range(9)) == 1280 and dr(1280) == 2, "1280")
ok(Fraction(1280, 256) == 5, "centre 5")
ok(cascade(range(1, 10)) == 2 and cascade(range(9, 0, -1)) == 2, "pointe 2 et retournement")

# 8 bis. Le bord restitue tout
def bord(s):
    s = list(s); b = [s[0]]
    while len(s) > 1:
        s = [dr(a + b_) for a, b_ in zip(s, s[1:])]
        b.append(s[0])
    return b
def restitue(b):
    return [dr(sum((1 if (j - i) % 2 == 0 else 8) * comb(j, i) * b[i] for i in range(j + 1))) for j in range(len(b))]
ok(bord([1, 6, 8, 1]) == [1, 7, 3, 8] and restitue([1, 7, 3, 8]) == [1, 6, 8, 1], "1681")
cnt = 0
for Lg in range(1, 6):
    for s in product(range(1, 10), repeat=Lg):
        assert restitue(bord(s)) == list(s)
        cnt += 1
ok(cnt == 66429, "bord sur 66 429 sequences")

# 9. XXXX -> 9 - X
ok(all(cascade([x] * 4) == (9 if x == 9 else 9 - x) for x in range(1, 10)), "XXXX")

# 10. Octet et axe
ok(sum((k + 1) * comb(7, k) for k in range(8)) == 576 == 24 ** 2 and dr(576) == 9, "octet")
def b3(n):
    p = 1
    while n:
        p *= n % 3 + 1; n //= 3
    return p
ok(all(sum(1 for k in range(n + 1) if comb(n, k) % 3) == b3(n) for n in range(201)), "fractale ternaire")
for e in range(2, 8):
    n = 3 ** e; t = n // 3
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    nz = {k: c % 9 for k, c in enumerate(row) if c % 9}
    assert nz == {0: 1, t: 3, 2 * t: 3, n: 1}
ok(True, "quatre positions jusqu'a la ligne 2187")

# 8 ter. Le losange (22 novembre 2026)
ok([cascade([1 if i == k else 0 for i in range(9)], pli=False) for k in range(9)] == l8, "le triangle est la cascade d'un 1 seul")
cnt = 0
for Lg in range(2, 6):
    for s in product(range(1, 10), repeat=Lg):
        assert cascade(s) == dr(cascade(s, pli=False))
        cnt += 1
ok(cnt == 66420 and cascade(range(1, 10), pli=False) == 1280, "plier a chaque palier ou a la pointe")
ok(sum(c * c for c in l8) == 12870 == comb(16, 8) and dr(12870) == 9, "losange de neuf positions")
ok(sum(comb(4, k) ** 2 for k in range(5)) == 70 == comb(8, 4), "losange de cinq positions")
ok(all(sum(comb(n, k) ** 2 for k in range(n + 1)) == comb(2 * n, n) for n in range(1, 33)), "losange = centre de la ligne double")
ok(11 ** 4 == 14641 and cascade([1, 4, 6, 4, 1], pli=False) == 70 and cascade([1, 4, 6, 4, 1]) == 7, "14641 passe dans la cascade donne 70")
def classes(n):
    c = Counter()
    for G in combinations(range(2 * n), n):
        G = set(G); x = 0; g = 0
        for i in range(2 * n):
            nx = x + (-1 if i in G else 1)
            if x < 0 or nx < 0:
                g += 1
            x = nx
        c[g // 2] += 1
    return c
for n in range(1, 9):
    c = classes(n)
    assert len(c) == n + 1 and set(c.values()) == {comb(2 * n, n) // (n + 1)} and comb(2 * n, n) % (n + 1) == 0
ok(classes(8)[0] == 1430 and 9 * 1430 == 12870, "neuf parts egales de 1430")

# 8 quater. Où loge le pi (27 novembre 2026)
def centre(n):  # centre de la ligne 2n sur son total, multiplié par sqrt(pi n)
    return float(Fraction(comb(2 * n, n), 4 ** n)) * sqrt(pi * n)
ok(abs(centre(4) - 0.9693) < 5e-5 and abs(centre(8) - 0.9845) < 5e-5
   and abs(centre(100) - 0.99875) < 5e-6 and abs(centre(10000) - 0.9999875) < 5e-8, "tableau du centre")
ok(all(centre(n) < centre(n + 1) < 1 for n in range(1, 300)), "par en dessous, ligne apres ligne (1 a 300)")
ok(256 ** 2 == 65536 == 4 ** 8 == sum(comb(16, k) for k in range(17))
   and Fraction(12870, 65536) == Fraction(6435, 32768), "deux facons de carrer")
ok(all(Fraction(sum(comb(n, k) ** 2 for k in range(n + 1)), (2 ** n) ** 2) == Fraction(comb(2 * n, n), 4 ** n)
       for n in range(1, 33)), "losange sur carre du total = centre de la ligne double")
G = [[l8[i] * l8[j] for j in range(9)] for i in range(9)]
ok(sum(map(sum, G)) == 65536 and sum(G[i][i] for i in range(9)) == 12870, "le losange est la diagonale du carre")
ok([sum(G[i][m - i] for i in range(9) if 0 <= m - i <= 8) for m in range(17)] == [comb(16, m) for m in range(17)]
   and [comb(16, m) for m in range(5)] == [1, 16, 120, 560, 1820], "le carre lu de biais ecrit la ligne 16")
hh = 1e-3
aire = sum(exp(-(k * hh) ** 2) for k in range(-10000, 10001)) * hh
ok(abs(aire * aire - pi) < 1e-12 and abs(aire - sqrt(pi)) < 1e-12, "aire au carre = pi")
ok(all(abs(exp(-x * x) * exp(-y * y) - exp(-1.69)) < 1e-15
       for x, y in [(1.3, 0.0), (0.0, 1.3), (0.5, 1.2), (1.2, 0.5), (-0.5, -1.2)]), "meme cercle, meme hauteur")
w = 1.0
for k in range(1, 200001):
    w *= (2 * k) * (2 * k) / ((2 * k - 1) * (2 * k + 1))
ok(abs(2 * w - 3.14159) < 5e-6, "produit de Wallis")

if __name__ == "__main__":
    print("verifications :", N, "zero echec")
