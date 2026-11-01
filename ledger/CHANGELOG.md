# Ledger Changelog

Newest first. Each entry lists claims added or changed, statuses changed, and investigations ingested. The first `## v` heading is the current ledger version.

## v0.3 — 2026-11-01

Cited source baselines (ASN-0007). Registrar: Claude Opus 5.5. Self-registration; human review advised.

- **Registered INV-0008** (Claude Opus 5.5, full context, source work). Added C-0039 (the *Xugua* attests the received order), C-0040 (*Jingshi Yizhuan* palace heads and stated world lines) and C-0041 (Zhu Xi's case counts give the yarrow-standard law; no split law attested).
- **First datasets in `data/`:** received order, eight-palace table and procedure texts. Each is cited to pinned Wikisource revisions, compared across two digital witnesses where available, and `unchecked` against print. The raw snapshots are frozen under `investigations/INV-0008-cited-source-baselines/sources/`.
- **Verification-log notes** (recomputation on cited data; same family as the originator; statuses unchanged):
  - C-0002, C-0003, C-0004, C-0006, C-0009, C-0017(b) and C-0018 hold on the cited tables.
  - INV-0005's saved blind transcriptions match them.
  - Source notes on C-0032 and C-0033.
- **Notes added** to DEF-011, DEF-017, Q-008, Q-011 (now partly addressed), DIR-005, DIR-006, DIR-007 and DIR-008. SRC-001, SRC-002, SRC-006 and SRC-007 now cite digital witnesses.
- **Verification:** none. No claim changed status. INV-0005, INV-0006 and INV-0007, run or coordinated in another session, are not registered here.

## v0.2 — 2026-10-31

Adjudication of the manuscript-assisted expansion; first registrations since v0.1. Registrar: Claude Opus 5.5. Human review of both extractions is advised.

- **Registered INV-0003** (Codex assistant, gpt family, context-exposed). Allocated as C-0027 (L1, conditional), C-0028 (L2), C-0029 (L3), C-0030 (L5) and C-0031 (L6, scoped negative). L4 is kept as a methodological fixture. The registrar is a different family from the originator but is context-exposed.
- **Ingested and registered INV-0004** (Claude Opus 5.5, full context, literature-assisted): C-0032–C-0036 (channels, split sensitivity, conditional coin-model bound, computer-assisted all-noise label ordering, endpoint extremality) and C-0037–C-0038 (conjectures). Self-registered.
- **Added:** DEF-017 (procedure models), DEF-018 (labels), DEF-019 (robustness rates); Q-009–Q-011. DIR-006 is now `lightly explored`.
- **Verification:** none. INV-0004 recomputed INV-0003's finite claims with independent code and found no discrepancy. This is recorded in the claim logs as context-exposed and not a protocol verification. All 38 claims remain `reported`.
- **Planning:** added draft ASN-0014 (GPT-family verification of C-0032–C-0036); withdrew ASN-0010; ASN-0011 and ASN-0012 deferred in the roadmap. See `roadmap/literature/openai-math/adjudication.md`.

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
