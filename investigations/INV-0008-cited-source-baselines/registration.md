# INV-0008 — Registration

Registrar: Claude Opus 5.5 (the originator), 2026-11-01. **This is a self-registration. A human or GPT-family coordinator should review the extraction.**

The original output is `output.md`, together with `build-results.json` and `comparison-results.json`. Never edit any of them.

## Local results to ledger

| Local result | Exact statement and assumptions | Related existing record | Ledger ID and action | Evidence and verification limits |
|---|---|---|---|---|
| S1 | D-1 received order from two witnesses; full agreement | SRC-001; C-0002 etc. (inputs) | dataset `data/zhouyi-received-order.v1.csv`; no claim | executed parse; unchecked against print |
| S2 | Xugua's 61 introduced names follow received positions 3–30, 32–64 | C-0002 | C-0039, new reported | two digital witnesses |
| S3 | D-2 palace table from two Jingshi witnesses; doubled heads; stated world line (6, 1, 2, 3, 4, 5, 4, 3) by position | C-0016, C-0017, C-0018 | C-0040, new reported; dataset `data/jingshi-yizhuan-eight-palaces.v1.csv` | 57 explicit, 7 indirect, 1 emended reading |
| S4 | Unsourced editorial palace table agrees in membership; different palace presentation order | — | recorded in the D-2 sidecar as a variant; no claim | secondary |
| S5 | Zhu Xi's case counts give the yarrow-standard law; remainder and hung-stalk conventions attested; no split law | C-0032, C-0033, DEF-017, Q-011 | C-0041, new reported; dataset `data/procedure-texts.v1.csv` | one witness; equal case weighting is interpretive |
| S6 | Mnemonic attestation not found | C-0018, Q-008 | lead added to Q-008 and SRC-006; no claim | bounded search |
| B | C-0002, C-0003, C-0004, C-0006, C-0009, C-0017(b), C-0018 hold on cited data; INV-0005's transcriptions match | those claims | dated verification-log notes; statuses unchanged | same family as originator; context-exposed recomputation |

Notes were also added to DEF-011, DEF-017, Q-008, Q-011, DIR-005, DIR-006, DIR-007 and DIR-008. SRC-001, SRC-002, SRC-006 and SRC-007 now carry citations to digital witnesses.

## Considered and not registered

| Location | Result or idea | Reason / future use |
|---|---|---|
| §3 A4 | Palace presentation order differs between the Jingshi witnesses and later tables, including INV-0005's | Affects no claim; recorded as a dataset variant. |
| §5 | Xici arrangement differs between witnesses | Textual variant only; recorded in the D-7 sidecar. |
| §8 | Najia, guaqi and Shao Yong intake leads | Intake notes on DIR-005 and DIR-008; no data built. |

## Attribution, novelty and shared inputs

- All witnesses are Wikisource volunteer transcriptions. Their mutual independence is plausible but not established.
- No novelty is claimed for any result. The palace table, the Xugua order and the 1/16, 5/16, 7/16, 3/16 derivation are traditional or standard.
- The comparisons implement ledger definitions, so they share the encoding (DEF-001) with the claims they check.

## Dependency and disagreement review

- No disagreement with any registered record.
- C-0017 and C-0018 rest on D-1 and D-2 for their source side. If a printed-edition check changes a row, revisit C-0040 and these notes.
- C-0021 depends on C-0017. It is unaffected, since C-0017(b) agrees with the cited data.
- INV-0005 (ASN-0001) is the protocol verification of C-0002 and C-0017–C-0019. Nothing here substitutes for it, and nothing here was supplied to it.

## Coverage and next selection

- ASN-0007 is completed, with the gaps listed in its completion note.
- The cheapest decisive next step is a human check of D-1 and D-2 against a printed edition.
- C-0017(a) can be checked against the procedure as the Jingshi text narrates it, entry by entry.
- Q-008 needs full-text corpora beyond Wikisource.
