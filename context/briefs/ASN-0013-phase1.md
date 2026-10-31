---
id: brief-ASN-0013-phase1
assignment: ASN-0013
context_mode: targeted
contains: local claim statements, formal definitions and source theorem statement; no pilot code or derivations
created: 2026-10-31
---
# Reported formal claims to audit

All claims are unverified. You receive no original proofs or code in this phase. A separate manuscript states the Boolean-information inequality below; treat it as an explicit conditional premise for the general transfer, and independently check finite cases. This assignment does not ask you to verify an entire external manuscript from a statement alone.

## Definitions

X=(L,U) is uniform on {0,1}^{2k}; Y=X xor E with independent Bernoulli(p) noise, independent of X, 0≤p≤1/2. G(X)=L xor U and q=2p(1−p). Entropies are in bits. The imported premise is: for uniform independent Z and independent symmetric crossover r, any Boolean f has I(f(Z);Z xor noise)≤1−h₂(r), attained by a coordinate.

At k=3, coordinates are bottom-to-top. R reverses the six coordinates and C complements them. Use the formal difference words

    000000,100000,110000,111000,111100,111110,111010,000010.

For each x choose d with G(d)=G(x). If unique and x xor d=(B,B), call B the base label. This is a mathematical definition; correspondence to historical palace tables is not assigned here.

## Claims

**L1.** For all k and p as above, I(g(G(X));Y)=I(g(G(X));G(Y)) for every Boolean g. Conditional on the imported premise, its maximum is 1−h₂(q), attained by a coordinate of G. The raw-coordinate maximum benchmark is 1−h₂(p).

**L2.** At k=3, (B,G) is uniform on all 64 label pairs. At p=1/8 the reported information values are I(B;Y)=1.103576694734 and I(G;Y)=0.726364612385; at p=1/4 they are 0.378621055176 and 0.136697991225. The full G formula is 3[1−h₂(q)]. At each of these two parameters, exactly the six signed coordinate functions maximize the information among all 256 Boolean functions of G, within the numerical precision reported. Assess whether rigorous numerical bounds can certify the comparison.

**L3.** The simple undirected graph on six-bit words allowing an edge from x to Cx and to Rx when Rx≠x has exactly 4,096 perfect matchings. For 2k lines the claimed count is 2^(2^{2k−2}−2^{k−1}). This is not the number of received-order arrangements or a claim about historical probabilities.

**L4.** With margins (2,2), the three 2×2 tables have masses (1/3,1/3,1/3) under uniform tables and (1/6,2/3,1/6) under uniformly labelled allocations of two objects of each type to two rows of size two.

**L5.** A sweep of independent fair swaps along all six coordinate directions on 64 labelled positions gives every single label an exactly uniform endpoint. Its full-permutation total variation from uniform is nevertheless at least 1−2^192/64!, greater than 1−5×10^−32. The finite support obstruction forces at least ten physical layers to reach TV≤1/4. No finite upper-mixing claim is made.

**L6.** Every nonzero linear character evaluated along any complete enumeration of all 64 six-bit words is balanced. Its sign polynomial P satisfies P(1)=0, so it cannot have a strictly positive lower modulus everywhere on the unit circle. This does not exclude spectral comparisons away from 1 or aperiodic correlation questions.

For each claim independently derive, refute, or narrow it. State whether computations were executed. End with provisional verdicts and stop before the original evidence is supplied.
