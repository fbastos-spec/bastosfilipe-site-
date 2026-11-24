# projection_echelle_verif.py
# Controles de la piece "La preuve par projection d'echelle" (Corpus ARC, Filipe Bastos).
# Calcul entier exact, sauf le bloc Mandelbrot (flottants double precision, declare).
from math import isqrt, pi
from fractions import Fraction
ok = 0; tot = 0
def controle(nom, cond, detail=""):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(("CONFORME " if cond else "ECART    ") + nom + ((" : " + str(detail)) if detail != "" else ""))

def dr(n):
    r = n % 9
    return 9 if r == 0 else r

# 1. Les deux carres autour de 6m : l'ecart vaut m sauts de 24
M = 10**6
controle("1. (6m+1)^2 - (6m-1)^2 = 24m pour m = 1 a 10^6",
         all((6*m+1)**2 - (6*m-1)**2 == 24*m for m in range(1, M+1)))
controle("2. exemples 25/49, 121/169, 289/361", (49-25, 169-121, 361-289) == (24, 48, 72), (49-25, 169-121, 361-289))
m = 10**9
A, B = (6*m-1)**2, (6*m+1)**2
controle("3. echelle un milliard : ecart / 24 rend le rang", (B-A) % 24 == 0 and (B-A)//24 == m, (B-A)//24)
m = 7 * 10**30 + 3
A, B = (6*m-1)**2, (6*m+1)**2
controle("4. echelle 7 x 10^30 + 3 : meme lecture", (B-A)//24 == m and (B-A) % 24 == 0)

# 2. Lecture a l'envers : test d'une paire de carres
def est_paire(A, B):
    # A < B deux carres ; paire autour d'un 6m ?
    if B <= A: return None
    d = B - A
    if d % 24: return None
    if 8*(A+B) != d*d + 16: return None
    return d // 24
controle("5. test 8(A+B) = (B-A)^2 + 16 vrai sur toutes les paires, m = 1 a 10^5",
         all(est_paire((6*m-1)**2, (6*m+1)**2) == m for m in range(1, 10**5+1)))
carres = [n*n for n in range(1, 400)]
faux = [(a, b) for i, a in enumerate(carres) for b in carres[i+1:] if est_paire(a, b) is not None
        and not (isqrt(b) - isqrt(a) == 2 and (isqrt(a)+1) % 6 == 0)]
controle("6. le test ne retient aucune autre paire de carres (carres de 1 a 399)", faux == [], len(faux))

# 3. Sauts de 24 depuis 1 : rang du saut = m(3m-1)/2 ou m(3m+1)/2
rangs = []
good = True
for m in range(1, 2001):
    for s in (-1, 1):
        n = 6*m + s
        q, r = divmod(n*n - 1, 24)
        good &= (r == 0 and q == m*(3*m+s)//2)
        rangs.append(q)
controle("7. (6m-1)^2 et (6m+1)^2 = 1 + 24 x m(3m-1)/2 et 1 + 24 x m(3m+1)/2, m = 1 a 2000", good)
controle("8. premiers rangs de saut : 1, 2, 5, 7, 12, 15, 22, 26", sorted(rangs)[:8] == [1, 2, 5, 7, 12, 15, 22, 26], sorted(rangs)[:8])

# 4. La position se garde d'un registre a l'autre
import random
random.seed(9)
g = True
for _ in range(20000):
    a = random.randrange(1, 10**12); b = random.randrange(1, 10**12)
    g &= dr(a*b) == dr(dr(a)*dr(b)) and dr(a+b) == dr(dr(a)+dr(b))
    k, r = (a - dr(a)) // 9, dr(a)
    g &= a == 9*k + r and 1 <= r <= 9
controle("9. n = 9k + position (1 a 9), position du produit et de la somme lues sur les positions, 20 000 tirages", g)
controle("10. positions des carres des places des rails : seulement 1, 4, 7",
         {dr((6*m+s)**2) for m in range(1, 5000) for s in (-1, 1)} == {1, 4, 7})

# 5. Le compte d'une echelle lu dans l'echelle du dessous (Legendre 1808)
def crible(N):
    s = bytearray([1])*(N+1); s[0:2] = b"\0\0"
    for i in range(2, isqrt(N)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return s
N = 10**6
s = crible(N)
P = [i for i in range(2, 1001) if s[i]]
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(maxsize=None)
def phi(x, a):
    if a == 0: return x
    if x == 0: return 0
    return phi(x, a-1) - phi(x // P[a-1], a-1)
compte = phi(N, len(P)) + len(P) - 1
controle("11. premiers jusqu'a 10^6 par les 168 premiers jusqu'a 1000 seulement : 78 498", compte == sum(s) == 78498, compte)

# 6. Jumeaux : rangs libres sur un tour = produit des (g - 2)
def libres(gs):
    T = 1
    for g in gs: T *= g
    c = 0
    for k in range(1, T+1):
        if all((6*k-1) % g and (6*k+1) % g for g in gs): c += 1
    return c, T
res = [libres(gs) for gs in ([5, 7], [5, 7, 11], [5, 7, 11, 13], [5, 7, 11, 13, 17])]
controle("12. rangs libres des deux cotes sur un tour : 15/35, 135/385, 1485/5005, 22275/85085",
         res == [(15, 35), (135, 385), (1485, 5005), (22275, 85085)], res)
prod = [3*5, 3*5*9, 3*5*9*11, 3*5*9*11*15]
controle("13. ces comptes sont les produits des (g - 2)", [r[0] for r in res] == prod, prod)
part = [Fraction(*r) for r in res]
controle("14. la part baisse a chaque etage et ne s'annule a aucun", all(part[i] > part[i+1] > 0 for i in range(3)),
         [round(float(p)*100, 2) for p in part])
jum = [k for k in range(1, N//6) if s[6*k-1] and s[6*k+1]]
controle("15. rangs k ou 6k-1 et 6k+1 sont premiers tous deux, jusqu'a 10^6 : 8 168", len(jum) == 8168, len(jum))
tw = sum(1 for p in range(3, N-1) if s[p] and s[p+2])
controle("16. paires de jumeaux jusqu'a 10^6 : 8 169", tw == 8169, tw)

# 7. Mandelbrot : il faut iterer pour savoir ; pres du bord le compte de pas grandit sans plafond
def pas_de_fuite(c, lim=10**8):
    z = 0.0; n = 0
    while abs(z) <= 2 and n < lim:
        z = z*z + c; n += 1
    return n
vals = []
for e in (1e-2, 1e-4, 1e-6, 1e-8):
    n = pas_de_fuite(0.25 + e)
    vals.append((e, n, n * e**0.5))
print("    c = 1/4 + e :", [(e, n, round(x, 4)) for e, n, x in vals])
controle("17. c = 1/4 : la suite reste bornee (jamais au-dela de 1/2 en 10^6 pas)", (lambda: (lambda z: z <= 0.5)(
    __import__("functools").reduce(lambda z, _: z*z + 0.25, range(10**6), 0.0)))())
controle("18. c = 1/4 + e : pas avant la fuite 30, 312, 3 140, 31 414", [v[1] for v in vals] == [30, 312, 3140, 31414], [v[1] for v in vals])
controle("19. pas x point d'ecart : 3,0 puis 3,12 puis 3,140 puis 3,1414 (pi = 3,14159...)",
         abs(vals[-1][2] - pi) < 3e-4 and all(abs(vals[i+1][2]-pi) < abs(vals[i][2]-pi) for i in range(3)), [round(v[2], 5) for v in vals])
# rayon de fuite : au-dela de 2, la suite ne revient pas (controle sur une grille)
g = True
for i in range(-40, 41):
    for j in range(-40, 41):
        c = complex(i/20, j/20)
        if abs(c) > 2: continue
        z = 0j; sorti = False
        for _ in range(200):
            z = z*z + c
            if sorti and abs(z) <= 2: g = False
            if abs(z) > 2: sorti = True
            if abs(z) > 1e6: break
controle("20. une fois sortie du rayon 2, la suite n'y rentre pas (grille de 6 561 valeurs de c, 200 pas)", g)

# 8. Les briques du Volume 2, chapitre 12
controle("21. 22 + 23 = 45, 31 + 32 = 63, 220 + 221 = 441 ; positions (4, 5) chaque fois",
         (22+23, 31+32, 220+221) == (45, 63, 441) and all((dr(a), dr(b)) == (4, 5) for a, b in ((22, 23), (31, 32), (220, 221))))
# 9. Le relais : 5 x 7 + 1 = 36 et 49 - 25 = 24
controle("22. 5 x 7 + 1 = 36 = 6^2 ; (6m-1)(6m+1) + 1 = (6m)^2 pour m = 1 a 10^5",
         5*7+1 == 36 and all((6*m-1)*(6*m+1)+1 == (6*m)**2 for m in range(1, 10**5+1)))
controle("23. somme des deux bords 12m, produit de position 8, m = 1 a 10^5",
         all((6*m-1)+(6*m+1) == 12*m and dr((6*m-1)*(6*m+1)) == 8 for m in range(1, 10**5+1)))

# 10. La premiere piece sur Riemann (fevrier 2026) : la position decide a toute taille
# Corps du nonagone : x^3 - 3x + 1 (racines 2cos(2pi/9), 2cos(4pi/9), 2cos(8pi/9))
Pm = [p for p in range(5, 20000) if s[p]]
def nrac(p): return sum(1 for x in range(p) if (x*x*x - 3*x + 1) % p == 0)
tab = {}
gg = True
for p in Pm[:600]:
    r = nrac(p); pos = dr(p)
    gg &= (r == 3) == (pos in (1, 8)) and r in (0, 3)
    tab.setdefault(pos, set()).add(r)
controle("24. x^3 - 3x + 1 a trois solutions chez p quand la position de p est 1 ou 8, aucune sinon (600 premiers depuis 5)", gg, {k: sorted(v) for k, v in sorted(tab.items())})
# caractere cubique de conducteur 9 : constant sur chaque paire d'inverses
import cmath
w = cmath.exp(2j*cmath.pi/3)
chi = {}
x = 1
for e in range(6):
    chi[x] = w**e; x = (x*2) % 9
paires = [(1, 8), (2, 7), (4, 5)]
controle("25. le caractere cubique de 9 prend la meme valeur sur les deux membres de chaque paire (1,8), (2,7), (4,5)",
         all(abs(chi[a]-chi[b]) < 1e-12 for a, b in paires), [(a, b, round((cmath.phase(chi[a])*3/(2*pi)) % 3)) for a, b in paires])
controle("26. les trois valeurs somment a zero : 1 + w + w^2 = 0", abs(sum(chi[a] for a, _ in paires)) < 1e-12)
cnt = {pp: 0 for pp in paires}
for p in range(5, N+1):
    if s[p]:
        d = dr(p)
        for pp in paires:
            if d in pp: cnt[pp] += 1
controle("27. premiers de 5 a 10^6 par paire : 26 162 / 26 196 / 26 138", list(cnt.values()) == [26162, 26196, 26138], list(cnt.values()))
big = 10**100 + 267   # entier de 101 chiffres ; sa position se lit sans le factoriser
controle("28. un entier de 101 chiffres : position lue sur ses chiffres = position de 9k + r", dr(big) == (sum(map(int, str(big))) - 1) % 9 + 1, dr(big))
controle("29. demi-envergure sur envergure = 1/2 pour chaque paire (x, 9 - x), x = 1 a 4",
         all(Fraction(9-2*x, 2) / (9-2*x) == Fraction(1, 2) for x in range(1, 5)))

# 11. Le pli universel (Octet Rule, aout 2025) : la table de tout entier se plie en quatre paires
controle("30. positions de ka et de (9-k)a : somme 9, ou 18 quand les deux sont 9, a = 1 a 10^5",
         all(dr(k*a)+dr((9-k)*a) in (9, 18) for a in range(1, 10**5+1) for k in range(1, 5)))
gros = 7 * 10**40 + 12345
controle("31. meme pli pour un multiplicateur de 41 chiffres ; la table de 5 : 5,1,6,2,7,3,8,4,9",
         all(dr(k*gros)+dr((9-k)*gros) in (9, 18) for k in range(1, 5)) and [dr(5*k) for k in range(1, 10)] == [5,1,6,2,7,3,8,4,9])
print()
print(f"{tot} controles, {ok} conformes")
