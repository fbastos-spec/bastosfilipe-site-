# Vérifications du Théorème d'or v0.1 (bibliothèque standard seulement)
import sys, random
out = []
def ok(label, cond):
    out.append(f"{label}   {'OK' if cond else 'ECHEC'}"); assert cond, label
dr = lambda n: 9 if n % 9 == 0 else n % 9
from fractions import Fraction as Fr
random.seed(9); N = 100000; cnt = [0] * 10; worst = Fr(0)
for n in range(1, N + 1):
    cnt[random.randint(1, 8)] += 1
    m = Fr(sum(a * cnt[a] for a in range(1, 9)), n)
    rhs = Fr(sum((2 * a - 9) * (cnt[a] - cnt[9 - a]) for a in range(1, 5)), 2 * n)
    worst = max(worst, abs((m - Fr(9, 2)) - rhs))
ok(f"Th 2.1 : identité écart au centre = somme pondérée des paires ouvertes, {N} pas, écart max {float(worst):.1e}", worst == 0)
ok("Centre des paires 4.5 ; centre avec la clôture 5.0 ; différence 0.5", sum(range(1, 9)) / 8 == 4.5 and sum(range(1, 10)) / 9 == 5.0)
def consec(s): return all(s[i + 1] - s[i] == 1 for i in range(len(s) - 1)) or all(s[i] - s[i + 1] == 1 for i in range(len(s) - 1))
tress = [a for a in range(1, 10) if consec([dr(a * k) for k in range(1, 10)][0::2]) and consec([dr(a * k) for k in range(1, 10)][1::2])]
r5 = [dr(5 * k) for k in range(1, 10)]
r4 = [dr(4 * k) for k in range(1, 10)]
ok(f"Tressage, clôture comprise : seule la rangée du 5 ; rangée du 5 = {','.join(map(str, r5))} ; le 4 tresse à la clôture près",
   tress == [5] and r5 == [5, 1, 6, 2, 7, 3, 8, 4, 9] and r5[0::2] == [5, 6, 7, 8, 9] and r5[1::2] == [1, 2, 3, 4]
   and r4[0::2][:4] == [4, 3, 2, 1] and r4[1::2] == [8, 7, 6, 5])
p = []; x = 1
for _ in range(6): x = dr(x * 5); p.append(x)
ok(f"Puissances de 5 en racines : {','.join(map(str, p))} ; période 6 ; axe jamais touché", p == [5, 7, 8, 4, 2, 1] and not set(p) & {3, 6, 9})
src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)
print("\n".join(out))
