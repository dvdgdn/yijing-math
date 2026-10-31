---
id: INV-0002
title: GPT-6.1 Sol Max initial investigation (output not in repository)
status: missing-output
role: legacy
assignment: none
model: GPT-6.1 Sol Max
model_identifier: unknown
prompt: unknown
prompt_version: unknown
context_mode: unknown
materials: unknown
output: missing
handoff: none
date_run: unknown
registered: 2026-10-31
preceded_by: []
followed_by: []
---
# INV-0002 — GPT-6.1 Sol Max initial investigation (placeholder)

## Why this record exists

The repository setup brief states that existing investigation outputs from both Claude Opus 5.5 and GPT-6.1 Sol Max may be present. At setup (2026-10-31) the repository contained only the Claude Opus 5.5 output (INV-0001). No GPT-6.1 Sol Max output was found in the repository or among the documents supplied with the setup brief.

The setup brief lists topics covered by "the existing investigations" that do not appear in INV-0001: minimal behavioral quotients and automata-theoretic representations, noncommutation of operations, and limits on reconstructing the received ordering. **This report may be their source, but that is unconfirmed.** Those topics are recorded as directions with absent sources (DIR-001 to DIR-003). No claims are attributed to this investigation.

This ID is reserved so the report can be registered in place when found.

## Known

- Model: GPT-6.1 Sol Max (from the setup brief).

## Unknown

Prompt, supplied materials, context mode, exact model identifier, date, settings, and the output itself. The legacy layout (outputs stored as `investigations/prompts/<prompt-name>/<model>.md`) suggests it may have been run on the same legacy prompt as INV-0001, but nothing confirms this.

## When the output is found

1. Save it **verbatim** as `output.md` in this folder (or, if it is part of the legacy layout, at `investigations/prompts/yijing_paradigm_transcendence/gpt_6_1_sol_max.md`), and set `output:` to that path.
2. Add its SHA-256 to `FROZEN.sha256` (`shasum -a 256 <path> >> FROZEN.sha256`).
3. Fill in whatever provenance is actually known (prompt, date); leave the rest `unknown`.
4. Register its claims as described in `methods/ledger-conventions.md` §4. Pay particular attention to claims equivalent to INV-0001's (add a source and a derivation rather than a new record) and to conflicts (open `DSP-` entries).
5. Reassess DIR-001 to DIR-003, the verification backlog (Claude Opus 5.5 can then verify GPT-6.1 Sol Max's claims), and the roadmap.
6. Set `status: registered` and bump the ledger version.

## Relationships

- **Concurrent:** INV-0001.
