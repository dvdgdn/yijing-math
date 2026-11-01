Investigation ID: INV-0006. Assignment: ASN-0014.

---

# Phase 2: Audit the Original Evidence

Your phase-1 verdicts are fixed. Compare them with the supplied report, output and code. Explain discrepancies. Audit the computer-assisted argument for V4 region by region: the analytic bounds near p = 0 and p = 1/2, the monotonicity argument, the grid and its numerical margin. Check the exact source statement used for V3.

Give a final verdict table distinguishing formal correctness, numerical support and external applicability. Do not give historical verdicts.

Follow the common research charter and the research handoff protocol.

---

## Supplied material: `investigations/INV-0004-divination-information-bounds/output.md`

# Divination channels, Boolean information bounds, and the robustness of hexagram labels

Date: 2026-10-31. Role: full-context specialist and outside adjudicator, literature-assisted. Model: Claude Opus 5.5 (model family claude; exact identifier unknown). Context-exposed: the whole repository was visible, including INV-0001, INV-0003 and the pinned manuscript library. **Every result below is reported. None is a verification.** Local IDs R1–R8 are mapped to the ledger in `registration.md`.

## 1. Question and stopping rule

The aim was to choose, from the whole pinned manuscript corpus, the results that give real leverage on a 64-element object, and to turn the best of them into checkable Yijing-specific consequences.

The working filter came from an independent read of all 373 family descriptions and a keyword sweep of all 721 abstracts; the screen is recorded in `roadmap/literature/openai-math/adjudication.md`. A theorem helps at this scale only if it quantifies over a space too large to enumerate. Two examples are all 2^64 Boolean questions about a hexagram, or all balanced 8-class labels. Asymptotic theorems are vacuous at n = 6 unless the question concerns the n-line family.

Exactly one family passes the filter cleanly: family 119, the Courtade–Kumar theorem. Its natural Yijing target is the divination layer. The questions fixed before computing were:

1. Which line-change channel does each divination procedure induce?
2. What does family 119 then say about yes/no questions?
3. How robust are the three traditional eight-valued labels (trigram, palace and generation) under that channel, at every noise level?
4. Does anything survive when the yarrow procedure's asymmetry removes the theorem's hypotheses?

Stopping rule: stop after exact answers to questions 1–3 and bounded evidence for question 4. Do not open further observable classes.

## 2. Models (explicit; no cited procedure is assumed)

Hexagram x ∈ {0,1}⁶, read bottom to top, yang = 1 (DEF-001). Each procedure generates the six line values independently. A line value v ∈ {6,7,8,9} determines the primary line X (yang iff v ∈ {7,9}) and the change bit E (iff v ∈ {6,9}). The changed hexagram is Y = X ⊕ E. When E = 0, Y = X is used as a formal convention.

| Model | Definition | P(6), P(7), P(8), P(9) |
|---|---|---|
| coins | three fair coins worth 2 or 3; value = sum | 1/8, 3/8, 3/8, 1/8 |
| yarrow-standard | first change removes 5 or 9 stalks (3/4, 1/4); second and third remove 4 or 8 (1/2, 1/2) | 1/16, 5/16, 7/16, 3/16 |
| yarrow-uniform | 49 stalks. Each change: left heap L uniform on 1..n−1; one stalk is hung from the right heap; both heaps are counted by fours (remainder 1–4, an empty heap gives 0) | 77/1612, 4051193/14556360, 424399/939120, 5957/26832 |
| yarrow-binomial | as yarrow-uniform, with L ~ Binomial(n, 1/2) conditioned on 1 ≤ L ≤ n−1 | 0.0625, 0.3125, 0.4375, 0.1875 (to 4 places; exact rationals in `results.json`) |

The labels are defined on x = (L, U), with L the lower trigram (lines 1–3) and U the upper (lines 4–6):

- **T** = L, the lower trigram. By symmetry the same holds for any three lines.
- **G** = L ⊕ U, the generation label. Its i-th bit says whether lines i and i+3 differ.
- **B** = the base trigram b in x = (b, b) ⊕ d(G), with d(G) the unique word of the difference set D = {000000, 100000, 110000, 111000, 111100, 111110, 111010, 000010} (DEF-011) having that G. This is the palace label.

B and G are each uniform on eight values and jointly determine x (C-0016). Whether D encodes a cited palace table is C-0017. Nothing here depends on that correspondence.

## 3. Results

### R1. The procedures as line channels (exact)

| Model | P(primary yang) | P(change \| yang) | P(change \| yin) | P(changed yang) | I(primary; changed), 6 lines | I(primary; change mask), 6 lines |
|---|---|---|---|---|---|---|
| coins | 1/2 | 1/4 | 1/4 | 1/2 | 1.13233 bits | 0 |
| yarrow-standard | 1/2 | 3/8 | 1/8 | 3/8 | 1.23261 bits | 0.37367 bits |
| yarrow-uniform | 0.500322 | 0.443736 | 0.095595 | 0.326078 | 1.12701 bits | 0.70867 bits |
| yarrow-binomial | 0.499998 | 0.375001 | 0.125002 | 0.374999 | 1.23259 bits | 0.37367 bits |

**Consequences.**

- Under the coins model, the primary hexagram is uniform. The primary-to-changed transition is *exactly* the product binary symmetric channel with crossover 1/4. The changing-line mask is independent of the primary hexagram.
- INV-0003 described its p = 1/4 channel as an artificial model choice (§1 there), but that channel *is* the coins model. Its L1–L2 numbers at p = 1/4 are therefore statements about this model of the three-coin oracle. The source question remains open: is the three-coin method as modelled here, and is a changed hexagram defined when nothing changes?
- Under yarrow-standard, the primary is again uniform. The transition, however, is a binary *asymmetric* channel (yang→yin 3/8, yin→yang 1/8). The changed hexagram is biased toward yin, with P(yang) = 3/8 per line.
- The *set of moving lines* carries 0.374 bits about the primary hexagram under yarrow-standard and none under coins.
- Under both models each line moves with probability 1/4. The number of moving lines is Binomial(6, 1/4) under both, so reading rules keyed to the number of moving lines see identical statistics.

Evidence: exact rational computation; per-line informations are evaluated with binary64 logarithms.

### R2. Sensitivity of yarrow probabilities to the splitting model (exact)

The textbook values 1/16, 5/16, 7/16, 3/16 are what yarrow-binomial reproduces to about 10⁻⁶. They are *not* robust to how the heap is split.

- Under yarrow-uniform the old-yang/old-yin ratio rises from 3 to 4.65 (5957/26832 ÷ 77/1612).
- The primary hexagram stops being exactly uniform: P(yang) = 14565731/29112720 ≈ 0.500322.
- Information leaked by the moving-line set almost doubles, from 0.374 to 0.709 bits.

Hence any claim about "the" yarrow probabilities needs both a cited procedure description and a physical model of the split.

### R3. One-bit questions under the coins model (conditional on external family 119)

**Statement.** Assume Corollary `main:ck` of family 119 (import contract in §5). Under the coins model, every deterministic yes/no question f about the primary hexagram satisfies

    I(f(primary); changed) ≤ 1 − h₂(1/4) ≈ 0.188722 bits.

A single line attains this bound. Because the coin joint law is exchangeable (Y = X ⊕ E with X and E independent uniform and symmetric), the same bound holds for every question about the changed hexagram regarding the primary.

The corollary also gives a refined bound ψ(ρ r_m)/ln 2 for a question with output mean m, with ρ = 1/2. Sharpness for biased questions is not claimed by the source.

**Proof.** R1 gives the hypotheses of the corollary exactly: uniform input, independent symmetric noise, ρ = 1 − 2·(1/4) = 1/2. ∎

**Exact values for formally defined questions** (bits, coins model; yarrow columns for comparison, where the bound does not apply):

| Question | Yes-count | Coins I | Refined bound | Yarrow, about primary | Yarrow, about changed |
|---|---|---|---|---|---|
| line 1 is yang | 32 | 0.18872 | 0.18872 | 0.20543 | 0.20543 |
| at least four yang lines | 22 | 0.12718 | 0.18195 | 0.13439 | 0.10059 |
| lower trigram has ≥ 2 yang lines | 32 | 0.14741 | 0.18872 | 0.15975 | 0.15283 |
| palace label = 000 | 8 | 0.05551 | 0.12112 | 0.06311 | 0.07468 |
| lower trigram = upper trigram | 8 | 0.01971 | 0.12112 | 0.02215 | 0.03092 |
| figure equals its top-to-bottom reading | 8 | 0.01971 | 0.12112 | 0.02215 | 0.03092 |
| generation label = 111 | 8 | 0.01971 | 0.12112 | 0.02314 | 0.03017 |
| exactly three yang lines | 20 | 0.01395 | 0.17810 | 0.01625 | 0.04009 |
| odd number of yang lines | 32 | 0.00018 | 0.18872 | 0.00026 | 0.00067 |

**What the import adds.**

- The source's own prior-work section reports that balanced functions were already covered at |ρ| ≤ 0.914 by a computer-assisted argument (Yu 2026, cited there; not checked here). It also reports that Samorodnitsky covered a high-noise range. Coin noise is ρ = 0.5. If those reports are right, the newly supplied part is the bound for **biased** questions (like most rows above) and the bias-refined curve.
- An independent preprint, arXiv:2609.26444 (22 Sep 2026; authors as listed on the abstract page: Mahdavifar and Beirami), also claims a proof of the Courtade–Kumar conjecture. Only its abstract page was read. The premise therefore has two claimed independent proofs; neither was audited here.
- A useful empirical remark: the refined bound is far from attained by traditional-looking biased questions. For example, palace membership retains 46% of its refined bound.

### R4. Robustness ordering of the three labels at every noise level (computer-assisted proof)

**Theorem.** Let X be uniform on {0,1}⁶ and Y = X ⊕ E with independent Bernoulli(p) noise bits. Then for every 0 < p < 1/2:

    I(T(X);Y) > I(B(X);Y) > I(G(X);Y).

At p = 1/4, the coins model (R1), the values are 0.566166 > 0.378621 > 0.136698 bits.

This settles the all-noise comparison that INV-0003 §3 left open and that ASN-0010 proposed as its first extension. It adds the comparison with the trigram.

**Proof.** All three labels have entropy 3 bits, so it suffices to compare H(λ|Y). By data processing, BSC(p₂) is a degradation of BSC(p₁) for p₁ < p₂ ≤ 1/2. Hence p ↦ H(λ|Y) is nondecreasing for each label λ. Each comparison is split into three regions.

*B versus G.*

- **High noise, p ≥ 0.23.** Line 6 is the third bit of B (every word of D has line 6 = 0), so I(B;Y) ≥ I(X₆;Y) = 1 − h₂(p) = φ(ρ), with ρ = 1 − 2p. Also I(G;Y) = 3φ(ρ²) exactly, because the three bits of G pass through independent BSC(2p(1−p)) channels (INV-0003 L1's reduction, re-derived here).
  - From φ(t) = (1/ln 2)Σ_{k≥1} t^{2k}/(2k(2k−1)) we get φ(ρ) ≥ ρ²/(2 ln 2) and 3φ(ρ²) ≤ 3ρ⁴/(2 ln 2·(1−ρ⁴)).
  - The first exceeds the second whenever ρ⁴ + 3ρ² − 1 < 0, i.e. for ρ < 0.5502. That covers p ≥ 0.23.
- **Low noise, p ≤ 2⁻¹⁰.** By Fano, H(B|Y) ≤ H(B|B(Y)) ≤ h₂(P_e) + P_e log₂ 7.
  - Exactly 128 of the 192 edges of the 6-cube cross palace boundaries: each palace induces 8 internal edges. So a single flip changes B with probability 2/3, and P_e ≤ 1 − (1−p)⁶ − 2p(1−p)⁵ ≤ 4p + 10p².
  - Using h₂(x) ≤ x log₂(e/x) and H(G|Y) = 3h₂(2p(1−p)) ≥ 6p(1−p)(log₂(1/p) − 1), the inequality reduces to a linear inequality in L = log₂(1/p). Its threshold is L > 7.57, and L ≥ 10 here.
- **Middle, [2⁻¹⁰, 0.23].** A geometric grid of 30 intervals with ratio 6/5 is used, with exact rational p. On each interval [a, b] the code checks H(G|Y)(a) − H(B|Y)(b) > 10⁻¹⁰. The smallest margin is 0.0102.

*T versus B.*

- **Low noise, p ≤ 2⁻¹⁴.** Condition on the event A = {|E| ≤ 1}. Then H(B|Y) ≥ P(A)·avg_y h₂(m_y p/(1+5p)), where m_y is the number of palace-boundary flips at y. The distribution of m_y is 3 (8 vertices), 4 (48), 5 (8), with mean 4. Against H(T|Y) = 3h₂(p), the inequality reduces to L·(4(1−5p) − 3) > (1−5p)c₁ + 3 log₂ e, with c₁ = avg m_y log₂ m_y = 8.0456. The threshold is L > 12.39.
- **High noise, p ≥ 0.48475.** First, I(T;Y) = 3φ(ρ) ≥ 3ρ²/(2 ln 2).
  - For the upper bound on I(B;Y), use t ln t − t + 1 ≤ (t−1)²/(2 min(1,t)). Write χ²_B(ρ) = Σ_j ρ^{2j} W_j(B), where W_j(B) = Σ_k Σ_{|S|=j} f̂_k(S)²/π_k exactly, with W(B) = (0, 13/8, 5/2, 9/4, 1/2, 1/8, 0). Then I(B;Y) ≤ χ²_B(ρ)/(2 ln 2 (1 − Cρ)), with C = max_k Σ_S |f̂_k(S)|/π_k = 15.
  - The required inequality 3ρ²(1 − 15ρ) > χ²_B(ρ) holds for ρ ≤ 0.0305.
- **Middle, [2⁻¹⁴, 0.4849].** The grid has 233 intervals: geometric with ratio 9/8 below 0.05, and steps of 1/400 above. The smallest margin is 5.4 × 10⁻⁴, attained near p = 0.483.

Grid masses are exact rationals. Logarithms use binary64 libm calls; the stated margin assumes a per-call error far below 10⁻¹². This is a computer-assisted argument, not a formal interval-arithmetic certificate. ∎

### R5. Why this ordering: endpoint coefficients and their extremal values

For any eight-valued label λ with blocks A_k, as p → 0 and as ρ = 1 − 2p → 0:

    I(λ;Y) = H(λ) − β(λ)·p log₂(1/p) + O(p),      β(λ) = 2|∂λ|/64 (mean number of single flips that change the label),
    I(λ;Y) = W₁(λ)·ρ²/(2 ln 2) + O(ρ⁴),            W₁(λ) = Σ_k ‖s(A_k)‖²/(64|A_k|),  s_i(A) = Σ_{x∈A} (−1)^{x_i}.

The first expansion follows from the one-flip posterior. In the second, the cubic Kullback–Leibler term first meets Fourier levels (1, 1, 2), so it is O(ρ⁴).

| Label | β (low-noise loss rate) | W₁ (high-noise gain rate) | Internal edges per block |
|---|---|---|---|
| trigram T | 3 | 3 | 12 |
| palace B | 4 | 13/8 | 8 |
| generation G | 6 | 0 | 0 |

**Extremality among balanced eight-valued labels** (blocks of size 8):

- **Low noise.** β ≥ 3 by the edge-isoperimetric inequality for the hypercube: an 8-set has at least 24 boundary edges. This is classical (Harper; Bernstein; Hart); the equality case is cited, not checked here. Partitions into three-dimensional coordinate subcubes attain β = 3.
- **High noise.** ‖s(A)‖² ≤ 192 for every 8-subset of {0,1}⁶, so W₁ ≤ 3.
  - Proof: the maximizer's own s(A) is an even integer vector, and A must be a top-8 set for it. A search over the 210 sorted nonnegative candidate directions in {0,2,4,6,8}⁶ (up to signed coordinate permutations) gives the maximum 192. It is attained only by directions proportional to (0,0,0,1,1,1), whose top-8 set is a coordinate 3-subcube.
  - Hence W₁ = 3 exactly when every block is a coordinate 3-subcube.
- **Worst case.** G attains the worst possible value at both ends: every flip changes it (β = 6, the maximum) and it has no level-1 weight (W₁ = 0, the minimum).

**Reading.**

- The trigram decomposition is the most change-robust three-bit description of a hexagram at both noise extremes.
- The generation label, i.e. the pattern of which line pairs (1,4), (2,5), (3,6) differ, is among the least robust possible.
- The palace label lies strictly between at every noise level.

This explains INV-0003's numerical gap: it is an isoperimetric phenomenon at low noise and a level-1 Fourier phenomenon at high noise.

### R6. Conjecture: the trigram is the most informative balanced three-bit label at every noise level

**Statement.** For every 0 < p < 1/2, partitions into coordinate 3-subcubes maximize I(λ(X);Y) among all balanced eight-valued labels on six lines.

This is the case (n = 6, k = 3) of a conjecture that arXiv:2609.26444 states for 2 ≤ k ≤ 7, according to its abstract page. The same abstract reports a coding-based counterexample for k ≥ 8. The present statement is therefore not new as a conjecture. What is reported here is evidence for this instance:

- endpoint optimality (R5);
- the trigram is a strict local maximum under every single swap of two hexagrams between blocks, at p = 1/10, at p = 1/4 (coins) and under yarrow-standard. The best swap changes I by −0.0196, −0.0107 and −0.0118 bits respectively;
- simulated annealing from the palace partition and three random partitions (60,000 swaps each) never exceeded the trigram value. Each target's best run ended exactly at the trigram value with all blocks affine.

Not ruled out: an unbalanced eight-valued label, or a non-affine balanced label far from every searched start, exceeding the trigram at intermediate p.

### R7. Conjecture: single lines stay optimal under the yarrow asymmetry

The hypotheses of family 119 fail for the yarrow models: the channel is asymmetric, and the input is biased for questions about the changed hexagram or under yarrow-uniform. Even so:

- **Exhaustive.** For n = 1, 2, 3, 4 lines, all nonconstant Boolean functions (up to 65,534) were scanned for coins and the three yarrow models, in both directions (question about primary; question about changed). In every case the maximum is attained only by the 2n signed single-line functions. At n = 4 the best non-coordinate function trails by 0.008–0.028 bits.
- **Local search.** At six lines, 65 seeded hill-climbs per model and direction (yarrow-standard and yarrow-uniform) from random, biased and structured starts all ended at a single line.

Conjecture: the Courtade–Kumar conclusion holds for these binary asymmetric product channels. No literature addressing asymmetric channels was found in a short search. Novelty is unknown.

Not ruled out: a non-coordinate optimum at n = 5 or 6 that escapes local search; failure for more extreme asymmetric channels than those tested. The tested channels include two artificial ones, (a, b) = (0.5, 0) and (0.8, 0), probed separately at n ≤ 4; that probe is not part of the frozen run.

### R8. Independent recomputation of INV-0003 (cross-family, context-exposed)

My own code, not importing INV-0003's code, reproduces every finite statement of INV-0003 and its supplement:

- **L1.** The reduction discrepancy is below 2 × 10⁻¹⁵ across all 254 nonconstant functions of G. Exactly 6 functions attain 1 − h₂(q) at p = 1/8 and 1/4.
- **L2.** All four values agree to at least 12 significant digits, and B and G are independent.
- **L3.** The matching-count formula agrees by direct counting for k = 1, …, 5.
- **L4.** Agrees.
- **L5.** Exact uniform one-sweep marginals for all 64 starting labels; log₂(2¹⁹²/64!) = −103.99514394…; at least 10 physical shuffles are needed.
- **L6.** Agrees.
- **Supplement.** The majorization counterexample is reproduced exactly.

I found no error. Two of INV-0003's framings are superseded by R1 and R4: the "artificial channel", and the open all-noise question. This is not a protocol verification: there was no isolation and no two-phase separation. ASN-0013 remains the route to `verified`.

## 4. Source-dependent observations (adjudicator notes; not findings)

These come from general knowledge, not checked against cited sources; they belong to ASN-0007/ASN-0008.

- **G and correspondence.** G records, for each traditional "correspondence" (應) pair of positions (1,4), (2,5), (3,6), whether the two lines are of opposite kind. Opposite kind is the usual criterion for a responding pair. On this reading, R5 says that the correspondence pattern is maximally fragile under line change. C-0019 already links G to the generation mnemonic.
- **Line 6 in the palace system.** Every word of D leaves line 6 unchanged. This matches the commonly stated rule that the top line of a palace hexagram is never altered. It is also what gives B its line-6 coordinate, used in R4.
- **Coins and palaces in practice.** The three-coin method and the palace/generation system are commonly described as used together in one later divinatory practice, with changed lines read relative to the primary hexagram's palace. If that is right, R3–R5 describe information budgets of a procedure actually paired with these labels. Citation needed.

## 5. Import contract (standards §14)

| Field | Content |
|---|---|
| Source and revision | openai/math @ 4eaee87548250b2682affda7d05d947c05554bae, family 119, *Sharp binary-information contraction on the discrete cube*, `build/main.tex` (frozen copy in `investigations/library/`) |
| Exact statement | Corollary `main:ck`: for f: {−1,1}ⁿ → {−1,1} with mean m, I(f(X);Y) ≤ ψ(\|ρ\| r_m) ≤ ψ(\|ρ\|), r_m = ψ⁻¹(H(m)), X uniform, Y_i = X_i Z_i with independent signs E Z_i = ρ; signed coordinates attain at m = 0 |
| Review level | theorem statement and surrounding definitions read; proof not audited; Lean not run |
| Hypotheses checked | uniform input (R1), independent identical symmetric noise (R1), deterministic Boolean output (R3 questions) |
| Missing hypotheses | asymmetric noise and biased input (yarrow models): **not covered**; R7 is a conjecture with evidence |
| Elementary baseline | exhaustive check of all Boolean functions is impossible at n = 6 (2⁶⁴); exhaustive at n ≤ 4 agrees |
| New deliverable | R3, the exact coin-oracle question bound with bias refinement; the use of the theorem is limited to R3 and the k = 1 parts of R6–R7. R4 and R5 use only classical tools and do not depend on the import |
| Independent support | arXiv:2609.26444 claims a separate proof of the same statement (abstract only read). It and family 119 are not checked here |
| Rejection / reopening | reopen R3 if either proof is withdrawn; reopen R7 if an asymmetric-channel version appears in either line of work |

## 6. Attempt map and negative results

| Attempt | Scope | Outcome | Not ruled out / next |
|---|---|---|---|
| Whole-corpus screen | 373 family descriptions read in full, 721 abstracts keyword-swept | one clean transfer (119); details in `adjudication.md` | individual manuscripts behind families were not read beyond abstracts |
| Asymmetric probe (pre-run) | n ≤ 3 then n ≤ 4, channels (1/4,1/4), (3/8,1/8), (0.5,0), (0.8,0), (0.9,0.05), (0.45,0.02) | single lines always optimal | n = 5 exhaustive (about 2³¹ functions after output-complement symmetry) not run |
| Partition search, first try | short annealing, 15,000 swaps | did not reach the trigram (non-converged) | superseded by longer runs, the palace start and the exact swap-neighborhood check |
| All-p proof, T vs B near p = 1/2 | χ² bound | needs ρ ≤ 0.0305; the grid had to reach 0.4849 | a sharper high-noise bound would shorten the grid |

## 7. Novelty search actually done

- Web searches (2026-10-31) for: the Courtade–Kumar problem on asymmetric or Z channels; exact yarrow probabilities under split models; information-theoretic analysis of the primary and changed hexagrams.
- Results: arXiv:2609.26444 (relevant to R3 and R6). General sources give the standard yarrow probabilities, including the observation that old yang is three times as likely as old yin under the standard model. No information-theoretic treatment of the two hexagrams was found.
- Not searched: Chinese-language scholarship; the probability and statistics literature on yarrow modelling.
- Novelty of R1, R2, R4, R5 and R7 as applications is therefore **unknown**. R4's proof technique is classical, and Courtade and Kumar used an edge-isoperimetric argument for their low-noise case.

## 8. Local registry

| Local ID | Contribution | Evidence | Depends on | Next |
|---|---|---|---|---|
| R1 | Procedures → line channels; coins = BSC(1/4) with independent change mask; yarrow = asymmetric | exact computation | DEF-001; model definitions | cited procedure descriptions (ASN-0007) |
| R2 | Yarrow probabilities depend on the split model | exact rationals | R1 models | cite the procedure; choose split models from sources or experiments |
| R3 | Coin-oracle one-bit bound with bias refinement | conditional transfer | family 119; R1 | different-family verification of the transfer |
| R4 | T > B > G for all 0 < p < 1/2 | computer-assisted proof | C-0016 (structure of D), R1 | isolated verification |
| R5 | Endpoint expansions; subcube optimality and G worst-case at both ends | proof; exact computation; cited edge-isoperimetry | — | verification; literature check |
| R6 | Conjecture: trigram optimal among balanced 3-bit labels for every p | endpoint proofs, swap check, annealing | arXiv:2609.26444 context | proof attempt or counterexample search (specialist) |
| R7 | Conjecture: single lines optimal under yarrow channels | exhaustive n ≤ 4, local search n = 6 | — | n = 5 exhaustive; proof attempt |
| R8 | INV-0003 finite claims recomputed; no error | own code | INV-0003 | ASN-0013 for protocol verification |

## 9. Reproducibility

- Code: `compute/experiments/INV-0004/divination_information.py` (Python 3.9.6, standard library only), run with `--nmax 4 --starts 60 --iters 60000 --restarts 4 --seed 20261031`.
- Output: `results.json` in this folder. The script's SHA-256 is recorded inside it. The run took 34 s.
- Exact rationals are used for every probability, grid mass and integer optimum. Information values use binary64 logarithms. Local searches are seeded.
- Reproduce into a fresh path; never overwrite the frozen output.

---

## Supplied material: `investigations/INV-0004-divination-information-bounds/results.json`

{
 "ck_table": {
  "note": "Bounds are conditional on Corollary main:ck of external family 119 (uniform input, independent symmetric noise). They do not apply to the yarrow columns.",
  "p": 0.25,
  "rho": 0.5,
  "rows": [
   {
    "ck_refined_bits": 0.1887218755408672,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.18872187554086534,
    "mean_pm1": 0.0,
    "observable": "line 1 is yang",
    "ones": 32,
    "yarrow_changed_question_I_bits": 0.205434779862684,
    "yarrow_primary_question_I_bits": 0.20543477986268402
   },
   {
    "ck_refined_bits": 0.1887218755408672,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.18872187554086534,
    "mean_pm1": 0.0,
    "observable": "line 6 is yang",
    "ones": 32,
    "yarrow_changed_question_I_bits": 0.20543477986268296,
    "yarrow_primary_question_I_bits": 0.20543477986268377
   },
   {
    "ck_refined_bits": 0.12111998121820448,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.01970894282478915,
    "mean_pm1": -0.75,
    "observable": "lower and upper trigram equal",
    "ones": 8,
    "yarrow_changed_question_I_bits": 0.030924381515235293,
    "yarrow_primary_question_I_bits": 0.022148227211161484
   },
   {
    "ck_refined_bits": 0.12111998121820448,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.05551436263614194,
    "mean_pm1": -0.75,
    "observable": "palace label equals 000",
    "ones": 8,
    "yarrow_changed_question_I_bits": 0.07467959651755716,
    "yarrow_primary_question_I_bits": 0.06310635451314288
   },
   {
    "ck_refined_bits": 0.12111998121820448,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.01970894282478899,
    "mean_pm1": -0.75,
    "observable": "generation label equals 111 (all three line pairs differ)",
    "ones": 8,
    "yarrow_changed_question_I_bits": 0.03016664910464943,
    "yarrow_primary_question_I_bits": 0.023141720470275663
   },
   {
    "ck_refined_bits": 0.18194613768436071,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.1271780016155823,
    "mean_pm1": -0.3125,
    "observable": "at least four yang lines",
    "ones": 22,
    "yarrow_changed_question_I_bits": 0.10059308816628802,
    "yarrow_primary_question_I_bits": 0.13439270878437887
   },
   {
    "ck_refined_bits": 0.17810214124973847,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.013949650209017268,
    "mean_pm1": -0.375,
    "observable": "exactly three yang lines",
    "ones": 20,
    "yarrow_changed_question_I_bits": 0.04009102848213705,
    "yarrow_primary_question_I_bits": 0.016252276945667145
   },
   {
    "ck_refined_bits": 0.1887218755408672,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.14741284439799268,
    "mean_pm1": 0.0,
    "observable": "lower trigram has at least two yang lines",
    "ones": 32,
    "yarrow_changed_question_I_bits": 0.15282601601523155,
    "yarrow_primary_question_I_bits": 0.15974635396732664
   },
   {
    "ck_refined_bits": 0.12111998121820448,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.019708942824789136,
    "mean_pm1": -0.75,
    "observable": "reading the figure top-to-bottom gives the same figure",
    "ones": 8,
    "yarrow_changed_question_I_bits": 0.03092438151523539,
    "yarrow_primary_question_I_bits": 0.02214822721116147
   },
   {
    "ck_refined_bits": 0.1887218755408672,
    "ck_universal_bits": 0.1887218755408672,
    "coins_I_bits": 0.00017611740112635776,
    "mean_pm1": 0.0,
    "observable": "odd number of yang lines",
    "ones": 32,
    "yarrow_changed_question_I_bits": 0.0006738176090717411,
    "yarrow_primary_question_I_bits": 0.00025945651924112875
   }
  ]
 },
 "dictator_n6": {
  "yarrow-standard|changed-question": {
   "best_coordinate_I_bits": 0.20543477986268402,
   "best_start": "all-yang-or-1",
   "local_search_best_I_bits": 0.20543477986268402,
   "local_search_best_is_signed_coordinate": true,
   "starts": 65
  },
  "yarrow-standard|primary-question": {
   "best_coordinate_I_bits": 0.20543477986268402,
   "best_start": "random-0",
   "local_search_best_I_bits": 0.20543477986268402,
   "local_search_best_is_signed_coordinate": true,
   "starts": 65
  },
  "yarrow-uniform|changed-question": {
   "best_coordinate_I_bits": 0.18783543159742247,
   "best_start": "random-54",
   "local_search_best_I_bits": 0.187835431597423,
   "local_search_best_is_signed_coordinate": true,
   "starts": 65
  },
  "yarrow-uniform|primary-question": {
   "best_coordinate_I_bits": 0.18783543159742186,
   "best_start": "random-31",
   "local_search_best_I_bits": 0.18783543159742203,
   "local_search_best_is_signed_coordinate": true,
   "starts": 65
  }
 },
 "dictator_scans": {
  "coins|n=1|changed-question": {
   "best_dictator_I_bits": 0.1887218755408671,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.1887218755408671,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "coins|n=1|primary-question": {
   "best_dictator_I_bits": 0.1887218755408671,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.1887218755408671,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "coins|n=2|changed-question": {
   "best_dictator_I_bits": 0.18872187554086708,
   "best_non_coordinate_I_bits": 0.13167462567018212,
   "best_non_coordinate_truth_table": "1110",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.05704724987068496,
   "max_I_bits": 0.18872187554086708,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "coins|n=2|primary-question": {
   "best_dictator_I_bits": 0.18872187554086708,
   "best_non_coordinate_I_bits": 0.13167462567018212,
   "best_non_coordinate_truth_table": "1110",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.05704724987068496,
   "max_I_bits": 0.18872187554086708,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "coins|n=3|changed-question": {
   "best_dictator_I_bits": 0.18872187554086728,
   "best_non_coordinate_I_bits": 0.14741284439799343,
   "best_non_coordinate_truth_table": "11010100",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.04130903114287385,
   "max_I_bits": 0.18872187554086728,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "coins|n=3|primary-question": {
   "best_dictator_I_bits": 0.18872187554086728,
   "best_non_coordinate_I_bits": 0.14741284439799343,
   "best_non_coordinate_truth_table": "11010100",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.04130903114287385,
   "max_I_bits": 0.18872187554086728,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "coins|n=4|changed-question": {
   "best_dictator_I_bits": 0.18872187554086745,
   "best_non_coordinate_I_bits": 0.16059141716989944,
   "best_non_coordinate_truth_table": "1111100011110000",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.028130458370968003,
   "max_I_bits": 0.18872187554086745,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "coins|n=4|primary-question": {
   "best_dictator_I_bits": 0.18872187554086745,
   "best_non_coordinate_I_bits": 0.16059141716989944,
   "best_non_coordinate_truth_table": "1111100011110000",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.028130458370968003,
   "max_I_bits": 0.18872187554086745,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "yarrow-binomial|n=1|changed-question": {
   "best_dictator_I_bits": 0.2054323548363628,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.2054323548363628,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "yarrow-binomial|n=1|primary-question": {
   "best_dictator_I_bits": 0.20543235483636285,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.20543235483636285,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "yarrow-binomial|n=2|changed-question": {
   "best_dictator_I_bits": 0.20543235483636285,
   "best_non_coordinate_I_bits": 0.1658419767160236,
   "best_non_coordinate_truth_table": "1110",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.03959037812033925,
   "max_I_bits": 0.20543235483636285,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "yarrow-binomial|n=2|primary-question": {
   "best_dictator_I_bits": 0.20543235483636296,
   "best_non_coordinate_I_bits": 0.1514022140516963,
   "best_non_coordinate_truth_table": "1110",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.05403014078466667,
   "max_I_bits": 0.20543235483636296,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "yarrow-binomial|n=3|changed-question": {
   "best_dictator_I_bits": 0.20543235483636296,
   "best_non_coordinate_I_bits": 0.17632836355395337,
   "best_non_coordinate_truth_table": "10001111",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.02910399128240959,
   "max_I_bits": 0.20543235483636296,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "yarrow-binomial|n=3|primary-question": {
   "best_dictator_I_bits": 0.20543235483636316,
   "best_non_coordinate_I_bits": 0.16462784462074598,
   "best_non_coordinate_truth_table": "11101010",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.04080451021561718,
   "max_I_bits": 0.20543235483636316,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "yarrow-binomial|n=4|changed-question": {
   "best_dictator_I_bits": 0.20543235483640915,
   "best_non_coordinate_I_bits": 0.1920889176187297,
   "best_non_coordinate_truth_table": "1011001100110011",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.013343437217679444,
   "max_I_bits": 0.20543235483640915,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "yarrow-binomial|n=4|primary-question": {
   "best_dictator_I_bits": 0.20543235483637323,
   "best_non_coordinate_I_bits": 0.17784953840196233,
   "best_non_coordinate_truth_table": "0001010101010101",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.027582816434410906,
   "max_I_bits": 0.20543235483637323,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "yarrow-standard|n=1|changed-question": {
   "best_dictator_I_bits": 0.20543477986268438,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.20543477986268438,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "yarrow-standard|n=1|primary-question": {
   "best_dictator_I_bits": 0.2054347798626843,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.2054347798626843,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "yarrow-standard|n=2|changed-question": {
   "best_dictator_I_bits": 0.20543477986268424,
   "best_non_coordinate_I_bits": 0.16584369567857501,
   "best_non_coordinate_truth_table": "1110",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.039591084184109226,
   "max_I_bits": 0.20543477986268424,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "yarrow-standard|n=2|primary-question": {
   "best_dictator_I_bits": 0.20543477986268432,
   "best_non_coordinate_I_bits": 0.15140362049566777,
   "best_non_coordinate_truth_table": "0001",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.05403115936701655,
   "max_I_bits": 0.20543477986268432,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "yarrow-standard|n=3|changed-question": {
   "best_dictator_I_bits": 0.20543477986268444,
   "best_non_coordinate_I_bits": 0.17633039355407432,
   "best_non_coordinate_truth_table": "10110011",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.02910438630861012,
   "max_I_bits": 0.20543477986268444,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "yarrow-standard|n=3|primary-question": {
   "best_dictator_I_bits": 0.20543477986268432,
   "best_non_coordinate_I_bits": 0.1646296065524552,
   "best_non_coordinate_truth_table": "00010101",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.04080517331022912,
   "max_I_bits": 0.20543477986268432,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "yarrow-standard|n=4|changed-question": {
   "best_dictator_I_bits": 0.20543477986268466,
   "best_non_coordinate_I_bits": 0.19209112123696664,
   "best_non_coordinate_truth_table": "1000000011111111",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.013343658625718013,
   "max_I_bits": 0.20543477986268466,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "yarrow-standard|n=4|primary-question": {
   "best_dictator_I_bits": 0.20543477986268446,
   "best_non_coordinate_I_bits": 0.1778514650811696,
   "best_non_coordinate_truth_table": "1111111110000000",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.02758331478151485,
   "max_I_bits": 0.20543477986268446,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "yarrow-uniform|n=1|changed-question": {
   "best_dictator_I_bits": 0.18783543159742166,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.18783543159742166,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "yarrow-uniform|n=1|primary-question": {
   "best_dictator_I_bits": 0.18783543159742164,
   "best_non_coordinate_I_bits": null,
   "best_non_coordinate_truth_table": null,
   "functions_attaining_max": 2,
   "functions_scanned": 2,
   "gap_bits": null,
   "max_I_bits": 0.18783543159742164,
   "max_attained_only_by_signed_coordinates": true,
   "n": 1
  },
  "yarrow-uniform|n=2|changed-question": {
   "best_dictator_I_bits": 0.1878354315974217,
   "best_non_coordinate_I_bits": 0.15800507664360644,
   "best_non_coordinate_truth_table": "0001",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.029830354953815252,
   "max_I_bits": 0.1878354315974217,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "yarrow-uniform|n=2|primary-question": {
   "best_dictator_I_bits": 0.18783543159742166,
   "best_non_coordinate_I_bits": 0.14037198577522939,
   "best_non_coordinate_truth_table": "0001",
   "functions_attaining_max": 4,
   "functions_scanned": 14,
   "gap_bits": 0.04746344582219228,
   "max_I_bits": 0.18783543159742166,
   "max_attained_only_by_signed_coordinates": true,
   "n": 2
  },
  "yarrow-uniform|n=3|changed-question": {
   "best_dictator_I_bits": 0.18783543159742253,
   "best_non_coordinate_I_bits": 0.16680889414215583,
   "best_non_coordinate_truth_table": "11010101",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.021026537455266697,
   "max_I_bits": 0.18783543159742253,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "yarrow-uniform|n=3|primary-question": {
   "best_dictator_I_bits": 0.18783543159742194,
   "best_non_coordinate_I_bits": 0.15084618627700927,
   "best_non_coordinate_truth_table": "11111000",
   "functions_attaining_max": 6,
   "functions_scanned": 254,
   "gap_bits": 0.03698924532041267,
   "max_I_bits": 0.18783543159742194,
   "max_attained_only_by_signed_coordinates": true,
   "n": 3
  },
  "yarrow-uniform|n=4|changed-question": {
   "best_dictator_I_bits": 0.18783543159748195,
   "best_non_coordinate_I_bits": 0.17977500135896568,
   "best_non_coordinate_truth_table": "0100110011001100",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.00806043023851627,
   "max_I_bits": 0.18783543159748195,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  },
  "yarrow-uniform|n=4|primary-question": {
   "best_dictator_I_bits": 0.1878354315974335,
   "best_non_coordinate_I_bits": 0.16280819040625805,
   "best_non_coordinate_truth_table": "1110101010101010",
   "functions_attaining_max": 8,
   "functions_scanned": 65534,
   "gap_bits": 0.025027241191175442,
   "max_I_bits": 0.1878354315974335,
   "max_attained_only_by_signed_coordinates": true,
   "n": 4
  }
 },
 "inv0003_check": {
  "L1 p=1/4": {
   "bound_1_minus_h_q": 0.04556599707503495,
   "functions_attaining": 6,
   "max_I": 0.045565997075036085,
   "max_abs_reduction_discrepancy": 1.033895191682177e-15
  },
  "L1 p=1/8": {
   "bound_1_minus_h_q": 0.24212153746160459,
   "functions_attaining": 6,
   "max_I": 0.2421215374616056,
   "max_abs_reduction_discrepancy": 1.5959455978986625e-15
  },
  "L2 independence (all 64 pairs occur once)": true,
  "L2 p=1/4": {
   "B": 0.37862105517587913,
   "G": 0.13669799122510595,
   "G_formula": 0.13669799122510484
  },
  "L2 p=1/8": {
   "B": 1.1035766947342796,
   "G": 0.7263646123848208,
   "G_formula": 0.7263646123848138
  },
  "L3": {
   "k=1": {
    "count": 1,
    "formula_agrees": true
   },
   "k=2": {
    "count": 4,
    "formula_agrees": true
   },
   "k=3": {
    "count": 4096,
    "formula_agrees": true
   },
   "k=4": {
    "count": "72057594037927936",
    "formula_agrees": true
   },
   "k=5": {
    "count": "1766847064778384329583297500742918515827483896875618958121606201292619776",
    "formula_agrees": true
   }
  },
  "L4": {
   "extreme_event_allocation": "1/3",
   "extreme_event_uniform_table": "2/3",
   "multiplicities": [
    1,
    4,
    1
   ]
  },
  "L5": {
   "log2_64_factorial": 295.99514394172405,
   "log2_support_over_64_factorial": -103.99514394172405,
   "min_physical_shuffles_for_tv_quarter": 10,
   "one_sweep_marginals_uniform": true
  },
  "L6": {
   "all_nonzero_characters_balanced": true
  },
  "supplement": {
   "B_majorizes_G_fails": true,
   "sorted_B": [
    "301/512",
    "49/512",
    "49/512",
    "49/512",
    "43/512",
    "7/512",
    "7/512",
    "7/512"
   ],
   "sorted_G": [
    "15625/32768",
    "4375/32768",
    "4375/32768",
    "4375/32768",
    "1225/32768",
    "1225/32768",
    "1225/32768",
    "343/32768"
   ],
   "top4_B": "7/8",
   "top4_G": "14375/16384"
  }
 },
 "labels": {
  "generation": {
   "C_abs_fourier": "7",
   "W1": "0",
   "block_sizes": [
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8
   ],
   "boundary_degree_distribution": {
    "6": 64
   },
   "boundary_edges": 192,
   "fourier_levels_W": [
    "0",
    "0",
    "3",
    "0",
    "3",
    "0",
    "1"
   ],
   "internal_edges_per_block": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
   ],
   "mean_boundary_degree_beta": "6",
   "values": {
    "coins": 0.13669799122510595,
    "coins-type BSC p=1/4": 0.13669799122510595,
    "coins-type BSC p=1/8": 0.7263646123848208,
    "yarrow-binomial": 0.1570119125609682,
    "yarrow-binomial (questions about changed hexagram)": 0.21350987813069622,
    "yarrow-standard": 0.15701525196075886,
    "yarrow-standard (questions about changed hexagram)": 0.21351294551121802,
    "yarrow-uniform": 0.12938750588609105,
    "yarrow-uniform (questions about changed hexagram)": 0.22873420312318912
   }
  },
  "max_level1_weight_8_sets": {
   "max_norm_sq": "192",
   "maximizing_directions": [
    [
     0,
     0,
     0,
     2,
     2,
     2
    ],
    [
     0,
     0,
     0,
     4,
     4,
     4
    ],
    [
     0,
     0,
     0,
     6,
     6,
     6
    ],
    [
     0,
     0,
     0,
     8,
     8,
     8
    ]
   ],
   "subcube_value": 192
  },
  "palace": {
   "C_abs_fourier": "15",
   "W1": "13/8",
   "block_sizes": [
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8
   ],
   "boundary_degree_distribution": {
    "3": 8,
    "4": 48,
    "5": 8
   },
   "boundary_edges": 128,
   "fourier_levels_W": [
    "0",
    "13/8",
    "5/2",
    "9/4",
    "1/2",
    "1/8",
    "0"
   ],
   "internal_edges_per_block": [
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8
   ],
   "mean_boundary_degree_beta": "4",
   "values": {
    "coins": 0.37862105517587913,
    "coins-type BSC p=1/4": 0.37862105517587913,
    "coins-type BSC p=1/8": 1.1035766947342796,
    "yarrow-binomial": 0.41590588717621174,
    "yarrow-binomial (questions about changed hexagram)": 0.4475431954899946,
    "yarrow-standard": 0.41591150034520113,
    "yarrow-standard (questions about changed hexagram)": 0.4475486716191166,
    "yarrow-uniform": 0.3726411703788705,
    "yarrow-uniform (questions about changed hexagram)": 0.42721552527649154
   }
  },
  "sweep_bsc": [
   {
    "generation": 2.5790516291879095,
    "p": 0.01,
    "palace": 2.690961895487824,
    "trigram": 2.757620592312265
   },
   {
    "generation": 2.2841636428975214,
    "p": 0.02,
    "palace": 2.464867290882254,
    "trigram": 2.5756783723745396
   },
   {
    "generation": 2.0392267238475226,
    "p": 0.03,
    "palace": 2.2713923910024008,
    "trigram": 2.4168244265052707
   },
   {
    "generation": 1.827593449462337,
    "p": 0.04,
    "palace": 2.0996670393490593,
    "trigram": 2.2731234327527616
   },
   {
    "generation": 1.6411723554381483,
    "p": 0.05,
    "palace": 1.9444597495338318,
    "trigram": 2.1408091286521307
   },
   {
    "generation": 1.47508721827381,
    "p": 0.06,
    "palace": 1.8026474829652923,
    "trigram": 2.017665242536573
   },
   {
    "generation": 1.3260407076712852,
    "p": 0.07,
    "palace": 1.672137628381849,
    "trigram": 1.9022290472993293
   },
   {
    "generation": 1.191633844653501,
    "p": 0.08,
    "palace": 1.5514210617949513,
    "trigram": 1.7934624293931807
   },
   {
    "generation": 1.070029951385561,
    "p": 0.09,
    "palace": 1.439352115940066,
    "trigram": 1.6905905488076876
   },
   {
    "generation": 0.9597688628151588,
    "p": 0.1,
    "palace": 1.3350272951980071,
    "trigram": 1.5930132192321578
   },
   {
    "generation": 0.859655568031819,
    "p": 0.11,
    "palace": 1.2377127913572772,
    "trigram": 1.5002521255064045
   },
   {
    "generation": 0.7686892697818588,
    "p": 0.12,
    "palace": 1.1467984404119365,
    "trigram": 1.4119174041379114
   },
   {
    "generation": 0.6860159845722364,
    "p": 0.13,
    "palace": 1.0617670447438867,
    "trigram": 1.3276854449160223
   },
   {
    "generation": 0.6108956331861402,
    "p": 0.14,
    "palace": 0.982173132232036,
    "trigram": 1.2472835650714347
   },
   {
    "generation": 0.5426784605169481,
    "p": 0.15,
    "palace": 0.9076277774367068,
    "trigram": 1.1704790858507983
   },
   {
    "generation": 0.4807876899358301,
    "p": 0.16,
    "palace": 0.8377874647734269,
    "trigram": 1.0970713360782876
   },
   {
    "generation": 0.42470647724361843,
    "p": 0.17,
    "palace": 0.772345732927783,
    "trigram": 1.0268856637673414
   },
   {
    "generation": 0.3739679108600473,
    "p": 0.18,
    "palace": 0.7110267853688881,
    "trigram": 0.9597688628151593
   },
   {
    "generation": 0.3281472213842904,
    "p": 0.19,
    "palace": 0.6535805237177925,
    "trigram": 0.8955856203483106
   },
   {
    "generation": 0.28685562682652765,
    "p": 0.2,
    "palace": 0.5997786322988934,
    "trigram": 0.8342157153379155
   },
   {
    "generation": 0.24973541102080654,
    "p": 0.21,
    "palace": 0.5494114536776413,
    "trigram": 0.775551780206182
   },
   {
    "generation": 0.21645594700816773,
    "p": 0.22,
    "palace": 0.5022854692997512,
    "trigram": 0.7194974911141014
   },
   {
    "generation": 0.18671045520474472,
    "p": 0.23,
    "palace": 0.45822125002400194,
    "trigram": 0.6659660893603911
   },
   {
    "generation": 0.16021334052919123,
    "p": 0.24,
    "palace": 0.4170517766055659,
    "trigram": 0.6148791618464271
   },
   {
    "generation": 0.13669799122510362,
    "p": 0.25,
    "palace": 0.3786210551758864,
    "trigram": 0.5661656266226167
   },
   {
    "generation": 0.11591494991813933,
    "p": 0.26,
    "palace": 0.3427829707606702,
    "trigram": 0.5197608825221542
   },
   {
    "generation": 0.09763038778598565,
    "p": 0.27,
    "palace": 0.30940033502771547,
    "trigram": 0.4756060913754627
   },
   {
    "generation": 0.08162482780213054,
    "p": 0.28,
    "palace": 0.2783440941885176,
    "trigram": 0.43364756831959905
   },
   {
    "generation": 0.06769207432644553,
    "p": 0.29,
    "palace": 0.2494926702642144,
    "trigram": 0.3938362609817818
   },
   {
    "generation": 0.05563831489904558,
    "p": 0.3,
    "palace": 0.2227314144341035,
    "trigram": 0.3561273023079172
   },
   {
    "generation": 0.0452813666672478,
    "p": 0.31,
    "palace": 0.19795215538204092,
    "trigram": 0.32047962486644455
   },
   {
    "generation": 0.03645004495876636,
    "p": 0.32,
    "palace": 0.17505282877435002,
    "trigram": 0.28685562682652765
   },
   {
    "generation": 0.028983635475810843,
    "p": 0.33,
    "palace": 0.1539371764808779,
    "trigram": 0.25522088166082524
   },
   {
    "generation": 0.022731454699139952,
    "p": 0.34,
    "palace": 0.13451450606185755,
    "trigram": 0.22554388508093037
   },
   {
    "generation": 0.01755248555732747,
    "p": 0.35,
    "palace": 0.11669950251642991,
    "trigram": 0.19779583387354638
   },
   {
    "generation": 0.013315077385277263,
    "p": 0.36,
    "palace": 0.10041208541934532,
    "trigram": 0.17195043223352346
   },
   {
    "generation": 0.00989670078063476,
    "p": 0.37,
    "palace": 0.08557730543435271,
    "trigram": 0.1479837219388025
   },
   {
    "generation": 0.007183749254201732,
    "p": 0.38,
    "palace": 0.07212527484376352,
    "trigram": 0.12587393332110075
   },
   {
    "generation": 0.0050713806281565965,
    "p": 0.39,
    "palace": 0.05999112721841682,
    "trigram": 0.10560135448474028
   },
   {
    "generation": 0.0034633920143760655,
    "p": 0.4,
    "palace": 0.04911500171079419,
    "trigram": 0.08714821663599093
   },
   {
    "generation": 0.002272122947224453,
    "p": 0.41,
    "palace": 0.03944204771666726,
    "trigram": 0.07049859372654632
   },
   {
    "generation": 0.0014183818817992133,
    "p": 0.42,
    "palace": 0.030922445849425273,
    "trigram": 0.05563831489904558
   },
   {
    "generation": 0.0008313918263946896,
    "p": 0.43,
    "palace": 0.02351144133097227,
    "trigram": 0.04255488846323496
   },
   {
    "generation": 0.0004487513751034733,
    "p": 0.44,
    "palace": 0.017169386050203794,
    "trigram": 0.03123743633383036
   },
   {
    "generation": 0.00021640786300913817,
    "p": 0.45,
    "palace": 0.011861785698687566,
    "trigram": 0.021676638036562945
   },
   {
    "generation": 8.863978844608766e-05,
    "p": 0.46,
    "palace": 0.007559348583317416,
    "trigram": 0.01386468353930903
   },
   {
    "generation": 2.804605218065248e-05,
    "p": 0.47,
    "palace": 0.004238032957304405,
    "trigram": 0.007795234296772424
   },
   {
    "generation": 5.53995132301921e-06,
    "p": 0.48,
    "palace": 0.0018790900170113645,
    "trigram": 0.0034633920143760655
   },
   {
    "generation": 3.462468147752418e-07,
    "p": 0.49,
    "palace": 0.00046910009088030336,
    "trigram": 0.0008656747415640709
   }
  ],
  "trigram": {
   "C_abs_fourier": "7",
   "W1": "3",
   "block_sizes": [
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8
   ],
   "boundary_degree_distribution": {
    "3": 64
   },
   "boundary_edges": 96,
   "fourier_levels_W": [
    "0",
    "3",
    "3",
    "1",
    "0",
    "0",
    "0"
   ],
   "internal_edges_per_block": [
    12,
    12,
    12,
    12,
    12,
    12,
    12,
    12
   ],
   "mean_boundary_degree_beta": "3",
   "values": {
    "coins": 0.5661656266226001,
    "coins-type BSC p=1/4": 0.5661656266226001,
    "coins-type BSC p=1/8": 1.3693066704012038,
    "yarrow-binomial": 0.6162970645090886,
    "yarrow-binomial (questions about changed hexagram)": 0.6162970645090883,
    "yarrow-standard": 0.6163043395880506,
    "yarrow-standard (questions about changed hexagram)": 0.616304339588052,
    "yarrow-uniform": 0.5635062947922651,
    "yarrow-uniform (questions about changed hexagram)": 0.5635062947922655
   }
  }
 },
 "ordering_proof": {
  "B_vs_G": {
   "proved": true,
   "regionA": {
    "L_threshold": 7.567276155442228,
    "holds": true,
    "p_max": 0.0009765625,
    "slope_positive": true
   },
   "regionB": {
    "all_hold": true,
    "at_interval": [
     0.0009765625,
     0.001171875
    ],
    "intervals": 30,
    "smallest_gap": 0.010224087915801185
   },
   "regionC": {
    "holds": true,
    "line6_is_function_of_B": true,
    "p_min": 0.23,
    "rho_max": 0.54
   }
  },
  "T_vs_B": {
   "covers": true,
   "proved": true,
   "regionA": {
    "L_threshold": 12.386315822284665,
    "c1": 8.045565997075032,
    "holds": true,
    "p_max": 6.103515625e-05,
    "slope_positive": true
   },
   "regionB": {
    "all_hold": true,
    "at_interval": [
     0.48218083881676194,
     0.48468083881676194
    ],
    "intervals": 233,
    "p_top": 0.4849,
    "smallest_gap": 0.0005406728624741675
   },
   "regionC": {
    "C": 15.0,
    "W": [
     0.0,
     1.625,
     2.5,
     2.25,
     0.5,
     0.125,
     0.0
    ],
    "holds": true,
    "p_min": 0.48475000000000007,
    "rho_max": 0.03049999999999987
   }
  },
  "margin": 1e-10
 },
 "parameters": {
  "iters": 60000,
  "nmax": 4,
  "out": "investigations/INV-0004-divination-information-bounds/results.json",
  "restarts": 4,
  "seed": 20261031,
  "starts": 60
 },
 "partition_search": {
  "bsc p=1/10": {
   "best_blocks_affine": [
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true
   ],
   "best_found_I_bits": 1.5930132192321644,
   "best_minus_trigram": 1.0880185641326534e-14,
   "best_seed": 20261034,
   "iterations": 60000,
   "reference": {
    "generation": 0.959768862815166,
    "palace": 1.3350272951980087,
    "trigram": 1.5930132192321536
   },
   "restarts": 4,
   "runs": [
    {
     "best_I_bits": 1.5541102062046903,
     "seed": 20261031,
     "start": "palace"
    },
    {
     "best_I_bits": 1.5745721656625074,
     "seed": 20261032,
     "start": "random"
    },
    {
     "best_I_bits": 1.5613795749038435,
     "seed": 20261033,
     "start": "random"
    },
    {
     "best_I_bits": 1.5930132192321644,
     "seed": 20261034,
     "start": "random"
    }
   ],
   "trigram_best_single_swap_change": -0.019615323909698557
  },
  "coins": {
   "best_blocks_affine": [
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true
   ],
   "best_found_I_bits": 0.5661656266226036,
   "best_minus_trigram": 3.552713678800501e-15,
   "best_seed": 20261031,
   "iterations": 60000,
   "reference": {
    "generation": 0.13669799122510595,
    "palace": 0.37862105517587913,
    "trigram": 0.5661656266226001
   },
   "restarts": 4,
   "runs": [
    {
     "best_I_bits": 0.5661656266226036,
     "seed": 20261031,
     "start": "palace"
    },
    {
     "best_I_bits": 0.5348214613615041,
     "seed": 20261032,
     "start": "random"
    },
    {
     "best_I_bits": 0.5558383688368802,
     "seed": 20261033,
     "start": "random"
    },
    {
     "best_I_bits": 0.5432670257678988,
     "seed": 20261034,
     "start": "random"
    }
   ],
   "trigram_best_single_swap_change": -0.01070804401252623
  },
  "yarrow-standard": {
   "best_blocks_affine": [
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true
   ],
   "best_found_I_bits": 0.6163043395880529,
   "best_minus_trigram": 2.220446049250313e-15,
   "best_seed": 20261033,
   "iterations": 60000,
   "reference": {
    "generation": 0.15701525196075886,
    "palace": 0.41591150034520113,
    "trigram": 0.6163043395880506
   },
   "restarts": 4,
   "runs": [
    {
     "best_I_bits": 0.5963453374606078,
     "seed": 20261031,
     "start": "palace"
    },
    {
     "best_I_bits": 0.5925791811575806,
     "seed": 20261032,
     "start": "random"
    },
    {
     "best_I_bits": 0.6163043395880529,
     "seed": 20261033,
     "start": "random"
    },
    {
     "best_I_bits": 0.5944206523138164,
     "seed": 20261034,
     "start": "random"
    }
   ],
   "trigram_best_single_swap_change": -0.011787691085459406
  }
 },
 "procedures": {
  "coins": {
   "change_given_yang": "1/4",
   "change_given_yin": "1/4",
   "change_probability": "1/4",
   "changed_yang": "1/2",
   "line_values": {
    "6": "1/8",
    "7": "3/8",
    "8": "3/8",
    "9": "1/8"
   },
   "line_values_float": {
    "6": 0.125,
    "7": 0.375,
    "8": 0.375,
    "9": 0.125
   },
   "per_line": {
    "H_line_value": 1.811278124459133,
    "I_primary_changed": 0.18872187554086706,
    "I_primary_changemask": 0.0
   },
   "primary_uniform": true,
   "primary_yang": "1/2",
   "six_lines": {
    "H_line_value": 10.867668746754799,
    "I_primary_changed": 1.1323312532452023,
    "I_primary_changemask": 0.0
   },
   "symmetric_channel": true
  },
  "yarrow-binomial": {
   "change_given_yang": "672546119820069660013155951085376758638085499422329499440/1793450157430030556091891376697427409870758084137659094383",
   "change_given_yin": "896743396694730168916023097412452746198907847734121642757/7173860472608645497839307165476334029060261392731058158733",
   "change_probability": "2046928250312683139274043897222166015559741401/8187684238921615588656719698273659184522152045",
   "changed_yang": "2505425154063850132420107225086895085972032171007/6681150341876744322517708407148603385170873773495",
   "line_values": {
    "6": "989025002936669647033541284478551/15824142799565753324482534551859395",
    "7": "4483616150439843584314941702448202604930690338861318379772/14347661102328767722206872672266043668543293729281694536265",
    "8": "2923010419512598658183534967828270164639513804408/6681150341876744322517708407148603385170873773495",
    "9": "810195516184874144216162224198772672/4321045929146407604973774060149329933"
   },
   "line_values_float": {
    "6": 0.06250101604011123,
    "7": 0.3124980523628418,
    "8": 0.4375010694178633,
    "9": 0.18749986217918369
   },
   "per_line": {
    "H_line_value": 1.7490009615184108,
    "I_primary_changed": 0.2054323548363628,
    "I_primary_changemask": 0.06227855486985567
   },
   "primary_uniform": false,
   "primary_yang": "1024828661388588889195366500969958519926147476650090911076/2049665871761252531743838953180863381220470532754527790895",
   "six_lines": {
    "H_line_value": 10.494005769110466,
    "I_primary_changed": 1.2325941290181768,
    "I_primary_changemask": 0.37367132921913404
   },
   "symmetric_channel": false
  },
  "yarrow-standard": {
   "change_given_yang": "3/8",
   "change_given_yin": "1/8",
   "change_probability": "1/4",
   "changed_yang": "3/8",
   "line_values": {
    "6": "1/16",
    "7": "5/16",
    "8": "7/16",
    "9": "3/16"
   },
   "line_values_float": {
    "6": 0.0625,
    "7": 0.3125,
    "8": 0.4375,
    "9": 0.1875
   },
   "per_line": {
    "H_line_value": 1.7489992230622806,
    "I_primary_changed": 0.20543477986268455,
    "I_primary_changemask": 0.062278901396852326
   },
   "primary_uniform": true,
   "primary_yang": "1/2",
   "six_lines": {
    "H_line_value": 10.493995338373683,
    "I_primary_changed": 1.2326086791761073,
    "I_primary_changemask": 0.37367340838111396
   },
   "symmetric_channel": false
  },
  "yarrow-uniform": {
   "change_given_yang": "6463345/14565731",
   "change_given_yin": "1390620/14546989",
   "change_probability": "224399/831792",
   "changed_yang": "153113/469560",
   "line_values": {
    "6": "77/1612",
    "7": "4051193/14556360",
    "8": "424399/939120",
    "9": "5957/26832"
   },
   "line_values_float": {
    "6": 0.047766749379652605,
    "7": 0.27831085518632404,
    "8": 0.4519113638299685,
    "9": 0.22201103160405486
   },
   "per_line": {
    "H_line_value": 1.7230328535503356,
    "I_primary_changed": 0.18783543159742155,
    "I_primary_changemask": 0.11811243264103344
   },
   "primary_uniform": false,
   "primary_yang": "14565731/29112720",
   "six_lines": {
    "H_line_value": 10.338197121302013,
    "I_primary_changed": 1.1270125895845293,
    "I_primary_changemask": 0.7086745958462006
   },
   "symmetric_channel": false
  }
 },
 "python": "3.9.6",
 "script_sha256": "23a8458b4f072124939ea8de91a42cb41703756962d800801b683505096f1a47"
}

---

## Supplied material: `compute/experiments/INV-0004/divination_information.py`

#!/usr/bin/env python3
"""INV-0004: divination channels, Boolean information bounds, and robustness of hexagram labels.

Exploratory and computer-assisted computation for a full-context investigation (context-exposed;
not a verification). Python standard library only. Deterministic except for the seeded local
searches, whose seeds are recorded in the output.

Conventions: a hexagram is an integer x in [0, 64); bit i (i = 0..5) is line i+1 counted from the
bottom; yang = 1. Lower trigram L = lines 1-3 = x & 7, upper trigram U = lines 4-6 = x >> 3.

Models are stated explicitly; none is asserted to be a cited historical procedure:
  coins            three fair two-valued coins worth 2 or 3; line value = sum (6, 7, 8, 9)
  yarrow-standard  first change removes 5 or 9 stalks with probabilities 3/4, 1/4; second and
                   third changes remove 4 or 8 with probabilities 1/2, 1/2
  yarrow-uniform   49 stalks; each change splits n stalks with left heap L uniform on 1..n-1,
                   hangs one stalk from the right heap, counts both heaps by fours (remainder
                   1..4, an empty heap contributing 0)
  yarrow-binomial  as yarrow-uniform, but L ~ Binomial(n, 1/2) conditioned on 1 <= L <= n-1

Sections (keys of the JSON output):
  procedures      exact line-value laws and induced primary->changed channels
  ck_table        Courtade-Kumar bound (external family 119, conditional) vs exact values, coins
  dictator_scans  exhaustive search over all Boolean functions, n <= 4, all models, both directions
  dictator_n6     seeded local search over Boolean functions on six lines
  labels          trigram / palace / generation labels: exact structure, coefficients, values
  ordering_proof  computer-assisted proof of I(T;Y) > I(B;Y) > I(G;Y) for 0 < p < 1/2
  partition_search seeded local search over balanced eight-block labels
  inv0003_check   independent recomputation of INV-0003 L1-L6 and its supplement
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
import random
import sys
from fractions import Fraction as Fr

N = 64
LN2 = math.log(2.0)

# ----------------------------------------------------------------------------- encodings

def word(s):
    """Bottom-to-top 0/1 string -> integer."""
    return sum(int(c) << i for i, c in enumerate(s))


def popcount(x):
    return bin(x).count("1")


D_STRINGS = ["000000", "100000", "110000", "111000", "111100", "111110", "111010", "000010"]
D_WORDS = [word(s) for s in D_STRINGS]


def lower(x):
    return x & 7


def upper(x):
    return x >> 3


def gen_label(x):
    """G(x) = L xor U: which of the line pairs (1,4), (2,5), (3,6) differ."""
    return lower(x) ^ upper(x)


D_BY_G = {gen_label(d): d for d in D_WORDS}
assert len(D_BY_G) == 8


def palace_label(x):
    z = x ^ D_BY_G[gen_label(x)]
    assert lower(z) == upper(z)
    return lower(z)


def trigram_label(x):
    return lower(x)


LABELS = {
    "trigram": [trigram_label(x) for x in range(N)],
    "palace": [palace_label(x) for x in range(N)],
    "generation": [gen_label(x) for x in range(N)],
}

# ----------------------------------------------------------------------------- entropy helpers

def h2(p):
    """Binary entropy in bits (float argument)."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def plogp(q):
    """-q log2 q for an exact Fraction or float, accurate near 0 and 1."""
    if q <= 0 or q >= 1:
        return 0.0
    if isinstance(q, Fr) and q > Fr(1, 2):
        e = float(1 - q)
        return -(1.0 - e) * math.log1p(-e) / LN2
    qf = float(q)
    return -qf * math.log2(qf)


def entropy(probs):
    return sum(plogp(q) for q in probs)

# ----------------------------------------------------------------------------- procedures

def coin_values():
    dist = {}
    for c in itertools.product((2, 3), repeat=3):
        dist[sum(c)] = dist.get(sum(c), Fr(0)) + Fr(1, 8)
    return dist


def remainder(m):
    if m == 0:
        return 0
    r = m % 4
    return 4 if r == 0 else r


def split_law(n, kind):
    if kind == "uniform":
        return {L: Fr(1, n - 1) for L in range(1, n)}
    if kind == "binomial":
        w = {L: Fr(math.comb(n, L)) for L in range(1, n)}
        tot = sum(w.values())
        return {L: v / tot for L, v in w.items()}
    raise ValueError(kind)


def one_change(n, kind):
    out = {}
    for L, pr in split_law(n, kind).items():
        removed = 1 + remainder(L) + remainder(n - L - 1)
        out[removed] = out.get(removed, Fr(0)) + pr
    return out


def yarrow_values(kind):
    if kind == "standard":
        firsts = {5: Fr(3, 4), 9: Fr(1, 4)}
        later = {4: Fr(1, 2), 8: Fr(1, 2)}
        dist = {}
        for r1, a in firsts.items():
            for r2, b in later.items():
                for r3, c in later.items():
                    v = (49 - r1 - r2 - r3) // 4
                    dist[v] = dist.get(v, Fr(0)) + a * b * c
        return dist
    dist = {}

    def rec(n, depth, pr):
        if depth == 3:
            assert n % 4 == 0
            dist[n // 4] = dist.get(n // 4, Fr(0)) + pr
            return
        law = one_change(n, kind)
        allowed = {5, 9} if depth == 0 else {4, 8}
        assert set(law) <= allowed, (n, depth, law)
        for r, q in law.items():
            rec(n - r, depth + 1, pr * q)

    rec(49, 0, Fr(1))
    return dist


def line_channel(values):
    """From P(6..9): primary yang prob pi, a = P(change | yang), b = P(change | yin)."""
    p6, p7, p8, p9 = (values.get(v, Fr(0)) for v in (6, 7, 8, 9))
    assert p6 + p7 + p8 + p9 == 1
    pi = p7 + p9
    return {"P6": p6, "P7": p7, "P8": p8, "P9": p9, "pi": pi,
            "a": p9 / pi, "b": p6 / (1 - pi), "changed_yang": p7 + p6, "change": p6 + p9}


def per_line_info(ch):
    pi, a, b = ch["pi"], ch["a"], ch["b"]
    # joint law of (X, Y) for one line
    j = {(1, 1): pi * (1 - a), (1, 0): pi * a, (0, 1): (1 - pi) * b, (0, 0): (1 - pi) * (1 - b)}
    py1 = j[(1, 1)] + j[(0, 1)]
    i_xy = entropy([pi, 1 - pi]) + entropy([py1, 1 - py1]) - entropy(list(j.values()))
    # X versus change indicator E
    pe1 = pi * a + (1 - pi) * b
    je = [pi * a, pi * (1 - a), (1 - pi) * b, (1 - pi) * (1 - b)]
    i_xe = entropy([pi, 1 - pi]) + entropy([pe1, 1 - pe1]) - entropy(je)
    h_v = entropy([ch["P6"], ch["P7"], ch["P8"], ch["P9"]])
    return {"I_primary_changed": i_xy, "I_primary_changemask": i_xe, "H_line_value": h_v}


def product_joint(ch, n=6):
    """Joint law J[x][y] of primary and changed hexagram (n lines), exact Fractions."""
    pi, a, b = ch["pi"], ch["a"], ch["b"]
    one = {(1, 1): pi * (1 - a), (1, 0): pi * a, (0, 1): (1 - pi) * b, (0, 0): (1 - pi) * (1 - b)}
    size = 1 << n
    J = [[Fr(1)] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            w = Fr(1)
            for i in range(n):
                w *= one[((x >> i) & 1, (y >> i) & 1)]
            J[x][y] = w
    return J


def bsc_joint(p, n=6):
    size = 1 << n
    return [[(p ** popcount(x ^ y)) * ((1 - p) ** (n - popcount(x ^ y))) / size for y in range(size)]
            for x in range(size)]

# ----------------------------------------------------------------------------- information of functions

def boolean_info(J, f_set):
    """I(f(In); Out) in bits for the indicator of the input set f_set, joint J[in][out] (floats)."""
    n_out = len(J[0])
    pin = [sum(r) for r in J]
    pout = [sum(J[i][o] for i in range(len(J))) for o in range(n_out)]
    alpha = sum(pin[i] for i in f_set)
    tot = h2(alpha)
    for o in range(n_out):
        p1 = sum(J[i][o] for i in f_set)
        tot -= pout[o] * h2(p1 / pout[o])
    return tot


def label_info(J, labels):
    """I(lambda(In); Out) in bits; J may hold Fractions (exact masses) or floats."""
    n_in, n_out = len(J), len(J[0])
    K = max(labels) + 1
    rows = [[0] * n_out for _ in range(K)]
    for i in range(n_in):
        r = rows[labels[i]]
        Ji = J[i]
        for o in range(n_out):
            r[o] += Ji[o]
    pk = [sum(r) for r in rows]
    pout = [sum(rows[k][o] for k in range(K)) for o in range(n_out)]
    tot = 0.0
    for k in range(K):
        for o in range(n_out):
            m = rows[k][o]
            if m:
                tot += float(m) * math.log2(float(m) / (float(pk[k]) * float(pout[o])))
    return tot


def cond_entropy_label_bsc(labels, p, profile):
    """H(lambda(X) | Y) in bits for BSC(p), p an exact Fraction, using distance profiles."""
    w = [(p ** d) * ((1 - p) ** (6 - d)) for d in range(7)]
    tot = 0.0
    for y in range(N):
        prof = profile[y]
        for k in range(len(prof)):
            q = sum(prof[k][d] * w[d] for d in range(7))
            tot += plogp(q)
    return tot / N


def distance_profiles(labels):
    K = max(labels) + 1
    prof = []
    for y in range(N):
        rows = [[0] * 7 for _ in range(K)]
        for x in range(N):
            rows[labels[x]][popcount(x ^ y)] += 1
        prof.append(rows)
    return prof

# ----------------------------------------------------------------------------- section: procedures

def section_procedures():
    models = {"coins": coin_values(), "yarrow-standard": yarrow_values("standard"),
              "yarrow-uniform": yarrow_values("uniform"), "yarrow-binomial": yarrow_values("binomial")}
    out = {}
    channels = {}
    for name, vals in models.items():
        ch = line_channel(vals)
        channels[name] = ch
        info = per_line_info(ch)
        out[name] = {
            "line_values": {str(k): str(v) for k, v in sorted(vals.items())},
            "line_values_float": {str(k): float(v) for k, v in sorted(vals.items())},
            "primary_yang": str(ch["pi"]), "change_given_yang": str(ch["a"]),
            "change_given_yin": str(ch["b"]), "changed_yang": str(ch["changed_yang"]),
            "change_probability": str(ch["change"]),
            "per_line": info,
            "six_lines": {k: 6 * v for k, v in info.items()},
            "symmetric_channel": ch["a"] == ch["b"],
            "primary_uniform": ch["pi"] == Fr(1, 2),
        }
    return out, channels

# ----------------------------------------------------------------------------- section: CK table

def psi(r):
    """psi(r) = log 2 - H(r) in nats, H(r) the entropy of a sign of mean r."""
    def term(t):
        return 0.0 if t <= 0 else -t * math.log(t)
    return LN2 - (term((1 + r) / 2) + term((1 - r) / 2))


def psi_inv(v):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if psi(mid) < v:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ck_bounds(alpha, rho):
    m = 2 * alpha - 1
    H_m = LN2 - psi(m)                      # entropy of the output (nats)
    r_m = psi_inv(H_m)
    return psi(abs(rho) * r_m) / LN2, psi(abs(rho)) / LN2


OBSERVABLES = {
    "line 1 is yang": lambda x: x & 1,
    "line 6 is yang": lambda x: (x >> 5) & 1,
    "lower and upper trigram equal": lambda x: int(lower(x) == upper(x)),
    "palace label equals 000": lambda x: int(palace_label(x) == 0),
    "generation label equals 111 (all three line pairs differ)": lambda x: int(gen_label(x) == 7),
    "at least four yang lines": lambda x: int(popcount(x) >= 4),
    "exactly three yang lines": lambda x: int(popcount(x) == 3),
    "lower trigram has at least two yang lines": lambda x: int(popcount(lower(x)) >= 2),
    "reading the figure top-to-bottom gives the same figure": lambda x: int(all(((x >> i) & 1) == ((x >> (5 - i)) & 1) for i in range(3))),
    "odd number of yang lines": lambda x: popcount(x) & 1,
}


def section_ck(channels):
    Jc = product_joint(channels["coins"])
    Jy = product_joint(channels["yarrow-standard"])
    Jcf = [[float(v) for v in r] for r in Jc]
    Jyf = [[float(v) for v in r] for r in Jy]
    Jyb = [list(col) for col in zip(*Jyf)]   # questions about the changed hexagram
    rows = []
    rho = 0.5
    for name, fn in OBSERVABLES.items():
        f = [x for x in range(N) if fn(x)]
        alpha = len(f) / N
        refined, universal = ck_bounds(alpha, rho)
        fy = [y for y in range(N) if fn(y)]
        rows.append({
            "observable": name, "ones": len(f), "mean_pm1": 2 * alpha - 1,
            "coins_I_bits": boolean_info(Jcf, f), "ck_universal_bits": universal,
            "ck_refined_bits": refined,
            "yarrow_primary_question_I_bits": boolean_info(Jyf, f),
            "yarrow_changed_question_I_bits": boolean_info(Jyb, fy),
        })
    return {"rho": rho, "p": 0.25, "rows": rows,
            "note": "Bounds are conditional on Corollary main:ck of external family 119 (uniform input, "
                    "independent symmetric noise). They do not apply to the yarrow columns."}

# ----------------------------------------------------------------------------- section: dictator scans

def gray_scan(J):
    """Exhaustive scan over all nonconstant Boolean functions of the input of joint J (floats)."""
    n_in, n_out = len(J), len(J[0])
    pin = [sum(r) for r in J]
    pout = [sum(J[i][o] for i in range(n_in)) for o in range(n_out)]
    p1 = [0.0] * n_out
    alpha = 0.0
    member = [0] * n_in
    best = []
    total = 1 << n_in
    for i in range(1, total):
        bit = (i & -i).bit_length() - 1
        sgn = -1.0 if member[bit] else 1.0
        member[bit] ^= 1
        alpha += sgn * pin[bit]
        Jb = J[bit]
        for o in range(n_out):
            p1[o] += sgn * Jb[o]
        g = i ^ (i >> 1)
        if g == total - 1:
            continue
        val = h2(alpha)
        for o in range(n_out):
            po = pout[o]
            val -= po * h2(p1[o] / po)
        best.append((val, g))
    best.sort(reverse=True)
    return best


def dictator_sets(n):
    return [frozenset(x for x in range(1 << n) if (x >> j) & 1) for j in range(n)]


def scan_summary(J, n):
    res = gray_scan(J)
    dsets = dictator_sets(n)
    dict_masks = set()
    for s in dsets:
        m = sum(1 << x for x in s)
        dict_masks.add(m)
        dict_masks.add(((1 << (1 << n)) - 1) ^ m)
    best_val = res[0][0]
    dict_best = max(v for v, g in res if g in dict_masks)
    nondict = [(v, g) for v, g in res if g not in dict_masks]
    top_nd = nondict[0] if nondict else (None, None)
    attaining = [g for v, g in res if v >= best_val - 1e-12]
    return {"n": n, "functions_scanned": len(res), "max_I_bits": best_val,
            "best_dictator_I_bits": dict_best,
            "max_attained_only_by_signed_coordinates": all(g in dict_masks for g in attaining),
            "functions_attaining_max": len(attaining),
            "best_non_coordinate_I_bits": top_nd[0],
            "best_non_coordinate_truth_table": None if top_nd[1] is None else format(top_nd[1], "0%db" % (1 << n)),
            "gap_bits": None if top_nd[0] is None else best_val - top_nd[0]}


def section_dictator_scans(channels, nmax):
    out = {}
    for name, ch in channels.items():
        for n in range(1, nmax + 1):
            J = [[float(v) for v in r] for r in product_joint(ch, n)]
            Jb = [list(col) for col in zip(*J)]
            out["%s|n=%d|primary-question" % (name, n)] = scan_summary(J, n)
            out["%s|n=%d|changed-question" % (name, n)] = scan_summary(Jb, n)
    return out

# ----------------------------------------------------------------------------- section: n = 6 local search

def hill_climb_boolean(J, start, rng, max_rounds=200):
    n_in, n_out = len(J), len(J[0])
    pin = [sum(r) for r in J]
    pout = [sum(J[i][o] for i in range(n_in)) for o in range(n_out)]
    member = list(start)
    alpha = sum(pin[i] for i in range(n_in) if member[i])
    p1 = [sum(J[i][o] for i in range(n_in) if member[i]) for o in range(n_out)]

    def value(al, pp):
        if al <= 1e-15 or al >= 1 - 1e-15:
            return -1.0
        v = h2(al)
        for o in range(n_out):
            v -= pout[o] * h2(pp[o] / pout[o])
        return v

    cur = value(alpha, p1)
    for _ in range(max_rounds):
        improved = False
        order = list(range(n_in))
        rng.shuffle(order)
        for x in order:
            sgn = -1.0 if member[x] else 1.0
            na = alpha + sgn * pin[x]
            npp = [p1[o] + sgn * J[x][o] for o in range(n_out)]
            v = value(na, npp)
            if v > cur + 1e-13:
                member[x] ^= 1
                alpha, p1, cur = na, npp, v
                improved = True
        if not improved:
            break
    return cur, member


def section_dictator_n6(channels, starts, seed):
    rng = random.Random(seed)
    out = {}
    for name in ("yarrow-standard", "yarrow-uniform"):
        J = [[float(v) for v in r] for r in product_joint(channels[name])]
        for direction, M in (("primary-question", J), ("changed-question", [list(c) for c in zip(*J)])):
            dvals = [boolean_info(M, [x for x in range(N) if (x >> j) & 1]) for j in range(6)]
            structured = {
                "majority>=4": [int(popcount(x) >= 4) for x in range(N)],
                "majority>=3": [int(popcount(x) >= 3) for x in range(N)],
                "and(1,2)": [int((x & 3) == 3) for x in range(N)],
                "or(1,2)": [int((x & 3) != 0) for x in range(N)],
                "all-yang-or-1": [int(popcount(x) >= 5) for x in range(N)],
            }
            best = (-1.0, None, None)
            for label, st in structured.items():
                v, m = hill_climb_boolean(M, st, rng)
                if v > best[0]:
                    best = (v, label, m)
            for s in range(starts):
                dens = rng.choice([0.5, 0.25, 0.125, 0.75, rng.random()])
                st = [int(rng.random() < dens) for _ in range(N)]
                if sum(st) in (0, N):
                    continue
                v, m = hill_climb_boolean(M, st, rng)
                if v > best[0]:
                    best = (v, "random-%d" % s, m)
            is_coord = any(best[2] == [((x >> j) & 1) ^ c for x in range(N)] for j in range(6) for c in (0, 1))
            out["%s|%s" % (name, direction)] = {
                "best_coordinate_I_bits": max(dvals), "local_search_best_I_bits": best[0],
                "local_search_best_is_signed_coordinate": is_coord, "starts": starts + len(structured),
                "best_start": best[1]}
    return out

# ----------------------------------------------------------------------------- section: labels

def fourier_levels(labels):
    """W_j = sum_k sum_{|S|=j} fhat_k(S)^2 / pi_k (exact Fractions), and C = max_{k,y} sum_S |fhat_k(S)|/pi_k."""
    K = max(labels) + 1
    W = [Fr(0)] * 7
    absum = []
    for k in range(K):
        A = [x for x in range(N) if labels[x] == k]
        pi = Fr(len(A), N)
        tot_abs = Fr(0)
        for S in range(1, N):
            c = Fr(sum(1 if popcount(S & x) % 2 == 0 else -1 for x in A), N)
            W[popcount(S)] += c * c / pi
            tot_abs += abs(c) / pi
        absum.append(tot_abs)
    return W, max(absum)


def edge_structure(labels):
    K = max(labels) + 1
    internal = [0] * K
    boundary_degree = [0] * N
    for x in range(N):
        for i in range(6):
            y = x ^ (1 << i)
            if labels[y] == labels[x]:
                if x < y:
                    internal[labels[x]] += 1
            else:
                boundary_degree[x] += 1
    return internal, boundary_degree


def max_level1_weight(size):
    """max over subsets A of {0,1}^6 with |A| = size of ||s(A)||^2, s_i(A) = sum_{x in A} (-1)^{x_i}.

    Equals max over nonzero u of T(u)^2 / ||u||^2, T(u) = sum of the `size` largest <chi(x), u>; the
    maximizer's own s(A) is an integer vector, so up to signed permutations it suffices to range over
    sorted nonnegative integer vectors with entries congruent to size mod 2 in [0, size]."""
    chis = [[1 - 2 * ((x >> i) & 1) for i in range(6)] for x in range(N)]
    vals = [v for v in range(0, size + 1) if (v - size) % 2 == 0]
    best = Fr(-1)
    arg = []
    for u in itertools.combinations_with_replacement(vals, 6):
        nu = sum(c * c for c in u)
        if nu == 0:
            continue
        dots = sorted((sum(c * u[i] for i, c in enumerate(ch)) for ch in chis), reverse=True)
        t = sum(dots[:size])
        val = Fr(t * t, nu)
        if val > best:
            best, arg = val, [u]
        elif val == best:
            arg.append(u)
    return best, arg


def section_labels(channels):
    out = {}
    Jc = product_joint(channels["coins"])
    Jy = {m: product_joint(channels[m]) for m in ("yarrow-standard", "yarrow-uniform", "yarrow-binomial")}
    for name, lab in LABELS.items():
        internal, bdeg = edge_structure(lab)
        W, C = fourier_levels(lab)
        beta = Fr(sum(bdeg), N)
        sizes = [lab.count(k) for k in range(8)]
        entry = {
            "block_sizes": sizes, "internal_edges_per_block": internal,
            "boundary_edges": sum(bdeg) // 2, "mean_boundary_degree_beta": str(beta),
            "boundary_degree_distribution": {str(d): bdeg.count(d) for d in sorted(set(bdeg))},
            "fourier_levels_W": [str(w) for w in W], "W1": str(W[1]), "C_abs_fourier": str(C),
            "values": {},
        }
        for p in (Fr(1, 8), Fr(1, 4)):
            entry["values"]["coins-type BSC p=%s" % p] = label_info(bsc_joint(p), lab)
        entry["values"]["coins"] = label_info(Jc, lab)
        for m, J in Jy.items():
            entry["values"][m] = label_info(J, lab)
            entry["values"][m + " (questions about changed hexagram)"] = label_info([list(c) for c in zip(*J)], lab)
        out[name] = entry
    best192, arg = max_level1_weight(8)
    out["max_level1_weight_8_sets"] = {"max_norm_sq": str(best192), "maximizing_directions": [list(u) for u in arg],
                                       "subcube_value": 3 * 64}
    # an interior sweep (floats) for the record
    sweep = []
    profs = {name: distance_profiles(lab) for name, lab in LABELS.items()}
    for j in range(1, 50):
        p = Fr(j, 100)
        row = {"p": float(p)}
        for name in LABELS:
            row[name] = 3.0 - cond_entropy_label_bsc(LABELS[name], p, profs[name])
        sweep.append(row)
    out["sweep_bsc"] = sweep
    return out

# ----------------------------------------------------------------------------- section: ordering proof

def phi_lower(rho):
    return rho * rho / (2 * LN2)


def section_ordering_proof(margin=1e-10):
    """Computer-assisted proof that, for X uniform and Y = X xor BSC(p) noise, 0 < p < 1/2,
    I(T;Y) > I(B;Y) > I(G;Y).  Three regions per comparison; see the report for derivations."""
    profs = {name: distance_profiles(lab) for name, lab in LABELS.items()}
    labT, labB, labG = LABELS["trigram"], LABELS["palace"], LABELS["generation"]
    internal, bdeg = edge_structure(labB)
    assert sum(internal) == 64 and sum(bdeg) == 256
    res = {"margin": margin}

    # ---- B versus G
    # Region A: p <= 2^-10, Fano bound on H(B|Y) against H(G|Y) = 3 h(2p(1-p)).
    # Requirement (derived in the report): 6(1-p)(L-1) > (4+10p)(L + log2(7e/(4+10p))) for L = log2(1/p).
    pA = 2.0 ** -10
    c4 = 4 + 10 * pA
    slope = 6 * (1 - pA) - c4
    need = (6 * (1 - pA) + c4 * math.log2(7 * math.e / 4)) / slope
    regionA_BG = {"p_max": pA, "slope_positive": slope > 0, "L_threshold": need, "holds": slope > 0 and need < 10}
    # Region C: p >= 0.23, I(B;Y) >= 1 - h(p) (line 6 is a function of B) and I(G;Y) = 3(1 - h(q)).
    # Requirement: rho^4 + 3 rho^2 - 1 < 0, rho = 1 - 2p.
    rhoC = 1 - 2 * 0.23
    regionC_BG = {"p_min": 0.23, "rho_max": rhoC, "holds": rhoC ** 4 + 3 * rhoC ** 2 - 1 < 0,
                  "line6_is_function_of_B": all(((x >> 5) & 1) == ((labB[x] >> 2) & 1) for x in range(N))}
    # Region B: monotone grid on [2^-10, 0.23].
    grid = [Fr(1, 1024)]
    while grid[-1] < Fr(23, 100):
        grid.append(min(grid[-1] * Fr(6, 5), Fr(23, 100)))
    ok = True
    worst = None
    for a, b in zip(grid, grid[1:]):
        hB = cond_entropy_label_bsc(labB, b, profs["palace"])        # H(B|Y) at right end (upper bound)
        hG = cond_entropy_label_bsc(labG, a, profs["generation"])    # H(G|Y) at left end (lower bound)
        gap = hG - hB
        if worst is None or gap < worst[0]:
            worst = (gap, float(a), float(b))
        if gap <= margin:
            ok = False
    res["B_vs_G"] = {"regionA": regionA_BG, "regionC": regionC_BG,
                     "regionB": {"intervals": len(grid) - 1, "all_hold": ok, "smallest_gap": worst[0],
                                 "at_interval": worst[1:]},
                     "proved": regionA_BG["holds"] and regionC_BG["holds"] and ok}

    # ---- T versus B
    # Region A: p <= 2^-14: H(B|Y) >= P(|E|<=1) avg_y h(m_y p/(1+5p)) and H(T|Y) = 3 h(p).
    # Requirement: (1-5p)(4L - c1) > 3(L + log2 e), c1 = avg_y m_y log2 m_y.
    c1 = sum(m * math.log2(m) for m in bdeg) / N
    pA2 = 2.0 ** -14
    slope2 = 4 * (1 - 5 * pA2) - 3
    need2 = ((1 - 5 * pA2) * c1 + 3 / LN2) / slope2
    regionA_TB = {"p_max": pA2, "c1": c1, "slope_positive": slope2 > 0, "L_threshold": need2,
                  "holds": slope2 > 0 and need2 < 14}
    # Region C: high noise.  I(T;Y) >= 3 rho^2/(2 ln 2); I(B;Y) <= chi2_B(rho) / (2 ln 2 (1 - C rho)).
    W, C = fourier_levels(labB)
    Wf = [float(w) for w in W]
    Cf = float(C)

    def tb_high_ok(rho):
        chi2 = sum(Wf[j] * rho ** (2 * j) for j in range(1, 7))
        return C * rho < 1 and 3 * rho * rho * (1 - Cf * rho) > chi2

    rho_hi = 0.0
    step = 1e-4
    while tb_high_ok(rho_hi + step):
        rho_hi += step
    pC2 = (1 - rho_hi) / 2
    regionC_TB = {"rho_max": rho_hi, "p_min": pC2, "C": Cf, "W": Wf,
                  "holds": rho_hi > 0 and all(tb_high_ok(r * rho_hi / 1000) for r in range(1, 1001))}
    # Region B: monotone grid on [2^-14, pC2 rounded up].
    p_top = Fr(math.ceil(pC2 * 10000) + 1, 10000)
    grid = [Fr(1, 2 ** 14)]
    while grid[-1] < p_top:
        nxt = grid[-1] * Fr(9, 8)
        if nxt > Fr(1, 20):
            nxt = grid[-1] + Fr(1, 400)
        grid.append(min(nxt, p_top))
    ok = True
    worst = None
    for a, b in zip(grid, grid[1:]):
        hT = cond_entropy_label_bsc(labT, b, profs["trigram"])
        hB = cond_entropy_label_bsc(labB, a, profs["palace"])
        gap = hB - hT
        if worst is None or gap < worst[0]:
            worst = (gap, float(a), float(b))
        if gap <= margin:
            ok = False
    res["T_vs_B"] = {"regionA": regionA_TB, "regionC": regionC_TB,
                     "regionB": {"p_top": float(p_top), "intervals": len(grid) - 1, "all_hold": ok,
                                 "smallest_gap": worst[0], "at_interval": worst[1:]},
                     "covers": float(p_top) >= pC2,
                     "proved": regionA_TB["holds"] and regionC_TB["holds"] and ok and float(p_top) >= pC2}
    return res

# ----------------------------------------------------------------------------- section: partitions

def partition_search(J, iters, seed, start=None, T0=0.05):
    rng = random.Random(seed)
    n_out = len(J[0])
    pout = [sum(J[i][o] for i in range(N)) for o in range(n_out)]
    lab = list(start) if start else sum([[k] * 8 for k in range(8)], [])
    if not start:
        rng.shuffle(lab)
    rows = [[0.0] * n_out for _ in range(8)]
    for x in range(N):
        for o in range(n_out):
            rows[lab[x]][o] += J[x][o]
    pk = [sum(r) for r in rows]

    def contrib(k):
        r, s = rows[k], pk[k]
        return sum(m * math.log2(m / (s * pout[o])) for o, m in enumerate(r) if m > 0)

    cs = [contrib(k) for k in range(8)]
    cur = sum(cs)
    best = (cur, list(lab))
    T = T0
    decay = (1e-4 / T0) ** (1.0 / max(iters, 1))
    for _ in range(iters):
        i, j = rng.randrange(N), rng.randrange(N)
        ki, kj = lab[i], lab[j]
        if ki == kj:
            continue
        Ji, Jj = J[i], J[j]
        for o in range(n_out):
            d = Jj[o] - Ji[o]
            rows[ki][o] += d
            rows[kj][o] -= d
        pk[ki] += sum(Jj) - sum(Ji)
        pk[kj] -= sum(Jj) - sum(Ji)
        ci, cj = contrib(ki), contrib(kj)
        new = cur - cs[ki] - cs[kj] + ci + cj
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            lab[i], lab[j] = kj, ki
            cs[ki], cs[kj] = ci, cj
            cur = new
            if cur > best[0]:
                best = (cur, list(lab))
        else:
            for o in range(n_out):
                d = Jj[o] - Ji[o]
                rows[ki][o] -= d
                rows[kj][o] += d
            pk[ki] -= sum(Jj) - sum(Ji)
            pk[kj] += sum(Jj) - sum(Ji)
        T *= decay
    return best


def is_affine_block(block):
    b0 = block[0]
    S = {x ^ b0 for x in block}
    return all((a ^ b) in S for a in S for b in S)


def best_single_swap(J, lab):
    """Largest change in I(lambda; Out) over all swaps of two inputs between different blocks."""
    base = label_info(J, lab)
    best = None
    for i in range(N):
        for j in range(i + 1, N):
            if lab[i] == lab[j]:
                continue
            new = list(lab)
            new[i], new[j] = lab[j], lab[i]
            d = label_info(J, new) - base
            if best is None or d > best:
                best = d
    return best


def section_partitions(channels, iters, restarts, seed):
    out = {}
    targets = {"coins": [[float(v) for v in r] for r in product_joint(channels["coins"])],
               "bsc p=1/10": [[float(v) for v in r] for r in bsc_joint(Fr(1, 10))],
               "yarrow-standard": [[float(v) for v in r] for r in product_joint(channels["yarrow-standard"])]}
    for name, J in targets.items():
        ref = {lbl: label_info(J, lab) for lbl, lab in LABELS.items()}
        best = None
        runs = []
        for r in range(restarts):
            start = LABELS["palace"] if r == 0 else None
            v, lab = partition_search(J, iters, seed + r, start=start)
            runs.append({"seed": seed + r, "start": "palace" if start else "random", "best_I_bits": v})
            if best is None or v > best[0]:
                best = (v, lab, seed + r)
        blocks = [sorted(x for x in range(N) if best[1][x] == k) for k in range(8)]
        out[name] = {"reference": ref, "best_found_I_bits": best[0], "best_seed": best[2],
                     "best_minus_trigram": best[0] - ref["trigram"],
                     "best_blocks_affine": [is_affine_block(b) for b in blocks],
                     "runs": runs, "iterations": iters, "restarts": restarts,
                     "trigram_best_single_swap_change": best_single_swap(J, LABELS["trigram"])}
    return out

# ----------------------------------------------------------------------------- section: INV-0003 check

def count_matchings(adj, vertices):
    """Count perfect matchings of the induced graph by component-wise recursion (small components)."""
    seen, total = set(), 1
    for v in vertices:
        if v in seen:
            continue
        comp, stack = [], [v]
        seen.add(v)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)

        def rec(rem):
            if not rem:
                return 1
            u = min(rem)
            return sum(rec(rem - {u, w}) for w in adj[u] if w in rem)
        total *= rec(frozenset(comp))
    return total


def section_inv0003():
    out = {}
    # L1: reduction and optimum over all 256 functions of G, p = 1/8 and 1/4
    for p in (Fr(1, 8), Fr(1, 4)):
        J = [[float(v) for v in r] for r in bsc_joint(p)]
        q = float(2 * p * (1 - p))
        bound = 1 - h2(q)
        vals, red = [], 0.0
        Gy = [gen_label(y) for y in range(N)]
        for g in range(1, 255):
            f = [x for x in range(N) if (g >> gen_label(x)) & 1]
            v = boolean_info(J, f)
            # I(g(G(X)); G(Y)): joint of g(G(X)) with G(Y)
            joint = {}
            for x in range(N):
                for y in range(N):
                    key = ((g >> gen_label(x)) & 1, Gy[y])
                    joint[key] = joint.get(key, 0.0) + J[x][y]
            pa = {}
            pb = {}
            for (a_, b_), m in joint.items():
                pa[a_] = pa.get(a_, 0.0) + m
                pb[b_] = pb.get(b_, 0.0) + m
            vr = sum(m * math.log2(m / (pa[a_] * pb[b_])) for (a_, b_), m in joint.items() if m > 0)
            red = max(red, abs(v - vr))
            vals.append((v, g))
        vals.sort(reverse=True)
        attaining = [g for v, g in vals if v >= vals[0][0] - 1e-12]
        out["L1 p=%s" % p] = {"max_I": vals[0][0], "bound_1_minus_h_q": bound,
                              "max_abs_reduction_discrepancy": red, "functions_attaining": len(attaining)}
    # L2 values
    for p in (Fr(1, 8), Fr(1, 4)):
        J = bsc_joint(p)
        out["L2 p=%s" % p] = {"B": label_info(J, LABELS["palace"]), "G": label_info(J, LABELS["generation"]),
                              "G_formula": 3 * (1 - h2(float(2 * p * (1 - p))))}
    pairs = {(LABELS["palace"][x], LABELS["generation"][x]) for x in range(N)}
    out["L2 independence (all 64 pairs occur once)"] = len(pairs) == 64
    # L3: matchings of the reversal/complement graph, 2k lines
    l3 = {}
    for k in range(1, 6):
        n = 2 * k
        size = 1 << n
        rev = lambda x: int(format(x, "0%db" % n)[::-1], 2)
        adj = {x: set() for x in range(size)}
        for x in range(size):
            c = x ^ (size - 1)
            adj[x].add(c)
            adj[c].add(x)
            r = rev(x)
            if r != x:
                adj[x].add(r)
                adj[r].add(x)
        cnt = count_matchings(adj, range(size))
        formula = 2 ** (2 ** (2 * k - 2) - 2 ** (k - 1))
        l3["k=%d" % k] = {"count": str(cnt) if cnt > 10 ** 15 else cnt, "formula_agrees": cnt == formula}
    out["L3"] = l3
    # L4: allocation multiplicities for margins (2,2)
    mult = [math.comb(2, a) * math.comb(2, 2 - a) for a in range(3)]
    out["L4"] = {"multiplicities": mult, "extreme_event_uniform_table": "2/3",
                 "extreme_event_allocation": str(Fr(mult[0] + mult[2], sum(mult)))}
    # L5: exact one-sweep marginals and the support bound
    marg_ok = True
    for start in range(N):
        dist = {start: Fr(1)}
        for i in range(6):
            nd = {}
            for pos, pr in dist.items():
                for tgt in (pos, pos ^ (1 << i)):
                    nd[tgt] = nd.get(tgt, Fr(0)) + pr / 2
            dist = nd
        marg_ok &= len(dist) == N and all(v == Fr(1, N) for v in dist.values())
    log2fact = math.log2(math.factorial(64))
    out["L5"] = {"one_sweep_marginals_uniform": marg_ok, "log2_64_factorial": log2fact,
                 "log2_support_over_64_factorial": 192 - log2fact,
                 "min_physical_shuffles_for_tv_quarter": math.ceil((log2fact + math.log2(0.75)) / 32)}
    # L6: balanced characters
    out["L6"] = {"all_nonzero_characters_balanced": all(sum(1 if popcount(a & x) % 2 == 0 else -1 for x in range(N)) == 0
                                                        for a in range(1, N))}
    # Supplement: majorization counterexample at p = 1/8, y = 0
    p = Fr(1, 8)
    post_B, post_G = [Fr(0)] * 8, [Fr(0)] * 8
    for x in range(N):
        w = (p ** popcount(x)) * ((1 - p) ** (6 - popcount(x)))
        post_B[LABELS["palace"][x]] += w
        post_G[LABELS["generation"][x]] += w
    sB = sorted(post_B, reverse=True)
    sG = sorted(post_G, reverse=True)
    out["supplement"] = {"sorted_B": [str(v) for v in sB], "sorted_G": [str(v) for v in sG],
                         "top4_B": str(sum(sB[:4])), "top4_G": str(sum(sG[:4])),
                         "B_majorizes_G_fails": sum(sB[:4]) < sum(sG[:4])}
    return out

# ----------------------------------------------------------------------------- main

def to_jsonable(o):
    if isinstance(o, Fr):
        return str(o)
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    return o


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", required=True)
    ap.add_argument("--nmax", type=int, default=4)
    ap.add_argument("--starts", type=int, default=60)
    ap.add_argument("--iters", type=int, default=60000)
    ap.add_argument("--restarts", type=int, default=4)
    ap.add_argument("--seed", type=int, default=20261031)
    args = ap.parse_args()
    results = {"python": platform.python_version(), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
               "parameters": vars(args)}
    procs, channels = section_procedures()
    results["procedures"] = procs
    print("procedures done", flush=True)
    results["ck_table"] = section_ck(channels)
    print("ck done", flush=True)
    results["inv0003_check"] = section_inv0003()
    print("inv0003 check done", flush=True)
    results["labels"] = section_labels(channels)
    print("labels done", flush=True)
    results["ordering_proof"] = section_ordering_proof()
    print("ordering proof done", flush=True)
    results["dictator_scans"] = section_dictator_scans(channels, args.nmax)
    print("dictator scans done", flush=True)
    results["dictator_n6"] = section_dictator_n6(channels, args.starts, args.seed)
    print("n6 search done", flush=True)
    results["partition_search"] = section_partitions(channels, args.iters, args.restarts, args.seed)
    print("partition search done", flush=True)
    with open(args.out, "w") as fh:
        json.dump(to_jsonable(results), fh, indent=1, sort_keys=True)
        fh.write("\n")


if __name__ == "__main__":
    sys.exit(main())

---

## Supplied material: `investigations/library/openai-math-4eaee875/sources/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex`

\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{microtype,booktabs,array,xcolor,xurl,graphicx,tikz}
\usepackage[colorlinks=true,linkcolor=blue!50!black,citecolor=blue!50!black,urlcolor=blue!50!black]{hyperref}
\hypersetup{pdftitle={Sharp binary-information contraction on the discrete cube},pdfauthor={OpenAI},pdfsubject={Binary information, entropy production, and cube noise}}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\E}{\mathbb E}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Cov}{Cov}
\numberwithin{equation}{section}
\setlength{\emergencystretch}{2em}
\allowdisplaybreaks[1]
\title{Sharp binary-information contraction\\on the discrete cube}
\author{OpenAI}
\date{September 24, 2026}
\begin{document}
\maketitle
\begin{abstract}
We prove sharp contraction of the information carried by a binary channel
under independent symmetric noise on a uniform discrete cube. At fixed
initial information, a noisy coordinate retains the most information.
The Boolean specialization resolves the Courtade--Kumar conjecture and
gives an output-entropy refinement. We also establish a stronger
mean-dependent entropy-production bound. The proof combines an explicit
three-point optimizer for the local joining problem, two entropy
capacities, and a common-output thinning inequality, followed by dimension
induction and integration along the noise semigroup.
\end{abstract}

\section{The contraction theorem and its mechanism}
\label{main:section}

A one-bit summary of independent fair bits can be chosen before those
bits pass through independent binary symmetric channels. Which summary
retains the most information about the noisy observation? Kumar and
Courtade formulated the conjecture that a single input coordinate is
optimal at every noise level and in every dimension
\cite{KumarCourtade2013,CourtadeKumar2014}. We prove a sharp comparison
for arbitrary randomized binary summaries, together with a
mean-dependent bound on their instantaneous information loss.

Let $\Omega_n=\{-1,1\}^n$ carry uniform measure. All information
is measured with natural logarithms. For $r\in[-1,1]$, define
\[
 L=\log2,\qquad
 H(r)=-\frac{1+r}{2}\log\frac{1+r}{2}
      -\frac{1-r}{2}\log\frac{1-r}{2},\qquad \psi(r)=L-H(r),
\]
with $0\log0=0$. Thus $H(r)$ is the entropy of a sign of mean $r$.
For a soft binary channel $u:\Omega_n\to[-1,1]$, define
\[
 I(u)=H(\E u)-\E H(u)=\E\psi(u)-\psi(\E u).
\]
Let $X$ be uniform on $\Omega_n$. If an auxiliary sign $U$ has conditional mean
$\E[U\mid X]=u(X)$, then $I(u)=I(U;X)$.  For
$-1\le\rho\le1$, let $Y_i=X_iZ_i$, where the signs $Z_i$
are independent of $(X,U)$ and each other, with $\E Z_i=\rho$.
The noise operator is $T_\rho u(y)=\E[u(X)\mid Y=y]$.
Thus $\E[U\mid Y]=T_\rho u(Y)$ and $I(T_\rho u)=I(U;Y)$.

\begin{theorem}[Sharp soft-channel contraction]
\label{main:soft}
For every finite $n\ge0$, every $u:\Omega_n\to[-1,1]$, and
$-1\le\rho\le1$,
\begin{equation}
 I(T_\rho u)
 \le\psi\!\left(|\rho|\,\psi^{-1}(I(u))\right).
 \label{main:interpolation}
\end{equation}
The inverse is the nonnegative increasing branch on $[0,L]$.
For $n\ge1$, every soft coordinate $u(x)=a x_i$, $|a|\le1$,
attains equality.
\end{theorem}

The parameter $\psi^{-1}(I(u))$ is the amplitude of a fair soft
coordinate with the same information as $u$.  The theorem says that
this effective amplitude contracts at least as fast as a coordinate.
Sharpness concerns all soft channels at a given initial information;
it does not assert that every biased Boolean source attains the bound.

\begin{corollary}[The Boolean bound with output bias]
\label{main:ck}
For every finite $n\ge0$, $\rho\in[-1,1]$, and
$f:\Omega_n\to\{-1,1\}$, put
$m=\E f$ and $r_m=\psi^{-1}(H(m))$.  Then
\begin{equation}
 I(f(X);Y)\le\psi(|\rho|r_m)\le\psi(|\rho|).
 \label{main:bound}
\end{equation}
For $n\ge1$, signed coordinate functions attain the bound at $m=0$.
If $0<|m|<1$ and $0<|\rho|\le1$, the refined upper curve is
strictly below the universal curve $\psi(|\rho|)$.
\end{corollary}

For noise crossover probability $\varepsilon\in[0,1/2]$, one has
$\rho=1-2\varepsilon$. Writing
$h_2(p)=-p\log_2p-(1-p)\log_2(1-p)$, the universal bound in bits is
\[
 I_2(f(X);Y)\le\frac{\psi(\rho)}{L}=1-h_2(\varepsilon).
\]
This is the Courtade--Kumar conjecture. The refinement uses the actual
entropy of the Boolean output, while the input distribution remains uniform.

\subsection{Prior work and related results}

Ordentlich, Shayevitz, and Weinstein
\cite{OrdentlichShayevitzWeinstein2016} obtained asymptotically sharp
high-noise bounds for balanced Boolean functions. Samorodnitsky
\cite{Samorodnitsky2016} proved the conjecture for all
Boolean functions in a dimension-independent high-noise range.
Yu's work on $\Phi$-stability and local optimality
\cite{Yu2023,Yu2026} enlarged the proved range for balanced functions;
the latter gives $0\le\rho\le0.914$ by a computer-assisted argument.
Javanmard and Woodruff \cite{JavanmardWoodruff2026} extended
Courtade and Kumar's coordinatewise sum bound
\cite[Theorem~1]{CourtadeKumar2014} from balanced functions to
arbitrary output bias and refined high-noise entropy estimates.

Several nearby formulations clarify the role of the full noisy vector.
Pichler, Piantanida, and Matz \cite{PichlerPiantanidaMatz2018} proved
coordinate optimality when the observation is also reduced to one
Boolean output. At fixed output mean, Li and M\'edard
\cite{LiMedard2021} identified lexicographic optimizers at sufficiently
low noise and related high-noise optimizers to first-level Fourier
weight, in dimension-dependent ranges. Barnes and \"Ozg\"ur
\cite{BarnesOzgur2020} proved the equivalence of the balanced conjecture
and a symmetrized Li--M\'edard moment inequality.
Kindler, O'Donnell, and Witmer \cite{KindlerODonnellWitmer2016}
proved fixed-mean Gaussian and spherical analogues. These fixed-mean
questions are distinct from attainability of the refined upper curve
in Corollary~\ref{main:ck}.

Chen, Gohari, and Nair \cite{ChenGohariNair2025} developed the
differential approach that we use: prove a local entropy-production
inequality, lift it by induction on the cube dimension, and integrate
along the noise semigroup. Their approach builds on the auxiliary
receiver method of Gohari and Nair \cite{GohariNair2022}. The
August 2026 revision of Chen--Gohari--Nair disproves one proposed auxiliary inequality
\cite[Appendix~B]{ChenGohariNair2025}; the local comparisons below
are proved directly. Their symmetric optimizer is a predecessor of
our arbitrary-mean joining problem, as explained in
Section~\ref{canonical:section}.

Recent preprints announce proofs of the Courtade--Kumar conjecture by
several routes. Chen, Gohari, Javanmard, Lin, Mirrokni, Nair, and
Woodruff~\cite{ChenEtAl2026CK} use a computer-assisted Bellman inequality;
Ky and Tran~\cite{KyTran2026CK} develop entropy-production and spectral
estimates with computer-assisted verification;
Mahdavifar and Beirami~\cite{MahdavifarBeirami2026CK} use
entropy flow, Fourier analysis, and bounds for pivotal sets; and
Kramer and Saglam~\cite{KramerSaglam2026} prove a finite-noise
bound that retains the Boolean output bias.
The overlap with the first work extends beyond the Boolean conjecture:
its Lemma~9.2 applies to arbitrary binary channels, and retaining the
initial information when integrating its production bound gives
Theorem~\ref{main:soft} and Corollary~\ref{main:ck}.
Our proof solves the joining problem with a common entropy budget and
uses two capacities and common-output thinning. It also proves the additional
mean-dependent production estimate in
Theorem~\ref{upgrade:production}; we compare the two production
profiles in Section~\ref{flow:comparison}.

\subsection{From information loss to a local joining inequality}

For an interior soft field $g:\Omega_n\to(-1,1)$, put
\begin{equation}
 m=\E g,\qquad e=\E H(g),\qquad I(g)=H(m)-e,
 \qquad D(g)=\E[V(g)Ng],
 \label{main:functionals}
\end{equation}
where $V(r)=\operatorname{atanh}r$ and
\[
 N=\frac12\sum_{i=1}^n(\mathrm{Id}-\mathrm{flip}_i),
 \qquad P_t=T_{e^{-t}}=e^{-tN}.
\]
Here $\mathrm{flip}_i$ flips coordinate $i$. Mean conservation and
finite-dimensional differentiation give
\begin{equation}
 \frac{d}{dt}I(P_tg)=-D(P_tg).
 \label{main:flow-identity}
\end{equation}
The production of a soft coordinate $g(x)=r x_i$ is $rV(r)$.
We therefore define its rate by
$F(\psi(r))=rV(r)$ for $0\le r<1$ and seek the inequality
$D(g)\ge F(I(g))$. Once this is proved,
$r_t=\psi^{-1}(I(P_tg))$ satisfies $r_t'\le-r_t$ whenever
$I(P_tg)>0$. Integrating gives Theorem~\ref{main:soft};
Section~\ref{flow:section} treats zero information and boundary-valued
inputs.

The local-to-global program is due to
Chen--Gohari--Nair \cite[Definition~1 and Theorem~2]{ChenGohariNair2025}.
To see the required local comparison, split the cube along one
coordinate into fields $g_+,g_-$ on $\Omega_{n-1}$. Their productions
satisfy the exact identity
\begin{equation}
 D(g)=\frac{D(g_+)+D(g_-)}2+\E c(g_+,g_-),\qquad
 c(a,b)=\frac{a-b}{4}\{V(a)-V(b)\},
 \label{main:energy-split}
\end{equation}
where the last expectation is over the remaining coordinates.
Write $m_\pm=\E g_\pm$ and $I_\pm=I(g_\pm)$.
For a profile with $\Phi_m(0)=0$, the required induction step is that
the joining edges pay its increase:
\[
 \E c(g_+,g_-)
 \ge\Phi_m(I(g))-
 \frac{\Phi_{m_+}(I_+)+\Phi_{m_-}(I_-)}2.
\]
The information-only choice $\Phi_m(I)=F(I)$ does not satisfy the
corresponding local comparison for every coupled pair law
\cite[Remark~5]{ChenGohariNair2025}. The proof must retain the mean
as well as the information.

\subsection{Two profiles and the geometry of the joining cost}

The linear estimate $D(g)\ge2I(g)$ follows from the classical cube
logarithmic Sobolev inequality and its entropy-dissipation consequence,
within the hypercontractive framework of Bonami, Gross, and Beckner
\cite{Bonami1970,Gross1975,Beckner1975}; see also
Bobkov--Tetali \cite[Example~3.7]{BobkovTetali2006} for the modified logarithmic
Sobolev formulation. Mrs.\ Gerber's lemma \cite{WynerZiv1973} contains
the same scalar one-bit entropy curve, but its direct vector form has
dimension-normalized arguments. The nonlinear surplus above $2I$ is
the part that needs a new local comparison.

Since $F'(0)=2$, define
\[
 S(I)=F(I)-2I\quad(0\le I<L),\qquad S(I)=0\quad(I<0).
\]
For $|m|<1$ and $0\le I<H(m)$, set
\begin{equation}
 \mathcal B_m(I)=2I+(1-m^2)S\!\left(
 L-\frac{H(m)-I}{1-m^2}\right).
 \label{main:profile}
\end{equation}
The factor $1-m^2$ is useful because the average of the two child
variance factors at means $m\pm\delta$ is $1-m^2-\delta^2$.
Convexity therefore pools their surplus terms in the same form.
Section~\ref{reserve:section} explains the two-capacity allocation
behind this profile and proves its local joining inequality.
The same two capacities occur in the Boolean finite-noise bound of
Kramer and Saglam~\cite{KramerSaglam2026}; that section gives the comparison.

To prove the local joining inequality for $\mathcal B$, regard
$(g_+(X'),g_-(X'))$ as a coupled pair
of random variables, where $X'$ is uniform on the remaining cube.
We minimize the joining cost over all coupled pair laws with the same
child means and average conditional entropy, extending $c$ by zero at
the equal corners and by $+\infty$ at every other boundary pair.
The exact optimizer has one interior pair $(a_c,b_c)$ and possibly
the two equal-output corners $(1,1)$ and $(-1,-1)$.
Section~\ref{canonical:section} proves this description by assigning a
nonnegative price to entropy. Section~\ref{capacity:section} proves the
one-bit inequality that pays the interior pair. Adding either common
output reduces the payment required by $\mathcal B$ at least in
proportion to the retained mass. Composing these two operations pays
the full optimizer. Throughout this minimization, the original face
entropies remain in the child profiles; only their average enters the
cost problem.

At mean zero, $\mathcal B_0=F$, but at other means neither profile
can be discarded. We prove local joining for their maximum,
\begin{equation}
 \widehat{\mathcal B}_m(I)
 =\max\{\mathcal B_m(I),F(I)\}.
 \label{main:hybrid-profile}
\end{equation}
Two comparisons make this possible. First,
\begin{equation}
 I\ge L/2\quad\Longrightarrow\quad
 \mathcal B_m(I)\ge F(I).
 \label{main:threshold}
\end{equation}
Thus only parents below half information can require the $F$ branch.
At such a parent, convexity at the original child states reduces the
unpaid amount to $F(I)-F(j)$, where $j=(I_++I_-)/2$.

For the second comparison, reflect the output signs if necessary so
that the parent mean is nonnegative. An optimizer with one corner then
combines a core of nonnegative center with $(1,1)$.
Section~\ref{thinning:section} shows that this addition reduces the
increment at least in proportion to the retained mass, and so the
one-bit inequality pays the mixture. When both corners occur, the core
is reflected, $(r,-r)$. Holding the core and its mass fixed preserves the separation of the
child means, their average conditional entropy, and the joining cost.
We increase the common mean until one corner disappears, as in
Figure~\ref{fig:reflected-core}. Below half information the required
increment increases during this motion. The one-corner endpoint
therefore pays the original state as well.

Section~\ref{upgrade:section} combines these comparisons and performs
dimension induction to prove the following strengthening of the scalar
rate inequality.

\begin{theorem}[Sharp soft production]
\label{upgrade:production}
For every finite $n\ge0$ and every $g:\{-1,1\}^n\to(-1,1)$,
with $m=\E g$,
\begin{equation}
 D(g)\ge\widehat{\mathcal B}_m(I(g))
       =\max\{\mathcal B_m(I(g)),F(I(g))\}
       \ge F(I(g)).
 \label{upgrade:production-bound}
\end{equation}
\end{theorem}

The scalar facts needed by the local comparisons are proved in
Section~\ref{scalar:section}. Section~\ref{flow:section} integrates
the production bound and compares its mean-dependent part with the
profile of Chen et al.\ \cite{ChenEtAl2026CK}.


\input{sections/scalar}
\input{sections/canonical}
\input{sections/capacity}
\input{sections/reserve}
\input{sections/thinning}
\input{sections/upgrade}
\input{sections/flow}
\bibliographystyle{plain}
\bibliography{references}
\end{document}
