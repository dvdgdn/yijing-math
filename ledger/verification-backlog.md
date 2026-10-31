# Verification Backlog

Claims awaiting independent verification, in priority order. Priority weighs the claim's value, the number of claims depending on it, and how cheaply it can be checked. **No claim in the ledger has been independently verified as of v0.1.**

Every claim currently registered was originated by Claude Opus 5.5 (INV-0001). Under the rules in `methods/ledger-conventions.md` §3.2, verification that yields `verified` must come from a different model family (initially GPT-6.1 Sol Max) or a qualified human.

| Priority | Claims | What needs checking | Assignment | Prerequisites |
|---|---|---|---|---|
| 1 | C-0016, C-0017, C-0018, C-0019 | Palace transversal theorem; correctness of the encoding D against the source procedure; agreement with a palace table and with the mnemonic; reversal law and its prediction for all 28 reversal pairs. Strongest result of INV-0001. | ASN-0001 | Verifier's own transcription of a palace table; ideally a cited table (data task D-2). |
| 1 | C-0002 | Pairing of the received order by σ. Foundation for C-0003, C-0004, C-0013, C-0024. | ASN-0001 | Verifier's own transcription of the received order. |
| 2 | C-0026 | Label-swap invariance, checked result by result. | ASN-0001 and ASN-0002 | — |
| 2 | C-0003, C-0006, C-0009, C-0014 | Source-dependent observations about the received order. | ASN-0002 | Transcription of the received order. |
| 2 | C-0005, C-0010, C-0011, C-0015 | Statistical claims: exact recomputation under precisely stated null models; ambiguities in statistic definitions; multiplicity. | ASN-0002 | — |
| 3 | C-0007, C-0008, C-0012, C-0013 | Formal facts about N, A, and Hamming distance. Routine. | ASN-0002 | — |
| 3 | C-0021 | Refutation of the "ambitious conjecture". Depends on C-0017 and C-0019. | after ASN-0001 | ASN-0001 results. |
| 4 | C-0001, C-0004 | Short formal arguments. Check in passing. | ASN-0001 / ASN-0002 | — |
| — | C-0020 | Ill-posed until the generalized nuclear map is specified. Needs specification work, not verification. | none yet (Q-005) | — |
| — | C-0022, C-0023 | Historical and source claims. Need cited historical sources, not mathematical verification. | none yet (Q-001, data task D-3) | Cited transcriptions. |
| — | C-0024, C-0025 | Competing hypotheses. Tested, not verified. | ASN-0005 | — |

## Data prerequisites

Several verifications depend on transcriptions of historical arrangements. Until the cited datasets described in `data/README.md` exist, verifiers use their own transcriptions and include them in full in their reports. The registrar then compares transcriptions across investigations. Disagreements between transcriptions are themselves recorded findings.
