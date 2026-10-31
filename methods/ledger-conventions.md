# Ledger Conventions

This is the canonical specification of the research ledger: identifiers, claim records, status vocabulary, and the rules for registering, verifying, correcting, and retiring claims. The ledger itself lives in [`ledger/`](../ledger/).

The ledger records what the program has *claimed*, on what evidence, and with what verification. It is not a list of truths. A record exists so that future investigators can see exactly what was asserted, by whom, on what basis, and what has and has not been checked.

## 1. Identifiers

Identifiers are stable. They are never reused, never renumbered, and never deleted. A retired item keeps its ID and gets a terminal status.

| Prefix | Object | Where | Example format |
|---|---|---|---|
| `INV-` | Investigation: one run of one model on one assignment | `investigations/INV-NNNN-slug/record.md` | 4 digits |
| `ASN-` | Assignment: a prepared research task, before or after launch | `roadmap/assignments/ASN-NNNN-slug.md` | 4 digits |
| `C-` | Claim: theorem, observation, conjecture, negative result, etc. | `ledger/claims/C-NNNN.md` | 4 digits |
| `DEF-` | Definition or encoding used by claims | `ledger/definitions.md` | 3 digits |
| `Q-` | Open question (precise enough to be answered) | `ledger/questions.md` | 3 digits |
| `DIR-` | Research direction or area, including unexplored ones | `ledger/directions.md` | 3 digits |
| `DSP-` | Dispute: contradictory claims or competing explanations | `ledger/disputes.md` | 3 digits |
| `SRC-` | Historical or textual source: an arrangement, text, or procedure | `data/sources.md` | 3 digits |

Investigators use **local IDs** in their reports (for example `L1`, `T4`, `Theorem 2`). The registrar maps local IDs to ledger IDs in the investigation's `registration.md`. The mapping is how attribution survives deduplication.

## 2. Claim records

One claim per file: `ledger/claims/C-NNNN.md`. Each file has a flat front-matter block followed by fixed sections.

### 2.1 Front matter

The front matter uses a deliberately small YAML subset: one `key: value` per line; values are plain text or inline lists `[a, b]`; no nesting, no multi-line values. Long text belongs in the body. (GitHub renders this block as a table; `tools/yj.py` parses it with the standard library only.)

```yaml
---
id: C-NNNN
title: Short descriptive title
type: theorem
status: reported
polarity: positive
domain: formal
contingency: definitional
evidence: proof in source; exhaustive computation reported, code not supplied
sources: [INV-NNNN]
verifiers: []
depends_on: [DEF-NNN, C-NNNN]
related: []
competes_with: []
supersedes: []
superseded_by: []
value: medium
registered: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

| Field | Meaning |
|---|---|
| `type` | What kind of claim this is (§3.1). |
| `status` | Its verification state (§3.2). Independent of `type`. |
| `polarity` | `positive` (asserts a structure or relation exists), `negative` (asserts something fails or was ruled out), `inconclusive` (evidence does not decide). |
| `domain` | `formal` (about defined mathematical objects only), `source-dependent` (about a specific attested arrangement, text, or procedure as encoded; true only if the transcription and encoding are right), `historical` (about origin, dating, authorship, transmission, or intention), `interpretive` (about meaning; speculative by nature). |
| `contingency` | `definitional` (follows from the chosen definitions alone), `contingent` (depends on contingent features of the sources), `mixed`, or `n/a`. |
| `evidence` | Short description of the evidence *as it exists*, including what is missing (e.g. "computation reported; code not supplied"). |
| `sources` | Investigations that asserted or independently derived the claim. Every claim needs at least one. |
| `verifiers` | Verification investigations (`INV-…`) or human verifiers (`human:Name`). Empty until verification happens. |
| `depends_on` | Definitions and claims this claim uses. |
| `related`, `competes_with` | Links to related claims and to claims offering incompatible or rival explanations. |
| `supersedes`, `superseded_by` | Correction and generalization chain. |
| `value` | Value of further investigation: `high`, `medium`, `low`, `unknown`. Deliberately separate from `status`; a weakly supported claim can be highly worth testing. |
| `registered`, `updated` | ISO dates. |

### 2.2 Body sections

Every claim file has these level-2 headings, in this order. Write "None recorded." rather than deleting a section.

1. `## Statement`: the exact mathematical statement, in the originator's terms where possible. If the registrar restated it, say so and give the original location.
2. `## Definitions and assumptions`: definitions used (by `DEF-` ID where available), encodings, data, and any assumptions, including historical ones.
3. `## Provenance`: each source investigation, model, and location (section, theorem number). List independent derivations separately; they are not verifications.
4. `## Evidence and verification`: the evidence as reported; then a **verification log** listing each verification attempt with verifier, method, date, and verdict.
5. `## Scope and limitations`: what the claim covers and does not. **Negative and inconclusive claims must contain a line beginning `Not ruled out:`** that states what the result leaves open.
6. `## Objections and alternatives`: counterexamples, objections, simpler explanations, rival claims.
7. `## Further investigation`: recommended next steps, including what would raise or lower confidence.

## 3. Vocabularies

### 3.1 Claim types

| `type` | Use for |
|---|---|
| `theorem` | A precise statement with a claimed proof (which may be reported only). |
| `construction` | An explicit object or procedure, with stated properties. |
| `computational-observation` | A fact established (or claimed) by finite computation over specified data. |
| `statistical-result` | An assessment against a stated null model. Must record the statistic, null model, value, and multiplicity handling. |
| `conjecture` | A precise statement believed but unproven. |
| `hypothesis` | An explanatory or speculative proposal, possibly not yet precise. |
| `counterexample` | A specific object that refutes a specific statement. |
| `impossibility` | A proof that something cannot hold under stated conditions. |
| `bounded-search` | An unsuccessful search, with the search space stated exactly. |
| `inconclusive` | Evidence that does not decide the question, with the reason. |
| `historical-claim` | A claim about history, sources, dating, transmission, or intention. |
| `interpretation` | A proposed meaning or reading. |

### 3.2 Verification status

| `status` | Meaning | Requirements |
|---|---|---|
| `reported` | Asserted by its source investigation(s). Not independently checked. **An investigator's statement that something is proven or computed leaves the claim at `reported`.** | At least one source. |
| `in-verification` | Assigned to a verification investigation that has not yet reported. | Name the assignment in the verification log. |
| `reproduced` | Independently re-derived or recomputed in a separate, isolated session, with agreement, but **by the same model family as an originator** or without adversarial audit. | At least one verifier. |
| `verified` | Independently checked by an investigator of a **different model family** from every originator, or by a qualified human, following the verifier protocol, with no unresolved objection. | At least one verifier meeting that condition. Metadata prerequisites checked by `tools/yj.py validate`; the human still reviews the actual audit and verdict. |
| `disputed` | Verifications disagree, or a substantive objection is unresolved. | Open a `DSP-` entry. |
| `refuted` | Shown false *as stated*. Refutes this formulation only. | Link the counterexample or impossibility claim. |
| `superseded` | Replaced by a corrected or generalized claim. | `superseded_by` set. |
| `withdrawn` | Withdrawn by the originator or registrar, e.g. as an extraction error. | Reason in the body. |

Notes:

- Agreement between models is evidence, not proof. Two models agreeing that a statement is proven does not make it `verified` unless one of them verified the other's work under the verifier protocol.
- For conjectures and hypotheses, the status describes what the record itself asserts: that the statement is open and supported by the stated evidence. If a conjecture is later proven, register a new `theorem` claim that `supersedes` it; do not retype the old record.
- `verified` does not mean certain. It means independently checked, with the log saying how. Record `model_family` explicitly on investigations; unknown provenance cannot establish cross-family independence. Record `independence: isolated` only with evidence of isolation in the investigation record. A model verifier must have completed its verification and must not also be an originator of the same claim. The validator checks these necessary conditions; metadata cannot establish that a proof audit was adequate.
- Mathematical correctness, source correspondence, and significance require separate verdicts in the verification log. State which aspects remain unchecked. Do not give a mixed claim an unqualified `verified` status while a required aspect remains unresolved; split distinct assertions into successor records when needed.

## 4. Operations

### Registering an investigation's claims

1. Read the original output. Never edit it.
2. For each significant claim, search the ledger (`ledger/INDEX.md`, then candidate records) for an equivalent claim.
   - **New claim:** create `C-NNNN.md` with status `reported`.
   - **Equivalent to an existing claim:** add the investigation to `sources`, and record the new derivation under Provenance. An independent derivation is evidence of robustness, not verification. Do not promote the status. If adding an originator changes the model-family independence of an existing verification, review and record whether `verified` still qualifies before retaining it.
   - **Equivalent but differently formulated:** keep one record, add the alternative formulation under Statement, and note any difference in assumptions. If the formulations are not provably equivalent, make two records and link them with `related`.
   - **Conflicts with an existing claim:** register it, link both with `competes_with`, and open a `DSP-` entry.
3. Write `registration.md` in the investigation folder: a table mapping each local result to ledger IDs, plus every result considered and *not* registered, with the reason. Use [`investigations/_template/registration.md`](../investigations/_template/registration.md). Also preserve a compact map of attempted approaches and their exact bounds, evidence locations, stopping reasons, and untested variations. A failed approach can prevent repeated work without warranting a separate claim; a significant negative result still needs a claim record.
4. Add new open questions (`Q-`), directions (`DIR-`), and disputes (`DSP-`).
5. Update assignment coverage and outcomes, record the next selection decision under [`research-cycle.md`](research-cycle.md) §8–9, then run `python3 tools/yj.py index` followed by `python3 tools/yj.py validate`.

### Verifying a claim

1. Create a verification assignment (role: verifier) assigned to a model family that did not originate the claim.
2. On return, add the verification investigation to `verifiers`, write a verification-log entry, and set status by the table in §3.2.
3. If the verifier corrected the claim, register the corrected statement as a new claim that `supersedes` the old one, unless the correction is purely typographical.

### Correcting, disputing, reversing

- Never delete a claim or rewrite its history. Change status, add log entries, and link successors.
- A refutation applies to the formulation refuted. If a failed formulation belongs to a broader direction, record under `Not ruled out:` what remains open, and leave the `DIR-` entry open unless the whole direction has genuinely been addressed.
- Reversals are normal. Record the reason and the evidence in the claim's log, and bump the ledger version in `ledger/CHANGELOG.md`.

### Negative results

A negative result is only useful if a future investigator can tell exactly what was excluded. Record:

- the exact statement tested, encoding, data, and operations;
- the type of failure: counterexample, impossibility proof, bounded search (with bounds), or statistically inconclusive (with power considerations where possible);
- `Not ruled out:` the nearby formulations, encodings, generalizations, and sources the result does not touch.

## 5. Ledger versions

The ledger has a version recorded at the top of `ledger/CHANGELOG.md` (`v0.1`, `v0.2`, …). Bump the minor version after each reconciliation that changes claims. Each entry lists the claims added, statuses changed, and the investigations ingested.


## 6. Reuse, independence, and changed premises

Deduplicate by statement **and assumptions**, not by terminology or conclusion alone. Require an argument for equivalence; if uncertain, keep separate linked records. Preserve every source/local-result mapping. A literature antecedent, independent derivation, independent implementation, and independent source transcription are distinct kinds of support. Two model families can share the same erroneous data or published argument. Record shared inputs and exposure in provenance rather than treating family diversity as sufficient evidence of independence.

Whenever a premise is refuted, disputed, superseded, or withdrawn, run `python3 tools/yj.py impact ID`. Review the transitive claim dependents and assignments it lists, plus any unrecorded source/data dependencies. The generated board highlights such review triggers. A refuted premise does not automatically refute its consequences: they may have another proof. A corrected premise does not automatically transfer verification either. Append a dated dependency-review note to each affected claim: what changed, which argument/aspect is affected, what remains supported, and the needed follow-up. Where support is now unresolved, use `disputed` with a dispute record, or `reported` if independent verification no longer applies, and explain the transition. Never silently keep a stale verification.

If an encoding, transcription, or definition changes, retain the old version and register the correction separately where required. Review both theorems and source-dependent uses. `impact` follows recorded `depends_on` links; missing links are a limit of the record, not evidence that no impact exists.
