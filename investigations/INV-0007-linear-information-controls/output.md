# Linear coding controls for information through hexagram change

Date: 2026-11-01. Role: full-context specialist. Model family: GPT; exact model identifier and settings unknown. This continues the coordinator conversation, which has read the earlier reports and originated INV-0003. **All results are reported, not independently verified.**

## 1. Scope and decision

The user authorized starting the highest-value research after a review of INV-0004. Two isolated verifications were launched separately. This investigation develops the review's explicit counterexample without sending it to either verifier's blind first phase.

The question is what linear coding-theoretic controls teach about the information retained by traditional hexagram labels. The stopping rule is a checkable all-noise comparison, a complete linear upper-bound argument, and an exact classification at coin noise. This is formal mathematics on six independent uniform bits; it establishes no historical choice, intent, textual meaning or physical benefit from retaining more information.

Set X uniform on F₂⁶ and Y = X ⊕ E, with E having independent Bernoulli(p) bits, independent of X. Unless stated otherwise, 0 < p < 1/2 and ρ = 1 − 2p. Entropies are in bits. Write x₁ through x₆ bottom to top. The earlier labels are T(x) = (x₁,x₂,x₃) and G(x) = (x₁⊕x₄,x₂⊕x₅,x₃⊕x₆).

## 2. L1: a balanced label less informative than generation at every noise level

Define

    Λ(x) = (x₁⊕x₃⊕x₅, x₂⊕x₃⊕x₆, x₄⊕x₅⊕x₆).

Its matrix has columns 001, 010, 011, 100, 101, 110 (bit labels read in the displayed row convention). These are six distinct nonzero vectors of F₂³, so its rank is three. Each of its eight labels occurs eight times. Its row space has nonzero word weights 3,3,3,3,4,4,4; it is a punctured binary simplex construction, with the name used descriptively rather than as a novelty claim.

**Theorem.** I(G(X);Y) > I(Λ(X);Y) for every 0 < p < 1/2.

**Proof.** For any full-rank linear label A, uniformity of X implies that E and Y are independent. Therefore

    I(AX;Y) = 3 − H(AE).

The sorted probabilities of Λ(E), with a common denominator 8, are

    a = 1 + 4ρ³ + 3ρ⁴,
    b = 1 − ρ⁴  (six occurrences),
    c = 1 − 4ρ³ + 3ρ⁴.

Here a > b > c when 0 < ρ < 1. The sorted probabilities of G(E), also with denominator 8, are

    d₀ = (1+ρ²)³,
    d₁ = (1+ρ²)²(1−ρ²)  (three occurrences),
    d₂ = (1+ρ²)(1−ρ²)²  (three occurrences),
    d₃ = (1−ρ²)³.

For k = 1,...,7, subtract the sum of the largest k Λ-probabilities from the corresponding G-sum. Eight times these differences, in order, are A,B,C,D,C,B,A, where

    A = ρ²(1−ρ)²(ρ²+2ρ+3),
    B = 4ρ²(1−ρ),
    C = ρ²(1−ρ)(ρ³+ρ²+ρ+5),
    D = 2ρ²(1−ρ)(ρ³+ρ²+ρ+3).

Every expression is strictly positive. Thus the noise law G(E) strictly majorizes Λ(E). Strict Schur concavity of Shannon entropy gives H(G(E)) < H(Λ(E)), proving the theorem. The supplied script verifies every polynomial identity exactly. ∎

At p = 1/4, I(G;Y) = 0.136697991225... bits and I(Λ;Y) = 0.047311437251... bits. The noise masses of Λ, sorted, are (352,480,480,480,480,480,480,864)/4096. Displayed information values use 60-digit Decimal logarithms; the proof uses no numerical logarithms.

### Endpoint interpretation

Both labels have β = 6 and W₁ = 0, the worst possible values of the two coefficients in INV-0004 R5. Nevertheless their complete information functions are strictly ordered throughout the open noise interval.

At low noise, with L = log₂(1/p),

    H(Λ(E)) = 6pL + 6p log₂ e + O(p²L),
    H(G(E)) = 6pL + 6p(log₂ e − 1) + O(p²L),
    I(G;Y) − I(Λ;Y) = 6p + O(p²L).

This follows because Λ has six distinct single-flip syndromes, whereas G groups the six flips into three pairs.

At high noise,

    I(G;Y) = 3ρ⁴/(2 ln 2) + O(ρ⁸),
    I(Λ;Y) = 4ρ⁶/(2 ln 2) + O(ρ⁸).

The latter follows by expanding the eight explicit masses around uniformity. Their first deviations have degree three; four nonzero dual words have weight three. Thus the leading-coefficient statement in C-0036 survives, but its title and summaries must not imply that G minimizes complete information. No refutation of its precise coefficient inequalities is claimed.

## 3. L2: coordinate projections are optimal among all affine linear labels

**Theorem.** Let A be any rank-k binary matrix on n input bits and let λ(x)=Ax⊕b. Then, for every 0 ≤ p ≤ 1/2,

    I(λ(X);Y) ≤ k[1 − h₂(p)].

For 0 < p < 1/2 equality holds exactly when A has precisely k nonzero columns, necessarily linearly independent. These are coordinate projections followed by an invertible output transformation and an optional output offset.

**Proof.** As above, I(λ(X);Y)=k−H(AE). Choose k independent columns S and write AE=A_S E_S ⊕ A_R E_R. Conditioning on E_R gives

    H(AE) ≥ H(AE | E_R) = H(A_S E_S) = k h₂(p).

For strictness, the distribution of A_S E_S has nonzero Fourier coefficients in every character when 0 < ρ < 1. It cannot be invariant under translation by a nonzero vector: such invariance would annihilate a character which evaluates to −1 on that vector. Adding any extra nonzero column convolves this distribution with a nontrivial two-point Bernoulli law. Strict entropy concavity increases its entropy. Further independent additions cannot decrease entropy. If there are no extra nonzero columns, equality is immediate. ∎

This uses only elementary entropy and linear algebra, not family 119 or any claimed Courtade–Kumar proof. It resolves the affine-linear subclass of Q-009. It does not resolve the conjecture over all balanced eight-valued labels; a better label, if one exists, must have a non-affine partition. Nonlinear output renaming of an affine partition also leaves its information unchanged and cannot improve the benchmark.

## 4. L3: complete exact coin-noise classification of linear three-bit labels

There are exactly

    [6 choose 3]₂ = (63·62·60)/(7·6·4) = 1395

three-dimensional subspaces of F₂⁶, hence 1395 rank-three linear-label partitions up to invertible linear output renaming. Output offsets do not change these partitions. The script enumerates their unique reduced-row-echelon bases, then independently enumerates every unordered triple of nonzero row vectors and checks equality of the resulting subspace sets.

For each label A and each output z, Fourier inversion gives

    P(AE=z) = (1/8) Σ_{u∈F₂³} (−1)^(u·z) ρ^wt(uA).

Up to permutation of the eight outputs, the enumeration gives 22 distinct multisets of probability polynomials in ρ. This is a grouping by exact noise law; it is not asserted to classify coordinate-permutation orbits in general.

At coin noise, p=1/4, every mass is an integer n_z divided by D=4096. Consequently

    I(AX;Y) = −9 + (1/4096) log₂ ∏_z n_z^(n_z).

Comparing the positive integers ∏ n_z^(n_z) compares information exactly. No floating-point or logarithmic approximation enters any extremal verdict.

**Exhaustive result.**

- The 20 coordinate-projection partitions are exactly the maxima, at 0.566165626622... bits.
- The 30 coordinate permutations of Λ's partition are exactly the minima, at 0.047311437251... bits.
- Every other rank-three linear partition lies strictly between these extremes.

The script enumerates all 720 input-coordinate permutations of Λ and checks that their distinct row spaces are precisely the 30 minimizing spaces. It also checks that all 20 maxima are precisely the coordinate choices. All 1395 RREF bases are preserved in the output, grouped into the 22 polynomial profiles.

This is a finite reported theorem with an exhaustive computation; it is not an independent verification, and its novelty relative to coding theory is unknown.

## 5. What remains open and what failed

**Candidate extension.** Λ might minimize information among all balanced affine-linear three-bit labels of six bits for every 0 < p < 1/2. The result above establishes this only at p=1/4. L1 compares Λ with G at every p; that is a different statement.

A tempting proof would show that every competing linear noise law majorizes Λ's law. This stronger condition is false. At p=1/4, the matrix with row bitmasks (9,10,60) has a smaller sum of its largest seven noise masses than Λ does. The script checks that failure with exact rationals. This does not refute the entropy comparison, only this sufficient proof route.

Not ruled out: all-noise linear minimality of Λ; a different minimizer at another p; a non-affine balanced partition retaining either more information than T or less than Λ. No claim of global minimality among nonlinear labels is made.

## 6. Yijing use and novelty calibration

The information analysis distinguishes three different kinds of object:

1. the traditional-looking trigram, palace and generation labels, with historical correspondence still subject to source work;
2. explicit artificial coding controls such as Λ;
3. general extremal statements over a specified comparison class.

L1 repairs an interpretive overstatement without discarding the precise endpoint coefficients. L2 prevents repeated searches for a better affine-linear trigram label. L3 supplies a rigorous low-retention control at the actual coin probability. Together with C-0035, conditionally on its eventual verification, the all-noise chain becomes T > B > G > Λ. Only the first two comparisons in that chain depend on the earlier computer-assisted proof.

Low retention is a mathematical feature, not an established defect of divination. Whether a reading should preserve or disrupt a particular distinction is a separate interpretive question. No evidence of historical optimization follows from any extremal calculation here.

Bounded prior-art search on 2026-11-01 used arXiv queries for linear quantization, Bernoulli syndrome entropy, simplex codes and most-informative linear functions. No source establishing the exact six-bit comparison or classification was identified in this bounded search. The methods are elementary coding and information theory; absence from these results does not establish novelty. Chinese-language scholarship and coding-theory classification tables were not exhaustively searched.

Related primary sources:

- [Kumar and Courtade, Which Boolean Functions are Most Informative?](https://arxiv.org/abs/1302.2512): the original one-bit problem, not a premise of L1–L3.
- [Mahdavifar and Beirami, The Most Informative Bit and Beyond, v2](https://arxiv.org/abs/2609.26444v2): its abstract motivates coordinate benchmarks, claims a one-bit proof and proposes optimality for 2–7 output bits. The proof was not audited here. Our affine-linear upper bound is self-contained and does not settle that broader conjecture.

## 7. Reproducibility and handoff

Executed code: `compute/experiments/INV-0007/linear_information.py`, standard-library Python, with output `results.json` in this investigation. The output records Python version, script hash, all finite classes, exact majorization polynomials and integer comparison outcomes. Reproduce to a fresh path:

```bash
python3 -I compute/experiments/INV-0007/linear_information.py --out /tmp/linear-information-reproduction.json
```

A first script check exposed a list-versus-tuple comparison error in a certificate assertion; the assertion was corrected before the frozen run. An independent exploratory script preceded the final implementation in the temporary research directory. Only the supplied final code/output are the reproducible evidence for the claims above.

| Local ID | Contribution | Evidence | Scope / next |
|---|---|---|---|
| L1 | Balanced Λ retains less information than G at every symmetric nontrivial noise level | explicit laws, exact majorization proof, exact polynomial identities | formal six-bit model; different-family audit |
| L2 | Coordinate projections maximize information among affine-linear rank-k labels for every noise level | self-contained entropy proof with equality characterization | general n,k symmetric-noise model; does not settle nonlinear Q-009 |
| L3 | Coin-noise extrema across all 1395 rank-three linear partitions | two exhaustive enumerations, exact integer comparisons | p=1/4 only; all-noise minimum unproved |

Immediate reuse: correct broad endpoint-extremality summaries; use Λ as an explicitly artificial comparison; focus any search for a better-than-trigram label on genuinely non-affine partitions. Keep this report out of blind sessions. A future verifier should derive from statements before receiving this evidence.
