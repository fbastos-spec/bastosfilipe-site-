# -*- coding: utf-8 -*-
# L'Énigme 6174, reconstruite : vérifications. Bibliothèque standard seule.
import sys
from collections import Counter
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
def DR(n): return 1 + (n - 1) % 9
def K(n, w):
    d = sorted(f"{n:0{w}d}"); return int("".join(reversed(d))) - int("".join(d))
def premier(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def non_uniformes(w): return [n for n in range(10 ** w) if len(set(f"{n:0{w}d}")) > 1]
def destin(n, w):
    vu = []; x = n
    while x not in vu: vu.append(x); x = K(x, w)
    return x, len(vu), vu[vu.index(x):]

# le lemme
ok("V1 lemme : K(n) est multiple de 9 pour tout n de 1 à 9999 (largeur 4), donc jamais premier, et de racine 9 dès le premier pas",
   all(K(n, 4) % 9 == 0 and not premier(K(n, 4)) and DR(K(n, 4)) == 9 for n in non_uniformes(4)))
ok("V2 les trois exemples : K(2026) = 5994, K(137) = 7173, K(8) = 7992", (K(2026, 4), K(137, 4), K(8, 4)) == (5994, 7173, 7992))
# deux chiffres
c2 = destin(9, 2)[2]
ok("V3 deux chiffres : le pas vaut 9 × (grand - petit) ; aucun point fixe ; un seul cycle, 09, 81, 63, 27, 45, les cinq multiples impairs de 9",
   all(K(n, 2) == 9 * (int(max(f"{n:02d}")) - int(min(f"{n:02d}"))) for n in non_uniformes(2))
   and not any(K(n, 2) == n for n in non_uniformes(2)) and c2 == [9, 81, 63, 27, 45]
   and all(set(destin(n, 2)[2]) == set(c2) for n in non_uniformes(2)) and sorted(c2) == [9 * k for k in (1, 3, 5, 7, 9)])
# trois chiffres
n3 = non_uniformes(3); pas3 = [destin(n, 3) for n in n3]
ok("V4 trois chiffres : le pas vaut 99 × (grand - petit), toujours un barreau 99k ; 495 = 45 × 11 = 5 × 99 est fixe (954 - 459) ; les 990 nombres y aboutissent, en six pas au plus",
   all(K(n, 3) == 99 * (int(max(f"{n:03d}")) - int(min(f"{n:03d}"))) for n in n3) and K(495, 3) == 495 == 45 * 11 == 5 * 99 and 954 - 459 == 495
   and len(n3) == 990 and all(d[0] == 495 for d in pas3) and max(d[1] - 1 if d[0] != n else 0 for d, n in zip(pas3, n3)) == 6)
def chemin(n, w):
    c = [n]
    while K(c[-1], w) != c[-1]: c.append(K(c[-1], w))
    return c
ok("V5 l'échelle : 099, 891, 792, 693, 594, 495 ; et 189, 792, 693, 594, 495 ; 198 - 189 = 9",
   chemin(99, 3) == [99, 891, 792, 693, 594, 495] and chemin(189, 3) == [189, 792, 693, 594, 495] and 198 - 189 == 9)
# quatre chiffres
n4 = non_uniformes(4); d4 = [destin(n, 4) for n in n4]
def pas4(n):
    a, b, c, d = sorted((int(x) for x in f"{n:04d}"), reverse=True); return 999 * (a - d) + 90 * (b - c)
dist = Counter(len(chemin(n, 4)) - 1 for n in n4)
ok("V6 quatre chiffres : le pas vaut 999 × (a - d) + 90 × (b - c) ; 6174 est fixe (7641 - 1467 = 999 × 6 + 90 × 2)",
   all(K(n, 4) == pas4(n) for n in n4) and K(6174, 4) == 6174 == 7641 - 1467 == 999 * 6 + 90 * 2)
ok(f"V7 les 9990 écritures non uniformes (8991 nombres de 1000 à 9999) aboutissent toutes à 6174, en sept pas au plus ; par nombre de pas, de 0 à 7 : {[dist[k] for k in range(8)]}",
   len(n4) == 9990 and sum(1 for n in n4 if n >= 1000) == 8991 and all(d[0] == 6174 for d in d4) and max(dist) == 7 and sum(dist.values()) == 9990)
ok("V8 6174 = 18 × 7³ = 2 × 3² × 7³ ; la somme de ses chiffres est 18 ; sa racine est 9", 6174 == 18 * 7 ** 3 == 2 * 3 ** 2 * 7 ** 3 and 6 + 1 + 7 + 4 == 18 and DR(6174) == 9)
# cinq chiffres
n5 = non_uniformes(5); cyc = set()
for n in n5:
    x = n
    for _ in range(40): x = K(x, 5)
    c = [x]
    while K(c[-1], 5) != x: c.append(K(c[-1], 5))
    cyc.add(tuple(sorted(c)))
ok("V9 cinq chiffres : aucun point fixe ; trois cycles, de longueurs 2, 4 et 4 (53955 et 59994 ; 61974, 82962, 75933, 63954 ; 62964, 71973, 83952, 74943)",
   not any(K(n, 5) == n for n in n5) and cyc == {(53955, 59994), (61974, 63954, 75933, 82962), (62964, 71973, 74943, 83952)})
# 495, 496, le demi
ok("V10 1 + 2 + … + 31 = 496 et 2 + … + 31 = 495 ; un pas mène 496 sur 495 (964 - 469) ; 694 aussi", sum(range(1, 32)) == 496 and sum(range(2, 32)) == 495 and K(496, 3) == 495 == 964 - 469 == K(694, 3))
ok("V11 le demi-point : 49 + 50 = 99, milieu 49,5 ; 10 × 49,5 = 495 ; 4 × 49,5 = 198 ; 4 × 49 = 196 ; 198 - 196 = 2", 49 + 50 == 99 and 495 * 2 == 10 * 99 and 198 * 2 == 4 * 99 and 4 * 49 == 196 and 198 - 196 == 2)
if len(sys.argv) > 1:
    src = open(sys.argv[1], encoding="utf-8").read()
    ok("V12 aucun tiret cadratin ni demi-cadratin dans la source", "—" not in src and "–" not in src)
for n, c in R: print(("OK   " if c else "FAUX ") + n)
print(f"{sum(c for _, c in R)} contrôles sur {len(R)} conformes")
sys.exit(0 if all(c for _, c in R) else 1)
