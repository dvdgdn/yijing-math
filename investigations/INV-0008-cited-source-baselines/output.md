# INV-0008 — Cited source baselines for the received order, the eight palaces and the divination procedure

- **Investigation:** INV-0008. **Assignment:** ASN-0007, "Establish cited source baselines and an intake plan for neglected material".
- **Role:** specialist (source work). The assignment specifies targeted context; this run was full-context (see `record.md`, Deviations).
- **Model:** Claude Opus 5.5 (exact identifier unknown). Same model family as INV-0001 and INV-0004.
- **Date:** 2026-11-01.
- **Tools and materials:**
  - Shell with Python 3.9.6.
  - Web search, plus the Wikisource (zh) MediaWiki API.
  - Full repository context, including INV-0001's claims, INV-0004, and INV-0005's saved blind phase-1 transcriptions.
  - The ctext.org API was tried and refused unauthenticated access, so it was not used.

**Nothing in this report is a verification under the protocol.** Every dataset is a working transcription. Two digital witnesses were compared mechanically; none was checked against a printed edition.

## 1. Executive findings

**Source packages built.** Three cited source packages now exist where `data/` held none. Each rests on hash-pinned snapshots of 184 Wikisource pages at fixed revision IDs (`sources/manifest.json`).

1. **D-1, received order** (`data/zhouyi-received-order.v1.csv`):
   - Taken from two independent Wikisource transcriptions:
     - the *Zhouyi* chapter pages (W1);
     - Kong Yingda's *Zhouyi zhengyi* (W2).
   - Each hexagram's six lines are parsed from the classic's own line-statement headings (初九 … 上六). No trigram convention is assumed.
   - W1 and W2 agree on every name (one spelling variant, 无妄/無妄), on the order, on all 384 line headings and on all 64 trigram compositions.
   - The trigram patterns are derived from the eight doubled chapters. The 56 other compositions then agree with the headings without exception.
   - The *Xugua* commentary independently attests the sequence: in both witnesses, the 61 hexagrams it introduces appear exactly in received positions 3–30 and 32–64.
2. **D-2, eight palaces** (`data/jingshi-yizhuan-eight-palaces.v1.csv`):
   - Taken from two Wikisource witnesses of the *Jingshi Yizhuan* 京氏易傳: a modern collated text (J1) and the Siku Quanshu text (J2).
   - All 64 entries agree in sequence, name (after recorded variant normalization) and trigram composition.
   - Every palace begins with a doubled trigram, in the text's order 乾 震 坎 艮 坤 巽 離 兌.
   - For every entry the text states which line holds the world (世). In 57 entries it names 世 outright; in 7 it says which line 居尊 or 立元首, and so on. The stated line follows the position pattern 6, 1, 2, 3, 4, 5, 4, 3 (pure, first to fifth generation, wandering soul, returning soul) for all 64.
3. **D-7, procedure texts** (`data/procedure-texts.v1.csv`):
   - The *Xici* dayan passage, in two witnesses whose arrangement differs.
   - Zhu Xi's 筮儀 and 明筮 from the *Yuanben Zhouyi benyi* (Siku text).
   - Jia Gongyan's Tang-dynasty account of coin divination, and Gu Yanwu's citation of it.

**Comparisons**, run only after the datasets were frozen (`comparison-results.json`):

4. **INV-0005's blind model transcriptions** of the order and the palace table match D-1 and D-2 in every name, line, trigram, palace membership and slot. The only difference is the order in which palaces are presented (§3, A4).
5. **Ledger claims on cited data.** The source-dependent statements of C-0002, C-0003, C-0004, C-0006, C-0009, C-0017(b) and C-0018 hold on the cited data.
   - D generates all 64 Jingshi palace entries (C-0017(b)).
   - The generation mnemonic of C-0018 reproduces the Jingshi generation of all 64 hexagrams and the world line the text states for each.
   - This is a same-family, context-exposed recomputation: it removes the "no cited source" gap but verifies nothing.
6. **Procedure source.** Zhu Xi's 筮儀 does more than describe the ritual:
   - It counts the cases of each change: the first change gives 奇 to 偶 as three to one (奇者三而偶者一), and the second and third give two to two (奇偶各得四之二).
   - Weighting these counted cases equally reproduces exactly the line law of the yarrow-standard model in DEF-017 (1/16, 5/16, 7/16, 3/16).
   - The same text attests remainders of one to four and a stalk hung from the right heap. It does not specify how the stalks are split; 明筮 says only 信手平分. This partly answers Q-011.

**Not achieved:**
- No earliest attestation of the generation mnemonic was found (Q-008).
- No accessible transcription of the Mawangdui order was found (D-3).
- No witness was checked against a printed edition.

## 2. Exact results

All results here are source-dependent. "Witness" means a specific Wikisource page revision, cited in `sources/manifest.json`. Facts about a witness are facts about that digital transcription.

### S1. Received order from two witnesses (D-1)

**Witnesses.**
- W1 is the 64 pages `周易/<name>`, revisions dated 2022-02-16 to 2026-09-27. The base edition is not stated on the pages, and the index page carries a 50% text-quality tag.
- W2 is `周易正義` (index revision 1645137) with its 64 chapter pages, attributed to Wang Bi and Han Kangbo (commentary) and Kong Yingda (subcommentary). The base edition is not stated beyond the Siku catalogue notice ("此本十卷").

**Procedure.** `compute/experiments/INV-0008/build_baselines.py` derives each field as follows:

| Field | W1 source | W2 source |
|---|---|---|
| Number | the page statement "第N卦" | position in the index list |
| Order | the previous/next links chain 1→64 identically, once 恆 in the links is identified with the page title 恒 | the index list order |
| Lines | the headings of the blue-styled line statements | paragraph-initial headings, excluding [疏] paragraphs and notes |
| Composition | the annotation "X下Y上" | the annotation "X下Y上" |

Each heading gives one line: 九 is yang (1), 六 is yin (0), and the six positions must run 初, 二, 三, 四, 五, 上 in that order.

**Results.**
- W1 numbers are exactly 1–64.
- W2's order equals W1's, with name variant 無妄 for 无妄.
- W2 marks 上經 for its first 30 entries and 下經 from entry 31.
- There are no line disagreements and no composition disagreements.
- All 64 line patterns are distinct.
- The eight doubled chapters (composition X下X上) have equal halves, giving eight distinct trigram patterns, and every one of the 64 compositions agrees with the headings under those patterns.

**Punctuation and markup variants**, absorbed by the parser:
- W1 否 uses "，" after its headings.
- W2 豫 and 剝 use "，".
- W2 乾 wraps its headings in `{{+|…}}`.

### S2. The Xugua attests the order

- **Witnesses:** `易傳/序卦` (revision 2611127) and `周易正義/10` (revision 2384519).
- **Procedure:** hexagram names following 受之以.
  - One witness reads "故受之既濟" without 以; the parser accepts both forms.
  - W2 runs Han Kangbo's commentary into the text, which repeats 未濟 once. Only first mentions count.
- **Result:** in both witnesses, the 61 names introduced this way are exactly received numbers 3–30 then 32–64, in order. The *Xugua* names 乾 and 坤 only as 天地, and opens its lower part without naming 咸. This is an attestation of the order inside the classical commentary tradition, independent of chapter numbering.

### S3. Eight-palace table from two witnesses (D-2)

**Witnesses.**
- J1: `京氏易傳` (revision 7903767). A modern collated text with notes signed 虎易注 that cite a "廣西版《易占解讀》"; its base edition is not stated.
- J2: `京氏易傳 (四庫全書本)`, 卷上 (revision 1562382) and 卷中 (revision 657265). An unproofread Siku Quanshu transcription with Lu Ji's notes.

**Procedure.**
- J1 entries are its section headings: glyph, composition (X下Y上, or X上X下 for doubled trigrams) and name.
- J2 entries are `{{SKchar}}{{SK notes|X下Y上}}` followed by the name.
- The world line is taken from J1's entry text by an ordered pattern list with one manual reading (乾: "壬戌在世，居宗廟", a note). Each phrase is then searched for in J2.

**Results.**
- J1 and J2 have 64 entries each, agreeing in sequence, composition and name. Name variants:
  - J2 writes 遯 for J1's 遁, 恒 for 恆, 剥 for 剝, 无妄 for 無妄, 頥 for 頤, 䝉 for 蒙, and 兊 for 兌.
  - **J2's 履 entry begins 天下有澤曰履**, with no leading name; it is identified by composition.
- Every name agrees with D-1 by composition.
- The eight blocks of eight begin with doubled trigrams, in order 乾 震 坎 艮 坤 巽 離 兌.
- The entries cover all 64 hexagrams.
- World line by position is (6, 1, 2, 3, 4, 5, 4, 3) in all eight palaces.
- 57 phrases name 世 explicitly. 7 are indirect: 震 宗廟處上六, 井 九五處至尊, 大過 降諸侯，立元首, 節 元士立元首, 噬嗑 六五居尊, 旅 其居初六元士, 渙 九五居尊.

**World-line phrase variants between the witnesses:**
- 觀: 諸侯臨世 / 諸候臨世.
- 解: 立大夫于世 / 立大夫於世.
- 咸: J1 九三三宮居世 / J2 九三三公居世. J1's 宮 looks like a transcription slip.
- 乾: the phrase appears in J2 only as a note.
- Both witnesses read 蒙 as 諸位立世. J1's editor emends 諸位 to 諸侯, and the line-4 reading relies on that emendation, or equally on the following 元士為應.

**The text explains its palace order.** At the 坤 palace's returning-soul entry (比), J1 reads "坤生三女巽離兌，分長中下". A note in the first palace reads "乾生三男，坤生三女" (J1 line 296; it is a note, not main text).

### S4. Secondary editorial table

The Wikisource `周易` index page (revision 7907208) carries an unsourced modern table, 分宮卦象次序表. Its eight palaces have the same members in the same within-palace sequence as J1. It presents the palaces in the order 乾 坎 艮 震 巽 離 坤 兌 rather than the text's order. It is not used as a source.

### S5. Procedure texts (D-7) and what they specify

**The Xici witnesses differ in arrangement.**
- `易傳/繫辭上` places the sentence on the sum of the numbers of heaven and earth (天數…地數…此所以成變化而行鬼神也) before 大衍之數五十.
- The *Zhengyi* classic-text segments (`{{yw}}` on `周易正義/07.08`) place 天數五，地數五… after 故再扐而後掛.
- Both continue through 十有八變而成卦 to 天下之能事畢矣.
- The procedural core (49 stalks used; divide into two; hang one; count by fours; return the remainder) reads the same in both.

**Zhu Xi's 筮儀** (`原本周易本義 (四庫全書本)/卷末下`, revision 527383):

| Feature | Text |
|---|---|
| Split | the 49 stalks are split by hand: "中分". The Siku transcription reads "中分四中九䇿", where "四十九" is expected; it is not corrected here. |
| Hung stalk | one stalk is taken from the right heap and hung: "取右大刻之䇿掛於左手之小指間" |
| Remainder | the remainder is "或一或二或三或四", that is, one to four, never zero |
| First change | the left and right remainders pair as 1–3, 2–2, 3–1 and 4–4, so with the hung stalk the total is 5 or 9: "奇者三而偶者一也" |
| Second and third changes | 1–2, 2–1, 3–4 and 4–3 give 4 or 8: "奇偶各得四之二焉" |
| Totals | 13, 17, 21 and 25 stalks give 老陽 (重), 少陰 (拆), 少陽 (單) and 老陰 (交) |

**Zhu Xi's 明筮** (`卷末上`) describes the split as "信手平分". It gives the same 5-or-9 and 4-or-8 totals.

**Consequence (exact; `comparison-results.json`, key `zhu_xi_equal_case_law`).** Weight the counted cases equally: first change 奇 with probability 3/4, later changes 奇 with probability 1/2, changes independent. Then:

| Line value | Cases | Probability |
|---|---|---|
| 老陽, 9 | three 奇 | 3/4 · 1/2 · 1/2 = 3/16 |
| 老陰, 6 | three 偶 | 1/4 · 1/2 · 1/2 = 1/16 |
| 少陰, 8 | two 奇 and one 偶 | 3/16 + 3/16 + 1/16 = 7/16 |
| 少陽, 7 | one 奇 and two 偶 | 3/16 + 1/16 + 1/16 = 5/16 |

This is the yarrow-standard model of DEF-017. The text counts cases; it does not assert that they are equally likely. Under the uniform-split model of C-0033 they are not. The remainder convention (one to four) and the right-heap hung stalk are those DEF-017 assumes for its yarrow-uniform and yarrow-binomial models. No text consulted specifies a split distribution.

**Coin method** (`儀禮註疏/卷一`, revision 2675798).
- Jia Gongyan's subcommentary says divination "now" uses coins.
- Three 少 is 重錢, i.e. 9; three 多 is 交錢, i.e. 6; two 多 and one 少 is 單錢, i.e. 7; two 少 and one 多 is 拆錢, i.e. 8.
- Gu Yanwu (`日知錄/卷15`, revision 2630492) quotes it with the gloss that 多 and 少 refer to remainder counts, and the convention 無字謂之陽，有字謂之陰.
- The names 重/交/單/拆 coincide with Zhu Xi's names for the four yarrow outcomes.
- Neither text states the number of coins tossed or a probability. The three-fair-coin model of DEF-017 is an idealization they do not fix.

### S6. Generation mnemonic (D-4): attestation not found

- Wikisource full-text search for 天同二世 returned no hits.
- Web searches found modern teaching pages. One, [shengxiao.net](https://www.shengxiao.net/zhouyi/liuyao/2042.html), attributes the verse and a companion verse (認宮訣) to a 《筮學指要》. I found no author, date or edition for that title.
- This is a lead, not an attestation. Q-008 stays open.
- The table the mnemonic summarizes is now attested independently. The Jingshi text states each hexagram's world line, and these agree with the mnemonic for all 64 (§3, B7). This says nothing about when the verse arose.

## 3. Comparisons after freezing (`comparison-results.json`)

The datasets, snapshots and build scripts were hashed into `FROZEN.sha256` before `compare_prior.py` was first run.

**A. Earlier transcriptions.**
- **A1.** INV-0005 phase 1, `received_order.tsv` (GPT-5.6 Sol, isolated, from memory) against D-1: 0 differences across 64 rows in name, lower trigram, upper trigram and six-line word.
- **A2.** INV-0005 phase 1, `eight_palaces_source.tsv` against D-2: 0 differences across 64 palace-slot assignments.
- **A3.** INV-0001 left no transcription in the repository, so nothing could be compared.
- **A4.** The palace presentation orders differ:
  - INV-0005 and the Wikisource editorial table use 乾 坎 艮 震 巽 離 坤 兌.
  - Both Jingshi witnesses use 乾 震 坎 艮 坤 巽 離 兌.
  - Membership and within-palace order are unaffected, and no registered claim depends on presentation order.

**B. Source-dependent ledger statements recomputed on D-1 and D-2.** Definitions are implemented from `ledger/definitions.md`.

| Claim | Result on cited data |
|---|---|
| C-0002 | All 32 pairs (2k−1, 2k) are σ-orbits: 28 reversal pairs and 4 complement pairs. The palindromes are 1, 2, 27, 28, 29, 30, 61, 62. |
| C-0003 | 18 R-figures in 1–30 and 18 in 31–64. |
| C-0004 | The palindrome pairs in the upper canon are pairs 1, 14 and 15 (hexagrams 1/2, 27/28, 29/30), so p = 3. |
| C-0006 | The doubled hexagrams 1, 2, 29, 30 are in the upper canon with palindromic trigrams. 51, 52, 57, 58 are in the lower canon with non-palindromic trigrams. |
| C-0009 | A = {1, 2, 63, 64}. |
| C-0017(b) | For each palace head b and slot label ℓ, b ⊕ d_ℓ (DEF-011) equals the Jingshi entry in all 64 cases. |
| C-0018 | Applying the mnemonic to φ(x) gives the Jingshi generation for all 64. Its world line equals the line the text states for all 64; 7 of those textual lines are read from indirect wording. |

**What these comparisons do and do not establish.**
- They establish that each statement holds on a cited, unchecked transcription.
- They do not verify mathematics. The checks are definitional once the data are fixed, and were run by the originator's model family with full context.
- They do not establish historical correspondence beyond these witnesses, and do not settle C-0017(a), the claim that D encodes the Jing Fang procedure as a procedure.
- The Jingshi text does narrate the procedure (e.g. 降入遯, 反為遊魂, 復歸本位為大有). Checking DEF-011 against that narration, entry by entry, was not done.

## 4. Failed attempts and access limits

| ID | Attempt | Outcome | Scope |
|---|---|---|---|
| F1 | ctext.org API (`gettext`) | `ERR_REQUIRES_AUTHENTICATION` | ctext not used. Scraping its HTML was avoided. |
| F2 | Mnemonic attestation: Wikisource full-text search, 3 web searches, 2 page fetches | Modern pages only; one unverified title lead | Not ruled out: attestation in Qing or Republican divination manuals not digitized on Wikisource. |
| F3 | Mawangdui silk manuscript order (D-3) on Wikisource | No transcription found; only the *Laozi* silk texts | Needs a published transcription, e.g. a volume of the Mawangdui excavation reports. Secondhand descriptions were not used. |
| F4 | Shanghai Museum Chu manuscript (D-6) | Not searched beyond the D-3 query | Needs the published Shanghai Museum volumes. |

## 5. Dependencies and evidence lineage

- **Shared inputs.** Both witnesses of each text are Wikisource transcriptions by volunteers. Their independence is plausible (different editions, different pages and markup conventions, different variants) but not established; one may have been copied from a digital source the other also used. Agreement is evidence against random transcription error, not against a shared upstream error.
- **Trigram patterns.** These come from the source itself (the doubled chapters of W1), not from an outside convention. D-2's six-line words are derived through D-1 (name and composition), not read from the Jingshi glyphs.
- **Variant map.** Normalization relies on the explicit seven-entry map in `build_baselines.py`. Any unknown name would have stopped the build.
- **Generation labels in D-2.** These are assigned by position (pure, first to fifth, wandering, returning). The text supports them with the world line it states and with 遊魂 and 歸魂 language, but does not label every entry with its generation name.
- **INV-0005.** Its phase 1 was saved and hash-frozen before this investigation read it. Its phase-2 package was already assembled and frozen. Nothing from this investigation was supplied to INV-0005 or INV-0006.

## 6. Alternative explanations and calibration

- **Expected agreement.** That a classical text and its subcommentary edition agree on order and lines is expected. The value here is citation and machine-checkability, not surprise.
- **C-0017(b) and C-0018.** The agreement is unsurprising if the palace table and the mnemonic were constructed from the same procedure. It confirms that INV-0001's encoding reproduces the table as transmitted in these witnesses; it is not independent evidence for the procedure's origin.
- **Zhu Xi's case counts.** They match yarrow-standard because both describe the same counting. Whether practitioners' splits make the counted cases equally likely is an empirical question the texts do not address (Q-011).
- **Novelty.** Not claimed for any result. The palace table, the *Xugua* order and the 1/16, 5/16, 7/16, 3/16 derivation are well known in the tradition and in secondary literature. The contribution is a reproducible, cited dataset for this programme.

## 7. Reproducibility

```bash
# 1. Snapshot (network; writes a new directory; already done for the frozen set)
python3 -I compute/experiments/INV-0008/fetch_sources.py --outdir /tmp/inv0008-snap
# 2. Build datasets from the frozen snapshot (no network)
python3 -I compute/experiments/INV-0008/build_baselines.py \
  --sources investigations/INV-0008-cited-source-baselines/sources \
  --order-csv /tmp/order.csv --palace-csv /tmp/palaces.csv \
  --procedure-csv /tmp/procedure.csv --out /tmp/build.json
# 3. Post-freeze comparisons
python3 -I compute/experiments/INV-0008/compare_prior.py \
  --order data/zhouyi-received-order.v1.csv --palaces data/jingshi-yizhuan-eight-palaces.v1.csv \
  --inv5-order investigations/INV-0005-verify-pairing-and-palaces/phase1/data/received_order.tsv \
  --inv5-palaces investigations/INV-0005-verify-pairing-and-palaces/phase1/data/eight_palaces_source.tsv \
  --out /tmp/compare.json
```

- Step 2 reproduces the frozen CSVs byte for byte from the frozen snapshot. It asserts every snapshot file's SHA-256 against the manifest.
- A fresh step 1 fetches current revisions, which may differ; use the permanent `oldid` URLs in the manifest to retrieve the frozen ones.
- **Execution.** All three scripts were executed. The build was revised several times against the frozen snapshot before the final run; the fixes concerned heading punctuation, a `{{+|}}` wrapper, a link spelling of 恆, a missing 以, and repeated commentary mentions. Every revision is recorded in this section and visible in the code comments. No dataset value was edited by hand.
- **Manual reading.** One world-line reading (乾) is a manual quote, asserted to occur verbatim in its entry.

## 8. Opportunities

1. **Check against a printed edition.** A human compares D-1 and D-2 with a cited printed edition (for example a Zhonghua shuju *Zhouyi zhengyi* and a punctuated *Jingshi Yizhuan*), logging differences in the sidecars. This promotes the checking status. It is the cheapest decisive step.
2. **C-0017(a) against the narrated procedure.** The Jingshi entries narrate each step (降入…, 反為遊魂, 復歸本位). A targeted verifier can check DEF-011 against that narration from J2 alone.
3. **Najia and feifu (DIR-008).** The same Jingshi witnesses carry stem-branch assignments and 飛伏 pairs for every entry, as notes such as 壬戌土，癸酉金. They are a ready source for a cited najia dataset.
4. **Guaqi (DIR-008).** Yixing's 卦議 is in `新唐書/卷027上` on Wikisource: a cited entry point for the Han guaqi correlations.
5. **Shao Yong arrangements (D-5).** `皇極經世` and `易學啟蒙通釋/圖` are on Wikisource. They are textual descriptions of the diagrams, not the diagrams; the arrangement must be reconstructed with care.
6. **Textual layer (ASN-0009).** W2, the *Zhengyi* classic text marked `{{yw}}`, and W1's line statements give a two-witness edition of the judgments and line statements.
7. **Q-011.** The texts fix the remainder and hung-stalk conventions. The split law is the remaining unknown, and needs an experiment or a source that describes splitting.

**Promising approach not attempted:** collate the 京氏易傳 四部叢刊本 scans (Wikisource hosts only image stubs) as a third Jingshi witness.

## 9. Recommended next assignments (proposals only)

| Question | Minimum inputs | Cheapest decisive check | Outcomes | Stop when |
|---|---|---|---|---|
| Do D-1 and D-2 survive a printed edition? | the two CSVs and one printed edition | human row-by-row check | Agreement upgrades checking status. A difference becomes a v2 dataset with a changelog entry. | all 64 rows checked |
| Does DEF-011 match the narrated Jingshi procedure, C-0017(a)? | J2 text, DEF-011 | extract each entry's transition phrase | Match supports (a). A mismatch scopes C-0017. | 64 transitions read |
| Where is the generation mnemonic first attested (Q-008)? | access to Ming and Qing divination manuals (e.g. a ctext key, Kanseki Repository) | full-text search for 天同二世 | A dated attestation, or a documented negative | three full-text corpora searched |

## 10. Registry

| Local ID | Claim | Evidence | Status | Domain / contingency | Prior claims | Next action |
|---|---|---|---|---|---|---|
| S1 | D-1 from two witnesses, which agree on order, names, all 384 headings and 64 compositions | executed parse of frozen snapshots | reported | source-dependent / contingent | C-0002, C-0003, C-0006, C-0009 (inputs) | printed-edition check |
| S2 | The Xugua's 61 introduced names follow received positions 3–30 and 32–64, in two witnesses | executed parse | reported | source-dependent / contingent | C-0002 | none |
| S3 | D-2 from two Jingshi witnesses, which agree on 64 entries; stated world lines follow (6, 1, 2, 3, 4, 5, 4, 3) by position in all 8 palaces | executed parse plus one manual reading | reported | source-dependent / contingent | C-0017, C-0018 | printed-edition check |
| S5 | Zhu Xi's 筮儀 counts cases 3:1 then 2:2. Equal weighting gives exactly 1/16, 5/16, 7/16, 3/16. It attests remainders of 1–4 and a right-heap hung stalk, but no split law. | text plus exact arithmetic | reported | source-dependent / contingent | C-0032, C-0033, DEF-017, Q-011 | Q-011 experiment or source |
| S6 | No attestation found for the generation mnemonic | bounded search | inconclusive | historical | C-0018, Q-008 | full-text corpora |
| B | C-0002, C-0003, C-0004, C-0006, C-0009, C-0017(b), C-0018 hold on cited data; INV-0005's transcriptions match | executed post-freeze comparison | reported (recomputation) | source-dependent | listed | verification-log notes only |
