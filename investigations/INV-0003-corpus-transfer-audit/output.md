# Manuscript transfer: results, finite probes, and priorities

Date: 2026-10-31. Role: full-context synthesis and coordination. Model: Codex assistant, exact model unknown. Context-exposed. All results below are **reported**, with registration and independent verification pending.

## 1. Scope and source status

The pinned catalogue contains 721 manuscripts in 373 families. A searchable catalogue ingests every title and abstract; keyword retrieval is not a proof review. Theorem statements in 16 manuscripts from 11 families were inspected. The manuscripts, companion results, and formalization links are evidence to inspect, not automatically verified facts or independent corroboration. No claim of exhaustive proof review or literature novelty is made.

Pinned source commit: `4eaee87548250b2682affda7d05d947c05554bae`. Principal theorem sources: [sharp binary information](../library/openai-math-4eaee875/sources/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex), [uniform tables](../library/openai-math-4eaee875/sources/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/build/sections/introduction.tex), [bounded tables](../library/openai-math-4eaee875/sources/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/build/sections/introduction.tex), [matching entropy](../library/openai-math-4eaee875/sources/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/sections/01-introduction.tex), and [coordinate shuffles](../library/openai-math-4eaee875/sources/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex). Exact labels and application limits are in the [transfer review](../../roadmap/literature/openai-math/transfers.md).

No historical dataset is used in the pilots. Hexagrams are formal six-bit words, with coordinate one the bottom line. The palace difference set is taken as a specified mathematical object; whether it matches a cited tradition remains C-0017, not established here. The symmetric channels below are model choices, not claims about a yarrow or coin procedure.

## 2. L1 — Optimal binary summaries of pairwise differences (conditional transfer)

Let X=(L,U) be uniform on {0,1}^{2k}; let Y=X xor E, where the 2k coordinates of E are independent Bernoulli(p), independent of X, with 0≤p≤1/2. Put D(X)=L xor U and q=2p(1-p). For every deterministic Boolean function g on k bits,

    I(g(D(X));Y) = I(g(D(X));D(Y)).

Assuming family 119's Courtade–Kumar theorem,

    I(g(D(X));Y) ≤ 1 − h₂(q),

in bits. A single difference coordinate attains the bound. A raw input coordinate retains 1−h₂(p) bits. For 0<p<1/2, q>p, so the best one-bit summary restricted to pairwise differences retains strictly less information than a raw coordinate. No uniqueness claim for equality is needed.

**Transfer proof.** The invertible coordinate change (L,U)↦(D,U) makes D and U independent uniform k-bit words. Write Z=E_L xor E_U. Then D(Y)=D xor Z is a binary symmetric product channel of crossover q. Conditional on D and all the noise, U(Y)=U xor E_U is still independent uniform. Thus U(Y) is independent of the pair (D,D(Y)); observing it adds no information about g(D). Apply the external binary-output theorem to the uniform k-bit input D and its product-noise observation D(Y). Taking g to be one coordinate proves attainment. The raw-coordinate formula is the ordinary binary symmetric channel calculation. End of proof, conditional on the imported theorem.

For k=3 the code exhaustively examines all 256 Boolean functions g at p=1/8 and p=1/4. At these two noise values, exactly the six signed coordinate truth tables attain the numerical maximum. The rational conditional masses are exact; entropy evaluation is binary64. This is a finite consistency check, not a verification of family 119 in all dimensions or at every noise level.

This transfer contributes a global benchmark for arbitrary nonlinear summaries and a parameterized research question beyond six lines. The reduction to the difference channel is elementary; the all-dimension optimization uses the imported theorem. General biased or dependent inputs and asymmetric changes fall outside its hypotheses.

## 3. L2 — Two equal-entropy palace labels have different noise robustness

Use the eight difference words in DEF-011. For each x define G(x)=φ(x)=L xor U, let d(G(x)) be the unique difference word with that φ-value, and define B(x) as the three-bit base in x xor d(G(x))=(B,B).

Enumeration checks that all 64 pairs (B,G) occur exactly once. Therefore B and G are independent uniform eight-valued labels, each with entropy three bits. This is a re-derivation of the encoding structure already in C-0016, not an independent verification or a new structural discovery.

The new finite observation concerns their response to the specified symmetric noise:

| Flip probability p | Raw lower trigram, formula 3[1−h₂(p)] | Base label I(B(X);Y) | Difference/generation label I(G(X);Y) |
|---|---|---|---|
| 1/8 | approximately 1.369307 | 1.103576694734 | 0.726364612385 |
| 1/4 | approximately 0.566166 | 0.378621055176 | 0.136697991225 |

For G the exact formula is 3[1−h₂(2p(1-p))], by independence of the three induced channels. For B the displayed values are direct numerical evaluations from exact integer posterior masses; the full arrays' hashes are in `pilot-results.json`. Both B and G labels may be renamed arbitrarily without changing mutual information. Their bit encodings are not used to compare their full eight-valued labels.

The base label is more robust at these two parameters, while a raw trigram retains more information than either. This prevents selecting the palace system merely because it looks robust compared with its own quotient. An all-noise ordering, a sharp optimality statement under explicit invariance constraints, and robustness to asymmetric or dependent changes remain open. The observed gaps are worth explaining, but neither historical purpose nor literature novelty follows.

## 4. L3 — Exactly 4,096 opposition-compatible pairings at six lines

For all six-bit words construct a simple undirected graph whose edges join x to Cx and, when different from x, to Rx. This uses the weak constraint that paired words may be related by reversal or complement. It does not impose the received rule preferring reversal whenever possible.

The graph has eight two-vertex components and twelve four-cycles. A two-vertex component has one perfect matching; a four-cycle has two. Hence there are exactly 2¹²=4,096 perfect matchings. The code explicitly enumerates all 4,096 combinations and checks that each covers every word once.

**General count.** For 2k lines, k≥1, the commuting involutions R and C have 2^k fixed points of R and 2^k fixed points of RC. These sets are disjoint because C has no fixed point. They form 2^k two-vertex orbits. All remaining points lie in four-vertex orbits, giving 2^{2k−2}−2^{k−1} four-cycles. Thus the number of matchings in this specified graph is

    2^(2^{2k−2} − 2^{k−1}).

Each orbit contributes independently, proving the count. End of proof. At k=3 this gives 4,096.

The uniform matching law has entropy 12 bits. At its edge marginals the imported family-113 pointwise entropy bounds evaluate to −22.5≤H≤24 bits. The negative lower bound is vacuous and the upper bound is loose. Therefore a general matching FPRAS or entropy bound does not materially improve this particular finite problem. Exact factorization should be used first. More complicated compatibility graphs may change that assessment.

The result counts a formal comparison class, not historical candidate arrangements. A probability under the uniform matching law would require choosing that law explicitly; it would not be a probability of historical design. Novelty of this elementary orbit count is unknown.

## 5. L4 — A sampling theorem does not choose the correct null measure

With row and column margins (2,2), the three 2×2 tables are

    [[0,2],[2,0]], [[1,1],[1,1]], [[2,0],[0,2]].

A uniform-table law assigns masses (1/3,1/3,1/3). Uniformly assigning two objects of each of two types to two labelled rows of size two induces multiplicities (1,4,1), hence probabilities (1/6,2/3,1/6). This follows by counting choose(2,a)choose(2,2−a) allocations for the first cell a. The extreme-table event has probabilities 2/3 and 1/3, respectively. End of finite counting proof.

Family 115's exact sampler concerns the first law. It must not silently replace a permutation/token-allocation null with that law. For textual categories, canon allocations, or trigram tables, the elementary objects and induced measure must be specified before selecting a sampler. The toy example is methodological and is not evidence about any actual Yijing table.

The unbounded uniform-table sampler has no cell restrictions. The companion counting theorem handles upper bounds, including structural zeros. A bounded sampler would need a justified reduction or separate implementation and error analysis; it is not supplied merely by citing the unbounded sampler. General counting results also do not automatically count sequences when adjacency, order, or unique-use constraints are missing from the encoding.

## 6. L5 — Uniform hexagram marginals can conceal almost maximal order dependence

In the coordinate-switch form of a Thorp sweep on 64 positions, independently swap each pair along coordinate one, then coordinate two, and so on through coordinate six. This is a formal local transformation of positions. It is not asserted to be an attested generation procedure for the received order.

Each particular label ends uniformly among the 64 positions after one sweep: each coordinate is refreshed by an independent fair choice exactly once. The code verifies all 64 initial labels' exact marginal laws. Nevertheless the entire permutation used at most 192 random bits, so it has support of size at most 2¹⁹². Comparing with the uniform law on S₆₄ gives

    TV ≥ 1 − 2^192/64! = 1 − 2^(−103.995143941724…).

This is the finite support bound in the source's Theorem `thm:mixing`, or directly the uniform measure of the support. In particular one-card uniformity is compatible with full-order distance from uniform greater than 1−5×10^−32. The source's finite support obstruction also forces at least ten physical shuffles to reach TV≤1/4. End of finite argument.

The upper-mixing claim in the principal manuscript is asymptotic. Its 1600d statement is not a numerical certificate at d=6. The regular-trace companion states an all-dyadic-size bound but leaves its absolute power unspecified in the theorem statement; the needed effective constant has not been extracted here. Do not use either as a practical burn-in certificate for 64 positions.

This supplies a useful new line: study locally generated orderings using joint observables, full-permutation obstructions, and complexity relative to a fixed grammar. Membership in the generated group is insufficient: coordinate-edge transpositions generate all of S₆₄. Useful questions concern short descriptions, bounded-depth constraints, or independently discriminating predictions.

## 7. L6 — A direct spectral transfer fails for balanced hexagram characters

For any complete enumeration x₀,…,x₆₃ of the six-bit words and any nonzero linear character a, let sⱼ=(−1)^{a·xⱼ} and P(z)=Σⱼsⱼzʲ. Exactly half the words have each sign, so P(1)=0. Thus P cannot satisfy a positive lower bound everywhere on the unit circle.

This blocks direct use of the positive lower envelope in family 076's ultraflat construction for these balanced sequences, regardless of the ordering. End of proof.

Not ruled out: spectral questions away from z=1, aperiodic correlation, nonlinear or biased observables, incomplete arrangements, and different sequence alphabets. The result does not close the study of ordering spectra. At length 64, the new general Barker/circulant obstruction also needs comparison with older dyadic finite-length obstructions before being credited with additional leverage.

## 8. Priorities and unresolved work

1. **Information-preserving observables and invariance tradeoffs (family 119).** Strongest direct transfer: matched finite objects, a quantitative all-dimension benchmark, and a finite gap worth explaining. Next: independently reproduce L1–L2, seek a proof or counterexample to all-noise comparisons, compare with raw-coordinate and alternative-partition baselines, then introduce source-supported asymmetric procedures.
2. **Constrained comparison ensembles (family 115; conditional support from 113/131).** Strongest methodological upgrade: replace an arbitrary single null with precisely specified conditional laws and quantify uncertainty. Begin with exact finite examples. The imported algorithm is relevant only after the combinatorial model and measure match; constants and implementation remain work, not delivered acceleration.
3. **Local transformations and joint ordering structure (family 238).** Strong finite obstruction and a distinct modelling direction. Next: fix the allowable operations independently of the target order; compute joint statistics and short-program limits before looking for historical fits. Extract finite constants only if a mixing-based analysis truly needs them.

Families 134 and 161 supply interpretation safeguards: low generalized star height is universal and does not ensure a short useful explanation; matching selected motif densities need not certify full randomness. Family 206's undecidability is not an obstruction to analyzing an explicitly fixed finite algebra. Family 122's independent deletion-trace model has not been established for historical witnesses. Quantum dimension-six bases and the six-vertex model share vocabulary or numbers with hexagrams but no applicable mathematical mapping has been supplied.

These are positive priorities, not closures of deferred territory. Every deferred route needs a concrete mapping, nonvacuous finite statement, and an advantage over the elementary baseline before promotion.

## 9. Reproducibility, dependencies and next checks

Executed code: `compute/experiments/INV-0003/corpus_pilots.py`. Complete saved output: `pilot-results.json`. To reproduce, write to a fresh scratch output path; never overwrite the frozen output or code. All enumeration is deterministic. Exact noise weights use integer powers and exact probabilities use rational arithmetic; information values use binary64 logarithms. The code states every artificial model and contains the complete eight-word difference set. No source data or cited historical correspondence is smuggled into the formal computation.

The local results depend on different evidence: L1's general optimization is conditional on an external theorem, L2's information values are numerical, L3/L4/L5/L6 have elementary arguments and finite checks where stated. Agreement with a source result does not verify that source. New records should retain these distinctions.

Next assignments must independently verify the local consequences before significance is assigned; audit the external theorem and its exact formalized statement separately where a global application relies on it. Source work must establish the procedure/arrangement inputs before any result is called a fact about historical Yijing material. Novelty research must search the application statements, not only the new manuscripts' terminology.

## 10. Local registry

| Local ID | Exact contribution | Evidence / status | Dependencies | Recommended next action |
|---|---|---|---|---|
| L1 | Binary summaries of pairwise differences reduce to noise q=2p(1−p); conditional optimum 1−h₂(q) | reduction proof; imported optimization conditional; reported | uniform independent symmetric noise; family 119 | verify reduction and source statement; extend only after hypothesis audit |
| L2 | Base/difference labels have the displayed distinct information values at two noise parameters | complete finite integer masses, numerical entropy; reported | specified D, L1's channel model; encoding structure in C-0016 | independently recompute; search all-noise proof and novelty |
| L3 | Opposition graph has 4,096 matchings at six lines; general count given above | orbit argument and six-line enumeration; reported | specified R,C; family 113 only for bound comparison | check count; use exact baseline; avoid unnecessary general algorithms |
| L4 | Uniform tables and uniformly labelled allocations induce different null probabilities | exact three-table enumeration; reported | specified allocation model; family 115 scope | design the intended ensemble before choosing a sampler |
| L5 | One-sweep uniform marginals coexist with TV≥1−2¹⁹²/64! for the full ordering | finite support argument and exact marginal check; reported | specified coordinate switches; family 238 finite lemma | test joint statistics and finite-depth mechanisms |
| L6 | Balanced nonzero character sequences have P(1)=0 and cannot satisfy an everywhere positive ultraflat lower envelope | elementary proof; reported scoped negative | complete word enumeration; family 076 comparison | use a correctly constrained spectral baseline; retain nearby variants |
