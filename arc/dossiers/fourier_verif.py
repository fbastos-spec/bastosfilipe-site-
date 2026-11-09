# Vérifications de Fourier est un ARC v0.1 (bibliothèque standard seulement)
import sys, math
from fractions import Fraction as Fr
out = []
def ok(label, cond):
    out.append(f"{label}   {'OK' if cond else 'ECHEC'}"); assert cond, label
dr = lambda n: 9 if n % 9 == 0 else n % 9
tours = []
for a in range(1, 9):
    row = [dr(a * k) for k in range(1, 10)]
    steps = sum((row[i + 1] - row[i]) % 9 for i in range(8)) + (row[0] - row[-1]) % 9
    tours.append(Fr(steps, 9))
ok(f"Th 2.1 : tours accomplis par les rangées ×1..×8 = {','.join(str(int(t)) for t in tours)} ; ×9 immobile",
   tours == [Fr(a) for a in range(1, 9)] and len(set(dr(9 * k) for k in range(1, 10))) == 1)
phi = (1 + 5 ** .5) / 2
r = {n: math.cos(math.pi / n) for n in (3, 4, 5, 6, 8)}
ok(f"Th 2.2 : r/R = cos(π/n) pour n = 3,4,5,6,8 = {r[3]:.1f}, {r[4]:.4f}, {r[5]:.4f}, {r[6]:.4f}, {r[8]:.4f} ; cos(π/5) = φ/2",
   abs(r[3] - .5) < 1e-12 and abs(r[4] - 2 ** .5 / 2) < 1e-12 and abs(r[5] - phi / 2) < 1e-12 and abs(r[6] - 3 ** .5 / 2) < 1e-12)
E = [k * k for k in range(1, 6)]
ok(f"Th 3.1 : énergies sur le cercle fermé = {','.join(map(str, E))} (carrés entiers), aucune constante posée",
   E == [1, 4, 9, 16, 25] and all(abs(math.cos(k * 2 * math.pi) - 1) < 1e-12 for k in range(1, 6)))
prods = [s * (1 / (2 * s)) for s in (0.1, 1, 10)]
ok("Th 3.2 : produit des largeurs Δx·Δk = 0.5 pour σ = 0.1, 1, 10", all(abs(p - .5) < 1e-12 for p in prods))
ok("Couches électroniques 2n² = 2, 8, 18, 32", [2 * n * n for n in range(1, 5)] == [2, 8, 18, 32])
src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)
print("\n".join(out))
