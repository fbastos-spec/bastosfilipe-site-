---
title: "The Octet Rule as Arithmetic Necessity"
subtitle: "Derivation from the involution φ(x) = 9 − x and the Universal Fold Theorem"
author: "Filipe Bastos"
date: "Architecture of Relational Coherence (ARC). Version 8.0, 24 November 2026. First written August 2025; previous file v6.0, March 2026 (seventh Zenodo version). CC BY 4.0"
---

**Abstract.** The chemical octet rule, the observation that atoms are stable with eight valence electrons, has been treated since Lewis (1916) as an experimental fact explained afterwards by orbital filling (s²p⁶). This paper states what in it is arithmetic. On the nine digits, the involution φ(x) = 9 − x arranges exactly eight elements in four pairs summing to 9, with fixed point 4.5 between two digits, and the ninth element, 9, can belong to no pair. The structure is universal: for every integer a ≥ 1, the cycle of digital roots of a, 2a, …, 9a closes on 9 and folds into four pairs (Universal Fold Theorem). The Fibonacci cycle of digital roots, of period 24, folds into 12 + 12. The periodic table folds on 119.

**What version 8.0 changes.** Version 6.0 was never revised after March 2026. It was the seventh version deposited on Zenodo; this one is numbered 8.0 so that the file and the deposit carry the same number. In the meantime the ARC corpus re-read it line by line (Volume 2, chapter 10, with its Annex B). This version carries those corrections into the paper itself. Nothing is silently removed: every withdrawn or restated claim is listed in section 12 with its date. Each statement now carries a status: **T**, theorem, a finite computation or a proof, re-run by the script `octet_verif.py` (29 checks); **F**, a fact held by science, with author and date; **R**, a reading of the author, declared as such.

# 1. The question

Since Mendeleev (1869) the periodic table arranges the elements by recurring properties. Quantum mechanics gives a dynamical model (orbitals s, p, d, f), but the number eight is never derived there: it is accepted as a filling rule. The question of this paper: which part of the octet is a necessity of arithmetic, independent of any physical model?

# 2. The nine digits

**2.1 (T).** The integers 1 to 9 are written with one symbol. After 9 there is no tenth digit: there is 10, the 1 started again one floor up. Every number is n = 9k + position, with k the count of turns and the position from 1 to 9. The 9 is kept as 9.

**2.2 (T). Structural determination.** The set {1, …, 9} with closure 9 determines: (i) φ(x) = 9 − x arranges {1, …, 8} in exactly four pairs summing to 9; (ii) the centre 4.5 is a half-integer and is not a digit; (iii) the projection constant k = 0.5 is the smallest half-span, that of the pair (4, 5); (iv) the interface 10 + 1 = 11 is prime; (v) the working elements are 8 = 2³, hence 4 = 2² pairs; (vi) the closure is 9 = 3², the square of a prime.

**2.3 (T, corrected). The base.** Version 6.0 wrote that 10 needs two symbols "in every positional system". That holds in every base up to 10 and fails from base 11 on, where ten is one symbol. The exact statement: 1 to 9 are the only single symbols common to all bases from 10 upward. The base does not found the nine digits; it depends on them.

**2.4 (T, corrected). Uniqueness of base 10.** Version 6.0 proved uniqueness from four conditions (b − 1 composite, b − 2 a power of 2, (b − 1)/2 not an integer, b + 1 prime) and checked up to b = 34. Those four conditions are also met by b = 66, 130, 4098 and 32 770. The fault was the omission of condition (vi). With the closure b − 1 = p², the square of a prime, uniqueness is proved in general, twice. First: b − 2 = p² − 1 = (p − 1)(p + 1) is a power of 2; two powers of 2 that differ by 2 are 2 and 4; so p = 3 and b = 10. Second: b + 1 = p² + 2 is divisible by 3 for every prime p other than 3, hence not prime; again p = 3, b = 10. The full structure of 2.2 exists only in base 10.

# 3. The octet theorem

**3.1 (T).** φ(x) = x would require x = 4.5. No digit is its own partner; every element of {1, …, 8} has exactly one complement.

**3.2 (T). Octet theorem.** The largest subset of {1, …, 9} that splits into complete pairs under φ is {1, …, 8}, with exactly four pairs: (1, 8), (2, 7), (3, 6), (4, 5). The 9 makes every pairing possible, being the target sum, and takes part in none.

**3.3 (R). The chemical octet.** "Chemical stability at eight valence electrons corresponds to the maximum number of elements forming complete inversion pairs under closure 9." Version 6.0 called this a corollary. It is a reading: no step of the proof links the digits 1 to 8 to the electrons of a shell. The count of pairs is a theorem; its identity with Lewis's rule is the author's reading.

# 4. The fold: concentric spheres

**4.1 (T).** Turn the sequence 1, …, 8 about a pivot p. Each digit x describes a sphere of radius |x − p|. The two members of every pair share their sphere if and only if p = 4.5. For p = 5: radius 4 for 1, radius 3 for 8; the pair (1, 8) does not close.

| Shell | Pair | Radius | Capacity |
|---|---|---|---|
| S1 | (4, 5) | 0.5 | 2 |
| S2 | (3, 6) | 1.5 | 2 |
| S3 | (2, 7) | 2.5 | 2 |
| S4 | (1, 8) | 3.5 | 2 |

**4.2 (R).** Four concentric spheres, four pairs, total capacity 8. The author reads the atom as emerging from this fold. The numerical link is T; the identity of these spheres with electron shells is R, since the real shell capacities are 2, 8, 18, 32 (section 8.3).

# 5. Precedents: Abegg, Lewis, Linnett

**5.1 (F, corrected).** Abegg stated that the largest number of electrons an element can give and the largest it can take sum to 8 (announced 1902, reference paper 1904). The cubic atom with eight corners is Lewis's (notes of 1902, published 1916), not Abegg's as version 6.0 wrote. Pauling (1931) replaces the cube by orbitals. Linnett (1961) proposes the double quartet: two tetrahedra of four electrons of like spin, interpenetrating into a cube.

**5.2 (R).** Abegg's rule is the octet theorem in chemical language: if one valence is x, the other is 8 − x. In Linnett's double quartet the two quartets are the two sides of 4.5, {1, 2, 3, 4} and {5, 6, 7, 8}.

# 6. The Universal Fold Theorem

**Definition.** For an integer a ≥ 1, the cycle of a is C(a) = (DR(a), DR(2a), …, DR(9a)), where DR is the digital root, from 1 to 9.

**6.1 (T). Universal Fold (restated).** For every a ≥ 1: (i) DR(9a) = 9: the 9 closes the cycle; (ii) for k from 1 to 4, the positions k and 9 − k form a pair whose sum is 9, or 18 when both are 9. Version 6.0 stated "summing to 9" and gave the 18 only inside the proof; the statement now says it.

*Proof.* DR(ka) + DR((9 − k)a) reduces like ka + (9 − k)a = 9a, so it is a multiple of 9; each term lies between 1 and 9, so the sum is 9 or 18. It is 18 exactly when 9 divides ka, and then 9 divides (9 − k)a as well: the two 9s stand face to face. When 3 does not divide a, the cycle is a permutation of {1, …, 9}.

C(5) = (5, 1, 6, 2, 7, 3, 8, 4, 9): 5 + 4, 1 + 8, 6 + 3, 2 + 7. C(7) = (7, 5, 3, 1, 8, 6, 4, 2, 9). C(3) = (3, 6, 9, 3, 6, 9, 3, 6, 9): positions 3 and 6 give 9 + 9 = 18.

**6.2 (T).** The four pairs are the only way to split {1, …, 8} into pairs summing to 9. They are not a property of one sequence.

**6.3 (R, added 24 November 2026). Proof by scale projection.** The theorem says "for every a": the table of a 41-digit number folds like the table of 5 (check 10). The author named this kind of proof on 23 November 2026: *proof by scale projection*. "If I carry the computation to that scale, the relation tells me what I shall find there." The turn closes (9), the count of turns is kept (k in n = 9k + position), the relation is carried to the chosen scale. The Universal Fold, written in August 2025, is the earliest example of it in the corpus (see *La preuve par projection d'échelle*, v1.1).

# 7. The mirror

**7.1 (T). Mirror cost.** For every integer n and its digit reversal ñ, n − ñ is a multiple of 9: both have the same digit sum. For three digits abc: abc − cba = 99(a − c) = 9 × 11 × (a − c).

**7.2 (T, corrected). Mirror sum.** For two digits, n + ñ = 11(a + b). Version 6.0 added that "more generally" the sum is governed by 11. That fails at three digits: 123 + 321 = 444, which 11 does not divide. The exact statement: when n has an even number of digits, n + ñ is a multiple of 11 (check 14).

**7.3 (R).** The difference measures the tension, always on the closure 9; the sum confirms the relation on the interface 11, for pairs of even length.

# 8. The Fibonacci cycle

**8.1 (T).** The digital roots of the Fibonacci sequence have period 24 (Wall, 1960):

1, 1, 2, 3, 5, 8, 4, 3, 7, 1, 8, 9 | 8, 8, 7, 6, 4, 1, 5, 6, 2, 8, 1, 9

**8.2 (T). Fibonacci fold.** Positions k and k + 12 sum to 9 for k = 1 to 11; the twelfth pair is the two closures, 9 + 9 = 18.

**8.3 (T).** With 9 written 9, the two halves sum to 52 and 65, the cycle to 117. With 9 written 0, they sum to 43 and 56, the cycle to 99. Both counts are right; one must name the writing used.

**8.4 (R).** The golden ratio is the limit of a sequence whose positions already obey the four pairs: a consequence of the octet structure, not its cause.

# 9. The periodic table

**9.1 (T). Descent from uranium.** 92 = 8 × 11 + 4. Going down by steps of 11: 92, 81, 70, 59, 48, 37, 26, 15, 4. The nine stations have positions 2, 9, 7, 5, 3, 1, 8, 6, 4, a full permutation, and sum to 432.

**9.2 (T, R).** This descent does not fold into pairs of 9 (6, 13, 13, 4). The fold holds for cycles, where the 9 is at the end; the descent is a path, where the 9 is crossed on the way (station 81). Reading: a cycle that folds gives a closed, stable structure; a path that does not fold carries tension. That uranium is radioactive "because it has not reached closure" is a reading, not a nuclear theory.

**9.3 (F, R).** The periods have lengths 2, 8, 8, 18, 18, 32, 32, that is 2n² for n = 1 to 4, each twice (F). That the factor 2 is the relation, position of 11, is R.

**9.4 (T). Mendeleev fold.** Pair each element Z from 1 to 118 with 119 − Z: 59 pairs, from (1, 118) to (59, 60). The sum of the two positions is always 2 or 11: position 2, that of 11. Half sums 1770 and 5251, total 7021. 119 = 7 × 17.

**9.5 (R).** The table folds on the interface, where the cycles fold on the closure. The three modes, by the place of the 9: at the end (cycle, closure 9), crossed (path, no fold), among the others (relation, fold on 2). The match of these three modes with three domains of physics is a reading.

# 10. The ratio 22/7 (corrected)

**10.1 (T, R).** Version 6.0 stated π = 22/7 as a theorem and wrote that 3.14159… "is the decimal expansion of this ratio". Both are withdrawn. 22/7 = 3.142857…, a periodic expansion that leaves π at the third decimal; and the transcendence of π (Lindemann, 1882) depends on no writing. What stays is the address: 22/7 = 11/3.5, the interface over the half-span of 7, read on the Fundamental Figure. The claim is about structure, not about measure (Volume 2, 2.12; Register of Errors, G.5).

# 11. Growth

**11.1 (T).** The multiples of 7 from 7 to 63 have positions 7, 5, 3, 1, 8, 6, 4, 2, 9.

**11.2 (T, R).** 24 + 25 = 49; 23 + 32 = 55, the tenth Fibonacci number; 32 − 23 = 9; 23 is the ninth prime; 64 − 46 = 18. The equalities are T; their names (the inner arm, the seal) are R.

# 12. What changed from v6.0

| v6.0 | v8.0 | Source of the correction |
|---|---|---|
| Th 2.4, uniqueness of base 10 from four conditions | restated with b − 1 = p²; proved in general (2.4) | Volume 2, 3.3; Register G.4 |
| "10 requires two symbols in every positional system" | true up to base 10 only (2.3) | Volume 2, 3.2 |
| Cor 3.5, chemical octet as corollary | reading (3.3) | Volume 2, 10.4 |
| Abegg and the cube | the cube is Lewis's (5.1) | Volume 2, 10.9 |
| Th 6.4, "pairs summing to 9" | 9, or 18 when both are 9 (6.1) | this version |
| Th 7.3, mirror sum "more generally" | even number of digits only (7.2) | Volume 2, 10.14 |
| Th 10.2 and Rem 10.3, π = 22/7 | withdrawn as measure, kept as address (10.1) | Volume 2, 2.12; Register G.5 |
| Radioactivity of uranium, three modes and physics | readings (9.2, 9.5) | Volume 2, 10.21, 10.25 |

# 13. Conclusion

The involution φ(x) = 9 − x arranges {1, …, 8} in exactly four pairs summing to 9, with the ninth element as closure. That is a theorem, and so is the Universal Fold. That the chemical rule *is* this theorem remains the author's reading. What would bring the theorems down: one integer a whose cycle does not fold. The script re-runs them.

# Sources

Abegg, R., *Zeitschrift für anorganische Chemie* 39, 1904. Lewis, G. N., *Journal of the American Chemical Society* 38, 1916, 762-785. Pauling, L., 1931. Linnett, J. W., 1961. Wall, D. D., *American Mathematical Monthly* 67, 1960, 525-532. Lindemann, F., 1882. Mendeleev, D., 1869. ARC corpus: Volume 2, chapters 2, 3 and 10, Annex B; Register of Errors, G.4, G.5, G.17; *La preuve par projection d'échelle*.

Model, questions, readings and rules: Filipe Bastos. Scribe: Claude, under the author's contradiction. Computations, wording and audits assisted by AI (ChatGPT, Gemini, DeepSeek, GLM), at his request. ARC corpus, CC BY 4.0.
