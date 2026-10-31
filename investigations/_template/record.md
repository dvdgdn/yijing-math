---
id: INV-NNNN
title: <Short title>
status: prepared
role: <explorer | specialist | verifier | synthesis | paradigm-breaker | coordinator>
assignment: ASN-NNNN
model: <model name as offered by the provider, e.g. "GPT-6.1 Sol Max">
model_identifier: unknown
prompt: investigations/INV-NNNN-slug/prompt.md
prompt_version: <e.g. role verifier.v1 + charter.v1 + handoff-protocol.v2>
context_mode: <minimal | targeted | full>
materials: [<exact list of supplied files>]
output: investigations/INV-NNNN-slug/output.md
handoff: in output
date_run: unknown
registered: none
preceded_by: []
followed_by: []
---
# INV-NNNN — <Short title>

<!-- Copy this folder to investigations/INV-NNNN-slug/. Use the next unused number. Fill in only what is actually known; write "unknown" otherwise. Never invent model identifiers, dates, or settings. -->

## Summary

<Two or three sentences, written after the output is in: what the investigation did and reported.>

## Provenance

| Item | Value |
|---|---|
| Package sent | `prompt.md` (SHA-256: <from tools/yj.py assemble>) |
| Interface | <e.g. "chat web interface, new conversation, memory off, no project files"> |
| Model as shown in the interface | <exact text shown, or unknown> |
| Date run | <YYYY-MM-DD, or unknown> |
| Tools available to the model | <e.g. code execution on/off, web search on/off, unknown> |
| Follow-up messages | <none, or a list with their exact text saved as followup-N.md> |

## Supplied materials

<Exact list, matching the assignment's materials (and materials_part2 for two-phase work).>

## Deviations

<Anything that departed from the assignment or the isolation procedure. "None" if none.>

## Relationships

- **Preceded by:** <INV IDs whose results were supplied, or that this replicates>
- **Followed by:** <filled in later>

## Registration

<Filled in at registration: ledger version and claim IDs. Mapping in registration.md.>
