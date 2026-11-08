# Vérifications de La Prédiction est un acte d'incertitude v0.1 (bibliothèque standard seulement)
import sys
from fractions import Fraction as Fr

out = []
def ok(label, cond):
    out.append(f"{label}   {'OK' if cond else 'ECHEC'}")
    assert cond, label

# Patriot : 0,1 écrit avec 23 chiffres binaires après la virgule (registre 24 bits)
t = Fr(1, 10)
stored = Fr(int(t * 2**23), 2**23)
eps = t - stored
ticks = 100 * 3600 * 10
drift = eps * ticks
dist = drift * 1676
ok(f"Patriot   : coupe par tic = {eps} s = {float(eps):.4e} ; {ticks} tics ; dérive {float(drift):.4f} s ; {float(dist):.1f} m",
   abs(float(drift) - 0.3433) < 0.001 and 500 < float(dist) < 650)

# Vancouver
ecart = Fr("1098.892") - Fr("524.811")
n = 460 * 3000
par = ecart / n
ok(f"Vancouver : écart {float(ecart)} ; {n} troncatures ; {float(par):.6f} par troncature, dans [0, 0.001]",
   float(ecart) == 574.081 and 0 < par < Fr(1, 1000))

# Ariane
mx = 2**15 - 1
ok(f"Ariane    : maximum 16 bits signés = {mx} ; {mx+1} déborde", mx == 32767)

# Lorenz
e0 = Fr("0.506127") - Fr("0.506")
ok(f"Lorenz    : écart initial {float(e0):.2e}", e0 == Fr(127, 1000000))

# Typographie
src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)

print("\n".join(out))
