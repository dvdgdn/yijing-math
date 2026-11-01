# State of Knowledge — Ledger v0.3

**Full-context document.** Never include this file, or anything derived from it, in a minimal-context package.

This is a one-page orientation. The records in `claims/` are authoritative; this page only summarizes them.

## Headline

- **Nothing in the ledger has been independently verified.** All 41 claims are `reported`:
  - C-0001–C-0026 from INV-0001 (Claude Opus 5.5, legacy).
  - C-0027–C-0031 from INV-0003 (Codex, gpt family, full context).
  - C-0032–C-0038 from INV-0004 and C-0039–C-0041 from INV-0008 (both Claude Opus 5.5, full context).

  INV-0003, INV-0004 and INV-0008 are context-exposed.
- **Cited source data now exist** (INV-0008): the received order, the *Jingshi Yizhuan* palace table and procedure texts, from pinned Wikisource witnesses, unchecked against print. On them, the source-dependent statements of C-0002, C-0003, C-0004, C-0006, C-0009, C-0017(b) and C-0018 hold. This is a same-family recomputation, not a verification.
- The second existing investigation (INV-0002, GPT-6.1 Sol Max) is **not in the repository**. Topics the setup brief attributes to the existing investigations but which INV-0001 does not cover (automata-theoretic quotients, noncommutation, reconstruction limits) are recorded as directions with absent sources (DIR-001 to DIR-003), not as claims.
- INV-0004 recomputed INV-0003's finite claims with independent code and found no error. This is cross-family but context-exposed, so not a verification. No contradictions between investigations are recorded.

## What INV-0001 reports (all unverified)

**Formal results** (definition-driven; true of the constructions as defined):
- A reversal-else-complement map σ is a fixed-point-free involution (C-0001).
- The nuclear map N is linear, commutes with R and C, and every hexagram reaches a four-element period-2 subspace A within two steps (C-0007, C-0008). A is also characterized by line-position extremes (C-0012).
- The palace difference set D is a transversal of the doubled-trigram subspace P, so the palaces partition the 64 hexagrams with one hexagram of each "trigram difference" per palace (C-0016). Reversal swaps generations 1↔5 and 2↔4 (C-0019). INV-0001 calls the transversal result its strongest.

**Source-dependent observations** (depend on transcriptions and encodings of attested material):
- The received order's 32 pairs are the orbits of σ (C-0002).
- Each canon contains 18 R-orbits (C-0003), which arithmetically fixes the 30/34 cut given three palindrome pairs in the upper canon (C-0004). Doubled trigrams split between canons by trigram symmetry (C-0006).
- A = hexagrams {1, 2, 63, 64}, the first and last pairs (C-0009).
- D encodes the Jing Fang procedure and reproduces palace tables and a traditional generation mnemonic (C-0017, C-0018).
  - A cited palace table now exists, and D reproduces all 64 of its entries (C-0040; C-0017 log).
  - The procedure as the text narrates it (C-0017(a)) is unchecked.
  - The mnemonic's attestation is unknown (Q-008).

**Statistical results** (all under one pair-shuffling null model, which INV-0001 calls its weakest assumption):
- Endpoint placement of A has probability about 0.0021 (C-0010). This is post hoc.
- Canon balance is not rare, about 22% (C-0005). The order does not track N beyond the endpoints (C-0011). Absence of distance-5 transitions is not significant after multiplicity (C-0015).

**Negative result:** a proposed unification ("every traditional structure is ⟨R, C⟩-equivariant") is refuted by the palace system (C-0021). This refutes that formulation only.

**Conjectures and hypotheses:** stratification of R-symmetry by historical layer (C-0022, which depends on C-0023 and on unargued dating assumptions); generalization to 2k lines (C-0020, ill-posed); competing hypotheses H2 and H0 about structure beyond the pairing (C-0024, C-0025).

## What INV-0003 and INV-0004 report (all unverified)

**Manuscript transfers (INV-0003).**
- Binary summaries of the trigram difference reduce to noise 2p(1−p), with a conditional optimum (C-0027).
- Palace and generation labels differ in noise robustness at two noise values (C-0028).
- The reversal-or-complement graph has 4,096 perfect matchings (C-0029).
- A one-sweep coordinate shuffle gives uniform marginals but a far-from-uniform order (C-0030).
- A scoped negative spectral transfer (C-0031).

**Divination layer (INV-0004, literature-assisted).**
- The coins model is exactly the symmetric line-change channel at 1/4. The standard yarrow model is asymmetric (3/8, 1/8), and its moving lines reveal 0.374 bits about the primary hexagram (C-0032). Yarrow probabilities depend on how the stalks are split (C-0033).
- Under coins, no yes/no question carries more than 0.1887 bits from one hexagram to the other. This is conditional on external family 119 (C-0034).
- For every line-change probability, trigram > palace > generation in retained information, by a computer-assisted proof (C-0035). Trigram-type labels are optimal and the generation label worst possible at both noise extremes (C-0036).
- Two conjectures: the trigram is optimal at every noise level, an instance of a published conjecture (C-0037); single lines stay optimal under the yarrow asymmetry (C-0038).

## What INV-0008 reports (all unverified)

**Source attestations** (two digital witnesses each, unchecked against print):
- The *Xugua* introduces the hexagrams in the received order (C-0039).
- In the *Jingshi Yizhuan*, each palace is headed by a doubled trigram, and the world line it states follows the palace position (C-0040).
- Zhu Xi's 筮儀 counts its cases so that equal weighting gives the textbook yarrow law. It fixes the remainder and hung-stalk conventions but no split law (C-0041).

## Live disputes

- DSP-001: what explains the endpoint placement (nuclear dynamics, line-position extremes, chance, other)?
- DSP-002: is the received order structured beyond its pairing?
- DSP-003: is the R-symmetry split a historical stratification or an artifact?

## Largest gaps

1. No independent verification of anything (verification backlog priority 1: palace cluster and pairing).
2. The missing GPT-6.1 Sol Max report.
3. Cited data are only digital witnesses: no printed-edition check yet, and no Mawangdui, Chu or Shao Yong dataset.
4. A single encoding (binary vectors, bottom to top) used throughout; representation-dependence largely unexamined (DIR-009).
5. Layers untouched or barely touched: divination procedures (DIR-006, one assisted full-context investigation; reading rules and sources untouched), text (DIR-007), other arrangements (DIR-005), other Han systems (DIR-008).
