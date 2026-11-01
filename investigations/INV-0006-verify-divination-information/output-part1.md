Phase 1 is complete. I did not inspect any original proof, evidence, or code.

| Claim | Provisional verdict | Key finding |
|---|---|---|
| V1 | `confirmed` | All distributions and information values agree exactly. |
| V2 | `ill-posed` | Exact fractions agree, but “within \(10^{-6}\)” is false; maximum error is \(1.9476371583\times10^{-6}\). |
| V3 | `confirmed` (conditional) | Premise applies exactly in both channel directions; the premise itself remains assumed. |
| V4 | `confirmed` | Rational interval certificate proves both strict inequalities for every \(0<p<1/2\). |
| V5 | `confirmed` | Both expansions, all coefficients, and both extremal results were proved or exhaustively certified. |

Deliverables:

- [Full phase-1 report](/private/tmp/yijing-research-20261101/INV-0006/ASN-0014-phase1-report.md:1)
- [Complete verification code](/private/tmp/yijing-research-20261101/INV-0006/phase1_verify.py:1)

The verifier executed successfully using only Python’s standard library. I have stopped before phase 2 and await the original reasoning and evidence.