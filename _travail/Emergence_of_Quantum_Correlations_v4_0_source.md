---
title: "Emergence of Quantum Correlations via Sequential Geometric Projection"
subtitle: "A Relational, Deterministic, and Operator-Free Framework"
author: "Filipe Bastos"
date: "Version 4.0, November 2026. Supersedes v1.2 (February 2026) and v3.6 (March 2026). CC BY 4.0"
---

Architecture of Relational Coherence (ARC) · D2technologie Inc. · contact@d2technologie.com

*This work is dedicated to my parents, Joaquim and Agostinha, to Sophie, to my children Soleil, Delfine, Justin, and Yanie, and to all the Portuguese people who carry saudade in their blood and who have carried history forward so that the future may discover.*

Model, questions, readings and rules: Filipe Bastos. Scribe: Claude, under the author's contradiction. Computations, wording and audits assisted by AI, at his request.

## Abstract

We present a deterministic framework in which the singlet correlation $E(a,b) = -\cos\theta_{ab}$ and the Tsirelson bound $2\sqrt{2}$ follow from geometric and relational constraints alone, with no Hilbert space, no operator, no collapse and no ontological randomness. A pair shares one relational state $\lambda$ on the sphere $S^2$. A first reading takes a sign; the state is replaced by the inverse of that reading on its axis; the second reading is a linear-response threshold. The cosine follows in two lines. The framework has three ceilings, and it states what separates them: the pair read by its sides gives 2, the pair read by its diagonals gives $2\sqrt{2}$, and the pair read by the bare sign gives 4. The three follow one another by $\sqrt{2}$, the ratio of the two circles of a square, and the quantum ceiling over the algebraic one equals the inscribed radius over the circumscribed radius. The cosine is exact if and only if the reading has the flat density one half. The model is non-signalling; it is not Bell-local and does not claim to be; the joint table is the same whichever reading is written first. Every number marked as a theorem is recomputed by the companion script.

**Keywords:** quantum entanglement, Bell inequalities, Tsirelson bound, Popescu-Rohrlich box, deterministic models, geometric projection, relational coherence.

**Notice.** In v1.2 and v3.6 the second reading was written as a bare sign, $B = \mathrm{sgn}(\lambda'\cdot b)$. Read literally, that rule gives a step function and $S = 4$, not Eq. (4) and (5) of v1.2. The inscription was made too early. The reading rule was completed in *Tsirelson's Bound Without Hilbert Space* v4.1 (July 2026) and is the one used here. The update rule is unchanged. Details are in Appendix D.

**Status labels.** T: theorem, proved here or recomputed by the script. F: fact established by others, with author and date. R: reading of the author, declared as such. P: prediction with its refutation criterion. O: open.

## 1. Foundational Principles

This work rests on four principles (R).

- **P1. Relational Priority:** relations precede objects.
- **P2. Topological Zero Distance:** entangled systems share one global relational state.
- **P3. No Ontological Randomness:** randomness is epistemic, not fundamental.
- **P4. Structural Closure:** coherence is enforced by global constraints, not by dynamics.

## 2. The Shared Relational State

**2.1 (R).** Let $\lambda \in S^2$ be a unit vector representing the relational configuration of a singlet pair. Isotropy is a symmetry constraint: no orientation is privileged. It is the only distribution compatible with the absence of a preferred direction, and it is not an adjustable parameter.

**2.2 (T, Archimedes).** For $\lambda$ isotropic on $S^2$ and any fixed axis $a$, the height $a\cdot\lambda$ is spread evenly over $[-1, 1]$, and the expected magnitude $|a\cdot\lambda|$ is $1/2$. With a pencil: wrap the sphere in a cylinder; equal slices of the cylinder cover equal areas of the sphere (Archimedes, *On the Sphere and Cylinder*); fold the stick at its middle; the balance point of an evenly covered stick is its midpoint. This is the constant $k = 1/2$ of Section 8.

## 3. Topological Sequential Order

**3.1 (R).** Measurement events are ordered by a discrete, non-metric, Lorentz-invariant structure $T_{sys}$. This order sequences relational updates, not spacetime events. There is no preferred frame and no spacetime signal.

**3.2 (T, the order is not observable).** In the protocol of Section 4 the joint table is
$$P(A, B \mid a, b) = \tfrac{1}{4}\,(1 - AB\cos\theta_{ab}),$$
and it is the same whether the reading along $a$ or the reading along $b$ is written first. Bob does not depend on Alice any more than Alice depends on Bob: the pair carries both settings together, through their angle.

**Theorem 3.3 (T, the order is carried by the state).** No order has to be given from outside. Let the face more strongly bound to the state read first: the reading along $a$ comes first when $|\lambda\cdot a| \ge |\lambda\cdot b|$, the reading along $b$ otherwise (the degree of binding $\beta = |a\cdot\lambda|$ of Corpus ARC, Volume 7, statement 3.21). Then each face reads first half of the time, the margins stay at $1/2$, the joint table is that of 3.2, and $|S| = 2\sqrt{2}$.

*Proof.* The condition is unchanged when $\lambda$ is replaced by $-\lambda$, which reverses the first sign: given which face reads first, its outcome is $\pm 1$ with equal weight, and the second reading follows as in Theorem 5.1. $\blacksquare$

**3.4 (R).** "Nobody gives the direction. The direction is already there, and the entangled other too." (the author, 22 November 2026). The written protocol has a first and a second line; the pair has none. Which reading is "first" is a property of the shared state, not a choice and not an event in spacetime.

## 4. The Protocol

**Definition 4.1.** Let $a, b$ be unit vectors, and let $\mu$ be a second variable, spread evenly over $[-1, 1]$, independent of $\lambda$, belonging to the reading.

1. First reading: $A = \mathrm{sgn}(\lambda\cdot a)$, $A \in \{+1, -1\}$.
2. Relational update: $\lambda' = -A\,a$.
3. Second reading: $B = \mathrm{sgn}(\lambda'\cdot b - \mu)$, $B \in \{+1, -1\}$.

The outcome is deterministic once the complete state $(\lambda, \mu)$ is given. There is no wavefunction, no operator, no collapse and no free parameter.

**4.2 (R).** The update is not a signal travelling in spacetime. It is a replacement of coordinate inside the shared state: the pair is one object with two faces, at relational distance zero, and the update activates one face and places the other where the second reading will find it. The pair carries the relation, $\lambda$; the reading carries $\mu$.

## 5. Emergence of the Quantum Correlation

**Theorem 5.1 (T, singlet correlation).** Under Definition 4.1, $E(a,b) = -\cos\theta_{ab}$ for all directions.

*Proof.* By isotropy $P(A = +1) = 1/2$. For fixed $\lambda'$, $P(B = +1 \mid \lambda') = P(\mu < b\cdot\lambda') = \tfrac{1}{2}(1 + b\cdot\lambda')$, since $\mu$ is even on $[-1,1]$; hence the expected value of $B$ given $\lambda'$ is $b\cdot\lambda'$. Then the expected value of $AB$ given $\lambda$ is $A\,(b\cdot(-A\,a)) = -A^2\,(a\cdot b) = -\cos\theta_{ab}$. It does not depend on $\lambda$. $\blacksquare$

**Theorem 5.2 (T, the bound).** With $S = E(a,b) - E(a,b') + E(a',b) + E(a',b')$ and the settings $a = 0°$, $a' = 90°$, $b = 45°$, $b' = 135°$, each of the four terms has magnitude $\cos 45° = \tfrac{1}{2}\sqrt{2}$ and $|S| = 2\sqrt{2}$. A scan of all settings degree by degree gives no larger value.

**Theorem 5.3 (T, non-signalling).** $P(A \mid a) = 1/2$ independently of $b$, and $P(B \mid b) = 1/2$ independently of $a$.

*Proof.* The first is isotropy. For the second, $P(B = +1) = \tfrac12 + \tfrac12\,\mathbb{E}[b\cdot(-A\,a)] = \tfrac12 - \tfrac12 (a\cdot b)\,\mathbb{E}[A] = \tfrac12$. $\blacksquare$

## 6. The Three Ceilings

**Theorem 6.1 (T, the bare sign).** If the second reading is the bare sign, $B = \mathrm{sgn}(\lambda'\cdot b)$, then $AB = -\mathrm{sgn}(a\cdot b)$ for every $\lambda$, so $E(a,b) = -\mathrm{sgn}(\cos\theta_{ab})$, a step function. At the settings of Theorem 5.2 the four correlations are $-1, +1, -1, -1$ and $|S| = 4$: the Popescu-Rohrlich box, the algebraic maximum compatible with no signalling.

**Theorem 6.2 (T, the hemisphere).** If, after the first reading, the state is taken as spread evenly over the hemisphere of axis $-A\,a$ and the second reading is its sign, then $E(a,b) = -(1 - 2\theta_{ab}/\pi)$, a straight law, and $|S| = 2$: the classical bound.

| Ceiling | Value | What is read |
|---|---|---|
| Classical (Bell, 1964) | $2$ | the sides only |
| Quantum (Tsirelson, 1980) | $2\sqrt{2}$ | the diagonals: the pair with its reading |
| Algebraic (Popescu and Rohrlich, 1994) | $4$ | the bare sign |

**Theorem 6.3 (T).** $2\sqrt{2} = \sqrt{2 \times 4}$: the quantum ceiling is the geometric mean of the other two; the three follow one another by the factor $\sqrt{2}$. The ratio $2\sqrt{2}/4 = \sqrt{2}/2$ equals $r/R$, the inscribed radius of a square over its circumscribed radius, and its square is $1/2$.

**6.4 (F, R).** With correlations at the algebraic maximum, any distributed Boolean function could be computed with one bit of communication (van Dam, 2005). Reading: the Tsirelson bound is the ceiling of relation without transport. What is instantaneous is the relation; what is bounded by $c$ is transport.

## 7. The Half Is Free

**Theorem 7.1 (T, the flat density).** Keep the protocol, the settings and the update, and change only how $\mu$ is spread between its two edges, never favouring a side. If $F(c)$ is the share of $\mu$ below $c = \lambda'\cdot b$, the correlation is $-(2F(c) - 1)$. It is the exact cosine at all angles if and only if $F(c) = \tfrac12 + \tfrac12 c$: the density is the constant $1/2$. Two receipts: a density gathered at the centre, $1 - |\mu|$, gives $|S| = 4\sqrt{2} - 2 \approx 3.66$; a density gathered at the edges, $|\mu|$, gives $|S| = 2$ at the settings of Theorem 5.2 (over all settings its maximum is $1 + \sqrt{2} \approx 2.414$, at spacings of 22.5°). Only the flat one gives the cosine, and its maximum over all settings is $2\sqrt{2}$.

**7.2 (R).** "The half is free. It charges nothing when you pass through it; the cost is the price of not passing through it." (the author, 11 November 2026). Through the half, the reading returns exactly what it receives: if the first face projects the value $x$ on the second direction, the second reads $+$ with chance $\tfrac12 + \tfrac12 x$ and the balance of its reading is $x$. Any other path distorts. As for the 4 of the bare sign, no measurement gives it: one does not lose what was never there.

**Remark 7.3 (T).** On the sphere, the part of $\lambda$ that the first sign did not read, its height along an axis taken perpendicular to the first axis $a$, has by 2.2 exactly this flat density, and it is unlinked to the sign $A$. Used as the threshold, it returns the cosine and $2\sqrt{2}$. On a circle it does not: the height is no longer evenly spread, and the law falls back to the straight one of Theorem 6.2. What Theorem 7.1 does not say is why the reading carries the flat density; this remark shows where the sphere itself holds it.

## 8. The Figure: Two Circles and a Square

**8.1 (F).** A square, its inscribed circle and its circumscribed circle: the three pieces are in Euclid (*Elements*, IV). The diagonal of the square is the diameter of the large circle; its side is the diameter of the small one. The ratio of the radii is $\sqrt{2}/2$ and the ratio of the areas is $1/2$.

**Theorem 8.2 (T; R for the identification).** $S_{max} = N \times k \times d = 4 \times \tfrac12 \times \sqrt{2} = 2\sqrt{2}$, and with $d = 1$, $4 \times \tfrac12 \times 1 = 2$. The arithmetic is exact. That $N = 4$ is the four settings of the square, $k = 1/2$ the projection constant of 2.2, and $d = \sqrt{2}$ the diagonal, is a reading of the known bound, not an independent derivation; in the proof, the 4 comes from the CHSH arrangement.

**Theorem 8.3 (T, the hourglass).** Stack the four inversion pairs $1$-$8$, $2$-$7$, $3$-$6$, $4$-$5$ at equal step. Their widths are $7, 5, 3, 1$, of sum $16 = 4^2$; the edges descend at 45°; the waist is empty, at $4.5$. The four directions of the drawing, 0°, 45°, 90°, 135°, are exactly the settings of Theorem 5.2. With the directions 0° and 90° alone, $|S| = 2$.

**8.4 (R).** "Classical: measure the sides. Quantum: measure the diagonals." "They pierced the form and wonder where the balance is, and they forgot to see that Tsirelson is a square." (the author, 14 November 2026). Hippasus isolated $\sqrt{2}$; Bell found 2 without it; Tsirelson found $2\sqrt{2}$ with it.

## 9. Status of Randomness, and Standard Objections

**9.1 (R).** The only source of apparent randomness is the dimensional projection $S^2 \to \{+1, -1\}$, which discards directional continuity. The Born rule is read as the statistical imprint of that compression.

**9.2 (R, determinism without superdeterminism).** The state $\lambda$ encodes relational constraints between outcomes, not individual outcome values. The measurement angles remain unconstrained by $\lambda$.

**9.3 (T, F, locality).** The model is non-signalling (Theorem 5.3). Like every model that reproduces the singlet cosine, it is not local in the sense of Bell, and Bell's theorem (1964) is not contested. In the vocabulary of Jarrett (1984) and Shimony (1986), a protocol written in one order shows parameter dependence without signalling; by 3.2 that order is not observable, and by 3.3 it need not be given. The claim of this paper is the geometric origin of the bound, not a restoration of Bell locality.

**9.4 (R, Lorentz invariance).** The updates depend only on the joint state and the local directions; the statistics are frame-independent.

**9.5 (R, why no operator).** The framework is static and relational. Seeking an operator would impose dynamical evolution on a geometric structure.

## 10. Entanglement as an Inversion Pair

**10.1 (R).** After the first reading, $\lambda'$ is the inverse of that reading on its axis. This is the structure $x \mapsto 9 - x$ realised physically: the outcome and the updated state form an inversion pair, and neither exists alone. The two outcomes are correlated not because a signal travels, but because they are two readings of one relational state from the two sides of the inversion. Correlation is memory, not causation.

## 11. Relation to Structural Closure

**Theorem 11.1 (T).** The map $x \mapsto 9 - x$ acts on $\{1, \dots, 8\}$ as an involution without fixed position and produces four pairs, $(1,8), (2,7), (3,6), (4,5)$, each of sum 9. Their common centre, the fixed point of the map, is $4.5$, between two positions. The ratio $4.5/9 = 1/2$, and in any base $b$ the same ratio is $\tfrac{(b-1)/2}{b-1} = 1/2$.

*Correction.* Earlier versions called $4.5$ "the arithmetic centre of $[1, 9]$". The centre of the positions 1 to 9 is 5. The value $4.5$ is the centre of the four pairs, the positions 1 to 8, the 9 being the closure.

**11.2 (R).** This $1/2$ and the $1/2$ of 2.2 are reached by two paths that do not speak to each other, discrete arithmetic and spherical geometry. The author reads the half-integer spin of fermions as this same ratio. It is a reading, not a derivation of spin.

## 12. The Ternary Structure Under Binary Measurements

**Theorem 12.1 (T, three chambers).** Outside the axis $\{3, 6, 9\}$, the positions come in neighbouring couples, one from each rail: $(1,2)$, $(4,5)$, $(7,8)$. Their centres are $1.5$, $4.5$, $7.5$; the walls between them are $3, 6, 9$; the gap is 3 each time.

**Theorem 12.2 (T, the triangle).** $4.5^2 + 6^2 = 7.5^2$. The three numbers are $3, 4, 5$ multiplied by $1.5$, and $4.5/7.5 = 3/5$, $6/7.5 = 4/5$. In the figure of Section 8, each point of the four-branched star opens at the acute angle of the triangle $3, 4, 5$ (*La Figure fondamentale*, 4.4 and 5.1). The perimeter is $18$, two turns of 9.

**Theorem 12.3 (T, the ladder).** From $4.5$ to $7.5$ by steps of $1/2$: $4.5, 5, 5.5, 6, 6.5, 7, 7.5$. Six steps, and $6 \times \tfrac12 = 3$; the pivot 6 is the third step, the exact middle.

**12.4 (R, O).** The author reads $4.5$ as the lower chamber and $7.5$ as the upper chamber, with the gap $\Delta c = 3$ as a ternary invariant under binary outcomes. Earlier versions posed $7.5$ by definition; Theorems 12.1 and 12.2 give it a count. The link between this arithmetic and the sphere of Sections 2 to 7 passes through the figure (6.3, 8.2, 8.3); these are correspondences of structure, not proofs, and their formal unification is open.

## 13. Falsifiability

Each of the following refutes the model if violated (P).

- **F1.** $E(a,b) = -\cos\theta_{ab}$ exactly, at all angles, for singlet pairs.
- **F2.** $S_{max} = 2\sqrt{2}$ exactly; any reproducible violation of the Tsirelson bound.
- **F3.** $P(A \mid a) = P(B \mid b) = 1/2$ for all settings; any observed signalling.
- **F4.** $k = 1/2$ for all binary readings on $S^2$.

These agree with standard quantum mechanics: they can refute the model and cannot separate it from quantum mechanics. Two statements of v1.2 are not carried here as tests: the criterion on $\Delta c \neq 3$, which has no written protocol, and the announcement of deviations from the cosine in "non-standard relational configurations", which contradicts F1 and has no operational definition (O).

## 14. Related Results

(F) Bell, 1964, the bound 2. Clauser, Horne, Shimony and Holt, 1969, the combination $S$. Tsirelson, 1980, the bound $2\sqrt{2}$. Aspect, Grangier and Roger, 1982, $S = 2.697 \pm 0.015$; Hensen et al., 2015, first loophole-free test. Popescu and Rohrlich, 1994, the maximum 4 without signalling. Toner and Bacon, 2003: the singlet correlation is reproduced exactly by a deterministic model on $S^2$ with two shared vectors and one single bit; the update of Definition 4.1 injects exactly one bit, the outcome $A$. Cerf, Gisin, Massar and Popescu, 2005: one use of the box of Theorem 6.1, with shared variables and no communication, reproduces the singlet statistics; this is the received counterpart of the passage from the bare sign to the reading of Definition 4.1. Landau, 1987, for the operator identity of Appendix C. Jarrett, 1984, and Shimony, 1986, for the decomposition of Bell locality.

## 15. Scope and Limits

The model reformulates the measurement of entangled spin-1/2 pairs; extension to several particles is open. It modifies no empirical prediction. An outcome is not stored in an object taken alone: it belongs to the relation, the pair and its reading together. This is principle P1; the received vocabulary calls such a model contextual, and the earlier statement that the model is "not contextual in the sense of Kochen and Specker" is withdrawn. It is not Bell-local (9.3). The decomposition of 8.2 is an exact arithmetic and a reading. Section 12 is arithmetic plus readings. No claim is made that this framework is the only deterministic non-signalling one: Bohm's theory is deterministic and non-signalling at the level of statistics.

## 16. Conclusion

Quantum correlations require neither ontological randomness nor collapse. They follow from one shared state on the sphere, one inversion, and one reading of flat density one half. The three known ceilings are three ways of reading the same square: its sides, its diagonals, its bare sign. What quantum mechanics measures at $2\sqrt{2}$ is the diagonal that the form always had.

## Appendix A. Uniqueness of the Relational Update

**(T, as stated in v1.2.)** The update must satisfy: (1) local outcome consistency, $A = \mathrm{sgn}(\lambda\cdot a)$; (2) total spin zero for the singlet; (3) minimal information injection, no degree of freedom beyond the outcome. An orthogonal projection $\lambda' \perp a$ violates (1); a rotation $\lambda' = R(\alpha)\lambda$ introduces an unconstrained parameter; a scaling violates the unit norm; a stochastic noise violates P3. The only transformation left is $\lambda' = -A\,a$. With Definition 4.1, determinism bears on the complete state $(\lambda, \mu)$. A continuous $\lambda$ cannot be rebuilt from the bit $A$ and the direction $a$.

## Appendix B. Comparison with Standard Interpretations

(R) Copenhagen: collapse, ontological randomness, measurement problem. Many-Worlds: universal wavefunction, branching. Bohm: particle positions, non-local dynamics, deterministic, non-signalling in its statistics. ARC: one geometric state on $S^2$, zero relational distance, no wavefunction, deterministic, falsifiable. The claim of v1.2, "only deterministic framework without non-local signalling", is withdrawn.

## Appendix C. The Double Derivation

Each load-bearing constant is derived twice, with a pencil and with the standard apparatus; the last line carries the same number.

| Constant | With a pencil | In the apparatus |
|---|---|---|
| $k = 1/2$ | cylinder around the sphere, one fold, one midpoint | $\mathbb{E}|a\cdot\lambda| = \tfrac12\int_0^\pi |\cos\theta|\sin\theta\,d\theta = \tfrac12$ |
| $2\sqrt{2}$ | diagonal of the square of side 2 | $\|\mathcal{B}^2\| \le 4 + 4 = 8$ |
| the mean | Descartes' proportional between 2 and 4 | $\sqrt{2\times 4} = 2\sqrt{2}$ |

## Appendix D. Version Notes

Nothing of v1.2 is erased; it stays on file with its sequel attached.

- **Reading rule.** v1.2, Eq. (3), and v3.6, Definition 1: bare sign. Read literally: Theorem 6.1. The "hemisphere overlap" wording of v3.6: Theorem 6.2. Completed rule: Definition 4.1 (from *Tsirelson's Bound Without Hilbert Space* v4.1, Theorem 2.1; Corpus ARC, Volume 7, chapters 1 and 2).
- **"No hidden variable distribution"** (v1.2, Section 5): the reading carries $\mu$ with the flat density one half (Theorem 7.1, Remark 7.3).
- **The centre** $4.5$: corrected wording (11.1).
- **The upper chamber** $7.5$: given a count (12.1, 12.2).
- **Exclusivity claim** of Appendix B: withdrawn.
- **Added:** the three ceilings; the flat density; the order symmetry; the figure and the hourglass; related results.
- **Not carried:** two statements of v1.2 listed in Section 13.
- **After an outside audit:** the order carried by the state (3.3, 3.4); the edge density stated at fixed settings, with its maximum (7.1); the axis of Remark 7.3; the sentence on Kochen and Specker withdrawn (Section 15); two related results added (Section 14).

## Appendix E. Verification and Sources

The script `emergence_verif.py` recomputes every statement marked T, in 37 checks, all passed on 22 November 2026: the three reading rules and their bounds; the cosine at all tested angles, in and out of the plane; the scan of settings; the margins; the joint table in both orders; the three densities of Theorem 7.1; Remark 7.3 on the sphere and on the circle; the model of Toner and Bacon; the constants of Sections 2, 6, 8, 11 and 12. Exact statements are checked in fractions or in closed form; sampled statements use three million draws with a stated tolerance.

Rechecked at source: Cerf, Gisin, Massar and Popescu, *Physical Review Letters* 94, 220403 (2005). Not rechecked at source: Landau, *Physics Letters A* 120, 54 (1987); Bell 1964; Clauser et al. 1969; Tsirelson 1980; Popescu and Rohrlich 1994; van Dam 2005; Toner and Bacon, *Physical Review Letters* 91, 187904 (2003); Jarrett, *Noûs* 18 (1984); Shimony 1986; Aspect et al. 1982; Hensen et al. 2015; Archimedes.

Corpus ARC: Volume 1, chapters 7 and 15; Volume 2, chapters 1, 4 and 13; Volume 7, chapters 1 and 2; *Tsirelson's Bound Without Hilbert Space* v4.1; *La Figure fondamentale* v2.5; *L'Observateur est la confusion* v0.17 (statements 2.2 to 2.2 ter).
