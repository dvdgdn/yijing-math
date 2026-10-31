# Pinned manuscript library and how to use it

**Full-context, coordinator-only.** Start with [transfers.md](transfers.md) for the source-grounded priorities and finite evidence. The [catalogue](catalogue.json) covers all 721 manuscripts in 373 families at upstream commit `4eaee87548250b2682affda7d05d947c05554bae`; it does not claim all proofs were reviewed. The 16 theorem-statement selections, limitations, and retrieval rules are in [screening.json](screening.json).

## Search without re-reading the entire collection

```bash
python3 tools/literature.py search --catalogue roadmap/literature/openai-math/catalogue.json information contraction
python3 tools/literature.py search --catalogue roadmap/literature/openai-math/catalogue.json contingency
python3 tools/literature.py search --catalogue roadmap/literature/openai-math/catalogue.json automata
```

Terms are combined with AND and searched in titles, abstracts, family descriptions and retrieval tags. Tags overlap; they are broad retrieval aids, not relevance or novelty verdicts. Each result links to the pinned original. Inspect a plausible statement before declaring applicability.

## Rebuild and check

```bash
python3 tools/literature.py build --source investigations/library/openai-math-4eaee875/CONTENTS.md --config roadmap/literature/openai-math/screening.json --commit 4eaee87548250b2682affda7d05d947c05554bae --out roadmap/literature/openai-math/catalogue.json
python3 tools/literature.py check --source investigations/library/openai-math-4eaee875/CONTENTS.md --config roadmap/literature/openai-math/screening.json --commit 4eaee87548250b2682affda7d05d947c05554bae --catalogue roadmap/literature/openai-math/catalogue.json
```

`check` detects a stale or edited catalogue relative to the snapshot and screening judgments. Repository validation separately checks the frozen source hashes. To incorporate a new release, add a new snapshot/manifest, compare changed or withdrawn source statements, and review affected transfers and assignments. Never overwrite the frozen snapshot or infer a new source result from an unchanged title.

## Reproduce the finite probes

```bash
python3 compute/experiments/INV-0003/corpus_pilots.py --out /private/tmp/yijing-corpus-pilot-reproduction.json
```

Use a fresh scratch path. The original report, executed code and numerical output are frozen. The output records exact integer/rational evidence separately from floating-point entropy; numerical comparison is not independent verification. The general information bound remains conditional on the external source theorem. Historical correspondence and literature novelty remain separate checks.

Canonical methodology: [external-result import](../../../methods/standards.md#14-importing-external-research), [assisted/unassisted coordination](../../../methods/research-cycle.md#10-literature-assisted-development-without-convergence-on-one-framing), and [ledger registration](../../../methods/ledger-conventions.md).
