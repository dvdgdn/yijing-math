---
id: ASN-0002
title: Verify the nuclear-map, canon-structure, and statistical claims
status: ready
role: verifier
context_mode: targeted
role_prompt: prompts/roles/verifier.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md, context/briefs/ASN-0002-phase1.md]
materials_part2: [investigations/prompts/yijing_paradigm_transcendence/claude_opus_5_5.md, ledger/claims/C-0003.md, ledger/claims/C-0004.md, ledger/claims/C-0005.md, ledger/claims/C-0006.md, ledger/claims/C-0007.md, ledger/claims/C-0008.md, ledger/claims/C-0009.md, ledger/claims/C-0010.md, ledger/claims/C-0011.md, ledger/claims/C-0012.md, ledger/claims/C-0013.md, ledger/claims/C-0014.md, ledger/claims/C-0015.md, ledger/claims/C-0026.md]
claims: [C-0003, C-0004, C-0005, C-0006, C-0007, C-0008, C-0009, C-0010, C-0011, C-0012, C-0013, C-0014, C-0015, C-0026]
recommended_model: GPT-6.1 Sol Max
excluded_models: [Claude Opus 5.5]
replication_of: none
investigations: []
purpose: verification
directions: [DIR-004, DIR-010]
questions: [Q-007]
work_items: [received-order-transcription, nuclear-formal-audit, received-statistics-audit, label-swap-audit]
prerequisites: []
intentional_overlap: [ASN-0001, ASN-0005, ASN-0007, ASN-0008]
created: 2026-10-31
---
# ASN-0002: Verify the nuclear-map, canon-structure, and statistical claims

## Rationale (coordinator only)

- **Intentional overlap:** ASN-0001 independently transcribes the received order and checks C-0026 on a different subset. ASN-0005 studies explanation sensitivity while this assignment audits reported values; do not execute its planned new tests here. ASN-0007 supplies a separately sourced baseline for comparison after phase 1. ASN-0008 audits prior art for overlapping claims. These outputs answer different questions and must be registered separately.

- Clears most of the remaining verification backlog (priorities 2 and 3) in one assignment. The claims share a transcription of the received order and the pair-shuffling null model.
- The statistical claims (C-0005, C-0010, C-0011, C-0015) have unstated methods and ambiguous statistics. Exact recomputation under precisely stated models is needed before DSP-001 and DSP-002 can be assessed.
- Also answers Q-007 (how much of C-0006 is implied by C-0002 to C-0004).
- **Model:** GPT-6.1 Sol Max, for the same reason as ASN-0001. Run in a **separate session** from ASN-0001 so that each verification is self-contained.
- *Alternatives considered:* splitting formal claims (C-0007, C-0008, C-0012, C-0013) into a separate low-priority assignment (rejected: they are quick and share definitions); waiting for ASN-0005 (rejected: ASN-0005 tests explanations, while this checks the reported numbers, and both are needed).

## Completion criteria (coordinator only)

- Verdicts for all 14 claims; exact values or Monte Carlo estimates with uncertainty for every probability; each ambiguity resolved by giving verdicts under each reading.
- A transcription of the received order to compare with ASN-0001's.
- On registration: update statuses and verification logs; register corrected values as superseding claims; update DSP-001, DSP-002, Q-007.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Verification of Reported Results on the Nuclear Map, the Canons, and Related Statistics

You are assigned to verify a set of claims reported by an earlier investigation in this program. They concern the nuclear-hexagram map, the division of the received (King Wen) order into two canons, Hamming distances in the order, and several statistical assessments under a random-arrangement null model. The claims and the definitions they use are listed under "Supplied materials".

You have been given selected material from earlier investigations in this program. Each prior finding carries a verification status; all the claims supplied to you are "reported", that is, unverified. You are not required to accept their representations or conclusions.

The verification has two phases. **In this phase you have the claims' statements and definitions only.** Derive or refute each claim independently, record a provisional verdict for each, and then stop. You will then receive the original reasoning and evidence for audit.

For the statistical claims, state the null model and the statistic exactly as you implement them. Where the claim is ambiguous, give a verdict under each reasonable reading. Prefer exact computation of probabilities. Report Monte Carlo results with sample size, seed, and uncertainty.

**Deliverables (phase 1).** For each claim: a precise restatement, your own derivation or computation (with code, stating whether it was executed), and a provisional verdict. A full transcription of the received order you used, with its source.

**Useful completion (phase 1).** Every claim has a provisional verdict with reasons, and every probability has an exact value or an estimate with stated uncertainty.

Stop after phase 1 and wait for the next message.
<!-- END ASSIGNMENT -->

<!-- BEGIN ASSIGNMENT PART 2 -->
# Phase 2: Audit

Your phase 1 verdicts are now on record. You now have the original report from which the claims were extracted, and the program's ledger records for each claim. The ledger records include notes flagging specific points to check. Those notes are not findings.

Audit each claim as described in your role instructions. Compare the original reasoning with your own derivation and explain any differences. Give particular attention to how the original defined its statistics and null model, and whether its significance assessments account for the number of patterns examined. The original report contains other results that are not assigned to you. You may comment briefly on errors you notice in them, but verdicts are required only for the assigned claims.

**Deliverables (phase 2).** The verdict table (claim; mathematical correctness; source correspondence; significance claims; one-line reason), detailed audit notes, and a final report following the research handoff protocol, including any new claims, corrections, objections, or questions.

**Useful completion.** Every assigned claim has a final verdict on each applicable aspect, with a statement of exactly what was checked, and any disagreement between your phase 1 derivation and the original is explained.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT PART 2 -->
