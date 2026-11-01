#!/usr/bin/env python3
"""Fresh Phase-1 checks for INV-0005 / ASN-0001.

This program uses only the two TSV transcriptions in ../data.  In particular,
the eight-palace TSV is treated as source data to be tested against, not as
output of the difference-vector construction.
"""

from csv import DictReader
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read_tsv(name):
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as f:
        return list(DictReader(f, delimiter="\t"))


received_rows = read_tsv("received_order.tsv")
palace_rows = read_tsv("eight_palaces_source.tsv")


def xor(a, b):
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))


ONES6 = "111111"


def R(x):
    return x[::-1]


def C(x):
    return xor(x, ONES6)


def sigma(x):
    return R(x) if R(x) != x else C(x)


def phi(x):
    return xor(x[:3], x[3:])


WORDS = tuple("".join(p) for p in product("01", repeat=6))
TRIGRAMS = {
    "Qian": "111",
    "Dui": "110",
    "Li": "101",
    "Zhen": "100",
    "Xun": "011",
    "Kan": "010",
    "Gen": "001",
    "Kun": "000",
}
D = (
    "000000",
    "100000",
    "110000",
    "111000",
    "111100",
    "111110",
    "111010",
    "000010",
)
STATUSES = (
    "pure/6th",
    "1st",
    "2nd",
    "3rd",
    "4th",
    "5th",
    "wandering",
    "returning",
)
EXPECTED_STATUS_BY_PHI = {
    "000": "pure/6th",
    "100": "1st",
    "110": "2nd",
    "111": "3rd",
    "011": "4th",
    "001": "5th",
    "101": "wandering",
    "010": "returning",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


# Input-data integrity checks.
require(len(received_rows) == 64, "received transcription does not have 64 rows")
require(len(palace_rows) == 64, "palace transcription does not have 64 rows")
by_number = {int(r["number"]): r for r in received_rows}
require(set(by_number) == set(range(1, 65)), "received numbers are not exactly 1..64")
require(len({r["word_bottom_to_top"] for r in received_rows}) == 64,
        "received words are not all distinct")
require({r["word_bottom_to_top"] for r in received_rows} == set(WORDS),
        "received words are not the complete six-bit cube")
for r in received_rows:
    require(r["lower_bits"] == TRIGRAMS[r["lower_trigram"]],
            f"bad lower trigram at #{r['number']}")
    require(r["upper_bits"] == TRIGRAMS[r["upper_trigram"]],
            f"bad upper trigram at #{r['number']}")
    require(r["word_bottom_to_top"] == r["lower_bits"] + r["upper_bits"],
            f"bad concatenation at #{r['number']}")
require(len({int(r["hex_number"]) for r in palace_rows}) == 64,
        "palace table does not contain every received number once")
require({int(r["hex_number"]) for r in palace_rows} == set(range(1, 65)),
        "palace table numbers are not exactly 1..64")
for r in palace_rows:
    rr = by_number[int(r["hex_number"])]
    require(r["hex_name_zh"] == rr["name_zh"],
            f"palace/received name mismatch at #{r['hex_number']}")


# C-0001: exhaustive check on all 64 words.
require(all(sigma(sigma(x)) == x for x in WORDS), "sigma is not involutive")
require(all(sigma(x) != x for x in WORDS), "sigma has a fixed point")


# C-0002: all received adjacent pairs, plus the claimed counts and R-fixed list.
received_pairs = []
for odd in range(1, 65, 2):
    a = by_number[odd]["word_bottom_to_top"]
    b = by_number[odd + 1]["word_bottom_to_top"]
    require(sigma(a) == b and sigma(b) == a,
            f"received pair {odd}-{odd+1} is not a sigma orbit")
    received_pairs.append((odd, odd + 1, "R" if R(a) == b else "C"))
require(sum(kind == "R" for _, _, kind in received_pairs) == 28,
        "received reversal-pair count is not 28")
require(sum(kind == "C" for _, _, kind in received_pairs) == 4,
        "received complement-pair count is not 4")
r_fixed_numbers = [int(r["number"]) for r in received_rows
                   if R(r["word_bottom_to_top"]) == r["word_bottom_to_top"]]
require(r_fixed_numbers == [1, 2, 27, 28, 29, 30, 61, 62],
        "unexpected list of R-fixed received hexagrams")


# C-0016: exact image of D under phi and the unique 8x8 decomposition.
phi_D = [phi(d) for d in D]
require(len(set(phi_D)) == 8 and set(phi_D) == {"".join(p) for p in product("01", repeat=3)},
        "phi is not a bijection on D")
P = tuple(t + t for t in ("".join(p) for p in product("01", repeat=3)))
decompositions = {
    x: [(b, d) for b in P for d in D if xor(b, d) == x]
    for x in WORDS
}
require(all(len(v) == 1 for v in decompositions.values()),
        "not every word has exactly one P+D decomposition")
for b in P:
    vals = [phi(xor(b, d)) for d in D]
    require(len(set(vals)) == 8, f"palace based at {b} misses/repeats a phi value")


# C-0017: compare all 64 independently transcribed source-table cells with D.
for r in palace_rows:
    slot = int(r["slot_order"])
    base = by_number[int(r["base_number"])]["word_bottom_to_top"]
    actual = by_number[int(r["hex_number"])]["word_bottom_to_top"]
    require(base[:3] == base[3:], f"palace base #{r['base_number']} is not doubled")
    require(r["status"] == STATUSES[slot],
            f"source status/slot mismatch for #{r['hex_number']}")
    require(actual == xor(base, D[slot]),
            f"D construction disagrees with source table for #{r['hex_number']}")


# C-0018: status depends only on phi, both generated and in all source rows.
require({phi(d): STATUSES[i] for i, d in enumerate(D)} == EXPECTED_STATUS_BY_PHI,
        "D induces a different status-by-phi table")
for r in palace_rows:
    x = by_number[int(r["hex_number"])]["word_bottom_to_top"]
    require(r["status"] == EXPECTED_STATUS_BY_PHI[phi(x)],
            f"source status is not status(phi) for #{r['hex_number']}")


# C-0019: formal identity, induced status map, and all 28 received R-pairs.
require(all(phi(R(x)) == phi(x)[::-1] for x in WORDS),
        "phi(Rx) != reverse(phi(x)) somewhere")
EXPECTED_REVERSED_STATUS = {
    "pure/6th": "pure/6th",
    "1st": "5th",
    "2nd": "4th",
    "3rd": "3rd",
    "4th": "2nd",
    "5th": "1st",
    "wandering": "wandering",
    "returning": "returning",
}
status_by_number = {int(r["hex_number"]): r["status"] for r in palace_rows}
word_to_number = {r["word_bottom_to_top"]: int(r["number"]) for r in received_rows}
nonpal_r_orbits = []
seen = set()
for x in WORDS:
    if x == R(x) or x in seen:
        continue
    y = R(x)
    seen.update((x, y))
    nx, ny = word_to_number[x], word_to_number[y]
    sx, sy = status_by_number[nx], status_by_number[ny]
    require(EXPECTED_REVERSED_STATUS[sx] == sy,
            f"traditional status reversal failure at #{nx}/#{ny}")
    nonpal_r_orbits.append(tuple(sorted((nx, ny))))
require(len(nonpal_r_orbits) == 28, "there are not exactly 28 nonpalindromic R-orbits")
require(set(nonpal_r_orbits) == {(a, b) for a, b, k in received_pairs if k == "R"},
        "received reversal pairs and all nonpalindromic R-orbits differ")


# C-0026 under coherent relabelling: a physical figure formerly x is now C(x).
swapped_by_number = {n: C(r["word_bottom_to_top"]) for n, r in by_number.items()}
require(all(sigma(sigma(x)) == x and sigma(x) != x for x in WORDS),
        "C-0001 fails in swapped coordinates")
for odd in range(1, 65, 2):
    require(sigma(swapped_by_number[odd]) == swapped_by_number[odd + 1],
            f"C-0002 fails after relabelling at {odd}-{odd+1}")
require(all(phi(C(x)) == phi(x) for x in WORDS),
        "phi is not invariant under global label swap")
for r in palace_rows:
    slot = int(r["slot_order"])
    base_swapped = swapped_by_number[int(r["base_number"])]
    actual_swapped = swapped_by_number[int(r["hex_number"])]
    require(actual_swapped == xor(base_swapped, D[slot]),
            f"palace construction fails after relabelling at #{r['hex_number']}")
    require(EXPECTED_STATUS_BY_PHI[phi(actual_swapped)] == r["status"],
            f"status changes after relabelling at #{r['hex_number']}")
require(all(phi(R(C(x))) == phi(C(x))[::-1] for x in WORDS),
        "C-0019 identity fails in swapped coordinates")


print("PASS input integrity: 64 received figures; 64 palace-table entries")
print("PASS C-0001: exhaustive over 64 words")
print("PASS C-0002: 32 adjacent sigma-orbits = 28 R-pairs + 4 C-pairs")
print("  R-fixed numbers:", ",".join(map(str, r_fixed_numbers)))
print("PASS C-0016: phi(D) in D order =", ",".join(phi_D))
print("PASS C-0017(table): all 64 source-table cells equal base xor D[slot]")
print("PASS C-0018: all 64 source statuses equal status(phi(x))")
print("PASS C-0019: identity on 64 words and status rule on 28 R-orbits")
print("PASS C-0026: coherent global label swap checks")
