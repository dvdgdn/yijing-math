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
| Research coordinator | full | Reconciles reports into the ledger and drafts the next assignments. A human approves. | [`coordinator.v2.md`](../prompts/roles/coordinator.v2.md) |

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

**B. Handoff.** Each investigator ends with a report following the handoff protocol (`prompts/components/handoff-protocol.v3.md`). Save the output verbatim (`output.md`) and fill in the investigation record.

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

Every assignment file has a **Rationale (coordinator only)** section recording why it was chosen and what the alternatives were. State the decision its outcomes could change, the minimum inputs, a bounded deliverable, and a stopping or continuation condition. Compare qualitative information value and cost honestly; do not invent precise scores. This section is never sent to the investigator.

## 4. Redundancy and replication

The goal is to minimize **accidental** duplication while allowing **deliberate** replication.

- Before writing an assignment, review `roadmap/BOARD.md`, the relevant assignment rationales, claim records, and prior `registration.md` search logs. Compare the precise question, source/data version, operations, assumptions, and deliverable; different titles can hide identical work.
- Two concurrent assignments with overlapping objectives must state in their rationale why both are needed. Acceptable reasons: independent replication of a high-value claim; deliberately different context modes on the same territory (e.g. a minimal explorer and a targeted specialist); competing explanations each needing a defender.
- Mark deliberate replications with `replication_of:` in the assignment front matter, and shared active work with reciprocal `intentional_overlap:` entries (§8). A replication does not count as verification unless it follows the verifier protocol and comes from a different model family.
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


## 8. Coordinator board and assignment contracts

`roadmap/BOARD.md` is generated from assignment, investigation, and ledger metadata by `python3 tools/yj.py index`. `python3 tools/yj.py plan` previews it without writing. The index command also regenerates the visual coordinator overview at `roadmap/dashboard.html`; local live-view usage is documented in [`roadmap/DASHBOARD.md`](../roadmap/DASHBOARD.md). It shows queued and running work, unmet prerequisites, direction/question coverage, declared overlap, verification debt, and changed premises with dependents. The board is full-context coordinator material; never send it, or its coverage annotations, to minimal or targeted investigators.

Add these coordinator-only fields to each assignment, using the flat front-matter format in [`ledger-conventions.md`](ledger-conventions.md). Start with [`assignment-template.v2.md`](../prompts/components/assignment-template.v2.md).

| Field | Meaning |
|---|---|
| `purpose` | `verification`, `development`, `exploration`, `source-work`, `prior-art`, `synthesis`, or `reset`. Distinguishes enabling work from research coverage, independently of role. |
| `directions`, `questions` | Lists of the directions and precise questions the work addresses. An intake task may support a direction without exploring it; the board separates enabling work. |
| `work_items` | Short lowercase hyphenated keys for concrete outputs, not entire mathematical fields. Reuse an existing key when the same work would be done. Add a new key only for a different question, source/version, method, or deliverable; explain the distinction in the rationale. |
| `prerequisites` | Assignment IDs that must be completed and registered before this assignment is ready. Use only hard gates. Record soft preferences or claims accepted conditionally in the rationale. |
| `intentional_overlap` | Other assignment IDs sharing work keys or claim targets on purpose. Declare on both assignments and explain each partner in the coordinator rationale. Use `replication_of` as well when this is replication. |

`validate` rejects undeclared exact overlap among draft, ready, or launched assignments, unknown targets, dependency cycles, ready assignments with unfinished prerequisites, and inconsistent assignment/investigation links. Completed assignments need registered output before they can satisfy prerequisites. This catches clerical omissions, not semantic equivalence. Review broad or differently worded assignments sharing directions manually. Sharing a claim can mean auditing different aspects; explain the division rather than removing the target to evade the check.

The lifecycle in §7 records work in flight: create a prepared investigation, list it on the assignment, and mark both running/launched when the human actually sends the package. Do not reserve work indefinitely without a run: on each reconciliation review stalled launched work, record its state, and abandon or replace it with a reason if appropriate. Preserve every record. A ready assignment is available, not a promise that it must run this cycle.

`assemble` prepares text; it does not launch research or certify human approval. Draft packages can be previewed for review. Keep an assignment draft until its inputs and contract are concrete. Once its text has been sent, preserve it and create a successor assignment for a materially changed task.

## 9. An adaptive portfolio, not a fixed queue

At each reconciliation choose a small next launch slate, with a written decision in `roadmap/`:

1. **Repair the evidence base.** Identify a high-impact verification, dispute, missing output, source transcription, or literature gap that would change later work. Prefer checking a load-bearing premise to accumulating consequences of it.
2. **Develop a promising lead.** Ask for the next discriminating consequence or a useful construction, with success, failure, and inconclusive outcomes specified. Avoid asking repeatedly for a more persuasive description of the same pattern.
3. **Protect unfamiliar territory.** Reserve at least one bounded assignment for material, questions, or framings not already developed. For a very small slate or a source bottleneck, record why this is deferred and name the enabling task or next review point. Different role names or mathematical vocabulary alone do not establish diversity. The existing direction list is revisable, not an exhaustive taxonomy.

These are planning needs, not three compulsory runs or numerical quotas. Inspect variation in sources, objects, questions, representations, model families, and context exposure. Source and prior-art work may unlock several directions but cannot be counted as completed exploration of them. Keep a short deferred-candidate list with a reason and a reopening trigger; neglected ideas must not disappear simply because the latest report is more salient.

Keep minimal investigators blind. For a targeted successor, supply a short brief of exact statements already available, failed formulations with their scope, unresolved variations, and reusable inputs. Ask for a consequence beyond those results. For a minimal explorer, use only the neutral territory specification and tolerate overlap; compare with the ledger after the report is fixed. Record such rediscovery as coverage evidence, retaining attribution. Do not reveal prior failures merely to save a blind investigator time.

Before synthesis or adversarial collaboration, preserve each participant's independent position. Compare exact assumptions and source versions before calling a difference a contradiction. If opponents can agree on a discriminating test, fix it before examining the outcome. If they cannot, preserve the incompatible formulations and the unresolved test-design question.

At the end of a cycle record: what decision changed; which claims, sources, and failed approaches are now reusable; what remains uncertain; which territory remains neglected; and the trigger for the next slate. Distinguish meaningful new consequences, useful rediscovery, and repeated stalled approaches. Assess surprise, significance, usefulness, and novelty separately, with evidence or unknown for each. Neither claim count nor model agreement is a measure of progress. If a framing repeatedly yields no new checkable consequences, change the question, source, or context mode before repeating it.

## 10. Literature-assisted development without convergence on one framing

A large external result collection is a candidate library, not an assignment to apply every result. Use the import contract in [`standards.md`](standards.md) §14. Search the complete catalogue, inspect likely statements, reject wrong-domain or vacuous transfers with a scoped reason, and prioritize concrete consequences over paper prestige or keyword similarity. Keep unreviewed candidates explicitly unreviewed and record what would reopen a deferred transfer.

Route a promising transfer through distinct outputs: source/hypothesis audit, application and finite probe, substantive extension, and independent verification. These can run conditionally where useful; do not wait for a complete audit of a long external proof merely to test a small application. Do not silently promote the global premise when a finite special case works. Preserve theorem dependencies and source revisions so later corrections can be traced.

Give assisted specialists only the exact source statements and local findings their tasks need. Keep at least one unassisted exploration/reset lane when capacity permits, following §9's deferral rule for a small slate. A corpus-assisted investigator does not count as a minimal reset, however new the imported mathematics is. Compare assisted and unassisted findings after their reports are fixed; do not erase attribution or count a shared source as independent support.

A completed report awaiting registration is visible on the coordinator board. Reconcile it before counting its findings as registered knowledge. New external literature can change the proposed launch order, but it does not settle missing source data, existing verification debt, or historical correspondence.
