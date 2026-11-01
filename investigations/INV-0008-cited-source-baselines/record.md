---
id: INV-0008
title: Cited source baselines for the received order, the eight palaces and the divination procedure
status: registered
role: specialist
assignment: ASN-0007
model: Claude Opus 5.5
model_family: claude
independence: context-exposed
model_identifier: unknown
prompt: investigations/INV-0008-cited-source-baselines/request.md
prompt_version: continuing conversation; ASN-0007 assignment text used as scope; no assembled package
context_mode: full
materials: [roadmap/assignments/ASN-0007-source-baselines.md, data/README.md, data/sources.md, ledger/definitions.md, ledger/claims/C-0002.md, ledger/claims/C-0017.md, ledger/claims/C-0018.md, ledger/claims/C-0033.md, investigations/INV-0005-verify-pairing-and-palaces/phase1/data/received_order.tsv, investigations/INV-0005-verify-pairing-and-palaces/phase1/data/eight_palaces_source.tsv]
output: investigations/INV-0008-cited-source-baselines/output.md
handoff: in output, build-results.json and comparison-results.json
date_run: 2026-11-01
registered: 2026-11-01
preceded_by: [INV-0001, INV-0005]
followed_by: []
---
# INV-0008 — Cited source baselines

## Summary

The user asked to begin research on the highest-value direction. The coordinator conversation chose ASN-0007, for three reasons:

- Every source-dependent claim rested on uncited transcriptions.
- INV-0005's blind phase 1 had just recorded that Jing Fang attribution stays undetermined without a cited table.
- The two isolated verifications were already running in the GPT family.

Results:

- Three cited working datasets were built from hash-pinned Wikisource snapshots: received order, eight palaces, and procedure texts.
- Each was compared across two digital witnesses.
- After freezing, the datasets were compared with INV-0005's blind transcriptions and with the checkable source-dependent ledger statements.

All results are reported. Nothing is verified.

## Provenance

| Item | Value |
|---|---|
| Package sent | none; `request.md` is the user's message in a continuing conversation that already contained the repository setup, INV-0004 and its adjudication |
| Interface | Claude desktop app (Code tab), agent with repository read/write, shell, web search and fetch |
| Model as shown | Claude Opus 5.5 (exact identifier unknown) |
| Date run | 2026-11-01 |
| Tools | Python 3.9.6; zh.wikisource.org MediaWiki API (184 pages, revisions in `sources/manifest.json`); web search for the mnemonic; ctext.org API refused unauthenticated access and was not used |
| Follow-up messages | none |

**Exploratory steps before the frozen run.** Probe fetches and parser prototypes ran in a scratch directory. A first snapshot of 178 pages, taken by the same script before redirect targets and coin sources were added, was used only to design parsers. The frozen snapshot is a single later run of the final `fetch_sources.py`.

**Order of operations.**
1. Snapshot.
2. Parser fixes, recorded in output §7.
3. Datasets, snapshots and build scripts hashed into `FROZEN.sha256`.
4. Only then were INV-0005's transcriptions read for content and the comparisons run.

## Independence evidence

None claimed. The investigator is the same family as INV-0001's originator, set up this repository, and authored INV-0004.

INV-0005's phase-1 transcriptions were saved and frozen by another coordinator session before this investigation read them. Nothing produced here was sent to INV-0005 or INV-0006.

The source parse is mechanical and does not use the claims it was later compared with. But the comparison code implements definitions taken from the ledger, so the comparison is a recomputation, not an independent derivation.

## Deviations

- The assignment specifies targeted context; this run had full context.
- Source checking is limited to two digital witnesses per text. No printed edition was consulted, so every dataset is `unchecked`.
- The Mawangdui (D-3) and Chu (D-6) packages were not built: no accessible transcription was found.
- The mnemonic attestation (D-4) remains unknown.
- The investigator also registered its own output. A human or GPT-family coordinator should review `registration.md`.

## Relationships

- **Preceded by:** INV-0001 (the claims whose source-dependent statements were recomputed); INV-0005 (its saved phase-1 transcriptions were compared after freezing).
- **Followed by:** none yet. Proposed next steps are in output §9.
