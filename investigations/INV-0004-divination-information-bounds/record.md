---
id: INV-0004
title: Divination channels, Boolean information bounds, and the robustness of hexagram labels
status: registered
role: specialist
assignment: none
model: Claude Opus 5.5
model_family: claude
independence: context-exposed
model_identifier: unknown
prompt: investigations/INV-0004-divination-information-bounds/request.md
prompt_version: continuing conversation; no assembled isolated package
context_mode: full
materials: [README.md, roadmap/literature/openai-math/transfers.md, roadmap/literature/openai-math/catalogue.json, investigations/library/openai-math-4eaee875/CONTENTS.md, investigations/library/openai-math-4eaee875/sources/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex, investigations/INV-0003-corpus-transfer-audit/output.md, investigations/INV-0003-corpus-transfer-audit/additional-attempt.md, ledger/claims/C-0016.md, ledger/claims/C-0019.md, ledger/definitions.md, context/objects/divination.md]
output: investigations/INV-0004-divination-information-bounds/output.md
handoff: in output and results.json
date_run: 2026-10-31
registered: 2026-10-31
preceded_by: [INV-0001, INV-0003]
followed_by: []
---
# INV-0004 — Divination channels and label robustness

## Summary

A full-context continuation of the repository conversation adjudicated the user's manuscript-assisted expansion. It screened the whole pinned corpus independently and applied its one clean transfer, family 119, to the divination layer. Results:

- Exact channel identifications for coin and yarrow models.
- A conditional one-bit bound for the coin oracle.
- A computer-assisted proof of the all-noise ordering trigram > palace > generation.
- Endpoint extremality of the trigram and generation labels.
- Two conjectures with exhaustive or local-search evidence.
- An independent recomputation of INV-0003's finite claims.

All results are reported; none is a verification.

## Provenance

| Item | Value |
|---|---|
| Package sent | none; `request.md` is the user's request in a continuing conversation that already contained the repository setup and its maintenance history |
| Interface | Claude desktop app (Code tab), agent with repository read/write, shell and web search |
| Model as shown | Claude Opus 5.5 (exact identifier unknown) |
| Date run | 2026-10-31 |
| Tools available | shell with Python 3.9.6; web search and fetch; no Lean |
| Follow-up messages | none |

Exploratory probes in a scratch directory preceded the frozen run (Boolean scans at n ≤ 4 on six channels; a short partition search). They are described in `output.md` §6 and not preserved as files. The frozen computation is `compute/experiments/INV-0004/divination_information.py`; its output is `results.json`.

## Supplied materials

The `materials` field lists the principal inputs. Full ambient repository context was available. Web sources consulted: three searches and the arXiv abstract page for 2609.26444 (see `output.md` §7).

## Independence evidence

None claimed. The investigator set up this repository, extracted INV-0001's claims (same model family as INV-0001), saw INV-0003 and the coordination material, and chose the territory knowing that ASN-0004 covers the same direction blind. Cross-family relative to INV-0003 (gpt) and to the external manuscripts (unnamed OpenAI model), but context-exposed. Nothing here can promote a claim to `verified` or `reproduced`.

## Deviations

Not run from an assembled package; no isolation. The investigator also acted as registrar for its own output and for INV-0003. A human or a different-family coordinator should review the registration.

## Relationships

- **Preceded by:** INV-0001 (palace encoding and C-0016), INV-0003 (pilot results and open questions).
- **Followed by:** none yet; ASN-0014 is prepared to verify R1–R5.
