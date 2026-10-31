---
id: ASN-0005
title: Pre-specified sensitivity and discrimination tests of competing explanations for structure in the received order
status: ready
role: specialist
context_mode: targeted
role_prompt: prompts/roles/specialist.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md, context/briefs/ASN-0005-explanations.md, methods/standards.md]
materials_part2: []
claims: [C-0003, C-0005, C-0006, C-0009, C-0010, C-0011, C-0012, C-0015, C-0024, C-0025]
recommended_model: Claude Opus 5.5
excluded_models: []
replication_of: none
investigations: []
purpose: development
directions: [DIR-004]
questions: [Q-002, Q-004, Q-006]
work_items: [received-order-transcription, explanation-sensitivity-tests]
prerequisites: []
intentional_overlap: [ASN-0001, ASN-0002, ASN-0007, ASN-0008]
created: 2026-10-31
---
# ASN-0005: Pre-specified sensitivity and discrimination tests of competing explanations

## Rationale (coordinator only)

- **Intentional overlap:** ASN-0001 and ASN-0002 independently transcribe the same order. ASN-0002 audits old values; this assignment designs and executes sensitivity analyses and new discriminating consequences. ASN-0007 builds a cited baseline, while ASN-0008 checks novelty of shared claims. Do not treat recomputation, source agreement, or prior art as fresh statistical evidence.

- DSP-001 and DSP-002 are the program's central explanatory disputes, and every statistic bearing on them so far was exploratory, with one null model (Q-004). This assignment fixes a sensitivity and discrimination plan before further computation, and implements part of INV-0001's own recommended next step (Q-002).
- **Two parts** to freeze the next analysis: the design is produced and saved (frozen) before execution is requested.
- **Selected-data limit:** P1–P3 are already known and selected. Withheld p-values and a new plan do not make them fresh evidence. Only genuinely unexamined consequences or data, identified with an access/eligibility record before testing, can support confirmatory inference. Otherwise label results descriptive or sensitivity analyses. The earlier search universe is unknown.
- **Context:** targeted. The brief gives the phenomena, the competing explanations, and the list of statistics already examined, which is needed for multiplicity accounting. It deliberately withholds the reported p-values to avoid anchoring, and does not name the originating model. `methods/standards.md` is included because the assignment is about statistical method.
- **Model:** Claude Opus 5.5. The claims under test were originated by Claude Opus 5.5, but this is a new planned sensitivity investigation; its purpose differs from auditing the old values. Freezing the plan limits additional flexibility; it does not remove earlier selection. Its results will themselves need verification by GPT-6.1 Sol Max in a later cycle.
- *Alternatives considered:* GPT-6.1 Sol Max (would make GPT do all cycle-1 work touching INV-0001's claims, leaving Claude only exploration); waiting for ASN-0002's recomputation (rejected: independent, and both can run concurrently).

## Completion criteria (coordinator only)

- Part 1 output is a complete fixed analysis plan, including the prior-exposure record and confirmatory eligibility of each test. Save it frozen as `output-part1.md` **before** sending part 2.
- Part 2 reports every planned test. Any deviations are reported; exploratory analyses are labeled.
- On registration: new statistical claims; update DSP-001 and DSP-002, Q-004 and Q-006; update C-0024 and C-0025 evidence sections.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Pre-specified Sensitivity and Discrimination Tests of Explanations for Structure in the Received Order

You are assigned to design, and then carry out, a pre-specified sensitivity and discrimination analysis of competing explanations for reported features of the received (King Wen) order. The phenomena and explanations are listed under "Supplied materials".

You have been given selected material from earlier investigations in this program, listed under "Supplied materials". Each prior finding carries a verification status; treat "reported" findings as unverified. You are not required to accept their representations or conclusions. List the identifier of every prior finding you rely on.

The work has two parts in this conversation. **In this part, design the analysis. Do not compute any test outcome.** Write a fixed analysis plan that specifies:

1. each hypothesis to be tested, stated precisely enough to be refuted;
2. the statistics, including at least one that could discriminate between explanations (a) and (b) for P3 through consequences beyond the four hexagrams themselves, and at least one that could discriminate between H2 and H0;
3. several null models, each justified, including at least one that is not the pair-shuffling model;
4. thresholds and multiplicity handling, distinguishing the known earlier tests from the unknown earlier search universe; correcting only the listed tests cannot establish control over that unknown selection;
5. what each possible outcome would imply for each explanation;
6. an exposure record and which, if any, consequences or data remain genuinely unexamined. Reanalysis of the supplied phenomena is descriptive. A new statistic on already inspected material is not automatically independent evidence; justify any confirmatory status, or label the test a sensitivity analysis.

You may conclude that no eligible confirmatory test is available. A well-scoped sensitivity analysis or proof that the explanations are observationally indistinguishable is useful. Do not manufacture a significant result.

You may conclude that some of the explanations cannot be discriminated by any feasible test. If so, say why. You may also propose explanations not listed.

**Useful completion (part 1).** A fixed analysis plan complete enough that someone else could execute it without making further decisions.

Stop after part 1 and wait for the next message.
<!-- END ASSIGNMENT -->

<!-- BEGIN ASSIGNMENT PART 2 -->
# Part 2: Execution

Your analysis plan is now on record and fixed. Reanalysis of previously selected patterns remains descriptive; use confirmatory language only for tests whose eligibility was justified in that plan. Execute it exactly.

Report every planned test, including those with null results. If you must deviate (for example, because a statistic turns out to be ill-defined), report the deviation and its reason, and keep the frozen version alongside. You may then carry out additional analyses, clearly labeled as exploratory.

**Deliverables.** Results of every planned test; code (stating whether it was executed) and exact data, including your full transcription of the received order and its source; deviations; exploratory analyses, labeled as such; an assessment of each explanation for P3 and of H2 and H0, with confidence and value of further investigation stated separately.

**Useful completion.** Every planned test is reported and every explanation is assessed.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT PART 2 -->
