# -*- coding: utf-8 -*-
# Les trois corps n'ont jamais bougé, v1.2 : recontrôle du 18 novembre 2026 (sections 2.2, 3.1, 3.2 et 4.1).
# Python 3, bibliothèque standard seule. Durée : quelques minutes.
# Protocole, dit en entier : problème de Burrau (masses 3, 4, 5 en (1, 3), (-2, -1), (1, -1), au repos, G = 1) ;
# saute-mouton en forme poussée, glissement, poussée ; écart d'énergie = |E - E0| / |E0|, relevé à chaque pas ;
# troncature vers zéro des positions et des vitesses après chaque pas, puis forces recalculées.
from math import sqrt, trunc
M = [3.0, 4.0, 5.0]
def depart(): return [1.0, -2.0, 1.0], [3.0, -1.0, -1.0], [0.0] * 3, [0.0] * 3
def forces(x, y):
    ax = [0.0] * 3; ay = [0.0] * 3
    for i in range(3):
        for j in range(i + 1, 3):
            dx = x[j] - x[i]; dy = y[j] - y[i]; r2 = dx * dx + dy * dy; r3 = r2 * sqrt(r2)
            ax[i] += M[j] * dx / r3; ay[i] += M[j] * dy / r3; ax[j] -= M[i] * dx / r3; ay[j] -= M[i] * dy / r3
    return ax, ay
def energie(x, y, vx, vy):
    e = sum(0.5 * M[i] * (vx[i] ** 2 + vy[i] ** 2) for i in range(3))
    for i in range(3):
        for j in range(i + 1, 3): e -= M[i] * M[j] / sqrt((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2)
    return e
def calcul(h, duree, dec=None, reperes=()):
    x, y, vx, vy = depart(); e0 = energie(x, y, vx, vy); ax, ay = forces(x, y)
    f = 10.0 ** dec if dec else None
    n = int(round(duree / h)); n10 = int(round(10 / h)); rep = {int(round(t / h)): t for t in reperes}
    emax = 0.0; pmax = 0.0; lmax = 0.0; lieux = {}
    for s in range(1, n + 1):
        for i in range(3):
            vx[i] += 0.5 * h * ax[i]; vy[i] += 0.5 * h * ay[i]; x[i] += h * vx[i]; y[i] += h * vy[i]
        ax, ay = forces(x, y)
        for i in range(3): vx[i] += 0.5 * h * ax[i]; vy[i] += 0.5 * h * ay[i]
        if f:
            for i in range(3):
                x[i] = trunc(x[i] * f) / f; y[i] = trunc(y[i] * f) / f; vx[i] = trunc(vx[i] * f) / f; vy[i] = trunc(vy[i] * f) / f
            ax, ay = forces(x, y)
        if s <= n10:
            emax = max(emax, abs((energie(x, y, vx, vy) - e0) / e0))
            pmax = max(pmax, sqrt(sum(M[i] * vx[i] for i in range(3)) ** 2 + sum(M[i] * vy[i] for i in range(3)) ** 2))
            lmax = max(lmax, abs(sum(M[i] * (x[i] * vy[i] - y[i] * vx[i]) for i in range(3))))
        if s in rep: lieux[rep[s]] = (x[:], y[:])
    return e0, emax, abs((energie(x, y, vx, vy) - e0) / e0), pmax, lmax, lieux
R = []
def ok(nom, cond): R.append((nom, bool(cond))); print(("conforme : " if cond else "ÉCHEC : ") + nom, flush=True)
# 4.1 : l'énergie et le pas, à pleine précision, sur dix unités de temps
E = {h: calcul(h, 10.0) for h in (4e-5, 2e-5, 1e-5)}
ok("énergie de départ -769/60", abs(E[1e-5][0] + 769 / 60) < 1e-12)
ok(f"4.1 écart maximal d'énergie sur dix unités : {100*E[4e-5][1]:.1f} %, {100*E[2e-5][1]:.1f} %, {100*E[1e-5][1]:.2f} % pour les pas 4, 2 et 1 × 10^-5",
   abs(E[4e-5][1] - 0.504) < 0.005 and abs(E[2e-5][1] - 0.132) < 0.002 and abs(E[1e-5][1] - 0.0332) < 0.0005)
ok(f"4.1 l'écart maximal est divisé par quatre quand le pas est divisé par deux : rapports {E[4e-5][1]/E[2e-5][1]:.2f} et {E[2e-5][1]/E[1e-5][1]:.2f}",
   3.6 < E[4e-5][1] / E[2e-5][1] < 4.2 and 3.8 < E[2e-5][1] / E[1e-5][1] < 4.2)
ok(f"4.1 à la dixième unité de temps l'écart est retombé sous 10^-7 pour les trois pas ({E[4e-5][2]:.0e}, {E[2e-5][2]:.0e}, {E[1e-5][2]:.0e})",
   all(E[h][2] < 1e-7 for h in E))
ok(f"2.2 et 4.1 quantité de mouvement et moment cinétique sous 2 × 10^-12 pour les trois pas", all(E[h][3] < 2e-12 and E[h][4] < 2e-12 for h in E))
# 3.1 et 3.2 : les coupes, pas de 2 × 10^-5, vingt unités de temps, relations relevées sur les dix premières
T = (2, 6, 10, 16, 20)
ref = calcul(2e-5, 20.0, None, T)
att = {9: ((2.9e-5, 0.0043, 0.021, 5.8, 160), 0.00069, 0.0008), 7: ((0.0028, 0.48, 20, 110, 650), 0.068, 0.059), 5: ((380, 4100, 7800, 13000, 17000), 3.1, 8600)}
for d in (9, 7, 5):
    c = calcul(2e-5, 20.0, d, T)
    ec = [max(sqrt((c[5][t][0][i] - ref[5][t][0][i]) ** 2 + (c[5][t][1][i] - ref[5][t][1][i]) ** 2) for i in range(3)) for t in T]
    ok(f"3.1 coupe à {d} décimales, écart du corps le plus déplacé à t = 2, 6, 10, 16, 20 : " + " ; ".join(f"{v:.2g}" for v in ec),
       all(abs(v / a - 1) < 0.06 for v, a in zip(ec, att[d][0])))
    ok(f"3.2 coupe à {d} décimales, sur dix unités : quantité de mouvement jusqu'à {c[3]:.2g}, moment cinétique jusqu'à {c[4]:.2g}",
       abs(c[3] / att[d][1] - 1) < 0.06 and abs(c[4] / att[d][2] - 1) < 0.06)
assert all(k for _, k in R); print(len(R), "contrôles, tous conformes")
