# INV-0001 — Registration Notes

Registrar: repository setup run by Claude Opus 5.5 (2026-10-31), acting as registrar. **The registrar is the same model family as the originating investigator.** The extraction below should be reviewed by the human coordinator, or by a GPT-6.1 Sol Max coordinator run, before it is relied on heavily.

Original output: `investigations/prompts/yijing_paradigm_transcendence/claude_opus_5_5.md` (unchanged).

## Mapping of local results to ledger claims

| Location in INV-0001 | Local label | Ledger IDs | Action |
|---|---|---|---|
| §4 Theorem 1, sentence 1 | Theorem 1 (σ involution) | C-0001 | new |
| §4 Theorem 1, sentences 2–3 | Theorem 1 (King Wen pairs = σ-orbits) | C-0002 | new |
| §4 Theorem 2, para 1 | Theorem 2 (canon balance) | C-0003 | new |
| §4 Theorem 2, para 2 | 30/34 explanation | C-0004 | new |
| §6 "Theorems 1 and 2" | balance not rare (22%) | C-0005 | new |
| §4 Theorem 2, para 3 | "second observation" (doubled trigrams) | C-0006 | new |
| §4 Theorem 3, sentence 1 | Theorem 3 (N linear, N⁴ = N²) | C-0007 | new |
| §4 Theorem 3, Fitting paragraph | Theorem 3 (decomposition, A) | C-0008 | new |
| §4 Theorem 3, "In King Wen numbering" | A = {1, 2, 63, 64} | C-0009 | new |
| §4 Theorem 3, null model paragraph | endpoint probability 0.0021, 1/31 | C-0010 | new |
| §4 "But H4 fails" | H4 statistics | C-0011 | new |
| §4 "The endpoint fact is equally explained" | A = constant ∪ all-correct/incorrect | C-0012 | new |
| §4 H3 paragraph, sentence 1 | within-pair distances even | C-0013 | new |
| §4 H3 paragraph, sentence 2 | between-pair distribution, no 5 | C-0014 | new |
| §4 H3 paragraph, sentences 3–4 | no-5 p = 0.043, not significant | C-0015 | new |
| §5 Theorem 4 + proof | palace transversal | C-0016 | new |
| §5 procedure description + worked example | D encodes the procedure; matches tables | C-0017 | new |
| §5 Corollary A | generation from trigram agreement; mnemonic | C-0018 | new |
| §5 Corollary B; §7 decisive check | reversal swaps generations | C-0019 | new |
| §6 "Generalization" | 2k lines | C-0020 | new (as conjecture: underspecified) |
| §3 ambitious conjecture; §6 refutation | V-equivariance refuted | C-0021 | new |
| §6 revised version; §7 | stratification conjecture | C-0022 | new |
| §6 last sentence of refutation paragraph | Mawangdui order organized by upper trigram | C-0023 | new |
| §3 H2; §7 assessment | H2 | C-0024 | new |
| §3 H0 | H0 | C-0025 | new |
| §2 | label-swap invariance | C-0026 | new |

New definitions: DEF-001 to DEF-016 (DEF-016 is the registrar's gloss of a term used informally). New questions: Q-001 to Q-008. Directions: DIR-004, DIR-005, DIR-009, DIR-010, DIR-011 draw on this investigation. Disputes: DSP-001 to DSP-003.

## Considered and not registered

| Location | Content | Reason |
|---|---|---|
| §3 H1 | Shao Yong's order is base-2 counting | True by construction; INV-0001 itself says it "explains nothing about King Wen". Recorded here only. |
| §2 | "Line order is not arbitrary… that dependence is earned" | Methodological position, not a claim. Noted in C-0026's scope. |
| §2 | Hamming distance "plays no explanatory role elsewhere" | Vague; partially covered by C-0015. |
| §3 H5 | Han procedures are coset constructions relative to P | Hypothesis statement; its content is registered as C-0016. |
| §7 | Null model is the weakest assumption | Recorded as an objection in C-0005, C-0010, C-0011, C-0015, and as Q-004. |
| §7 | Pre-registered grammar of operators and statistics | Recorded as Q-002 and DIR-004. |
| §7 | "The theorems are certain" | The investigator's confidence statement. It does not change status; all claims are `reported`. |

## Issues noted during extraction

1. **Blanket computational claim.** The output states: "All claims below were checked by exhaustive computation over the 64 hexagrams." It supplies no code, data, or output. The statement cannot apply literally to the null-model probabilities (which concern random orderings, not the 64 hexagrams) or to the historical claims. Each record states the evidence as it actually exists.
2. **No data transcription.** The received order, the palace tables, and the mnemonic are used without a cited source or a written-out transcription. Every source-dependent claim inherits this gap.
3. **Ambiguities** are recorded in C-0010 (event definition), C-0011 (statistic definitions), C-0014 (meaning of "between pairs"), C-0020 (generalized nuclear map undefined), and C-0021 (imprecise conjecture).
4. **Registrar notes** (labeled in each record) flag possible prior literature (C-0002, C-0003, C-0009), a suspected exact value (C-0010), an exactly computable probability (C-0005), and a possible dependence between C-0006 and C-0004. These are pointers for verifiers, not findings.

## Agreements and contradictions with other investigations

None assessable: INV-0002's output is absent.
