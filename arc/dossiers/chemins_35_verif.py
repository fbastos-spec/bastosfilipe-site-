# -*- coding: utf-8 -*-
# Tous les chemins mènent à 35 : la position, l'adresse et la racine. Vérifications. Python 3, bibliothèque standard seule.
import sys
from math import gcd
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
rac = lambda n: 1 + (n - 1) % 9          # la racine, de 1 à 9 ; le 9 reste 9
tours = lambda n: (n - rac(n)) // 9      # n = 9 × tours + racine
ok("V1 35 = 9 × 3 + 8 : trois tours et racine 8, écriture unique ; même racine pour 8, 17, 26, 44",
   (tours(35), rac(35)) == (3, 8) and all(9 * t + r != 35 for t in range(0, 10) for r in range(1, 10) if (t, r) != (3, 8)) and [rac(n) for n in (8, 17, 26, 44)] == [8] * 4)
# partitions : nombre de façons d'écrire n comme somme, sans compter l'ordre
N = 400; p = [1] + [0] * N
for k in range(1, N + 1):
    for n in range(k, N + 1): p[n] += p[n - k]
ok("V2 35 s'écrit comme somme de 14 883 façons sans compter l'ordre, de 2^34 = 17 179 869 184 façons en le comptant",
   p[35] == 14883 and 2 ** 34 == 17179869184)
ok("V3 dès 4 et jusqu'à 400, il y a plus de sommes que le nombre lui-même : 4 en a 5, 5 en a 7, 6 en a 11 ; 1, 2 et 3 en ont 1, 2 et 3",
   (p[1], p[2], p[3], p[4], p[5], p[6]) == (1, 2, 3, 5, 7, 11) and all(p[n] > n for n in range(4, N + 1)))
M = {k: divmod(35, k) for k in range(2, 10)}
ok("V4 les marcheurs vers 35 : pas de 2, 17 tours reste 1 ; de 3, 11 reste 2 ; de 4, 8 reste 3 ; de 5, 7 tours juste ; de 6, 5 reste 5 ; de 7, 5 tours juste ; de 8, 4 reste 3 ; de 9, 3 reste 8",
   M == {2: (17, 1), 3: (11, 2), 4: (8, 3), 5: (7, 0), 6: (5, 5), 7: (5, 0), 8: (4, 3), 9: (3, 8)})
ok("V5 les seules paires qui atteignent 35 d'un seul produit sont (1, 35) et (5, 7) ; 37 n'a que (1, 37) ; 5 × 5 + 10 = 3 × 11 + 2 = 30 + 5 = 25 + 10 = 35",
   [(a, 35 // a) for a in range(1, 6) if 35 % a == 0] == [(1, 35), (5, 7)] and [(a, 37 // a) for a in range(1, 7) if 37 % a == 0] == [(1, 37)]
   and 5 * 5 + 10 == 3 * 11 + 2 == 30 + 5 == 25 + 10 == 35)
ok("V6 l'alliage garde la racine : 35 × 35 = 1225, racine 1, comme 8 × 8 = 64 ; 35 + 10 = 45, racine 9, comme 8 + 1 ; la règle tient pour toutes les paires jusqu'à 300",
   35 * 35 == 1225 and rac(1225) == 1 == rac(64) and rac(45) == 9 == rac(8 + 1)
   and all(rac(a * b) == rac(rac(a) * rac(b)) and rac(a + b) == rac(rac(a) + rac(b)) for a in range(1, 301) for b in range(1, 301)))
ok("V7 les voisins : 34 = 2 × 17, 35 = 5 × 7, 36 = 6 × 6 ; deux voisins n'ont aucun facteur commun (contrôlé jusqu'à 100 000) ; racines 7, 8, 9",
   34 == 2 * 17 and 36 == 6 * 6 and all(gcd(n, n + 1) == 1 for n in range(1, 100001)) and [rac(n) for n in (34, 35, 36)] == [7, 8, 9])
# le suivant par la retenue : écriture en neuf signes, de 1 à 9, sans autre signe
def code(n):
    d = []
    while n > 0:
        r = rac(n); d.append(r); n = (n - r) // 9
    return d[::-1]
def suivant(d):
    d = d[:]; i = len(d) - 1
    while i >= 0 and d[i] == 9: d[i] = 1; i -= 1      # au bout du cycle : retour à 1, le voisin compte un tour
    if i < 0: return [1] + d
    d[i] += 1; return d
ok("V8 le suivant sans axiome : sur l'écriture en neuf signes, la règle « avancer d'un cran, ou revenir à 1 et reporter un tour » donne l'écriture de n + 1 pour tout n de 1 à 200 000",
   all(suivant(code(n)) == code(n + 1) for n in range(1, 200001)))
ok("V9 en tours et racine : si la racine n'est pas 9 elle avance d'un cran, si elle est 9 elle revient à 1 et les tours augmentent de 1 (contrôlé de 1 à 200 000)",
   all((tours(n + 1), rac(n + 1)) == ((tours(n), rac(n) + 1) if rac(n) < 9 else (tours(n) + 1, 1)) for n in range(1, 200001)))
def boucle(c):
    r = lambda n: 1 + (n - 1) % c
    orb = []; vus = set()
    for s in range(1, c + 1):
        if s in vus: continue
        o = []; x = s
        while x not in o: o.append(x); x = r(2 * x)
        vus |= set(o); orb.append(o)
    return dict(paires=(c - 1) // 2, centre=c / 2, parts=[d for d in range(2, c) if c % d == 0], doublement=orb)
B = {c: boucle(c) for c in (3, 5, 7, 9, 15)}
ok("V10 les clôtures 5, 7, 9 : 2, 3, 4 paires d'inverses ; centres 2,5, 3,5, 4,5 ; 5 et 7 ne se partagent pas, 9 se partage par 3 ; le doublement parcourt 1, 2, 4, 3 dans 5, se coupe en 1, 2, 4 et 3, 6, 5 dans 7, parcourt 1, 2, 4, 8, 7, 5 dans 9 en laissant 3, 6 à part",
   [B[c]['paires'] for c in (5, 7, 9)] == [2, 3, 4] and [B[c]['centre'] for c in (5, 7, 9)] == [2.5, 3.5, 4.5] and B[5]['parts'] == [] == B[7]['parts'] and B[9]['parts'] == [3]
   and B[5]['doublement'] == [[1, 2, 4, 3], [5]] and B[7]['doublement'] == [[1, 2, 4], [3, 6, 5], [7]] and B[9]['doublement'] == [[1, 2, 4, 8, 7, 5], [3, 6], [9]])
ok("V11 9 est le premier impair qui se partage : 3, 5, 7 sont premiers ; le suivant est 15 = 3 × 5, à parts inégales",
   [n for n in range(3, 16, 2) if any(n % d == 0 for d in range(2, n))] == [9, 15] and B[15]['parts'] == [3, 5])
L = 10 ** 6; puis = set()
for b in range(2, 1001):
    x = b * b
    while x <= L: puis.add(x); x *= b
ok("V12 8 = 2³ et 9 = 3² ; jusqu'à un million, ce sont les deux seules puissances voisines", 8 == 2 ** 3 and 9 == 3 ** 2 and [n for n in sorted(puis) if n + 1 in puis] == [8])
if len(sys.argv) > 1:
    t = open(sys.argv[1], encoding='utf-8').read()
    ok("V13 typographie de la source : aucun tiret long ni moyen", '—' not in t and '–' not in t)
for nom, c in R: print(("conforme : " if c else "ÉCHEC : ") + nom)
assert all(c for _, c in R); print(len(R), "contrôles, tous conformes")
