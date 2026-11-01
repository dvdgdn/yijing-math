#!/usr/bin/env python3
"""Build cited working transcriptions from frozen Wikisource snapshots (INV-0008).

Reads <sources>/manifest.json and the snapshot files it lists. Never fetches.
Every value in the datasets is parsed from the snapshots; the hexagram order
is read from the snapshots, never from a list typed into this script.

Outputs:
  --order-csv     received order (D-1)
  --palace-csv    Jingshi Yizhuan eight-palace table (D-2)
  --procedure-csv procedure source excerpts (D-7)
  --out           JSON with every parse, witness comparison and anomaly

Standard library only:
    python3 -I build_baselines.py --sources DIR --order-csv F --palace-csv F \
        --procedure-csv F --out F
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys

TRIGRAMS = "乾坤震巽坎離艮兌"
# Character variants met in the witnesses, mapped to the forms used in the
# Wikisource Zhouyi chapter titles (witness W1). Applied only to names.
VARIANTS = {"兊": "兌", "無妄": "无妄", "恆": "恒", "遁": "遯", "剥": "剝", "頥": "頤", "䝉": "蒙"}
POS = {"初": 1, "二": 2, "三": 3, "四": 4, "五": 5, "上": 6}
HEADING = re.compile(r"(初[九六]|[九六][二三四五]|上[九六])")
NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
GENERATIONS = ["本宮", "一世", "二世", "三世", "四世", "五世", "遊魂", "歸魂"]


def cn_number(s):
    if s == "十":
        return 10
    if "十" in s:
        a, b = s.split("十")
        return (NUM[a] if a else 1) * 10 + (NUM[b] if b else 0)
    return NUM[s]


def unconvert(s):
    """Remove MediaWiki language-conversion markup -{...}- and -{A|...}-."""
    return re.sub(r"-\{(?:[^|{}]*\|)?([^{}]*)\}-", r"\1", s)


def unlink(s):
    return re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", s)


def norm(name):
    for a, b in VARIANTS.items():
        name = name.replace(a, b)
    return name


def heading_lines(found):
    """Map an ordered list of line headings to a bottom-to-top bit string."""
    pos = [POS[h[0]] if h[0] in "初上" else POS[h[1]] for h in found]
    if pos != [1, 2, 3, 4, 5, 6]:
        return None
    return "".join("1" if "九" in h else "0" for h in found)


class Snap:
    def __init__(self, d):
        self.d = d
        self.m = json.load(open(os.path.join(d, "manifest.json"), encoding="utf-8"))
        self.by = {p["title"]: p for p in self.m["pages"]}

    def text(self, title):
        p = self.by[title]
        raw = open(os.path.join(self.d, p["file"]), "rb").read()
        assert hashlib.sha256(raw).hexdigest() == p["sha256"], title
        return unconvert(raw.decode("utf-8"))

    def cite(self, title):
        p = self.by[title]
        return {"title": title, "revid": p["revid"], "url": p["permanent_url"]}

    def group(self, g):
        return [p["title"] for p in self.m["pages"] if p["group"] == g]


def parse_w1(snap, anomalies):
    """Wikisource 周易 chapter pages: number, composition, line headings, links."""
    rows = []
    for t in snap.group("zhouyi_chapters"):
        s = snap.text(t)
        name = t.split("/", 1)[1]
        num = re.findall(r"第([一二三四五六七八九十]+)卦", s)
        comp = re.findall(r"([%s])下([%s])上" % (TRIGRAMS, TRIGRAMS), s)
        # Line statements of the classic: blue-styled list items in the 易經 block.
        block = s.split("彖曰")[0]
        found = [h for line in block.splitlines() if "color:blue" in line
                 for h in re.findall(r">" + HEADING.pattern + r"[：，]", line)]
        lines = heading_lines(found)
        prev_ = re.findall(r"previous\s*=\s*\[\[\.\./([^|\]]+)", s)
        next_ = re.findall(r"next\s*=\s*\[\[\.\./([^|\]]+)", s)
        if len(num) != 1 or not comp or lines is None:
            anomalies.append({"witness": "W1", "page": t, "num": num, "comp": comp, "headings": found})
        rows.append({"name": name, "number": cn_number(num[0]) if num else None,
                     "lower": comp[0][0] if comp else None, "upper": comp[0][1] if comp else None,
                     "headings": found, "lines": lines,
                     # Navigation links spell 恒 as 恆; normalize before chaining.
                     "prev": norm(prev_[0]) if prev_ else None, "next": norm(next_[0]) if next_ else None,
                     "source": snap.cite(t)})
    return rows


def parse_w2(snap, anomalies):
    """Wikisource 周易正義 (王弼注, 孔穎達疏): index order, composition, headings."""
    idx = snap.text("周易正義")
    order = re.findall(r"^\*\[\[/(\d\d)([^|\]]+)\|([上下])經", idx, re.M)
    rows = []
    for k, (juan, name, canon) in enumerate(order, 1):
        t = "周易正義/%s%s" % (juan, name)
        s = snap.text(t)
        comp = re.findall(r"([%s])下([%s])上" % (TRIGRAMS, TRIGRAMS), s)
        body = re.sub(r"\{\{\*\|[^{}]*\}\}", "", s)
        paras = [re.sub(r"^\{\{\+\|", "", p.strip()) for p in body.splitlines()]
        found, seen = [], set()
        for p in paras:
            mm = re.match(HEADING.pattern + r"[：:，]", p)
            if mm and mm.group(1) not in seen:
                seen.add(mm.group(1))
                found.append(mm.group(1))
        lines = heading_lines(found)
        if not comp or lines is None:
            anomalies.append({"witness": "W2", "page": t, "comp": comp, "headings": found})
        rows.append({"index": k, "name": name, "juan": int(juan), "canon": canon,
                     "lower": comp[0][0] if comp else None, "upper": comp[0][1] if comp else None,
                     "headings": found, "lines": lines, "source": snap.cite(t)})
    return rows


def parse_xugua(text, names):
    """Names introduced by 受之以 in the main text of the Xugua."""
    text = unlink(re.sub(r"\{\{\*\|[^{}]*\}\}", "", text))
    keep = [p for p in text.splitlines() if not p.strip().startswith("[疏]")]
    text = "\n".join(keep)
    alts = sorted(set(names) | set(VARIANTS), key=len, reverse=True)
    # One witness reads 故受之既濟 without 以; the other runs Han Kangbo's
    # commentary into the text, so only the first mention of a name counts.
    pat = re.compile(r"受之以?《?(" + "|".join(map(re.escape, alts)) + ")")
    seq, repeats = [], []
    for m in pat.finditer(text):
        n = norm(m.group(1))
        (repeats if n in seq else seq).append(n)
    return seq, repeats


def chain_order(rows):
    by = {r["name"]: r for r in rows}
    starts = [r for r in rows if not r["prev"]]
    if len(starts) != 1:
        return None
    seq, cur = [], starts[0]
    while cur is not None and len(seq) <= len(rows):
        seq.append(cur["name"])
        cur = by.get(cur["next"]) if cur["next"] else None
    return seq


SHI_ROLE = [("元士", 1), ("大夫", 2), ("三公", 3), ("三宮", 3), ("諸侯", 4), ("諸位", 4),
            ("天子", 5), ("至尊", 5), ("宗廟", 6)]
# Patterns stating which line holds 世, tried in order on the entry text with
# punctuation kept. Group 1 is the phrase naming the world line.
SHI_PATTERNS = [
    r"((?:[初上][九六]|[九六][二三四五])?(?:歸魂|游魂|遊魂)?(?:立)?(?:元士|大夫|三公|三宮|諸侯|天子|宗廟|諸位)(?:居|臨|治|在|當|立|為|之)世)",
    r"((?:游魂|遊魂)立世(?:元士|大夫|三公|諸侯|天子|宗廟))",
    r"((?:元士|大夫|三公|諸侯)(?:歸魂|游魂|遊魂)之世)",
    r"(世(?:立|主|上見)(?:元士|大夫|三公|諸侯|天子|宗廟))",
    r"(立(?:元士|大夫|三公|諸侯)于世)",
    r"((?:元士|大夫|三公|諸侯)立[九六初上二三四五]*為世)",
    r"((?:[初上][九六]|[九六][二三四五])(?:立|居)世)",
    r"((?:[初上][九六]|[九六][二三四五])得位為世)",
    r"(陰處至尊為世)",
    r"((?:[初上][九六]|[九六][二三四五])(?:元士|大夫|三公|諸侯)?應世)",
    r"((?:[初上][九六]|[九六][二三四五])(?:處至尊|居尊))",
    r"((?:元士|大夫|三公|諸侯)立元首)",
    r"(降(?:元士|大夫|三公|諸侯)，立元首)",
    r"(其居(?:[初上][九六]|[九六][二三四五])(?:元士|大夫|三公|諸侯))",
    r"(宗廟處上[九六])",
    r"(居世)",
]
# Entries whose statement the patterns do not reach, read by the transcriber.
# Each quote must occur verbatim in that entry; the line follows from it.
SHI_MANUAL = {
    "乾": ("壬戌在世，居宗廟", 6),
}
# Readings of the world-line phrase in the Siku witness where it differs from
# the collated witness. Both strings are asserted to occur in their texts.
SIKU_VARIANTS = {
    "乾": ("壬戌在世，居宗廟", "{{SK notes|壬戌在世居宗廟}}"),
    "觀": ("諸侯臨世", "諸候臨世"),
    "解": ("立大夫于世", "立大夫於世"),
    "咸": ("九三三宮居世", "九三三公居世"),
}


def shi_line(phrase):
    m = re.search(r"([初上])[九六]|[九六]([二三四五])", phrase)
    by_line = POS[m.group(1) or m.group(2)] if m else None
    by_role = None
    for role, v in SHI_ROLE:
        if role in phrase:
            by_role = v
            break
    if phrase == "陰處至尊為世":
        by_role = 5
    if by_line and by_role and by_line != by_role:
        return None
    return by_line or by_role


def parse_jingshi_collated(snap, anomalies):
    s = snap.text("京氏易傳")
    heads = list(re.finditer(r"^===\s*(\S)\s+(\S)([上下])(\S)([上下])\s+(\S+?)\s*===", s, re.M))
    rows = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else s.find("==京氏易傳卷下==")
        body = s[m.end():end]
        a, ad, b, bd = m.group(2), m.group(3), m.group(4), m.group(5)
        lower, upper = (a, b) if ad == "下" else (b, a)
        name = m.group(6)
        main = re.sub(r"\{\{(?:\*|annotate)\|[^{}]*\}\}", "", body)
        phrase, line, how = None, None, None
        if name in SHI_MANUAL:
            phrase, line = SHI_MANUAL[name]
            assert phrase in body, name
            how = "manual"
        else:
            for pat in SHI_PATTERNS:
                mm = re.search(pat, main)
                if mm:
                    phrase, how = mm.group(1), "pattern"
                    line = shi_line(phrase)
                    break
        if line is None:
            anomalies.append({"witness": "J1", "entry": name, "shi_phrase": phrase})
        rows.append({"seq": i, "glyph": m.group(1), "name": name, "lower": lower, "upper": upper,
                     "composition_as_written": a + ad + b + bd, "shi_phrase": phrase,
                     "shi_line": line, "shi_how": how,
                     # explicit: the phrase itself names 世; indirect: it names the line that
                     # 居尊/立元首 etc., and the line is read from that wording.
                     "shi_basis": None if phrase is None else ("explicit" if "世" in phrase else "indirect"),
                     "mentions_youhun": ("游魂" in main or "遊魂" in main),
                     "mentions_guihun": "歸魂" in main})
    return rows, snap.cite("京氏易傳")


def parse_jingshi_siku(snap, names):
    s = "".join(snap.text("京氏易傳 (四庫全書本)/" + v) for v in ["卷上", "卷中"])
    ents = list(re.finditer(r"\{\{SKchar\|\d+\}\}\s*\{\{SK notes\|(\S)([上下])(\S)([上下])\}\}", s))
    alts = sorted(set(names) | set(VARIANTS), key=len, reverse=True)
    rows = []
    for i, m in enumerate(ents):
        end = ents[i + 1].start() if i + 1 < len(ents) else len(s)
        body = s[m.end():end]
        a, ad, b, bd = m.groups()
        a, b = norm(a), norm(b)
        lower, upper = (a, b) if ad == "下" else (b, a)
        lead = re.match("|".join(map(re.escape, alts)), body)
        rows.append({"seq": i, "lower": lower, "upper": upper,
                     "name_raw": lead.group(0) if lead else None,
                     "name": norm(lead.group(0)) if lead else None,
                     "opening": body[:12], "body_plain": re.sub(r"\{\{[^{}]*\}\}", "", body)})
    cites = [snap.cite("京氏易傳 (四庫全書本)/" + v) for v in ["卷上", "卷中"]]
    return rows, cites


def parse_editorial_table(snap, names):
    """Modern editorial palace table on the Wikisource 周易 index page (secondary)."""
    s = snap.text("周易")
    sec = s.split("分宮卦象次序表", 1)[1]
    images = "天澤火雷風水山地"
    alts = sorted(set(names) | set(VARIANTS), key=len, reverse=True)
    rows = []
    for m in re.finditer(r"^!(\S)為(\S)\s*\n\|(.+)$", sec, re.M):
        cells = [c.strip() for c in m.group(3).split("||")]
        members = [m.group(1)]
        for c in cells:
            assert c[0] in images and c[1] in images, c
            rest = c[2:]
            mm = re.fullmatch("|".join(map(re.escape, alts)), rest)
            members.append(norm(mm.group(0)) if mm else None)
        rows.append({"palace": m.group(1), "members": members})
    return rows, snap.cite("周易")


def excerpt(text, start, end):
    """Verbatim span, with wiki markup rendered as plain conventions:
    {{gap}} and line breaks dropped; small-character notes ({{SK notes|..}},
    {{注|..}}) as 〔..〕; Siku glyph images as [SKchar:N]."""
    i = text.index(start)
    j = text.index(end, i) + len(end)
    t = text[i:j]
    t = re.sub(r"\{\{gap\}\}|\n", "", t)
    t = re.sub(r"\{\{SKchar\|(\d+)\}\}", r"[SKchar:\1]", t)
    t = re.sub(r"\{\{(?:SK notes|注)\|([^{}]*)\}\}", r"〔\1〕", t)
    assert "{{" not in t and "[[" not in t, t[:80]
    return t


def main():
    ap = argparse.ArgumentParser()
    for k in ["--sources", "--order-csv", "--palace-csv", "--procedure-csv", "--out"]:
        ap.add_argument(k, required=True)
    a = ap.parse_args()
    snap = Snap(a.sources)
    anomalies = []
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "python": sys.version.split()[0],
           "manifest_sha256": hashlib.sha256(open(os.path.join(a.sources, "manifest.json"), "rb").read()).hexdigest(),
           "variants": VARIANTS}

    # ---- D-1: received order ----
    w1 = parse_w1(snap, anomalies)
    names = [r["name"] for r in w1]
    w1_by_num = sorted(w1, key=lambda r: r["number"] or 0)
    nums = [r["number"] for r in w1_by_num]
    chain = chain_order(w1)
    w2 = parse_w2(snap, anomalies)
    res["w1"] = {"numbers_are_1_to_64": nums == list(range(1, 65)),
                 "chain_equals_number_order": chain == [r["name"] for r in w1_by_num]}
    w2_names = [norm(r["name"]) for r in w2]
    w1_names = [r["name"] for r in w1_by_num]
    res["w2"] = {"count": len(w2), "order_equals_w1": w2_names == w1_names,
                 "name_variants": [(r["name"], norm(r["name"])) for r in w2 if r["name"] != norm(r["name"])],
                 "canon_boundary": [r["index"] for r in w2 if r["canon"] == "下"][:1]}
    by2 = {norm(r["name"]): r for r in w2}
    res["w1_w2_line_disagreements"] = [n for n in w1_names if by2[n]["lines"] != {r["name"]: r for r in w1}[n]["lines"]]
    res["w1_w2_composition_disagreements"] = [
        n for n in w1_names
        if (by2[n]["lower"], by2[n]["upper"]) != next((r["lower"], r["upper"]) for r in w1 if r["name"] == n)]
    # Trigram patterns from the eight doubled chapters of W1 (no outside convention).
    pattern = {}
    for r in w1:
        if r["lower"] == r["upper"] and r["lines"]:
            if r["lines"][:3] != r["lines"][3:]:
                anomalies.append({"witness": "W1", "doubled_but_unequal": r["name"]})
            pattern.setdefault(r["lower"], set()).add(r["lines"][:3])
    res["trigram_patterns"] = {k: sorted(v) for k, v in pattern.items()}
    pat = {k: next(iter(v)) for k, v in pattern.items() if len(v) == 1}
    res["trigram_patterns_complete"] = sorted(pat) == sorted(TRIGRAMS) and len(set(pat.values())) == 8
    res["w1_composition_vs_headings_disagreements"] = [
        r["name"] for r in w1 if pat.get(r["lower"], "?") + pat.get(r["upper"], "?") != r["lines"]]
    res["w1_distinct_line_patterns"] = len(set(r["lines"] for r in w1))
    xugua = {}
    for t in ["易傳/序卦", "周易正義/10"]:
        seq, repeats = parse_xugua(snap.text(t), names)
        expected = [n for k, n in enumerate(w1_names, 1) if k not in (1, 2, 31)]
        xugua[t] = {"source": snap.cite(t), "count": len(seq), "equals_received_without_1_2_31": seq == expected,
                    "sequence": seq, "repeated_mentions_dropped": repeats}
    res["xugua"] = xugua

    with open(a.order_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["number", "name", "name_zhengyi", "canon", "lower_trigram", "upper_trigram",
                    "lines_bottom_to_top", "line_headings"])
        for r in w1_by_num:
            z = by2[r["name"]]
            w.writerow([r["number"], r["name"], z["name"], "上經" if z["canon"] == "上" else "下經",
                        r["lower"], r["upper"], r["lines"], " ".join(r["headings"])])
    res["d1_rows"] = [{k: r[k] for k in ("number", "name", "lower", "upper", "lines", "source")} for r in w1_by_num]

    # ---- D-2: Jingshi Yizhuan palaces ----
    j1, j1_cite = parse_jingshi_collated(snap, anomalies)
    j2, j2_cite = parse_jingshi_siku(snap, names)
    number_of = {r["name"]: r["number"] for r in w1}
    lines_of = {r["name"]: r["lines"] for r in w1}
    comp_of = {(r["lower"], r["upper"]): r["name"] for r in w1}
    res["j1_count"], res["j2_count"] = len(j1), len(j2)
    cmp_rows, palace_rows = [], []
    for k, (x, y) in enumerate(zip(j1, j2)):
        nx = norm(x["name"])
        cmp_rows.append({
            "seq": k, "j1_name": x["name"], "j2_name_raw": y["name_raw"],
            "names_agree": y["name"] is None or nx == y["name"],
            "compositions_agree": (x["lower"], x["upper"]) == (y["lower"], y["upper"]),
            "name_matches_composition_via_d1": comp_of.get((x["lower"], x["upper"])) == nx,
            "j2_opening": y["opening"],
        })
    res["jingshi_witness_comparison"] = cmp_rows
    heads_ok = all(j1[8 * p]["lower"] == j1[8 * p]["upper"] for p in range(8)) and len(j1) == 64
    res["palace_heads_doubled"] = heads_ok
    res["palace_order"] = [j1[8 * p]["lower"] for p in range(8)] if len(j1) == 64 else None
    # Second witness for the world-line phrase: punctuation-free match in J2.
    snap_siku_text = "".join(snap.text("京氏易傳 (四庫全書本)/" + v) for v in ["卷上", "卷中"])
    strip_p = lambda t: re.sub(r"[，。：；、「」『』《》！？\s]", "", t).replace("陰", "隂").replace("遊", "游")
    for k, x in enumerate(j1):
        p, pos = x, k % 8
        y = j2[k] if k < len(j2) else None
        ph = strip_p(x["shi_phrase"] or "")
        found = bool(ph) and y is not None and ph in strip_p(y["body_plain"])
        variant = None
        if x["name"] in SIKU_VARIANTS:
            a_, b_ = SIKU_VARIANTS[x["name"]]
            assert a_ == x["shi_phrase"], x["name"]
            assert b_ in snap_siku_text, x["name"]
            variant = b_
        palace_rows.append({
            "palace_order": k // 8 + 1, "palace": j1[8 * (k // 8)]["lower"], "position": pos,
            "generation": GENERATIONS[pos], "name_collated": x["name"],
            "name_siku": y["name_raw"] if y else None, "name": norm(x["name"]),
            "received_number": number_of.get(norm(x["name"])),
            "lower_trigram": x["lower"], "upper_trigram": x["upper"],
            "lines_bottom_to_top": pat.get(x["lower"], "?") + pat.get(x["upper"], "?"),
            "shi_line": x["shi_line"], "shi_phrase": x["shi_phrase"], "shi_how": x["shi_how"],
            "shi_basis": x["shi_basis"], "shi_phrase_in_siku": found, "siku_variant": variant,
            "mentions_youhun": x["mentions_youhun"], "mentions_guihun": x["mentions_guihun"],
        })
    res["palace_rows"] = palace_rows
    res["palace_lines_match_d1_by_name"] = all(
        r["lines_bottom_to_top"] == lines_of.get(r["name"]) for r in palace_rows)
    res["palace_covers_all_64"] = sorted(r["received_number"] or 0 for r in palace_rows) == list(range(1, 65))
    with open(a.palace_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        cols = ["palace_order", "palace", "position", "generation", "name_collated", "name_siku",
                "received_number", "lower_trigram", "upper_trigram", "lines_bottom_to_top",
                "shi_line", "shi_basis", "shi_phrase"]
        w.writerow(cols)
        for r in palace_rows:
            w.writerow([r[c] if r[c] is not None else "" for c in cols])

    ed, ed_cite = parse_editorial_table(snap, names)
    j1_members = {j1[8 * p]["lower"]: [norm(j1[8 * p + i]["name"]) for i in range(8)] for p in range(8)}
    res["editorial_table"] = {"source": ed_cite, "rows": ed,
                              "disagreements_with_j1": [r["palace"] for r in ed
                                                        if r["members"][1:] != j1_members.get(r["palace"], [])[1:]
                                                        or norm(j1_members.get(r["palace"], [""])[0]) != r["palace"]]}
    res["citations"] = {"W1": "Wikisource 周易 chapter pages (see d1_rows sources)",
                        "W2": snap.cite("周易正義"), "J1": j1_cite, "J2": j2_cite}

    # ---- D-7: procedure excerpts ----
    proc = []
    xici = unlink(snap.text("易傳/繫辭上"))
    proc.append(("SRC-007", "易傳/繫辭上", snap.cite("易傳/繫辭上"),
                 excerpt(xici, "大衍之數五十", "天下之能事畢矣")))
    # Zhengyi marks the classic's own text with {{yw|...}}; join those segments.
    zy = "".join(re.findall(r"\{\{yw\|([^{}]*)\}\}", snap.text("周易正義/07.08")))
    proc.append(("SRC-007", "周易正義/07.08 (經文 segments)", snap.cite("周易正義/07.08"),
                 excerpt(zy, "大衍之數五十", "天下之能事畢矣")))
    shiyi = snap.text("原本周易本義 (四庫全書本)/卷末下")
    proc.append(("SRC-007", "原本周易本義 卷末下 筮儀", snap.cite("原本周易本義 (四庫全書本)/卷末下"),
                 excerpt(shiyi, "擇地", "揖筮者而退}}")))
    mingshi = snap.text("原本周易本義 (四庫全書本)/卷末上")
    proc.append(("SRC-007", "原本周易本義 卷末上 明筮", snap.cite("原本周易本義 (四庫全書本)/卷末上"),
                 excerpt(mingshi, "竒數之元", "數斯可察")))
    yili = snap.text("儀禮註疏/卷一")
    proc.append(("SRC-007", "儀禮註疏 卷一 (賈公彥疏)", snap.cite("儀禮註疏/卷一"),
                 excerpt(yili, "筮法，依七八九六之爻而記之", "拆錢則八也")))
    rzl = snap.text("日知錄/卷15")
    proc.append(("SRC-007", "日知錄 卷15", snap.cite("日知錄/卷15"),
                 excerpt(rzl, "無字謂之陽", "拆錢則八也")))
    with open(a.procedure_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_id", "witness", "revision_url", "text"])
        for sid, wit, c, txt in proc:
            w.writerow([sid, wit, c["url"], txt])
    res["procedure_excerpts"] = [{"witness": wit, "source": c, "chars": len(txt)} for _, wit, c, txt in proc]

    res["anomalies"] = anomalies
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")
    summary = {k: res[k] for k in ["w1", "w2", "w1_w2_line_disagreements", "w1_w2_composition_disagreements",
                                   "trigram_patterns_complete", "w1_composition_vs_headings_disagreements",
                                   "w1_distinct_line_patterns", "j1_count", "j2_count", "palace_heads_doubled",
                                   "palace_order", "palace_lines_match_d1_by_name", "palace_covers_all_64"]}
    summary["xugua"] = {t: (v["count"], v["equals_received_without_1_2_31"]) for t, v in xugua.items()}
    summary["anomalies"] = len(anomalies)
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
