---
id: ASN-0001
title: Verify the received-pairing claim and the palace-system cluster
status: ready
role: verifier
context_mode: targeted
role_prompt: prompts/roles/verifier.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v2.md
materials: [context/objects/hexagrams.md, context/briefs/ASN-0001-phase1.md]
materials_part2: [investigations/prompts/yijing_paradigm_transcendence/claude_opus_5_5.md, ledger/claims/C-0001.md, ledger/claims/C-0002.md, ledger/claims/C-0016.md, ledger/claims/C-0017.md, ledger/claims/C-0018.md, ledger/claims/C-0019.md, ledger/claims/C-0026.md]
claims: [C-0001, C-0002, C-0016, C-0017, C-0018, C-0019, C-0026]
recommended_model: GPT-6.1 Sol Max
excluded_models: [Claude Opus 5.5]
replication_of: none
investigations: []
created: 2026-10-31
---
# ASN-0001: Verify the received-pairing claim and the palace-system cluster

## Rationale (coordinator only)

- C-0016 to C-0019 are the result INV-0001 calls its strongest. Three of them (C-0016, C-0017, C-0018) are rated `value: high`, and the cluster is the basis of the refutation C-0021 and the stratification conjecture C-0022.
- C-0002 underlies C-0003, C-0004, C-0013 and C-0024. Checking it alongside the palace cluster is cheap.
- The source correspondence (C-0017, C-0018) is the weakest link: no palace table or mnemonic source was cited. A verifier from a different model family with its own transcription tests that directly.
- **Model:** GPT-6.1 Sol Max, because every claim was originated by Claude Opus 5.5. A Claude verification would yield at most `reproduced`.
- **Two-phase** so the verifier derives the claims before seeing INV-0001's arguments.
- *Alternatives considered:* verifying all 26 claims in one assignment (rejected: too diffuse, and phase-1 independence is harder to keep across many claims); verifying the palace cluster only (rejected: C-0002 is cheap and foundational).

## Completion criteria (coordinator only)

- Final verdict table for all seven claims, with the three aspects separated where they apply.
- Full transcriptions of the received order and the palace table, so they can be compared with other transcriptions and later with a cited source.
- On registration: add the investigation to each claim's `verifiers` and set status per `methods/ledger-conventions.md` §3.2. Register corrections as new superseding claims. Record any transcription disagreement as a finding.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Verification of Reported Results on the Received Pairing and the Palace System

You are assigned to verify a set of claims reported by an earlier investigation in this program. One concerns how the received (King Wen) order pairs hexagrams. The others concern the eight-palace system attributed to Jing Fang. The claims and the definitions they use are listed under "Supplied materials".

You have been given selected material from earlier investigations in this program. Each prior finding carries a verification status; all the claims supplied to you are "reported", that is, unverified. You are not required to accept their representations or conclusions.

The verification has two phases. **In this phase you have the claims' statements and definitions only.** Derive or refute each claim independently, record a provisional verdict for each, and then stop. You will then receive the original reasoning and evidence for audit.

Two of the claims concern whether a mathematical encoding matches the traditional palace procedure and tables. For these, rely on your own knowledge of the tradition, write out your transcription in full, and say where it comes from. If you know of variant palace tables or variant descriptions of the procedure, list them and say whether each claim holds for each variant.

**Deliverables (phase 1).** For each claim: a precise restatement, your own derivation or computation (with code, stating whether it was executed), and a provisional verdict. Full transcriptions of the received order and of the palace tables you used.

**Useful completion (phase 1).** Every claim has a provisional verdict with reasons, and every transcription is complete.

Stop after phase 1 and wait for the next message.
<!-- END ASSIGNMENT -->

<!-- BEGIN ASSIGNMENT PART 2 -->
# Phase 2: Audit

Your phase 1 verdicts are now on record. You now have the original report from which the claims were extracted, and the program's ledger records for each claim. The ledger records include notes flagging specific points to check. Those notes are not findings.

Audit each claim as described in your role instructions. Compare the original reasoning with your own derivation and explain any differences. Check the encoding of the palace procedure against the source tradition, and check whether each ledger record states what the original report says. The original report contains other results that are not assigned to you. You may comment briefly on errors you notice in them, but verdicts are required only for the assigned claims.

**Deliverables (phase 2).** The verdict table (claim; mathematical correctness; source correspondence; significance claims; one-line reason), detailed audit notes, and a final report following the research handoff protocol, including any new claims, corrections, objections, or questions.

**Useful completion.** Every assigned claim has a final verdict on each applicable aspect, with a statement of exactly what was checked, and any disagreement between your phase 1 derivation and the original is explained.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT PART 2 -->
