# Research Directions

Broad areas of inquiry and how much they have been explored. A direction is wider than a question: it names territory, not a specific answer to seek. **A direction is never closed because one formulation within it failed.** It may be marked `addressed` only when the territory has been examined from several independent angles, and the entry must then say what was examined.

Exploration status values: `unexplored`, `lightly explored`, `active`, `addressed`, `source absent` (named but no report available).

Entries marked "registrar suggestion" were added during repository setup from general knowledge of the subject, not derived from any investigation. They are prompts for planning, not findings.

### DIR-001 — Automata-theoretic representations and minimal behavioral quotients

*Status:* source absent. *Origin:* named in the repository setup brief as a topic of the existing investigations. No report in the repository covers it; INV-0001 does not. It may come from the missing INV-0002. No claims registered.

### DIR-002 — Noncommutation of operations

*Status:* source absent. *Origin:* as DIR-001. INV-0001 touches commutation only in passing (C-0007, C-0019). No claims registered from the brief's description.

### DIR-003 — Limits on reconstructing the received ordering

*Status:* source absent. *Origin:* as DIR-001. INV-0001 discusses what pairing and canon balance do and do not explain (C-0004, C-0005), but contains no reconstruction-limit results.

### DIR-004 — Symmetry classification of attested orderings and procedures

*Status:* lightly explored. *Origin:* INV-0001 §6–7. *Related:* Q-002, C-0021, C-0022, ASN-0005.

### DIR-005 — Arrangements other than the received order

Mawangdui manuscript order, the Chu manuscript, the Shao Yong arrangements, and others.
*Status:* lightly explored (assertions only: C-0023). *Related:* Q-001, SRC-003, SRC-004, SRC-005. *Needs:* cited transcriptions in `data/`. *Intake (INV-0008):* no Mawangdui or Chu transcription on Wikisource. Shao Yong material is available as text (`皇極經世`, `易學啟蒙通釋/圖`), not as diagrams.

### DIR-006 — Divination procedures and changing lines

Four-valued lines, the procedures that generate them, the transition from primary to second hexagram, and reading rules.
*Status:* lightly explored (one literature-assisted, full-context investigation: INV-0004, C-0032–C-0038). *Origin:* registrar suggestion; INV-0001 bracketed procedures other than the Jing Fang palaces. *Related:* ASN-0004 (blind exploration, deliberately not exposed to INV-0004), ASN-0014, Q-009–Q-011, SRC-007. Not examined: reading rules, the four-valued outcome beyond the change mask, and procedures other than the modelled yarrow and coin methods. Source questions: cited procedure texts now exist (`data/procedure-texts.v1.csv`; C-0041), and the split law is still unattested.

### DIR-007 — The textual layer as data

Judgments, line statements, and commentaries, studied for structure (e.g. how textual features relate to line position or to figure structure).
*Status:* unexplored. *Origin:* registrar suggestion; INV-0001 bracketed the text entirely. *Intake (INV-0008):* two pinned digital witnesses of the judgments and line statements, the Wikisource `周易` chapter pages and the classic text marked in `周易正義`, are snapshotted in `investigations/INV-0008-cited-source-baselines/sources/`. *Caution:* statistical work on text needs especially careful null models and multiple-comparison control (`methods/standards.md` §6–7).

### DIR-008 — Other Han and later correlative systems

For example the "attached stems" (納甲) system and calendrical correlations (卦氣) associated with Han scholarship, and later systems.
*Status:* unexplored. *Origin:* registrar suggestion. The content and attribution of these systems must be established from cited sources before any mathematical claim is made about them. *Intake (INV-0008):* the *Jingshi Yizhuan* witnesses carry stem-branch (納甲) and 飛伏 notes for every entry. Yixing's 卦議 (卦氣) is in `新唐書/卷027上` on Wikisource. Neither has been transcribed.

### DIR-009 — Representations other than binary vectors

Four-valued line encodings, non-vector representations, geometric, topological, order-theoretic, categorical, information-theoretic, or entirely new formalizations. Includes testing which existing results survive a change of representation.
*Status:* largely unexplored. *Origin:* registrar observation that INV-0001 worked in a single encoding throughout (DEF-001). *Related:* C-0026, ASN-0006.

### DIR-010 — Relations among operations and constructions

Compositions, incompatibilities, invariants, and possible generalizations of the operations and constructions associated with the Yijing.
*Status:* lightly explored (INV-0001: R, C, N, φ, D). *Related:* ASN-0003 (supplied assignment), DIR-002.

### DIR-011 — Mathematical structure and historical layers

Whether and how mathematical properties align with the dating of textual and procedural layers.
*Status:* lightly explored (C-0022). *Related:* Q-001, Q-008, DSP-003. *Caution:* needs historical evidence; mathematical alignment alone is not evidence of historical stratification.
