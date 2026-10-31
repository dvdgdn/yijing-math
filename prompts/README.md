# Prompt System

This directory holds the reusable, versioned text that is sent to investigators. Everything here is model-agnostic plain Markdown, and **must stay free of research findings** (see [`methods/context-modes.md`](../methods/context-modes.md) §4), because it is supplied in minimal-context packages.

## 1. Components of an investigation package

A package is assembled in this order. Each part is separated by a horizontal rule (`---`) on its own line.

| # | Part | Source | Notes |
|---|---|---|---|
| 1 | Role prompt | `prompts/roles/<role>.vN.md` | Front matter is stripped; only the body is sent. |
| 2 | Common research charter | `prompts/components/charter.v1.md` | Sent verbatim. |
| 3 | Supplied materials | Files listed in the assignment's `materials` | Each preceded by a heading `## Supplied material: <path>`. Front matter is stripped. |
| 4 | Assignment | Text between `<!-- BEGIN ASSIGNMENT -->` and `<!-- END ASSIGNMENT -->` in the assignment file | Rationale and coordinator notes are never sent. |
| 5 | Handoff protocol | `prompts/components/handoff-protocol.v3.md` | Sent verbatim; extends v2 with a compact search log and reuse contracts. |

For a **two-phase verification**, part 2 of the package contains only the text between `<!-- BEGIN ASSIGNMENT PART 2 -->` and `<!-- END ASSIGNMENT PART 2 -->`, followed by the files in `materials_part2`. Send it in the same conversation after the verifier has finished phase 1.

### Assembling with the tool

```bash
python3 tools/yj.py assemble ASN-0001 --part 1 --out investigations/INV-NNNN-slug/prompt-part1.md
```

The tool prints the SHA-256 of what it wrote. All front matter, including coverage and overlap fields, is excluded; only the marked assignment text is sent. `--overwrite` never permits replacing a frozen file. Assembly is a preview operation and does not launch an investigation. For minimal-context assignments it refuses to include ledger, investigation, roadmap, or brief material, or any text containing ledger IDs, and it warns about vocabulary listed in `ledger/leak-terms.txt`.

### Assembling by hand

Open the files in the order above, paste them into one document with `---` between parts, and do not include anything else. Save exactly what you sent as `prompt.md` in the investigation folder.

## 2. Roles

| Role | File | Default context | When to use |
|---|---|---|---|
| Independent explorer | [`roles/explorer.v1.md`](roles/explorer.v1.md) | minimal | Open exploration of a territory from the objects alone. Use for independent discovery and blind replication. |
| Specialist investigator | [`roles/specialist.v1.md`](roles/specialist.v1.md) | targeted | A specific question that benefits from selected prior results. |
| Adversarial verifier | [`roles/verifier.v1.md`](roles/verifier.v1.md) | targeted, two-phase | Checking specific claims made by a different model family. Phase 1 gets statements and definitions only; phase 2 gets the original evidence. |
| Synthesis investigator | [`roles/synthesis.v1.md`](roles/synthesis.v1.md) | full | Relating results across investigations; testing whether unifications are real. |
| Paradigm-breaking investigator | [`roles/paradigm-breaker.v1.md`](roles/paradigm-breaker.v1.md) | minimal | Conceptual reset; questioning objects, representations, and framings. A framing-exposed variant supplies the program's working assumptions (as a brief), not its results. |
| Research coordinator | [`roles/coordinator.v2.md`](roles/coordinator.v2.md) | full | Drafting reconciliation of new reports into the ledger, and drafting next assignments. A human approves. |

Role prompts deliberately do not repeat the charter. The charter carries the shared intellectual stance; the role prompt says what is specific to the role; the assignment says what to work on; the handoff protocol says how to report.

## 3. Component registry and provenance

"Supplied" means the text came from the human coordinator's earlier research-design discussion. "Legacy" means it was present in the repository before setup. "Setup" means it was written during repository setup and is a suggestion until the human coordinator reviews it.

| File | Version | Origin | Status | Notes |
|---|---|---|---|---|
| [`components/charter.v1.md`](components/charter.v1.md) | 1 | Supplied | frozen | Byte-identical to the supplied file `writing-block (3).md` (SHA-256 `c4ebf703…`). |
| [`components/handoff-protocol.v1.md`](components/handoff-protocol.v1.md) | 1 | Supplied | frozen | Byte-identical to the supplied file `writing-block (1).md` (SHA-256 `6cd9a861…`). |
| [`components/handoff-protocol.v2.md`](components/handoff-protocol.v2.md) | 2 | Setup | draft, retained | v1 unchanged, plus an appended section "Additional reporting requirements" (report header, executed-vs-described computation, full data transcriptions, extra registry columns for domain, contingency, scope, and prior-claim IDs). Purely additive. Use v1 if you prefer the original. |
| [`components/assignment-template.v1.md`](components/assignment-template.v1.md) | 1 | Setup | draft | Generalized from the supplied example assignment `writing-block (2).md` (SHA-256 `a88a6402…`), whose text is preserved verbatim as the assignment text of `roadmap/assignments/ASN-0003-relations-between-constructions.md`. |
| [`components/handoff-protocol.v3.md`](components/handoff-protocol.v3.md) | 3 | Maintenance (2026-10-31) | draft, default | v2 unchanged, plus search history, evidence lineage, qualified novelty/use, and next-step contracts. |
| [`components/assignment-template.v2.md`](components/assignment-template.v2.md) | 2 | Maintenance (2026-10-31) | draft, default | Coordinator fields and decision/stopping criteria under `methods/research-cycle.md` §8–9. |
| [`roles/coordinator.v2.md`](roles/coordinator.v2.md) | 2 | Maintenance (2026-10-31) | draft, default | v1 plus coverage, search-log, dependency-review and adaptive selection checks. |
| `roles/*.v1.md` | 1 | Setup | draft | Written during setup. `paradigm-breaker.v1.md` adapts the legacy prompts below; `verifier.v1.md` borrows the credence/confidence separation idea from the legacy `credence_confidence_separation.md`. |

Legacy prompts, preserved unchanged in their original location (`investigations/prompts/`):

| File | Description | Used by |
|---|---|---|
| `investigations/prompts/paradigm_transcendence.md` | Domain-general "frontier investigator" prompt with an `[INSERT HERE]` slot. | No recorded use. |
| `investigations/prompts/yijing_paradigm_transcendence.md` | Yijing-specific adaptation of the above, with an `[INSERT HERE]` slot for starting material. | INV-0001 (inferred from directory layout; see its record). |
| `investigations/prompts/credence_confidence_separation.md` | Prompt for evaluating a supplied statement conditionally, then assessing its truth, separating credence from confidence. | No recorded use. |
| `investigations/prompts/paradigm_transcendence.md~` | Editor backup file. Byte-identical to `credence_confidence_separation.md`, which suggests `paradigm_transcendence.md` was created by editing a copy of it. Preserved as found. | — |

SHA-256 hashes of all frozen files are in [`FROZEN.sha256`](../FROZEN.sha256).

## 4. Versioning rules

1. Files are named `<name>.v<N>.md`. The version number in the filename is authoritative.
2. A version is **frozen** once it has been sent to any investigator, or if it is a preserved original. Frozen files are listed in `FROZEN.sha256` and are never edited. `tools/yj.py validate` fails if a frozen file changes.
3. To improve a prompt, copy it to `v<N+1>`, edit, set `status: draft`, record `derived_from`, and add a row to the registry above describing the change. Do not delete old versions.
4. Draft versions (never sent) may be edited in place.
5. Every investigation record names the exact prompt versions used, and the investigation folder keeps the assembled package verbatim. The package, not the component files, is the definitive record of what an investigator saw.
6. Prompt changes that alter what investigators are asked to do (not just wording) should be noted in `ledger/CHANGELOG.md`, because they can change what kinds of results appear.

## 5. Writing prompts that work across models

- Plain Markdown, no model-specific syntax, tools, or features.
- State the role, the material supplied, the task, and the reporting format explicitly. Do not rely on system prompts or persistent instructions; the package is the whole instruction.
- Avoid encouraging any particular theory, representation, or level of ambition beyond the charter's.
- If an assignment needs code execution, say so in the assignment and accept reports that describe code without running it, provided they say so.
