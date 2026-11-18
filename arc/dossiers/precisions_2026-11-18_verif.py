# -*- coding: utf-8 -*-
# Contrôles des précisions du 18 novembre 2026 portées en fin de six dossiers. Python 3, bibliothèque standard seule.
from math import comb
from fractions import Fraction as F
R = []
def ok(nom, cond): R.append((nom, bool(cond))); print(("conforme : " if cond else "ÉCHEC : ") + nom)
dr = lambda n: 1 + (n - 1) % 9
# --- Les nombres de Heegner dans le code, 3.1
def code(n):
    d = []
    while n > 0:
        r = dr(n); d.append(r); n = (n - r) // 9
    return tuple(reversed(d))
W = {n: code(n) for n in range(10, 164)}; inv = {v: k for k, v in W.items()}
pal = [n for n, w in W.items() if w == w[::-1]]
paires = [(n, inv[w[::-1]]) for n, w in W.items() if w[::-1] in inv and inv[w[::-1]] > n]
fav = comb(len(paires), 2) * len(pal); tot = comb(154, 5)
ok(f"Heegner 3.1 : de 10 à 163, {len(paires)} paires miroirs disjointes et {len(pal)} palindromes ; {fav} ensembles sur {tot}, soit {fav/tot*1e6:.1f} par million, un sur {round(tot/fav)}",
   len(paires) == 36 and len(pal) == 18 and len({x for p in paires for x in p}) == 72 and fav == 11340 and tot == 675993780 and round(fav / tot * 1e6, 1) == 16.8
   and [code(n) for n in (11, 19, 43, 67, 163)] == [(1, 2), (2, 1), (4, 7), (7, 4), (1, 9, 1)])
# --- Modulo, 4.2.3 : le pas de la réciproque
def premiers(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
def fac(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def diviseurs_du_carre(f):
    D = [1]
    for p, e in f.items(): D = [d * p ** k for d in D for k in range(2 * e + 1)]
    return D
P = [p for p in premiers(200000) if p % 840 in (1, 121, 169, 289, 361, 529)]
accord = ouvertes = 0
for p in P:
    x = (p + 3) // 4; N = p * x; f = fac(x); f[p] = f.get(p, 0) + 1
    crit = any(q % 3 == 2 for q in fac(x)); us = [u for u in diviseurs_du_carre(f) if u % 3 == 2]
    if us:
        u = us[0]; v = N * N // u; y = (u + N) // 3; z = (v + N) // 3
        assert (u + N) % 3 == 0 and (v + N) % 3 == 0 and F(1, x) + F(1, y) + F(1, z) == F(4, p)
    accord += crit == bool(us); ouvertes += crit
ok(f"Modulo 4.2.3 : 3/N = 1/y + 1/z équivaut à (3y − N)(3z − N) = N² ; un diviseur de N² de reste 2 par 3 existe si et seulement si x a un facteur premier du rail 2, 5, 8 : {accord} accords sur {len(P)}, {ouvertes} portes ouvertes, {len(P)-ouvertes} fermées",
   len(P) == 511 and accord == 511 and ouvertes == 172)
# --- The End of the Integral Calculus Illusion, sections 2 et 14
ok("Intégrale 2 : root(mk) + root((9 − m)k) vaut 9, ou 18 quand les deux produits sont des multiples de 9 ; la racine de la somme est 9 dans tous les cas (m et k de 1 à 8, puis k jusqu'à 200)",
   all(dr(m * k) + dr((9 - m) * k) in (9, 18) and dr(dr(m * k) + dr((9 - m) * k)) == 9 for m in range(1, 9) for k in range(1, 201))
   and {dr(m * k) + dr((9 - m) * k) for m in range(1, 9) for k in range(1, 9)} == {9, 18})
# le U de 7 cases : socle [0,3]×[0,1], bras [0,1]×[1,3] et [2,3]×[1,3] ; un point qui voit chaque face est à gauche de x = 1 et à droite de x = 2
U = [(0, 0), (3, 0), (3, 3), (2, 3), (2, 1), (1, 1), (1, 3), (0, 3)]
def dans_le_noyau(px, py, U=U):
    for (x1, y1), (x2, y2) in zip(U, U[1:] + U[:1]):
        if (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1) < 0: return False
    return True
g = [F(i, 40) for i in range(0, 121)]
ok("Intégrale 14 : le U de 7 cases n'a aucun point qui voie chaque face (les murs intérieurs x = 1 et x = 2 demandent des côtés opposés ; grille de 121 × 121 points, aucun dans le noyau) ; un carré, lui, en a",
   not any(dans_le_noyau(a, b) for a in g for b in g) and dans_le_noyau(F(3, 2), F(3, 2), [(0, 0), (3, 0), (3, 3), (0, 3)]))
# --- Le théorème d'or, section 6 et É 2.2
import random
random.seed(9)
def ecart(t): return F(sum(t), len(t)) - F(9, 2)
tests = []
for _ in range(300):
    c = [random.randint(0, 6) for _ in range(4)]; t = []
    for a in range(1, 5): t += [a] * c[a - 1] + [9 - a] * c[a - 1]
    if t: tests.append(ecart(t) == 0)
ok("Théorème d'or 6 : dès que chaque position est tirée autant de fois que son inverse, l'écart au centre est exactement nul (300 suites) ; la première clause décrit donc un cas que l'identité interdit",
   all(tests) and len(tests) > 250)
# --- Les Tables Natives, sections 3 et 5
ok("Tables Natives 5 : le milieu des paires est 9/2 = 4,5 ; le milieu de la file des neuf points 1 à 9 est le point 5 ; les deux ruptures d'écriture, 4|5 et 5|6, sont à 4,5 et à 5,5",
   all(F(a + 9 - a, 2) == F(9, 2) for a in range(1, 5)) and F(sum(range(1, 10)), 9) == 5 and F(sum(range(1, 9)), 8) == F(9, 2) and F(4 + 5, 2) == F(9, 2) and F(5 + 6, 2) == F(11, 2))
# --- La Prédiction est un acte d'incertitude, É 4.6 et É 4.8
ok("Prédiction 4.6 et 4.8 : le seuil est 2^15 − 1 = 32 767 ; l'écart de départ de Lorenz est 0,506127 − 0,506 = 0,000127", 2 ** 15 - 1 == 32767 and F(506127, 10 ** 6) - F(506, 1000) == F(127, 10 ** 6))
assert all(k for _, k in R); print(len(R), "contrôles, tous conformes")
