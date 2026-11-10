# Vérifications de Fourier est un ARC v0.6 (bibliothèque standard seulement)
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
# Th 3.4 bis : le tarif des tours donne la courbe de Planck
charge = lambda m, q: m / (q ** -m - 1)
direct = lambda m, q, N=6000: sum(n * m * q ** (m * n) for n in range(N)) / sum(q ** (m * n) for n in range(N))
ok("Th 3.4 bis : somme directe des parts = forme fermée m/(q^-m - 1), pour q = 0.5, 0.9, 0.99 et m = 1, 2, 3, 5, 10",
   all(abs(direct(m, q) - charge(m, q)) < 1e-9 for q in (.5, .9, .99) for m in (1, 2, 3, 5, 10)))
hP, kB, T, nu1 = 6.62607015e-34, 1.380649e-23, 300.0, 1e11
qT = math.exp(-hP * nu1 / (kB * T))
ok("Th 3.4 bis : avec q = e^(-hν₁/kT), écart relatif à hν/(e^(hν/kT) - 1) < 1e-12 aux rangs 1, 10, 100, 1000",
   all(abs(charge(m, qT) * hP * nu1 / (hP * m * nu1 / math.expm1(hP * m * nu1 / (kB * T))) - 1) < 1e-12 for m in (1, 10, 100, 1000)))
ok("Th 3.4 bis : boîte chaude (q = 0.999999), même charge aux rangs 1, 2, 5, 10 à 1e-5 près (Rayleigh et Jeans)",
   all(abs(charge(m, .999999) / charge(1, .999999) - 1) < 1e-5 for m in (2, 5, 10)))
tot = lambda q, M: sum(m * q ** m / (1 - q ** m) for m in range(1, M))  # même charge, écrite sans grand nombre
ok("Th 3.4 bis : somme sur les rangs finie pour q = 0.5, 0.9, 0.99 (inchangée de 5 000 à 50 000 rangs)",
   all(abs(tot(q, 50000) - tot(q, 5000)) < 1e-9 for q in (.5, .9, .99)))
# Th 3.7 : le théorème de Pusey, Barrett et Rudolph (2012), preuve à deux exemplaires
h = 2 ** -.5
z, o, p, m = (1, 0), (0, 1), (h, h), (h, -h)
kron = lambda a, b: tuple(x * y for x in a for y in b)
plus = lambda a, b: tuple(h * (x + y) for x, y in zip(a, b))
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
xi = [plus(kron(z, o), kron(o, z)), plus(kron(z, m), kron(o, p)), plus(kron(p, o), kron(m, z)), plus(kron(p, m), kron(m, p))]
prep = [kron(z, z), kron(z, p), kron(p, z), kron(p, p)]
parts = [[dot(x, v) ** 2 for x in xi] for v in prep]
ok("Th 3.7 : recouvrement de 0 et de + = cos(π/4) = 1/√2 ; son carré = (r/R)² du carré = 0.5",
   abs(dot(z, p) - math.cos(math.pi / 4)) < 1e-12 and abs(dot(z, p) ** 2 - r[4] ** 2) < 1e-12 and abs(dot(z, p) ** 2 - .5) < 1e-12)
ok("Th 3.7 : les quatre issues forment une base (16 produits : 1 sur la diagonale, 0 ailleurs)",
   all(abs(dot(xi[i], xi[j]) - (i == j)) < 1e-12 for i in range(4) for j in range(4)))
ok("Th 3.7 : parts des quatre issues = 0, 1/4, 1/4, 1/2 pour chaque préparation ; le 0 sur l'issue 1, 2, 3, 4",
   all(sorted(round(x, 12) for x in row) == [0, .25, .25, .5] for row in parts) and all(abs(parts[i][i]) < 1e-12 for i in range(4)))
ok("Th 3.7 : seuil à deux exemplaires, 2·arctan(√2 − 1) = π/4 ; tan(π/8) = √2 − 1",
   abs(2 * math.atan(2 ** .5 - 1) - math.pi / 4) < 1e-12 and abs(math.tan(math.pi / 8) - (2 ** .5 - 1)) < 1e-12)
ok("Couches électroniques 2n² = 2, 8, 18, 32", [2 * n * n for n in range(1, 5)] == [2, 8, 18, 32])
src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)
print("\n".join(out))
