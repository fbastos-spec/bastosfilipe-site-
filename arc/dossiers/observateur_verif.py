# Vérifications de L'observateur est la confusion v0.12 (bibliothèque standard seulement)
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

def chsh(angles, N=200000, seed=9, tarif=True, side='B'):
    rnd = random.Random(seed)
    def unit(t): return (math.cos(t), math.sin(t), 0.0)
    def E(a, b):
        s = 0
        for _ in range(N):
            z = rnd.uniform(-1, 1); ph = rnd.uniform(0, 2 * math.pi); r = math.sqrt(1 - z * z)
            lam = (r * math.cos(ph), r * math.sin(ph), z)
            if side == 'B':
                A = 1 if sum(i * j for i, j in zip(a, lam)) >= 0 else -1
                lam2 = tuple(-A * i for i in a)
                mu = rnd.uniform(-1, 1) if tarif else 0.0
                B = 1 if sum(i * j for i, j in zip(b, lam2)) - mu >= 0 else -1
            else:
                B = 1 if sum(i * j for i, j in zip(b, lam)) >= 0 else -1
                lam2 = tuple(-B * i for i in b)
                mu = rnd.uniform(-1, 1) if tarif else 0.0
                A = 1 if sum(i * j for i, j in zip(a, lam2)) - mu >= 0 else -1
            s += A * B
        return s / N
    a0, a1, b0, b1 = (unit(math.radians(t)) for t in angles)
    return E(a0, b0) - E(a0, b1) + E(a1, b0) + E(a1, b1)
S_diag = abs(chsh((0, 90, 45, 135)))                 # réglages du sablier, lecture tarifée
S_free = abs(chsh((0, 90, 45, 135), tarif=False))    # lecture gratuite : lecteur sans tarif
S_flat = abs(chsh((0, 90, 0, 90)))                   # sans diagonales
ok(f"CHSH sphère, réglages 0°,45°,90°,135° : lecture tarifée S = {S_diag:.4f} = 2√2 ; lecture gratuite {S_free:.4f} ; sans diagonales {S_flat:.4f}",
   abs(S_diag - 2 * math.sqrt(2)) < 0.02 and abs(S_free - 4) < 0.001 and abs(S_flat - 2) < 0.02)

def marginals(a_deg, b_deg, N=200000, seed=11):
    rnd = random.Random(seed); a = (math.cos(math.radians(a_deg)), math.sin(math.radians(a_deg)), 0.0); b = (math.cos(math.radians(b_deg)), math.sin(math.radians(b_deg)), 0.0)
    sA = sB = 0
    for _ in range(N):
        z = rnd.uniform(-1, 1); ph = rnd.uniform(0, 2 * math.pi); r = math.sqrt(1 - z * z)
        lam = (r * math.cos(ph), r * math.sin(ph), z)
        A = 1 if sum(i * j for i, j in zip(a, lam)) >= 0 else -1
        lam2 = tuple(-A * i for i in a); mu = rnd.uniform(-1, 1)
        B = 1 if sum(i * j for i, j in zip(b, lam2)) - mu >= 0 else -1
        sA += A; sB += B
    return sA / N, sB / N
marg = [marginals(a, b) for a in (0, 90) for b in (45, 135)]
ok("Non-signalisation : marginales E[A], E[B] nulles pour les quatre réglages, Bob seul ne lit pas l'angle d'Alice : " + " ; ".join(f"({x:+.3f}, {y:+.3f})" for x, y in marg),
   all(abs(x) < 0.01 and abs(y) < 0.01 for x, y in marg))

S_A = abs(chsh((0, 90, 45, 135), side='A'))
ok(f"Alice lit en second et paie, Bob lit le premier au signe : S = {S_A:.4f} = 2√2 ; c'est la seconde lecture qui paie", abs(S_A - 2 * math.sqrt(2)) < 0.02)

def chsh2(cercle=False, premier_paie=False, N=200000, seed=5):
    rnd = random.Random(seed)
    def E(ad, bd):
        a = (math.cos(math.radians(ad)), math.sin(math.radians(ad))); b = (math.cos(math.radians(bd)), math.sin(math.radians(bd))); s = 0
        for _ in range(N):
            if cercle:
                ph = rnd.uniform(0, 2 * math.pi); lam = (math.cos(ph), math.sin(ph))
            else:
                z = rnd.uniform(-1, 1); ph = rnd.uniform(0, 2 * math.pi); r = math.sqrt(1 - z * z); lam = (r * math.cos(ph), r * math.sin(ph))
            mu = rnd.uniform(-1, 1); al = a[0] * lam[0] + a[1] * lam[1]; ab = a[0] * b[0] + a[1] * b[1]
            if premier_paie:
                A = 1 if al - mu >= 0 else -1; B = 1 if -A * ab >= 0 else -1
            else:
                A = 1 if al >= 0 else -1; B = 1 if -A * ab - mu >= 0 else -1
            s += A * B
        return s / N
    return abs(E(0, 45) - E(0, 135) + E(90, 45) + E(90, 135))
S_c = chsh2(cercle=True); S_p = chsh2(premier_paie=True)
ok(f"Même protocole sur un cercle au lieu de la sphère : S = {S_c:.4f} = 2√2 ; le ½ de ce protocole vient du tarif", abs(S_c - 2 * math.sqrt(2)) < 0.02)
ok(f"Première lecture payante, seconde gratuite : S = {S_p:.4f} = 4", abs(S_p - 4) < 0.001)

def chaine(N, tarif=True):
    pas = math.pi / (2 * N); E = (lambda th: -math.cos(th)) if tarif else (lambda th: -1.0 if math.cos(th) > 0 else 1.0)
    return abs(sum(E(pas) for _ in range(2 * N - 1)) - E((2 * N - 1) * pas))
ok("N réglages par côté : lecture tarifée 2N × cos(π/2N), lecture gratuite 2N, pour N = 2, 3, 4 : " + " ; ".join(f"{chaine(N):.4f} et {chaine(N, False):.0f}" for N in (2, 3, 4)),
   all(abs(chaine(N) - 2 * N * math.cos(math.pi / (2 * N))) < 1e-12 and chaine(N, False) == 2 * N for N in (2, 3, 4)) and abs(chaine(2) - 2 * math.sqrt(2)) < 1e-12)
ok("18 = 9 × 1 + 9 et 81 = 9 × 8 + 9 : k compte les tours fermés avant ; 18 = 9 × 2 ferme le deuxième, 81 = 9 × 9 le neuvième",
   (18 - DR(18)) // 9 == 1 and (81 - DR(81)) // 9 == 8 and DR(18) == DR(81) == 9 and 18 == 9 * 2 and 81 == 9 * 9)
RAILS = (1, 2, 4, 5, 7, 8); DROIT = (1, 4, 7)
som = {x: 9 - x for x in RAILS}
pro = {x: next(y for y in RAILS if DR(x * y) == 1) for x in RAILS}
ok("Inversion par la somme : paires (1,8), (2,7), (4,5) ferment à 9 et changent toujours de rail",
   all(x + som[x] == 9 and (x in DROIT) != (som[x] in DROIT) for x in RAILS))
ok("Inversion par le produit : 1×1, 2×5, 4×7, 8×8 rendent 1 et restent toujours dans le rail ; unique pour chaque position",
   pro == {1: 1, 2: 5, 4: 7, 5: 2, 7: 4, 8: 8} and all((x in DROIT) == (pro[x] in DROIT) for x in RAILS)
   and all(sum(1 for y in range(1, 10) if DR(x * y) == 1) == 1 for x in RAILS))
tro = {x: pro[som[x]] for x in RAILS}
ok("Les deux inversions dans les deux ordres donnent la même troisième : (1,8), (2,4), (5,7) ; l'axe 3, 6, 9 ne revient jamais à 1 par le produit",
   tro == {x: som[pro[x]] for x in RAILS} == {1: 8, 8: 1, 2: 4, 4: 2, 5: 7, 7: 5}
   and all(DR(a * y) in (3, 6, 9) for a in (3, 6, 9) for y in range(1, 10)))
ok("n × n / n : le carré rapporté à son côté rend n, et n rapporté à lui-même rend 1, n = 1..100000",
   all(Fr(n * n, n) == n and Fr(n, n) == 1 and n * Fr(n, n) == n for n in range(1, 100001)))
def orbite(x): return {x, som[x], pro[x], tro[x]}
ok("Les deux inversions rangent les rails en un bloc de quatre et une paire : " + str(sorted(orbite(2))) + " et " + str(sorted(orbite(1))) + " ; dans le bloc, trois appariements",
   orbite(2) == orbite(4) == orbite(5) == orbite(7) == {2, 4, 5, 7} and orbite(1) == orbite(8) == {1, 8}
   and {frozenset((x, f[x])) for f in (som, pro, tro) for x in (2, 4, 5, 7)} == {frozenset(p) for p in ((2, 7), (4, 5), (2, 5), (4, 7), (2, 4), (5, 7))})
def liaison(x, N=400000, seed=13):
    rnd = random.Random(seed); return sum(1 for _ in range(N) if x - rnd.uniform(-1, 1) >= 0) / N
ok("La liaison : chance de lire + à travers μ = ½ + ½ × (b · λ′), pour b · λ′ = 0 ; 0,5 ; 0,8 : " + " ; ".join(f"{liaison(x):.3f}" for x in (0, 0.5, 0.8)) + f" ; et pour l'inverse de 0,5 : {liaison(-0.5):.3f}",
   all(abs(liaison(x) - (0.5 + 0.5 * x)) < 0.004 for x in (-0.5, 0, 0.5, 0.8)))
def mm(P, Q): return tuple(tuple(sum(P[i][k] * Q[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def opp(P): return tuple(tuple(-v for v in r) for r in P)
PX = ((0, 1), (1, 0)); PZ = ((1, 0), (0, -1)); PI = ((1, 0), (0, 1)); PXZ = mm(PX, PZ)
def cl(P): return frozenset((P, opp(P)))
G4 = {cl(PI), cl(PX), cl(PZ), cl(PXZ)}
ok("Pauli : les deux produits croisés sont égaux au signe près, et le signe mis à part les quatre éléments ferment un groupe où chacun est son propre inverse",
   mm(PX, PZ) == opp(mm(PZ, PX)) and mm(PX, PZ) != mm(PZ, PX) and len(G4) == 4
   and all(cl(mm(next(iter(p)), next(iter(q)))) in G4 for p in G4 for q in G4) and all(cl(mm(next(iter(p)), next(iter(p)))) == cl(PI) for p in G4))
PLAFOND = 2**15 - 1
def chemin_carre(n): return max(n, n * n, (n * n) // n)
def chemin_un(n): return max(n, n // n, n * (n // n))
seuil = next(n for n in range(1, PLAFOND + 1) if chemin_carre(n) > PLAFOND)
ok(f"n × n / n, deux chemins sous le plafond {PLAFOND} : les deux rendent n ; le chemin par le carré déborde à partir de n = {seuil} (181 × 181 = {181 * 181}, 182 × 182 = {182 * 182}) ; le chemin par le 1 ne dépasse jamais n",
   seuil == 182 and 181 * 181 == 32761 <= PLAFOND < 182 * 182 == 33124
   and all((n * n) // n == n * (n // n) == n and chemin_un(n) == n for n in range(1, PLAFOND + 1))
   and all((chemin_carre(n) > PLAFOND) == (n >= 182) for n in range(1, PLAFOND + 1)))
src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)
print("\n".join(out))
