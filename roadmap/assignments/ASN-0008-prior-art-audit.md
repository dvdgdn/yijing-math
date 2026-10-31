---
id: ASN-0008
title: Audit prior art and identify precise differences from existing results
status: draft
role: specialist
context_mode: targeted
role_prompt: prompts/roles/specialist.v1.md
charter: prompts/components/charter.v1.md
handoff: prompts/components/handoff-protocol.v3.md
materials: [ledger/claims/C-0002.md, ledger/claims/C-0003.md, ledger/claims/C-0007.md, ledger/claims/C-0008.md, ledger/claims/C-0014.md, ledger/claims/C-0016.md, ledger/claims/C-0018.md, ledger/claims/C-0019.md, methods/standards.md]
materials_part2: []
claims: [C-0002, C-0003, C-0007, C-0008, C-0014, C-0016, C-0018, C-0019]
purpose: prior-art
directions: [DIR-004, DIR-009, DIR-010]
questions: []
work_items: [prior-art-audit]
prerequisites: []
intentional_overlap: [ASN-0001, ASN-0002, ASN-0005, ASN-0010]
recommended_model: either; requires literature access
excluded_models: []
replication_of: none
investigations: []
created: 2026-10-31
---
# ASN-0008: Prior-art audit

## Rationale (coordinator only)

- **Additional overlap:** ASN-0010 uses C-0016 for a new information comparison. This audit retains the earlier structural prior-art scope; a novelty claim about the information application needs its own literature check.

- Current claims contain several unchecked suggestions that results may already be known, while C-0019 asserts novelty without a search. Novelty should be checked before a long development programme grows around rediscoveries.
- **Intentional overlap:** ASN-0001 and ASN-0002 check the correctness of overlapping claims; this assignment checks literature and exact equivalence. ASN-0005 tests explanations bearing on C-0003. Prior publication, correctness, and explanatory significance are separate outcomes.
- Targeted context suffices. Do not send this report to fresh explorers; use it to improve later specialist briefs and the coordinator's choice of questions.
- Stop after the bounded search is documented. Failure to find a result is not a claim of originality, and a known result may still support a new consequence.

## Completion criteria (coordinator only)

- Per claim: sources actually consulted, exact passages or theorem locations, equivalence or difference in assumptions/conclusions, remaining uncertainty, and search queries/languages/coverage limits.
- Distinguish traditional observations, established mathematics applied here, and a potentially new consequence. Preserve attribution and a possible useful extension even when the main fact is known.
- Add evidence and literature notes to claim bodies through registration; do not promote verification status from a citation. Any newly asserted equivalence starts reported.

## Assignment text

<!-- BEGIN ASSIGNMENT -->
# Investigation Assignment: Prior Art and Exact Contribution

For the supplied claims, conduct a bounded literature audit. Determine which statements have identifiable antecedents and what, if anything, differs from those antecedents. Treat supplied claims as reported, and separate their mathematical correctness from their publication history.

Search by the underlying statement as well as its terminology, including alternate names and relevant source-language terms where you can assess them. Include both mathematical literature and traditional or historical sources where appropriate. State a search boundary before starting, prioritize the claims with the strongest novelty language, and report access limits. Do not infer novelty from unsuccessful keyword searches.

**Deliverables.** A claim-by-claim table: consulted source and exact location; what it actually states; match, weaker, stronger, or different result; remaining uncertainty; useful next consequence. Record queries, languages, databases or collections used, and works available only through secondary references. Never invent a citation or imply that an inaccessible work was read.

**Useful completion.** A traceable account of what the search establishes and does not establish, including exact differences wherever a relevant antecedent is found. An honest unresolved novelty assessment is useful.

Follow the common research charter and the research handoff protocol.
<!-- END ASSIGNMENT -->
