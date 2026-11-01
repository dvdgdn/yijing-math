# jingshi-yizhuan-eight-palaces.v1.csv

The eight palaces of 8 hexagrams each, in the sequence of the *Jingshi Yizhuan* 京氏易傳, with the line the text names as holding the world (世).

| Field | Content |
|---|---|
| Source | SRC-002. Two digital witnesses on zh.wikisource.org, retrieved 2026-11-01 at fixed revisions (see `investigations/INV-0008-cited-source-baselines/sources/manifest.json`). **J1**: `京氏易傳`, revision 7903767, a modern collated text with editor's notes signed 虎易注 citing a 廣西版《易占解讀》; base edition not stated. **J2**: `京氏易傳 (四庫全書本)`, 卷上 revision 1562382 and 卷中 revision 657265, a Siku Quanshu transcription with Lu Ji's notes, not marked as proofread. |
| Transcriber | Claude Opus 5.5, INV-0008, by script (`compute/experiments/INV-0008/build_baselines.py`). One world-line reading (乾) is a quoted manual reading asserted in the script. |
| Date | 2026-11-01 |
| Checking status | `unchecked`. Not compared with a printed edition. J1 and J2 agree on all 64 entries in sequence, name (after the variant mapping below) and trigram composition. |
| Conventions | `palace_order`: 1–8 in the text's sequence. `palace`: trigram of the block's first (doubled) entry. `position`: 0–7 within the block. `generation`: assigned by position as 本宮, 一世…五世, 遊魂, 歸魂; the text does not label every entry with this name. `name_collated` and `name_siku`: as written in J1 and J2 (empty where J2's entry opens without a name). `received_number`: the number of the same hexagram in `zhouyi-received-order.v1.csv`, matched by name and confirmed by composition. `lower_trigram`, `upper_trigram`: J1's composition, normalized to lower/upper; J1 writes doubled trigrams as X上X下. `lines_bottom_to_top`: derived from the composition using the trigram line patterns of the eight doubled hexagrams in `zhouyi-received-order.v1.csv`; not read from the glyphs. `shi_line`: 1–6, the line the entry names as holding 世, read from `shi_phrase`. `shi_basis`: `explicit` when the phrase contains 世; `indirect` when it names the line that 居尊/處至尊/立元首 or similar. |
| Known variants | Names: J1 遁, 恆, 剝, 無妄, 頤, 蒙, 兌; J2 遯, 恒, 剥, 无妄, 頥, 䝉, 兊. J2's 履 entry begins 天下有澤曰履 with no leading name. World-line phrases: 觀 諸侯臨世 (J1) / 諸候臨世 (J2); 解 立大夫于世 / 立大夫於世; 咸 九三三宮居世 (J1) / 九三三公居世 (J2); 乾's phrase occurs in J2 only as a note. Both read 蒙 諸位立世; J1's editor emends to 諸侯. Palace sequence: both witnesses 乾 震 坎 艮 坤 巽 離 兌; an unsourced modern table on the Wikisource `周易` index page (revision 7907208), and some other modern tables, present the palaces as 乾 坎 艮 震 巽 離 坤 兌. |
| Changelog | v1 (2026-11-01): first version. |
