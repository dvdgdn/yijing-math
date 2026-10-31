# Research Cycle and Coordination

This document describes how investigations are chosen, run, reconciled, and followed up. It is the canonical description of roles, the research cycle, and coordination rules.

## 1. Roles

| Role | Typical context | What it does | Prompt |
|---|---|---|---|
| Independent explorer | minimal | Explores a territory from the objects alone. | [`explorer.v1.md`](../prompts/roles/explorer.v1.md) |
| Specialist investigator | targeted | Works deeply on a specific question, using only the prior results it needs. | [`specialist.v1.md`](../prompts/roles/specialist.v1.md) |
| Adversarial verifier | targeted, two-phase | Independently derives, then audits, specific claims made by someone else. | [`verifier.v1.md`](../prompts/roles/verifier.v1.md) |
| Synthesis investigator | full | Looks for relationships and explanatory principles across results, and tests whether they are real. | [`synthesis.v1.md`](../prompts/roles/synthesis.v1.md) |
| Paradigm-breaking investigator | minimal (or framing-exposed) | Questions the framing itself: objects, representations, what counts as explanation. | [`paradigm-breaker.v1.md`](../prompts/roles/paradigm-breaker.v1.md) |
| Research coordinator | full | Reconciles reports into the ledger and drafts the next assignments. A human approves. | [`coordinator.v1.md`](../prompts/roles/coordinator.v1.md) |

Roles are assigned per investigation, not per model. Every model should rotate through every role over time.

The **human research coordinator** is responsible for approving ledger changes and launching assignments. A model in the coordinator role drafts; it does not finalize.

## 2. The default cycle

```
A. Independent discovery ──► B. Handoff ──► C. Reconciliation ──► D. Adversarial verification
        ▲                                                                   │
        │                                                                   ▼
G. Periodic conceptual reset ◄── F. Research planning ◄──────────── E. Synthesis
```

**A. Independent discovery.** Give investigators distinct but complementary assignments. They do not see one another's current work. Context mode per assignment (usually minimal or targeted).

**B. Handoff.** Each investigator ends with a report following the handoff protocol (`prompts/components/handoff-protocol.v2.md`). Save the output verbatim (`output.md`) and fill in the investigation record.

**C. Reconciliation.** The coordinator (human, or a model in the coordinator role with human review) registers claims per [`ledger-conventions.md`](ledger-conventions.md): deduplicates without losing attribution, identifies agreements and contradictions, maps dependencies, opens disputes, updates the verification backlog, and bumps the ledger version.

**D. Adversarial verification.** Significant claims go to a verifier from a **different model family** than every originator. Where possible use the two-phase protocol: the verifier derives the claim independently from its statement before reading the original proof. Same-family verification in an isolated session is allowed but yields `reproduced`, not `verified`.

**E. Synthesis.** A full-context investigator looks for relationships across results and possible deeper principles, and is required to test whether each apparent unification is genuine or an artifact of shared definitions and encodings.

**F. Research planning.** The coordinator selects the next assignments (§3) and records why.

**G. Periodic conceptual reset.** At least every second cycle, run at least one minimal-context investigation (explorer or paradigm-breaker) on a broad territory. Compare its findings with the ledger: rediscovery of registered results is evidence of robustness; findings outside the ledger reveal blind spots; disagreement with the program's framing is recorded as a direction or dispute, not dismissed.

Cycles are a default, not a requirement. Verification of a striking claim can start as soon as it is registered.

## 3. Selecting assignments

For each candidate assignment, the coordinator considers:

1. **Expected information value**: how much the possible outcomes would change what the program believes or does next. A claim on which many other claims depend has high verification value.
2. **Verification debt**: significant claims still at `reported`, especially those with dependents.
3. **Neglect**: directions marked unexplored in `ledger/directions.md`, representations no one has tried, sources no one has examined.
4. **Promising connections and disputes**: open `DSP-` entries, and cases where two independent results seem related.
5. **Diversity**: does the cycle include a mix of verification, deep work, fresh exploration, and challenges to the framing?
6. **Cost**: prefer assignments whose deliverables can be checked.

Every assignment file has a **Rationale (coordinator only)** section recording why it was chosen and what the alternatives were. This section is never sent to the investigator.

## 4. Redundancy and replication

The goal is to minimize **accidental** duplication while allowing **deliberate** replication.

- Before writing an assignment, check `roadmap/assignments/` and `ledger/INDEX.md` for overlapping work.
- Two concurrent assignments with overlapping objectives must state in their rationale why both are needed. Acceptable reasons: independent replication of a high-value claim; deliberately different context modes on the same territory (e.g. a minimal explorer and a targeted specialist); competing explanations each needing a defender.
- Mark deliberate replications with `replication_of:` in the assignment front matter. A replication does not count as verification unless it follows the verifier protocol and comes from a different model family.
- Do not reassign a negative result for re-testing *as stated* unless there is a specific reason to doubt it. Do assign variations that the result's `Not ruled out:` line leaves open.

## 5. Collaboration and competition

- **Competing explanations are first-class.** When two claims offer incompatible explanations of the same phenomenon, open a `DSP-` entry that states each position, the evidence, and a test that would discriminate between them. Neither is removed until the test is run or one is refuted.
- **Adversarial collaboration.** For a mature dispute, assign two investigators to defend opposing positions and to agree in advance on the discriminating test.
- **Building on others' work.** Specialists and synthesis investigators may build on prior claims, but their reports must list every prior claim relied on (by ID) so that a later refutation propagates correctly.

## 6. Model assignment and rotation

- Verification goes to a model family that did not produce the claim.
- Alternate roles: if one model did the exploration in a territory, the other should do the next verification there, and the first should take a different territory or role.
- Record model identity honestly. If the exact model identifier, date, or settings are unknown, write `unknown`. Never infer them.
- Model agreement is not proof. When two models independently reach the same result, register it as two derivations and still verify.

## 7. Lifecycle of an assignment

| Assignment `status` | Meaning |
|---|---|
| `draft` | Being written or reviewed. |
| `ready` | Approved and ready to launch. |
| `launched` | One or more investigations are running; listed under `investigations:`. |
| `completed` | All resulting investigations registered. |
| `withdrawn` | Not run; reason recorded. |

| Investigation `status` | Meaning |
|---|---|
| `prepared` | Folder and package created; not yet sent. |
| `running` | Sent; awaiting output. |
| `completed` | Output saved verbatim; not yet registered. |
| `registered` | Claims registered in the ledger. |
| `missing-output` | The investigation is known or believed to have happened, but its output is not in the repository. |
| `abandoned` | Not completed; reason recorded. |
