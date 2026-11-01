---
id: ASN-0010
title: Information-preserving observables and the cost of structural quotients
status: withdrawn
role: specialist
context_mode: targeted
role_prompt: prompts/roles/specialist.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md, context/briefs/ASN-0010-information-transfer.md, investigations/library/openai-math-4eaee875/sources/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex, methods/standards.md]
materials_part2: []
claims: [C-0016]
purpose: development
directions: [DIR-006, DIR-009, DIR-010]
questions: []
work_items: [information-observable-extension]
prerequisites: []
intentional_overlap: [ASN-0001, ASN-0008]
recommended_model: either; isolated session with code execution desirable
excluded_models: []
replication_of: none
investigations: []
created: 2026-10-31
---
# ASN-0010: Information-preserving observables

## Rationale (coordinator only)

- **Withdrawn 2026-10-31 (never launched).** INV-0004 settled the first extension option (all-noise comparison of the base and difference labels; C-0035, with the trigram added) and partly addressed the asymmetric option (C-0032, C-0038). What remains open is recorded as Q-009 and Q-010 (multi-bit optimality at intermediate noise; asymmetric single-bit optimality), candidates for an optional cycle-2 specialist. Verification of the new claims is ASN-0014. The original rationale is kept below for the record.

- Highest-priority direct transfer from the external corpus. Family 119 matches a finite Boolean model and provides an all-dimension nonlinear benchmark; INV-0003 L1–L2 supply a concrete gap rather than a verbal analogy.
- **Intentional overlap:** ASN-0001 verifies C-0016 and its historical correspondence. This task studies a new channel/observable consequence of the specified formal construction; it must not repeat the source-table audit or claim that it is complete. ASN-0008 checks prior art around C-0016, while this task must additionally check literature on the new information statement before asserting novelty.
- ASN-0013 independently audits the original pilot; do not spend this run merely reproducing every pilot value. Check the reduction, then develop one extension. ASN-0004 remains a blind exploration and receives none of this framing. Source-dependent asymmetric probabilities require ASN-0007's cited procedure material before historical use.
- Decision: can an information-versus-invariance tradeoff or a general comparison theorem replace isolated numerical differences? Prioritize that over more broad received-order pattern searches. Bound the run to one precise extension; an explicit counterexample is useful.

## Completion criteria (coordinator only)

- An exact statement beyond the two pilot points: proof, counterexample, or a bounded computational result with a remaining gap. Compare a raw-trigram baseline and at least one explicit alternative representation/partition where relevant.
- Import audit distinguishes the source theorem, its application, and the new contribution. No unqualified claim of global three-bit optimality from a binary theorem.
- A concrete next discriminating check, novelty-search scope, and a reason to continue or stop. Source correctness remains separate.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Information-Preserving Observables Under Line Changes

Use the supplied source theorem and formal pilot to develop a precise result about which structural summaries preserve information when lines change. The model is stated explicitly in the brief. It is a mathematical comparison model; no historical procedure or purpose is presumed.

First check the reduction to the induced difference channel and the exact hypotheses of the imported binary-information bound. Then choose **one** substantive extension: prove or refute an all-noise comparison of the supplied equal-entropy labels; establish an optimum or obstruction for a precisely defined invariance-compatible class; or show which part survives an explicitly specified asymmetric channel. State your question and stopping condition before expanding the computation.

The supplied work is reported, not independently verified. Distinguish an imported theorem from your transfer proof and your new consequence. Compare with elementary coordinate/trigram controls; a more robust label than one other label is not a global optimum. Renaming output labels must not change a full-label information comparison. Treat any multi-bit information argument separately from the source's Boolean-output theorem.

**Deliverables.** A precise extension and assumptions; proof or bounded numerical evidence with gaps; counterexample search; model/representation sensitivity; and the exact novelty search actually conducted. If no nontrivial extension survives, identify the obstacle and a nearby formulation that was not ruled out.

**Useful completion.** A checkable consequence beyond the supplied numerical points, or a precise obstruction showing why that proposed extension fails. Do not produce a broad catalogue of noise analogies.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT -->
