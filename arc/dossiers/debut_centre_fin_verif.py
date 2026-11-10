# Le debut, le centre et la fin v0.3 : verification (R10). Python 3, aucune bibliotheque externe.
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
mir2 = all((10*a+b)+(10*b+a) == 11*(a+b) and abs((10*a+b)-(10*b+a)) == 9*abs(a-b) for a in range(1,10) for b in range(1,10))
check("81 nombres de deux chiffres : ab + ba = 11(a+b), |ab - ba| = 9|a-b|", mir2)
check("25+52 = 77, 45+54 = 99, 46+64 = 37+73 = 110 = 11 x 10, 64-46 = 18", 25+52 == 77 and 45+54 == 99 and 46+64 == 37+73 == 110 == 11*10 and 64-46 == 18)
check("paires d'inverses : n + miroir = 99 = 9 x 11", all((10*a+(9-a)) + (10*(9-a)+a) == 99 for a in range(1,9)))
def miroir(n): return int(str(n)[::-1])
check("11 x 18 = 198, miroir 891 = 11 x 81 ; 27 -> 297/792 ; 36 -> 396/693 ; 45 -> 495/594, tous sur 9",
      all(11*k == v and miroir(v) == 11*miroir(k) and R(v) == 9 for k, v in ((18,198),(27,297),(36,396),(45,495))))
check("11 x k et 11 x miroir(k) sont miroirs des que les chiffres de k font au plus 9",
      all(miroir(11*k) == 11*miroir(k) for k in range(10,100) if k%10 and sum(map(int,str(k))) <= 9))
def e11(n):                    # ecart au 11 : chiffres de rang impair moins chiffres de rang pair, replie sur 11
    s = str(n); return (sum(int(c) for c in s[-1::-2]) - sum(int(c) for c in s[-2::-2])) % 11
check("72 et 27, 1729 et 1279 : meme racine et meme fin, ecart au 11 different",
      R(72) == R(27) and R(1729) == R(1279) and cascade([1,7,2,9]) == cascade([1,2,7,9]) and e11(72) != e11(27) and e11(1729) != e11(1279))
paires = {(R(n), e11(n)) for n in range(1, 100000)}
check("la paire (racine, ecart au 11) prend 99 valeurs", len(paires) == 99)
def change_detectee(L):
    for n in range(10**(L-1), 10**L):
        s = str(n); key = (R(n), e11(n))
        for i in range(L):
            for d in "0123456789":
                if d != s[i]:
                    m = int(s[:i] + d + s[i+1:])
                    if m >= 10**(L-1) and (R(m), e11(m)) == key: return False
        for i in range(L-1):
            if s[i] != s[i+1]:
                m = int(s[:i] + s[i+1] + s[i] + s[i+2:])
                if m >= 10**(L-1) and (R(m), e11(m)) == key: return False
    return True
check("quatre chiffres, 0 compris : tout chiffre change ou tout echange de voisins differents change la paire", change_detectee(4))
check("six chiffres, 0 compris : idem", change_detectee(6))

# 11. Le centre est l'operateur
def blocs_ok(n):
    s = str(n)
    return all(R(sum(R(int(s[i:j])) for i, j in zip((0,)+cuts, cuts+(len(s),)))) == R(n)
               for k in range(1, len(s)) for cuts in itertools.combinations(range(1, len(s)), k))
check("toute coupe en blocs de tout nombre de 10 a 99 999 : la somme des adresses des blocs est l'adresse du tout",
      all(blocs_ok(n) for n in range(10, 100000)))
check("12795 : 12|7|95 -> (3,7,5), 1|279|5 -> (1,9,5), 1|27|9|5 -> (1,9,9,5), 1279|5 -> (1,5), toutes en 6",
      [R(R(12)+R(7)+R(95)), R(R(1)+R(279)+R(5)), R(1+R(27)+9+5), R(R(1279)+5)] == [6]*4 and R(12795) == 6)
check("163 : coque (1,3) en 4, centre 6 -> 1 ; 1729 : coque (1,9) en 1, centre 72 en 9 -> 1 ; 12795 : coque (1,5)(2,9) en 8, centre 7 -> 6",
      R(4+6) == R(163) == 1 and R(1+R(72)) == R(1729) == 1 and R(R(1+5+2+9) + 7) == R(12795) == 6)
rot = {c: [R(x + c) for x in range(1, 10)] for c in range(1, 10)}
check("centre 9 : identite ; centres a et 9-a : rotations inverses", rot[9] == list(range(1,10)) and all(R(R(x+a) + (9-a)) == x for a in range(1,9) for x in range(1,10)))
check("centre 5 applique de proche en proche parcourt tout : 5,1,6,2,7,3,8,4,9", [R(5*k) for k in range(1,10)] == [5,1,6,2,7,3,8,4,9])
check("centres 3 et 6 : l'axe reste sur l'axe, un rail reste sur un rail", all(R(x+c) in (3,6,9) for x in (3,6,9) for c in (3,6)) and all(R(x+c) in (1,4,7,2,5,8) for x in (1,2,4,5,7,8) for c in (3,6)))

# 12. Les trois gestes
def chiffres(n): return [int(c) for c in str(n)]
def ps(n): d = chiffres(n); return (d[0]+d[1], d[2]+d[3])
check("9 : (c-1, d+1), somme de la seconde paire conservee, 1000..9999", all(ps(n+9) == ps(n) for n in range(1000,10000) if chiffres(n)[2] <= 8 and chiffres(n)[3] >= 1))
check("900 : (a+1, b-1), somme de la premiere paire conservee", all(ps(n+900) == ps(n) for n in range(1000,9000) if chiffres(n)[0] <= 8 and chiffres(n)[1] >= 1))
check("891 = 1000-100-10+1 : (+1,-1,-1,+1), les deux sommes de paires conservees, la racine aussi, les tours +99",
      891 == 1000-100-10+1 and all(ps(n+891) == ps(n) and R(n+891) == R(n) and (n+891-R(n+891))//9 - (n-R(n))//9 == 99
                                   for n in range(1000,9000) if chiffres(n)[0] <= 8 and chiffres(n)[1] >= 1 and chiffres(n)[2] >= 1 and chiffres(n)[3] <= 8))
check("909 = 900+9 : (+1,-1,+1,-1), les deux sommes conservees", 909 == 900+9 and all(ps(n+909) == ps(n) for n in range(1000,9000) if chiffres(n)[0] <= 8 and chiffres(n)[1] >= 1 and chiffres(n)[2] <= 8 and chiffres(n)[3] >= 1))
check("2534 + 891 = 3425, 2534 - 891 = 1643 ; paires (7,7) ; racine 5 ; tours 281, 380, 182",
      2534+891 == 3425 and 2534-891 == 1643 and all(ps(n) == (7,7) for n in (2534,3425,1643)) and all(R(n) == 5 for n in (2534,3425,1643)) and [(n-5)//9 for n in (2534,3425,1643)] == [281,380,182])
cl = [n for n in range(1000,10000) if ps(n) == (5,5)]
check("trente nombres a paires (5,5), tous en 1", len(cl) == 30 and all(R(n) == 1 for n in cl))
huit = sorted(int(''.join(map(str,p))) for p in itertools.permutations([1,2,3,4]) if p[0]+p[1] == 5 and p[2]+p[3] == 5)
check("les huit nombres a chiffres 1,2,3,4 et partenaires cote a cote ; produits de paires 4 et 6",
      huit == [1423,1432,2314,2341,3214,3241,4123,4132] and all({chiffres(n)[0]*chiffres(n)[1], chiffres(n)[2]*chiffres(n)[3]} == {4,6} for n in huit))
check("classe (5,5) connexe par pas de 9 et de 900", (lambda S: (lambda reach: reach == S)((lambda f: f(f, {cl[0]}))(lambda f, seen: seen if not (new := {m for n in seen for m in (n+9,n-9,n+900,n-900) if m in S} - seen) else f(f, seen | new))))(set(cl)))
check("99 = 100-1 = 9 x 11 fait glisser les moities le long de l'involution : 1944, 2043, 2142, 2241, 2340",
      99 == 100-1 == 9*11 and [(R(n//100), R(n%100)) for n in (1944,2043,2142,2241,2340)] == [(1,8),(2,7),(3,6),(4,5),(5,4)] and all(R(n) == 9 for n in (1944,2043,2142,2241,2340)))

# 13. Les moities partenaires et les longueurs
check("1944 = 19|44 (1,8), 2835 = 28|35, 8253 = 82|53 ; tous en 9 ; 1944 = 9 x 6^3 ; 1944 + 891 = 2835",
      [(R(n//100), R(n%100)) for n in (1944,2835,8253)] == [(1,8)]*3 and all(R(n) == 9 for n in (1944,2835,8253)) and 1944 == 9*216 and 1944+891 == 2835)
check("2916 = 29|16 (2,7) = 54^2 ; 2142 (3,6) ; 2241 (4,5)", (R(29),R(16)) == (2,7) and 2916 == 54**2 and (R(21),R(42)) == (3,6) and (R(22),R(41)) == (4,5))
check("quatre chiffres : moities inverses => tout en 9, sans exception", all(R(n) == 9 for n in range(1000,10000) if R(n//100) + R(n%100) == 9))
check("famille du 1 a deux chiffres : 10, 19, 28, 37, 46, 55, 64, 73, 82, 91 ; des 19, chiffres sommant a 10",
      [n for n in range(10,100) if R(n) == 1] == [10,19,28,37,46,55,64,73,82,91] and all(sum(chiffres(n)) == 10 for n in (19,28,37,46,55,64,73,82,91)))
check("19 x 91 = 1729 ; 37 x 73 = 2701 = 73e triangulaire ; (9a+1)(9b+1) = 9(9ab+a+b)+1 ; tours de 1729 = 192",
      19*91 == 1729 and 37*73 == 2701 == 73*74//2 and all((9*a+1)*(9*b+1) == 9*(9*a*b+a+b)+1 for a in range(60) for b in range(60)) and 9*2*10+2+10 == 192 == (1729-1)//9)
def coupes(L): return sorted({(L//b, b) for b in range(2, L) if L % b == 0})
check("coupes regulieres : 4 -> 2x2 ; 6 -> 2x3, 3x2 ; 8 -> 2x4, 4x2 ; 9 -> 3x3 ; aucune pour 3, 5, 7",
      coupes(4) == [(2,2)] and coupes(6) == [(2,3),(3,2)] and coupes(8) == [(2,4),(4,2)] and coupes(9) == [(3,3)] and all(coupes(L) == [] for L in (3,5,7)))
check("234567891 coupe en 3x3 = 234 / 567 / 891", [234567891//10**6, (234567891//1000)%1000, 234567891%1000] == [234,567,891])

# 14. Les paires sous les trois operations
inv_s = [(1,8),(2,7),(3,6),(4,5)]; inv_p = [(1,1),(2,5),(4,7),(8,8)]
check("inverses de somme : difference = double (27 - 2x ferme sur l'inverse de 2x) ; produit = inverse du carre",
      all(R(27 - 2*x) == inv(R(2*x)) for x in range(1,9)) and all(R(x*y) == inv(R(x*x)) for x, y in inv_s))
check("inverses de produit : somme sur (2,7) ; difference sur l'axe", all(R(x+y) in (2,7) for x, y in inv_p) and all(R(abs(x-y)+9) in (3,6,9) for x, y in inv_p))
D, G, A = {1,4,7}, {2,5,8}, {3,6,9}
rail = lambda x: 'D' if x in D else 'G' if x in G else 'A'
check("rails : D+D->G, G+G->D, D+G->A ; D-D, G-G -> A, D-G -> G, G-D -> D ; DxD->D, GxG->D, DxG->G ; axe absorbe le produit",
      all(rail(R(a+b)) == 'G' for a in D for b in D) and all(rail(R(a+b)) == 'D' for a in G for b in G) and all(rail(R(a+b)) == 'A' for a in D for b in G)
      and all(rail(R(a-b+9)) == 'A' for a in D for b in D) and all(rail(R(a-b+9)) == 'A' for a in G for b in G)
      and all(rail(R(a-b+9)) == 'G' for a in D for b in G) and all(rail(R(a-b+9)) == 'D' for a in G for b in D)
      and all(rail(R(a*b)) == 'D' for a in D for b in D) and all(rail(R(a*b)) == 'D' for a in G for b in G) and all(rail(R(a*b)) == 'G' for a in D for b in G)
      and all(rail(R(a*b)) == 'A' for a in A for b in range(1,10)))
check("73 - 37 = 36, 37 - 19 = 18, 91 - 19 = 72 : sur l'axe", all(R(d) == 9 for d in (73-37, 37-19, 91-19)))
check("typographie : aucun tiret cadratin dans la source", "—" not in open(__import__("sys").argv[1], encoding="utf-8").read() if len(__import__("sys").argv) > 1 else True)

print(f"\n{ok} verifications, aucun echec.")
