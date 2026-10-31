#!/usr/bin/env python3
"""Executed finite probes of external-result transfer; no historical data assumed.

Run: python3 compute/experiments/INV-0003/corpus_pilots.py --out FILE
All mathematical claims remain reported pending an independent audit.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path


def entropy(masses):
    total = sum(masses)
    return -sum((n / total) * math.log2(n / total) for n in masses if n)


def binary_entropy(p):
    return entropy([p, 1-p])


def reverse(x, n=6):
    return sum(((x >> i) & 1) << (n-1-i) for i in range(n))


def difference(x):
    return (x & 7) ^ (x >> 3)


def channel(numerator, denominator, n=6):
    size = 1 << n
    q = denominator - numerator
    weights = [[numerator ** bin(x ^ y).count('1') * q ** (n-bin(x ^ y).count('1'))
                for y in range(size)] for x in range(size)]
    normalizer = denominator ** n
    assert all(sum(row) == normalizer for row in weights)
    assert all(sum(row[y] for row in weights) == normalizer for y in range(size))
    return weights, normalizer


def information(labels, weights, normalizer):
    size = len(labels)
    unique = sorted(set(labels))
    sums = [[sum(weights[x][y] for x in range(size) if labels[x] == label)
             for label in unique] for y in range(size)]
    assert all(sum(row) == normalizer for row in sums)
    value = entropy(list(Counter(labels).values())) - sum(entropy(row) for row in sums) / size
    certificate = hashlib.sha256(json.dumps(sums, separators=(',', ':')).encode()).hexdigest()
    return value, certificate


def information_pilot():
    # Strings list the six coordinates from bottom to top; source correspondence is not asserted.
    words = ['000000', '100000', '110000', '111000', '111100', '111110', '111010', '000010']
    differences = [sum(int(bit) << i for i, bit in enumerate(word)) for word in words]
    representatives = {difference(d): d for d in differences}
    assert len(representatives) == 8
    generation = [difference(x) for x in range(64)]
    base = [(x ^ representatives[difference(x)]) & 7 for x in range(64)]
    assert all((x ^ representatives[difference(x)]) >> 3 == base[x] for x in range(64))
    assert Counter(generation) == Counter({i: 8 for i in range(8)})
    assert Counter(base) == Counter({i: 8 for i in range(8)})
    assert len(set(zip(generation, base))) == 64
    cases = []
    for a, b in [(1, 8), (1, 4)]:
        weights, normalizer = channel(a, b)
        p = Fraction(a, b)
        q = 2*p*(1-p)
        raw_coordinate, _ = information([x & 1 for x in range(64)], weights, normalizer)
        ginfo, ghash = information(generation, weights, normalizer)
        binfo, bhash = information(base, weights, normalizer)
        assert abs(raw_coordinate - (1-binary_entropy(p))) < 1e-12
        assert abs(ginfo - 3*(1-binary_entropy(q))) < 1e-12
        functions = []
        for truth_table in range(256):
            labels = [(truth_table >> generation[x]) & 1 for x in range(64)]
            value, _ = information(labels, weights, normalizer)
            functions.append((value, truth_table, sum((truth_table >> i) & 1 for i in range(8))))
        best = max(value for value, _, _ in functions)
        maximizers = [t for value, t, _ in functions if abs(value-best) < 1e-12]
        signed_coordinates = [sum((((i >> bit) & 1) ^ sign) << i for i in range(8))
                              for bit in range(3) for sign in range(2)]
        assert set(maximizers) == set(signed_coordinates)
        assert abs(best - (1-binary_entropy(q))) < 1e-12
        cases.append(dict(crossover=str(p), induced_difference_crossover=str(q),
                          raw_coordinate_information_bits=raw_coordinate,
                          generation_information_bits=ginfo, base_information_bits=binfo,
                          best_binary_difference_summary_bits=best,
                          maximizer_truth_tables=maximizers, boolean_functions_checked=256,
                          conditional_mass_sha256=dict(generation=ghash, base=bhash)))
    return dict(domain='Uniform six-bit input, independent identical symmetric bit flips; no historical probability model asserted',
                difference_words=words, joint_base_difference_pairs=64, cases=cases)


def matching_pilot():
    adjacency = {x: {x ^ 63} | ({reverse(x)} if reverse(x) != x else set()) for x in range(64)}
    remaining, components = set(adjacency), []
    while remaining:
        pending = [min(remaining)]
        component = set()
        while pending:
            x = pending.pop()
            if x not in component:
                component.add(x)
                pending.extend(adjacency[x] - component)
        remaining -= component
        components.append(component)
    counts = Counter(map(len, components))
    assert counts == {2: 8, 4: 12}
    assert all(len(adjacency[x]) == (1 if len(c) == 2 else 2) for c in components for x in c)
    # Enumerate local pairings directly, rather than assuming a component formula.
    def pairings(vertices):
        if not vertices:
            return [()]
        x = min(vertices)
        return [((x, y),) + tail for y in sorted(adjacency[x] & vertices)
                for tail in pairings(vertices - {x, y})]
    local = [pairings(c) for c in components]
    count = math.prod(map(len, local))
    assert count == 4096
    for choices in itertools.product(*local):
        pairs = [edge for choice in choices for edge in choice]
        assert len(pairs) == 32 and len({v for edge in pairs for v in edge}) == 64
    # Pointwise matching entropy theorem, evaluated in bits at the uniform law.
    edge_marginals = [Fraction(1) if len(c) == 2 else Fraction(1, 2)
                      for c in components for x in c for y in adjacency[x] if x < y]
    f = -sum(float(p)*math.log2(float(p)) for p in edge_marginals)
    b = -sum(float(1-p)*math.log2(float(1-p)) for p in edge_marginals if p < 1)
    lower = f - (2-2/32)*b
    return dict(vertices=64, component_sizes=dict(sorted(counts.items())), perfect_matchings=count,
                exact_uniform_entropy_bits=math.log2(count),
                external_entropy_lower_bits=lower, external_entropy_upper_bits=f,
                conclusion='The imported entropy estimate is loose here; exact factorization is preferable for this graph.')


def table_pilot():
    tables = [[[a, 2-a], [2-a, a]] for a in range(3)]
    multiplicities = [math.comb(2, a)*math.comb(2, 2-a) for a in range(3)]
    assert multiplicities == [1, 4, 1]
    return dict(row_margins=[2, 2], column_margins=[2, 2], tables=tables,
                uniform_table_probabilities=['1/3']*3,
                labelled_allocation_multiplicities=multiplicities,
                labelled_allocation_probabilities=[str(Fraction(w, sum(multiplicities))) for w in multiplicities],
                extreme_table_event_probabilities=dict(uniform_table='2/3', labelled_allocation='1/3'),
                conclusion='Uniform tables and tables induced by uniform labelled allocations are different null models.')


def shuffle_pilot():
    n, d, t = 64, 6, 6
    missing_mass = Fraction(1 << (t*n//2), math.factorial(n))
    lower_mixing_time = math.ceil(math.log2(Fraction(3,4)*math.factorial(n)) / (n//2))
    # Exact marginal action of one sweep on each initial label, integer weights.
    for initial in range(n):
        distribution = Counter({initial: 1})
        for direction in range(d):
            updated = Counter()
            for x, mass in distribution.items():
                updated[x] += mass
                updated[x ^ (1 << direction)] += mass
            distribution = updated
        assert distribution == Counter({i: 1 for i in range(n)})
    return dict(cards=n, physical_shuffles=t, random_bits=t*n//2,
                one_card_marginal_exactly_uniform=True,
                support_fraction_upper_bound=str(missing_mass),
                support_fraction_log2=float(math.log2(missing_mass.numerator)-math.log2(missing_mass.denominator)),
                total_variation_lower_bound_exact='1 - ('+str(missing_mass)+')',
                mixing_time_at_TV_one_quarter_at_least=lower_mixing_time,
                conclusion='One-card uniformity after one six-direction sweep does not establish uniformity of the order.')


def run():
    return dict(status='reported; full-context author computation, not independent verification',
                python=platform.python_version(), randomness='none; deterministic enumeration and exact integer masses',
                numerical_entropy='binary64 evaluation of logarithms; exact conditional masses hashed; not an interval certificate',
                information=information_pilot(), matching=matching_pilot(), null_measures=table_pilot(), shuffle=shuffle_pilot())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, indent=2, sort_keys=True))
