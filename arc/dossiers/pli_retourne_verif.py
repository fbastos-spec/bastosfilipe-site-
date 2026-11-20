# -*- coding: utf-8 -*-
# Le pli retourné. Vérifications. Python 3, bibliothèque standard seule.
import sys
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
rac = lambda n: 1 + (n - 1) % 9
ok("V1 la clôture garde ses tours : 9 × 4 = 36, racine 9, quatre tours ; pour tout n de 1 à 100 000, 9 × n a pour racine 9 et compte n tours, là où la congruence écrit 0",
   36 == 9 * 4 and rac(36) == 9 and all(rac(9 * n) == 9 and (9 * n) // 9 == n and (9 * n) % 9 == 0 for n in range(1, 100001)))
if len(sys.argv) > 1:
    t = open(sys.argv[1], encoding='utf-8').read()
    ok("typographie de la source : aucun tiret long ni moyen", '\u2014' not in t and '\u2013' not in t)
for nom, c in R: print(("conforme : " if c else "ÉCHEC : ") + nom)
assert all(c for _, c in R) and R; print(len(R), "contrôle(s), tous conformes")
