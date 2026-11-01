#!/usr/bin/env python3
"""Exact finite certificate for eight-point cells of the six-cube.

Classifies (a) cells with all degree-one/two character sums zero and
(b) cells with minimum Hamming distance at least three, after translation
to contain zero. It compares both independent searches with the complete
coordinate-permutation orbit of the specified linear kernel.
"""
import argparse
from collections import Counter
import hashlib
from itertools import combinations, permutations
import json
from pathlib import Path
import platform


def wt(x):
    return bin(x).count("1")


def cliques(candidates, adjacency, remaining, prefix=()):
    """Every requested-size clique once, in increasing candidate order."""
    if remaining == 0:
        yield prefix
        return
    for j, v in enumerate(candidates):
        tail = [w for w in candidates[j + 1:] if w in adjacency[v]]
        if len(tail) >= remaining - 1:
            yield from cliques(tail, adjacency, remaining - 1, prefix + (v,))


def permute_word(x, permutation):
    return sum(((x >> i) & 1) << permutation[i] for i in range(6))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    dest = Path(ap.parse_args().out)
    if dest.exists():
        raise SystemExit("Refusing to overwrite an existing output")
    # A balanced coordinate has three additional zero rows beyond fixed row 0.
    # Two independent balanced coordinates share exactly one of these zeros.
    triples = [sum(1 << i for i in triple) for triple in combinations(range(7), 3)]
    adjacency = {a: {b for b in triples if wt(a & b) == 1} for a in triples}
    column_cliques = list(cliques(triples, adjacency, 6))
    oa_cells = set()
    for columns in column_cliques:
        for permutation in permutations(range(6)):
            words = [0] + [sum((1 - ((columns[j] >> i) & 1)) << permutation[j]
                               for j in range(6)) for i in range(7)]
            oa_cells.add(tuple(sorted(words)))
    # Independently classify all eight-point codes containing zero and d >= 3.
    allowed = [x for x in range(1, 64) if wt(x) >= 3]
    distance_graph = {a: {b for b in allowed if wt(a ^ b) >= 3} for a in allowed}
    distance_cells = {tuple(sorted((0,) + rows)) for rows in cliques(allowed, distance_graph, 7)}
    rows = (21, 38, 56)
    kernel = tuple(x for x in range(64) if all(wt(x & r) % 2 == 0 for r in rows))
    orbit = {tuple(sorted(permute_word(x, p) for x in kernel)) for p in permutations(range(6))}
    assert len(column_cliques) == 210
    assert len(oa_cells) == len(distance_cells) == len(orbit) == 30
    assert oa_cells == distance_cells == orbit
    for cell in oa_cells:
        assert len(set(cell)) == 8 and 0 in cell
        assert all(a ^ b in cell for a in cell for b in cell)
        assert min(wt(a ^ b) for a, b in combinations(cell, 2)) == 3
        for s in range(1, 64):
            if wt(s) <= 2:
                assert sum((-1) ** wt(s & x) for x in cell) == 0
    translated = {tuple(sorted(x ^ a for x in cell)) for cell in oa_cells for a in range(64)}
    assert len(translated) == 240
    # All cells therefore have the same contribution to conditional label
    # entropy under coordinate-symmetric noise, by translation/permutation.
    result = {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "context": "full; context-exposed; reported research, not independent verification",
        "orthogonal_array_column_candidates": len(triples),
        "orthogonal_array_six_column_cliques": len(column_cliques),
        "distance_graph_candidates": len(allowed),
        "zero_containing_orthogonal_arrays": len(oa_cells),
        "zero_containing_distance_three_codes": len(distance_cells),
        "kernel_coordinate_orbit_size": len(orbit),
        "three_independent_descriptions_agree": True,
        "all_zero_containing_cells_are_linear": True,
        "all_translated_cells_count": len(translated),
        "kernel_rows": rows,
        "kernel": kernel,
        "zero_containing_cells": sorted(oa_cells),
        "all_translated_cells": sorted(translated),
        "scope": "8-point cells of the 6-cube only; endpoint information theorem requires the accompanying asymptotic argument",
    }
    with dest.open("x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print("210 column cliques; 30 normalized cells; 240 translated cells.")
    print("Orthogonal-array, minimum-distance and kernel-orbit classifications agree exactly.")
    print("Output:", dest)


if __name__ == "__main__":
    main()
