# Volume 8, chapitre 17 : le 198 dans le tableau périodique. Vérification (règle R10).
# Bibliothèque standard seulement. Usage : python3 tableau_198_verif.py
S = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr "
     "Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re "
     "Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg "
     "Cn Nh Fl Mc Lv Ts Og").split()
assert len(S) == 118
dr = lambda n: 1 + (n - 1) % 9
sym = lambda z: S[z - 1]

# 17.1 les treize triplets 8-9-1
T = [n for n in range(1, 117) if (dr(n), dr(n + 1), dr(n + 2)) == (8, 9, 1)]
assert T == [8, 17, 26, 35, 44, 53, 62, 71, 80, 89, 98, 107, 116] and all(dr(n) == 8 for n in T)
membres = {z for n in T for z in (n, n + 1, n + 2)}
assert len(membres) == 39
assert [sym(n) + sym(n + 1) + sym(n + 2) for n in T][:7] == ["OFNe", "ClArK", "FeCoNi", "BrKrRb", "RuRhPd", "IXeCs", "SmEuGd"]

# 17.3 à 17.5 : appartenances (les propriétés physiques sont des faits sourcés, non calculés ici)
assert {26, 27, 28, 64} <= membres                      # Fe, Co, Ni, Gd
assert {8, 28, 82} <= membres and not ({2, 20, 50} & membres)   # nombres magiques des protons
gaz = [2, 10, 18, 36, 54, 86, 118]; hal = [9, 17, 35, 53, 85, 117]
assert [z for z in gaz if z in membres] == [10, 18, 36, 54, 118]
assert [z for z in hal if z in membres] == [9, 17, 35, 53, 117]
assert [(sym(n), sym(n + 1), sym(n + 2)) for n in (17, 35, 53)] == [("Cl", "Ar", "K"), ("Br", "Kr", "Rb"), ("I", "Xe", "Cs")]

# 17.6 le miroir garde la place
rev = lambda z: int(str(z)[::-1])
for z in range(1, 1000):
    if z % 10: assert dr(rev(z)) == dr(z)
for z in sorted(membres):
    m = rev(z)
    if z % 10 and m <= 118 and m != z:
        assert m in membres and dr(m) == dr(z)
for a, b in [(26, 62), (28, 82), (35, 53), (46, 64), (17, 71), (29, 92), (38, 83), (47, 74)]:
    assert rev(a) == b and dr(a) == dr(b)

# 17.8 la répétition par les périodes de 18
periodes = [2, 8, 8, 18, 18, 32, 32]
assert sum(periodes) == 118
assert 35 - 17 == 18 == periodes[3] and 53 - 35 == 18 == periodes[4]
assert dr(17 + 18) == dr(17) and dr(53 + 32) != dr(53)           # At (85) sort du motif
assert (dr(85), dr(86), dr(87)) == (4, 5, 6)

# 17.10 et 17.11 les sommes
som = [3 * n + 3 for n in T]
assert som == [27 * k for k in range(1, 14)] and all(dr(s) == 9 for s in som)
assert som[2] == 81 and int(f"{som[2]}{dr(som[2])}") == 819 and 918 - 819 == 99
assert sorted("819") == sorted("198")
assert som[3] == 108 and int(f"{som[3]}{dr(som[3])}") == 1089 == 33 ** 2 == 198 + 891
assert som[6] == 189 == 198 - 9

# 17.13 l'interface
assert 26 + 27 + 28 + 29 == 110 == 11 * 10 and dr(29) == 2 and dr(30) == 3

# 17.16 ajouter 29
plus29 = [s + 29 for s in som]
assert plus29 == [56, 83, 110, 137, 164, 191, 218, 245, 272, 299, 326, 353, 380]
assert 137 - 29 == 108

# 17.18 les deux éléments qui suivent chaque triplet
suiv = [(n + 3, n + 4) for n in T]
assert all(dr(a) == 2 and dr(b) == 3 for a, b in suiv)
noms = [(sym(a), sym(b)) for a, b in suiv if b <= 118]
assert noms == [("Na", "Mg"), ("Ca", "Sc"), ("Cu", "Zn"), ("Sr", "Y"), ("Ag", "Cd"), ("Ba", "La"), ("Tb", "Dy"),
                ("W", "Re"), ("Bi", "Po"), ("U", "Np"), ("Md", "No"), ("Ds", "Rg")]
assert [a for a, b in suiv if a in (29, 47)] == [29, 47] and (110, 111) in suiv   # Cu, Ag en racine 2 ; Rg (111) en racine 3
print("Volume 8, chapitre 17 : toutes les vérifications passent.")
