# INV-0006 — ASN-0014: Independent Verification of Divination-Channel Claims (Phase 1)

- **Role:** Adversarial Mathematical Verifier
- **Model:** OpenAI Codex, GPT-5-based; exact deployment identifier not exposed
- **Phase status:** Blind independent derivation. I used only the phase-1 brief supplied in the prompt. I did not seek or inspect the earlier investigation's report, proof, code, or output.
- **Materials and tools:** The supplied definitions and claims; my own [`phase1_verify.py`](phase1_verify.py); Python 3.9 standard library and local shell execution. No web, literature, historical source, traditional table, or external dataset was consulted.
- **Execution status:** Every computation reported as executed below was actually run on 2026-11-01 and completed with exit code 0. Analytic derivations were written independently but have not been checked by a second implementation or verifier.

## Provisional verdict table

| Claim | Mathematical correctness | Source correspondence | Significance claims | One-line reason |
|---|---|---|---|---|
| V1 | `confirmed` | N/A—formal stipulated models | N/A—none made | Exact line tables give all stated conditionals and information values. |
| V2 | `ill-posed` | N/A—formal stipulated models | N/A—none made | The uniform-split fractions are exact; “to about \(10^{-6}\)” is true as an order statement but false if it means absolute error at most \(10^{-6}\). |
| V3 | `confirmed` (conditional) | N/A—formal channel | N/A—none made | The coin model meets the premise exactly in both directions; a coordinate bit attains the bound. The premise itself was not proved or assumed unconditionally. |
| V4 | `confirmed` | N/A—formal labels; no historical table claimed | N/A—none made | Exact posterior enumeration plus a rational interval certificate proves both strict inequalities for every \(0<p<1/2\). |
| V5 | `confirmed` | N/A—formal labels and cube | N/A—none made | Direct entropy expansions, exact edge/centroid calculations, an edge-isoperimetric proof, and an exhaustive exact cut-DP establish every part. |

All five claims are **definition-driven relative to the stipulated models and the supplied set \(D\)**. V2, V4, and the \(B\)-parts of V5 are data-specific—their values would change if the stipulated procedure or \(D\) changed—but they depend on no attested source in this assignment.

## 1. Executive findings

V1, conditional V3, V4, and V5 survive as stated. V4's universal quantifier is not based on sampling: I obtained a computer-assisted sign proof over the entire open interval. V5's extremal assertion was also checked without importing a classical result: an exact finite dynamic program proves the claimed centroid bound and equality case, while the edge bound used for \(\beta\) has a short induction.

The only objection is terminological precision in V2. For the binomial split, the four absolute deviations from \((1,5,7,3)/16\) are approximately

\[
(1.0160401,\;1.9476372,\;1.0694179,\;0.1378208)\times 10^{-6}.
\]

Thus “of order \(10^{-6}\)” is accurate, while “within \(10^{-6}\)” is not. A precise nearby statement is: **every deviation is below \(1.948\times10^{-6}\)**.

## 2. Exact mathematical results and derivations

### V1 — line laws and information

The precise reading is that the six line pairs \((X_i,E_i)\) are independent copies of the stated one-line law, and \(Y_i=X_i\oplus E_i\).

For coins and standard yarrow I independently obtained:

| value \(v\) | \(X\) | \(E\) | coins | yarrow-standard |
|---:|---:|---:|---:|---:|
| 6 | 0 | 1 | \(1/8\) | \(1/16\) |
| 7 | 1 | 0 | \(3/8\) | \(5/16\) |
| 8 | 0 | 0 | \(3/8\) | \(7/16\) |
| 9 | 1 | 1 | \(1/8\) | \(3/16\) |

For coins, the four entries factor as \(P(X=x)P(E=e)\), with \(X\sim\mathrm{Bernoulli}(1/2)\) and \(E\sim\mathrm{Bernoulli}(1/4)\). Consequently the six-line channel is exactly \(\mathrm{BSC}(1/4)^{\otimes6}\), and

\[
I(X;Y)=6[1-h_2(1/4)]
=1.132331253245203\ldots .
\]

For standard yarrow, independently combining the stipulated removals gives

\[
(P_6,P_7,P_8,P_9)=(1,5,7,3)/16.
\]

Hence \(X\) is fair,

\[
P(E=1\mid X=1)=\frac{3}{8},\qquad
P(E=1\mid X=0)=\frac{1}{8},
\]

\(P(Y=1)=P(6)+P(7)=3/8\), and \(P(E=1)=1/4\). Independence across lines gives

\[
\begin{aligned}
I(X;Y)
 &=6\left[h_2(3/8)-\tfrac12h_2(1/8)-\tfrac12h_2(3/8)\right]\\
 &=3[h_2(3/8)-h_2(1/8)]\\
 &=1.232608679176106\ldots,\\[2mm]
I(X;E)
 &=6\left[h_2(1/4)-\tfrac12h_2(1/8)-\tfrac12h_2(3/8)\right]\\
 &=0.373673408381113\ldots .
\end{aligned}
\]

**Classification:** definition-driven and standard/routine, not mathematically distinctive by itself.

### V2 — uniform and conditioned-binomial splits

I transcribed only the supplied formal procedure. Define

\[
r(k)=\begin{cases}0,&k=0,\\1+((k-1)\bmod4),&k>0.\end{cases}
\]

For current count \(n\) and left size \(\ell\), my transition was

\[
n'=n-\{1+r(\ell)+r(n-\ell-1)\}.
\]

I propagated this transition three times from the point mass at 49, using either

\[
P(\ell\mid n)=\frac1{n-1}
\quad\text{or}\quad
P(\ell\mid n)=\frac{\binom n\ell}{2^n-2},
\qquad 1\le \ell\le n-1.
\]

This exact `Fraction` computation was executed. For the uniform split it gives the complete law

| value | exact probability | decimal |
|---:|---:|---:|
| 6 | \(77/1612\) | 0.0477667493796526 |
| 7 | \(4051193/14556360\) | 0.2783108551863240 |
| 8 | \(424399/939120\) | 0.4519113638299685 |
| 9 | \(5957/26832\) | 0.2220110316040549 |

Therefore

\[
P(X=1)=P(7)+P(9)=\frac{14565731}{29112720}
=0.5003218867903789\ldots .
\]

For the conditioned-binomial split, the executed exact calculation gives:

| value | probability | signed deviation from standard yarrow |
|---:|---:|---:|
| 6 | 0.0625010160401112 | \(+1.0160401112\times10^{-6}\) |
| 7 | 0.3124980523628418 | \(-1.9476371582\times10^{-6}\) |
| 8 | 0.4375010694178633 | \(+1.0694178633\times10^{-6}\) |
| 9 | 0.1874998621791837 | \(-0.1378208163\times10^{-6}\) |

The complete exact rational outputs, including very large conditioned-binomial numerators and denominators, are printed by the reproducibility script.

**Ambiguous readings and verdicts:**

1. “The errors have order \(10^{-6}\)”: `confirmed`.
2. “Every absolute error is at most \(10^{-6}\)”: `refuted`; values 6, 7, and 8 exceed that threshold.
3. Corrected unambiguous version: “the maximum absolute error is \(1.9476371583\times10^{-6}\), hence below \(1.948\times10^{-6}\).”

**Classification:** definition-driven, data-specific, and a routine but nontrivial exact finite computation.

### V3 — transfer of the stated premise

This claim is conditional. I did not attempt to prove the premise.

The forward hypotheses hold exactly by V1: \(X\) consists of six independent fair bits and \(Y=X\oplus E\), with independent \(E_i\sim\mathrm{Bernoulli}(1/4)\). Thus the premise at \(r=1/4\) gives

\[
I(f(X);Y)\le1-h_2(1/4)=0.188721875540867\ldots
\]

for every Boolean \(f\).

For the reverse direction, for every \(e,y\),

\[
P(E=e,Y=y)=P(E=e)P(X=y\oplus e)=P(E=e)/64.
\]

So \(Y\) is also a vector of independent fair bits and \(E\) is independent of \(Y\); moreover \(X=Y\oplus E\). The same premise therefore applies with \(X,Y\) exchanged.

Taking \(f(X)=X_i\), the other five output bits are independent of \(X_i\), so

\[
I(X_i;Y)=I(X_i;Y_i)=1-h_2(1/4),
\]

and a single coordinate attains the bound. The reverse coordinate statement is identical.

**Classification:** definition-driven and trivial once V1 and the conditional premise are granted. This verdict does **not** promote the premise to a proved theorem.

### V4 — strict information ordering for every \(0<p<1/2\)

First, the supplied \(D\) really is a transversal for \(G\). Its \(G(d)=L(d)\oplus U(d)\) values are:

| \(d\) | \(G(d)\) |
|---|---|
| 000000 | 000 |
| 100000 | 100 |
| 110000 | 110 |
| 111000 | 111 |
| 111100 | 011 |
| 111110 | 001 |
| 111010 | 101 |
| 000010 | 010 |

They are all eight trigrams exactly once, so \(B\) is well-defined. Its fibers are

\[
A_b=(b,b)\oplus D,
\]

and \((B,G)\mapsto X=(B,B)\oplus d_G\) is a bijection. Hence \(T,B,G\) are all balanced.

Two mutual informations simplify analytically:

\[
I(T;Y)=3[1-h_2(p)].
\]

For each paired coordinate, \(G_i=X_i\oplus X_{i+3}\). The observed parity is crossed precisely when exactly one of the two noise bits is 1, with probability

\[
q=2p(1-p).
\]

The remaining observed bit in the pair carries no further information about the uniform input parity. The three pairs are independent, so

\[
I(G;Y)=3[1-h_2(2p(1-p))].
\]

For \(B\), and for the rigorous comparison, I enumerated exact posterior polynomials. If \(A_a\) is a label fiber, then for uniform \(X\)

\[
q_{a,y}(p)=P(\lambda(X)=a\mid Y=y)
=\sum_{x\in A_a}p^{d(x,y)}(1-p)^{6-d(x,y)},
\]

and

\[
H(\lambda(X)\mid Y)
=-\frac1{64}\sum_{y,a}q_{a,y}(p)\log_2q_{a,y}(p).
\]

Define

\[
F_{TB}=64\ln2\,[I(T;Y)-I(B;Y)],\qquad
F_{BG}=64\ln2\,[I(B;Y)-I(G;Y)].
\]

The executed certificate proves both functions positive as follows:

| range | method | \(F_{TB}\) certificate | \(F_{BG}\) certificate |
|---|---|---:|---:|
| \(0<p\le10^{-3}\) | isolate \(\ln(1/p)\) in \(F'\), interval-bound analytic remainder | \(F'_{TB}>358.54\) | \(F'_{BG}>624.42\) |
| \(10^{-3}\le p\le0.49\) | adaptive mean-value intervals | 38 intervals, depth \(\le8\), minimum lower margin \(>0.00207\) | 38 intervals, depth \(\le8\), minimum lower margin \(>0.00386\) |
| \(0.49\le p<1/2\) | put \(\rho=1-2p\), prove \(F(0)=F'(0)=0\) and \(F''>0\) | \(F''_{TB}>58.43\) | \(F''_{BG}>91.10\) |

All polynomial endpoints and operations use exact rational arithmetic. For logarithms, if \(z\in[1,2)\) and \(t=(z-1)/(z+1)\le1/3\), the code uses 16 terms of

\[
\ln z=2\sum_{j\ge0}\frac{t^{2j+1}}{2j+1}
\]

and adds the explicit rational tail bound

\[
0<R_N\le
\frac{2t^{2N+1}}{(2N+1)(1-t^2)}.
\]

The central certificate encloses both the midpoint value and the derivative throughout each accepted interval; it accepts \([a,b]\) only when

\[
F((a+b)/2)_{\rm lower}
-\sup_{[a,b]}|F'|\,(b-a)/2>0.
\]

This is a finite error-controlled proof, not a grid evaluation.

At \(p=1/4\), rigorous bit-valued enclosures from the same log bounds are:

\[
\begin{array}{c|c}
\lambda&I(\lambda(X);Y)\\\hline
T&[0.5661656266226014,\ 0.5661656266226015]\\
B&[0.3786210551758796,\ 0.3786210551758797]\\
G&[0.13669799122510506,\ 0.13669799122510518].
\end{array}
\]

These round to the three values in V4.

**Classification:** definition-driven and data-specific; the all-parameter ordering is nontrivial. The proof is computer-assisted and should ideally receive a second implementation audit in phase 2 or a later assignment.

### V5 — endpoint expansions and extremal statements

#### Small-noise expansion

For a balanced label \(\lambda\), fix \(Y=y\). The posterior mass on the label of \(y\) is \(1-O(p)\). For another label \(a\),

\[
P(\lambda(X)=a\mid Y=y)=m_{y,a}p+O(p^2),
\]

where \(m_{y,a}\) is the number of one-bit neighbors of \(y\) with label \(a\). Consequently

\[
H(\lambda(X)\mid Y=y)
=\left(\sum_{a\ne\lambda(y)}m_{y,a}\right)
p\log_2(1/p)+O(p).
\]

The finite average over \(y\) gives

\[
I(\lambda;Y)=3-\beta(\lambda)p\log_2(1/p)+O(p).
\]

The executed edge count gives

\[
\beta(T)=3,\qquad \beta(B)=4,\qquad \beta(G)=6.
\]

For \(B\), every fiber is a translate of \(D\); \(D\) induces exactly eight undirected cube edges, hence has average internal degree 2 and average external degree 4.

#### High-noise expansion

Write \(\chi_i(x)=(-1)^{x_i}\). For a fiber \(A\) and \(\rho=1-2p\),

\[
P(X\in A\mid Y=y)
=2^{-6}\sum_{x\in A}\prod_{i=1}^6
[1+\rho\chi_i(x)\chi_i(y)]
=\frac18+\frac{\rho}{64}\sum_i s_i(A)\chi_i(y)+O(\rho^2).
\]

Expanding relative entropy from the uniform distribution on eight labels and averaging over \(y\) yields

\[
I(\lambda;Y)=
\frac{\rho^2}{2\ln2}
\sum_A\frac{\lVert s(A)\rVert^2}{64|A|}
+O(\rho^4).
\]

The remainder is \(O(\rho^4)\), rather than merely \(O(\rho^3)\), because changing \(\rho\) to \(-\rho\) is equivalent to complementing every output bit, a bijection that leaves mutual information unchanged.

For \(T\), every fiber fixes three coordinates, so every squared centroid norm is \(3\cdot8^2=192\) and \(W_1(T)=3\). For \(G\), every coordinate is balanced within every fiber, so \(W_1(G)=0\). For \(B\), translations change only centroid signs, and the executed calculation gives

\[
s(D)=(-4,-2,0,4,2,8),\qquad \lVert s(D)\rVert^2=104,
\]

so

\[
W_1(B)=8\frac{104}{64\cdot8}=\frac{13}{8}.
\]

#### The \(\beta\) extremum

For a fiber \(A\), let \(e(A)\) be its number of internal cube edges. Then

\[
\beta=6-\frac{2}{64}\sum_Ae(A).
\]

The standard edge bound needed here has a short proof: every \(m\)-vertex subset of a cube induces at most \(m\log_2m/2\) edges. Split along a coordinate into sizes \(a\le b\). Induction gives at most

\[
\frac{a\log_2a+b\log_2b}{2}+a
\le\frac{(a+b)\log_2(a+b)}2,
\]

where the last inequality is \(h_2(a/(a+b))\ge2a/(a+b)\), true by concavity on \([0,1/2]\). Equality for \(m=8\) forces a three-dimensional coordinate subcube. Thus each fiber has at most 12 edges, so \(\beta\ge3\), with equality for partitions into coordinate 3-subcubes.

#### The centroid extremum

For an eight-set \(A\subset Q_6\), label its vertices \(0,\ldots,7\). Each cube coordinate is a cut \(S\mid S^c\) of these labels. Its contribution to the total unordered pairwise Hamming distance is \(|S|(8-|S|)\). If \(P(A)\) denotes that total, then

\[
\lVert s(A)\rVert^2=384-4P(A).
\]

I exhaustively dynamic-programmed over the 128 cuts modulo complementation, through six coordinates. The state is the partition of the eight row labels induced by the cuts so far; there are only 4,140 possible partitions. Nonnegative-cost states above 48 were discarded. The executed state/record counts after coordinates 1 through 6 were

\[
(128,128),\ (2795,5876),\ (4140,44630),\ (4140,76957),\
(4140,88683),\ (4140,90525).
\]

At the final discrete partition, the complete set of records with cost at most 48 was exactly

\[
[(48,(4,4,4))],
\]

where the profile records the minority sizes of nonconstant cuts. Hence \(P(A)\ge48\), so \(\lVert s(A)\rVert^2\le192\). Equality uses exactly three balanced nonconstant coordinates. Since those three cuts distinguish eight rows and there are exactly eight three-bit strings, all patterns occur; the other three coordinates are fixed. Thus equality holds **exactly** for coordinate 3-subcubes.

For a balanced label with eight fibers,

\[
W_1\le8\frac{192}{64\cdot8}=3,
\]

with equality when every fiber is a coordinate 3-subcube. Such partitions also attain \(\beta=3\).

**Classification:** the expansions are standard Fourier/entropy calculations; the numerical invariants are routine exact checks; the equality classification and combined extremal conclusion are nontrivial. No classical result was accepted without proof.

## 3. Failed hypotheses and negative results

1. **Strict \(10^{-6}\) reading of V2:** refuted only at that tolerance. This does not challenge the conditioned-binomial model or the statement that its deviations are of millionth order.
2. **A possible pointwise-majorization proof of \(I(B)>I(G)\):** failed. At \(p=1/10\) and \(y=000000\), the sorted \(B\)-posterior is
   \[
   (657,81,81,81,73,9,9,9)/1000,
   \]
   while the sorted \(G\)-posterior is
   \[
   (68921,15129,15129,15129,3321,3321,3321,729)/125000.
   \]
   The difference between their top-four cumulative masses is \(-226/15625\), so \(B\)'s posterior does not majorize \(G\)'s. This only rules out that simple proof route; the entropy inequality remains true and is certified by the interval argument.

## 4. Unresolved questions

- The Boolean-information premise in V3 remains an assumption, exactly as requested. This phase establishes only the transfer to and from the coin channel.
- V4 now has a finite certificate, but I did not find a short, purely analytic proof of the two strict inequalities. Whether a useful degradation, entropy, or refined-majorization argument exists remains open.
- No historical or source correspondence was investigated. The formal labels and the models named “yarrow” should not be treated as historically authenticated by this report.
- Phase-2 audit questions—whether the original author ran the claimed computations, used the same remainder convention, and proved the all-\(p\) quantifier—must await the original evidence.

## 5. Dependencies and evidence lineage

Every result was independently derived from the supplied definitions, not reused from a supplied proof, dataset, or program. The common inputs that could cause correlated errors are:

- the bottom-to-top bit convention;
- the eight supplied strings in \(D\);
- the stipulated treatment of an empty right heap after setting one stalk aside;
- the interpretation of the six lines as independent copies;
- the conditional nature of V3's premise.

The exact arithmetic, posterior enumeration, interval proof, and cut-DP all reside in one implementation. That is evidence from one lineage, not an independent replication of itself. A successor should especially recheck the transcription of \(D\), the posterior normalization, and the sign definitions \(F_{TB},F_{BG}\).

## 6. Alternative explanations and broader context

- V1 and the analytic parts of V4 follow from ordinary product-channel structure; they do not indicate a specifically Yijing phenomenon.
- The local V4 ordering near \(p=0\) is already explained by \(\beta(T)<\beta(B)<\beta(G)\), and near \(p=1/2\) by \(W_1(T)>W_1(B)>W_1(G)\). The nonlocal fact is that no crossing occurs in between.
- The V5 extrema are hypercube isoperimetric/centroid facts about all balanced eight-valued labels. Coordinate projections attain them regardless of any Yijing interpretation.
- The special middle position of \(B\) is contingent on the supplied transversal \(D\); no uniqueness or optimality of this \(D\) was claimed or established.

## 7. Reproducibility

The complete executed implementation is [`phase1_verify.py`](phase1_verify.py). It contains the full data transcription

```text
000000 100000 110000 111000 111100 111110 111010 000010
```

and no hidden input files. Run from this directory with:

```sh
python3 -u phase1_verify.py
```

The script uses only the Python standard library. It prints all exact V1/V2 probabilities, V4 values and certificate statistics, \(\beta\), \(W_1\), the centroid of \(D\), and every cut-DP state count quoted above.

Precision distinctions:

- V1 formulas and all V2 laws are exact; their displayed decimals are binary64 renderings.
- V4's displayed sampling helper is not used for the proof. The reported rigorous enclosures and every sign decision use exact `Fraction` endpoints plus explicit rational logarithm remainders.
- V5's counts and DP are exact integers/rationals.

## 8. Opportunities for further research

- Classify which transversals \(D\) give a global no-crossing order between \(T,B,G\), rather than merely the endpoint coefficient order.
- Determine whether \((\beta,W_1)\) imposes useful global bounds on information curves for balanced partitions of a cube.
- Classify partitions of \(Q_6\) into eight coordinate 3-subcubes, including mixed orientations, and identify equivalence classes under cube automorphisms.
- Seek a human-sized entropy proof of V4. A promising approach not attempted fully here is to exploit the six posterior types of \(B\) together with sharp entropy comparisons, rather than interval subdivision.

## 9. Recommended next assignments and next-step contracts

### A. Audit V4 with a second proof lineage

- **Question:** Are both inequalities positive for all \(0<p<1/2\) under an implementation independent of this script?
- **Minimum inputs:** The eight strings in \(D\), the definitions of \(T,B,G\), and the BSC law.
- **Cheapest decisive check:** Rebuild the posterior polynomials independently and certify signs with Bernstein-form interval arithmetic or exact Taylor models.
- **Outcomes:** Agreement strongly reduces implementation risk; a failed interval identifies a concrete parameter interval or transcription discrepancy.
- **Stopping condition:** A complete covering certificate with explicit error bounds, or an exact/numerically isolated counterexample.

### B. Replace the V4 certificate by an analytic comparison if possible

- **Question:** Can one prove \(H_T(p)<H_B(p)<H_G(p)\) using entropy inequalities for the six posterior types?
- **Minimum inputs:** The exact posterior enumerators generated from \(D\).
- **Cheapest decisive check:** Symbolically group the six entropy types and test candidate convexity or log-sum inequalities.
- **Outcomes:** A proof would explain the ordering; a counterexample to a proposed majorization/degradation relation would narrow the route, without challenging V4 itself.
- **Stopping condition:** A valid closed-form proof, or a catalog showing the natural degradation/majorization candidates fail.

### C. Clarify V2's registered precision

- **Question:** Was “about \(10^{-6}\)” intended as order of magnitude or as a hard tolerance?
- **Minimum inputs:** The original wording or author clarification.
- **Cheapest decisive check:** Compare the intended convention with the exact four deviations above.
- **Outcomes:** Keep V2 as written under the loose reading, or amend it to “maximum error below \(1.948\times10^{-6}\).”
- **Stopping condition:** An unambiguous numerical statement in the registry.

The immediate next procedural step is phase 2: obtain and audit the original reasoning and evidence without changing these provisional verdicts retroactively.

## Search log

| Attempt ID | Object/data version | Representation and exact question/bounds | Outcome and evidence | Why stopped / successor variation |
|---|---|---|---|---|
| S1 | Supplied line models, 2026-11-01 | Exact one-line tables and three-step rational Markov propagation | V1 confirmed; V2 exact laws in `phase1_verify.py` | Questions settled exactly. |
| S2 | Supplied \(D\) | Seek structural/majorization proof of V4 | Simple \(B\succ G\) pointwise majorization fails at \(p=1/10,y=0^6\); exact counterexample in §3 | Switched to direct entropy certification; successor could try a weaker averaged order. |
| S3 | Exact posterior distance enumerators | Prove both V4 signs on all \((0,1/2)\) | Three-region rational interval certificate executed; §2 and script | Stopped after complete coverage. |
| S4 | General balanced fibers plus supplied labels | Derive low-/high-noise coefficients | Expansions proved; exact \(\beta,W_1\) executed | Settled claimed coefficients. |
| S5 | Every 8-subset of \(Q_6\) | Exhaust all six cuts with total pair-distance cost \(\le48\) | Exact partition DP leaves only \((48,(4,4,4))\) | Exhaustive at the claimed bound; successor could seek a general analytic theorem. |

## Novelty and use

These derivations are new to this verifier. The supplied context does not establish whether they are new to the wider program, and I conducted no literature search, so I make no literature-novelty claim. Concrete uses are: an exact benchmark for implementations of the four stipulated line models; a certified ranking of the three formal labels under symmetric noise; and finite extremal tests that can screen proposed balanced labels. No historical use is established.

## 10. Machine-readable research registry (provisional phase 1)

| local claim ID | exact claim | evidence type | status | domain | contingency | dependencies | scope | prior claims | recommended next action |
|---|---|---|---|---|---|---|---|---|---|
| INV0006-P1-R1 | The complete V1 coin and standard-yarrow channel statements and numerical informations hold. | Exact derivation + executed finite arithmetic | confirmed | formal | definition-driven | stipulated independent line models | All of V1 | V1 | Audit original line table in phase 2. |
| INV0006-P1-R2U | Uniform-split model has \(P_6=77/1612\), \(P_9=5957/26832\), and \(P(X=1)=14565731/29112720\). | Executed exact rational DP | confirmed | formal | definition-driven | supplied split/remainder convention | The stipulated model only; no historical correspondence | V2 | Compare original recurrence and empty-heap handling. |
| INV0006-P1-R2B | Conditioned-binomial probabilities differ from \((1,5,7,3)/16\) by at most \(1.9476371583\times10^{-6}\). | Executed exact rational DP | confirmed-with-corrections | formal | definition-driven | supplied conditioned-binomial law | Refutes only a hard \(10^{-6}\) tolerance; confirms millionth order | V2 | Amend precision wording if hard tolerance was intended. |
| INV0006-P1-R3 | Assuming the stated Boolean-information premise, the V3 bound applies in both channel directions and a line attains it. | Exact conditional proof | confirmed | formal | definition-driven | V1 coin law; unproved stated premise | Does not prove the premise | V3, V1 | Audit that original result remained explicitly conditional. |
| INV0006-P1-R4 | For the supplied \(D\), \(I(T;Y)>I(B;Y)>I(G;Y)\) for every \(0<p<1/2\), with the stated \(p=1/4\) values. | Exact enumeration + executed rational interval certificate | confirmed | formal | definition-driven | supplied \(D\), BSC | Entire open parameter interval; endpoints intentionally excluded | V4 | Reimplement certificate independently or find analytic proof. |
| INV0006-P1-R5A | The small- and high-noise expansions in V5 hold for balanced labels with the stated \(\beta,W_1\) definitions. | Analytic entropy/Fourier derivation | confirmed | formal | definition-driven | balanced fibers, BSC | Asymptotic statements only | V5 | Compare normalization and remainder order with original proof. |
| INV0006-P1-R5B | \((\beta_T,\beta_B,\beta_G)=(3,4,6)\) and \((W_{1,T},W_{1,B},W_{1,G})=(3,13/8,0)\). | Executed exact edge/centroid enumeration | confirmed | formal | definition-driven | supplied \(D\) for \(B\) | Exact for these labels | V5 | Independently transcribe and recount \(D\). |
| INV0006-P1-R5C | Every 8-subset of \(Q_6\) has squared centroid norm at most 192, with equality exactly for coordinate 3-subcubes; balanced labels satisfy \(\beta\ge3,W_1\le3\), attained by coordinate-subcube partitions. | Analytic edge proof + executed exhaustive cut-DP | confirmed | formal | definition-driven | six-cube combinatorics | Exact for 8-subsets/balanced 8-valued labels | V5 | Seek general analytic centroid theorem or independently audit DP. |

---

**Phase-1 stopping point.** No original evidence has been viewed. These verdicts are provisional pending the requested phase-2 audit.
