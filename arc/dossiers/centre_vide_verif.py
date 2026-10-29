# Volume 2, É 1.12 bis et ter : le centre vide de la figure qui se trace seule.
# On relie tous les points de la figure entre eux ; on cherche la région autour du centre
# qu'aucune ligne ne traverse, hors des quatre droites qui passent par le centre.
import math, itertools
R = 1.0; r = R / math.sqrt(2)
grand = [(R*math.cos(k*math.pi/4), R*math.sin(k*math.pi/4)) for k in range(8)]   # 4 sommets du carré, 4 points des axes
petit = [(r*math.cos(k*math.pi/4), r*math.sin(k*math.pi/4)) for k in range(8)]   # 4 milieux des côtés, 4 points à 45°
noeuds = [(0.5*math.cos(math.pi/4+k*math.pi/2), 0.5*math.sin(math.pi/4+k*math.pi/2)) for k in range(4)]

def segments(P):
    return [(a, b) for a, b in itertools.combinations(P, 2) if abs(a[0]*b[1]-a[1]*b[0]) > 1e-9]

def rayon(segs, th):
    dx, dy = math.cos(th), math.sin(th); best = 9.0
    for (x1, y1), (x2, y2) in segs:
        ex, ey = x2-x1, y2-y1; D = dy*ex - dx*ey
        if abs(D) < 1e-14: continue
        s = (dx*y1 - dy*x1) / D
        if s < -1e-12 or s > 1+1e-12: continue
        t = (x1+s*ex)*dx + (y1+s*ey)*dy
        if t > 1e-12: best = min(best, t)
    return best

# les 4 nœuds sont des croisements de la figure : diagonales et carré inscrit dans le petit cercle
for (x, y) in noeuds:
    assert abs(abs(x)+abs(y) - r) < 1e-12 and abs(abs(x)-abs(y)) < 1e-12

# É 1.12 bis : les 16 points des deux cercles. Octogone régulier, sommet à R − r.
s16 = segments(grand+petit)
for k in range(8):
    assert abs(rayon(s16, k*math.pi/4 + 1e-9) - (R - r)) < 1e-6
assert abs(rayon(s16, math.pi/8) - (R - r)*math.cos(math.pi/8)) < 1e-9

# É 1.12 ter : avec les 4 nœuds (la figure telle qu'elle se dessine). Sommets R/4 et R√2/6, apothème R√5/10, aire R²/6.
s20 = segments(grand+petit+noeuds)
for k in range(4):
    assert abs(rayon(s20, math.pi/4 + k*math.pi/2 + 1e-9) - R/4) < 1e-6
    assert abs(rayon(s20, k*math.pi/2 + 1e-9) - R*math.sqrt(2)/6) < 1e-6
assert abs(min(rayon(s20, 2*math.pi*(i+0.5)/7200) for i in range(7200)) - R*math.sqrt(5)/10) < 1e-6
N = 36000
aire = sum(0.5*rayon(s20, 2*math.pi*(i+0.5)/N)**2 * 2*math.pi/N for i in range(N))
assert abs(aire - R*R/6) < 1e-6
assert abs(8*0.5*(R*math.sqrt(2)/6)*(R/4)*math.sin(math.pi/4) - R*R/6) < 1e-15   # aire exacte : 8 triangles
print("Centre vide : toutes les vérifications passent. Aire =", round(aire, 9))
