# Investigations

**Contains findings.** Do not supply anything from this directory to a minimal-context investigator.

One folder per investigation: `INV-NNNN-slug/`. An investigation is one run of one model on one assignment. Running the same assignment on two models gives two investigations.

## Contents of an investigation folder

| File | Contents | Mutable? |
|---|---|---|
| `record.md` | Metadata (front matter) and provenance. Start from [`_template/record.md`](_template/record.md); record family and isolation evidence explicitly. | Yes, to add facts as they become known. |
| `prompt.md` (or `prompt-part1.md`, `prompt-part2.md`) | The exact package sent to the model. | **Frozen** once sent. |
| `output.md` (or `output-part1.md`, `output-part2.md`) | The model's reply, verbatim, including its handoff report. | **Frozen.** Never edit, reformat, or correct. |
| `followup-N.md` | Any additional message sent in the same session, verbatim. | Frozen once sent. |
| `code/` | Code supplied by the investigator, verbatim. | Frozen. |
| `registration.md` | Registrar's result mapping, scoped attempt map, exclusions, shared inputs and follow-up decisions. Start from [`_template/registration.md`](_template/registration.md). | Yes, with dated notes. |

Frozen files are listed in [`FROZEN.sha256`](../FROZEN.sha256) and checked by `python3 tools/yj.py validate`.

## Legacy material

[`prompts/`](prompts/) holds the material present before repository setup: three legacy prompts, an editor backup file, and the Claude Opus 5.5 output (in `prompts/yijing_paradigm_transcendence/`). It is preserved unchanged in its original location. The prompts are described in [`prompts/README.md`](../prompts/README.md); the output is INV-0001.

## Index

| ID | Model | Role | Assignment | Context | Status |
|---|---|---|---|---|---|
| [INV-0001](INV-0001-claude-paradigm-transcendence/record.md) | Claude Opus 5.5 | legacy | none (legacy prompt) | unknown | registered |
| [INV-0002](INV-0002-gpt-initial-investigation/record.md) | GPT-6.1 Sol Max | legacy | none | unknown | missing-output |
| [INV-0003](INV-0003-corpus-transfer-audit/record.md) | Codex assistant; exact model unknown | synthesis | current user request; no isolated package | full, context-exposed | registered (C-0027–C-0031) |
| [INV-0004](INV-0004-divination-information-bounds/record.md) | Claude Opus 5.5 | specialist | current user request; no isolated package | full, context-exposed | registered (C-0032–C-0038) |

Add a row when you create an investigation folder.

| [INV-0005](INV-0005-verify-pairing-and-palaces/record.md) | GPT-5.6 Sol (max) | verifier | ASN-0001 | targeted, isolated | completed; registration pending |

| [INV-0006](INV-0006-verify-divination-information/record.md) | GPT-5.6 Sol (max) | verifier | ASN-0014 | targeted, isolated | running (blind phase 1) |

| [INV-0007](INV-0007-linear-information-controls/record.md) | Codex assistant; exact model unknown | specialist | ASN-0015 | full, context-exposed | completed; registration pending |

| [INV-0008](INV-0008-cited-source-baselines/record.md) | Claude Opus 5.5 | specialist | ASN-0007 | full, context-exposed | registered (C-0039–C-0041) |
