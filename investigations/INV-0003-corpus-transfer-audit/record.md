---
id: INV-0003
title: Full-context manuscript-transfer audit and finite bridge pilots
status: registered
role: synthesis
assignment: none
model: Codex assistant; exact model unknown
model_family: gpt
independence: context-exposed
model_identifier: unknown
prompt: investigations/INV-0003-corpus-transfer-audit/request.md
prompt_version: continuing conversation; no assembled isolated package
context_mode: full
materials: [README.md, AGENTS.md, roadmap/coordination-review.md, methods/research-cycle.md, methods/standards.md, ledger/definitions.md, ledger/claims/C-0016.md, ledger/claims/C-0017.md, ledger/claims/C-0019.md, investigations/library/openai-math-4eaee875/CONTENTS.md, roadmap/literature/openai-math/snapshot.json]
output: investigations/INV-0003-corpus-transfer-audit/output.md
handoff: in output and pilot-results.json
date_run: 2026-10-31
registered: 2026-10-31
preceded_by: [INV-0001]
followed_by: [INV-0004]
---
# INV-0003 — Manuscript-transfer audit

## Summary

A full-context continuation of the repository-maintenance conversation, explicitly requested by the human coordinator, examined the external manuscript collection and ran finite applicability probes. It is not independent of the legacy report, the ledger extraction, the preceding coordination review, or the external manuscripts. Proposed results remain reported/pending registration; no ledger claim was promoted.

## Provenance

- `request.md` records the current user request, not a complete assembled model prompt. Earlier conversation, system instructions, and ambient repository access were present. The complete conversation was not exported as an investigation package.
- Current source: `openai/math` at commit `4eaee87548250b2682affda7d05d947c05554bae`, retrieved through the GitHub connector on 2026-10-31. The pinned index was compared with the initial index and was identical. The source README describes 721 manuscripts in 373 families and varying verification stages.
- All 721 catalogue titles/abstracts were ingested into a searchable catalogue and subjected to automated retrieval rules. All family titles were surveyed for candidate selection. Theorem statements in 16 manuscripts from 11 families were inspected. Full proofs were not audited. Source caches include some surrounding material not read in full; cached does not mean reviewed.
- Exact cached-file paths and hashes: `roadmap/literature/openai-math/snapshot.json`. Pinned source text and formalization-scope documents are in `investigations/library/openai-math-4eaee875/`; their snapshots are frozen. Lean scopes were read for families 119, 115, and 238; Lean proofs were not compiled or independently checked.
- Executed Python 3.9.6 standard-library code: `compute/experiments/INV-0003/corpus_pilots.py`. Complete numerical output: `pilot-results.json`. No random samples: integer enumeration and exact rational probabilities, with binary64 logarithms for entropy. Those logarithms are numerical observations, not interval certificates.

## Supplied materials and ambient context

Full repository context from the preceding maintenance turn remained available. The `materials` field names the principal inputs, not an isolation boundary. Additional fetched theorem-source files and scope documents are exhaustively listed in the snapshot manifest. The model had shell execution and connected GitHub/web access.

## Deviations and independence

No fresh isolated session was used or claimed. The original palace encoding and proposed source correspondences were already visible. Imported papers are attributed to an unnamed OpenAI model; their results and companion papers cannot be treated as independent votes or as a different model-family verification. The study does not establish literature novelty of its applications.

## Registration

Registered 2026-10-31 by Claude Opus 5.5 (different family from the originator; context-exposed) as C-0027–C-0031; L4 kept as a methodological fixture. See the dated note in `registration.md`. Human review of the extraction is still advisable. Originally: pending human reconciliation. `registration.md` maps local results to existing claims or proposed new records. A completed report is not a verified claim. Future verification must distinguish the finite pilot, the transfer argument conditional on an external theorem, the external theorem itself, and source correspondence to the Yijing.

## Additional attempt

A later exact rational check within this continuation excluded a universal pointwise-majorization proof route for the L2 extension. The unchanged original report is supplemented by `additional-attempt.md` and its executed code; the failed sufficient condition does not refute the average entropy conjecture. See registration notes.
