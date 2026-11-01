#!/usr/bin/env python3
"""INV-0004: divination channels, Boolean information bounds, and robustness of hexagram labels.

Exploratory and computer-assisted computation for a full-context investigation (context-exposed;
not a verification). Python standard library only. Deterministic except for the seeded local
searches, whose seeds are recorded in the output.

Conventions: a hexagram is an integer x in [0, 64); bit i (i = 0..5) is line i+1 counted from the
bottom; yang = 1. Lower trigram L = lines 1-3 = x & 7, upper trigram U = lines 4-6 = x >> 3.

Models are stated explicitly; none is asserted to be a cited historical procedure:
  coins            three fair two-valued coins worth 2 or 3; line value = sum (6, 7, 8, 9)
  yarrow-standard  first change removes 5 or 9 stalks with probabilities 3/4, 1/4; second and
                   third changes remove 4 or 8 with probabilities 1/2, 1/2
  yarrow-uniform   49 stalks; each change splits n stalks with left heap L uniform on 1..n-1,
                   hangs one stalk from the right heap, counts both heaps by fours (remainder
                   1..4, an empty heap contributing 0)
  yarrow-binomial  as yarrow-uniform, but L ~ Binomial(n, 1/2) conditioned on 1 <= L <= n-1

Sections (keys of the JSON output):
  procedures      exact line-value laws and induced primary->changed channels
  ck_table        Courtade-Kumar bound (external family 119, conditional) vs exact values, coins
  dictator_scans  exhaustive search over all Boolean functions, n <= 4, all models, both directions
  dictator_n6     seeded local search over Boolean functions on six lines
  labels          trigram / palace / generation labels: exact structure, coefficients, values
  ordering_proof  computer-assisted proof of I(T;Y) > I(B;Y) > I(G;Y) for 0 < p < 1/2
  partition_search seeded local search over balanced eight-block labels
  inv0003_check   independent recomputation of INV-0003 L1-L6 and its supplement
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
import random
import sys
from fractions import Fraction as Fr

N = 64
LN2 = math.log(2.0)

# ----------------------------------------------------------------------------- encodings

def word(s):
    """Bottom-to-top 0/1 string -> integer."""
    return sum(int(c) << i for i, c in enumerate(s))


def popcount(x):
    return bin(x).count("1")


D_STRINGS = ["000000", "100000", "110000", "111000", "111100", "111110", "111010", "000010"]
D_WORDS = [word(s) for s in D_STRINGS]


def lower(x):
    return x & 7


def upper(x):
    return x >> 3


def gen_label(x):
    """G(x) = L xor U: which of the line pairs (1,4), (2,5), (3,6) differ."""
    return lower(x) ^ upper(x)


D_BY_G = {gen_label(d): d for d in D_WORDS}
assert len(D_BY_G) == 8


def palace_label(x):
    z = x ^ D_BY_G[gen_label(x)]
    assert lower(z) == upper(z)
    return lower(z)


def trigram_label(x):
    return lower(x)


LABELS = {
    "trigram": [trigram_label(x) for x in range(N)],
    "palace": [palace_label(x) for x in range(N)],
    "generation": [gen_label(x) for x in range(N)],
}

# ----------------------------------------------------------------------------- entropy helpers

def h2(p):
    """Binary entropy in bits (float argument)."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def plogp(q):
    """-q log2 q for an exact Fraction or float, accurate near 0 and 1."""
    if q <= 0 or q >= 1:
        return 0.0
    if isinstance(q, Fr) and q > Fr(1, 2):
        e = float(1 - q)
        return -(1.0 - e) * math.log1p(-e) / LN2
    qf = float(q)
    return -qf * math.log2(qf)


def entropy(probs):
    return sum(plogp(q) for q in probs)

# ----------------------------------------------------------------------------- procedures

def coin_values():
    dist = {}
    for c in itertools.product((2, 3), repeat=3):
        dist[sum(c)] = dist.get(sum(c), Fr(0)) + Fr(1, 8)
    return dist


def remainder(m):
    if m == 0:
        return 0
    r = m % 4
    return 4 if r == 0 else r


def split_law(n, kind):
    if kind == "uniform":
        return {L: Fr(1, n - 1) for L in range(1, n)}
    if kind == "binomial":
        w = {L: Fr(math.comb(n, L)) for L in range(1, n)}
        tot = sum(w.values())
        return {L: v / tot for L, v in w.items()}
    raise ValueError(kind)


def one_change(n, kind):
    out = {}
    for L, pr in split_law(n, kind).items():
        removed = 1 + remainder(L) + remainder(n - L - 1)
        out[removed] = out.get(removed, Fr(0)) + pr
    return out


def yarrow_values(kind):
    if kind == "standard":
        firsts = {5: Fr(3, 4), 9: Fr(1, 4)}
        later = {4: Fr(1, 2), 8: Fr(1, 2)}
        dist = {}
        for r1, a in firsts.items():
            for r2, b in later.items():
                for r3, c in later.items():
                    v = (49 - r1 - r2 - r3) // 4
                    dist[v] = dist.get(v, Fr(0)) + a * b * c
        return dist
    dist = {}

    def rec(n, depth, pr):
        if depth == 3:
            assert n % 4 == 0
            dist[n // 4] = dist.get(n // 4, Fr(0)) + pr
            return
        law = one_change(n, kind)
        allowed = {5, 9} if depth == 0 else {4, 8}
        assert set(law) <= allowed, (n, depth, law)
        for r, q in law.items():
            rec(n - r, depth + 1, pr * q)

    rec(49, 0, Fr(1))
    return dist


def line_channel(values):
    """From P(6..9): primary yang prob pi, a = P(change | yang), b = P(change | yin)."""
    p6, p7, p8, p9 = (values.get(v, Fr(0)) for v in (6, 7, 8, 9))
    assert p6 + p7 + p8 + p9 == 1
    pi = p7 + p9
    return {"P6": p6, "P7": p7, "P8": p8, "P9": p9, "pi": pi,
            "a": p9 / pi, "b": p6 / (1 - pi), "changed_yang": p7 + p6, "change": p6 + p9}


def per_line_info(ch):
    pi, a, b = ch["pi"], ch["a"], ch["b"]
    # joint law of (X, Y) for one line
    j = {(1, 1): pi * (1 - a), (1, 0): pi * a, (0, 1): (1 - pi) * b, (0, 0): (1 - pi) * (1 - b)}
    py1 = j[(1, 1)] + j[(0, 1)]
    i_xy = entropy([pi, 1 - pi]) + entropy([py1, 1 - py1]) - entropy(list(j.values()))
    # X versus change indicator E
    pe1 = pi * a + (1 - pi) * b
    je = [pi * a, pi * (1 - a), (1 - pi) * b, (1 - pi) * (1 - b)]
    i_xe = entropy([pi, 1 - pi]) + entropy([pe1, 1 - pe1]) - entropy(je)
    h_v = entropy([ch["P6"], ch["P7"], ch["P8"], ch["P9"]])
    return {"I_primary_changed": i_xy, "I_primary_changemask": i_xe, "H_line_value": h_v}


def product_joint(ch, n=6):
    """Joint law J[x][y] of primary and changed hexagram (n lines), exact Fractions."""
    pi, a, b = ch["pi"], ch["a"], ch["b"]
    one = {(1, 1): pi * (1 - a), (1, 0): pi * a, (0, 1): (1 - pi) * b, (0, 0): (1 - pi) * (1 - b)}
    size = 1 << n
    J = [[Fr(1)] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            w = Fr(1)
            for i in range(n):
                w *= one[((x >> i) & 1, (y >> i) & 1)]
            J[x][y] = w
    return J


def bsc_joint(p, n=6):
    size = 1 << n
    return [[(p ** popcount(x ^ y)) * ((1 - p) ** (n - popcount(x ^ y))) / size for y in range(size)]
            for x in range(size)]

# ----------------------------------------------------------------------------- information of functions

def boolean_info(J, f_set):
    """I(f(In); Out) in bits for the indicator of the input set f_set, joint J[in][out] (floats)."""
    n_out = len(J[0])
    pin = [sum(r) for r in J]
    pout = [sum(J[i][o] for i in range(len(J))) for o in range(n_out)]
    alpha = sum(pin[i] for i in f_set)
    tot = h2(alpha)
    for o in range(n_out):
        p1 = sum(J[i][o] for i in f_set)
        tot -= pout[o] * h2(p1 / pout[o])
    return tot


def label_info(J, labels):
    """I(lambda(In); Out) in bits; J may hold Fractions (exact masses) or floats."""
    n_in, n_out = len(J), len(J[0])
    K = max(labels) + 1
    rows = [[0] * n_out for _ in range(K)]
    for i in range(n_in):
        r = rows[labels[i]]
        Ji = J[i]
        for o in range(n_out):
            r[o] += Ji[o]
    pk = [sum(r) for r in rows]
    pout = [sum(rows[k][o] for k in range(K)) for o in range(n_out)]
    tot = 0.0
    for k in range(K):
        for o in range(n_out):
            m = rows[k][o]
            if m:
                tot += float(m) * math.log2(float(m) / (float(pk[k]) * float(pout[o])))
    return tot


def cond_entropy_label_bsc(labels, p, profile):
    """H(lambda(X) | Y) in bits for BSC(p), p an exact Fraction, using distance profiles."""
    w = [(p ** d) * ((1 - p) ** (6 - d)) for d in range(7)]
    tot = 0.0
    for y in range(N):
        prof = profile[y]
        for k in range(len(prof)):
            q = sum(prof[k][d] * w[d] for d in range(7))
            tot += plogp(q)
    return tot / N


def distance_profiles(labels):
    K = max(labels) + 1
    prof = []
    for y in range(N):
        rows = [[0] * 7 for _ in range(K)]
        for x in range(N):
            rows[labels[x]][popcount(x ^ y)] += 1
        prof.append(rows)
    return prof

# ----------------------------------------------------------------------------- section: procedures

def section_procedures():
    models = {"coins": coin_values(), "yarrow-standard": yarrow_values("standard"),
              "yarrow-uniform": yarrow_values("uniform"), "yarrow-binomial": yarrow_values("binomial")}
    out = {}
    channels = {}
    for name, vals in models.items():
        ch = line_channel(vals)
        channels[name] = ch
        info = per_line_info(ch)
        out[name] = {
            "line_values": {str(k): str(v) for k, v in sorted(vals.items())},
            "line_values_float": {str(k): float(v) for k, v in sorted(vals.items())},
            "primary_yang": str(ch["pi"]), "change_given_yang": str(ch["a"]),
            "change_given_yin": str(ch["b"]), "changed_yang": str(ch["changed_yang"]),
            "change_probability": str(ch["change"]),
            "per_line": info,
            "six_lines": {k: 6 * v for k, v in info.items()},
            "symmetric_channel": ch["a"] == ch["b"],
            "primary_uniform": ch["pi"] == Fr(1, 2),
        }
    return out, channels

# ----------------------------------------------------------------------------- section: CK table

def psi(r):
    """psi(r) = log 2 - H(r) in nats, H(r) the entropy of a sign of mean r."""
    def term(t):
        return 0.0 if t <= 0 else -t * math.log(t)
    return LN2 - (term((1 + r) / 2) + term((1 - r) / 2))


def psi_inv(v):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if psi(mid) < v:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ck_bounds(alpha, rho):
    m = 2 * alpha - 1
    H_m = LN2 - psi(m)                      # entropy of the output (nats)
    r_m = psi_inv(H_m)
    return psi(abs(rho) * r_m) / LN2, psi(abs(rho)) / LN2


OBSERVABLES = {
    "line 1 is yang": lambda x: x & 1,
    "line 6 is yang": lambda x: (x >> 5) & 1,
    "lower and upper trigram equal": lambda x: int(lower(x) == upper(x)),
    "palace label equals 000": lambda x: int(palace_label(x) == 0),
    "generation label equals 111 (all three line pairs differ)": lambda x: int(gen_label(x) == 7),
    "at least four yang lines": lambda x: int(popcount(x) >= 4),
    "exactly three yang lines": lambda x: int(popcount(x) == 3),
    "lower trigram has at least two yang lines": lambda x: int(popcount(lower(x)) >= 2),
    "reading the figure top-to-bottom gives the same figure": lambda x: int(all(((x >> i) & 1) == ((x >> (5 - i)) & 1) for i in range(3))),
    "odd number of yang lines": lambda x: popcount(x) & 1,
}


def section_ck(channels):
    Jc = product_joint(channels["coins"])
    Jy = product_joint(channels["yarrow-standard"])
    Jcf = [[float(v) for v in r] for r in Jc]
    Jyf = [[float(v) for v in r] for r in Jy]
    Jyb = [list(col) for col in zip(*Jyf)]   # questions about the changed hexagram
    rows = []
    rho = 0.5
    for name, fn in OBSERVABLES.items():
        f = [x for x in range(N) if fn(x)]
        alpha = len(f) / N
        refined, universal = ck_bounds(alpha, rho)
        fy = [y for y in range(N) if fn(y)]
        rows.append({
            "observable": name, "ones": len(f), "mean_pm1": 2 * alpha - 1,
            "coins_I_bits": boolean_info(Jcf, f), "ck_universal_bits": universal,
            "ck_refined_bits": refined,
            "yarrow_primary_question_I_bits": boolean_info(Jyf, f),
            "yarrow_changed_question_I_bits": boolean_info(Jyb, fy),
        })
    return {"rho": rho, "p": 0.25, "rows": rows,
            "note": "Bounds are conditional on Corollary main:ck of external family 119 (uniform input, "
                    "independent symmetric noise). They do not apply to the yarrow columns."}

# ----------------------------------------------------------------------------- section: dictator scans

def gray_scan(J):
    """Exhaustive scan over all nonconstant Boolean functions of the input of joint J (floats)."""
    n_in, n_out = len(J), len(J[0])
    pin = [sum(r) for r in J]
    pout = [sum(J[i][o] for i in range(n_in)) for o in range(n_out)]
    p1 = [0.0] * n_out
    alpha = 0.0
    member = [0] * n_in
    best = []
    total = 1 << n_in
    for i in range(1, total):
        bit = (i & -i).bit_length() - 1
        sgn = -1.0 if member[bit] else 1.0
        member[bit] ^= 1
        alpha += sgn * pin[bit]
        Jb = J[bit]
        for o in range(n_out):
            p1[o] += sgn * Jb[o]
        g = i ^ (i >> 1)
        if g == total - 1:
            continue
        val = h2(alpha)
        for o in range(n_out):
            po = pout[o]
            val -= po * h2(p1[o] / po)
        best.append((val, g))
    best.sort(reverse=True)
    return best


def dictator_sets(n):
    return [frozenset(x for x in range(1 << n) if (x >> j) & 1) for j in range(n)]


def scan_summary(J, n):
    res = gray_scan(J)
    dsets = dictator_sets(n)
    dict_masks = set()
    for s in dsets:
        m = sum(1 << x for x in s)
        dict_masks.add(m)
        dict_masks.add(((1 << (1 << n)) - 1) ^ m)
    best_val = res[0][0]
    dict_best = max(v for v, g in res if g in dict_masks)
    nondict = [(v, g) for v, g in res if g not in dict_masks]
    top_nd = nondict[0] if nondict else (None, None)
    attaining = [g for v, g in res if v >= best_val - 1e-12]
    return {"n": n, "functions_scanned": len(res), "max_I_bits": best_val,
            "best_dictator_I_bits": dict_best,
            "max_attained_only_by_signed_coordinates": all(g in dict_masks for g in attaining),
            "functions_attaining_max": len(attaining),
            "best_non_coordinate_I_bits": top_nd[0],
            "best_non_coordinate_truth_table": None if top_nd[1] is None else format(top_nd[1], "0%db" % (1 << n)),
            "gap_bits": None if top_nd[0] is None else best_val - top_nd[0]}


def section_dictator_scans(channels, nmax):
    out = {}
    for name, ch in channels.items():
        for n in range(1, nmax + 1):
            J = [[float(v) for v in r] for r in product_joint(ch, n)]
            Jb = [list(col) for col in zip(*J)]
            out["%s|n=%d|primary-question" % (name, n)] = scan_summary(J, n)
            out["%s|n=%d|changed-question" % (name, n)] = scan_summary(Jb, n)
    return out

# ----------------------------------------------------------------------------- section: n = 6 local search

def hill_climb_boolean(J, start, rng, max_rounds=200):
    n_in, n_out = len(J), len(J[0])
    pin = [sum(r) for r in J]
    pout = [sum(J[i][o] for i in range(n_in)) for o in range(n_out)]
    member = list(start)
    alpha = sum(pin[i] for i in range(n_in) if member[i])
    p1 = [sum(J[i][o] for i in range(n_in) if member[i]) for o in range(n_out)]

    def value(al, pp):
        if al <= 1e-15 or al >= 1 - 1e-15:
            return -1.0
        v = h2(al)
        for o in range(n_out):
            v -= pout[o] * h2(pp[o] / pout[o])
        return v

    cur = value(alpha, p1)
    for _ in range(max_rounds):
        improved = False
        order = list(range(n_in))
        rng.shuffle(order)
        for x in order:
            sgn = -1.0 if member[x] else 1.0
            na = alpha + sgn * pin[x]
            npp = [p1[o] + sgn * J[x][o] for o in range(n_out)]
            v = value(na, npp)
            if v > cur + 1e-13:
                member[x] ^= 1
                alpha, p1, cur = na, npp, v
                improved = True
        if not improved:
            break
    return cur, member


def section_dictator_n6(channels, starts, seed):
    rng = random.Random(seed)
    out = {}
    for name in ("yarrow-standard", "yarrow-uniform"):
        J = [[float(v) for v in r] for r in product_joint(channels[name])]
        for direction, M in (("primary-question", J), ("changed-question", [list(c) for c in zip(*J)])):
            dvals = [boolean_info(M, [x for x in range(N) if (x >> j) & 1]) for j in range(6)]
            structured = {
                "majority>=4": [int(popcount(x) >= 4) for x in range(N)],
                "majority>=3": [int(popcount(x) >= 3) for x in range(N)],
                "and(1,2)": [int((x & 3) == 3) for x in range(N)],
                "or(1,2)": [int((x & 3) != 0) for x in range(N)],
                "all-yang-or-1": [int(popcount(x) >= 5) for x in range(N)],
            }
            best = (-1.0, None, None)
            for label, st in structured.items():
                v, m = hill_climb_boolean(M, st, rng)
                if v > best[0]:
                    best = (v, label, m)
            for s in range(starts):
                dens = rng.choice([0.5, 0.25, 0.125, 0.75, rng.random()])
                st = [int(rng.random() < dens) for _ in range(N)]
                if sum(st) in (0, N):
                    continue
                v, m = hill_climb_boolean(M, st, rng)
                if v > best[0]:
                    best = (v, "random-%d" % s, m)
            is_coord = any(best[2] == [((x >> j) & 1) ^ c for x in range(N)] for j in range(6) for c in (0, 1))
            out["%s|%s" % (name, direction)] = {
                "best_coordinate_I_bits": max(dvals), "local_search_best_I_bits": best[0],
                "local_search_best_is_signed_coordinate": is_coord, "starts": starts + len(structured),
                "best_start": best[1]}
    return out

# ----------------------------------------------------------------------------- section: labels

def fourier_levels(labels):
    """W_j = sum_k sum_{|S|=j} fhat_k(S)^2 / pi_k (exact Fractions), and C = max_{k,y} sum_S |fhat_k(S)|/pi_k."""
    K = max(labels) + 1
    W = [Fr(0)] * 7
    absum = []
    for k in range(K):
        A = [x for x in range(N) if labels[x] == k]
        pi = Fr(len(A), N)
        tot_abs = Fr(0)
        for S in range(1, N):
            c = Fr(sum(1 if popcount(S & x) % 2 == 0 else -1 for x in A), N)
            W[popcount(S)] += c * c / pi
            tot_abs += abs(c) / pi
        absum.append(tot_abs)
    return W, max(absum)


def edge_structure(labels):
    K = max(labels) + 1
    internal = [0] * K
    boundary_degree = [0] * N
    for x in range(N):
        for i in range(6):
            y = x ^ (1 << i)
            if labels[y] == labels[x]:
                if x < y:
                    internal[labels[x]] += 1
            else:
                boundary_degree[x] += 1
    return internal, boundary_degree


def max_level1_weight(size):
    """max over subsets A of {0,1}^6 with |A| = size of ||s(A)||^2, s_i(A) = sum_{x in A} (-1)^{x_i}.

    Equals max over nonzero u of T(u)^2 / ||u||^2, T(u) = sum of the `size` largest <chi(x), u>; the
    maximizer's own s(A) is an integer vector, so up to signed permutations it suffices to range over
    sorted nonnegative integer vectors with entries congruent to size mod 2 in [0, size]."""
    chis = [[1 - 2 * ((x >> i) & 1) for i in range(6)] for x in range(N)]
    vals = [v for v in range(0, size + 1) if (v - size) % 2 == 0]
    best = Fr(-1)
    arg = []
    for u in itertools.combinations_with_replacement(vals, 6):
        nu = sum(c * c for c in u)
        if nu == 0:
            continue
        dots = sorted((sum(c * u[i] for i, c in enumerate(ch)) for ch in chis), reverse=True)
        t = sum(dots[:size])
        val = Fr(t * t, nu)
        if val > best:
            best, arg = val, [u]
        elif val == best:
            arg.append(u)
    return best, arg


def section_labels(channels):
    out = {}
    Jc = product_joint(channels["coins"])
    Jy = {m: product_joint(channels[m]) for m in ("yarrow-standard", "yarrow-uniform", "yarrow-binomial")}
    for name, lab in LABELS.items():
        internal, bdeg = edge_structure(lab)
        W, C = fourier_levels(lab)
        beta = Fr(sum(bdeg), N)
        sizes = [lab.count(k) for k in range(8)]
        entry = {
            "block_sizes": sizes, "internal_edges_per_block": internal,
            "boundary_edges": sum(bdeg) // 2, "mean_boundary_degree_beta": str(beta),
            "boundary_degree_distribution": {str(d): bdeg.count(d) for d in sorted(set(bdeg))},
            "fourier_levels_W": [str(w) for w in W], "W1": str(W[1]), "C_abs_fourier": str(C),
            "values": {},
        }
        for p in (Fr(1, 8), Fr(1, 4)):
            entry["values"]["coins-type BSC p=%s" % p] = label_info(bsc_joint(p), lab)
        entry["values"]["coins"] = label_info(Jc, lab)
        for m, J in Jy.items():
            entry["values"][m] = label_info(J, lab)
            entry["values"][m + " (questions about changed hexagram)"] = label_info([list(c) for c in zip(*J)], lab)
        out[name] = entry
    best192, arg = max_level1_weight(8)
    out["max_level1_weight_8_sets"] = {"max_norm_sq": str(best192), "maximizing_directions": [list(u) for u in arg],
                                       "subcube_value": 3 * 64}
    # an interior sweep (floats) for the record
    sweep = []
    profs = {name: distance_profiles(lab) for name, lab in LABELS.items()}
    for j in range(1, 50):
        p = Fr(j, 100)
        row = {"p": float(p)}
        for name in LABELS:
            row[name] = 3.0 - cond_entropy_label_bsc(LABELS[name], p, profs[name])
        sweep.append(row)
    out["sweep_bsc"] = sweep
    return out

# ----------------------------------------------------------------------------- section: ordering proof

def phi_lower(rho):
    return rho * rho / (2 * LN2)


def section_ordering_proof(margin=1e-10):
    """Computer-assisted proof that, for X uniform and Y = X xor BSC(p) noise, 0 < p < 1/2,
    I(T;Y) > I(B;Y) > I(G;Y).  Three regions per comparison; see the report for derivations."""
    profs = {name: distance_profiles(lab) for name, lab in LABELS.items()}
    labT, labB, labG = LABELS["trigram"], LABELS["palace"], LABELS["generation"]
    internal, bdeg = edge_structure(labB)
    assert sum(internal) == 64 and sum(bdeg) == 256
    res = {"margin": margin}

    # ---- B versus G
    # Region A: p <= 2^-10, Fano bound on H(B|Y) against H(G|Y) = 3 h(2p(1-p)).
    # Requirement (derived in the report): 6(1-p)(L-1) > (4+10p)(L + log2(7e/(4+10p))) for L = log2(1/p).
    pA = 2.0 ** -10
    c4 = 4 + 10 * pA
    slope = 6 * (1 - pA) - c4
    need = (6 * (1 - pA) + c4 * math.log2(7 * math.e / 4)) / slope
    regionA_BG = {"p_max": pA, "slope_positive": slope > 0, "L_threshold": need, "holds": slope > 0 and need < 10}
    # Region C: p >= 0.23, I(B;Y) >= 1 - h(p) (line 6 is a function of B) and I(G;Y) = 3(1 - h(q)).
    # Requirement: rho^4 + 3 rho^2 - 1 < 0, rho = 1 - 2p.
    rhoC = 1 - 2 * 0.23
    regionC_BG = {"p_min": 0.23, "rho_max": rhoC, "holds": rhoC ** 4 + 3 * rhoC ** 2 - 1 < 0,
                  "line6_is_function_of_B": all(((x >> 5) & 1) == ((labB[x] >> 2) & 1) for x in range(N))}
    # Region B: monotone grid on [2^-10, 0.23].
    grid = [Fr(1, 1024)]
    while grid[-1] < Fr(23, 100):
        grid.append(min(grid[-1] * Fr(6, 5), Fr(23, 100)))
    ok = True
    worst = None
    for a, b in zip(grid, grid[1:]):
        hB = cond_entropy_label_bsc(labB, b, profs["palace"])        # H(B|Y) at right end (upper bound)
        hG = cond_entropy_label_bsc(labG, a, profs["generation"])    # H(G|Y) at left end (lower bound)
        gap = hG - hB
        if worst is None or gap < worst[0]:
            worst = (gap, float(a), float(b))
        if gap <= margin:
            ok = False
    res["B_vs_G"] = {"regionA": regionA_BG, "regionC": regionC_BG,
                     "regionB": {"intervals": len(grid) - 1, "all_hold": ok, "smallest_gap": worst[0],
                                 "at_interval": worst[1:]},
                     "proved": regionA_BG["holds"] and regionC_BG["holds"] and ok}

    # ---- T versus B
    # Region A: p <= 2^-14: H(B|Y) >= P(|E|<=1) avg_y h(m_y p/(1+5p)) and H(T|Y) = 3 h(p).
    # Requirement: (1-5p)(4L - c1) > 3(L + log2 e), c1 = avg_y m_y log2 m_y.
    c1 = sum(m * math.log2(m) for m in bdeg) / N
    pA2 = 2.0 ** -14
    slope2 = 4 * (1 - 5 * pA2) - 3
    need2 = ((1 - 5 * pA2) * c1 + 3 / LN2) / slope2
    regionA_TB = {"p_max": pA2, "c1": c1, "slope_positive": slope2 > 0, "L_threshold": need2,
                  "holds": slope2 > 0 and need2 < 14}
    # Region C: high noise.  I(T;Y) >= 3 rho^2/(2 ln 2); I(B;Y) <= chi2_B(rho) / (2 ln 2 (1 - C rho)).
    W, C = fourier_levels(labB)
    Wf = [float(w) for w in W]
    Cf = float(C)

    def tb_high_ok(rho):
        chi2 = sum(Wf[j] * rho ** (2 * j) for j in range(1, 7))
        return C * rho < 1 and 3 * rho * rho * (1 - Cf * rho) > chi2

    rho_hi = 0.0
    step = 1e-4
    while tb_high_ok(rho_hi + step):
        rho_hi += step
    pC2 = (1 - rho_hi) / 2
    regionC_TB = {"rho_max": rho_hi, "p_min": pC2, "C": Cf, "W": Wf,
                  "holds": rho_hi > 0 and all(tb_high_ok(r * rho_hi / 1000) for r in range(1, 1001))}
    # Region B: monotone grid on [2^-14, pC2 rounded up].
    p_top = Fr(math.ceil(pC2 * 10000) + 1, 10000)
    grid = [Fr(1, 2 ** 14)]
    while grid[-1] < p_top:
        nxt = grid[-1] * Fr(9, 8)
        if nxt > Fr(1, 20):
            nxt = grid[-1] + Fr(1, 400)
        grid.append(min(nxt, p_top))
    ok = True
    worst = None
    for a, b in zip(grid, grid[1:]):
        hT = cond_entropy_label_bsc(labT, b, profs["trigram"])
        hB = cond_entropy_label_bsc(labB, a, profs["palace"])
        gap = hB - hT
        if worst is None or gap < worst[0]:
            worst = (gap, float(a), float(b))
        if gap <= margin:
            ok = False
    res["T_vs_B"] = {"regionA": regionA_TB, "regionC": regionC_TB,
                     "regionB": {"p_top": float(p_top), "intervals": len(grid) - 1, "all_hold": ok,
                                 "smallest_gap": worst[0], "at_interval": worst[1:]},
                     "covers": float(p_top) >= pC2,
                     "proved": regionA_TB["holds"] and regionC_TB["holds"] and ok and float(p_top) >= pC2}
    return res

# ----------------------------------------------------------------------------- section: partitions

def partition_search(J, iters, seed, start=None, T0=0.05):
    rng = random.Random(seed)
    n_out = len(J[0])
    pout = [sum(J[i][o] for i in range(N)) for o in range(n_out)]
    lab = list(start) if start else sum([[k] * 8 for k in range(8)], [])
    if not start:
        rng.shuffle(lab)
    rows = [[0.0] * n_out for _ in range(8)]
    for x in range(N):
        for o in range(n_out):
            rows[lab[x]][o] += J[x][o]
    pk = [sum(r) for r in rows]

    def contrib(k):
        r, s = rows[k], pk[k]
        return sum(m * math.log2(m / (s * pout[o])) for o, m in enumerate(r) if m > 0)

    cs = [contrib(k) for k in range(8)]
    cur = sum(cs)
    best = (cur, list(lab))
    T = T0
    decay = (1e-4 / T0) ** (1.0 / max(iters, 1))
    for _ in range(iters):
        i, j = rng.randrange(N), rng.randrange(N)
        ki, kj = lab[i], lab[j]
        if ki == kj:
            continue
        Ji, Jj = J[i], J[j]
        for o in range(n_out):
            d = Jj[o] - Ji[o]
            rows[ki][o] += d
            rows[kj][o] -= d
        pk[ki] += sum(Jj) - sum(Ji)
        pk[kj] -= sum(Jj) - sum(Ji)
        ci, cj = contrib(ki), contrib(kj)
        new = cur - cs[ki] - cs[kj] + ci + cj
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            lab[i], lab[j] = kj, ki
            cs[ki], cs[kj] = ci, cj
            cur = new
            if cur > best[0]:
                best = (cur, list(lab))
        else:
            for o in range(n_out):
                d = Jj[o] - Ji[o]
                rows[ki][o] -= d
                rows[kj][o] += d
            pk[ki] -= sum(Jj) - sum(Ji)
            pk[kj] += sum(Jj) - sum(Ji)
        T *= decay
    return best


def is_affine_block(block):
    b0 = block[0]
    S = {x ^ b0 for x in block}
    return all((a ^ b) in S for a in S for b in S)


def best_single_swap(J, lab):
    """Largest change in I(lambda; Out) over all swaps of two inputs between different blocks."""
    base = label_info(J, lab)
    best = None
    for i in range(N):
        for j in range(i + 1, N):
            if lab[i] == lab[j]:
                continue
            new = list(lab)
            new[i], new[j] = lab[j], lab[i]
            d = label_info(J, new) - base
            if best is None or d > best:
                best = d
    return best


def section_partitions(channels, iters, restarts, seed):
    out = {}
    targets = {"coins": [[float(v) for v in r] for r in product_joint(channels["coins"])],
               "bsc p=1/10": [[float(v) for v in r] for r in bsc_joint(Fr(1, 10))],
               "yarrow-standard": [[float(v) for v in r] for r in product_joint(channels["yarrow-standard"])]}
    for name, J in targets.items():
        ref = {lbl: label_info(J, lab) for lbl, lab in LABELS.items()}
        best = None
        runs = []
        for r in range(restarts):
            start = LABELS["palace"] if r == 0 else None
            v, lab = partition_search(J, iters, seed + r, start=start)
            runs.append({"seed": seed + r, "start": "palace" if start else "random", "best_I_bits": v})
            if best is None or v > best[0]:
                best = (v, lab, seed + r)
        blocks = [sorted(x for x in range(N) if best[1][x] == k) for k in range(8)]
        out[name] = {"reference": ref, "best_found_I_bits": best[0], "best_seed": best[2],
                     "best_minus_trigram": best[0] - ref["trigram"],
                     "best_blocks_affine": [is_affine_block(b) for b in blocks],
                     "runs": runs, "iterations": iters, "restarts": restarts,
                     "trigram_best_single_swap_change": best_single_swap(J, LABELS["trigram"])}
    return out

# ----------------------------------------------------------------------------- section: INV-0003 check

def count_matchings(adj, vertices):
    """Count perfect matchings of the induced graph by component-wise recursion (small components)."""
    seen, total = set(), 1
    for v in vertices:
        if v in seen:
            continue
        comp, stack = [], [v]
        seen.add(v)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)

        def rec(rem):
            if not rem:
                return 1
            u = min(rem)
            return sum(rec(rem - {u, w}) for w in adj[u] if w in rem)
        total *= rec(frozenset(comp))
    return total


def section_inv0003():
    out = {}
    # L1: reduction and optimum over all 256 functions of G, p = 1/8 and 1/4
    for p in (Fr(1, 8), Fr(1, 4)):
        J = [[float(v) for v in r] for r in bsc_joint(p)]
        q = float(2 * p * (1 - p))
        bound = 1 - h2(q)
        vals, red = [], 0.0
        Gy = [gen_label(y) for y in range(N)]
        for g in range(1, 255):
            f = [x for x in range(N) if (g >> gen_label(x)) & 1]
            v = boolean_info(J, f)
            # I(g(G(X)); G(Y)): joint of g(G(X)) with G(Y)
            joint = {}
            for x in range(N):
                for y in range(N):
                    key = ((g >> gen_label(x)) & 1, Gy[y])
                    joint[key] = joint.get(key, 0.0) + J[x][y]
            pa = {}
            pb = {}
            for (a_, b_), m in joint.items():
                pa[a_] = pa.get(a_, 0.0) + m
                pb[b_] = pb.get(b_, 0.0) + m
            vr = sum(m * math.log2(m / (pa[a_] * pb[b_])) for (a_, b_), m in joint.items() if m > 0)
            red = max(red, abs(v - vr))
            vals.append((v, g))
        vals.sort(reverse=True)
        attaining = [g for v, g in vals if v >= vals[0][0] - 1e-12]
        out["L1 p=%s" % p] = {"max_I": vals[0][0], "bound_1_minus_h_q": bound,
                              "max_abs_reduction_discrepancy": red, "functions_attaining": len(attaining)}
    # L2 values
    for p in (Fr(1, 8), Fr(1, 4)):
        J = bsc_joint(p)
        out["L2 p=%s" % p] = {"B": label_info(J, LABELS["palace"]), "G": label_info(J, LABELS["generation"]),
                              "G_formula": 3 * (1 - h2(float(2 * p * (1 - p))))}
    pairs = {(LABELS["palace"][x], LABELS["generation"][x]) for x in range(N)}
    out["L2 independence (all 64 pairs occur once)"] = len(pairs) == 64
    # L3: matchings of the reversal/complement graph, 2k lines
    l3 = {}
    for k in range(1, 6):
        n = 2 * k
        size = 1 << n
        rev = lambda x: int(format(x, "0%db" % n)[::-1], 2)
        adj = {x: set() for x in range(size)}
        for x in range(size):
            c = x ^ (size - 1)
            adj[x].add(c)
            adj[c].add(x)
            r = rev(x)
            if r != x:
                adj[x].add(r)
                adj[r].add(x)
        cnt = count_matchings(adj, range(size))
        formula = 2 ** (2 ** (2 * k - 2) - 2 ** (k - 1))
        l3["k=%d" % k] = {"count": str(cnt) if cnt > 10 ** 15 else cnt, "formula_agrees": cnt == formula}
    out["L3"] = l3
    # L4: allocation multiplicities for margins (2,2)
    mult = [math.comb(2, a) * math.comb(2, 2 - a) for a in range(3)]
    out["L4"] = {"multiplicities": mult, "extreme_event_uniform_table": "2/3",
                 "extreme_event_allocation": str(Fr(mult[0] + mult[2], sum(mult)))}
    # L5: exact one-sweep marginals and the support bound
    marg_ok = True
    for start in range(N):
        dist = {start: Fr(1)}
        for i in range(6):
            nd = {}
            for pos, pr in dist.items():
                for tgt in (pos, pos ^ (1 << i)):
                    nd[tgt] = nd.get(tgt, Fr(0)) + pr / 2
            dist = nd
        marg_ok &= len(dist) == N and all(v == Fr(1, N) for v in dist.values())
    log2fact = math.log2(math.factorial(64))
    out["L5"] = {"one_sweep_marginals_uniform": marg_ok, "log2_64_factorial": log2fact,
                 "log2_support_over_64_factorial": 192 - log2fact,
                 "min_physical_shuffles_for_tv_quarter": math.ceil((log2fact + math.log2(0.75)) / 32)}
    # L6: balanced characters
    out["L6"] = {"all_nonzero_characters_balanced": all(sum(1 if popcount(a & x) % 2 == 0 else -1 for x in range(N)) == 0
                                                        for a in range(1, N))}
    # Supplement: majorization counterexample at p = 1/8, y = 0
    p = Fr(1, 8)
    post_B, post_G = [Fr(0)] * 8, [Fr(0)] * 8
    for x in range(N):
        w = (p ** popcount(x)) * ((1 - p) ** (6 - popcount(x)))
        post_B[LABELS["palace"][x]] += w
        post_G[LABELS["generation"][x]] += w
    sB = sorted(post_B, reverse=True)
    sG = sorted(post_G, reverse=True)
    out["supplement"] = {"sorted_B": [str(v) for v in sB], "sorted_G": [str(v) for v in sG],
                         "top4_B": str(sum(sB[:4])), "top4_G": str(sum(sG[:4])),
                         "B_majorizes_G_fails": sum(sB[:4]) < sum(sG[:4])}
    return out

# ----------------------------------------------------------------------------- main

def to_jsonable(o):
    if isinstance(o, Fr):
        return str(o)
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    return o


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", required=True)
    ap.add_argument("--nmax", type=int, default=4)
    ap.add_argument("--starts", type=int, default=60)
    ap.add_argument("--iters", type=int, default=60000)
    ap.add_argument("--restarts", type=int, default=4)
    ap.add_argument("--seed", type=int, default=20261031)
    args = ap.parse_args()
    results = {"python": platform.python_version(), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
               "parameters": vars(args)}
    procs, channels = section_procedures()
    results["procedures"] = procs
    print("procedures done", flush=True)
    results["ck_table"] = section_ck(channels)
    print("ck done", flush=True)
    results["inv0003_check"] = section_inv0003()
    print("inv0003 check done", flush=True)
    results["labels"] = section_labels(channels)
    print("labels done", flush=True)
    results["ordering_proof"] = section_ordering_proof()
    print("ordering proof done", flush=True)
    results["dictator_scans"] = section_dictator_scans(channels, args.nmax)
    print("dictator scans done", flush=True)
    results["dictator_n6"] = section_dictator_n6(channels, args.starts, args.seed)
    print("n6 search done", flush=True)
    results["partition_search"] = section_partitions(channels, args.iters, args.restarts, args.seed)
    print("partition search done", flush=True)
    with open(args.out, "w") as fh:
        json.dump(to_jsonable(results), fh, indent=1, sort_keys=True)
        fh.write("\n")


if __name__ == "__main__":
    sys.exit(main())
