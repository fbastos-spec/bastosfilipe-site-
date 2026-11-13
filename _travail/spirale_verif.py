# -*- coding: utf-8 -*-
# On a confondu sphère et spirale : vérifications. Bibliothèque standard seule.
import sys
from fractions import Fraction as Fr
from math import pi, isqrt
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
def DR(n): return 1 + (n - 1) % 9
def tours(n): return (n - 1) // 9
def chiffres(n): return sum(int(c) for c in str(n))
N = 100000

# ---------- 1. Le 9 ne ferme rien
ok("V1 ajouté, le 9 garde l'adresse et monte d'un tour (n de 1 à 100000) ; multiplié, il donne la racine 9 pour tout n",
   all(DR(n + 9) == DR(n) and tours(n + 9) == tours(n) + 1 and DR(9 * n) == 9 for n in range(1, N + 1)))
rep = lambda k: int("1" * k)
ok("V2 la règle des ordres : 9 × 1…1 + 1 = 10^k pour k de 1 à 60 ; 10^k est à l'adresse 1, au tour 1…1",
   all(9 * rep(k) + 1 == 10 ** k and DR(10 ** k) == 1 and tours(10 ** k) == rep(k) for k in range(1, 61)))
L = lambda n: len(str(n))
ok("V3 l'ordre nouveau : par + 1 il ne s'ouvre que depuis 9, 99, 999, 9999, 99999 ; par + 9 depuis 1 à 9, 91 à 99, 991 à 999",
   [n for n in range(1, N) if L(n + 1) > L(n)] == [9, 99, 999, 9999, 99999]
   and [n for n in range(1, 2000) if L(n + 9) > L(n)] == list(range(1, 10)) + list(range(91, 100)) + list(range(991, 1000)))
def division_1_par_3(k):
    r, q = 1, []
    for _ in range(k):
        r *= 10; q.append(r // 3); r %= 3
    return q, r
ok("V4 1 divisé par 3 : le reste vaut 1 à chacun des 200 premiers pas ; 10^k = 3 × 3…3 + 1 ; 0,3…3 × 3 = 0,9…9 = 1 moins 10^-k (k de 1 à 60)",
   all(division_1_par_3(k) == ([3] * k, 1) for k in range(1, 201))
   and all(10 ** k == 3 * int("3" * k) + 1 and 3 * Fr(int("3" * k), 10 ** k) == 1 - Fr(1, 10 ** k) for k in range(1, 61)))
def racines_dizaine(d): return [DR(10 * d + u) for u in range(10)]
ok("V5 théorème des dizaines : dans chaque dizaine (jusqu'à 100000) une seule racine revient deux fois, celle du nombre des dizaines, au début et à la fin",
   all(sorted(racines_dizaine(d)) == sorted(list(range(1, 10)) + [DR(d)]) and racines_dizaine(d)[0] == racines_dizaine(d)[9] == DR(d) for d in range(1, N // 10)))
r1 = [n for n in range(1, 101) if DR(n) == 1]
caches = [n for n in r1 if "1" not in str(n)]
ok("V6 racine 1 : 1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100 ; le premier sans chiffre 1 est 28, huitième après 20 ; les sept sans chiffre 1 vont en miroirs de somme 110 autour de 55",
   r1 == [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100] and caches == [28, 37, 46, 55, 64, 73, 82] and 28 - 20 == 8
   and [DR(n) for n in range(20, 29)] == [2, 3, 4, 5, 6, 7, 8, 9, 1] and all(a + b == 110 and str(a) == str(b)[::-1] for a, b in ((28, 82), (37, 73), (46, 64), (55, 55))))
def sigma_propre(n): return sum(d for d in range(1, n) if n % d == 0)
parfaits = [2 ** (p - 1) * (2 ** p - 1) for p in (2, 3, 5, 7, 13, 17, 19, 31)]
tri = lambda x: isqrt(8 * x + 1) ** 2 == 8 * x + 1
ok("V7 28 = 1 + 2 + … + 7 = 1 + 2 + 4 + 7 + 14 ; les parfaits pairs 28, 496, 8128, 33550336 et les quatre suivants ont la racine 1 et sont triangulaires ; 6 a la racine 6",
   sum(range(1, 8)) == 28 == sigma_propre(28) and sigma_propre(496) == 496 and sigma_propre(8128) == 8128 and parfaits[:4] == [6, 28, 496, 8128]
   and DR(6) == 6 and all(DR(p) == 1 for p in parfaits[1:]) and all(tri(p) for p in parfaits))

# ---------- 2. Collatz avec les neuf ajouts
def pas(d): return lambda x: x // 2 if x % 2 == 0 else 3 * x + d
rail = lambda r: "D" if r in (1, 4, 7) else ("G" if r in (2, 5, 8) else "A")
ok("V8 la frappe 3n + d tombe sur le rail de d, pour d de 1 à 9 et pour 11 et 27 (n de 1 à 100000)",
   all(rail(DR(3 * n + d)) == rail(DR(d)) for d in list(range(1, 10)) + [11, 27] for n in range(1, N + 1)))
def frappes_avant_9(n):
    f = pas(9); x = n; k = 0
    while x % 9:
        if x % 2: k += 1
        x = f(x)
    return k
ok("V9 avec + 9 : multiple de 9 après deux frappes au plus (départs de 1 à 100000), puis racine 9 gardée ; le pas de 9m vaut 9 fois le pas de Collatz de m ; même relation pour d = 1, 3, 5, 7, 11",
   max(frappes_avant_9(n) for n in range(1, N + 1)) == 2 and all(DR(pas(9)(9 * m)) == 9 for m in range(1, N))
   and all(pas(d)(d * m) == d * pas(1)(m) for d in (3, 5, 7, 9, 11) for m in range(1, 50000)))
def cycles(d, lim=N):
    f = pas(d); issue = {}
    for n in range(1, lim + 1):
        x = n; vu = set(); chemin = []
        while x not in issue and x not in vu:
            vu.add(x); chemin.append(x); x = f(x)
        if x in issue: c = issue[x]
        else:
            boucle = chemin[chemin.index(x):]; c = min(boucle)
            for v in boucle: issue[v] = c
        for v in chemin: issue.setdefault(v, c)
    return sorted(set(issue[n] for n in range(1, lim + 1)))
C = {d: cycles(d) for d in (1, 3, 5, 7, 9, 11, 27)}
ok("V10 cycles atteints par les départs de 1 à 100000 (plus petit terme de chacun) : + 1 : 1 ; + 3 : 3 ; + 5 : 1, 5, 19, 23, 187, 347 ; + 7 : 5, 7 ; + 9 : 9 ; + 11 : 1, 11, 13 ; + 27 : 27",
   C == {1: [1], 3: [3], 5: [1, 5, 19, 23, 187, 347], 7: [5, 7], 9: [9], 11: [1, 11, 13], 27: [27]})
def fige(d):
    x = 1; rs = []
    for _ in range(40): x = 3 * x + d; rs.append(DR(x))
    return rs
ok("V11 ajouts pairs 2, 4, 6, 8 : un impair donne un impair ; la racine se fige dès la deuxième frappe sur 9 moins la moitié de l'ajout : 8, 7, 6, 5",
   all((3 * n + d) % 2 == 1 for d in (2, 4, 6, 8) for n in range(1, 20001, 2)) and all(set(fige(d)[1:]) == {9 - d // 2} for d in (2, 4, 6, 8)))
def axe_apres(d):
    f = pas(d)
    for n in range(1, 20001):
        x = n; vu = False
        for _ in range(400):
            if x % 2: vu = True
            x = f(x)
            if vu and x % 3 == 0: return True
    return False
ok("V12 avec + 1, + 7, + 11, aucun départ de 1 à 20000 ne retouche l'axe après la première frappe ; avec + 9 tous y sont",
   not axe_apres(1) and not axe_apres(7) and not axe_apres(11) and all(pas(9)(n) % 3 == 0 for n in range(1, 20001, 2)))

# ---------- 3. Le centre visible
marche = [1, 8, 2, 7, 3, 6, 4, 5, Fr(9, 2)]
ok("V13 la marche des paires 1, 8, 2, 7, 3, 6, 4, 5, 4,5 : enjambées 7, 6, 5, 4, 3, 2, 1, puis 1/2, en changeant de sens à chaque pas",
   [abs(b - a) for a, b in zip(marche, marche[1:])] == [7, 6, 5, 4, 3, 2, 1, Fr(1, 2)]
   and all((b - a) * (c - b) < 0 for a, b, c in zip(marche, marche[1:], marche[2:])))
pave = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
ok("V14 le pavé tordu, le 1 lu 10 : centre 6 ; les quatre paires opposées font 12 = 9 + 3 = 11 + 1 ; chacune vaut une paire du cadastre plus 3 ; 6 = 4,5 + 1,5",
   pave[1][1] == 6 and all(pave[i][j] + pave[2 - i][2 - j] == 12 for i in range(3) for j in range(3)) and 12 == 9 + 3 == 11 + 1 and Fr(9, 2) + Fr(3, 2) == 6
   and DR(10) == 1 and DR(12) == 3 and DR(11) == 2)
ok("V15 la liste de 12 à 23 : racines 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5", [DR(n) for n in range(12, 24)] == [3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5])

# ---------- 4. Sphère et spirale
def ecart(k): return abs(k - 2 * pi * round(k / (2 * pi)))
records = []; best = 1.0
for k in range(1, 1000):
    if ecart(k) < best: best = ecart(k); records.append(k)
ok("V16 le rayon posé en arc : six pas font 6, le tour fait 2π, il manque 0,2832 ; retours les plus proches à 44 pas (7 tours, 0,0177) et 710 pas (113 tours, 0,00006)",
   abs((2 * pi - 6) - 0.28319) < 1e-5 and records[-3:] == [44, 333, 710] and round(44 / (2 * pi)) == 7 and round(710 / (2 * pi)) == 113
   and abs(ecart(44) - 0.0177) < 1e-4 and abs(ecart(710) - 6.03e-5) < 1e-6)
ok("V17 1/8 = 0,125 et 9/8 = 1,125 : 9/8 = 1 + 1/8", Fr(9, 8) == 1 + Fr(1, 8) and float(Fr(1, 8)) == 0.125 and float(Fr(9, 8)) == 1.125)
S = lambda k: 13 + k * (k + 1) // 2
emp = [4, 5, 7, 1, 5, 1, 7, 5, 4]
ok("V18 la spirale du soleil 13 + k(k + 1)/2 : empreinte 4 5 7 1 5 1 7 5 4, de somme 39, revenant tous les neuf termes (100000 termes) ; le neuvième pas vaut 9 et mène à 58, de racine 4 comme 13",
   [DR(S(k)) for k in range(9)] == emp and sum(emp) == 39 and all(DR(S(k)) == emp[k % 9] for k in range(N)) and S(9) - S(8) == 9 and S(9) == 58 and DR(58) == DR(13) == 4)
ok("V19 d'un passage au suivant les neuf termes montent de 45, 54, 63, 72, 81, 90, 99, 108, 117, soit 5 à 13 tours de 9",
   [S(k + 9) - S(k) for k in range(9)] == [45, 54, 63, 72, 81, 90, 99, 108, 117] and [(S(k + 9) - S(k)) // 9 for k in range(9)] == list(range(5, 14)))
T = [S(k) for k in range(44)]
ok("V20 jusqu'à 1000 : 44 termes, de 13 à 959 ; miroirs dans la suite 14 et 41, 19 et 91, 338 et 833, 478 et 874 ; carrés 16, 49, 289 ; triangulaires 28 et 91 ; 118 en est ; 137, 196, 198, 495, 496 n'en sont pas",
   len(T) == 44 and T[-1] == 959 and S(44) > 1000
   and sorted((a, int(str(a)[::-1])) for a in T if int(str(a)[::-1]) in T and int(str(a)[::-1]) > a) == [(14, 41), (19, 91), (338, 833), (478, 874)]
   and [x for x in T if isqrt(x) ** 2 == x] == [16, 49, 289] and [x for x in T if tri(x)] == [28, 91] and 118 in T and not any(x in T for x in (137, 196, 198, 495, 496)))
f = lambda k: 13 + Fr(k * (k + 1), 2)
ok("V21 les deux cônes : la loi redonne 13, 14, 16, 19 en reculant ; son point le plus bas est à mi-chemin des deux 13 et vaut 13 moins 1/8, soit 103/8 = 12,875 ; 3 + 9 = 12 et 4 + 9 = 13",
   [f(k) for k in (-1, -2, -3, -4)] == [13, 14, 16, 19] and f(Fr(-1, 2)) == 13 - Fr(1, 8) == Fr(103, 8) and all(f(Fr(-1, 2)) < f(Fr(-1, 2) + Fr(j, 100)) for j in range(-300, 301) if j)
   and all(f(Fr(-1, 2) + Fr(j, 7)) == f(Fr(-1, 2) - Fr(j, 7)) for j in range(1, 50)) and 3 + 9 == 12 and 4 + 9 == 13)
def suite(a, b, n=24):
    r = []
    for _ in range(n): r.append(DR(a)); a, b = b, a + b
    return r
fib = suite(1, 1, 240)
ok("V22 phi : les racines de Fibonacci tournent en 24 ; pliées en 12 et 12, onze colonnes font 9 et la douzième, 9 et 9, fait 18 ; les quatre paires d'inverses y sont",
   fib[:24] == [1, 1, 2, 3, 5, 8, 4, 3, 7, 1, 8, 9, 8, 8, 7, 6, 4, 1, 5, 6, 2, 8, 1, 9] and all(fib[i] == fib[i + 24] for i in range(200))
   and [a + b for a, b in zip(fib[:12], fib[12:24])] == [9] * 11 + [18] and {frozenset((a, b)) for a, b in zip(fib[:11], fib[12:23])} == {frozenset(p) for p in ((1, 8), (2, 7), (3, 6), (4, 5))})
ok("V23 les deux moitiés font 52 = 13 × 4 et 65 = 13 × 5, le tour 117 = 13 × 9 = 12 × 9 + 9 = 3 × 39 ; avec le 9 lu 0 il resterait 108",
   sum(fib[:12]) == 52 == 13 * 4 and sum(fib[12:24]) == 65 == 13 * 5 and sum(fib[:24]) == 117 == 13 * 9 == 12 * 9 + 9 == 3 * 39 and sum(x % 9 for x in fib[:24]) == 99 and 12 * 9 == 108)
autres = {(2, 1): (43, 74), (1, 3): (48, 69), (1, 4): (55, 62)}
ok("V24 autres suites de même loi, départs (2, 1), (1, 3), (1, 4) : tour 117 aussi, moitiés 43 et 74, 48 et 69, 55 et 62, aucune multiple de 13",
   all((sum(suite(*d)[:12]), sum(suite(*d)[12:])) == m and sum(m) == 117 and m[0] % 13 and m[1] % 13 for d, m in autres.items()))
F = [1, 1]
while F[-1] < 10 ** 60: F.append(F[-1] + F[-2])
ok("V25 nombres communs à Fibonacci (jusqu'à soixante chiffres) et à la spirale : 13 et 34 seulement ; 34 est le septième terme ; tour commun des deux empreintes : 72 = 3 × 24 = 8 × 9",
   sorted(set(x for x in F if x >= 13 and tri(x - 13))) == [13, 34] and S(6) == 34 and all((fib[6 + j], emp[j % 9]) == (fib[6 + j + 72], emp[(j + 72) % 9]) for j in range(150))
   and not all(fib[6 + j] == fib[6 + j + 24] and emp[j % 9] == emp[(j + 24) % 9] for j in range(72)))

# ---------- 5. L'atome
ok("V26 1 + 3 + 5 = 9 cases, deux électrons par case : 18 ; cœurs 18, 36, 54 ; la somme des chiffres de Z vaut Z moins le cœur pour 20 à 29, 40 à 49, 60 à 69",
   1 + 3 + 5 == 9 and 2 * 9 == 18 and all(chiffres(Z) == Z - 18 for Z in range(20, 30)) and all(chiffres(Z) == Z - 36 for Z in range(40, 50)) and all(chiffres(Z) == Z - 54 for Z in range(60, 70)))
anom = {24: ((4, 2), (5, 1)), 29: ((9, 2), (10, 1)), 41: ((3, 2), (4, 1)), 42: ((4, 2), (5, 1)), 44: ((6, 2), (7, 1)), 45: ((7, 2), (8, 1)), 46: ((8, 2), (10, 0)), 47: ((9, 2), (10, 1)), 78: ((8, 2), (9, 1)), 79: ((9, 2), (10, 1))}
e = lambda t: 10 * t[0] + t[1]
ok("V27 anomalies en d et s, écrites d puis s : l'écart entre l'attendu et le réel vaut 9 (18 pour le palladium, 82, 91, 100) et le total est gardé ; chrome et molybdène : 42 devient 51",
   all(sum(a) == sum(r) for a, r in anom.values()) and {Z: e(r) - e(a) for Z, (a, r) in anom.items()} == {24: 9, 29: 9, 41: 9, 42: 9, 44: 9, 45: 9, 46: 18, 47: 9, 78: 9, 79: 9}
   and e(anom[24][0]) == e(anom[42][0]) == 42 and e(anom[24][1]) == 51 and [6 + 9 * k for k in range(1, 7)] == [15, 24, 33, 42, 51, 60])
ok("V28 racine 9 puis racine 1 : 18 et 19, 36 et 37, 54 et 55 ; au premier tour 9 et 10 ; 137 moins 37 = 100, à l'adresse 1",
   [(DR(a), DR(a + 1)) for a in (9, 18, 36, 54)] == [(9, 1)] * 4 and 137 - 37 == 100 and DR(100) == 1 and DR(37) == 1)

# ---------- 6. La cellule
ok("V29 files de tubuline : doublet 13 + 10 = 23 ; triplet 13 + 10 + 10 = 33 ; cil 9 × 23 + 2 × 13 = 233, treizième de Fibonacci ; centriole 9 × 33 = 297 = 11 × 27 ; 9 + 2 = 11 ; 9 triplets = 27 tubes",
   13 + 10 == 23 and 13 + 20 == 33 and 9 * 23 + 2 * 13 == 233 == F[12] and 9 * 33 == 297 == 11 * 27 and 9 + 2 == 11 and 9 * 3 == 27)
ok("V30 colonne vertébrale : 7 + 12 + 5 + 5 + 4 = 33 = 24 mobiles + 9 soudées", 7 + 12 + 5 + 5 + 4 == 33 and 7 + 12 + 5 == 24 and 5 + 4 == 9)

if len(sys.argv) > 1:
    src = open(sys.argv[1], encoding="utf-8").read()
    ok("V31 aucun tiret cadratin ni demi-cadratin dans la source", "—" not in src and "–" not in src)
for n, c in R: print(("OK   " if c else "FAUX ") + n)
print(f"{sum(c for _, c in R)} contrôles sur {len(R)} conformes")
sys.exit(0 if all(c for _, c in R) else 1)
