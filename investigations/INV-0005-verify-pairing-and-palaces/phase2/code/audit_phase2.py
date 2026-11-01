#!/usr/bin/env python3
"""Bounded significance checks added during the Phase-2 audit.

These are deliberately labelled comparison classes, not historical null
models.  They quantify two narrow readings of "the soul moves fill the gaps."
"""

from itertools import combinations, product
from math import comb


def xor(a, b):
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))


def phi(x):
    return xor(x[:3], x[3:])


def toggle(x, one_based_line):
    i = one_based_line - 1
    return x[:i] + str(1 - int(x[i])) + x[i + 1:]


prefix = ("000000", "100000", "110000", "111000", "111100", "111110")
all_words = tuple("".join(p) for p in product("01", repeat=6))
all_phi = {"".join(p) for p in product("01", repeat=3)}
prefix_phi = {phi(x) for x in prefix}
missing_phi = all_phi - prefix_phi

# Comparison class 1: keep the six prefix representatives; choose an unordered
# pair of distinct additional vectors uniformly from the other 58 words.
remaining = tuple(x for x in all_words if x not in prefix)
successes = []
for a, b in combinations(remaining, 2):
    if prefix_phi | {phi(a), phi(b)} == all_phi and len(prefix_phi | {phi(a), phi(b)}) == 8:
        successes.append((a, b))
assert len(remaining) == 58
assert len(successes) == 64
assert len(successes) / comb(58, 2) == 64 / 1653

# Comparison class 2: keep generations 1--5 and the rule "returning restores
# the lower trigram"; allow wandering to revert any one of the five lines
# changed at generation 5.  This is a five-member local-procedure family.
fifth = prefix[-1]
local_rows = []
for line in range(1, 6):
    wandering = toggle(fifth, line)
    returning = "000" + wandering[3:]
    image = prefix_phi | {phi(wandering), phi(returning)}
    local_rows.append((line, wandering, phi(wandering), returning, phi(returning), image == all_phi))
assert [r[0] for r in local_rows if r[-1]] == [4]

print("Fixed prefix phi values:", ",".join(phi(x) for x in prefix))
print("Missing phi values:", ",".join(sorted(missing_phi)))
print("Arbitrary-vector comparison: 64 successful unordered pairs / C(58,2)=1653")
print("Arbitrary-vector success fraction:", f"{64/1653:.12f}")
print("Local reversion comparison:")
for row in local_rows:
    line, w, pw, r, pr, ok = row
    print(f"  line {line}: wandering={w} phi={pw}; returning={r} phi={pr}; transversal={ok}")
print("Local success count: 1/5 (only line 4)")
