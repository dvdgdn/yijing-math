#!/usr/bin/env python3
"""Exact counterexample to a sufficient proof strategy, not to an entropy claim."""
from fractions import Fraction as F

words = ['000000','100000','110000','111000','111100','111110','111010','000010']
differences = [sum(int(bit) << i for i, bit in enumerate(s)) for s in words]
def phi(x):
    return (x & 7) ^ (x >> 3)
representatives = {phi(d): d for d in differences}
base = [(x ^ representatives[phi(x)]) & 7 for x in range(64)]
p = F(1,8)
weights = [p**h*(1-p)**(6-h) for h in range(7)]
q = 2*p*(1-p)
posterior_base = sorted([sum(weights[bin(x).count('1')] for x in range(64) if base[x] == b)
                         for b in range(8)], reverse=True)
posterior_difference = sorted([q**bin(g).count('1')*(1-q)**(3-bin(g).count('1'))
                               for g in range(8)], reverse=True)
assert sum(posterior_base) == sum(posterior_difference) == 1
assert sum(posterior_base[:4]) == F(7,8)
assert sum(posterior_difference[:4]) == F(14375,16384)
assert sum(posterior_base[:4]) < sum(posterior_difference[:4])
print('At p=1/8 and Y=0, the base posterior does not majorize the difference posterior.')
print('Top-four masses:',sum(posterior_base[:4]),'<',sum(posterior_difference[:4]))
print('This rules out the pointwise-majorization proof route; it does not refute an average entropy comparison.')
