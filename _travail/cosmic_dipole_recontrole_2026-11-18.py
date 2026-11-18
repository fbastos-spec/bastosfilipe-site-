# -*- coding: utf-8 -*-
# Resolving the 5σ Cosmic Dipole Anomaly, v1.5: recheck of 18 November 2026. Python 3, standard library only.
from math import sqrt, log, e
R = []
def ok(name, cond): R.append((name, bool(cond))); print(("pass : " if cond else "FAIL : ") + name)
def fac(n):
    f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    return f + ([n] if n > 1 else [])
REG = {2, 3, 5, 7, 11, 13, 73, 137, 163}
ok("§0bis.3  27,951 = 3 × 7 × 11³ ; the printed product 3² × 5 × 11 × 113 is 55,935 ; no factor 113 ; every factor is in the register", fac(27951) == [3, 7, 11, 11, 11] and 9 * 5 * 11 * 113 == 55935 and set(fac(27951)) <= REG and set(fac(12500)) <= REG)
ok("§0bis.6.1  161/72 = 7 × 23 / 2³ × 3² brings in 23, outside the register, and is less precise than 27,951/12,500 (4.31e-5 against 1.20e-5)",
   fac(161) == [7, 23] and 23 not in REG and round(abs(161 / 72 - sqrt(5)) * 1e5, 2) == 4.31 and round(abs(27951 / 12500 - sqrt(5)) * 1e5, 2) == 1.20)
ok("§0bis.6.2  137,036 = 2² × 34,259 with 34,259 prime ; the printed product 2² × 7³ × 11² × 113 is 18,759,356", fac(137036) == [2, 2, 34259] and 4 * 343 * 121 * 113 == 18759356)
ok("§0bis.5  the couple (137, 36): 137 − 36 = 101, 137 + 36 = 173 prime, 137 × 36 = 4932 = 2² × 3² × 137", 137 - 36 == 101 and fac(173) == [173] and fac(4932) == [2, 2, 3, 3, 137])
m = [99 * k for k in range(1, 10)]
ok("§5.1  every multiple of 99 below 1089 carries the factor 11, and every one satisfies N + mirror(N) = 1089 (99 read 099)",
   all(11 in fac(n) for n in m) and all(n + int(f"{n:03d}"[::-1]) == 1089 for n in m))
s = [945]
while s[-1] > 3: s.append(s[-1] - (101 if s[-1] > 36 else 11))
d = [a - b for a, b in zip(s, s[1:])]
ok("§9.3  945 → 3: thirteen stations, nine jumps of 101 then three jumps of 11", s == [945, 844, 743, 642, 541, 440, 339, 238, 137, 36, 25, 14, 3] and d == [101] * 9 + [11] * 3)
ok("§5  8 + 64/81 = 8.79012 agrees with 8.7903 to three decimals, not four", round(8 + 64 / 81, 5) == 8.79012 and round(8 + 64 / 81, 3) == 8.790 and round(8 + 64 / 81, 4) != 8.7903)
ok("§0bis.3  relative errors: ln 2 by 2695/3888 is 1.62e-5, e by 5760/2119 is 6.80e-6 (not the same precision)",
   round(abs(2695 / 3888 - log(2)) / log(2) * 1e5, 2) == 1.62 and round(abs(5760 / 2119 - e) / e * 1e6, 2) == 6.80)
ok("§0bis.3  √2 − 140/99 = 7.2148e-5 is close to 1/13,860 = 7.2150e-5, not equal to it", round((sqrt(2) - 140 / 99) * 1e5, 4) == 7.2148 and round(1e5 / 13860, 4) == 7.2150)
dr = lambda n: 1 + (n - 1) % 9
F = [1, 1]
while len(F) < 24: F.append(F[-1] + F[-2])
D = [dr(x) for x in F]
ok("§3  the 24 roots of the Fibonacci cycle fold into twelve pairs: eleven sum to 9, the twelfth, (9, 9), sums to 18, of root 9", [D[i] + D[i + 12] for i in range(12)] == [9] * 11 + [18])
assert all(k for _, k in R); print(len(R), "checks, all passed")
