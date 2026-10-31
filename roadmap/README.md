# Research Roadmap

**Contains findings** (in assignment rationales). Never supply this directory to an investigator. Only the text between an assignment's `BEGIN ASSIGNMENT` / `END ASSIGNMENT` markers is sent.

This roadmap is provisional. Revise it after every reconciliation. Assignments are prepared here and launched as investigations (see the main README).

## Cycle 1 (prepared 2026-10-31, ledger v0.1)

The cycle has two goals. First, start independent verification of the only existing results. Second, avoid building the program on a single investigation's framing: it opens two unexplored or independent lines and runs the first conceptual reset.

| ID | Title | Role | Context | Recommended model | Claims | Order |
|---|---|---|---|---|---|---|
| [ASN-0001](assignments/ASN-0001-verify-pairing-and-palaces.md) | Verify the received pairing and the palace-system cluster | verifier (two-phase) | targeted | GPT-6.1 Sol Max | C-0001, C-0002, C-0016–C-0019, C-0026 | first |
| [ASN-0002](assignments/ASN-0002-verify-nuclear-canon-statistics.md) | Verify the nuclear-map, canon, and statistical claims | verifier (two-phase) | targeted | GPT-6.1 Sol Max | C-0003–C-0015, C-0026 | any time |
| [ASN-0003](assignments/ASN-0003-relations-between-constructions.md) | Relations between Yijing constructions (supplied text, verbatim) | explorer | targeted (topics only) | Claude Opus 5.5 | — | any time |
| [ASN-0004](assignments/ASN-0004-divination-structure.md) | Fresh exploration: divination procedures and changing lines | explorer | **minimal** | Claude Opus 5.5 | — | any time |
| [ASN-0005](assignments/ASN-0005-preregistered-explanation-tests.md) | Pre-registered tests of competing explanations | specialist (two-part) | targeted | Claude Opus 5.5 | C-0003, C-0005, C-0006, C-0009–C-0012, C-0015, C-0024, C-0025 | any time |
| [ASN-0006](assignments/ASN-0006-conceptual-reset.md) | Conceptual reset: questioning the framing | paradigm-breaker | **minimal** | GPT-6.1 Sol Max | — | any time |

All six are independent and can run concurrently, each in its own fresh session. ASN-0001 comes first because it targets the highest-value claims.

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
