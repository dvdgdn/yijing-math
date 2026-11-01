---
id: ASN-0014
title: Independently verify the divination-channel and label-robustness claims
status: launched
role: verifier
context_mode: targeted
role_prompt: prompts/roles/verifier.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/briefs/ASN-0014-phase1.md]
materials_part2: [investigations/INV-0004-divination-information-bounds/output.md, investigations/INV-0004-divination-information-bounds/results.json, compute/experiments/INV-0004/divination_information.py, investigations/library/openai-math-4eaee875/sources/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex]
claims: [C-0032, C-0033, C-0034, C-0035, C-0036]
purpose: verification
directions: [DIR-006]
questions: []
work_items: [divination-information-verification]
prerequisites: []
intentional_overlap: []
recommended_model: GPT-6.1 Sol Max (different family from the originator); isolated session with code execution
excluded_models: [Claude]
replication_of: INV-0004
investigations: [INV-0006]
created: 2026-10-31
---
# ASN-0014: Verify divination-channel and label-robustness claims

## Rationale (coordinator only)

- INV-0004 (Claude, context-exposed) is the first investigation in DIR-006. It settles INV-0003's open all-noise question with a computer-assisted proof (C-0035) and identifies the coins model with the symmetric channel at 1/4 (C-0032). Both are load-bearing for any later work on information through change, so a different-family isolated check is the cheapest way to make them usable.
- GPT family is the different family from the originator. Note the shared lineage for C-0034 only: the imported theorem comes from an unnamed OpenAI model. The verifier checks the transfer, not the theorem.
- Not included: C-0037 and C-0038 (conjectures; nothing to verify beyond the recorded searches); historical correspondence of the models (ASN-0007).
- Distinct from ASN-0013 (Claude verifies INV-0003). No overlap with ASN-0004: that blind run must not see this brief or its results before its own output is frozen.
- Decision: can C-0032–C-0036 be relied on by later assisted work? End after verdicts.

## Completion criteria (coordinator only)

- Phase 1 frozen before phase 2. Own derivations and code for V1–V5.
- Separate verdicts: formal correctness, numerical support (including whether the grid argument's floating-point assumption is acceptable), external applicability for V3.
- Any correction is registered as a new claim; nothing in INV-0004 is edited.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Independent Verification of Divination-Channel Claims

Independently check the five reported claims in the supplied brief. They concern explicit probability models and formal labels, not historical facts about any procedure or table.

Use your own arguments and implementation. For V4, a numerical evaluation at sample points is not a proof for all p; either supply a complete argument (analytic, or computer-assisted with explicit error control) or state exactly what your evidence covers. For V3, check that the premise's hypotheses hold exactly for the stated model; you are not asked to prove the premise. For V5, check both the expansions and the extremal statements; say which parts you proved and which you accepted from cited classical results.

**Phase 1 deliverables.** Provisional verdicts for V1–V5 with derivations, code and stated precision; executed versus described computations distinguished. Do not seek the original report or code.

Stop after phase 1 and wait for the original evidence.
<!-- END ASSIGNMENT -->

<!-- BEGIN ASSIGNMENT PART 2 -->
# Phase 2: Audit the Original Evidence

Your phase-1 verdicts are fixed. Compare them with the supplied report, output and code. Explain discrepancies. Audit the computer-assisted argument for V4 region by region: the analytic bounds near p = 0 and p = 1/2, the monotonicity argument, the grid and its numerical margin. Check the exact source statement used for V3.

Give a final verdict table distinguishing formal correctness, numerical support and external applicability. Do not give historical verdicts.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT PART 2 -->
