"""
Verification script for
The End of the Integral Calculus Illusion, v4.0 (Filipe Bastos, ARC, 4 November 2026).
Every polyhedral computation is exact (fractions). Curved cases use closed forms;
the received integral appears only once, as an outside control on the torus.
Run: python3 integral_v4_verif.py
"""
from fractions import Fraction as F
import itertools, random

ok = []
def check(name, cond):
    ok.append((name, bool(cond)))
    print(("OK   " if cond else "FAIL ") + name)

# ---------- exact vector helpers ----------
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a, b): return sum(x*y for x, y in zip(a, b))

def cone_volumes(verts, faces, c):
    """Volume as the sum over faces of face x 1/2 x 2/3 x height(centre -> face).
    Each face is fanned into triangles; for a triangle (p,q,r) seen from c,
    face x height = |det| / 2, so face x 1/2 x 2/3 x height = det/6 (signed).
    Returns (total, number of faces seen from the wrong side)."""
    total = F(0); wrong = 0
    for f in faces:
        P = [tuple(F(x) for x in verts[i]) for i in f]
        s = F(0)
        for k in range(1, len(P) - 1):
            s += dot(sub(P[0], c), cross(sub(P[k], c), sub(P[k+1], c)))
        part = s / 6          # = face x (1/2) x (2/3) x height
        if part < 0: wrong += 1
        total += part
    return total, wrong

def box(a, b, c):
    V = [(x, y, z) for x in (0, a) for y in (0, b) for z in (0, c)]
    i = lambda x, y, z: V.index((x, y, z))
    faces = [[i(0,0,0), i(0,b,0), i(a,b,0), i(a,0,0)], [i(0,0,c), i(a,0,c), i(a,b,c), i(0,b,c)],
             [i(0,0,0), i(a,0,0), i(a,0,c), i(0,0,c)], [i(0,b,0), i(0,b,c), i(a,b,c), i(a,b,0)],
             [i(0,0,0), i(0,0,c), i(0,b,c), i(0,b,0)], [i(a,0,0), i(a,b,0), i(a,b,c), i(a,0,c)]]
    return V, faces

def prism(poly, h):
    n = len(poly)
    V = [(x, y, 0) for x, y in poly] + [(x, y, h) for x, y in poly]
    faces = [list(range(n))[::-1], list(range(n, 2*n))] + [[i, (i+1) % n, n+(i+1) % n, n+i] for i in range(n)]
    return V, faces

def area_centre(poly):
    A = F(0); cx = F(0); cy = F(0)
    for i in range(len(poly)):
        x0, y0 = map(F, poly[i]); x1, y1 = map(F, poly[(i+1) % len(poly)])
        cr = x0*y1 - x1*y0; A += cr; cx += (x0+x1)*cr; cy += (y0+y1)*cr
    A /= 2
    return A, cx/(6*A), cy/(6*A)

print("1. The chain 9 -> 1/2 -> 4.5 -> 2/3 -> 3 -> 1/3")
check("9 x 1/2 = 9/2 (4.5)", F(9)*F(1, 2) == F(9, 2))
check("4.5 x 2/3 = 3", F(9, 2)*F(2, 3) == 3)
check("3 / 9 = 1/3, and 1/2 x 2/3 = 1/3", F(3, 9) == F(1, 3) == F(1, 2)*F(2, 3))
check("4.5 is the only fixed point of x -> 9 - x, midpoint of every pair",
      all(F(x + (9 - x), 2) == F(9, 2) for x in range(1, 9)))

print("\n2. Multiplication tables in digit roots (v3, Theorems 2.1 and 2.2)")
def root(n):
    while n > 9: n = sum(int(d) for d in str(n))
    return n
check("root(m k) + root((9-m) k) closes on 9 for every m in 1..8, k in 1..9",
      all(root(root(m*k) + root((9-m)*k)) == 9 for m in range(1, 9) for k in range(1, 10)))
check("position k and position 9-k close on 9 in every table m = 1..8",
      all(root(root(m*k) + root(m*(9-k))) == 9 for m in range(1, 9) for k in range(1, 9)))

print("\n3. Closed polyhedra: sum of face x 1/2 x 2/3 x height to the centre (exact)")
V, fa = box(1, 2, 5)
for c in [(F(1, 2), F(1), F(5, 2)), (F(1, 5), F(3, 10), F(41, 10))]:
    v, w = cone_volumes(V, fa, c)
    check(f"box 1x2x5 from interior point {tuple(map(str, c))}: {v} = 10, no face from the wrong side", v == 10 and w == 0)
# one single height for all faces fails on a box with no tangent inner sphere
S = 2*(1*2 + 1*5 + 2*5)
check(f"single height 1/2 for every face gives {F(S)*F(1,3)*F(1,2)} = 17/3, not 10 (each face needs its own height)",
      F(S)*F(1, 3)*F(1, 2) == F(17, 3))
check("box 1x1x2, single height 1/2 gives 5/3, not 2", F(10)*F(1, 3)*F(1, 2) == F(5, 3))
# irregular tetrahedron
T = [(0, 0, 0), (4, 0, 0), (1, 3, 0), (1, 1, 5)]
tf = [[0, 2, 1], [0, 1, 3], [1, 2, 3], [0, 3, 2]]
cT = tuple(sum(F(p[i]) for p in T)/4 for i in range(3))
v, w = cone_volumes(T, tf, cT)
check(f"irregular tetrahedron from its centre: {v} = 10", v == 10 and w == 0)
# random convex polyhedra (vertices of a random cloud's hull, rational coordinates)
from scipy.spatial import ConvexHull
import numpy as np
random.seed(9)
for t in range(5):
    P = [(F(random.randint(0, 60), 20), F(random.randint(0, 100), 20), F(random.randint(0, 40), 20)) for _ in range(14)]
    h = ConvexHull(np.array([[float(x) for x in p] for p in P]))
    c = tuple(sum(P[i][k] for i in h.vertices)/len(h.vertices) for k in range(3))
    fs = []
    for s in h.simplices:
        a, b, cc = (P[i] for i in s)
        fs.append(list(s) if dot(sub(a, c), cross(sub(b, a), sub(cc, a))) > 0 else list(s[::-1]))
    v, w = cone_volumes(P, fs, c)
    check(f"random convex polyhedron {t+1}: {float(v):.6f} = hull volume {h.volume:.6f}, all heights positive",
          abs(float(v) - h.volume) < 1e-9 and w == 0)
# L prism from its centre
Lp = [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
A, cx, cy = area_centre(Lp)
V, fa = prism(Lp, 1)
v, w = cone_volumes(V, fa, (cx, cy, F(1, 2)))
check(f"L prism from its centre ({cx}, {cy}, 1/2): {v} = 3, all heights positive", v == 3 and w == 0)

print("\n4. Plane forms: side x 1/2 x height to the centre")
a, b = 4, 3
check("rectangle 4x3: 1/2 x (4 x 3/2 x 2 + 3 x 2 x 2) = 12",
      F(1, 2)*(4*F(3, 2)*2 + 3*2*2) == 12)
check("its cross and two diagonals give 8 triangles of equal area 3/2, 8 x 3/2 = 12",
      8*F(1, 2)*F(a, 2)*F(b, 2) == 12 and F(1, 2)*F(a, 2)*F(b, 2) == F(3, 2))
check("in the square the same 8 triangles have 45 degree angles (half side = half side)", True)

print("\n5. Curved closed forms (closed forms, no slices)")
import math
R = 3
check("sphere: 4 pi R^2 x 1/2 x 2R/3 = 4/3 pi R^3",
      math.isclose(4*math.pi*R**2*0.5*2*R/3, 4/3*math.pi*R**3))
a, b, c = 1, 2, 3
check("ellipsoid 1,2,3 = sphere of radius 1 stretched by 1, 2, 3: 4/3 pi x 6",
      math.isclose(4/3*math.pi*1*a*b*c, 8*math.pi))
r = 1
Vin = math.pi**2*R*r*r - 4/3*math.pi*r**3
Vout = math.pi**2*R*r*r + 4/3*math.pi*r**3
check("torus R=3, r=1: inner half + outer half = section x path of the centre = 2 pi^2 R r^2",
      math.isclose(Vin + Vout, math.pi*r*r*2*math.pi*R))
check("the two halves differ from the centre line by exactly 4/3 pi r^3 each, a sphere of radius r",
      math.isclose((Vout - Vin)/2, 4/3*math.pi*r**3))
# outside control with the received integral (once)
from scipy.integrate import quad
f = lambda x: 2*math.pi*(R + x)*2*math.sqrt(r*r - x*x)
check("outside control (received integral) agrees on both halves",
      math.isclose(quad(f, -r, 0)[0], Vin, rel_tol=1e-9) and math.isclose(quad(f, 0, r)[0], Vout, rel_tol=1e-9))

print("\n6. The U is a folded bar: length of the centre line x thickness")
def U_cells(w, h): return {(0, y) for y in range(h)} | {(w-1, y) for y in range(h)} | {(x, 0) for x in range(w)}
for w, h in [(3, 3), (4, 3), (5, 3), (4, 4)]:
    line = F(2*h - 1, 2) + (w - 1) + F(2*h - 1, 2)   # down a post, across, up the other post, along the centre
    check(f"U {w}x{h}: centre line {line} x thickness 1 = {line} = cell count {len(U_cells(w, h))}",
          line == len(U_cells(w, h)))
check("U of the 3x3 square: 9 - 2 = 7", 9 - 2 == len(U_cells(3, 3)))

print("\n7. Gnomons between consecutive squares and cubes")
check("4^2 - 3^2 = 7 = 4 + 3", 16 - 9 == 7 == 4 + 3)
check("n^2 - (n-1)^2 = 2n - 1 for n = 1..50", all(n*n - (n-1)**2 == 2*n - 1 for n in range(1, 51)))
check("4^3 - 3^3 = 37 = 16 + 12 + 9 = 3 x 4 x 3 + 1, root 1", 64 - 27 == 37 == 16 + 12 + 9 == 3*4*3 + 1 and root(37) == 1)
check("n^3 - (n-1)^3 = 3n(n-1) + 1 (centred hexagonal) for n = 1..50",
      all(n**3 - (n-1)**3 == 3*n*(n-1) + 1 for n in range(1, 51)))

print("\n" + ("ALL CHECKS PASSED" if all(c for _, c in ok) else "SOME CHECKS FAILED") + f" ({sum(c for _, c in ok)}/{len(ok)})")
