# INV-0005 — ASN-0001: Verification of Reported Results on the Received Pairing and the Palace System

- **Role:** Adversarial Mathematical Verifier
- **Phase:** 1, blind independent derivation; the original reasoning and evidence were not supplied or inferred
- **Model:** OpenAI Codex, GPT-5 family (exact deployment identifier not exposed)
- **Materials supplied:** `context/objects/hexagrams.md`, `context/briefs/ASN-0001-phase1.md`, the assignment and common charter, all reproduced in `prompt-part1.md`
- **External source actually queried:** the locally installed Python `unicodedata` database, Unicode 13.0.0, for all names at U+4DC0–U+4DFF; this cross-checks the modern received number/name order, not the six-line extraction or ancient provenance
- **Tools actually used:** Python 3.9.6 code execution and plain-text TSV data; no network, web search, book, article, database, or original proof was consulted
- **Source of the two transcriptions:** my pre-existing knowledge of the standard received hexagram figures and the conventional 京房八宮 (Jing Fang eight-palace) table, entered before running the tests. This is independent of the withheld evidence but is not an edition-level source audit and is not a second verification of my own work.

## Provisional verdict table

Here “source” concerns correspondence to an attested or conventional arrangement, not merely internal consistency. A dash means that aspect is not asserted by the claim. No supplied claim makes a significance, novelty, rarity, or historical-intent claim beyond C-0017's attribution language.

| Claim | Mathematical correctness | Source correspondence | Significance claims | One-line reason |
|---|---|---|---|---|
| C-0001 | `confirmed` | — | — | A two-case proof shows that σ squares to the identity and changes every word. |
| C-0002 | `confirmed` | `confirmed` (provisional source basis) | — | In the full received transcription, all 32 adjacent pairs are σ-orbits: 28 reversal pairs and four complementary pairs of the eight palindromes. |
| C-0016 | `confirmed` | — | — | In D-order, φ(D) is `000,100,110,111,011,001,101,010`, all of F₂³ exactly once; the uniqueness claims follow from `ker φ=P`. |
| C-0017 | `confirmed` | `confirmed-with-corrections` | — | D reproduces all 64 cells of the conventional table transcribed here, but “Jing Fang” is confirmed only as the conventional system-name; actual authorship/use by the historical Jing Fang is `undetermined`. |
| C-0018 | `confirmed` | `confirmed` (for the conventional contextual reading of the mnemonic) | — | The eight φ-values give exactly the eight stated statuses, and every one of the 64 transcribed palace assignments agrees. |
| C-0019 | `confirmed` | `confirmed` (relative to the transcribed conventional table) | — | Formally `φ(Rx)=R₃φ(x)`; all 28 non-palindromic reversal orbits obey the induced generation swap in the palace table. |
| C-0026 | `confirmed` under the natural recoding | `confirmed-with-corrections` | — | A coherent label swap sends every old coordinate word x to Cx; it preserves φ and D and conjugates all relevant operations. It inherits C-0017's historical caveat. |

These verdicts are provisional Phase-1 verdicts. In particular, “source confirmed” above means agreement with the complete conventional transcriptions recorded below and, for the received names/order, a Unicode cross-check. It does **not** mean that a critical Zhouyi edition, a primary Jing Fang text, or variant palace traditions have already been audited.

## 1. Precise restatements, derivations, and provisional assessments

### C-0001 — σ is fixed-point-free involutive

**Precise restatement.** On the 64 words of \(\mathbb F_2^6\), define
\[
\sigma(x)=\begin{cases}R(x)&R(x)\ne x,\\ C(x)&R(x)=x.\end{cases}
\]
Then \(\sigma^2(x)=x\) and \(\sigma(x)\ne x\) for every x.

There is no material ambiguity once R and C are fixed. “No fixed points” means no coordinate word x satisfies \(\sigma(x)=x\).

**Derivation.** R and C commute, since reversing coordinates and toggling each coordinate commute.

- If \(Rx\ne x\), then \(R(Rx)=x\ne Rx\), so the first branch is used at both x and Rx. Thus \(\sigma^2x=R^2x=x\), while \(\sigma x=Rx\ne x\).
- If \(Rx=x\), then \(R(Cx)=C(Rx)=Cx\), so Cx is also R-fixed. The second branch is therefore used twice, giving \(\sigma^2x=C^2x=x\). Also \(Cx\ne x\), since each of six bits changes.

The executed exhaustive check over all 64 words agreed with the proof.

**Provisional verdict:** mathematical correctness `confirmed`. This is **definition-driven** and **standard elementary** (a short case split, not a contingent Yijing fact).

### C-0002 — received adjacent pairs are exactly the σ-orbits

**Precise restatement.** When each received hexagram number n is assigned the bottom-to-top word in Appendix A, the unordered sets \(\{2k-1,2k\}\) for \(1\le k\le32\) are the 32 two-element σ-orbits. Of those, the four pairs
\[
(1,2),\ (27,28),\ (29,30),\ (61,62)
\]
use C because both members are R-fixed; every other adjacent pair uses R.

The word “exactly” has two components: every adjacent pair is one σ-orbit, and because those 32 disjoint pairs exhaust 64 figures there are no further orbits.

**Transcription basis and source limitation.** Appendix A is my full received-order transcription. The number/name order was cross-checked by actually enumerating Unicode 13.0.0 characters U+4DC0–U+4DFF and inspecting all 64 official names. The trigram compounds and bottom-to-top words came from my pre-existing knowledge plus the supplied trigram bit convention; they were not extracted from Unicode or checked against a critical textual edition.

**Derivation/check.** Applying R to the Appendix-A words gives the following reversal pairs:

`3–4, 5–6, 7–8, 9–10, 11–12, 13–14, 15–16, 17–18, 19–20, 21–22, 23–24, 25–26, 31–32, 33–34, 35–36, 37–38, 39–40, 41–42, 43–44, 45–46, 47–48, 49–50, 51–52, 53–54, 55–56, 57–58, 59–60, 63–64`.

There are 28 of these. Exhaustively testing R-fixity gives exactly
\[
1,2,27,28,29,30,61,62.
\]
Their words and complements are
\[
111111\leftrightarrow000000,\quad
100001\leftrightarrow011110,\quad
010010\leftrightarrow101101,\quad
110011\leftrightarrow001100,
\]
which are respectively the four adjacent pairs listed above. C-0001 then makes each a two-element σ-orbit. The exhaustive program tested σ in both directions for every adjacent pair, not just the counts.

**Provisional verdict:** mathematical correctness `confirmed`; source correspondence `confirmed` on the stated provisional basis. The property is **contingent** on the received order and **nontrivial as a source pattern**, although its finite verification is elementary. No statistical rarity or editorial-intent conclusion follows from this check.

### C-0016 — D is a transversal for the doubled-trigram kernel

**Precise restatement.** Regard \(\phi:\mathbb F_2^6\to\mathbb F_2^3\) as
\[
\phi(l,u)=l\oplus u.
\]
The restriction \(\phi|_D\) is bijective. Consequently addition gives a bijection
\[
P\times D\longrightarrow\mathbb F_2^6,\qquad (b,d)\mapsto b\oplus d,
\]
and for fixed b each of the eight values of φ occurs once in \(b\oplus D\).

**Derivation.** Direct calculation in the supplied D-order gives:

| Status | d | lower(d) ⊕ upper(d) = φ(d) |
|---|---|---|
| pure | `000000` | `000` |
| 1st | `100000` | `100` |
| 2nd | `110000` | `110` |
| 3rd | `111000` | `111` |
| 4th | `111100` | `011` |
| 5th | `111110` | `001` |
| wandering | `111010` | `101` |
| returning | `000010` | `010` |

These are all eight three-bit words. Moreover,
\[
\ker\phi=\{(l,u):l=u\}=P.
\]
For any x, choose the unique \(d\in D\) with \(\phi(d)=\phi(x)\). Then
\(\phi(x\oplus d)=0\), so \(b=x\oplus d\in P\), giving existence. If
\(x=b\oplus d=b'\oplus d'\), application of φ gives
\(\phi(d)=\phi(d')\), whence \(d=d'\) and then \(b=b'\), giving uniqueness.
Finally, \(\phi(b\oplus d)=\phi(d)\) for \(b\in P\), so each palace has one member of each φ-value.

The executed program also enumerated all \(8\cdot8=64\) sums and checked that every six-bit word has exactly one decomposition.

**Provisional verdict:** `confirmed`. It is **definition-driven** and **standard elementary linear algebra/coset-transversal reasoning**. The choice of D is contingent on the supplied procedure, but the claim follows necessarily once D is fixed.

### C-0017 — correspondence of the procedure and D to the eight-palace tradition

**Precise restatement and ambiguity.** There are three separable assertions:

1. Sequentially applying the stated line changes to a doubled trigram produces the eight listed difference vectors D.
2. For each of the eight pure bases, those differences reproduce the conventional palace/generation assignments for all 64 hexagrams.
3. Calling this the “Jing Fang” construction either (weak reading) identifies the conventional tradition/system so named, or (strong reading) asserts that the historical Jing Fang personally authored or used this exact procedure/table.

The word “then” matters: the returning-soul operation restores the lower trigram **of the wandering-soul figure**, not independently of the fifth-generation figure. The latter reading would give a different vector and is not the standard table.

**Independent derivation of D from the stated procedure.** Relative to a base b, the cumulative changes are
\[
000000,100000,110000,111000,111100,111110.
\]
Reverting line 4 toggles the fourth coordinate of `111110`, yielding `111010`. Restoring coordinates 1–3 to the base then yields `000010`. Thus assertion 1 is exact.

**Full table comparison.** Appendix B is my pre-computation transcription of the conventional table. For each row the executed program looked up the received word x and the palace base b, and checked
\[
x=b\oplus D[\text{slot}].
\]
All 64 distinct rows passed, with all received numbers 1–64 appearing exactly once. This is a cell-by-cell check, not an inference from a few exemplar palaces.

**Source and variants.** My source here is pre-existing knowledge of the standard 八宮卦 sequence used in the Jing Fang/Najia tradition; I did not consult an edition during this phase. I know of harmless presentational variants in palace-block order, character form, and the labels `本宮`, `本卦`, or `六世` for the pure member. Procedural mnemonics also phrase the last two moves differently (for example, “游魂復/變四，歸魂變下三”), but when read sequentially they give the same membership table. I did not check a corpus of editions and do not claim that no substantive historical variant exists.

**Provisional verdicts:**

- Assertions 1 and 2: mathematical correctness `confirmed`; conventional-table correspondence `confirmed` relative to Appendix B.
- Assertion 3, weak system-name reading: `confirmed-with-corrections`—the exact safe statement is “this is the conventional eight-palace construction attributed to Jing Fang.”
- Assertion 3, strong historical-authorship/use reading: `undetermined`; a dated primary-source audit is missing.

This claim is **definition-driven** for assertion 1 and **contingent/source-dependent** for assertions 2–3. The encoding is elementary; the 64-cell source comparison is **nontrivial** even though no individual cell is difficult.

### C-0018 — generation is exactly a function of φ

**Precise restatement.** Under the unique palace assignment of C-0016/C-0017, the status of x is determined solely by the three-bit word \(\phi(x)\), with the asserted eight-row lookup. “Generation” is being used broadly to include `pure/6th`, wandering soul, and returning soul, not only generations 1–5. `Pure/6th` means the pure palace hexagram, traditionally with the 世 line at line 6; it need not be called a chronological “sixth generation.”

**Derivation.** If \(x=b\oplus d\), then \(\phi(x)=\phi(b)\oplus\phi(d)=\phi(d)\), because \(b\in P=\ker\phi\). C-0016 makes d, hence its status, a function of φ(x). The calculation is:

| φ(x), earth-man-heaven differences | Status | Mnemonic clause under its conventional exact-pattern reading |
|---|---|---|
| `000`, none | pure/6th | 本宮六世 |
| `100`, earth only | 1st | 地變初 |
| `110`, earth and man | 2nd | 天同二世 |
| `111`, all three | 3rd | 三世異 |
| `011`, man and heaven | 4th | 地同四世 |
| `001`, heaven only | 5th | 天變五 |
| `101`, earth and heaven | wandering | 人同游魂 |
| `010`, man only | returning | 人變歸 |

The short mnemonic is contextual: for example, `天同二世` does not mean that every pattern with the heaven bit equal is second generation; it names the exact pattern where heaven alone agrees. With this standard eight-case reading, it is precisely the stated truth table. Independently of the algebraic deduction, the program compared this lookup with every Appendix-B row; all 64 passed.

**Provisional verdict:** mathematical correctness `confirmed`; mnemonic/conventional-table correspondence `confirmed`, with the contextual-reading caveat above. The formal dependence is **definition-driven and standard** once D is known; the match to traditional assignments and wording is **contingent and source-dependent**.

### C-0019 — reversal reverses φ and swaps the corresponding statuses

**Precise restatement.** Let \(R_3(a,b,c)=(c,b,a)\). The claim is
\(\phi(R_6x)=R_3\phi(x)\) for every x. Composing the C-0018 lookup with \(R_3\) gives the stated status involution. The source-dependent last sentence says that all 28 non-palindromic R-orbits, as assigned in the conventional palace table, realize that involution.

**Derivation.** Write \(x=(l,u)\), where l and u are stored bottom-to-top. Then
\[
R_6x=(R_3u,R_3l),
\]
so, using linearity of reversal over coordinatewise XOR,
\[
\phi(R_6x)=R_3u\oplus R_3l
=R_3(u\oplus l)=R_3(l\oplus u)=R_3\phi(x).
\]
The resulting status map is
\[
\text{1st}\leftrightarrow\text{5th},\qquad
\text{2nd}\leftrightarrow\text{4th},
\]
with `pure/6th`, `3rd`, `wandering`, and `returning` fixed. This follows by reversing each of the eight φ-words in C-0018.

The executed check evaluated the identity on all 64 words. It then formed every non-palindromic R-orbit from the full cube, found exactly 28, looked up both endpoints in Appendix B, and checked the status map. All passed. It separately checked that those 28 orbits equal the 28 received adjacent reversal pairs from C-0002.

**Provisional verdict:** mathematical correctness `confirmed`; conventional table correspondence `confirmed` relative to Appendix B. The identity and induced map are **definition-driven and standard**; the statement about the particular traditional table is **contingent/source-dependent** and its complete 28-orbit check is nontrivial as data validation.

### C-0026 — invariance under swapping the binary line labels

**Precise restatement and reading.** A coherent change from yang=1/yin=0 to yang=0/yin=1 sends the coordinate word for every fixed physical figure from x to
\(T(x)=Cx=x\oplus111111\). All definitions must then be applied in the new coordinates. On this natural reading, the earlier claims retain the same truth values. Merely changing the prose attached to 0 and 1 while holding every word-to-figure association fixed is not a recoding of the same data and is not the reading assessed here.

**Derivation.** The following identities settle the formal claims:
\[
RT=TR,\qquad CT=TC,\qquad \sigma T=T\sigma,
\]
where the last identity also uses preservation of R-fixity by T. Further,
\[
\phi(T(l,u))=(l\oplus111)\oplus(u\oplus111)=l\oplus u=\phi(l,u).
\]
If an old palace member is \(x=b\oplus d\), its new coordinates are
\[
Tx=Tb\oplus d.
\]
Thus the base changes to the oppositely encoded doubled trigram while the difference vector d, D membership, φ-value, and status do not change. Received physical order and palace names/numbers are unchanged, and reversal relations are conjugated by T. The executed program checked these assertions over all words, pairs, and 64 palace rows.

**Provisional verdict:** mathematical correctness `confirmed` under coherent global recoding; source correspondence `confirmed-with-corrections`, because a representational change adds no historical evidence and therefore inherits C-0017's authorship limitation. This is **definition-driven and standard change-of-coordinates symmetry** for the mathematics; any source correspondence remains contingent on the underlying physical transcription.

## 2. Computation and reproducibility

The computation was **actually executed**, not merely described. The exact command was:

```sh
/usr/bin/python3 -B code/verify_phase1.py
```

The sandbox emitted two harmless inability-to-create-compiler-cache warnings, after which Python exited with code 0 and printed:

```text
PASS input integrity: 64 received figures; 64 palace-table entries
PASS C-0001: exhaustive over 64 words
PASS C-0002: 32 adjacent sigma-orbits = 28 R-pairs + 4 C-pairs
  R-fixed numbers: 1,2,27,28,29,30,61,62
PASS C-0016: phi(D) in D order = 000,100,110,111,011,001,101,010
PASS C-0017(table): all 64 source-table cells equal base xor D[slot]
PASS C-0018: all 64 source statuses equal status(phi(x))
PASS C-0019: identity on 64 words and status rule on 28 R-orbits
PASS C-0026: coherent global label swap checks
```

The complete implementation is `code/verify_phase1.py`. Its complete input data are `data/received_order.tsv` and `data/eight_palaces_source.tsv`, also reproduced in human-readable form in Appendices A and B. The program uses only Python's standard library. It validates row counts, number coverage, bit uniqueness, trigram concatenation, and name agreement before testing any claim.

This is my own implementation checking my own transcription and derivation. It is reproducible evidence and was blind to the withheld proof, but it is **not** described as independent verification of itself. In particular, shared transcription mistakes could survive internal consistency checks.

## 3. Research handoff

### 3.1 Executive findings

All formal mathematical claims survive Phase 1. The strongest unifying fact is that P is exactly \(\ker\phi\) and D is a complete transversal detected by φ. That one quotient-space observation proves the partition, the one-of-each-φ property, and the generation lookup. Reversal descends to coordinate reversal on the quotient, giving the generation swaps without consulting the received order.

The two contingent arrangements also match: the complete received transcription has the claimed σ pairing, and the complete conventional palace transcription is reproduced cell-for-cell by D. The only material unresolved point is historical/source-critical: no primary source was checked, so strict authorship by the historical Jing Fang and universality across variants remain undetermined.

### 3.2 Exact mathematical results

1. **Fixed-point-free involution theorem.** The piecewise map σ is a fixed-point-free involution on \(\mathbb F_2^6\).
2. **Received pairing result.** On Appendix A, the adjacent received pairs are 28 R-orbits and four C-orbits on the eight R-fixed words.
3. **Transversal theorem.** \(P=\ker\phi\), \(\phi|_D\) is bijective, and addition \(P\times D\to\mathbb F_2^6\) is bijective.
4. **Status factorization.** The conventional palace status map factors as \(g\circ\phi\), where g is the eight-row C-0018 lookup.
5. **Equivariance theorem.** \(\phi R_6=R_3\phi\); hence status reversal is exactly 1↔5, 2↔4, with the other four classes fixed.
6. **Recoding invariance.** Global line-label recoding T=C preserves φ and D-differences and conjugates the received-pair operations.

Proofs and exhaustive procedures are given above and in the code.

### 3.3 Failed hypotheses and negative results

- No supplied mathematical statement was refuted.
- A strong reading of “is the Jing Fang construction” as a demonstrated historical-authorship claim was **not established**. This is missing evidence, not a counterexample.
- The mnemonic cannot be read as eight independent one-bit implications; e.g. “heaven agrees” alone describes four φ-patterns. It matches the table only under its conventional exact-pattern/contextual reading. This corrects a possible over-literal interpretation but does not refute C-0018.
- No claim of statistical rarity, explanatory uniqueness, editorial intention, or historical mathematical intent was tested, because none was formally supplied.

### 3.4 Unresolved conjectures/questions

1. Does the extant text attributed to Jing Fang explicitly attest the exact eight-step procedure, or only a table/equivalent assignment? Primary text, edition, passage, and dating are needed.
2. Are there historically attested palace tables with substantively different membership or generation assignments, rather than merely a different block layout, glyph form, or terminology?
3. Does a critical received-text edition give exactly the same 64 figure/number correspondences as Appendix A? This is overwhelmingly expected but was not source-critically checked here.
4. What, if anything, is mathematically or historically distinctive about the received order realizing the σ-orbits consecutively? The present work proves the fact, not its rarity or cause.

### 3.5 Dependencies

- C-0001 uses only supplied R/C/σ definitions.
- C-0002 uses the supplied encoding convention and Appendix A; source confidence depends on that transcription.
- C-0016 uses only the supplied D, P, and φ.
- C-0017's formal encoding uses the stated sequential procedure; its table claim uses both appendices; attribution requires external historical evidence not used here.
- C-0018 depends mathematically on C-0016 and source-wise on Appendix B and the conventional reading of the mnemonic.
- C-0019 depends mathematically on the definitions and, for generation labels, C-0018; its last sentence uses both appendices.
- C-0026 assumes “swap labels” means a coherent global recoding of every physical figure.

### 3.6 Alternative explanations and generalizations

- C-0016 is not intrinsically a specifically Yijing phenomenon. For any \(n\), the map \((l,u)\mapsto l\oplus u\) on \(\mathbb F_2^{2n}\) has diagonal kernel, and any set selecting one representative of each quotient class gives an analogous \(2^n\)-by-\(2^n\) partition. What is contingent here is that the traditional D happens to be such a transversal and which labels its representatives carry.
- C-0018 is therefore an immediate quotient-coordinate description of the supplied palace procedure, not separate evidence that the procedure was designed from XOR or binary algebra.
- C-0019 follows from reversal equivariance for any length 2n split into two n-blocks. Its formal identity alone has no demonstrated historical significance.
- C-0002 may reflect the known received practice of pairing inverse figures and complementing vertically symmetric figures. Mathematics alone does not decide when, why, or by whom that editorial rule arose.

### 3.7 Reproducibility

The exact code, data, command, output, conventions, and complete transcriptions are supplied above and below. The search space was the full finite set of 64 six-bit words; there was no random seed, sampling, pruning, tolerance, or unreported parameter. Python version was 3.9.6; only `csv`, `itertools`, and `pathlib` were used.

### 3.8 Opportunities for further research

- Build an edition-cited, image-backed data lineage for both arrangements and have a second researcher transcribe each independently.
- Collate palace variants chronologically and distinguish system attribution, textual attestation, and historical authorship.
- Generalize the quotient/transversal characterization to classify all line-change procedures whose status is a function only of lower/upper trigram difference.
- Quantify how restrictive consecutive σ-pairing is among plausible sequence models before attaching significance to C-0002.

### 3.9 Recommended next assignments and next-step contracts

| Assignment | Precise question | Minimum inputs | Cheapest decisive check | Possible outcomes and effect | Stopping condition |
|---|---|---|---|---|---|
| Primary-source palace audit | Does a specified early/received text attest these exact 64 memberships and the sequential last two moves? | Edition scans/transcription, bibliographic metadata, passage locations | Double-transcribe every named hexagram and procedural verb, then diff against Appendix B/D | Exact match confirms source correspondence; equivalent table but different procedure narrows C-0017(a); mismatch yields a variant/counterexample; silence leaves authorship undetermined | Every relevant passage in the selected witnesses is cited and every one of 64 cells is accounted for |
| Independent received-figure audit | Are all Appendix-A name/number/line triples correct in a critical edition? | One or preferably two edition facsimiles with figure glyphs | Independent bottom-to-top six-line transcription followed by a 64-row diff | Match upgrades source confidence; any mismatch localizes C-0002's dependence | Two independent transcriptions reconcile all discrepancies |
| Variant palace census | Are there substantive historical variants of membership/status? | A bounded, dated corpus of palace tables | Normalize character, block-order, and terminology variants; compare the 64 `(number,status,palace)` triples | No differences in the bounded corpus supports stability; differences delimit C-0017–19 | Corpus and inclusion dates are fixed in advance and all tables are normalized |
| Distinctiveness of received pairing | Is adjacency of σ-orbits unusual under an explicit null model or constrained family? | Appendix A, σ, and a justified family of alternative orders | Count/prove the proportion of orders satisfying the same adjacency condition, with constraints declared first | Tiny rate under a justified model supports rarity; high/definition-driven rate deflates it; model sensitivity leaves significance unresolved | Exact count/proof for the declared finite family or predeclared Monte Carlo precision |

**Promising approach not attempted:** a facsimile-level primary-source audit that extracts the line glyphs and palace entries directly from dated editions, with two blind transcribers. It was not attempted because no such source corpus was supplied or locally available in this blind phase.

### 3.10 Search log

| Attempt | Object/source and version | Representation/operations | Exact question/bounds | Outcome/evidence | Why stopped / successor change |
|---|---|---|---|---|---|
| A1 | Supplied formal definitions | Exhaustive strings in \(\{0,1\}^6\), R/C/σ/φ/XOR | All 64 words; all formal claims | All assertions passed; `code/verify_phase1.py` | Exhaustive finite bounds reached; successor can independently reimplement |
| A2 | My received-order transcription v1 | 64 numbered bottom-to-top words | All 32 adjacent pairs, all R-fixed words, complete word coverage | 28 R-pairs, 4 C-pairs; Appendix A and executed output | Exact finite check complete; successor should change the source/transcriber, not search bounds |
| A3 | My conventional palace transcription v1 | 64 `(palace,slot,number)` cells plus received words | Compare every cell with `base XOR D[slot]`; compare every status with φ | 64/64 matches; Appendix B and executed output | Exact finite check complete; successor should use an edition-derived table |
| A4 | Python `unicodedata` 13.0.0 | U+4DC0–U+4DFF official names in code-point order | Cross-check all 64 modern received number/name positions | All 64 enumerated and manually inspected; command described in header/source note | Unicode is not a critical historical edition and does not independently extract my bit words |
| A5 | Conventional mnemonic as quoted | Eight exact φ-patterns | Does each clause match one status, and can clauses stand as one-bit implications? | Exact-pattern reading matches all eight; isolated one-bit reading is underdetermining | Linguistic/source audit requires historical commentaries not available here |

### 3.11 Evidence lineage and shared-error risks

| Result | Lineage | Shared inputs / correlated-error risks | Successor must check |
|---|---|---|---|
| C-0001 | Blind derivation from supplied definitions plus own exhaustive implementation | Same author wrote proof and code | Reimplement or inspect case split |
| C-0002 | My own received transcription; Unicode cross-check only for modern order/names; own program | My memory may correlate figure compositions and pairing expectations; Unicode modern standard may reproduce received convention without historical evidence | Edition-derived figures, independent transcriber |
| C-0016 | Blind derivation from supplied D/P/φ plus own program | D itself came from the claim; proof and code share it | Recompute φ(D) from registered statement |
| C-0017 | Palace table entered from my prior knowledge before computation; generated D derived separately from prose | Both my remembered table and understanding of procedure come from the same broad modern tradition | Primary/edition sources and variant corpus |
| C-0018 | Algebra from C-0016 plus 64-row table comparison | Depends on D and Appendix B; mnemonic segmentation is conventional | Historical mnemonic context and independent table |
| C-0019 | Direct algebra plus all-orbit table lookup | Table portion inherits both appendices | Independent implementation and source tables |
| C-0026 | Direct coordinate-change proof plus exhaustive check | Assumes coherent global recoding | Confirm alternative author intended same reading |

### 3.12 Novelty and use

- **New to me in this run:** the claims were derived blind and the complete cross-table equivalences were computed here.
- **New to this program:** not claimed; every central statement was already present as a reported claim.
- **Literature novelty:** not assessed and not claimed. No literature search was performed.
- **Concrete use:** φ provides a constant-time, palace-base-free classifier for conventional generation/status; the reversal identity provides a compact consistency check for any digitized palace table. The quotient proof also exposes exactly which parts are generic binary algebra rather than distinctive historical structure.

### 3.13 Machine-readable research registry

| local_claim_id | exact_claim | evidence_type | status | domain | contingency | scope | dependencies | prior_claims | recommended_next_action |
|---|---|---|---|---|---|---|---|---|---|
| INV0005-P1-R01 | σ is a fixed-point-free involution on F2^6. | two-case proof; exhaustive 64-word execution | confirmed | formal | definition-driven | all 64 six-bit words | supplied R,C,σ | C-0001 | independent code/proof review only |
| INV0005-P1-R02 | The 32 received adjacent pairs are exactly 28 R-orbits plus four C-orbits on R-fixed figures. | complete transcription; exhaustive 32-pair execution | confirmed | source-dependent | contingent | Appendix-A received order | encoding; Appendix A; R01 | C-0002 | independent critical-edition transcription |
| INV0005-P1-R03 | φ maps D bijectively to F2^3 and addition P×D→F2^6 is bijective. | explicit image table; kernel proof; exhaustive 64-sum execution | confirmed | formal | definition-driven | supplied P,D,φ exactly | supplied definitions | C-0016 | independent proof/code review only |
| INV0005-P1-R04 | The stated sequential procedure yields exactly D. | direct eight-step derivation | confirmed | formal | definition-driven | procedure read sequentially, returning after wandering | supplied procedure | C-0017(a) | audit wording against primary source |
| INV0005-P1-R05 | D reproduces all 64 assignments in the conventional eight-palace table transcribed here. | complete 64-cell table comparison | confirmed | source-dependent | contingent | Appendix B, not all possible variants | Appendices A-B; R03-R04 | C-0017(b) | edition-derived independent table |
| INV0005-P1-R06 | The exact construction/table is historically Jing Fang's own. | no primary-source evidence | undetermined | historical | contingent | no authorship conclusion; conventional attribution only | dated primary sources missing | C-0017(a) | primary-source palace audit |
| INV0005-P1-R07 | Conventional status is the stated function of φ. | algebraic deduction; eight-row truth table; 64-cell comparison | confirmed | formal and source-dependent | definition-driven formally; contingent as tradition | supplied D and Appendix B | R03; R05 | audit mnemonic in context |
| INV0005-P1-R08 | φ(Rx)=reverse(φ(x)), inducing 1↔5 and 2↔4 and fixing four statuses; all 28 R-orbits match the table. | algebraic proof; exhaustive 64-word and 28-orbit execution | confirmed | formal and source-dependent | definition-driven formally; contingent for table | all words/orbits under Appendices A-B | R02; R07 | independent table/code check |
| INV0005-P1-R09 | Coherent global yin/yang label recoding preserves C-0001, C-0002, C-0016–19. | conjugacy/invariance proof; exhaustive execution | confirmed-with-corrections | formal and source-dependent | definition-driven formally | natural recoding x→Cx; inherits R06 limitation | R01-R08 | confirm intended reading; no new historical inference |

## Appendix A — complete received-order transcription

Conventions: each six-bit word is \(x_1\ldots x_6\), bottom to top. “Lower / upper” names and writes the two trigrams in that same storage convention. Traditional compound descriptions often say the upper trigram first; this table deliberately does not.

| No. | Name | Lower / upper | Word x1…x6 |
|---:|---|---|---|
| 1 | 乾 (Qian) | Qian `111` / Qian `111` | `111111` |
| 2 | 坤 (Kun) | Kun `000` / Kun `000` | `000000` |
| 3 | 屯 (Zhun) | Zhen `100` / Kan `010` | `100010` |
| 4 | 蒙 (Meng) | Kan `010` / Gen `001` | `010001` |
| 5 | 需 (Xu) | Qian `111` / Kan `010` | `111010` |
| 6 | 訟 (Song) | Kan `010` / Qian `111` | `010111` |
| 7 | 師 (Shi) | Kan `010` / Kun `000` | `010000` |
| 8 | 比 (Bi) | Kun `000` / Kan `010` | `000010` |
| 9 | 小畜 (Xiao Chu) | Qian `111` / Xun `011` | `111011` |
| 10 | 履 (Lu) | Dui `110` / Qian `111` | `110111` |
| 11 | 泰 (Tai) | Qian `111` / Kun `000` | `111000` |
| 12 | 否 (Pi) | Kun `000` / Qian `111` | `000111` |
| 13 | 同人 (Tong Ren) | Li `101` / Qian `111` | `101111` |
| 14 | 大有 (Da You) | Qian `111` / Li `101` | `111101` |
| 15 | 謙 (Qian, Modesty) | Gen `001` / Kun `000` | `001000` |
| 16 | 豫 (Yu) | Kun `000` / Zhen `100` | `000100` |
| 17 | 隨 (Sui) | Zhen `100` / Dui `110` | `100110` |
| 18 | 蠱 (Gu) | Xun `011` / Gen `001` | `011001` |
| 19 | 臨 (Lin) | Dui `110` / Kun `000` | `110000` |
| 20 | 觀 (Guan) | Kun `000` / Xun `011` | `000011` |
| 21 | 噬嗑 (Shi He) | Zhen `100` / Li `101` | `100101` |
| 22 | 賁 (Bi, Grace) | Li `101` / Gen `001` | `101001` |
| 23 | 剝 (Bo) | Kun `000` / Gen `001` | `000001` |
| 24 | 復 (Fu) | Zhen `100` / Kun `000` | `100000` |
| 25 | 無妄 (Wu Wang) | Zhen `100` / Qian `111` | `100111` |
| 26 | 大畜 (Da Chu) | Qian `111` / Gen `001` | `111001` |
| 27 | 頤 (Yi) | Zhen `100` / Gen `001` | `100001` |
| 28 | 大過 (Da Guo) | Xun `011` / Dui `110` | `011110` |
| 29 | 坎 (Kan) | Kan `010` / Kan `010` | `010010` |
| 30 | 離 (Li) | Li `101` / Li `101` | `101101` |
| 31 | 咸 (Xian) | Gen `001` / Dui `110` | `001110` |
| 32 | 恆 (Heng) | Xun `011` / Zhen `100` | `011100` |
| 33 | 遯 (Dun) | Gen `001` / Qian `111` | `001111` |
| 34 | 大壯 (Da Zhuang) | Qian `111` / Zhen `100` | `111100` |
| 35 | 晉 (Jin) | Kun `000` / Li `101` | `000101` |
| 36 | 明夷 (Ming Yi) | Li `101` / Kun `000` | `101000` |
| 37 | 家人 (Jia Ren) | Li `101` / Xun `011` | `101011` |
| 38 | 睽 (Kui) | Dui `110` / Li `101` | `110101` |
| 39 | 蹇 (Jian, Obstruction) | Gen `001` / Kan `010` | `001010` |
| 40 | 解 (Xie) | Kan `010` / Zhen `100` | `010100` |
| 41 | 損 (Sun) | Dui `110` / Gen `001` | `110001` |
| 42 | 益 (Yi, Increase) | Zhen `100` / Xun `011` | `100011` |
| 43 | 夬 (Guai) | Qian `111` / Dui `110` | `111110` |
| 44 | 姤 (Gou) | Xun `011` / Qian `111` | `011111` |
| 45 | 萃 (Cui) | Kun `000` / Dui `110` | `000110` |
| 46 | 升 (Sheng) | Xun `011` / Kun `000` | `011000` |
| 47 | 困 (Kun, Oppression) | Kan `010` / Dui `110` | `010110` |
| 48 | 井 (Jing) | Xun `011` / Kan `010` | `011010` |
| 49 | 革 (Ge) | Li `101` / Dui `110` | `101110` |
| 50 | 鼎 (Ding) | Xun `011` / Li `101` | `011101` |
| 51 | 震 (Zhen) | Zhen `100` / Zhen `100` | `100100` |
| 52 | 艮 (Gen) | Gen `001` / Gen `001` | `001001` |
| 53 | 漸 (Jian, Development) | Gen `001` / Xun `011` | `001011` |
| 54 | 歸妹 (Gui Mei) | Dui `110` / Zhen `100` | `110100` |
| 55 | 豐 (Feng) | Li `101` / Zhen `100` | `101100` |
| 56 | 旅 (Lu, Traveller) | Gen `001` / Li `101` | `001101` |
| 57 | 巽 (Xun) | Xun `011` / Xun `011` | `011011` |
| 58 | 兌 (Dui) | Dui `110` / Dui `110` | `110110` |
| 59 | 渙 (Huan) | Kan `010` / Xun `011` | `010011` |
| 60 | 節 (Jie) | Dui `110` / Kan `010` | `110010` |
| 61 | 中孚 (Zhong Fu) | Dui `110` / Xun `011` | `110011` |
| 62 | 小過 (Xiao Guo) | Gen `001` / Zhen `100` | `001100` |
| 63 | 既濟 (Ji Ji) | Li `101` / Kan `010` | `101010` |
| 64 | 未濟 (Wei Ji) | Kan `010` / Li `101` | `010101` |

## Appendix B — complete conventional eight-palace transcription

The palace blocks appear in the conventional order 乾、坎、艮、震、巽、離、坤、兌 used in my source memory. Block order itself is not used in any proof. `pure/6th` records both the pure-palace status and the traditional sixth-line 世 designation. The words come from Appendix A; φ is recomputed from each word, not copied from D.

| Palace | Status | Hexagram | Word x1…x6 | φ |
|---|---|---:|---|---|
| 乾 (Qian) | pure/6th | 1 乾 | `111111` | `000` |
| 乾 (Qian) | 1st | 44 姤 | `011111` | `100` |
| 乾 (Qian) | 2nd | 33 遯 | `001111` | `110` |
| 乾 (Qian) | 3rd | 12 否 | `000111` | `111` |
| 乾 (Qian) | 4th | 20 觀 | `000011` | `011` |
| 乾 (Qian) | 5th | 23 剝 | `000001` | `001` |
| 乾 (Qian) | wandering | 35 晉 | `000101` | `101` |
| 乾 (Qian) | returning | 14 大有 | `111101` | `010` |
| 坎 (Kan) | pure/6th | 29 坎 | `010010` | `000` |
| 坎 (Kan) | 1st | 60 節 | `110010` | `100` |
| 坎 (Kan) | 2nd | 3 屯 | `100010` | `110` |
| 坎 (Kan) | 3rd | 63 既濟 | `101010` | `111` |
| 坎 (Kan) | 4th | 49 革 | `101110` | `011` |
| 坎 (Kan) | 5th | 55 豐 | `101100` | `001` |
| 坎 (Kan) | wandering | 36 明夷 | `101000` | `101` |
| 坎 (Kan) | returning | 7 師 | `010000` | `010` |
| 艮 (Gen) | pure/6th | 52 艮 | `001001` | `000` |
| 艮 (Gen) | 1st | 22 賁 | `101001` | `100` |
| 艮 (Gen) | 2nd | 26 大畜 | `111001` | `110` |
| 艮 (Gen) | 3rd | 41 損 | `110001` | `111` |
| 艮 (Gen) | 4th | 38 睽 | `110101` | `011` |
| 艮 (Gen) | 5th | 10 履 | `110111` | `001` |
| 艮 (Gen) | wandering | 61 中孚 | `110011` | `101` |
| 艮 (Gen) | returning | 53 漸 | `001011` | `010` |
| 震 (Zhen) | pure/6th | 51 震 | `100100` | `000` |
| 震 (Zhen) | 1st | 16 豫 | `000100` | `100` |
| 震 (Zhen) | 2nd | 40 解 | `010100` | `110` |
| 震 (Zhen) | 3rd | 32 恆 | `011100` | `111` |
| 震 (Zhen) | 4th | 46 升 | `011000` | `011` |
| 震 (Zhen) | 5th | 48 井 | `011010` | `001` |
| 震 (Zhen) | wandering | 28 大過 | `011110` | `101` |
| 震 (Zhen) | returning | 17 隨 | `100110` | `010` |
| 巽 (Xun) | pure/6th | 57 巽 | `011011` | `000` |
| 巽 (Xun) | 1st | 9 小畜 | `111011` | `100` |
| 巽 (Xun) | 2nd | 37 家人 | `101011` | `110` |
| 巽 (Xun) | 3rd | 42 益 | `100011` | `111` |
| 巽 (Xun) | 4th | 25 無妄 | `100111` | `011` |
| 巽 (Xun) | 5th | 21 噬嗑 | `100101` | `001` |
| 巽 (Xun) | wandering | 27 頤 | `100001` | `101` |
| 巽 (Xun) | returning | 18 蠱 | `011001` | `010` |
| 離 (Li) | pure/6th | 30 離 | `101101` | `000` |
| 離 (Li) | 1st | 56 旅 | `001101` | `100` |
| 離 (Li) | 2nd | 50 鼎 | `011101` | `110` |
| 離 (Li) | 3rd | 64 未濟 | `010101` | `111` |
| 離 (Li) | 4th | 4 蒙 | `010001` | `011` |
| 離 (Li) | 5th | 59 渙 | `010011` | `001` |
| 離 (Li) | wandering | 6 訟 | `010111` | `101` |
| 離 (Li) | returning | 13 同人 | `101111` | `010` |
| 坤 (Kun) | pure/6th | 2 坤 | `000000` | `000` |
| 坤 (Kun) | 1st | 24 復 | `100000` | `100` |
| 坤 (Kun) | 2nd | 19 臨 | `110000` | `110` |
| 坤 (Kun) | 3rd | 11 泰 | `111000` | `111` |
| 坤 (Kun) | 4th | 34 大壯 | `111100` | `011` |
| 坤 (Kun) | 5th | 43 夬 | `111110` | `001` |
| 坤 (Kun) | wandering | 5 需 | `111010` | `101` |
| 坤 (Kun) | returning | 8 比 | `000010` | `010` |
| 兌 (Dui) | pure/6th | 58 兌 | `110110` | `000` |
| 兌 (Dui) | 1st | 47 困 | `010110` | `100` |
| 兌 (Dui) | 2nd | 45 萃 | `000110` | `110` |
| 兌 (Dui) | 3rd | 31 咸 | `001110` | `111` |
| 兌 (Dui) | 4th | 39 蹇 | `001010` | `011` |
| 兌 (Dui) | 5th | 15 謙 | `001000` | `001` |
| 兌 (Dui) | wandering | 62 小過 | `001100` | `101` |
| 兌 (Dui) | returning | 54 歸妹 | `110100` | `010` |
