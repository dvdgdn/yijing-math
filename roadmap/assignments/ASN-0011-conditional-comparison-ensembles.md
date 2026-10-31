---
id: ASN-0011
title: Conditional comparison ensembles with the correct elementary measure
status: draft
role: specialist
context_mode: targeted
role_prompt: prompts/roles/specialist.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md, context/briefs/ASN-0011-null-transfers.md, investigations/library/openai-math-4eaee875/sources/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/build/sections/introduction.tex, investigations/library/openai-math-4eaee875/sources/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/build/sections/introduction.tex, methods/standards.md]
materials_part2: []
claims: []
purpose: development
directions: [DIR-004, DIR-007]
questions: [Q-004]
work_items: [conditional-ensemble-reference]
prerequisites: []
intentional_overlap: []
recommended_model: either; isolated session with code execution
excluded_models: []
replication_of: none
investigations: []
created: 2026-10-31
---
# ASN-0011: Conditional comparison ensembles

## Rationale (coordinator only)

- Family 115 could replace inappropriate broad randomizations with tractable conditional ensembles. The key first step is modelling and measure, not an assumption that the external existence theorem is a ready library.
- Q-004 also appears in ASN-0005. Deliberate division: this task delivers a finite reference ensemble, an exact induced measure and algorithm/error contract; ASN-0005 owns explanation hypotheses, thresholds and test execution. Do not independently compute its selected phenomena or silently alter a frozen plan. The distinct work keys record this output boundary.
- ASN-0009's textual pilot may later use the reference method once features and sources are fixed. Source acquisition remains ASN-0007. The formal reference model can be designed without waiting for a complete historical corpus; historical assertions cannot.
- Decision: can a relevant conditional comparison be encoded faithfully, and does the imported result improve on exact enumeration/dynamic programming? Stop if no such advantage or valid encoding is found, retaining the counterexample or modelling limitation.

## Completion criteria (coordinator only)

- One explicitly defined elementary sample space, induced law and state representation; a complete small reference enumeration and a justified sampling/counting path.
- An account of which constraints are preserved, randomized, or omitted. The multiplicity correction from elementary outcomes to tables/graphs is explicit.
- Source theorem hypotheses and numerical/sampling approximation errors are separated from Monte Carlo and selection uncertainty. No historical p-value is required for completion.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Correct Conditional Comparison Ensembles

Develop one conditional comparison ensemble that could answer a precise question about an arrangement or textual feature, preserving constraints that should not be randomized. Use the supplied external sampling/counting statements only when their hypotheses match your representation.

Define the elementary randomized objects first. Show whether each table or graph corresponds to one elementary outcome or many, and with what weights. A uniform-table law, a uniform ordering law, and a uniform labelled-allocation law are different choices. Say which scientific question your law answers.

Implement a fully enumerated small reference problem. Compare the intended law with at least one plausible alternative and identify an event whose probability differs or prove equivalence. State when ordinary exact methods suffice. If scaling requires the imported algorithm, give a concrete reduction, identify the needed source lemmas, and establish an implementable error/running-time contract; do not claim acceleration from the theorem statement alone.

Do not execute another investigation's explanation-test battery. The output here is the reusable comparison model and its reference checks. Any later test of selected phenomena must retain its exposure and multiplicity record.

**Deliverables.** Exact sample space and measure; state correspondence and weights; constraints preserved/omitted; reference code and results; theorem applicability or failure; and the next source input needed for a substantive application.

**Useful completion.** A successor can use the model without guessing its law, or can see exactly why the proposed encoding or imported theorem fails. No positive finding about historical design is required.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT -->
