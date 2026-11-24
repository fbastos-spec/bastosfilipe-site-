# octet_verif.py : checks for "The Octet Rule as Arithmetic Necessity", v8.0 (ARC corpus, Filipe Bastos)
# Exact integer arithmetic only.
from math import isqrt
from itertools import combinations
ok = tot = 0
def check(name, cond, detail=""):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ((" : " + str(detail)) if detail != "" else ""))
dr = lambda n: (n - 1) % 9 + 1
isp = lambda n: n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
rev = lambda n: int(str(n)[::-1])

check("1. four pairs (1,8),(2,7),(3,6),(4,5) sum to 9; 9 has no partner in 1..9", [(x, 9-x) for x in range(1, 5)] == [(1,8),(2,7),(3,6),(4,5)] and 9-9 not in range(1, 10))
subs = [s for r in range(10) for s in combinations(range(1, 10), r) if all(9-x in s and 9-x != x for x in s)]
check("2. largest subset of 1..9 closed under x -> 9-x without fixed point has 8 elements", max(map(len, subs)) == 8 and max(subs, key=len) == tuple(range(1, 9)))
check("3. pivot: |x-p| = |9-x-p| for all x only at p = 4.5 (p tested on halves from 0 to 9)", [p/2 for p in range(0, 19) if all(abs(2*x-p) == abs(2*(9-x)-p) for x in range(1, 9))] == [4.5])
check("4. half-spans of the pairs: 0.5, 1.5, 2.5, 3.5", [(9-2*x)/2 for x in (4, 3, 2, 1)] == [0.5, 1.5, 2.5, 3.5])
# universal fold
A = 10**5
check("5. DR(9a) = 9 for a = 1..10^5", all(dr(9*a) == 9 for a in range(1, A+1)))
check("6. DR(ka) + DR((9-k)a) is 9 or 18, a = 1..10^5, k = 1..4", all(dr(k*a)+dr((9-k)*a) in (9, 18) for a in range(1, A+1) for k in range(1, 5)))
check("7. the sum is 18 exactly when both terms are 9, i.e. when 9 divides ka", all((dr(k*a)+dr((9-k)*a) == 18) == ((k*a) % 9 == 0) for a in range(1, 5000) for k in range(1, 5)))
check("8. when 3 does not divide a, the cycle is a permutation of 1..9", all(sorted(dr(k*a) for k in range(1, 10)) == list(range(1, 10)) for a in range(1, 5000) if a % 3))
check("9. C(5) = 5,1,6,2,7,3,8,4,9 ; C(7) = 7,5,3,1,8,6,4,2,9 ; C(3) = 3,6,9,3,6,9,3,6,9",
      [dr(5*k) for k in range(1, 10)] == [5,1,6,2,7,3,8,4,9] and [dr(7*k) for k in range(1, 10)] == [7,5,3,1,8,6,4,2,9] and [dr(3*k) for k in range(1, 10)] == [3,6,9]*3)
big = 7 * 10**40 + 12345
check("10. the fold at a 41-digit multiplier", all(dr(k*big)+dr((9-k)*big) in (9, 18) for k in range(1, 5)))
# mirror
check("11. mirror cost: n - reverse(n) is a multiple of 9, n = 10..10^6", all((n - rev(n)) % 9 == 0 for n in range(10, 10**6)))
check("12. two digits: n + reverse(n) = 11(a+b)", all((10*a+b) + (10*b+a) == 11*(a+b) for a in range(1, 10) for b in range(10)))
check("13. v6.0 general claim fails at three digits: 123 + 321 = 444, not a multiple of 11", 123+321 == 444 and 444 % 11 != 0)
check("14. corrected: with an even number of digits, n + reverse(n) is a multiple of 11 (n to 10^6, no trailing zero)",
      all((n + rev(n)) % 11 == 0 for n in range(10, 10**6) if len(str(n)) % 2 == 0 and n % 10))
# Fibonacci
F = [1, 1]
while len(F) < 480: F.append(F[-1] + F[-2])
d = [dr(x) for x in F]
check("15. Fibonacci positions: period 24 (checked on 480 terms), not shorter", all(d[i] == d[i+24] for i in range(456)) and all(any(d[i] != d[i+p] for i in range(100)) for p in range(1, 24)))
check("16. first period: 1,1,2,3,5,8,4,3,7,1,8,9 | 8,8,7,6,4,1,5,6,2,8,1,9", d[:24] == [1,1,2,3,5,8,4,3,7,1,8,9,8,8,7,6,4,1,5,6,2,8,1,9])
check("17. fold k / k+12: eleven sums of 9, the twelfth 18", [d[i]+d[i+12] for i in range(12)] == [9]*11 + [18])
check("18. half sums 52 and 65, whole 117 (9 written 9); 43, 56, 99 (9 written 0)", (sum(d[:12]), sum(d[12:24]), sum(d[:24])) == (52, 65, 117) and (sum(x % 9 for x in d[:12]), sum(x % 9 for x in d[12:24])) == (43, 56))
# periodic table
st = list(range(92, 0, -11))
check("19. descent 92, 81, ..., 4: nine stations, positions 2,9,7,5,3,1,8,6,4, sum 432", st == [92,81,70,59,48,37,26,15,4] and [dr(x) for x in st] == [2,9,7,5,3,1,8,6,4] and sum(st) == 432)
p = [dr(x) for x in st]
check("20. the descent does not fold: with the 9 set aside, the pairs give 6, 13, 13, 4", [p[0]+p[8], p[2]+p[7], p[3]+p[6], p[4]+p[5]] == [6, 13, 13, 4], [p[0]+p[8], p[2]+p[7], p[3]+p[6], p[4]+p[5]])
check("21. Mendeleev fold: 59 pairs (Z, 119-Z), position of the sum always 2 (sum of positions 2 or 11)", all(dr(z)+dr(119-z) in (2, 11) for z in range(1, 60)) and dr(119) == 2 and 119 == 7*17)
check("22. half sums 1770 and 5251, total 7021", (sum(range(1, 60)), sum(range(60, 119))) == (1770, 5251) and 1770+5251 == 7021)
check("23. period lengths 2, 8, 8, 18, 18, 32, 32 are 2n^2, total 118", sum([2, 8, 8, 18, 18, 32, 32]) == 118 and [2*n*n for n in (1, 2, 3, 4)] == [2, 8, 18, 32])
# base
weak = [b for b in range(3, 40000) if not isp(b-1) and (b-2) & (b-3) == 0 and b % 2 == 0 and isp(b+1)]
check("24. v6.0 four conditions are also met by 66, 130, 4098, 32770", weak == [10, 66, 130, 4098, 32770], weak)
strong = [b for b in range(3, 10**6) if isqrt(b-1)**2 == b-1 and isp(isqrt(b-1)) and (b-2) & (b-3) == 0]
check("25. with closure b-1 = square of a prime and b-2 a power of 2: only b = 10 (b to 10^6)", strong == [10], strong)
check("26. p^2 + 2 is divisible by 3 for every prime p other than 3 (p to 10^5)", all((q*q+2) % 3 == 0 for q in range(2, 10**5) if isp(q) and q != 3))
# pi
from fractions import Fraction
check("27. 22/7 = 11/3.5 = 3.142857... differs from 3.14159... at the third decimal", Fraction(22, 7) == Fraction(11) / Fraction(7, 2) and str(Fraction(22, 7).numerator * 10**6 // 7) == "3142857")
# growth
check("28. multiples of 7 from 7 to 63: positions 7,5,3,1,8,6,4,2,9", [dr(7*k) for k in range(1, 10)] == [7,5,3,1,8,6,4,2,9])
check("29. 24 + 25 = 49 ; 23 + 32 = 55 = F10 ; 32 - 23 = 9 ; 23 is the 9th prime ; 64 - 46 = 18", 24+25 == 49 and F[9] == 55 and 32-23 == 9 and [q for q in range(2, 30) if isp(q)][8] == 23 and 64-46 == 18)
print(); print(f"{tot} checks, {ok} pass")
