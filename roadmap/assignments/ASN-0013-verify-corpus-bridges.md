---
id: ASN-0013
title: Independently audit finite manuscript bridges and their applicability
status: draft
role: verifier
context_mode: targeted
role_prompt: prompts/roles/verifier.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md, context/briefs/ASN-0013-phase1.md]
materials_part2: [investigations/INV-0003-corpus-transfer-audit/output.md, investigations/INV-0003-corpus-transfer-audit/pilot-results.json, compute/experiments/INV-0003/corpus_pilots.py, investigations/library/openai-math-4eaee875/sources/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex, investigations/library/openai-math-4eaee875/sources/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex]
claims: []
purpose: verification
directions: [DIR-004, DIR-006, DIR-009, DIR-010]
questions: []
work_items: [corpus-bridge-finite-audit]
prerequisites: []
intentional_overlap: []
recommended_model: non-GPT family or qualified human; initially Claude Opus 5.5
excluded_models: [GPT]
replication_of: INV-0003
investigations: []
created: 2026-10-31
---
# ASN-0013: Verify corpus bridges

## Rationale (coordinator only)

- INV-0003 is context-exposed, GPT-family, and completed with registration pending. Independently verify the local consequences before building significance on them. The original 721 papers are not independently checked merely because the applications work.
- Scope is the formal statements L1–L6 and correct use of external hypotheses, not historical palace correspondence and not a complete proof audit of the imported global theorem. Conditional statements must remain conditional unless their premise is independently established.
- ASN-0010 extends the information result; ASN-0012 extends local-order consequences. This assignment audits their common starting pilot. ASN-0001 retains the existing palace/source audit. If rederiving C-0016, a Claude verifier is the same family as its original originator and cannot thereby promote that existing claim to verified.
- Preferred cross-family audit: Claude or a qualified human for this report's GPT-originated local findings. The unnamed external model's exact identity remains unknown. A different family alone is not sufficient; require isolation, own implementation, proof checks and separate applicability verdicts.
- Decision: which local bridges are safe to develop, which need correction, and what remains conditional? End after exact verdicts and corrections, not a fresh broad exploration.

## Completion criteria (coordinator only)

- Phase 1 recorded and frozen before phase 2; independent code or derivations for each finite claim; numerical entropy gaps preferably bounded with rigorous errors.
- Final verdicts distinguish formal correctness, external-theorem applicability, numerical evidence and historical scope. A source dependency not audited stays explicit.
- Register corrected claims or new objections without editing the frozen report. No global status may exceed the verification actually performed.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Independent Audit of Manuscript Transfer Claims

Independently check the six local claims in the supplied brief. They concern formal models, not an asserted reconstruction of historical Yijing material. The general information optimum is conditional on an explicitly stated external premise; check the reduction and finite cases without claiming that this alone proves the premise.

Use your own arguments and implementation. Check dimensions, probability measures, output alphabets, finite/asymptotic quantifiers and the numerical precision needed to support strict comparisons. A theorem about binary summaries must not be silently applied to arbitrary multi-bit labels. A uniform table is not automatically the image of a uniform law on labelled objects.

**Phase 1 deliverables.** Provisional verdicts for L1–L6 with derivations or counterexamples; executed versus described computations distinguished; any needed reformulations or numerical bounds. Do not seek the original report or code.

Stop after phase 1 and wait for the original evidence.
<!-- END ASSIGNMENT -->

<!-- BEGIN ASSIGNMENT PART 2 -->
# Phase 2: Audit the Original Evidence and Transfer Scope

Your independent derivations are fixed. Compare them with the supplied report, output and code. Explain discrepancies and audit the exact source statements used. State which conclusions follow by elementary arguments and which remain conditional on an external theorem whose full proof you have not checked.

Give a final verdict table for each local claim, distinguishing formal correctness, numerical support and external applicability. Historical correspondence is unassigned; do not supply a historical verdict from a formal calculation. Identify duplicated existing structure separately from the new local consequence, and preserve source attribution.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT PART 2 -->
