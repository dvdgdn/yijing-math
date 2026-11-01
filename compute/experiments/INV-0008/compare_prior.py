#!/usr/bin/env python3
"""Post-freeze comparisons for INV-0008.

Run only after the v1 datasets are frozen. Compares the cited datasets with
(a) the blind model transcriptions saved by INV-0005 phase 1 and (b) the
source-dependent statements of ledger claims that are mechanically checkable
on the order and palace tables. Definitions are implemented from
ledger/definitions.md (DEF-001 to DEF-014). This is a context-exposed
recomputation, not a verification under the protocol.

Standard library only:
    python3 -I compare_prior.py --order F --palaces F --inv5-order F --inv5-palaces F --out F
"""
import argparse
import csv
import hashlib
import json
import sys

PINYIN = {"Qian": "乾", "Kun": "坤", "Zhen": "震", "Xun": "巽", "Kan": "坎", "Li": "離", "Gen": "艮", "Dui": "兌"}
VARIANTS = {"兊": "兌", "無妄": "无妄", "恆": "恒", "遁": "遯", "剥": "剝", "頥": "頤", "䝉": "蒙"}
D = {"pure": "000000", "1st": "100000", "2nd": "110000", "3rd": "111000", "4th": "111100",
     "5th": "111110", "wandering": "111010", "returning": "000010"}           # DEF-011
POSITION_LABEL = ["pure", "1st", "2nd", "3rd", "4th", "5th", "wandering", "returning"]
MNEMONIC = {(): "pure", ("earth",): "1st", ("earth", "man"): "2nd", ("earth", "man", "heaven"): "3rd",
            ("man", "heaven"): "4th", ("heaven",): "5th", ("earth", "heaven"): "wandering",
            ("man",): "returning"}                                         # C-0018 table
WORLD_LINE = {"pure": 6, "1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "wandering": 4, "returning": 3}


def norm(n):
    for a, b in VARIANTS.items():
        n = n.replace(a, b)
    return n


def xor(a, b):
    return "".join("1" if p != q else "0" for p, q in zip(a, b))


R = lambda x: x[::-1]                                                      # DEF-002
C = lambda x: xor(x, "111111")                                             # DEF-003
sigma = lambda x: R(x) if R(x) != x else C(x)                              # DEF-006


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    for k in ["--order", "--palaces", "--inv5-order", "--inv5-palaces", "--out"]:
        ap.add_argument(k, required=True)
    a = ap.parse_args()
    res = {"python": sys.version.split()[0], "script_sha256": sha(__file__),
           "inputs": {k: {"path": getattr(a, k.replace("-", "_")), "sha256": sha(getattr(a, k.replace("-", "_")))}
                      for k in ["order", "palaces", "inv5_order", "inv5_palaces"]}}
    order = list(csv.DictReader(open(a.order, encoding="utf-8")))
    pal = list(csv.DictReader(open(a.palaces, encoding="utf-8")))
    word = {int(r["number"]): r["lines_bottom_to_top"] for r in order}
    num_of = {w: n for n, w in word.items()}
    name = {int(r["number"]): r["name"] for r in order}

    # ---- (a) blind model transcriptions from INV-0005 phase 1 ----
    t5 = list(csv.DictReader(open(a.inv5_order, encoding="utf-8"), delimiter="\t"))
    diffs = []
    for r in t5:
        n = int(r["number"])
        got = {"name": norm(r["name_zh"]), "lower": PINYIN[r["lower_trigram"]], "upper": PINYIN[r["upper_trigram"]],
               "word": r["word_bottom_to_top"]}
        ref = next(x for x in order if int(x["number"]) == n)
        want = {"name": ref["name"], "lower": ref["lower_trigram"], "upper": ref["upper_trigram"],
                "word": ref["lines_bottom_to_top"]}
        for k in got:
            if got[k] != want[k]:
                diffs.append({"number": n, "field": k, "inv5": got[k], "cited": want[k]})
    res["inv5_order"] = {"rows": len(t5), "differences": diffs}
    p5 = list(csv.DictReader(open(a.inv5_palaces, encoding="utf-8"), delimiter="\t"))
    cited = {(r["palace"], int(r["position"])): int(r["received_number"]) for r in pal}
    pd = []
    for r in p5:
        key = (r["palace_zh"].replace("兊", "兌"), int(r["slot_order"]))
        if cited.get(key) != int(r["hex_number"]):
            pd.append({"palace": key[0], "slot": key[1], "inv5": int(r["hex_number"]), "cited": cited.get(key)})
    res["inv5_palaces"] = {"rows": len(p5), "differences": pd,
                           "palace_order_inv5": list(dict.fromkeys(r["palace_zh"] for r in p5)),
                           "palace_order_cited": list(dict.fromkeys(r["palace"] for r in pal))}

    # ---- (b) source-dependent claims recomputed on the cited tables ----
    b = {}
    pairs = [(word[2 * k - 1], word[2 * k]) for k in range(1, 33)]
    b["C-0002"] = {"all_pairs_are_sigma_orbits": all(sigma(x) == y for x, y in pairs),
                   "reversal_pairs": sum(R(x) == y and R(x) != x for x, y in pairs),
                   "complement_pairs": sum(R(x) == x and C(x) == y for x, y in pairs),
                   "palindromes": sorted(n for n, w in word.items() if R(w) == w)}
    fig = lambda ns: len({min(word[n], R(word[n])) for n in ns})
    b["C-0003"] = {"figures_upper_1_30": fig(range(1, 31)), "figures_lower_31_64": fig(range(31, 65))}
    b["C-0004"] = {"palindrome_pairs_in_upper": [k for k in range(1, 16) if R(word[2 * k - 1]) == word[2 * k - 1]]}
    doubled = sorted(n for n, w in word.items() if w[:3] == w[3:])
    b["C-0006"] = {"doubled": doubled,
                   "upper_doubled": [n for n in doubled if n <= 30],
                   "upper_doubled_trigram_palindromic": all(word[n][:3] == word[n][:3][::-1] for n in doubled if n <= 30),
                   "lower_doubled_trigram_nonpalindromic": all(word[n][:3] != word[n][:3][::-1] for n in doubled if n > 30)}
    A = ["000000", "111111", "101010", "010101"]                           # DEF-014
    b["C-0009"] = {"A_numbers": sorted(num_of[w] for w in A)}
    # C-0017(b): palaces generated by D from each doubled head, against the cited table.
    mism = []
    for r in pal:
        head = next(int(x["received_number"]) for x in pal if x["palace"] == r["palace"] and x["position"] == "0")
        lab = POSITION_LABEL[int(r["position"])]
        predicted = num_of[xor(word[head], D[lab])]
        if predicted != int(r["received_number"]):
            mism.append({"palace": r["palace"], "position": int(r["position"]), "cited": int(r["received_number"]),
                         "from_D": predicted})
    b["C-0017b"] = {"rows": len(pal), "mismatches": mism}
    # C-0018: mnemonic table applied to phi(x), against cited generation and stated world line.
    mm, wl = [], []
    for r in pal:
        w = word[int(r["received_number"])]
        phi = xor(w[:3], w[3:])                                            # DEF-010
        diff = tuple(p for p, bit in zip(("earth", "man", "heaven"), phi) if bit == "1")
        gen = MNEMONIC[diff]
        if gen != POSITION_LABEL[int(r["position"])]:
            mm.append({"number": int(r["received_number"]), "mnemonic": gen, "cited_position": r["generation"]})
        if WORLD_LINE[gen] != int(r["shi_line"]):
            wl.append({"number": int(r["received_number"]), "mnemonic_line": WORLD_LINE[gen], "text_line": int(r["shi_line"])})
    b["C-0018"] = {"generation_mismatches": mm, "world_line_mismatches": wl,
                   "rows_with_indirect_world_line": sum(r["shi_basis"] == "indirect" for r in pal)}
    res["claims_on_cited_data"] = b
    # Zhu Xi's case counts (筮儀): first change odd:even = 3:1, later changes 2:2.
    from fractions import Fraction as F
    from itertools import product
    law = {6: F(0), 7: F(0), 8: F(0), 9: F(0)}
    probs = [{"odd": F(3, 4), "even": F(1, 4)}, {"odd": F(1, 2), "even": F(1, 2)}, {"odd": F(1, 2), "even": F(1, 2)}]
    for seq in product(["odd", "even"], repeat=3):
        p = probs[0][seq[0]] * probs[1][seq[1]] * probs[2][seq[2]]
        odd = seq.count("odd")
        law[{3: 9, 0: 6, 2: 8, 1: 7}[odd]] += p
    res["zhu_xi_equal_case_law"] = {k: str(v) for k, v in law.items()}
    assert law == {6: F(1, 16), 7: F(5, 16), 8: F(7, 16), 9: F(3, 16)}
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(json.dumps({"inv5_order_differences": len(diffs), "inv5_palace_differences": len(pd),
                      "palace_orders": [res["inv5_palaces"]["palace_order_inv5"], res["inv5_palaces"]["palace_order_cited"]],
                      **b}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
