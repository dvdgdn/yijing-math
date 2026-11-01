# Data and Source Provenance

This directory holds the project's working transcriptions of historical material (arrangements, tables, procedures) and the registry of sources they come from ([`sources.md`](sources.md)).

It must stay free of research findings: data files may be supplied to minimal-context investigators.

## Principles

- **Working data is not authority.** A dataset here is the project's current transcription of a source. Using it does not make it historically authoritative, and it may contain errors. Every dataset records exactly where it came from and how well it has been checked.
- **One dataset per source.** Different arrangements, editions, and reconstructions are separate datasets, never merged. When sources disagree, record the variants.
- **No silent corrections.** Correcting a dataset means a new version with a changelog line saying what changed and on what authority.

## Dataset conventions

Each dataset is a plain CSV file (UTF-8, header row) plus a sidecar `<name>.meta.md` containing:

| Field | Content |
|---|---|
| Source | `SRC-` ID, edition, volume and page, or URL with access date. |
| Transcriber | Human name, or model name with the `INV-` ID of the investigation that produced it. |
| Date | When transcribed. |
| Checking status | `unchecked`, `double-entered` (two independent transcriptions agree), or `checked against <edition>`. |
| Conventions | Line order, symbols, numbering, and any normalization of names or characters. |
| Known variants | Variant readings, and where they occur. |
| Changelog | Versioned corrections. |

Name files `<source>-<content>.v<N>.csv`, for example `received-order.v1.csv`.

## Datasets

| Dataset | Content | Source | Checking status |
|---|---|---|---|
| [`zhouyi-received-order.v1.csv`](zhouyi-received-order.v1.csv) ([meta](zhouyi-received-order.v1.meta.md)) | Received order: number, name, canon, trigrams, six lines bottom to top | SRC-001 | unchecked (two digital witnesses) |
| [`jingshi-yizhuan-eight-palaces.v1.csv`](jingshi-yizhuan-eight-palaces.v1.csv) ([meta](jingshi-yizhuan-eight-palaces.v1.meta.md)) | Eight-palace sequence with generation position and stated world line | SRC-002 | unchecked (two digital witnesses) |
| [`procedure-texts.v1.csv`](procedure-texts.v1.csv) ([meta](procedure-texts.v1.meta.md)) | Verbatim excerpts on the yarrow-stalk and coin procedures | SRC-007 | unchecked |

The raw page snapshots behind these datasets, with revision IDs and hashes, are in `investigations/INV-0008-cited-source-baselines/sources/`.

## Pending datasets

Until a dataset exists, investigators write out their own transcriptions in full in their reports, and the registrar compares transcriptions across investigations. Agreement between model transcriptions is useful but does not replace checking against a cited edition.

| Task | Dataset | Source | Notes |
|---|---|---|---|
| D-1 | Received order: number, name (pinyin and characters), lower and upper trigram, six lines bottom to top | SRC-001 | v1 exists (characters only, no pinyin). Next: check against a printed edition. |
| D-2 | Eight-palace table: palace, generation, hexagram | SRC-002 | v1 exists. Next: check against a printed edition; a third witness (四部叢刊本 scans). |
| D-3 | Mawangdui manuscript order | SRC-004 | Needed for work comparing arrangements. No transcription on Wikisource (2026-11-01); needs a published transcription. |
| D-4 | Generation-line mnemonic: earliest attestation and text | SRC-006 | Historical; needed to judge whether the mnemonic is independent of the palace tables. |
| D-5 | Shao Yong arrangements | SRC-003 | Circular and square diagrams; record which diagram and which source. |
| D-6 | Chu bamboo manuscript: which hexagrams survive and whether any order is recoverable | SRC-005 | Historical scholarship needed. |
| D-7 | Divination procedures: the yarrow-stalk procedure text and the coin method | SRC-007 | v1 exists (excerpts). Interpretations beyond Zhu Xi not collected. |

Recommended procedure for D-1 and D-2: two independent transcriptions (for example a human from a printed edition and a model in an isolated session), compared mechanically, with every disagreement resolved against the cited edition and logged in the sidecar.
