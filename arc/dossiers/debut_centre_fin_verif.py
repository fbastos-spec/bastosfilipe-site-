# Le debut, le centre et la fin v0.1 : verification (R10). Python 3, aucune bibliotheque externe.
# Chaque nombre cite dans le document est recalcule ici ; une assertion qui echoue arrete le build.
import itertools
from math import comb, prod

def R(n):                      # racine : somme iteree des chiffres, le 9 reste 9
    return 1 + (n - 1) % 9 if n else 0

def cascade(d):                # chaque chiffre s'unit a son voisin, l'union est repliee par la racine
    d = list(d)
    while len(d) > 1:
        d = [R(d[i] + d[i + 1]) for i in range(len(d) - 1)]
    return d[0]

def inv(x):                    # l'inverse dans la somme : x et 9 - x ferment sur 9
    return 9 - x if x != 9 else 9

ok = 0
def check(label, cond):
    global ok
    assert cond, label
    ok += 1
    print("[OK]", label)

Q = list(itertools.product(range(1, 10), repeat=4))       # 6 561 nombres de quatre chiffres sans 0

# 2. La cascade en nombres
check("1729 -> 892 -> 82 -> 1", cascade([1, 7, 2, 9]) == 1 and [R(1+7), R(7+2), R(2+9)] == [8, 9, 2])
check("1279 -> 397 -> 37 -> 1", cascade([1, 2, 7, 9]) == 1 and [R(1+2), R(2+7), R(7+9)] == [3, 9, 7])
check("2728 -> 991 -> 91 -> 1", cascade([2, 7, 2, 8]) == 1)
check("poids de Pascal a quatre chiffres : 1, 3, 3, 1", [comb(3, i) for i in range(4)] == [1, 3, 3, 1])

# 3. La loi du debut, du centre et de la fin
check("6 561 nombres : la fin vaut les extremites plus trois fois le centre",
      len(Q) == 6561 and all(cascade(t) == R(t[0] + t[3] + 3 * (t[1] + t[2])) for t in Q))

# 4. Le centre selon son rail
pas = {1: 3, 4: 3, 7: 3, 2: 6, 5: 6, 8: 6, 3: 9, 6: 9, 9: 9}
check("rail {1,4,7} : 3, 12, 21 ferment sur 3", {R(3 * c) for c in (1, 4, 7)} == {3})
check("rail {2,5,8} : 6, 15, 24 ferment sur 6", {R(3 * c) for c in (2, 5, 8)} == {6})
check("axe {3,6,9} : 9, 18, 27 ferment sur 9", {R(3 * c) for c in (3, 6, 9)} == {9})
check("6 561 nombres : la fin vaut les extremites plus le pas du rail du centre",
      all(cascade(t) == R(t[0] + t[3] + pas[R(t[1] + t[2])]) for t in Q))

# 5. Le theoreme de l'inverse
cas = [t for t in Q if R(t[0] + t[3]) != 9 and R(t[1] + t[2]) == 9 - R(t[0] + t[3])]
check(f"{len(cas)} nombres a extremites x et centre 9 - x : la fin est l'inverse du double de x",
      all(cascade(t) == inv(R(2 * R(t[0] + t[3]))) for t in cas))
check("x = 7 : fin 4", inv(R(2 * 7)) == 4)
check("table x -> fin : 1->7, 2->5, 3->3, 4->1, 5->8, 6->6, 7->4, 8->2",
      [inv(R(2 * x)) for x in range(1, 9)] == [7, 5, 3, 1, 8, 6, 4, 2])

# 6. La symbiose
sym4 = [t for t in Q if cascade(t) == R(sum(t))]
check("quatre chiffres : 729 nombres ou cascade et racine tombent ensemble",
      len(sym4) == 729 and set(sym4) == {t for t in Q if R(t[1] + t[2]) == 9})
T3 = list(itertools.product(range(1, 10), repeat=3))
sym3 = [t for t in T3 if cascade(t) == R(sum(t))]
check("trois chiffres : 81 nombres, exactement ceux dont le centre est 9",
      len(sym3) == 81 and all(t[1] == 9 for t in sym3))
T6 = list(itertools.product(range(1, 10), repeat=6))
check("six chiffres : symbiose si et seulement si la deuxieme couche (2e, 5e) ferme sur 9",
      all((cascade(t) == R(sum(t))) == (R(t[1] + t[4]) == 9) for t in T6))
check("six chiffres : 59 049 nombres sur 531 441", sum(cascade(t) == R(sum(t)) for t in T6) == 59049 and len(T6) == 531441)
T5 = list(itertools.product(range(1, 10), repeat=5))
check("cinq chiffres : symbiose si et seulement si 3 x (2e + 4e) + 5 x centre ferme sur 9",
      all((cascade(t) == R(sum(t))) == (R(3 * (t[1] + t[3]) + 5 * t[2]) == 9) for t in T5))
check("cinq chiffres : 6 561 nombres sur 59 049", sum(cascade(t) == R(sum(t)) for t in T5) == 6561)

# 7. Les bouts et le coeur
bad = 0; ends9 = 0; ends9_ok = 0
for n in range(10, 10**6):
    s = str(n); a, z = int(s[0]), int(s[-1]); c = sum(map(int, s[1:-1]))
    if R(R(a + z) + R(c)) != R(n) if c else R(a + z) != R(n): bad += 1
    if a + z == 9:
        ends9 += 1
        if (R(c) if c else 9) == R(n): ends9_ok += 1
check("de 10 a 999 999 : l'adresse est la cloture des bouts plus le coeur, sans exception", bad == 0)
check("99 999 nombres a bouts inverses : le coeur porte seul l'adresse", ends9 == 99999 and ends9_ok == 99999)
check("1729 et 2728 : bouts 10, coeur 9, adresse 1",
      all(R(int(s[0]) + int(s[-1])) == 1 and R(int(s[1]) + int(s[2])) == 9 and R(int(s)) == 1 for s in ("1729", "2728")))
check("quatre chiffres : bouts sommant 10 et coeur sommant 9 : 90 nombres",
      sum(1 for n in range(1000, 10000) if int(str(n)[0]) + int(str(n)[3]) == 10 and int(str(n)[1]) + int(str(n)[2]) == 9) == 90)
check("1729 + 999 = 2728", 1729 + 999 == 2728)
check("inverses du produit : 2 x 5, 4 x 7, 1 x 1, 8 x 8 ferment sur 1",
      [R(2*5), R(4*7), R(1*1), R(8*8)] == [1, 1, 1, 1] and
      sorted((a, b) for a in range(1, 10) for b in range(a, 10) if R(a * b) == 1) == [(1, 1), (2, 5), (4, 7), (8, 8)])
tot = okp = 0
for n in range(1000, 10**6):
    s = str(n)
    if "0" in s: continue
    if R(int(s[0]) * int(s[-1])) == 1:
        tot += 1
        okp += R(prod(map(int, s))) == R(prod(map(int, s[1:-1])))
check("44 226 nombres (4 a 6 chiffres, sans 0) a bouts inverses du produit : le coeur porte le produit",
      tot == 44226 and okp == tot)

# 8. Le carre des quatre partenaires
def chiffres(n): return [int(c) for c in str(n)]
check("1257 : cascade 2, racine 6 ; 7521 : 2, 6 ; 8742 : 7, 3 ; 2478 : 7, 3",
      [(cascade(chiffres(n)), R(n)) for n in (1257, 7521, 8742, 2478)] == [(2, 6), (2, 6), (7, 3), (7, 3)])
nb = 0; mir = invk = True
for L in range(2, 7):
    for t in itertools.product(range(1, 10), repeat=L):
        nb += 1
        if cascade(t) != cascade(t[::-1]) or R(sum(t)) != R(sum(t[::-1])): mir = False
        u = tuple(9 - x for x in t)
        if 0 in u: continue
        if cascade(u) != inv(cascade(t)) or R(sum(u)) != inv(R(sum(t))): invk = False
check(f"{nb} nombres de 2 a 6 chiffres : le miroir garde la cascade et la racine", nb == 597861 and mir)
check("le meme releve : l'inverse inverse la cascade et la racine", invk)

# 9. Les positions lues
lues = {L: [i for i in range(L) if comb(L - 1, i) % 9] for L in (10, 28, 82)}
check("longueur 10 : rangs 0, 3, 6, 9", lues[10] == [0, 3, 6, 9])
check("longueur 28 : rangs 0, 9, 18, 27", lues[28] == [0, 9, 18, 27])
check("longueur 82 : rangs 0, 27, 54, 81", lues[82] == [0, 27, 54, 81])

# 10. Le 11 : le miroir et le sens du coeur
def miroir(n): return int(str(n)[::-1])
deux = [(a, b) for a in range(1, 10) for b in range(1, 10)]
check("81 nombres de deux chiffres : n + miroir = 11 x (a + b)", all((10*a+b) + (10*b+a) == 11*(a+b) for a, b in deux))
check("81 nombres de deux chiffres : le plus grand moins le plus petit = 9 x l'ecart des chiffres",
      all(max(10*a+b, 10*b+a) - min(10*a+b, 10*b+a) == 9*abs(a-b) for a, b in deux))
check("25 + 52 = 77 ; 45 + 54 = 99 ; 46 + 64 = 37 + 73 = 110 ; 64 - 46 = 18",
      25+52 == 77 and 45+54 == 99 and 46+64 == 110 and 37+73 == 110 and 64-46 == 18)
check("11 x k et 11 x miroir(k) sont miroirs des que les deux chiffres de k font au plus 9",
      all(miroir(11*(10*a+b)) == 11*(10*b+a) for a, b in deux if a+b <= 9))
check("198/891, 297/792, 396/693, 495/594 : onze fois les paires d'inverses, racine 9",
      [(11*k, miroir(11*k)) for k in (18, 27, 36, 45)] == [(198, 891), (297, 792), (396, 693), (495, 594)]
      and all(R(11*k) == 9 for k in (18, 27, 36, 45, 54, 63, 72, 81)))
def ecart11(d):                # somme des rangs impairs et des rangs pairs, l'ecart replie sur le 11
    return (sum(d[0::2]) - sum(d[1::2])) % 11
check("72 et 27 : meme racine, ecart au 11 distinct", R(72) == R(27) and ecart11([7, 2]) != ecart11([2, 7]))
check("1729 et 1279 : meme fin, meme racine, ecart au 11 distinct",
      cascade([1,7,2,9]) == cascade([1,2,7,9]) and R(1729) == R(1279) and ecart11([1,7,2,9]) != ecart11([1,2,7,9]))
for L in (4, 6):
    sep = True; vals = set()
    for t in itertools.product(range(10), repeat=L):
        v = (R(sum(t)), ecart11(t)); vals.add(v)
        for i in range(L):
            for y in range(10):
                if y != t[i]:
                    e = list(t); e[i] = y
                    if (R(sum(e)), ecart11(e)) == v: sep = False
        for i in range(L - 1):
            if t[i] != t[i+1]:
                e = list(t); e[i], e[i+1] = e[i+1], e[i]
                if (R(sum(e)), ecart11(e)) == v: sep = False
    check(f"{10**L} nombres de {L} chiffres (0 compris) : un chiffre change ou deux voisins echanges changent toujours la paire (racine, ecart au 11)", sep)
check("la paire prend 99 valeurs hors du nombre nul : 9 x 11", len({(R(sum(t)), ecart11(t)) for t in itertools.product(range(10), repeat=4) if any(t)}) == 99)

print(f"\n{ok} verifications, aucun echec.")
