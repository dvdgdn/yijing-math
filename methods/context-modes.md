# Context Modes and Investigator Isolation

Every investigation is assigned one of three context modes. The mode determines what the investigator is **intentionally given**. This document is the canonical description of the modes and of how to keep them honest.

The program depends on these modes. If every investigator inherits the accumulated findings, the program will mostly rediscover its own assumptions. If none of them do, it will keep redoing settled work. The modes let the coordinator decide which risk to take for each assignment.

## 1. The three modes

| Mode | Purpose | Supplied | Never supplied |
|---|---|---|---|
| **minimal** | Independent exploration; conceptual reset; deliberate independent replication. | Role prompt, charter, assignment text, neutral object descriptions from `context/objects/` (plus, if the assignment needs them, source data from `data/` and methodology documents from `methods/`), handoff protocol. | Anything from `ledger/`, `investigations/`, `roadmap/` coordinator notes, `context/briefs/`; claim IDs; previous findings, failed hypotheses, or preferred representations. |
| **targeted** | Specialist work and verification without redoing settled work, and without over-constraining. | Everything in minimal, plus a brief in `context/briefs/` or specific ledger records containing **only** what the assignment needs: definitions, the specific claims, the specific open questions. | The rest of the ledger; unrelated findings; summaries. |
| **full** | Synthesis, verification planning, research coordination. | The full research record: `ledger/` (summary, index, claims, questions, directions, disputes, backlog) and investigation records as needed. | — |

Choose the least context that will serve the assignment. When in doubt between minimal and targeted, ask: "Would knowing the prior result make this investigator less likely to find something different?" If yes, use minimal.

## 2. What counts as "supplied"

Distinguish:

- **Intentionally supplied material**: the exact text pasted or uploaded into the investigator's session. This is what the context mode controls, and it is recorded in the investigation record and saved as `prompt.md`.
- **Unavoidable background knowledge**: what the model already knows, including published literature on the Yijing. The program does not control this. Investigators are asked to cite literature they use and to say when a result is already known.
- **Ambient access**: anything the investigator *could* read but was not given, for example repository files when the investigator runs as an agent inside this repository, global instructions files, persistent memory, or project knowledge attached to a chat workspace. **Ambient access defeats minimal mode and must be removed.**

## 3. Preserving isolation: required practice

For **minimal** and **targeted** investigations:

1. **Assemble the package from listed files only.** Use `python3 tools/yj.py assemble ASN-NNNN`, which concatenates the components named in the assignment and refuses to build a minimal package that includes ledger, investigation, roadmap, or brief material or that mentions ledger IDs. It also warns if the package contains vocabulary listed in `ledger/leak-terms.txt`. All file inputs, including role, charter, handoff, and later-phase materials, are resolved within the repository before context boundaries are checked; alternate path spellings and symlinks do not bypass those boundaries. Manual assembly is fine; follow the same order and check by hand.
2. **Run in a fresh session with no ambient context.**
   - Use a new chat or conversation, not one that has seen any other material.
   - Do not use a chat "project" or workspace that has repository files, prior reports, or custom instructions attached. Use an empty one or none.
   - Turn off persistent memory or personalization features for the session, or use an account or workspace where they hold nothing about this program.
   - **Do not run a minimal or targeted investigation as an agent with access to this repository.** An agent with file access can read the ledger whether or not it is told to. If an agent needs a workspace (for running code), give it an empty directory containing only the assembled package and any supplied data files.
3. **Save exactly what was sent.** Store the assembled package verbatim as `prompt.md` (or `prompt-part1.md`, `prompt-part2.md`) in the investigation folder, and record its SHA-256 in the record.
4. **Record deviations.** If isolation was broken (wrong attachment, memory on, follow-up messages that added context), record it in the investigation record under "Deviations". An investigation that was not isolated can still be valuable, but its findings must not be counted as independent.

For **full** investigations, running as an agent inside this repository is acceptable and often convenient.

Coverage tags, work keys, overlap declarations, the coordination board, and selection rationales are coordinator metadata. They are excluded from assembled packages. Targeted successors may receive scoped reuse briefs under [`research-cycle.md`](research-cycle.md) §9; minimal investigators do not receive the map of what has already been explored.

## 4. Repository files that must stay clean

Some files may reach a minimal-context investigator directly (as package components) or indirectly (as instructions loaded automatically by agent tools). They must contain **no findings, claim IDs, failed hypotheses, or preferred representations**:

- `README.md`, `AGENTS.md`, `CLAUDE.md`
- everything in `methods/`, `prompts/`, `context/objects/`, `data/`, `compute/README.md`, `tools/`

`tools/yj.py validate` checks these files for ledger IDs and leak-term vocabulary. Findings live only in `ledger/`, `investigations/`, `roadmap/`, and `context/briefs/`.

Rule of thumb for writing clean files: describe **objects and procedures** (what a hexagram is, what an attested arrangement contains), never **results** (what is true of them). Methodology examples should use toy or generic cases, not current findings.

## 5. Variants

- **Framing-exposed minimal** (for paradigm-breaking work): the investigator also receives a list of the program's *working assumptions and representations*, but not its results, and is asked to attack them. The list is written as a brief in `context/briefs/` and the assignment is recorded as `targeted` with a note, since a list of assumptions is still information about the program.
- **Two-phase verification** (targeted): phase 1 supplies only claim statements and definitions, so the verifier derives independently; phase 2, in the same session, supplies the original proof and evidence for audit. See [`prompts/roles/verifier.v1.md`](../prompts/roles/verifier.v1.md).
- **Blind replication** (minimal): the same assignment as an earlier investigation, given to a different session or model without the earlier report, to test whether a finding is rediscovered independently. Record `replication_of:` in the assignment.

## 6. Checking a minimal package by hand

Before sending a minimal package, read it once and confirm:

- [ ] It contains only: role prompt, charter, assignment text, object descriptions, source data, methodology documents, handoff protocol.
- [ ] The assignment text does not describe what earlier investigators found, tried, or failed at.
- [ ] No ledger IDs (`C-…`, `Q-…`, `DEF-…`, `DIR-…`, `DSP-…`) appear.
- [ ] No representation is presented as preferred; any encoding mentioned is presented as a choice.
- [ ] The session it will be pasted into is fresh, with memory and attachments off.
