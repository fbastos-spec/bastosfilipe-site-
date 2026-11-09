# Vérifications de L'observateur est la confusion v0.3 (bibliothèque standard seulement)
import sys, math, random
from fractions import Fraction as Fr

out = []
def ok(label, cond):
    out.append(f"{label}   {'OK' if cond else 'ECHEC'}"); assert cond, label

def DR(n): return 9 if n % 9 == 0 else n % 9
ok("Bijection n = 9k + DR(n), n = 1..100000",
   all(9 * ((n - DR(n)) // 9) + DR(n) == n for n in range(1, 100001)))

x0 = Fr(1, 3); x = x0; w = []; tours = 0; good = True
for n in range(9):
    w.append(tours)
    good &= (x + tours) / 2**n == x0
    y = 2 * x; k = int(y); x = y - k; tours = 2 * tours + k
ok(f"Pli depuis 1/3 : tours jetés {','.join(map(str, w))} ; x0 restitué à chaque pas",
   w == [0, 0, 1, 2, 5, 10, 21, 42, 85] and good)

ok("Ariane : seuil 16 bits signés 32767 ; 32768 déborde", 2**15 - 1 == 32767)

def chsh(angles, N=200000, seed=9, tarif=True):
    rnd = random.Random(seed)
    def unit(t): return (math.cos(t), math.sin(t), 0.0)
    def E(a, b):
        s = 0
        for _ in range(N):
            z = rnd.uniform(-1, 1); ph = rnd.uniform(0, 2 * math.pi); r = math.sqrt(1 - z * z)
            lam = (r * math.cos(ph), r * math.sin(ph), z)
            A = 1 if sum(i * j for i, j in zip(a, lam)) >= 0 else -1
            lam2 = tuple(-A * i for i in a)
            mu = rnd.uniform(-1, 1) if tarif else 0.0
            B = 1 if sum(i * j for i, j in zip(b, lam2)) - mu >= 0 else -1
            s += A * B
        return s / N
    a0, a1, b0, b1 = (unit(math.radians(t)) for t in angles)
    return E(a0, b0) - E(a0, b1) + E(a1, b0) + E(a1, b1)
S_diag = abs(chsh((0, 90, 45, 135)))                 # réglages du sablier, lecture tarifée
S_free = abs(chsh((0, 90, 45, 135), tarif=False))    # lecture gratuite : lecteur sans tarif
S_flat = abs(chsh((0, 90, 0, 90)))                   # sans diagonales
ok(f"CHSH sphère, réglages 0°,45°,90°,135° : lecture tarifée S = {S_diag:.4f} = 2√2 ; lecture gratuite {S_free:.4f} ; sans diagonales {S_flat:.4f}",
   abs(S_diag - 2 * math.sqrt(2)) < 0.02 and abs(S_free - 4) < 0.001 and abs(S_flat - 2) < 0.02)

src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)
print("\n".join(out))
