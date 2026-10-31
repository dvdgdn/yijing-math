# Instructions for AI Agents

## If you are a research investigator

If you were given a research assignment (as an explorer, specialist, verifier, paradigm-breaker, or similar), **do not read files in this repository** beyond the materials you were explicitly given. The program depends on investigators seeing only their intended context. If you are an agent with repository access and a minimal-context or targeted assignment, stop and tell the human coordinator that the investigation should be run in an isolated session (see `methods/context-modes.md`).

The rest of this file is for agents maintaining the repository.

## Repository maintenance

This is a Markdown research repository for a multi-investigator mathematical research program on the Yijing. Start with `README.md`. The canonical documents are:

| Topic | Document |
|---|---|
| Roles, research cycle, assignment selection | `methods/research-cycle.md` |
| Context modes and isolation | `methods/context-modes.md` |
| Mathematical and computational standards | `methods/standards.md` |
| Ledger format, IDs, statuses, registration, verification | `methods/ledger-conventions.md` |
| Prompt assembly and versioning | `prompts/README.md` |

Do not restate these documents elsewhere. Link to them.

## Rules

1. **Never modify a frozen file.** `FROZEN.sha256` lists them: legacy prompts and outputs, supplied documents, sent prompt packages, investigation outputs. Never reformat, correct, or "clean up" an original output.
2. **Never fabricate.** No invented model identifiers, dates, settings, citations, historical evidence, computational results, or verification outcomes. Write `unknown`.
3. **Status discipline.** An investigator's assertion leaves a claim `reported`. `verified` requires a verifier from a different model family than every originator, or a qualified human. Agreement between models is not proof.
4. **Never delete or renumber** claims, questions, directions, disputes, investigations, or assignments. Change status and link successors.
5. **Negative results are scoped.** Never close a research direction because one formulation failed.
6. **Keep clean files clean.** `README.md`, `AGENTS.md`, `CLAUDE.md`, `methods/`, `prompts/`, `context/objects/`, `data/`, `compute/README.md`, and `tools/` must contain no findings, ledger IDs, failed hypotheses, or preferred representations. Findings belong only in `ledger/`, `investigations/`, `roadmap/`, `context/briefs/`.
7. **Distinguish** formal results, source-dependent claims, historical claims, and interpretations. Distinguish original material, setup infrastructure, and suggestions.
8. **Validate** after every change: `python3 tools/yj.py index` then `python3 tools/yj.py validate`.
9. **Do not push, rewrite history, or launch model investigations** unless the human coordinator asks.
10. **Prompt versions are immutable once sent.** Improve a prompt by creating the next version (`prompts/README.md` §4).
