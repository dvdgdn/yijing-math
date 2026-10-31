# Mathematical and Computational Standards

These standards apply to every investigation report and every ledger record. They implement the discipline asked for in the research charter ([`prompts/components/charter.v1.md`](../prompts/components/charter.v1.md)). They do not prescribe any particular mathematics.

## 1. Definitions

- Define every object, operation, and encoding before using it. State conventions explicitly: line order, which line value is which symbol, orientation, numbering.
- When a definition encodes a traditional procedure or arrangement, say which source the encoding follows (`SRC-` ID where one exists) and where the encoding involves an interpretive choice.
- Prefer definitions that do not depend on arbitrary labels. If a result depends on an arbitrary choice, say so (§5).

## 2. Proofs and proof gaps

- A **proof** is a complete argument that a competent reader can check. Mark the end of each proof.
- A **proof sketch** is labeled as such, with the missing steps identified.
- A **proof gap** is marked explicitly at the point where it occurs ("Gap: …"), with what would close it.
- "It can be shown", "clearly", or "by computation" without the computation are not proofs.
- A proof checked only by its author remains `reported`. See [`ledger-conventions.md`](ledger-conventions.md) §3.2.

## 3. Exhaustive finite verification

Many statements here concern finite sets and can be settled by enumeration. When a claim is verified this way:

- State the exact domain enumerated (e.g. "all ordered pairs of elements of the set S, |S| = n") and confirm the enumeration covers it.
- Give the code or exact pseudocode, the input data, and the output (or its hash if large).
- State whether the computation was **actually executed** or only described. A described computation is not evidence that it was run.
- A finite verification establishes the claim for that domain only. Generalizations need separate proof.

## 4. Reproducible computation

- Prefer short, self-contained scripts using a language's standard library. Python 3 (standard library only) is the default; other languages are welcome if the script is self-contained.
- Every script states its inputs, outputs, and parameters. Randomized procedures fix and report a seed and the number of samples, and report Monte Carlo uncertainty.
- Data used by a script lives in `data/` with provenance, or is included in full in the script or report.
- Verification scripts go in `compute/verification/`; exploratory computation in `compute/experiments/`. See [`compute/README.md`](../compute/README.md).
- A verifier writes their own implementation. Re-running the originator's code checks reproducibility, not correctness.

## 5. Alternative encodings

A property of an encoding is not automatically a property of the objects encoded.

- For each significant result, identify which encoding choices it uses (labels, orientation, numerical representation, choice of operations, metric).
- Test whether the result survives natural alternatives: swapping the two line labels, reversing line order, alternative numerical encodings, alternative choices of operations that are traditionally equally justified.
- Report which results are invariant and which depend on a choice. A result that depends on an arbitrary choice may still be interesting, but it is a fact about the encoding.
- When the investigator searched over many encodings before finding a pattern, report how many (§7).

## 6. Null models

Claims that a pattern is non-random, designed, or special need a null model.

- State the null model exactly: what is held fixed, what is randomized, and the distribution.
- Justify why it is appropriate. A null model that randomizes features that were never free (for example, features forced by definitions) overstates significance. One that holds fixed the very features under test understates it.
- Where the right null model is unclear, use several and report how conclusions change. Sensitivity to the null model is itself a finding.
- Distinguish "rare under this null model" from "designed". The former is a statistical statement; the latter is a historical claim and needs historical evidence (§9).
- Prefer exact computation of null probabilities when feasible; otherwise report Monte Carlo sample sizes and uncertainty.

## 7. Multiple hypotheses and the garden of forking paths

The space of encodings, operations, and statistics is large. Patterns found by searching it are expected.

- Count, or honestly estimate, how many patterns, statistics, or encodings were examined before reporting one.
- Label analyses as **exploratory** (hypothesis-generating) or **confirmatory** (pre-specified before seeing the outcome).
- For confirmatory claims, write down the test, statistic, null model, and threshold before computing, and record that pre-specification in the report.
- Freezing a plan after inspecting the phenomenon prevents further flexibility; it does not make that phenomenon fresh confirmatory evidence. A new model or hidden p-values do not erase prior exposure or selection. Use genuinely unexamined data or consequences, with their eligibility and access fixed before testing, for confirmatory inference. When none are available, label the work a pre-specified sensitivity analysis or descriptive comparison.
- Record the program-wide search history, not only the current investigator's tests. If the earlier search space is unknown, say so; a correction for a short known list does not account for unknown selection. For simulation-based calibration of a search, the simulation must repeat the entire specified selection procedure.
- Apply a correction (Bonferroni, Holm, or a false-discovery-rate method) when reporting several tests, or explain why not.
- A p-value from an exploratory search is a description, not evidence of significance.

## 8. Definition-driven versus contingent results

- **Definition-driven** (`contingency: definitional`): follows from the chosen definitions alone. True of any system defined the same way. Often valuable as structure, but it says nothing specific about the Yijing's received material.
- **Contingent** (`contingency: contingent`): depends on facts about attested arrangements, texts, or procedures that could have been otherwise.
- Many results are **mixed**: a definitional theorem plus a contingent fact about where some object sits. Separate the two parts explicitly.

## 9. Mathematical results versus historical claims

- A theorem about a formalization establishes a mathematical fact about that formalization.
- That a historical arrangement *has* a property is a source-dependent claim: it depends on the transcription and encoding being right.
- That the property was *intended*, *known*, or *caused* the arrangement is a historical claim. It requires historical evidence such as texts, dating, or transmission history. Mathematical elegance or statistical rarity is not historical evidence of intent.
- Never invent references, dates, or historical evidence. If a historical statement comes from general knowledge, say so and flag it for checking.

## 10. Multiple historical arrangements and procedures

- The received order, the Mawangdui manuscript order, the Shao Yong arrangements, the Jing Fang palace system, divination procedures, and others are **distinct objects**. Each has its own `SRC-` entry in [`data/sources.md`](../data/sources.md).
- Every claim about an arrangement or procedure names the source it concerns. Do not transfer properties from one arrangement to another without checking.
- When sources disagree (variant readings, different editions, different reconstructions), record the variants rather than silently choosing one.
- A dataset in `data/` is the project's working transcription. **Using it does not make it historically authoritative.** Each dataset records its provenance and checking status.

## 11. Explanatory power and novelty

When assessing a proposed explanation or structure, ask:

- **Compression:** how much observed structure does it account for, relative to its assumptions and adjustable choices?
- **Out-of-sample reach:** does it reconstruct or predict features that were not used to formulate it?
- **Uniqueness:** is it one of many equally convenient descriptions?
- **Inevitability:** would any system defined the same way show it?
- **Robustness:** does it survive alternative encodings and null models?

Novelty claims:

- Say "not known to the investigator" unless a literature check was done, and describe the check.
- Rediscovering a known result is still useful as an independent derivation; report it as such.

## 12. Generalization

For each significant result, ask whether it survives generalization: other numbers of lines, other alphabets, other groups of operations, other arrangements. Report whether the Yijing case is a special instance of a general pattern, an exceptional case, or not yet known. A result that holds for every case of the general construction is a fact about the construction.

## 13. Confidence versus value of investigation

Report separately:

- **Confidence**: how well supported the claim is now.
- **Value of further investigation**: how much would be learned by testing, extending, or refuting it.

A speculative hypothesis can deserve priority because testing it would be unusually informative. A certain but trivial result may deserve none. The ledger records these separately (`status` and `value`).

## 14. Importing external research

A published or model-produced manuscript is a source to assess, not an automatic verification of a claim in this programme. Large collections need explicit selection and provenance:

- Pin the source revision and exact theorem, page/label and hypotheses. Preserve a stable reference or source snapshot and its hash. Record whether the title/abstract, theorem statement, relevant proof, code, or formal artifact was actually inspected. Do not describe retrieval or keyword screening as proof review.
- Give an explicit application map: source objects to target objects, required hypotheses, preserved relationships, and a consequence. Check input distributions, output types, independence, source variants, quantifier order, finite versus asymptotic scope, and effective constants. If a finite bound is vacuous, say so.
- Compare with an elementary or already available method. A powerful new theorem may supply no practical or mathematical improvement for the particular instance. Separate transfer feasibility, incremental benefit, implementability, and novelty of the application.
- Keep the source theorem, the transfer argument, the new consequence, and historical/source correspondence distinct. Develop a consequence conditionally when its external premise is not yet checked. Finite independent tests can establish a relevant special case without verifying the global theorem.
- Inspect what a formalization proves, including its assumptions and correspondence to the needed statement. A catalogue link is not a successful build or an independent check. Record actual compiler/artifact versions and runs, or unknown. Do not infer coverage for every companion paper from a family-level marker.
- Trace shared lemmas, code, datasets and model lineage. Papers in a collection are not independent confirmations merely because they have different titles. A correction or withdrawal triggers review of uses of that source; follow the dependency-review procedure in [`ledger-conventions.md`](ledger-conventions.md) §6.
- Search the literature for the proposed application as well as the imported theorem. State the new contribution precisely. A new vocabulary, reproof, or tiny instance of a general result may be useful, but is not automatically a novel discovery.

Reports should include a compact import contract with fields: source and revision; exact statement; source verification/review level; required hypotheses; application map; checked and missing hypotheses; elementary baseline; new deliverable; finite test; and rejection/reopening condition. Record the source-containing contract under `context/briefs/`, `investigations/`, or `roadmap/`, never in a minimal-safe template.
