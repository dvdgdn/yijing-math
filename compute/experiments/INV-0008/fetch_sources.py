#!/usr/bin/env python3
"""Snapshot Wikisource pages used as cited source witnesses for INV-0008.

Fetches the current revision of each listed page through the MediaWiki API,
writes each wikitext verbatim to <outdir>/<pageid>.wiki, and records a
manifest with title, page id, revision id, revision timestamp, retrieval time,
SHA-256 and a permanent oldid URL. The output directory must not exist yet.

Standard library only. Usage:
    python3 -I fetch_sources.py --outdir DIR
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://zh.wikisource.org/w/api.php"
UA = "yijing-math-research/0.1 (cited source baseline INV-0008; https://github.com/dvdgdn/yijing-math)"

ZHOUYI_CHAPTERS = (
    "乾 坤 屯 蒙 需 訟 師 比 小畜 履 泰 否 同人 大有 謙 豫 隨 蠱 臨 觀 "
    "噬嗑 賁 剝 復 无妄 大畜 頤 大過 坎 離 咸 恒 遯 大壯 晉 明夷 家人 睽 蹇 解 "
    "損 益 夬 姤 萃 升 困 井 革 鼎 震 艮 漸 歸妹 豐 旅 巽 兌 渙 節 中孚 小過 既濟 未濟"
).split()
# The list above only names the pages to download; the order used in any
# dataset is read from the snapshots themselves, never from this list.

GROUPS = {
    "zhouyi_index": ["周易"],
    "zhouyi_chapters": ["周易/" + n for n in ZHOUYI_CHAPTERS],
    "zhouyi_commentaries": ["周易/序卦", "周易/雜卦", "周易/繫辭上", "周易/說卦"],
    # The four pages above are redirects; these are their targets.
    "yizhuan": ["易傳/序卦", "易傳/雜卦", "易傳/繫辭上", "易傳/說卦"],
    "zhengyi_index": ["周易正義"],
    "jingshi_collated": ["京氏易傳"],
    "jingshi_siku": ["京氏易傳 (四庫全書本)", "京氏易傳 (四庫全書本)/卷上",
                     "京氏易傳 (四庫全書本)/卷中", "京氏易傳 (四庫全書本)/卷下"],
    "benyi_siku": ["原本周易本義 (四庫全書本)", "原本周易本義 (四庫全書本)/卷末上",
                   "原本周易本義 (四庫全書本)/卷末下", "原本周易本義 (四庫全書本)/卷01"],
    # Coin-method attestation: Jia Gongyan's subcommentary on the Yili, and a Qing citation of it.
    "coin_method": ["儀禮註疏/卷一", "日知錄/卷15"],
}


def api_get(params):
    params = dict(params, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def list_prefix(prefix):
    out, cont = [], {}
    while True:
        d = api_get(dict({"action": "query", "list": "allpages", "apprefix": prefix,
                          "aplimit": "500"}, **cont))
        out += [p["title"] for p in d["query"]["allpages"]]
        if "continue" not in d:
            return out
        cont = d["continue"]


def fetch(titles):
    d = api_get({"action": "query", "prop": "revisions", "rvprop": "ids|timestamp|content",
                 "rvslots": "main", "titles": "|".join(titles)})
    return d["query"]["pages"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    if os.path.exists(a.outdir):
        sys.exit("refusing to write into an existing directory")
    os.makedirs(a.outdir)
    groups = dict(GROUPS)
    # Kong Yingda's Zhouyi zhengyi chapter pages, discovered by prefix.
    groups["zhengyi_chapters"] = [t for t in list_prefix("周易正義/")]
    manifest = {"api": API, "user_agent": UA, "pages": []}
    for group, titles in groups.items():
        for i in range(0, len(titles), 25):
            batch = titles[i:i + 25]
            pages = fetch(batch)
            retrieved = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            for p in pages:
                if p.get("missing"):
                    manifest["pages"].append({"group": group, "title": p["title"], "missing": True})
                    continue
                rev = p["revisions"][0]
                text = rev["slots"]["main"]["content"]
                raw = text.encode("utf-8")
                fn = "%d.wiki" % p["pageid"]
                with open(os.path.join(a.outdir, fn), "wb") as f:
                    f.write(raw)
                manifest["pages"].append({
                    "group": group, "title": p["title"], "pageid": p["pageid"],
                    "revid": rev["revid"], "rev_timestamp": rev["timestamp"],
                    "retrieved": retrieved, "bytes": len(raw),
                    "sha256": hashlib.sha256(raw).hexdigest(), "file": fn,
                    "permanent_url": "https://zh.wikisource.org/w/index.php?oldid=%d" % rev["revid"],
                })
            time.sleep(1.0)
    manifest["pages"].sort(key=lambda r: (r["group"], r["title"]))
    with open(os.path.join(a.outdir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
        f.write("\n")
    missing = [r["title"] for r in manifest["pages"] if r.get("missing")]
    print("pages:", len(manifest["pages"]), "missing:", missing)


if __name__ == "__main__":
    main()
