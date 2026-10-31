# Ledger Changelog

Newest first. Each entry lists claims added or changed, statuses changed, and investigations ingested. The first `## v` heading is the current ledger version.

## v0.1 — 2026-10-31

Initial registry, created during repository setup.

- **Ingested:** INV-0001 (Claude Opus 5.5, legacy prompt `yijing_paradigm_transcendence.md`). Registration notes: `investigations/INV-0001-claude-paradigm-transcendence/registration.md`.
- **Placeholder:** INV-0002 (GPT-6.1 Sol Max). Output absent from the repository; nothing registered.
- **Added:** claims C-0001 to C-0026 (all `reported`); definitions DEF-001 to DEF-016; questions Q-001 to Q-008; directions DIR-001 to DIR-011; disputes DSP-001 to DSP-003.
- **Verification:** none performed. Claim extraction was done by Claude Opus 5.5 acting as registrar, the same model family as the originator. The extraction should be reviewed by the human coordinator or by a GPT-6.1 Sol Max coordinator run.
- **Registrar notes** (clearly labeled in the records) were added to C-0002, C-0003, C-0005, C-0006, C-0009, C-0010, C-0023 and to several definitions. They flag checks for verifiers and possible prior literature. They are not findings.


### Coordination maintenance — 2026-10-31

- No claims added or changed; all 26 remain reported. No investigations launched, mathematical verification performed, or ledger reconciliation implied.
- New draft defaults: handoff protocol v3 adds compact search history, evidence lineage, qualified novelty/use and reusable follow-up contracts; coordinator prompt v2 adds board, dependency-review and adaptive selection checks; assignment template v2 adds coordinator metadata and stopping/decision criteria. Earlier versions are retained unchanged.
- Existing unsent assignments now reference handoff v3; ASN-0003's supplied assignment text retains its original hash. ASN-0005 now asks for pre-specified sensitivity/discrimination analyses and distinguishes previously selected patterns from eligible new confirmatory tests.
- Added a generated coordination board, transitive dependency review and explicit independence metadata. Legacy investigation independence remains unknown. Added draft assignments ASN-0007 to ASN-0009 and a provisional [selection review](../roadmap/coordination-review.md).


### Manuscript-assisted development — 2026-10-31

- No existing claim added, changed or promoted. INV-0003 is a completed, context-exposed report with local results and registration pending; its proposed registration distinguishes conditional imported results, finite numerical evidence and elementary proofs.
- Pinned the external mathematical catalogue and selected source statements; added searchable retrieval records, explicit review levels, and qualitative transfer priorities in `roadmap/literature/openai-math/`. External manuscripts and formalization links are not automatically verified.
- Prepared draft assignments ASN-0010–ASN-0013 for information-preserving observables, conditional comparison ensembles, local permutation structure and independent audit. No other-model investigation was launched. The unassisted exploration lane and existing historical/source checks remain.
- Added canonical external-result import and assisted-development guidance. The reusable investigator role/handoff prompts are unchanged in this phase; source-specific findings stay in targeted briefs and roadmap material.


### Visual coordination dashboard — 2026-10-31

- Added a generated local HTML overview of existing records, with assignment/evidence/territory/manuscript views, model-family fit, pending registration and a Claude coordinator handoff guide.
- `tools/yj.py index` refreshes the HTML alongside both Markdown indexes; optional local serving refreshes valid changes and preserves the last valid snapshot when records are inconsistent. No browser action changes research metadata.
- No claims, investigation outcomes, verification statuses or frozen originals changed. Priority cards are coordinator suggestions sourced from `roadmap/dashboard-notes.json`.
