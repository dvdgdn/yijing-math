# zhouyi-received-order.v1.csv

The order of the 64 hexagrams in the transmitted *Zhouyi*, with names, canon, trigram composition and the six lines of each hexagram.

| Field | Content |
|---|---|
| Source | SRC-001. Two digital witnesses on zh.wikisource.org, retrieved 2026-11-01 at fixed revisions (permanent URLs and SHA-256 in `investigations/INV-0008-cited-source-baselines/sources/manifest.json`). **W1**: the 64 chapter pages `周易/<name>`; base edition not stated on the pages. **W2**: `周易正義` (index revision 1645137) and its chapter pages, Wang Bi and Han Kangbo commentary with Kong Yingda's subcommentary; base edition not stated beyond a ten-*juan* arrangement. |
| Transcriber | Claude Opus 5.5, INV-0008, by script (`compute/experiments/INV-0008/build_baselines.py`) from the frozen snapshots; no value entered by hand. |
| Date | 2026-11-01 |
| Checking status | `unchecked`. Not compared with a printed edition. The two digital witnesses were compared mechanically: order, names (one variant, below), all line headings and all trigram compositions agree. Their independence as transcriptions is plausible but not established. |
| Conventions | `number`: W1's statement "第N卦", equal to W2's list position. `name`: W1 page title (traditional characters). `name_zhengyi`: W2 spelling. `canon`: W2's 上經/下經 headings. `lower_trigram`, `upper_trigram`: the annotation "X下Y上" in W1 (identical in W2). `lines_bottom_to_top`: read from the classic's line-statement headings, 初 (line 1) to 上 (line 6); `1` = 九 (yang), `0` = 六 (yin). `line_headings`: the headings as they appear. |
| Known variants | 无妄 (W1) / 無妄 (W2). W1 navigation links write 恆 where the page title is 恒. W1 否, W2 豫 and W2 剝 punctuate headings with "，" rather than "："; W2 乾 wraps headings in a template. The *Xugua* (SRC-001 commentary layer), in `易傳/序卦` and `周易正義/10`, introduces hexagram names in an order that can be compared with this table; `易傳/序卦` reads "故受之既濟" without 以. |
| Changelog | v1 (2026-11-01): first version. |
