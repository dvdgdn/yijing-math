# Research dashboard

Open [dashboard.html](dashboard.html) directly in a browser for the self-contained snapshot. It includes the research overview, assignments, evidence, directions/questions, manuscript search, record details, and a working guide for Claude coordination. All fonts and interface assets are local to the HTML; there is no account or external service to connect.

**Coordinator-only: this page contains findings.** Keep it outside the packages and workspaces of minimal or targeted investigators. The authoritative context and isolation procedure is [methods/context-modes.md](../methods/context-modes.md).

## Keep it current

Every coordinator or maintenance agent, including Claude, uses the existing repository checks after changing the research records:

```bash
python3 tools/yj.py index
python3 tools/yj.py validate
```

`index` now generates the claim index, the coordination board, and `roadmap/dashboard.html` from the same records. Never hand-edit the generated HTML. Refresh a directly opened file after rebuilding. `validate` detects a stale dashboard and preserves the usual checks on originals, metadata and context boundaries.

For a live view, run from the repository:

```bash
python3 tools/yj.py dashboard --serve --port 0
```

Open the printed Local URL and leave that terminal running. `--port 0` selects an available port. You may choose a fixed unused port instead. The page checks every five seconds while visible. Valid changes rebuild the shared exports and reload the page; invalid changes leave the last valid snapshot visible with an error notice. Fix the underlying records to resume. Ctrl+C stops the local server. This serves local documents read-only on 127.0.0.1; it does not publish the programme.

## What to edit

| Change | Authoritative input |
|---|---|
| Assignment status, scope, family recommendation, overlap or prerequisites | `roadmap/assignments/ASN-NNNN-*.md` |
| Actual model, running/completed state, output and independence | `investigations/INV-NNNN-*/record.md` |
| A statement, evidence or verifier | `ledger/claims/`; use [ledger conventions](../methods/ledger-conventions.md) |
| Direction coverage, question or dispute status | `ledger/directions.md`, `ledger/questions.md`, `ledger/disputes.md` |
| The proposed priority cards | [`dashboard-notes.json`](dashboard-notes.json); update when the coordinator changes the slate |
| Manuscript counts and per-paper inspection judgments | [`literature/openai-math/`](literature/openai-math/README.md); rebuild its catalogue using its documented commands |
| Layout and interaction | `tools/dashboard/`; generator in `tools/dashboard.py` |

The overview distinguishes ready/draft work from actual running investigations, registered claims from reports awaiting registration, and suggestions from model ownership. It derives those counts from records. It does not infer successful verification from agreement or from a completed output. Record dates shown in the footer come from explicit metadata; a live check time means the sources were checked, not that a new investigation occurred.

## Starting with Claude

Use **How to use this → Open coordinator handoff** to hand the repository to a full-context Claude coordinator. Use **Assignments → Claude opportunities** to find work compatible with Claude's model family, including drafts that still need review. An assignment detail shows its source record, prerequisites, linked runs and assembly command.

The coordinator reserves an unused investigation ID and checks work in flight before launch. The assembly command prints an investigator package; it does not reserve an ID, approve a draft, or launch a model. Use the canonical [research cycle](../methods/research-cycle.md) and [prompt assembly](../prompts/README.md) procedures for the actual handoff. An agent with this repository attached has full context, appropriate for coordination or explicitly full-context synthesis. Perform a minimal or targeted investigation in a separate clean session or workspace.

The browser's filters, record drawers and copy buttons do not edit research records. After a report returns, the coordinator records and reconciles it through the normal workflow, then rebuilds. This keeps Claude and Codex looking at the same research state.
