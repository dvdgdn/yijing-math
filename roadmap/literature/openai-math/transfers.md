# OpenAI mathematics → Yijing: transfer review and priorities

**Full-context coordinator material.** This is a source-based research plan with reported pilot results, not a list of verified discoveries. It supersedes the launch-order suggestion in `roadmap/coordination-review.md` for the manuscript-assisted track; it does not erase that review or the independent-exploration track.

## What was actually examined

Pinned upstream repository: [openai/math at 4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae), retrieved 2026-10-31. Its [README](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/README.md) calls the material raw research data at different verification stages. This snapshot has **721 manuscripts, 373 families**, not 722. Family numbering has gaps; family number 378 does not mean 378 active families.

- [catalogue.json](catalogue.json): all 721 titles and abstracts, pinned links, retrieval tags, and explicit per-paper review levels. All entries received automated retrieval screening; unreviewed entries are not declared irrelevant.
- [screening.json](screening.json): reproducible retrieval rules and the 16 theorem-level selections from 11 families. These are qualitative source/application judgments, not invented numerical scores.
- [snapshot.json](snapshot.json): cached-source paths and hashes. The complete index, selected source text and relevant formalization-scope documents are preserved and frozen under `investigations/library/`.
- [INV-0003](../../../investigations/INV-0003-corpus-transfer-audit/output.md): proofs of transfer reductions and finite obstructions, complete computational report, limitations and local claim registry. [Numerical output](../../../investigations/INV-0003-corpus-transfer-audit/pilot-results.json) and [executed code](../../../compute/experiments/INV-0003/corpus_pilots.py).

Full proofs of the selected manuscripts were not audited and Lean was not run. A cached source is not necessarily read in full. A family-level Lean link does not mean every companion statement is formalized. All papers come from the same unnamed model lineage, with possible internal dependencies; 721 papers are not 721 independent confirmations.

## Priority 1: Which structural observables preserve information under change?

**External result.** Family 119, [Sharp binary-information contraction on the discrete cube](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf), Corollary `main:ck`: for uniform independent bits X and independent symmetric crossover p, every Boolean summary satisfies I(f(X);Y)≤1−h₂(p); a coordinate attains the bound. Its output-bias refinement remains a uniform-input theorem. The companion Hellinger theorem supplies another contraction functional. The [formalization scope](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/119.md) was inspected; the formal proof was not checked here.

**Concrete bridge.** For X=(L,U), the three trigram-difference bits G=L xor U pass through independent noise q=2p(1−p). The other part of Y is independent nuisance information about G. Thus the external theorem bounds **all** Boolean summaries g(G), including nonlinear ones, by 1−h₂(q). This applies to 2k lines for every k if the source theorem is accepted. It provides an explicit global benchmark against which a proposed summary can be compared.

**Finite evidence already obtained.** Exhaustive evaluation of all 256 functions of G at p=1/8 and p=1/4 reproduces that optimum in the six-line case. For the mathematical palace encoding, the base label B and difference/generation label G are independent uniform three-bit labels. At p=1/4:

| Observable | Output entropy | Retained information about the noisy full hexagram |
|---|---|---|
| Raw lower trigram | 3 bits | approximately 0.566166 bits |
| Palace base label B | 3 bits | approximately 0.378621 bits |
| Trigram-difference/generation label G | 3 bits | approximately 0.136698 bits |

The comparison is invariant under renaming the eight output labels. It does not treat a three-bit label as if it were one Boolean output: the source theorem applies to each one-bit summary of G; the full-label numbers are computed separately. The raw-trigram control prevents a misleading claim that the traditional-looking label is globally optimal.

**Failed proof route already retained.** An exact p=1/8 posterior example rules out universal pointwise majorization as a sufficient argument for the proposed all-noise comparison. The average-information question remains open. The [supplement](../../../investigations/INV-0003-corpus-transfer-audit/additional-attempt.md) and targeted brief preserve this scope so the next investigator can use a different route.

**What could be discovered.** A classification of robustness under specified symmetries and change mechanisms; an all-noise comparison or a counterexample; exact costs of insisting on a particular quotient; sensitivity to swapping representation, source procedure, or input prior. An informative negative outcome would be that an apparent advantage disappears under an equally justified model. These questions concern mathematical utility and information loss without presuming divinatory efficacy or historical intention.

**First work package:** [ASN-0010](../../assignments/ASN-0010-information-preserving-observables.md). The exact pilot and conditional reduction are ready for [ASN-0013](../../assignments/ASN-0013-verify-corpus-bridges.md). C-0017 and cited procedure work in ASN-0007 remain separate prerequisites for historical applications. ASN-0004 stays blind so its discoveries can be compared with the literature-assisted framing afterward.

**Stop/revise condition.** If only routine restatements survive, or robustness is entirely determined by an arbitrary observable choice, report that limitation and move to a sharper constrained question. Do not count the application of a known theorem as literature novelty without searching the actual application statement.

## Priority 2: Can apparent structure survive the right conditional comparison?

**External results.** Family 115 supplies [exact uniform sampling of integer tables with arbitrary margins](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf), Theorem `thm:main`, and [approximate counting with individual cell bounds](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf), Theorem `thm:main`. Both dimensions vary and capacities are binary encoded. The first has no forbidden cells. The second includes structural zeros but is a counting theorem. Do not assume it directly provides an implemented bounded-table sampler.

**Concrete bridge.** Allocation tables for source-supported categories, canon positions, or textual features can preserve specified margins while varying the association under study. A precise encoding can make a conditional ensemble tractable without destroying features that were not free to vary. This is relevant to Q-004, the explanatory disputes and the textual pilot.

**Finite evidence already obtained.** Three tables with margins (2,2) have probabilities (1/3,1/3,1/3) under a uniform-table law and (1/6,2/3,1/6) under uniformly labelled allocations. The extreme-event probability changes from 2/3 to 1/3. An exact sampler for the wrong law would give a precisely wrong test.

**What could be discovered.** Which received-order or textual associations carry information beyond simpler preserved constraints; which alleged surprises are forced by margins or multiplicity; a discriminating statistic whose interpretation survives several explicitly justified ensembles. No current historical association or p-value is established by the toy computation.

**First work package:** [ASN-0011](../../assignments/ASN-0011-conditional-comparison-ensembles.md). Build finite exact reference cases before implementing a large new algorithm. Deliver a model and an unbiased/error-controlled reference calculation to ASN-0005, which retains responsibility for its explanation-test plan. Source acquisition remains ASN-0007's work. The source theorem offers a scaling route, not a delivered practical speed-up; run-time constants and code remain to be assessed.

**Supporting but conditional:** families 113 and 131. Matchings are relevant only when the constraints really encode a matching problem. Degree-preserving graph switches require simple undirected graphs with a fixed labelled degree sequence, not arbitrary directed transformation graphs or constrained orderings. The explicit family-131 mixing bound is 2n⁸ steps: at n=64 this is 562,949,953,421,312 steps for TV≤1/4, not a practical short burn-in guarantee.

**Pilot-driven demotion.** The graph allowing reversal or complement edges on 64 words has only 4,096 perfect matchings and an exact component decomposition. Family 113's pointwise entropy estimate gives the loose interval [−22.5,24] bits, whereas the exact uniform entropy is 12 bits. Use exact factorization here; reopen the imported general algorithms only for a genuinely harder compatibility graph.

**Stop/revise condition.** If the target law cannot be encoded without deleting a relevant constraint, the imported theorem does not apply. If exact finite methods already settle the problem, prefer them. If all discrimination is based on previously selected patterns, report sensitivity/descriptive results rather than retroactive confirmation.

## Priority 3: Do local changes constrain a whole ordering in detectable ways?

**External result.** Family 238, [Optimal-order mixing of the Thorp shuffle](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/paper.pdf), Theorem `thm:mixing` and §2. Positions are binary words; a physical step is a matching of independent swaps followed by a cyclic coordinate rotation. In the moving frame, a sweep visits each coordinate. The asymptotic full-permutation mixing result is stronger than the already elementary fact that individual labels become uniform.

**Concrete bridge and finite evidence.** On 64 positions a six-direction sweep makes every individual label exactly uniform. Yet it uses only 192 fair bits, implying full-order TV distance at least 1−2¹⁹²/64!, greater than 1−5×10⁻³². Therefore local or one-object statistics can miss almost all remaining dependence in an order. This finite consequence is already established as a reported result with a short argument and exact marginal checks.

**What could be discovered.** Low-depth constraints in locally generated arrangements, information retained in joint relations after simple marginals wash out, and consequences separating short local mechanisms from arbitrary permutation models. Fix operations and a description budget before fitting an attested arrangement. Coordinate switches generate the whole symmetric group, so eventual generatability is not an explanation.

**First work package:** [ASN-0012](../../assignments/ASN-0012-local-permutation-structure.md). Start with exact small-dimensional transition laws and joint statistics, then apply to cited arrangements. Never assume that an arbitrary proposed transformation is historically attested.

**Finite-size gate.** The principal upper bound is asymptotic; 1600d does not certify mixing at d=6. The regular-trace companion has an all-dyadic statement with an unspecified absolute moment in its theorem. Extract an effective constant if it is needed, or use a different certified finite calculation. Do not replace this with “we ran enough sweeps.”

## Further transfers, safeguards, and deferred routes

| Family | Exact result inspected or catalogue lead | Current judgment and reopening trigger |
|---|---|---|
| 134 | Generalized star height ≤3 for every regular language, allowing complement; theorem has no expression-size bound | Useful guardrail for DIR-001/DIR-010: a few repetition levels are not evidence of special Yijing structure. Promote only if a size/prediction advantage over generic finite automata is shown. |
| 206 | Finite-lattice representability and general undecidability | No direct conclusion about the explicit congruences of a fixed 64-state operator algebra. Reopen with a concrete representation problem and a finite, useful consequence. |
| 161 | A 35-vertex bipartite pattern fails Sidorenko/forcing | Guardrail: selected motif densities do not automatically characterize randomness. No claim that its specific counterexample is a Yijing graph. Reopen when a meaningful graph model and test vocabulary exist. |
| 076 | Real-sign ultraflat polynomials for sufficiently large lengths | Direct transfer fails for balanced nonzero characters on a full 64-word enumeration, whose polynomial vanishes at 1. Reopen for a punctured spectrum, another observable class, or a different question. |
| 179 | Circulant Hadamard/Barker nonexistence beyond specified orders | Provides a general ceiling, but the new contribution at dyadic length 64 must be compared with older elementary obstructions. Do not allocate a major run merely to restate nonexistence. |
| 122 | Uniform reconstruction from independent deletion traces with known channel | Historical witnesses are not established as iid traces of one original. Reopen only after a justified loss/transmission model; otherwise treat this as an explicitly artificial benchmark. |
| 127 (catalogue-level) | Influence ≤8d√n for degree-d threshold functions | At n=6 this exceeds the elementary bound n for every d≥1. No finite improvement established. Reopen for a justified parameterized family with nonvacuous constants. |
| 229 (catalogue-level) | Three/four-state broadcasting thresholds on trees | Four line values alone do not supply a broadcast tree, the required symmetry, or a ferromagnetic channel. Reopen if a source-grounded transition model meets those hypotheses. |
| 266 / 225 (catalogue-level) | Dimension-six quantum bases / six-vertex lattice models | “Six” denotes different mathematical objects. No applicable map was found; avoid a number-based analogy. A nontrivial map with preserved relations could reopen either route. |
| 378 (catalogue-level) | Fixed-width counting algorithms refuting ETH | The tiny finite cases here do not require asymptotic worst-case acceleration. Keep as a scaling lead only if a genuine bottleneck and implementation advantage are demonstrated. |
| Remaining catalogue | Searchable title/abstract records, including many results in distant disciplines | Unreviewed, not disproved or permanently excluded. Rescreen when a new object/question, credible bridge, or source revision changes relevance. |

## Execute as a coordinated programme

1. **Reconcile the local pilot.** INV-0003 is completed and context-exposed; registration is pending. Assign its local claims to independent audit without treating it as source verification or novelty certification.
2. **Launch small, complementary assisted work.** First choose ASN-0010 plus independent ASN-0013, with source work ASN-0007 alongside where capacity allows. ASN-0011 is the next methodological package. ASN-0012 is a bounded distinct modelling branch. All newly prepared assignments remain draft pending the coordinator's launch decision.
3. **Retain unassisted discovery.** ASN-0004 and the reset ASN-0006 receive no corpus map or pilot findings. Compare reports afterward to separate literature-enabled advances from rediscovery or common framing. This is purposeful context diversity, not a second attempt at the same declared deliverable.
4. **Resolve the evidence base.** ASN-0001's palace/source verification and recovery of INV-0002 remain valuable. The corpus does not remove a missing transcription or historical ambiguity. Mathematical development may proceed conditionally while those source questions remain explicit.
5. **Close the handoff.** Each assisted result states its exact imported lemma, hypotheses, application map, contribution beyond the lemma, finite tests, negative scope, and next discriminating consequence. Search prior art for both the imported theorem and the new application. Ask for a prediction, classification, useful construction or informative obstruction, not another catalogue of analogies.
6. **Update by decision, not volume.** Reconcile after the first assisted/audit pair before launching every candidate. Promote routes that yield checkable consequences or eliminate an important ambiguity. Stop or reformulate routes whose transfer is vacuous, generic, wrong-domain, or already known with no useful extension.

Canonical import and coordination procedures are in [standards.md](../../../methods/standards.md) and [research-cycle.md](../../../methods/research-cycle.md). This review supplies findings and current choices, not a parallel specification of the programme.
