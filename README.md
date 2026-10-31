# Yijing Mathematical Research Program

A long-running, multi-investigator program to discover and rigorously characterize mathematical structures, relationships, and possibilities associated with the Yijing (I Ching). The intellectual stance is set by the common research charter, [`prompts/components/charter.v1.md`](prompts/components/charter.v1.md). Its aim is to expand what can genuinely be understood, not to confirm an interpretation or recover a predetermined theory.

The investigators are frontier AI models, initially **Claude Opus 5.5** and **GPT-6.1 Sol Max**. They work as independent explorers, specialists, adversarial verifiers, synthesis researchers, and paradigm-breakers, coordinated by a human through this repository. The repository is plain Markdown plus standard-library coordination tools.

> **If you are an AI investigator who has been given a research assignment, stop reading here.** Work only from the material you were given. See [`methods/context-modes.md`](methods/context-modes.md) for why.

## Why several independent investigators

- **Discovery:** different models, prompts, and amounts of context find different things. Independence protects against the program rediscovering its own assumptions.
- **Verification:** a claim checked only by its author, or only by the same model family, can share that author's blind spots. Significant claims are verified by a different model family.
- **Competition:** rival explanations are kept side by side and tested, not merged.
- **Agreement between models is evidence, not proof.**

## Repository map

```
README.md            this file
AGENTS.md, CLAUDE.md maintenance instructions for AI agents working in the repository (no findings)
FROZEN.sha256        hashes of files that must never change (originals, sent prompts, outputs)
methods/             canonical methodology (no findings)
  research-cycle.md      roles, the research cycle, assignment selection, replication, rotation
  context-modes.md       minimal / targeted / full context, and how to keep investigators isolated
  standards.md           mathematical and computational standards
  ledger-conventions.md  claim records, IDs, status vocabulary, registering and verifying
prompts/             versioned prompt components and role prompts (no findings); see prompts/README.md
context/
  objects/           neutral descriptions of the source material, safe for minimal context
  briefs/            targeted context written for specific assignments (contains findings)
ledger/              the research ledger: claims, definitions, questions, directions, disputes (findings)
investigations/      one folder per investigation: record, exact prompt, verbatim output, registration (findings)
  prompts/           legacy prompts and output present before setup, preserved unchanged
roadmap/             current plan and prepared assignments (findings in coordinator rationales)
data/                working transcriptions of historical sources, with provenance (no findings)
compute/             verification code and computational experiments
tools/yj.py          validate the repository, regenerate the claim index and coordination board, assemble packages
```

**Clean and contaminated zones.** Files that can reach a minimal-context investigator, or are loaded automatically by agent tools, contain no findings: the root documents, `methods/`, `prompts/`, `context/objects/`, `data/`, `compute/README.md`, `tools/`. Findings live only in `ledger/`, `investigations/`, `roadmap/`, and `context/briefs/`. `tools/yj.py validate` enforces this.

## Research dashboard

Open [`roadmap/dashboard.html`](roadmap/dashboard.html) for the generated visual overview, assignment search, evidence status, and Claude collaboration guide. `python3 tools/yj.py index` refreshes it alongside the Markdown indexes. For automatic updates while reviewing the research, run `python3 tools/yj.py dashboard --serve --port 0` and open its printed Local URL. Usage and source locations: [`roadmap/DASHBOARD.md`](roadmap/DASHBOARD.md).

## Current state

- Ledger **v0.1**: claims extracted from one legacy investigation (INV-0001, Claude Opus 5.5). **None is independently verified.** Orientation: [`ledger/summary.md`](ledger/summary.md) (full-context material).
- The GPT-6.1 Sol Max investigation (INV-0002) is **not in the repository**. Its record is a placeholder.
- Six assignments for cycle 1 are ready, with seven additional draft candidates: [`roadmap/README.md`](roadmap/README.md). Coordinator coverage, overlap, and prerequisites: [`roadmap/BOARD.md`](roadmap/BOARD.md). External-library priorities and the completed full-context pilot are linked from the roadmap; registration is pending.

## How to run the program

### 1. Choose an assignment

Review [`roadmap/BOARD.md`](roadmap/BOARD.md) and the current selection decision in [`roadmap/README.md`](roadmap/README.md). Pick a `ready` assignment, or write a new one from [`prompts/components/assignment-template.v2.md`](prompts/components/assignment-template.v2.md). Every assignment states its role, context mode, exact materials, recommended model, and a coordinator-only rationale. Selection criteria and redundancy rules: [`methods/research-cycle.md`](methods/research-cycle.md).

### 2. Assemble the package

```bash
python3 tools/yj.py assemble ASN-NNNN --inv INV-NNNN --out investigations/INV-NNNN-slug/prompt.md
```

This concatenates role prompt, charter, supplied materials, assignment text, and handoff protocol (order and manual alternative: [`prompts/README.md`](prompts/README.md)). For minimal-context assignments it refuses to include findings. For two-phase assignments, assemble `--part 1` and `--part 2` separately.

### 3. Run it in isolation

Paste the package into a **new conversation** with the chosen model, with persistent memory off and no project files or custom instructions attached. Do not run minimal or targeted investigations as an agent with access to this repository. Details: [`methods/context-modes.md`](methods/context-modes.md) §3.

### 4. Save and record

Save the reply verbatim as `output.md`. Never edit it. Append the hashes of the prompt and output to `FROZEN.sha256`. Fill in `record.md` from [`investigations/_template/record.md`](investigations/_template/record.md), writing `unknown` for anything you do not know (model identifier, settings). Never guess.

### 5. Register the findings

Extract each significant claim into the ledger following [`methods/ledger-conventions.md`](methods/ledger-conventions.md) §4: deduplicate without losing attribution, record evidence as it actually exists, open disputes for conflicts, and write `registration.md`. A model in the coordinator role can draft this ([`prompts/roles/coordinator.v2.md`](prompts/roles/coordinator.v2.md)); a human approves.

### 6. Verify and update claims

Send significant claims to a verifier of a **different model family** ([`prompts/roles/verifier.v1.md`](prompts/roles/verifier.v1.md), two-phase). Only that, or a qualified human check, makes a claim `verified`. Corrections become new claims that supersede the old. Nothing is deleted.

### 7. Plan the next cycle

Reconcile, update the backlog and roadmap, record the next selection decision, and include a minimal-context reset at least every second cycle. Assignment contracts, overlap review and adaptive selection are specified in [`methods/research-cycle.md`](methods/research-cycle.md) §8–9; correction impact is specified in [`methods/ledger-conventions.md`](methods/ledger-conventions.md) §6.

```bash
python3 tools/yj.py index
```

```bash
python3 tools/yj.py validate
```

Run both after every repository change. `index` refreshes the claim index, coordination board and HTML dashboard. Use `python3 tools/yj.py plan` for a read-only board and `python3 tools/yj.py impact ID` for a dependency review. Tool regression checks: `python3 -m unittest discover -s tools/tests`. External-library search and snapshot checks are documented in the roadmap; import standards are in [`methods/standards.md`](methods/standards.md) §14.

## Worked example: launching ASN-0001 with GPT-6.1 Sol Max

```bash
mkdir -p investigations/INV-0004-verify-pairing-and-palaces
cp investigations/_template/record.md investigations/INV-0004-verify-pairing-and-palaces/record.md
python3 tools/yj.py assemble ASN-0001 --part 1 --inv INV-0004 --out investigations/INV-0004-verify-pairing-and-palaces/prompt-part1.md
pbcopy < investigations/INV-0004-verify-pairing-and-palaces/prompt-part1.md   # macOS clipboard
```

1. Open a **new** GPT-6.1 Sol Max conversation with memory off and no project or files attached. Paste and send.
2. Save the reply verbatim as `investigations/INV-0004-verify-pairing-and-palaces/output-part1.md`.
3. Assemble part 2 and paste it into the **same** conversation:

   ```bash
   python3 tools/yj.py assemble ASN-0001 --part 2 --out investigations/INV-0004-verify-pairing-and-palaces/prompt-part2.md
   pbcopy < investigations/INV-0004-verify-pairing-and-palaces/prompt-part2.md
   ```

4. Save the reply as `output-part2.md`, then freeze everything that was sent or received:

   ```bash
   shasum -a 256 investigations/INV-0004-verify-pairing-and-palaces/prompt-part*.md investigations/INV-0004-verify-pairing-and-palaces/output-part*.md >> FROZEN.sha256
   ```

5. Fill in `record.md` (model as shown in the interface, date, `context_mode: targeted`, materials), set ASN-0001 to `status: launched` with `investigations: [INV-0004]`, add a row to `investigations/README.md`, register the verdicts, and run `validate`.

The same steps work in Claude: open a new conversation with no project knowledge or memory, paste the package, and save the reply.

## Preserving intellectual independence

- Give each investigator the least context that serves its assignment, and record exactly what was given.
- Keep findings out of clean files, including `AGENTS.md`, `CLAUDE.md`, and prompt templates, which can reach investigators automatically.
- Use fresh sessions. Memory features, chat projects with attached files, and repository access all leak context.
- Run minimal-context investigations regularly, including blind replications of important results.
- Never tell an investigator what answer is expected.

## Avoiding overstatement and premature closure

- An investigator saying "proven" or "verified by computation" leaves a claim at `reported`.
- Keep formal mathematics, claims about specific historical sources, historical claims, and interpretations distinct. Elegance and statistical rarity are not evidence of historical intent.
- A property of an encoding is not automatically a property of the objects. Check alternative encodings.
- A failed formulation refutes that formulation. Every negative result records what it does **not** rule out, and directions stay open unless genuinely addressed.
- Record confidence and value of further investigation separately.
- Prefer corrections and reversals, recorded openly, to silent edits.

## Provenance of this setup

- **Preserved originals:** `investigations/prompts/` (legacy prompts and the Claude Opus 5.5 output); the supplied charter and handoff protocol (`prompts/components/*.v1.md`, byte-identical); the supplied example assignment (verbatim in ASN-0003). All are hash-checked via `FROZEN.sha256` or the assignment's recorded hash.
- **Organizational infrastructure** introduced at setup (2026-10-31): directory structure, methods documents, ledger format, tooling, investigation records, roadmap.
- **Suggestions** written at setup, pending the human coordinator's review: role prompts v1, handoff protocol v2 (additive to v1), the assignment template, the INV-0001 claim extraction, and registrar notes in claim records. They were written by Claude Opus 5.5, the same model family as INV-0001's investigator.
