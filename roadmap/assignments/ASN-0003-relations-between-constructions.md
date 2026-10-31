---
id: ASN-0003
title: Mathematical relations between Yijing constructions (supplied assignment)
status: ready
role: explorer
context_mode: targeted
role_prompt: prompts/roles/explorer.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md]
materials_part2: []
claims: []
recommended_model: Claude Opus 5.5
excluded_models: []
replication_of: none
assignment_text_sha256: a88a6402301f50f2425b3b383fe6d7f7f22ee32419ea5b26ff6c1c1e34134d89
investigations: []
purpose: exploration
directions: [DIR-002, DIR-010]
questions: []
work_items: [operation-relations-exploration]
prerequisites: []
intentional_overlap: []
created: 2026-10-31
---
# ASN-0003: Mathematical relations between Yijing constructions

## Provenance

The assignment text below is the supplied document `writing-block (2).md` from the human coordinator's research-design discussion, reproduced **verbatim**. `tools/yj.py validate` checks that the text between the markers still has SHA-256 `a88a6402…`. Do not edit it; write a new assignment if it needs changing. The generalized template `prompts/components/assignment-template.v1.md` was derived from it.

## Rationale (coordinator only)

- The coordinator wrote this assignment for the program. It covers DIR-010 (relations among operations and constructions), and possibly DIR-002 (noncommutation), whose source report is absent.
- **Context:** the text names the topics earlier investigations examined, but no findings. That is targeted context limited to topic disclosure. Supplying INV-0001's report was considered and rejected for this cycle: with nothing yet verified, an independent attempt is worth more than avoiding overlap. The text's own instruction, "You are not required to accept their representations or conclusions", is harmless without the reports.
- **Role:** explorer. The text asks for independent, open-ended work rather than a specific question.
- **Model:** Claude Opus 5.5, in a fresh isolated session, to balance cycle 1 (GPT-6.1 Sol Max takes ASN-0001, ASN-0002 and ASN-0006). Known limitation: INV-0001 was also Claude Opus 5.5 and covered several of these operations, so overlap with INV-0001 is likely. Results matching INV-0001 count as independent derivations from the same model family, not as verification. Results beyond INV-0001 are the main value.
- **Possible deliberate replication:** after INV-0002 is located, consider running the same text with GPT-6.1 Sol Max if its report does not already cover this ground.

## Completion criteria (coordinator only)

- A set of results on interactions, compositions, incompatibilities, invariants or generalizations, each with status, and an adversarial self-evaluation as the text requires.
- On registration: map results equivalent to INV-0001 claims as additional derivations, and register new claims and questions.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Mathematical Relations Between Yijing Constructions

You are assigned an independent investigation of mathematical relationships among the structural operations and constructions associated with the Yijing.

Your objective is to discover what can be learned from their interactions, compositions, incompatibilities, invariants, and possible generalizations.

Existing investigations have examined reversal, complementation, nuclear hexagrams, trigram decomposition, and selected ordering and palace structures. You are not required to accept their representations or conclusions.

You may explore unfamiliar operations, construct new mathematical formulations, or question whether the objects under investigation have been defined in the most productive way.

Do not merely enumerate known mathematical descriptions. Seek consequences that were not obvious from the starting definitions.

Give particular attention to cases where several independent observations appear to follow from one principle, but test whether the apparent unification is genuine.

You should not assume that any common principle exists.

Work independently until you have a substantive set of findings. Then evaluate your strongest results adversarially.

At the end, identify which claims warrant independent verification and which questions would be most valuable for another investigator to pursue.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT -->
