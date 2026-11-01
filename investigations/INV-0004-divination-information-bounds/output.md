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
