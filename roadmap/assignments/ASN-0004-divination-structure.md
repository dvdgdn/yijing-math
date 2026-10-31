---
id: ASN-0004
title: Fresh exploration — mathematical structure of divination procedures and changing lines
status: ready
role: explorer
context_mode: minimal
role_prompt: prompts/roles/explorer.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [context/objects/hexagrams.md, context/objects/divination.md]
materials_part2: []
claims: []
recommended_model: Claude Opus 5.5
excluded_models: []
replication_of: none
investigations: []
purpose: exploration
directions: [DIR-006, DIR-009]
questions: []
work_items: [divination-structure-exploration]
prerequisites: []
intentional_overlap: []
created: 2026-10-31
---
# ASN-0004: Fresh exploration of divination procedures and changing lines

## Rationale (coordinator only)

- DIR-006 is entirely unexplored. INV-0001 set aside every procedure except the Jing Fang palaces. The divinatory layer has four-valued lines and a primary-to-second hexagram transition, so it is a natural place for structure that the two-valued framing (DEF-001) cannot see.
- **Minimal context**, to give the program a genuinely fresh investigation, as the setup brief requires. Nothing about INV-0001 is disclosed; the territory was chosen because it is unexplored, and the investigator is not told that.
- **Model:** Claude Opus 5.5, to balance cycle 1.
- *Alternatives considered:* a minimal-context exploration of the received order itself (deferred: it is the territory INV-0001 worked in, so it is better suited to a later blind replication); the textual layer, DIR-007 (deferred: it needs stronger statistical safeguards and a text source).

## Completion criteria (coordinator only)

- At least one precise result about a named procedure and at least one about the transition structure, each with stated dependence on variant procedures.
- On registration: everything new goes to the ledger; note any rediscovery of registered results as independent derivations.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Mathematical Structure of Divination Procedures and Changing Lines

You are assigned an independent investigation of the procedures by which hexagrams are generated in divination, and of the relationship between a primary hexagram and the second hexagram obtained by changing its moving lines.

Your objective is to discover what mathematical structure these procedures and transitions have, how that structure depends on which procedure or reading rule is used, and how it relates to the structure of the hexagrams themselves.

You have been given only the common research charter, this assignment, a description of the relevant objects and source material, and the research handoff protocol. You have deliberately not been given the findings of other investigators in this program. Work from the supplied material and your general knowledge, and cite any literature you rely on.

You may explore unfamiliar approaches, construct new formulations, or question whether the objects have been defined in the most productive way.

You are not limited to the following, but you may find them useful starting points. What does each procedure, as described in a named source, actually compute? Which features of the outcome depend on the procedure and which do not? What structure does the passage from primary to second hexagram give the set of hexagrams? Do traditional reading rules admit a precise mathematical description, and what follows from it?

**Deliverables.** A precise description, with source, of every procedure and reading rule you analyze. Code or exact pseudocode for every computation, stating whether it was executed. An explicit account of which results depend on choices among variant procedures or rules.

**Useful completion.** At least one precise, checked result about a procedure as described in a named source, at least one about the structure of the primary-to-second transition, and an honest map of what you tried and what failed.

At the end, identify which of your claims most warrant independent verification and which questions would be most valuable for another investigator to pursue.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT -->
