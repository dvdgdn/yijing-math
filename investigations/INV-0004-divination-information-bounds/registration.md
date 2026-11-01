# INV-0004 — Registration

Registrar: Claude Opus 5.5 (the originator), 2026-10-31. **Self-registration; a human or GPT-family coordinator should review the extraction.**
Original output: `output.md` §3 (R1–R8), with `results.json`. Never edit either.

## Local results to ledger

| Local result | Exact statement and assumptions | Related existing record | Ledger ID and action | Evidence and verification limits |
|---|---|---|---|---|
| R1 | Procedure models → line channels; coins = symmetric channel 1/4 with independent change mask; yarrow-standard asymmetric (3/8, 1/8) | C-0027, C-0028 (identifies their p = 1/4 channel) | C-0032, new reported | exact; source correspondence unverified |
| R2 | Yarrow probabilities depend on the split model | — | C-0033, new reported | exact; idealized split laws |
| R3 | Coin-model one-bit bound and bias refinement | C-0027 (same imported theorem) | C-0034, new reported | conditional on external family 119 |
| R4 | T > B > G for every 0 < p < 1/2 | C-0028 (two-point case); C-0016 (structure of D) | C-0035, new reported | computer-assisted proof with binary64 logarithms |
| R5 | Endpoint rates; subcube optimality; generation worst case | C-0035 | C-0036, new reported | expansions, exact maximization, cited edge isoperimetry |
| R6 | Trigram optimal among balanced 3-bit labels for all p | external conjecture (arXiv:2609.26444) | C-0037, new conjecture; Q-009 | local evidence only |
| R7 | Single lines optimal under yarrow channels | C-0034 | C-0038, new conjecture; Q-010 | exhaustive n ≤ 4, local n = 6 |
| R8 | INV-0003 L1–L6 recomputed; no error | C-0027–C-0031 | verification-log notes; no status change | context-exposed, not a protocol verification |

Also added: DEF-017 (procedure models), DEF-018 (labels), DEF-019 (robustness rates); Q-011 (split model); DIR-006 status updated.

## Considered and not registered

| Location | Result or idea | Reason / future use |
|---|---|---|
| R3 table | Values for nine individual questions | Kept as data in `results.json`; not separate claims |
| §4 | Correspondence (應) reading of G; line 6 fixed in palaces; coins used with palaces in practice | Source-dependent general knowledge; registrar note on DEF-018; ASN-0007/ASN-0008 |
| §6 | Yarrow-channel label values (T 0.6163, B 0.4159, G 0.1570) | Numerical data only; the ordering under asymmetric noise is not proved |

## Attempt map

As in `output.md` §6. The scratch probes (six channels at n ≤ 4; one short partition search) are recorded there, not preserved as files.

## Attribution, novelty and shared inputs

- R3 rests on an external theorem from an unnamed OpenAI model (family 119). A separate preprint claims the same theorem; neither is audited.
- R4–R5 use classical tools (data processing, Fano, edge isoperimetry, Fourier expansion) and need no corpus result.
- R6 is an instance of a published conjecture.
- Novelty of R1, R2, R4, R5 and R7 is unknown (searches in `output.md` §7).
- Context exposure: full, including INV-0001 (same family) and INV-0003.

## Dependency and disagreement review

- C-0035 depends on C-0016 only through the stated set D, which is checkable by computation. It does not depend on C-0017.
- If ASN-0001 corrects D, C-0035 still holds for the D as defined and would need a dated note.
- No disagreement with any registered record.
- C-0027 and C-0028 gain a dated note that their channel at p = 1/4 is the coins model.

## Coverage and next selection

- DIR-006 is now lightly explored in the assisted lane. ASN-0004 remains a deliberately blind comparison.
- INV-0003's open all-noise question (ASN-0010's first option) is settled by C-0035, and ASN-0010's asymmetric option is partly addressed by C-0038 and R1. ASN-0010 is withdrawn.
- Verification of C-0032–C-0036 goes to the new ASN-0014 (GPT family, two-phase, isolated). C-0037 and C-0038 are open problems for an optional specialist in cycle 2.
