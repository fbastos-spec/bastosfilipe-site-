# Le Zero non construisible v0.3 : verification (R10). Python, numpy, scipy.
import re, sys
from math import factorial, pi, log, exp
import numpy as np
from scipy.special import loggamma

ok = True
SORTIE = []
def dire(x=""):
    SORTIE.append(x); print(x)
def check(label, cond):
    global ok
    dire(("[OK] " if cond else "[ECHEC] ") + label)
    ok = ok and bool(cond)

src = open(sys.argv[1], encoding="utf-8").read()
tete, corps = src.split("\n## Avant-propos", 1)
corps = corps.split("## Annexe")[0]
B = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510, 43867/798, -174611/330]
def zeta(s, N=60):                       # Euler-Maclaurin, valable pour tout s complexe hors de 1
    s = complex(s); n = np.arange(1, N)
    tot = np.sum(n ** (-s)) + N ** (1 - s) / (s - 1) + 0.5 * N ** (-s); f = s
    for k in range(1, 11):
        tot += B[k - 1] / factorial(2 * k) * f * N ** (-s - 2 * k + 1); f *= (s + 2 * k - 1) * (s + 2 * k)
    return tot
Lam = lambda s: pi ** (-s / 2) * np.exp(loggamma(s / 2)) * zeta(s)

dire("0. Typographie et mots")
check("aucun tiret long ni moyen", chr(0x2014) not in src and chr(0x2013) not in src)
hors = re.sub(r"«[^»]*»", "", tete + corps).lower()
bannis = ["hasard", "moyenne", "modulo", "instabilit", "oppos", "apoph"]
check(f"aucun mot banni hors citation ({len(bannis)} racines)", not any(b in hors for b in bannis))

dire("1. Le zero d'une paire est au centre")
check("2x - 9 ne s'annule qu'en 4,5 ; aucune position de 1 a 9 ne l'annule", all(2 * x - 9 != 0 for x in range(1, 10)) and 2 * 4.5 - 9 == 0)
check("2 et 7 : 2 + 7 = 9 et (2 + 7)/2 = 4,5", 2 + 7 == 9 and (2 + 7) / 2 == 4.5)

dire("2. Avec le produit d'Euler, zeta ne s'annule pas (sigma = 1,1)")
sig = 1.1; borne = (zeta(2 * sig) / zeta(sig)).real
mini = min(abs(zeta(sig + 1j * t)) for t in np.arange(0, 200, 0.05))
check(f"min |zeta| sur t de 0 a 200 = {mini:.4f}, au-dessus de zeta(2,2)/zeta(1,1) = {borne:.4f}", mini >= borne > 0)

dire("3. Dans la bande, le denominateur 1 - 2^(1-s) ne s'annule pas")
ok3 = all(abs(1 - 2 ** (1 - complex(x, t))) >= 2 ** (1 - x) - 1 - 1e-12 and 2 ** (1 - x) - 1 > 0
          for x in np.arange(0.05, 1.0, 0.05) for t in np.arange(0, 60, 0.5))
check("|1 - 2^(1-s)| >= 2^(1-sigma) - 1 > 0 sur une grille de la bande", ok3)

dire("4. Au premier zero, eta s'annule")
rho = 0.5 + 14.134725141734693j
den = 1 - 2 ** (1 - rho); eta = zeta(rho) * den
check(f"|zeta(rho)| et |eta(rho)| sous 10^-10 ; |1 - 2^(1-rho)| = {abs(den):.2f}",
      abs(zeta(rho)) < 1e-10 and abs(eta) < 1e-10 and round(abs(den), 2) == 2.37)

dire("5. Sur la droite, l'inverse et le miroir coincident : Lambda est reelle")
r_droite = max(abs(Lam(0.5 + 1j * t).imag) / abs(Lam(0.5 + 1j * t).real) for t in (5.0, 20.0, 33.0))
r_hors = min(abs(Lam(0.7 + 1j * t).imag) / abs(Lam(0.7 + 1j * t).real) for t in (5.0, 20.0, 33.0))
check(f"|Im/Re| sur la droite : sous 10^-12 ; a 0,7 : au moins {r_hors:.1e}", r_droite < 1e-12 and r_hors > 1e-2)
check("equation fonctionnelle Lambda(s) = Lambda(1 - s) a 10^-12 pres (s = 0,3 + 2i)",
      abs(Lam(0.3 + 2j) - Lam(0.7 - 2j)) / abs(Lam(0.3 + 2j)) < 1e-12)

dire("6. La face finie : critere de Lagarias jusqu'a 100 000")
N = 100000; sd = [0] * (N + 1)
for d in range(1, N + 1):
    for m in range(d, N + 1, d): sd[m] += d
H = 1.0; pire = (1e9, 0); viol = []
for n in range(2, N + 1):
    H += 1 / n; b = H + exp(H) * log(H)
    if sd[n] > b: viol.append(n)
    if (b - sd[n]) / b < pire[0]: pire = ((b - sd[n]) / b, n)
check(f"sigma(n) <= H + e^H ln H pour n de 2 a {N} : violations {viol} ; marge minimale {100 * pire[0]:.2f} % en n = {pire[1]}",
      viol == [] and pire[1] == 12 and abs(100 * pire[0] - 1.1) < 0.1)

dire("7. Doubler, carrer, et la porte de Riemann")
from scipy.integrate import quad
from scipy.special import gamma as G
psi = lambda x: sum(exp(-k * k * pi * x) for k in range(1, 60))
check("Jacobi : 2psi(x) + 1 = x^(-1/2) (2psi(1/x) + 1) a x = 0,5 et 1,7 (10^-12 pres)",
      all(abs((2 * psi(x) + 1) - x ** -0.5 * (2 * psi(1 / x) + 1)) < 1e-12 for x in (0.5, 1.7)))
I = quad(lambda x: exp(-4 * pi * x) * x ** 0.5, 0, float("inf"))[0]
check(f"integrale de e^(-n^2 pi x) x^(s/2-1) = Gamma(s/2) pi^(-s/2) / n^s (n = 2, s = 3) : {I:.10f}",
      abs(I - G(1.5) * pi ** -1.5 / 8) < 1e-10)
check("2n = n^2 n'a qu'une solution de 1 a 10 000 : n = 2, valeur 4",
      [k for k in range(1, 10001) if 2 * k == k * k] == [2])
DR = lambda m: 1 + (m - 1) % 9
check("DR(x^2) = DR((9 - x)^2) pour x de 1 a 8 ; huit positions, quatre racines, deux par deux",
      all(DR(x * x) == DR((9 - x) ** 2) for x in range(1, 9)) and len({DR(x * x) for x in range(1, 9)}) == 4)

dire("8. Le compte des statuts")
n = {"Th": len(re.findall(r"\*\*Th\.\*\*", corps)), "F": len(re.findall(r"\*\*F\.\*\*", corps)), "L": len(re.findall(r"\*\*L\.\*\*", corps))}
m = re.search(r"Statuts : Théorèmes (\d+), Lectures (\d+), Faits (\d+)", tete)
ecrit = tuple(int(x) for x in m.groups()) if m else None
check(f"statuts annonces {ecrit} = statuts comptes {(n['Th'], n['L'], n['F'])} (Th, L, F)", ecrit == (n["Th"], n["L"], n["F"]))
dire("VERDICT : " + ("TOUTES LES VERIFICATIONS PASSENT" if ok else "AU MOINS UN ECHEC"))
if len(sys.argv) > 2:
    open(sys.argv[2], "w", encoding="utf-8").write("\n".join(SORTIE))
assert ok
