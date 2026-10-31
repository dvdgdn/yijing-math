# Research Roadmap

**Contains findings** (in assignment rationales). Never supply this directory to an investigator. Only the text between an assignment's `BEGIN ASSIGNMENT` / `END ASSIGNMENT` markers is sent.

Start with the generated [coordination board](BOARD.md) and the [coordination review and proposed launch slate](coordination-review.md). Canonical contracts, overlap checks and adaptive planning: [`methods/research-cycle.md`](../methods/research-cycle.md) §8–9.

This roadmap is provisional. Revise it after every reconciliation. Assignments are prepared here and launched as investigations (see the main README).

## Manuscript-assisted track (added 2026-10-31)

The [pinned corpus transfer review](literature/openai-math/transfers.md) updates the proposed launch priority using all 721 catalogue titles/abstracts, 16 inspected theorem statements, and the completed finite pilot INV-0003. All new claims remain reported/pending registration. It changes the proposed assisted slate without removing the blind-exploration lane or resolving existing source debt.

| Priority | Draft work package | Concrete outcome sought |
|---|---|---|
| 1 | [ASN-0010](assignments/ASN-0010-information-preserving-observables.md) | A general information/robustness comparison or precise obstruction beyond two finite pilot points. |
| 1, independent audit | [ASN-0013](assignments/ASN-0013-verify-corpus-bridges.md) | Two-phase verification of the pilot's local claims and theorem applicability, with independent code. |
| 2 | [ASN-0011](assignments/ASN-0011-conditional-comparison-ensembles.md) | A correctly weighted conditional ensemble and exact finite reference calculation for later explanation/text tests. |
| 3 | [ASN-0012](assignments/ASN-0012-local-permutation-structure.md) | A joint-information or bounded-depth ordering consequence under a fixed local grammar. |

Suggested assisted first slate: ASN-0010 plus ASN-0013, with source work ASN-0007 alongside as capacity allows. Retain ASN-0004 or ASN-0006 as an unassisted run rather than giving every investigator the same papers. ASN-0001 remains the palace/source verification owner. No new assignment has been launched; new packages are drafts and are assembled for review, not approved runs.

[Search the complete catalogue](literature/openai-math/README.md) before opening a new transfer. The review records direct matches, finite-scope failures, elementary methods that beat imported machinery, and reopening triggers. Pending registration is visible on the board.

## Cycle 1 (prepared 2026-10-31, ledger v0.1)

The cycle has two goals. First, start independent verification of the only existing results. Second, avoid building the program on a single investigation's framing: it opens two unexplored or independent lines and runs the first conceptual reset.

| ID | Title | Role | Context | Recommended model | Claims | Order |
|---|---|---|---|---|---|---|
| [ASN-0001](assignments/ASN-0001-verify-pairing-and-palaces.md) | Verify the received pairing and the palace-system cluster | verifier (two-phase) | targeted | GPT-6.1 Sol Max | C-0001, C-0002, C-0016–C-0019, C-0026 | first |
| [ASN-0002](assignments/ASN-0002-verify-nuclear-canon-statistics.md) | Verify the nuclear-map, canon, and statistical claims | verifier (two-phase) | targeted | GPT-6.1 Sol Max | C-0003–C-0015, C-0026 | any time |
| [ASN-0003](assignments/ASN-0003-relations-between-constructions.md) | Relations between Yijing constructions (supplied text, verbatim) | explorer | targeted (topics only) | Claude Opus 5.5 | — | any time |
| [ASN-0004](assignments/ASN-0004-divination-structure.md) | Fresh exploration: divination procedures and changing lines | explorer | **minimal** | Claude Opus 5.5 | — | any time |
| [ASN-0005](assignments/ASN-0005-preregistered-explanation-tests.md) | Pre-specified sensitivity and discrimination tests | specialist (two-part) | targeted | Claude Opus 5.5 | C-0003, C-0005, C-0006, C-0009–C-0012, C-0015, C-0024, C-0025 | any time |
| [ASN-0006](assignments/ASN-0006-conceptual-reset.md) | Conceptual reset: questioning the framing | paradigm-breaker | **minimal** | GPT-6.1 Sol Max | — | any time |

All six can run in separate fresh sessions, with intentional overlap recorded on the assignments. The proposed next slate and reasons to defer candidates are in the [coordination review](coordination-review.md); the ready list need not be launched all at once. ASN-0001 remains the first verification priority. ASN-0005's frozen plan cannot turn already selected patterns into fresh confirmatory evidence.

### How cycle 1 covers the planned mix

| Need | Assignments |
|---|---|
| Independent verification of the strongest results | ASN-0001 (palace cluster, pairing), ASN-0002 |
| Apparent contradictions or competing explanations | ASN-0005 (DSP-001, DSP-002) |
| Underexamined structures | ASN-0004 (DIR-006), ASN-0003 (DIR-010) |
| Explanatory claims tested against alternatives | ASN-0005 |
| Fresh investigation without exposure to previous findings | ASN-0004, ASN-0006 |

### Model rotation

- In cycle 1 GPT-6.1 Sol Max verifies, because every registered claim came from Claude Opus 5.5, and it runs the conceptual reset, because the current framing came from Claude. Claude Opus 5.5 explores and runs the pre-registered tests.
- In cycle 2 the roles should swap: Claude Opus 5.5 verifies GPT-6.1 Sol Max's results (from INV-0002 once located, and from ASN-0006), GPT-6.1 Sol Max verifies ASN-0004 and ASN-0005, and a minimal-context exploration goes to Claude.
- Recommendations are not rules. If a model is unavailable, any assignment except the verifications can run on either model. Verifications must not be run on the originating model family if the result is to count as `verified`.

### Coordinator tasks alongside cycle 1 (human)

1. **Locate the GPT-6.1 Sol Max report** (INV-0002) and register it. See `investigations/INV-0002-gpt-initial-investigation/record.md`.
2. **Source data:** begin the cited transcriptions listed in `data/README.md` (received order, palace table, mnemonic source). Verifiers will supply their own transcriptions meanwhile.
3. **Review the setup's drafts:** role prompts v1, handoff protocol v2, the assignment template, and the claim extraction for INV-0001 were all written during setup by Claude Opus 5.5 and have not been reviewed.

## Additional prepared drafts (2026-10-31)

These are candidates, not approved launches. They use handoff v3 and the coordinator contract fields. Draft status and unmet prerequisites are visible on the board.

| Assignment | Purpose | Readiness / value |
|---|---|---|
| [ASN-0007](assignments/ASN-0007-source-baselines.md) | Cited baselines and source intake | Enables source-dependent work and neglected material; preserve blind verifier transcriptions before comparison. |
| [ASN-0008](assignments/ASN-0008-prior-art-audit.md) | Bounded prior-art audit | Separates novelty from correctness and identifies precise useful extensions; requires literature access. |
| [ASN-0009](assignments/ASN-0009-textual-pilot.md) | Minimal textual pilot | A distinct underexamined layer; remains draft until ASN-0007 yields a fixed cited source excerpt. |

## Candidates for cycle 2

Choose these after cycle 1 is reconciled. Listed so they are not forgotten. None is committed.

- **Q-003** (specialist): how special is a cumulative bottom-up rule that yields a transversal? Best run after ASN-0001 confirms or corrects C-0016 and C-0017.
- **Synthesis** (full context): once two or more investigations are registered and some claims verified.
- **Blind replication** (minimal explorer on the received order): tests whether INV-0001's main results are rediscovered without prompting.
- **Framing-exposed paradigm-breaker:** supply the program's working assumptions (not results) and ask for attacks on them.
- **Historical layer** (specialist with historical sources): Q-001, Q-008, and the dating assumptions in C-0022.
- **Generalization** (specialist): Q-005.
- **Other arrangements and systems:** DIR-005, DIR-008, once cited data exist.

## Change log

- 2026-10-31: Cycle 1 prepared during repository setup.

- 2026-10-31: Coordination maintenance added explicit coverage/overlap/prerequisites, draft source/prior-art/text tasks, and an adaptive selection review. Revised unsent ASN-0005 to distinguish selected-pattern sensitivity from eligible confirmation. No investigations launched or claim statuses changed.

- 2026-10-31: Added a pinned external manuscript library, reported full-context finite probes (INV-0003; registration pending), source-grounded transfer priorities, and draft assignments ASN-0010–ASN-0013. Existing claims remain unchanged.
