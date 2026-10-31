# State of Knowledge — Ledger v0.1

**Full-context document.** Never include this file, or anything derived from it, in a minimal-context package.

This is a one-page orientation. The records in `claims/` are authoritative; this page only summarizes them.

## Headline

- **Nothing in the ledger has been independently verified.** All 26 claims are `reported`, from a single investigation (INV-0001, Claude Opus 5.5).
- The second existing investigation (INV-0002, GPT-6.1 Sol Max) is **not in the repository**. Topics the setup brief attributes to the existing investigations but which INV-0001 does not cover (automata-theoretic quotients, noncommutation, reconstruction limits) are recorded as directions with absent sources (DIR-001 to DIR-003), not as claims.
- No cross-investigation agreements or contradictions can be assessed until a second investigation is registered.

## What INV-0001 reports (all unverified)

**Formal results** (definition-driven; true of the constructions as defined):
- A reversal-else-complement map σ is a fixed-point-free involution (C-0001).
- The nuclear map N is linear, commutes with R and C, and every hexagram reaches a four-element period-2 subspace A within two steps (C-0007, C-0008). A is also characterized by line-position extremes (C-0012).
- The palace difference set D is a transversal of the doubled-trigram subspace P, so the palaces partition the 64 hexagrams with one hexagram of each "trigram difference" per palace (C-0016). Reversal swaps generations 1↔5 and 2↔4 (C-0019). INV-0001 calls the transversal result its strongest.

**Source-dependent observations** (depend on transcriptions and encodings of attested material):
- The received order's 32 pairs are the orbits of σ (C-0002).
- Each canon contains 18 R-orbits (C-0003), which arithmetically fixes the 30/34 cut given three palindrome pairs in the upper canon (C-0004). Doubled trigrams split between canons by trigram symmetry (C-0006).
- A = hexagrams {1, 2, 63, 64}, the first and last pairs (C-0009).
- D encodes the Jing Fang procedure and reproduces palace tables and a traditional generation mnemonic (C-0017, C-0018). Cited sources for the tables and mnemonic are absent.

**Statistical results** (all under one pair-shuffling null model, which INV-0001 calls its weakest assumption):
- Endpoint placement of A has probability about 0.0021 (C-0010). This is post hoc.
- Canon balance is not rare, about 22% (C-0005). The order does not track N beyond the endpoints (C-0011). Absence of distance-5 transitions is not significant after multiplicity (C-0015).

**Negative result:** a proposed unification ("every traditional structure is ⟨R, C⟩-equivariant") is refuted by the palace system (C-0021). This refutes that formulation only.

**Conjectures and hypotheses:** stratification of R-symmetry by historical layer (C-0022, which depends on C-0023 and on unargued dating assumptions); generalization to 2k lines (C-0020, ill-posed); competing hypotheses H2 and H0 about structure beyond the pairing (C-0024, C-0025).

## Live disputes

- DSP-001: what explains the endpoint placement (nuclear dynamics, line-position extremes, chance, other)?
- DSP-002: is the received order structured beyond its pairing?
- DSP-003: is the R-symmetry split a historical stratification or an artifact?

## Largest gaps

1. No independent verification of anything (verification backlog priority 1: palace cluster and pairing).
2. The missing GPT-6.1 Sol Max report.
3. No cited data: every source-dependent claim rests on uncited transcriptions.
4. A single encoding (binary vectors, bottom to top) used throughout; representation-dependence largely unexamined (DIR-009).
5. Whole layers untouched: divination procedures (DIR-006), text (DIR-007), other arrangements (DIR-005), other Han systems (DIR-008).
