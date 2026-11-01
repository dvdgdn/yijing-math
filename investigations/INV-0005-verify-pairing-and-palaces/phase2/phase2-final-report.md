# INV-0005 — ASN-0001: Final Audit of the Received Pairing and Eight-Palace Claims

- **Role:** Adversarial Mathematical Verifier
- **Model:** OpenAI Codex, GPT-5 family (exact deployment identifier not exposed)
- **Phase:** 2 audit; Phase 1 was completed and recorded before the original report or ledger entries were supplied
- **Materials audited:** the original report `investigations/prompts/yijing_paradigm_transcendence/claude_opus_5_5.md`; ledger records C-0001, C-0002, C-0016, C-0017, C-0018, C-0019, C-0026; the Phase-1 report, code, and complete transcriptions in this investigation directory
- **External sources/tools:** Python 3.9.6 was actually executed. The only external data lookup in either phase was Python's local Unicode 13.0.0 database for the modern received name/order sequence. No network, book, article, primary text, or palace-table edition was available or consulted.
- **Blindness statement:** Phase 1 was genuinely blind. The Phase-1 files have not been retroactively altered.

## Final verdict table

“Source correspondence” distinguishes agreement with the complete conventional transcriptions used here from historical attribution, edition-level provenance, or universality across variants. A dash means that the aspect is not claimed.

| Claim | Mathematical correctness | Source correspondence | Significance claims | One-line reason |
|---|---|---|---|---|
| C-0001 | `confirmed` | — | — | The original's compressed argument is valid; the full two-branch proof and all 64 cases agree. |
| C-0002 | `confirmed` | `confirmed` | — | A complete received-order transcription gives exactly 28 adjacent R-pairs and four adjacent C-pairs on the eight R-palindromes; the original supplied no reproducible data or output. |
| C-0016 | `confirmed` | — | `undetermined` | The original proof is complete and matches the blind derivation; “deepest” is subjective and “distinctive” lacks a historically justified comparison class. |
| C-0017 | `confirmed` | `confirmed-with-corrections` | — | D exactly encodes the stated sequential procedure and matches all 64 cells of one conventional standard table; the original cites no table, and strict Jing Fang provenance or all-variant agreement remains unestablished. |
| C-0018 | `confirmed` | `confirmed-with-corrections` | `undetermined` | Status is exactly a function of φ and the quoted mnemonic matches under its conventional eight-pattern reading; the mnemonic's date, source, and asserted independence are undocumented. |
| C-0019 | `confirmed` | `confirmed-with-corrections` | `undetermined` | The identity is formal and all 28 R-orbits pass in the transcribed table, but “every standard table” and literature novelty were not established. |
| C-0026, restricted to the assigned claims | `confirmed-with-corrections` | `confirmed-with-corrections` | — | Coherent recoding x↦Cx preserves the truth of the assigned claims; “every result is C-equivariant” is not literally the right mathematical formulation, and the ledger's report-wide expansion exceeds this audit's assigned scope. |

No assigned mathematical claim is refuted. The corrections concern source scope, reproducibility, terminology, and unsupported significance—not the finite algebraic conclusions.

## 1. Audit framework and comparison with Phase 1

The original mathematical reasoning is strikingly close to the Phase-1 derivation:

- Both prove C-0001 by separating R-palindromes from non-palindromes.
- Both compute the same ordered image
  `000,100,110,111,011,001,101,010` for φ(D).
- Both identify `P=ker φ` and derive unique decomposition from the bijection on D.
- Both derive C-0018 by observing `φ(b⊕d)=φ(d)`.
- Both derive C-0019 from reversal of the lower/upper blocks.

The differences are evidential rather than algebraic. The original gives no input transcription, code, output, edition, or palace-table source. It proves C-0016 on paper, gives only two palace examples, and frames the 28-pair palace comparison as a “decisive check.” Phase 1 supplied complete transcriptions and actually executed all finite comparisons, but its palace data came from my pre-existing knowledge rather than an edition-cited independent source. Thus the audit can settle the mathematics and consistency with one conventional table, but it cannot upgrade historical provenance or universality across variants.

The original's opening sentence, “All claims below were checked by exhaustive computation,” is not reproducible evidence as delivered. It may describe a computation that really occurred, but no code, data, parameters, or output show that it ran. The later wording around C-0019 is also internally ambiguous: §7 presents the 28-pair comparison as a prospective decisive check, whereas the opening blanket sentence could be read to say it was already run. The ledger is right not to treat that blanket assertion as a demonstrated all-table audit.

## 2. Claim-by-claim audit

### C-0001 — fixed-point-free involution

**Original reasoning.** The source says σ is a fixed-point-free involution “because C preserves palindromes and has no fixed points.” This explicitly settles the palindrome branch. The non-palindrome branch additionally uses the elementary facts `R²=id` and `Rx≠x ⇒ R(Rx)≠Rx`. Those facts are not written, but the omission is expository rather than a logical gap.

**Comparison with Phase 1.** There is no substantive difference. Phase 1 wrote the two cases out and used `RC=CR` to show C maps an R-palindrome to another R-palindrome. The exhaustive 64-word check was actually executed and agreed.

**Ledger audit.** C-0001 faithfully states the source, dependencies, evidence level, and scope. Calling the source argument “one-line” is accurate. The suggested generalization also holds for every positive word length; length zero is the exceptional degenerate case because complement fixes the empty word.

**Final assessment.** Mathematical correctness `confirmed`. It is **definition-driven** and **standard elementary**, essentially trivial after the case split.

### C-0002 — received adjacent pairs are σ-orbits

**Original reasoning/evidence.** The report states the exact palindrome list and counts and says “which I checked for all 32,” but shows neither the 64 figures nor code/output. The source claim is therefore plausible and correct but computationally unreproducible from the original report alone.

**Verifier check.** The complete bottom-to-top received transcription is in `data/received_order.tsv` and Phase-1 Appendix A. It contains every six-bit word exactly once. The actual execution checked σ in both directions for every pair `{2k−1,2k}`. It found:

- 28 reversal pairs: `3–4, 5–6, …, 25–26, 31–32, …, 59–60, 63–64`;
- four complement pairs: `1–2, 27–28, 29–30, 61–62`;
- exactly eight R-fixed figures: `1,2,27,28,29,30,61,62`.

This matches the original exactly. The modern number/name sequence was additionally cross-checked against all Unicode Yijing code points U+4DC0–U+4DFF. Unicode did not independently supply the bottom-to-top bit transcription.

**Ledger audit.** The registrar's reading of “the 32 King Wen pairs” as consecutive pairs `{2k−1,2k}` is compelled by the counts and conventional terminology and is faithful. The ledger correctly records the missing source edition, transcription, code, and output. It also correctly refrains from registering novelty.

**Final assessment.** Mathematical correctness and correspondence to the standard received arrangement `confirmed`. This is **contingent** and **nontrivial as a feature of the received sequence**, though checking it once data are supplied is elementary. No rarity, intention, or novelty conclusion follows.

### C-0016 — φ(D), transversal, partition, and one-of-each property

**Original proof audit.** The proof is complete:

1. It computes the eight distinct values of φ on D.
2. It identifies `P=ker φ`.
3. It chooses the unique d with `φ(d)=φ(x)` and sets `b=x⊕d`.

The uniqueness of b is implicit but immediate. The term “transversal of P” is standard shorthand for a set containing one representative of each additive coset of P. Every translate `b⊕D`, with `b∈P`, remains a transversal, and the addition map `P×D→F₂⁶` is bijective.

**Comparison with Phase 1.** The arguments coincide. Phase 1 made uniqueness explicit and enumerated all 64 sums. There is no hidden reliance on received order or traditional palace data: this theorem is formal given D.

**Ledger audit.** C-0016 accurately restates the theorem, proof, dependencies, and the separation from C-0017. It correctly notes that the original does not infer Jing Fang's historical knowledge from the algebra.

**Significance audit.** The original calls this its “strongest worked result,” “deepest result,” and says the distinctive fact is that the bottom-up rule lands on a transversal. The first two are subjective comparisons. “Not automatic” is literally correct, but distinctiveness requires a comparison class.

Two exact, newly executed benchmarks sharpen this without settling historical significance:

- Fix the six prefix vectors and choose two distinct extra vectors uniformly from the other 58 six-bit words. Exactly 64 of `C(58,2)=1653` unordered pairs fill the two missing φ-fibres, a fraction `64/1653 ≈ 0.0387175`.
- More structurally, keep generations 1–5 and the rule that returning restores the lower trigram, but let wandering revert any one of the five previously changed lines. Exactly one of the five choices works: reverting line 4. The five `(φ(wandering),φ(returning))` pairs are `(101,110)`, `(011,110)`, `(000,110)`, `(101,010)`, and `(011,100)`.

These counts support the narrow statement that the traditional soul moves are not forced by the first six vectors and do fill the missing classes in a special way. They do **not** justify a historical null model, a design claim, or “deepest.”

**Final assessment.** Mathematics `confirmed`; significance `undetermined`. The theorem is **definition-driven and standard finite linear algebra**. The chosen D and its procedural origin are contingent.

### C-0017 — procedure and traditional palace table

**Procedure audit.** Starting at the base, the cumulative differences are
`000000,100000,110000,111000,111100,111110`; reverting line 4 gives
`111010`; restoring the lower trigram to that of the palace base, from the wandering figure, gives `000010`. Thus D exactly represents the intended sequential procedure.

The original phrase “the returning soul restores the lower trigram” is slightly underspecified on its own. The safe wording is: “from the wandering-soul figure, restore lines 1–3 to their values in the doubled-trigram base.” The displayed D makes that intended reading clear.

**Traditional-table check.** Phase 1 transcribed the conventional eight blocks

`乾: 1,44,33,12,20,23,35,14`;  
`坎: 29,60,3,63,49,55,36,7`;  
`艮: 52,22,26,41,38,10,61,53`;  
`震: 51,16,40,32,46,48,28,17`;  
`巽: 57,9,37,42,25,21,27,18`;  
`離: 30,56,50,64,4,59,6,13`;  
`坤: 2,24,19,11,34,43,5,8`;  
`兌: 58,47,45,31,39,15,62,54`,

with slots `pure,1st,2nd,3rd,4th,5th,wandering,returning`. The executed check compared all 64 cells with `base⊕D[slot]`; all passed. The source's Zhun and Meng calculations also pass exactly.

**Source limitation.** Neither the original nor this audit consulted or cites a primary Jing Fang text or a dated palace-table edition. My transcription reflects the conventional standard table known from the Jing Fang/Najia tradition. Presentation variants in block order and terminology do not affect the check, but no corpus was examined for substantive variants. The original itself wisely says the theorem does not show that Jing Fang knew the algebra; “Jing Fang” should therefore be read as conventional attribution/system-name, not proved personal authorship.

**Ledger audit.** Part (a) is a faithful formalization. Part (b), as a true claim about the conventional table, is confirmed by this audit, but it is stronger than the evidence explicitly presented in the original. The original shows two cells and later states a 28-pair prediction; it never presents a 64-cell palace table or explicit all-64 table-comparison output. Its opening blanket computation claim “may cover” part (b), exactly as the ledger cautiously says, but does not demonstrate it. The ledger should mark part (b) as **inferred/registered from the report's system identification and blanket assertion**, not as an explicitly documented 64-cell result.

**Final assessment.** Mathematical encoding `confirmed`; source correspondence `confirmed-with-corrections`: confirmed for the one full conventional table recorded here, not for strict historical authorship or every possible variant. This is **definition-driven** for deriving D and **contingent, source-dependent, and nontrivial** for the 64 assignments.

### C-0018 — generation/status as a function of φ and mnemonic correspondence

**Formal audit.** If `x=b⊕d`, then `φ(x)=φ(d)` because `b∈ker φ`. Since `φ|D` is bijective, d and its status depend only on φ(x). The original truth table is correct. The 世-line itself is also determined once conventional status is included:

| φ | status | 世 line |
|---|---|---:|
| `000` | pure | 6 |
| `100` | 1st | 1 |
| `110` | 2nd | 2 |
| `111` | 3rd | 3 |
| `011` | 4th | 4 |
| `001` | 5th | 5 |
| `101` | wandering | 4 |
| `010` | returning | 3 |

**Mnemonic audit.** The table agrees with the supplied Chinese string under its conventional eight-case reading: `天同` names the exact pattern in which heaven alone agrees, `地同` the exact pattern in which earth alone agrees, and so forth. Read as isolated one-bit implications, clauses such as “heaven agrees” would be underdetermining; the source should state the contextual reading.

The sentence “the mnemonic is the map F₂⁶/P→D, written in words” is acceptable only after an identification: φ identifies the quotient with F₂³, and D is the chosen section; the mnemonic directly names the **status function** on quotient classes, and only thereby a representative in D.

**Source/significance audit.** The report supplies neither provenance nor date for the mnemonic. It also does not establish that the mnemonic is historically independent of the palace tables; it could be a later compression of the same assignments. “Not used to build the theory” is a statement about the original investigator's process and cannot be audited from the report. Therefore the match is real, but it is not independent corroboration on the evidence supplied.

**Ledger audit.** C-0018 faithfully records the formal claim, quoted mnemonic, missing source, uncheckable process statement, and shared-origin alternative. No correction to the registered mathematics is needed.

**Final assessment.** Mathematics `confirmed`; source correspondence `confirmed-with-corrections` to the quoted string and conventional table, while provenance remains undetermined; significance/independence `undetermined`. Formal dependence is **definition-driven and standard**; traditional correspondence is **contingent**.

### C-0019 — reversal law and generation reflection

**Formal proof audit.** For `x=(l,u)` stored bottom-to-top,
\[
R_6x=(R_3u,R_3l),\qquad
\phi(R_6x)=R_3u\oplus R_3l=R_3(l\oplus u)=R_3\phi(x).
\]
Reversing the eight φ-words gives exactly `1st↔5th`, `2nd↔4th`, with pure, 3rd, wandering, and returning fixed. The original's one-sentence derivation is correct; Phase 1 merely made the block calculation explicit.

**Table check.** The executed program formed all non-palindromic reversal orbits of the full cube, found 28, and checked the status of both endpoints in the complete palace transcription. All 28 passed. It also verified that these are precisely C-0002's 28 received reversal pairs. This supplies the decisive check the original proposed for one conventional table.

**Scope corrections.** The phrase “in every standard palace table” is universal. One conventional table, even checked exhaustively, cannot establish it without defining “standard” and surveying variants. Also, a counterexample in another table would not necessarily prove that the stated procedure is wrong; it might identify a variant table, a transcription error, or an overbroad universality claim. The original's “single counterexample would mean my statement of the procedure is wrong” is therefore too strong.

“A new consequence” is harmless if it means newly derived inside that report. If it means new to the literature, it is unsupported: no literature search or prior-art comparison is given. Finally, the theorem itself is an equivariance law with a nontrivial action on status labels. Interpreting it as “precisely the trace of broken symmetry” is additional and not forced by the theorem; the unlabelled palace partition's behavior under R must be distinguished from equivariance of the status map.

**Ledger audit.** C-0019 faithfully states the formal result and accurately treats the 28-pair statement as a prediction not demonstrably executed in the source. Its warning about unsupported novelty is appropriate, subject to the local-versus-literature ambiguity just noted.

**Final assessment.** Mathematics `confirmed`; table correspondence `confirmed-with-corrections` for the complete table used here, not “every standard table”; novelty/significance `undetermined`. The identity is **definition-driven and standard**; the traditional table check is **contingent and nontrivial as data validation**.

### C-0026 — yin/yang relabelling

**Scope ambiguity.** The assignment restricted C-0026 to C-0001, C-0002, C-0016–19. The ledger instead expands the original sentence to “each result of INV-0001.” Those are different claims. This audit settles the assigned restriction only; the report-wide statement would also require auditing the direction convention of Shao Yong binary counting, all null-model statistics, and every other unassigned result.

**Correct formal statement.** A coherent physical relabelling sends each old word x to
`T(x)=Cx`. Then
\[
RT=TR,\quad \sigma T=T\sigma,\quad \phi(Tx)=\phi(x),
\]
and `T(b⊕d)=T(b)⊕d`. Thus received physical pairs, D-differences, palace status, the φ lookup, and the reversal law retain their truth under the new coordinates. This was checked over all 64 words and all 64 table rows.

The original wording “every result is C-equivariant” is technically imprecise. Equivariance is a property of a map after actions on both domain and codomain are specified. For example, σ genuinely commutes with C, while φ is **invariant** under global complement (`φ(Cx)=φ(x)`), not complement-equivariant on a complemented three-bit codomain. The correct umbrella statement is that the assigned claims are invariant under the coordinate recoding T.

**Ledger audit.** The ledger faithfully quotes and broadens the original report, and correctly says no result-by-result evidence was supplied. For ASN-0001 it needs a scope note separating the restricted verified claim from the report-wide unverified claim.

**Final assessment.** Restricted mathematical claim `confirmed-with-corrections` using the precise recoding statement; source claims retain exactly their previous truth and limitations, hence source `confirmed-with-corrections`. It is **definition-driven and standard coordinate invariance**.

## 3. Ledger correspondence summary

| Ledger claim | Does it say what the original says? | Required correction or note |
|---|---|---|
| C-0001 | Yes | None. |
| C-0002 | Yes | Registrar's consecutive-pair reading is justified; original execution remains undocumented. |
| C-0016 | Yes | None; significance is appropriately flagged as unquantified. |
| C-0017 | Partly / reasonable inference | Part (b)'s all-64 agreement is not explicitly evidenced in the source; mark it inferred from system identification plus the blanket computation assertion, not demonstrated there. |
| C-0018 | Yes | Preserve the ledger's warning that “not used to build” is uncheckable and mnemonic independence is unresolved. |
| C-0019 | Yes | “New” must be split into new-in-report versus literature novelty; the latter is unverified. |
| C-0026 | Yes for the full-report quotation, no for ASN-0001 scope | Record a restricted verified version for these seven claims; do not treat it as verification of every INV-0001 result. |

## 4. Source correspondence audit

### Received order

The exact 64-row data are in `data/received_order.tsv` and Phase-1 Appendix A. Number/name order was checked against Unicode 13.0.0; figures were entered from standard trigram compositions. This is sufficient to confirm C-0002 for the standard modern received arrangement. It is not a critical-edition or manuscript provenance study.

### Palace procedure and table

The exact 64-row data are in `data/eight_palaces_source.tsv` and Phase-1 Appendix B. They reproduce the conventional table known to this verifier, and every cell agrees with D. However:

- no source edition is cited by the original;
- no source edition was available to this verifier;
- historical authorship by Jing Fang is not established;
- the mnemonic's source and date are not established;
- no variant corpus was surveyed.

Accordingly, source verdicts are intentionally limited to a complete conventional transcription, not elevated to primary-source historical confirmation.

## 5. Reproducibility record

Both programs were **actually executed** in Phase 2:

```sh
/usr/bin/python3 -B code/verify_phase1.py
/usr/bin/python3 -B code/audit_phase2.py
```

The first exited 0 and repeated all Phase-1 passes: 64-word input integrity, C-0001, 32 received pairs, φ(D), all 64 palace cells, all 64 status cells, all 28 reversal orbits, and coherent recoding. The second exited 0 and printed the exact `64/1653` and `1/5` comparison results stated above. Sandbox compiler-cache warnings were harmless and did not change either exit code.

Complete artifacts and SHA-256 hashes at audit time:

| Artifact | SHA-256 |
|---|---|
| `phase1-report.md` | `300e623b2d1a1b036d5e7fdcd0e23ce6ffcde01256a88b43972cb775ea114a7c` |
| `data/received_order.tsv` | `b30adc072d232703e83d566e69663abbaed040a47f995378315eb8f8bc4d4a40` |
| `data/eight_palaces_source.tsv` | `a3f65e5ad7235caaffe7067a2eea27ea89e5ab5a3b1f0c765e2a7cd4b1fd8790` |
| `code/verify_phase1.py` | `65d163682aa3d0a2c1dd03bdcedbaabdeb704b10e9fa9071f1f914c5f8033a0a` |
| `code/audit_phase2.py` | `f3abdaff117306dd3d03616d2f3eda88bcc41f14547134516fc43fb2d9bc2497` |

The full input transcriptions are incorporated into this report package by these exact files and are printed in full in Phase-1 Appendices A and B. They are not duplicated here, avoiding two nominally authoritative copies.

## 6. Research handoff protocol

### 6.1 Executive findings

All seven assigned mathematical claims survive audit. The original's Theorem 4 proof is sound and is its best-documented assigned result. The verifier's complete computations fill the original's missing finite checks: all 32 received pairs, all 64 palace assignments, all 64 φ/status assignments, and all 28 reversal orbits pass.

The strongest objections are evidential:

1. The original's blanket exhaustive-computation claim is not reproducible from anything supplied.
2. Its palace source is uncited and only two cells are shown.
3. “Every standard table,” “independent traditional rule,” and any literature novelty exceed the evidence.
4. “Every result is C-equivariant” should be replaced by precise claim-by-claim invariance under global recoding.

### 6.2 Exact mathematical results

1. σ is a fixed-point-free involution on F₂⁶.
2. The standard received adjacent pairs are exactly 28 R-orbits and four complementary pairs of R-palindromes.
3. `P=ker φ`, `φ|D` is bijective, and `P×D→F₂⁶` by addition is bijective.
4. The stated sequential palace procedure yields D and reproduces every cell of the recorded conventional palace table.
5. Palace status and 世 position factor through φ by the eight-row table above.
6. `φR₆=R₃φ`, inducing the exact status reflection law.
7. Global yin/yang recoding preserves all six preceding results in their assigned scope.
8. **New bounded comparison result:** among the five procedures obtained by changing only which previously flipped line is reverted for wandering and then restoring the lower trigram, only line 4 yields a transversal. Under the broader uniform extra-vector comparison, exactly `64/1653` pairs succeed.

### 6.3 Failed hypotheses and negative results

- No assigned mathematical theorem failed.
- The original evidence does not demonstrate that its claimed exhaustive computations actually ran.
- A single conventional table does not establish agreement with “every standard table.”
- The quoted mnemonic is not shown to be historically independent of the palace table.
- Literature novelty for C-0019 is not supported.
- Literal map-by-map “C-equivariance” is not a correct common description; the weaker recoding-invariance statement survives.
- The new comparison counts do not establish historical design or rarity because neither comparison class is historically justified.

### 6.4 Unresolved conjectures and questions

1. Which earliest securely dated source attests the eight palace blocks, the wandering/returning operations, and the quoted mnemonic?
2. Are there substantive palace-table variants, and if so do C-0018 and C-0019 survive each one?
3. Is Corollary B already explicit or implicit in earlier technical literature?
4. What pre-registered family of “comparable procedures” is historically and mathematically justified for assessing the distinctiveness of D?
5. Does the report-wide, rather than ASN-0001-restricted, label-swap claim survive every other result with conventions stated precisely?

### 6.5 Dependencies

- Formal results use the registered encoding, R, C, P, D, and φ.
- C-0002 depends on the received transcription.
- C-0017's table aspect depends on both complete transcriptions.
- C-0018's source aspect depends on the quoted mnemonic and C-0017.
- C-0019's table aspect depends on C-0017/C-0018; its algebra does not.
- C-0026 assumes coherent global recoding rather than merely changing prose labels while freezing word-to-figure assignments.
- Historical claims require sources not supplied to either investigator.

### 6.6 Alternative explanations and broader generalization

- For any n, `(l,u)↦l⊕u` has diagonal kernel in F₂²ⁿ. Any section of this quotient produces an analogous partition and a status lookup. Thus the quotient mechanism is standard; the contingent feature is the traditional D.
- The mnemonic may be a later encoding of palace assignments rather than independent corroboration.
- C-0019 is a generic reversal-equivariance identity for split words, not by itself evidence of historical awareness or broken symmetry.
- C-0002 may record a known editorial pairing convention; the algebra confirms it but does not identify its date or cause.

### 6.7 Reproducibility

The exact data, programs, commands, versions, hashes, and outputs are recorded in §5 and the Phase-1 report. All finite spaces were exhaustively enumerated. There was no sampling, random seed, omitted parameter, or tolerance. The significance benchmarks are exact counts under explicitly delimited artificial comparison classes.

### 6.8 Opportunities for further research

- Establish an edition-cited data lineage for received figures, palace tables, and the mnemonic.
- Classify all D-like transversals reachable by restricted line-change grammars.
- Separate symmetry of the unlabelled palace partition from equivariance of palace status under R.
- Search the literature specifically for the status-reflection law before calling it novel.
- Audit the original report's other theorems and statistical computations with supplied code/data.

### 6.9 Recommended next assignments and next-step contracts

| Assignment | Precise question | Minimum inputs | Cheapest decisive check | Outcomes and effect | Stopping condition |
|---|---|---|---|---|---|
| Primary-source palace audit | What exact procedure/table is attested, when, and under whose attribution? | Dated edition/facsimile, passage locations, bibliographic metadata | Two independent transcriptions of every procedural verb and 64 table cells | Match upgrades C-0017 source verdict; variants delimit it; silence leaves attribution open | All selected witnesses reconciled cell-by-cell with citations |
| Mnemonic provenance | When and where does the exact Chinese mnemonic first appear, and is it presented as derivation or summary? | Searchable dated corpus and page images | Exact/variant phrase search followed by page verification | Early independent derivation strengthens significance; later table mnemonic weakens independence | Earliest located attestation verified and bounded-corpus limitations stated |
| Corollary-B prior art | Is the 1↔5, 2↔4 reversal law known in palace literature? | Bibliographic databases and technical texts | Search terminology plus manual theorem-equivalence check | Prior art refutes global novelty; absence in bounded corpus leaves novelty provisional | Predeclared databases/date/languages exhausted |
| Procedure grammar | How rare are transversals among historically plausible line-change rules? | A preregistered grammar, equivalence relation, D/φ | Exhaustively enumerate the finite grammar | Exact rate supports or weakens “distinctive” within that grammar | Every grammar production enumerated and sensitivity variants reported |
| Full C-0026 audit | Does global recoding preserve every INV-0001 claim, including binary order and statistics? | Full claim list, precise actions/conventions, original code/data | Conjugate or recompute each claim under x↦Cx | Confirms report-wide version, finds counterexample, or requires convention correction | Every original result has a result-by-result entry |

One promising approach not attempted is a facsimile-based, double-blind transcription of early palace witnesses. It is the cheapest way to resolve the main remaining uncertainty but requires sources unavailable in this workspace.

### 6.10 Search log

| Attempt | Object/data version | Representation and bounds | Question | Outcome/evidence | Why stopped / successor change |
|---|---|---|---|---|---|
| P1-A1 | Registered formal definitions | All 64 six-bit words | C-0001, C-0016, formal C-0019, restricted C-0026 | Exact passes; `code/verify_phase1.py` | Finite space exhausted; independent reimplementation remains useful |
| P1-A2 | Received transcription v1 | All 64 entries and 32 adjacent pairs | C-0002 | 28 R + 4 C; full TSV/Appendix A | Data check complete; change source/transcriber next |
| P1-A3 | Palace transcription v1 | All 64 cells and 28 R-orbits | C-0017–19 | Every cell/orbit passes; TSV/Appendix B | Table check complete; change source/edition next |
| P2-A1 | Original and seven ledger records | Claim-by-claim textual comparison | Does each ledger entry match the report and its evidence? | Two scope/evidence corrections: C-0017(b), C-0026; §3 | All assigned entries audited |
| P2-A2 | Six fixed prefix vectors plus remaining cube | All `C(58,2)=1653` extra-vector pairs | How nonautomatic is gap filling under a broad exact baseline? | 64 successes; `code/audit_phase2.py` | Exact class exhausted; historical justification absent |
| P2-A3 | Five local reversion choices | Revert one of lines 1–5; restore lower trigram | Which local variant yields a transversal? | Only line 4; `code/audit_phase2.py` | Exact class exhausted; broaden with preregistered grammar |
| P2-A4 | Source provenance | Supplied report/ledger and locally available files | Can Jing Fang/mnemonic provenance be verified? | No cited or local edition; undetermined | Requires external primary/secondary sources |

### 6.11 Evidence lineage and correlated-error risks

| Result | Independent derivation versus reuse | Shared inputs / risk | Required successor check |
|---|---|---|---|
| C-0001 | Blind Phase-1 derivation; later compared with original proof | Same registered definitions | Independent proof review only |
| C-0002 | Verifier-created full transcription and code; original supplied no data | Modern standard knowledge and Unicode can share received convention; bit data came from verifier memory | Edition/facsimile transcription by another researcher |
| C-0016 | Blind proof and code; later matched original proof | Both start from registered D | Recompute D image independently |
| C-0017 | Verifier's remembered conventional table checked against independently derived D | Both knowledge streams belong to the same broad modern tradition | Cited source plus independent transcribers |
| C-0018 | Algebraic consequence plus supplied mnemonic text | Mnemonic may derive from the same palace tradition | Date/source the mnemonic |
| C-0019 | Blind formal proof; full lookup in verifier table | Table aspect inherits C-0017 data | Variant/cited tables and prior-art search |
| C-0026 | Direct recoding proof | Depends on intended meaning of label swap | Confirm scope and conventions result-by-result |
| New comparison counts | Fresh exhaustive program | Significance depends entirely on chosen comparison classes | Preregister historically defensible grammar |

### 6.12 Novelty and use

- **New to me/this investigation:** the blind all-64/all-28 verifier checks and both exact comparison counts (`64/1653` and `1/5`). The finite table checks were produced in Phase 1; the comparison counts were added in Phase 2.
- **New to this research program:** the supplied ledger shows no earlier verification of the registered claims, so the verification record is new. The two comparison counts are not present in the supplied context and may be new to the program, but no exhaustive program-wide search was possible.
- **Literature novelty:** no search was performed, so none is claimed.
- **Use:** φ gives a constant-time palace-status classifier; the reversal law is a strong data-integrity test; the local-variant count supplies a concrete starting grammar for significance analysis.

### 6.13 Machine-readable research registry

| local_claim_id | exact_claim | evidence_type | status | domain | contingency | scope | dependencies | prior_claims | recommended_next_action |
|---|---|---|---|---|---|---|---|---|---|
| INV0005-F-R01 | σ is a fixed-point-free involution on F₂⁶. | proof; exhaustive 64-case execution | confirmed | formal | definition-driven | all six-bit words | R,C,σ | C-0001 | close after independent review |
| INV0005-F-R02 | Standard received adjacent pairs are 28 R-orbits and four C-orbits on the eight R-fixed figures. | complete transcription; exhaustive execution | confirmed | source-dependent | contingent | recorded standard received arrangement | encoding; received TSV; R01 | C-0002 | edition-derived transcription |
| INV0005-F-R03 | φ maps D bijectively to F₂³ and P×D→F₂⁶ is bijective. | complete proof; exhaustive execution | confirmed | formal | definition-driven | registered D exactly | P,D,φ | C-0016 | close mathematically; separate significance |
| INV0005-F-R04 | The stated sequential procedure yields D. | direct derivation | confirmed | formal | definition-driven | returning read from wandering figure to base lower trigram | procedure | C-0017(a) | source wording audit |
| INV0005-F-R05 | D matches every cell of the recorded conventional eight-palace table. | full 64-cell execution | confirmed | source-dependent | contingent | one transcription, not all variants or provenance | received and palace TSVs; R03-R04 | C-0017(b) | cited edition comparison |
| INV0005-F-R06 | Palace status and 世 position are functions of φ by the stated lookup. | proof; 64-cell execution | confirmed | formal and source-dependent | definition-driven formally; contingent traditionally | recorded D/table | R03,R05 | source mnemonic and table |
| INV0005-F-R07 | The quoted mnemonic corresponds to the lookup as an eight-pattern contextual rule. | textual/algebraic comparison | confirmed | source-dependent | contingent | supplied string; provenance excluded | R06 | C-0018 | locate dated attestation |
| INV0005-F-R08 | φ(Rx)=reverse(φ(x)) and induces the stated status reflection. | proof; exhaustive 64-case execution | confirmed | formal | definition-driven | all words | R06 | C-0019 | close mathematically |
| INV0005-F-R09 | All 28 R-orbits obey the status reflection in the recorded table. | exhaustive 28-orbit lookup | confirmed | source-dependent | contingent | one table, not “every standard table” | R05-R08 | C-0019 | variant-table census |
| INV0005-F-R10 | Coherent x↦Cx recoding preserves C-0001, C-0002, C-0016–19. | conjugacy/invariance proof; execution | confirmed | formal and source-dependent | definition-driven formally | assigned restriction only | R01-R09 | C-0026 | separate full-report audit |
| INV0005-F-R11 | With prefix generations fixed, exactly 64 of 1653 unordered extra-vector pairs complete a φ-transversal. | exhaustive finite count | confirmed | formal | definition-driven relative to artificial class | uniform pairs from remaining 58 words | prefix D; φ | C-0016 significance | replace with justified grammar |
| INV0005-F-R12 | If wandering reverts one changed line 1–5 and returning restores the lower trigram, only line 4 yields a transversal. | exhaustive five-case count | confirmed | formal/procedural | contingent on comparison family | exactly five stated variants | prefix D; φ | C-0016 significance | extend preregistered grammar |
| INV0005-F-O01 | The exact system is personally authored/known algebraically by historical Jing Fang. | no primary-source evidence | undetermined | historical | contingent | no authorship or awareness conclusion | primary sources missing | C-0017 | primary-source audit |
| INV0005-F-O02 | C-0019 is novel in the literature. | no literature search | undetermined | historical/interpretive | contingent | new-in-report is not literature novelty | prior art missing | C-0019 | prior-art search |

## 7. Final disposition

The assigned mathematics is accepted. The ledger should be updated with the final verdicts above, the complete verifier artifacts, and two scope corrections: C-0017(b) was not explicitly demonstrated in the original, and C-0026 was verified here only for the assignment's restricted claims. Historical provenance, mnemonic independence, universal table scope, and literature novelty remain open. No Phase-3 mathematical repair is required; the next decisive work is source-critical and bibliographic.
