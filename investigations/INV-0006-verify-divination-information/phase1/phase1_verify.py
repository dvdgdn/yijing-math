#!/usr/bin/env python3
"""Independent finite checks for INV-0006 / ASN-0014, phase 1.

Only Python's standard library is used.  Exact finite probabilities and the
extremal search use Fraction/integer arithmetic.  Transcendental signs in the
V4 certificate use rational enclosures for log, obtained from the atanh
series with an explicit geometric tail bound.
"""

from __future__ import print_function

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, log2


BITS6 = list(product((0, 1), repeat=6))
D_STRINGS = (
    "000000", "100000", "110000", "111000",
    "111100", "111110", "111010", "000010",
)
D = [tuple(int(c) for c in word) for word in D_STRINGS]


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def g_label(x):
    return tuple(x[i] ^ x[i + 3] for i in range(3))


D_BY_G = {g_label(d): d for d in D}
assert len(D_BY_G) == 8


def t_label(x):
    return x[:3]


def b_label(x):
    d = D_BY_G[g_label(x)]
    z = xor(x, d)
    assert z[:3] == z[3:]
    return z[:3]


LABELS = {"T": t_label, "B": b_label, "G": g_label}


def h2(q):
    if q == 0 or q == 1:
        return 0.0
    return -q * log2(q) - (1 - q) * log2(1 - q)


# ---------------------------------------------------------------------------
# V1 and V2: exact line laws


def remainder_after_counting_by_fours(n):
    """The stipulated remainder: 0 for an empty heap; otherwise 1,...,4."""
    return 0 if n == 0 else (n - 1) % 4 + 1


def split_transition(n, model):
    """Exact distribution of the remaining count after one stipulated split."""
    out = defaultdict(F)
    if model == "uniform":
        denominator = n - 1
        weights = ((left, F(1, denominator)) for left in range(1, n))
    elif model == "binomial":
        denominator = 2 ** n - 2
        weights = ((left, F(comb(n, left), denominator))
                   for left in range(1, n))
    else:
        raise ValueError(model)
    for left, probability in weights:
        right_after_setting_one_aside = n - left - 1
        removed = (1 + remainder_after_counting_by_fours(left)
                   + remainder_after_counting_by_fours(
                       right_after_setting_one_aside))
        out[n - removed] += probability
    assert sum(out.values(), F(0)) == 1
    return dict(out)


def three_change_law(model):
    law = {49: F(1)}
    for unused_change in range(3):
        next_law = defaultdict(F)
        for n, pn in law.items():
            for remaining, conditional in split_transition(n, model).items():
                next_law[remaining] += pn * conditional
        law = dict(next_law)
    assert sum(law.values(), F(0)) == 1
    assert all(n % 4 == 0 for n in law)
    return {n // 4: probability for n, probability in sorted(law.items())}


# ---------------------------------------------------------------------------
# Polynomial and rational interval support for V4


def poly_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def poly_add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return poly_trim(out)


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly_trim(out)


def poly_pow(a, n):
    out = (F(1),)
    base = tuple(a)
    while n:
        if n & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        n //= 2
    return out


def poly_derivative(a):
    if len(a) == 1:
        return (F(0),)
    return tuple(F(i) * a[i] for i in range(1, len(a)))


def poly_eval(a, x):
    out = F(0)
    for coefficient in reversed(a):
        out = out * x + coefficient
    return out


def poly_compose_affine(a, constant, slope):
    """Return a(constant + slope*x)."""
    out = (F(0),)
    affine = (F(constant), F(slope))
    power = (F(1),)
    for coefficient in a:
        out = poly_add(out, tuple(coefficient * z for z in power))
        power = poly_mul(power, affine)
    return out


def distance_enumerator_to_polynomial(counts):
    out = (F(0),)
    p = (F(0), F(1))
    one_minus_p = (F(1), F(-1))
    for distance, count in enumerate(counts):
        if count:
            term = poly_mul(poly_pow(p, distance),
                            poly_pow(one_minus_p, 6 - distance))
            term = tuple(F(count) * z for z in term)
            out = poly_add(out, term)
    return out


class Interval(object):
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        values = (self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi)
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not (self.lo <= 0 <= self.hi)
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * as_interval(other).reciprocal()

    def __repr__(self):
        return "Interval(%r, %r)" % (self.lo, self.hi)


def as_interval(x):
    return x if isinstance(x, Interval) else Interval(x)


def interval_abs_upper(x):
    return max(abs(x.lo), abs(x.hi))


def interval_poly_eval(coefficients, x):
    out = Interval(0)
    for coefficient in reversed(coefficients):
        out = out * x + coefficient
    return out


# At t <= 1/3, 16 terms leave a tail below 2.1e-17.  The smallest
# accepted V4 sign margin is many orders of magnitude larger; the exact tail
# is nevertheless retained in every enclosure.
LOG_TERMS = 16


def atanh_log_series_bounds(t, terms=LOG_TERMS):
    """Enclose log((1+t)/(1-t)) for rational 0 <= t < 1."""
    assert 0 <= t < 1
    total = F(0)
    t_power = t
    t_squared = t * t
    for j in range(terms):
        total += 2 * t_power / (2 * j + 1)
        t_power *= t_squared
    tail = (2 * t ** (2 * terms + 1)
            / ((2 * terms + 1) * (1 - t_squared)))
    return Interval(total, total + tail)


LN2 = atanh_log_series_bounds(F(1, 3))


def two_to(k):
    return F(2 ** k) if k >= 0 else F(1, 2 ** (-k))


def log_fraction_bounds(x):
    """Rigorous natural-log enclosure of a positive Fraction."""
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < two_to(k):
        k -= 1
    while x >= two_to(k + 1):
        k += 1
    z = x / two_to(k)
    assert 1 <= z < 2
    t = (z - 1) / (z + 1)
    return atanh_log_series_bounds(t) + k * LN2


def interval_log(x):
    assert x.lo > 0
    return Interval(log_fraction_bounds(x.lo).lo,
                    log_fraction_bounds(x.hi).hi)


def distance_probability_interval(counts, interval_p, factor_power=0):
    """Enclose q(p)/p**factor_power from its nonnegative distance form."""
    assert interval_p.lo >= 0 and interval_p.hi < 1
    p = interval_p
    one_minus = Interval(1 - p.hi, 1 - p.lo)
    out = Interval(0)
    for distance, count in enumerate(counts):
        if count:
            assert distance >= factor_power
            out += (count * (p ** (distance - factor_power))
                    * (one_minus ** (6 - distance)))
    return out


def interval_power(self, n):
    assert n >= 0
    out = Interval(1)
    base = self
    while n:
        if n & 1:
            out = out * base
        base = base * base
        n //= 2
    return out


Interval.__pow__ = interval_power


def fibers(label_function):
    out = defaultdict(list)
    for x in BITS6:
        out[label_function(x)].append(x)
    assert len(out) == 8 and all(len(cell) == 8 for cell in out.values())
    return list(out.values())


def enumerator_counter(label_function):
    cells = fibers(label_function)
    counter = Counter()
    for y in BITS6:
        for cell in cells:
            counts = [0] * 7
            for x in cell:
                counts[sum(a != b for a, b in zip(x, y))] += 1
            counter[tuple(counts)] += 1
    assert sum(counter.values()) == 64 * 8
    return counter


ENUMERATORS = {name: enumerator_counter(function)
               for name, function in LABELS.items()}


def combined_entropy_terms(first, second):
    """Terms for 64*(natural entropy(first)-natural entropy(second))."""
    weights = Counter(ENUMERATORS[first])
    weights.subtract(ENUMERATORS[second])
    terms = []
    for counts, weight in sorted(weights.items()):
        if weight:
            terms.append((weight, counts,
                          distance_enumerator_to_polynomial(counts)))
    # Both posterior vectors sum to one for every y, so the combined
    # probability polynomial (and its derivative) must cancel identically.
    cancellation = (F(0),)
    for weight, unused_counts, polynomial in terms:
        cancellation = poly_add(
            cancellation, tuple(weight * z for z in polynomial))
    assert cancellation == (F(0),)
    return terms


TERMS_TB = combined_entropy_terms("B", "T")  # sign of I(T)-I(B)
TERMS_BG = combined_entropy_terms("G", "B")  # sign of I(B)-I(G)


def entropy_difference_at_point(terms, p):
    """Rigorous interval for -sum weight*q*ln(q), without the factor 1/64."""
    total = Interval(0)
    for weight, unused_counts, polynomial in terms:
        q = poly_eval(polynomial, p)
        assert q > 0
        total += -weight * q * log_fraction_bounds(q)
    return total


def q_interval_from_counts(counts, p_interval):
    return distance_probability_interval(counts, p_interval)


def q_derivative_interval(counts, p_interval):
    """Differentiate the nonnegative distance form term by term."""
    p = p_interval
    one_minus = Interval(1 - p.hi, 1 - p.lo)
    out = Interval(0)
    for distance, count in enumerate(counts):
        if not count:
            continue
        if distance:
            out += (count * distance * (p ** (distance - 1))
                    * (one_minus ** (6 - distance)))
        if 6 - distance:
            out -= (count * (6 - distance) * (p ** distance)
                    * (one_minus ** (5 - distance)))
    return out


def entropy_difference_derivative_interval(terms, a, b):
    p = Interval(a, b)
    total = Interval(0)
    for weight, counts, unused_polynomial in terms:
        q = q_interval_from_counts(counts, p)
        q_prime = q_derivative_interval(counts, p)
        total += -weight * q_prime * (interval_log(q) + 1)
    return total


def certify_central_interval(terms, left=F(1, 1000), right=F(49, 100)):
    """Mean-value interval certificate on [left,right]."""
    stack = [(left, right, 0)]
    accepted = []
    while stack:
        a, b, depth = stack.pop()
        midpoint = (a + b) / 2
        value = entropy_difference_at_point(terms, midpoint)
        derivative = entropy_difference_derivative_interval(terms, a, b)
        radius = (b - a) / 2
        margin = value.lo - interval_abs_upper(derivative) * radius
        if margin > 0:
            accepted.append((a, b, margin, depth))
            continue
        if depth >= 24:
            raise AssertionError("central certificate did not close: %r %r" % (a, b))
        stack.append((midpoint, b, depth + 1))
        stack.append((a, midpoint, depth + 1))
    return {
        "intervals": len(accepted),
        "max_depth": max(item[3] for item in accepted),
        "min_margin": min(item[2] for item in accepted),
    }


def leading_distance(counts):
    return next(i for i, count in enumerate(counts) if count)


def certify_small_p_derivative(terms, p0=F(1, 1000)):
    """Prove D'(p)>0 on (0,p0] after separating log(1/p)."""
    p = Interval(0, p0)
    coefficient = Interval(0)
    regular = Interval(0)
    for weight, counts, unused_polynomial in terms:
        k = leading_distance(counts)
        q_prime = q_derivative_interval(counts, p)
        r = distance_probability_interval(counts, p, factor_power=k)
        coefficient += weight * k * q_prime
        regular += -weight * q_prime * interval_log(r)
    assert coefficient.lo > 0
    log_one_over_p0 = -log_fraction_bounds(p0)
    lower = coefficient.lo * log_one_over_p0.lo + regular.lo
    assert lower > 0
    return coefficient, regular, lower


def rho_polynomial(counts):
    p_polynomial = distance_enumerator_to_polynomial(counts)
    return poly_compose_affine(p_polynomial, F(1, 2), F(-1, 2))


def certify_high_noise_second_derivative(terms, rho0=F(1, 50)):
    """Prove D''(rho)>0 on [0,rho0]."""
    rho = Interval(0, rho0)
    total = Interval(0)
    exact_derivative_at_zero = F(0)
    for weight, counts, unused_polynomial in terms:
        q = rho_polynomial(counts)
        q1 = poly_derivative(q)
        q2 = poly_derivative(q1)
        iq = interval_poly_eval(q, rho)
        iq1 = interval_poly_eval(q1, rho)
        iq2 = interval_poly_eval(q2, rho)
        total += -weight * (iq2 * (interval_log(iq) + 1)
                            + iq1 * iq1 / iq)
        exact_derivative_at_zero += -weight * poly_eval(q1, F(0))
    # At rho=0 every q is 1/8, so the common (ln q + 1) factor
    # multiplies the exact sum below.  Its vanishing proves D'(0)=0.
    assert exact_derivative_at_zero == 0
    assert total.lo > 0
    return total


def mutual_information_numeric(label_function, p):
    conditional_entropy = 0.0
    for y in BITS6:
        for cell in fibers(label_function):
            q = 0.0
            for x in cell:
                distance = sum(a != b for a, b in zip(x, y))
                q += p ** distance * (1 - p) ** (6 - distance)
            if q:
                conditional_entropy -= q * log2(q) / 64.0
    return 3.0 - conditional_entropy


def mutual_information_interval(name, p):
    """Rigorous bit-valued enclosure at a rational p."""
    entropy_nats = Interval(0)
    for counts, multiplicity in ENUMERATORS[name].items():
        q = poly_eval(distance_enumerator_to_polynomial(counts), p)
        entropy_nats += -F(multiplicity, 64) * q * log_fraction_bounds(q)
    return Interval(3) - entropy_nats / LN2


# ---------------------------------------------------------------------------
# V5: exact beta, W1, and the finite centroid extremum


def beta(label_function):
    changed = 0
    for x in BITS6:
        old = label_function(x)
        for i in range(6):
            y = list(x)
            y[i] ^= 1
            changed += label_function(tuple(y)) != old
    return F(changed, 64)


def centroid(cell):
    return tuple(sum(1 if x[i] == 0 else -1 for x in cell)
                 for i in range(6))


def w1(label_function):
    answer = F(0)
    for cell in fibers(label_function):
        s = centroid(cell)
        answer += F(sum(z * z for z in s), 64 * len(cell))
    return answer


def centroid_extremum_partition_dp():
    """Exact cut-DP proof for all 8-subsets of Q_6, up to row relabeling.

    Label the eight selected vertices 0,...,7.  A cube coordinate is a cut
    of these labels, considered modulo complementation.  Six cuts produce
    distinct vertices iff their common refinement is discrete.  The sum of
    cut costs |S|(8-|S|) is the total pairwise Hamming distance, which equals
    (384-||s||^2)/4.  We retain every cost/profile at most 48.
    """
    n = 8
    all_rows = (1 << n) - 1

    def popcount(mask):
        return bin(mask).count("1")

    cuts = []
    for mask in range(1 << n):
        complement = all_rows ^ mask
        if mask <= complement:
            size = popcount(mask)
            minority = min(size, n - size)
            cuts.append((mask, size * (n - size), minority))
    assert len(cuts) == 128

    def refine(partition, cut):
        blocks = []
        complement = all_rows ^ cut
        for block in partition:
            first = block & cut
            second = block & complement
            if first:
                blocks.append(first)
            if second:
                blocks.append(second)
        return tuple(sorted(blocks))

    states = {(all_rows,): {(0, ())}}
    state_counts = []
    for unused_coordinate in range(6):
        next_states = defaultdict(set)
        for partition, records in states.items():
            for cut, cost, minority in cuts:
                new_partition = refine(partition, cut)
                for old_cost, profile in records:
                    new_cost = old_cost + cost
                    if new_cost <= 48:
                        addition = () if minority == 0 else (minority,)
                        new_profile = tuple(sorted(profile + addition))
                        next_states[new_partition].add((new_cost, new_profile))
        states = dict(next_states)
        state_counts.append((len(states), sum(len(x) for x in states.values())))
    discrete = tuple(1 << i for i in range(n))
    records = sorted(states.get(discrete, set()))
    assert records == [(48, (4, 4, 4))]
    return state_counts, records


def main():
    print("INV-0006 / ASN-0014 independent phase-1 computation")

    print("\nV1")
    coin = {6: F(1, 8), 7: F(3, 8), 8: F(3, 8), 9: F(1, 8)}
    yarrow_standard = {6: F(1, 16), 7: F(5, 16),
                       8: F(7, 16), 9: F(3, 16)}
    print("coin law", coin)
    print("standard yarrow law", yarrow_standard)
    print("coin I(X;Y)", 6 * (1 - h2(0.25)))
    print("standard yarrow I(X;Y)",
          3 * (h2(F(3, 8)) - h2(F(1, 8))))
    print("standard yarrow I(X;E)",
          6 * (h2(F(1, 4))
               - (h2(F(1, 8)) + h2(F(3, 8))) / 2))

    print("\nV2")
    target = {6: F(1, 16), 7: F(5, 16), 8: F(7, 16), 9: F(3, 16)}
    for model in ("uniform", "binomial"):
        law = three_change_law(model)
        print(model)
        for value in (6, 7, 8, 9):
            print(value, law[value], float(law[value]),
                  "delta", float(law[value] - target[value]))
        print("primary yang", law[7] + law[9],
              float(law[7] + law[9]))

    print("\nV3")
    print("one-bit capacity", 1 - h2(0.25))

    print("\nV4 label checks and p=1/4 values")
    for name, function in LABELS.items():
        counts = Counter(function(x) for x in BITS6)
        assert sorted(counts.values()) == [8] * 8
        rigorous = mutual_information_interval(name, F(1, 4))
        print(name, mutual_information_numeric(function, 0.25),
              "rigorous enclosure", float(rigorous.lo), float(rigorous.hi))

    print("\nV4 rigorous sign certificates")
    for name, terms in (("T-B", TERMS_TB), ("B-G", TERMS_BG)):
        small = certify_small_p_derivative(terms)
        print(name, "small-p derivative lower bound", float(small[2]))
        central = certify_central_interval(terms)
        print(name, "central", central["intervals"], "intervals; max depth",
              central["max_depth"], "; min unnormalized natural-log margin",
              float(central["min_margin"]))
        high = certify_high_noise_second_derivative(terms)
        print(name, "rho second derivative enclosure",
              float(high.lo), float(high.hi))

    print("\nV5")
    for name, function in LABELS.items():
        print(name, "beta", beta(function), "W1", w1(function))
    print("D centroid", centroid(D), "squared norm",
          sum(z * z for z in centroid(D)))
    state_counts, records = centroid_extremum_partition_dp()
    print("centroid DP state/record counts by coordinate", state_counts)
    print("centroid DP final records at cost <=48", records)


if __name__ == "__main__":
    main()
