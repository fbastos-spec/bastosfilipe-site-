# -*- coding: utf-8 -*-
# Ni saut ni paquet. Vérifications. Python 3, bibliothèque standard seule.
import sys
R = []
def ok(nom, cond): R.append((nom, bool(cond)))
if len(sys.argv) > 1:
    t = open(sys.argv[1], encoding='utf-8').read()
    ok("typographie de la source : aucun tiret long ni moyen", '\u2014' not in t and '\u2013' not in t)
for nom, c in R: print(("conforme : " if c else "ÉCHEC : ") + nom)
assert all(c for _, c in R) and R; print(len(R), "contrôle(s), tous conformes")
