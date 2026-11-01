#!/usr/bin/env python3
"""Full-context research: exact linear-label controls on six uniform bits.

All verdicts use integer/rational arithmetic. Decimal logarithms only display
information values. No code or results from earlier investigations are imported.
Use --out with a fresh path; an existing output is never overwritten.
"""
import argparse
from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import reduce
import hashlib
import itertools
import json
from pathlib import Path
import platform


def weight(x):
    return bin(x).count("1")


def span(rows):
    return tuple(reduce(int.__xor__, (r for i, r in enumerate(rows) if u >> i & 1), 0)
                 for u in range(8))


def label(rows, x):
    return sum((weight(r & x) % 2) << i for i, r in enumerate(rows))


def bases():
    """Every 3-by-6 binary RREF matrix once; leftmost = least significant bit."""
    for pivots in itertools.combinations(range(6), 3):
        choices = []
        for pivot in pivots:
            free = [j for j in range(pivot + 1, 6) if j not in pivots]
            choices.append([(1 << pivot) + sum(((s >> i) & 1) << j for i, j in enumerate(free))
                            for s in range(1 << len(free))])
        yield from itertools.product(*choices)


def noise_polynomials(rows):
    """Eight coefficient vectors for 8 P(A E = z), as polynomials in rho."""
    words = span(rows)
    return tuple(sorted(tuple(sum((-1) ** weight(u & z) for u in range(8)
                                  if weight(words[u]) == j) for j in range(7))
                        for z in range(8)))


def poly_value(poly, rho):
    return sum(F(c) * rho ** j for j, c in enumerate(poly))


def noise_distribution(rows, p):
    """Independent direct enumeration over all 64 flip masks."""
    masses = [F(0)] * 8
    for e in range(64):
        d = weight(e)
        masses[label(rows, e)] += p ** d * (1 - p) ** (6 - d)
    return masses


def information(masses):
    with localcontext() as ctx:
        ctx.prec = 60
        ln2 = Decimal(2).ln()
        h = Decimal(0)
        for mass in masses:
            if mass:
                x = Decimal(mass.numerator) / Decimal(mass.denominator)
                h -= x * x.ln() / ln2
        return str(Decimal(3) - h)


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def add(*polys):
    out = [0] * max(map(len, polys))
    for p in polys:
        for i, v in enumerate(p):
            out[i] += v
    return out


def scale(p, c):
    return [c * v for v in p]


def pad(p):
    return list(p) + [0] * (7 - len(p))


def majorization_certificate():
    # Entries are numerator polynomials, each with common denominator 8.
    g0 = [1, 0, 3, 0, 3, 0, 1]
    g1 = [1, 0, 1, 0, -1, 0, -1]
    g2 = [1, 0, -1, 0, -1, 0, 1]
    g3 = [1, 0, -3, 0, 3, 0, -1]
    a = [1, 0, 0, 4, 3, 0, 0]
    b = [1, 0, 0, 0, -1, 0, 0]
    c = [1, 0, 0, -4, 3, 0, 0]
    g_sorted = [g0] + [g1] * 3 + [g2] * 3 + [g3]
    l_sorted = [a] + [b] * 6 + [c]
    r2 = [0, 0, 1]
    one_minus_r = [1, -1]
    expected = {
        1: multiply(multiply(r2, multiply(one_minus_r, one_minus_r)), [3, 2, 1]),
        2: scale(multiply(r2, one_minus_r), 4),
        3: multiply(multiply(r2, one_minus_r), [5, 1, 1, 1]),
        4: scale(multiply(multiply(r2, one_minus_r), [3, 1, 1, 1]), 2),
    }
    expected.update({5: expected[3], 6: expected[2], 7: expected[1]})
    differences = []
    for k in range(1, 8):
        diff = add(*g_sorted[:k], *[scale(q, -1) for q in l_sorted[:k]])
        assert pad(diff) == pad(expected[k])
        differences.append(diff)
    assert add(*g_sorted) == add(*l_sorted) == [8, 0, 0, 0, 0, 0, 0]
    assert tuple(sorted(tuple(q) for q in g_sorted)) == noise_polynomials((9, 18, 36))
    assert tuple(sorted(tuple(q) for q in l_sorted)) == noise_polynomials((21, 38, 56))
    return {
        "G_sorted_probability_numerators": g_sorted,
        "Lambda_sorted_probability_numerators": l_sorted,
        "G_minus_Lambda_top_k_numerators": differences,
        "factorization_identities_exact": True,
        "domain": "0 < rho < 1; all seven prefix differences strictly positive",
        "consequence": "G noise law strictly majorizes Lambda noise law; I(G;Y) > I(Lambda;Y)",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    dest = Path(args.out)
    if dest.exists():
        raise SystemExit("Refusing to overwrite an existing output")
    rows_list = list(bases())
    spaces = {tuple(sorted(span(rows))) for rows in rows_list}
    assert len(rows_list) == len(spaces) == 1395
    # Independent enumeration: all unordered triples of nonzero vectors.
    alternate = set()
    for rows in itertools.combinations(range(1, 64), 3):
        words = tuple(sorted(span(rows)))
        if len(set(words)) == 8:
            alternate.add(words)
    assert alternate == spaces
    profiles = defaultdict(list)
    for rows in rows_list:
        profiles[noise_polynomials(rows)].append(rows)
    p = F(1, 4)
    rho = 1 - 2 * p
    denominator = 4 ** 6
    ranked = []
    entries = []
    for polys, all_rows in profiles.items():
        rows = all_rows[0]
        masses = sorted(noise_distribution(rows, p))
        from_walsh = sorted(poly_value(q, rho) / 8 for q in polys)
        assert masses == from_walsh and sum(masses) == 1
        nums = [int(q * denominator) for q in masses]
        assert all(F(n, denominator) == q for n, q in zip(nums, masses))
        # I = -9 + (1/4096) log2(product n**n); order is exactly integer order.
        product = reduce(int.__mul__, (n ** n for n in nums), 1)
        ranked.append((product, polys))
        words = span(rows)
        entries.append({
            "representative_rows": list(rows),
            "equivalent_subspaces_count": len(all_rows),
            "all_rref_bases": [list(r) for r in all_rows],
            "noise_probability_numerators_at_coin": nums,
            "noise_probability_denominator_at_coin": denominator,
            "rho_polynomials_with_denominator_8": polys,
            "dual_weight_distribution": dict(sorted(Counter(weight(w) for w in words).items())),
            "coin_information_bits_approx": information(masses),
            "comparison_integer_bits": product.bit_length(),
            "comparison_integer_sha256": hashlib.sha256(product.to_bytes((product.bit_length()+7)//8, "big")).hexdigest(),
        })
    ranked.sort()
    minimum, min_profile = ranked[0]
    maximum, max_profile = ranked[-1]
    min_rows, max_rows = profiles[min_profile], profiles[max_profile]
    assert len(profiles) == 22
    assert len(min_rows) == 30 and len(max_rows) == 20
    assert min_profile == noise_polynomials((21, 38, 56))
    assert max_profile == noise_polynomials((1, 2, 4))
    permutation_orbit = set()
    for permutation in itertools.permutations(range(6)):
        changed_rows = tuple(sum(((row >> i) & 1) << permutation[i] for i in range(6))
                             for row in (21, 38, 56))
        permutation_orbit.add(tuple(sorted(span(changed_rows))))
    assert permutation_orbit == {tuple(sorted(span(r))) for r in min_rows}
    coordinate_spaces = {tuple(sorted(span(tuple(1 << i for i in coords))))
                         for coords in itertools.combinations(range(6), 3)}
    assert coordinate_spaces == {tuple(sorted(span(r))) for r in max_rows}
    assert all(minimum < value < maximum for value, profile in ranked
               if profile not in (min_profile, max_profile))
    for e in entries:
        profile = tuple(tuple(q) for q in e["rho_polynomials_with_denominator_8"])
        e["coin_rank_of_profile"] = next(i + 1 for i, (_, q) in enumerate(ranked) if q == profile)
    comparisons = {}
    for name, rows in [("trigram", (1, 2, 4)), ("generation", (9, 18, 36)), ("Lambda", (21, 38, 56))]:
        labels = [label(rows, x) for x in range(64)]
        assert sorted(Counter(labels).values()) == [8] * 8
        comparisons[name] = {
            "rows_bitmasks": rows,
            "dual_weights": sorted(weight(w) for w in span(rows)[1:]),
            "mean_boundary_degree": sum(any((row >> i) & 1 for row in rows) for i in range(6)),
            "W1": sum(weight(w) == 1 for w in span(rows)[1:]),
            "information_by_p": {str(q): information(noise_distribution(rows, q))
                                 for q in (F(1, 10000), F(1, 8), F(1, 4), F(49, 100))},
        }
    # Explicit obstruction to promoting a failed majorization route to a proof
    # of all-noise global minimality. Entropy ordering need not require majorization.
    candidate = (9, 10, 60)
    td = sorted(noise_distribution((21, 38, 56), p), reverse=True)
    other = sorted(noise_distribution(candidate, p), reverse=True)
    bad = [k for k in range(1, 8) if sum(td[:k]) > sum(other[:k])]
    assert bad
    result = {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "context": "full; context-exposed; reported research, not independent verification",
        "linear_subspaces": len(rows_list),
        "independent_enumeration_agrees": True,
        "distinct_noise_polynomial_profiles": len(profiles),
        "coin_extrema": {"minimum_rows": min_rows, "maximum_rows": max_rows,
                         "minimum_count": len(min_rows), "maximum_count": len(max_rows),
                         "strict_integer_comparisons": True,
                         "minimum_exactly_Lambda_coordinate_permutation_orbit": True,
                         "maximum_exactly_coordinate_projections": True},
        "profiles": sorted(entries, key=lambda e: e["coin_rank_of_profile"]),
        "traditional_and_control_labels": comparisons,
        "all_noise_G_vs_Lambda": majorization_certificate(),
        "failed_all_linear_majorization_route": {
            "competitor_rows": candidate, "p": str(p),
            "prefixes_at_which_Lambda_top_sum_exceeds_competitor": bad,
            "scope": "Not a counterexample to entropy optimality; only to universal majorization",
        },
    }
    with dest.open("x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print("1395 subspaces independently enumerated; 22 noise profiles; exact coin extrema: 30 minima, 20 maxima.")
    print("All-noise strict G > Lambda majorization identities checked exactly.")
    print("Output:", dest)


if __name__ == "__main__":
    main()
