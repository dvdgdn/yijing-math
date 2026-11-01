---
id: brief-ASN-0014-phase1
assignment: ASN-0014
context_mode: targeted
contains: claim statements and model definitions only; no proofs, code or numerical output from the originating report
created: 2026-10-31
---
# Reported claims to verify (phase 1)

All statements below are reported by an earlier investigation and are unverified. You receive no proofs, code or output in this phase.

## Conventions and models

A hexagram is x = (x₁, …, x₆) ∈ {0,1}⁶ read bottom to top, yang = 1; L = (x₁, x₂, x₃), U = (x₄, x₅, x₆). Each procedure model generates six line values in {6, 7, 8, 9} independently. Value v gives the primary line X (yang iff v ∈ {7, 9}) and a change bit E (iff v ∈ {6, 9}); the changed hexagram is Y = X ⊕ E, with Y = X when nothing changes.

- **coins:** sum of three fair coins worth 2 or 3.
- **yarrow-standard:** the first of three changes removes 5 or 9 stalks with probabilities 3/4, 1/4; the second and third remove 4 or 8 with probabilities 1/2, 1/2; the value is (49 − total removed)/4.
- **yarrow-uniform:** start with 49 stalks. In each change with n stalks, the left heap L is uniform on 1, …, n−1; one stalk is taken from the right heap and set aside; each heap is counted off by fours, leaving remainder 1–4 (an empty heap leaves 0); the removed count is 1 plus both remainders. Three changes; value = remaining/4.
- **yarrow-binomial:** as yarrow-uniform with L ~ Binomial(n, 1/2) conditioned on 1 ≤ L ≤ n−1.

The symmetric line-change channel with parameter p: X uniform on {0,1}⁶, E with six independent Bernoulli(p) bits independent of X, Y = X ⊕ E.

Labels: T(x) = L. G(x) = L ⊕ U. With the set D = {000000, 100000, 110000, 111000, 111100, 111110, 111010, 000010} (bottom-to-top strings), for each x let d be the unique element of D with L(d) ⊕ U(d) = G(x); then x ⊕ d = (b, b) for a three-bit b, and B(x) = b. A label is balanced if each of its 8 values occurs 8 times. These are mathematical definitions; correspondence to any historical table is not assigned here.

Entropies and informations are in bits; h₂ is binary entropy.

## Claims

**V1.** Under coins, X is uniform and the transition X → Y is the product binary symmetric channel with crossover 1/4, with E independent of X; I(X;Y) = 6[1 − h₂(1/4)] ≈ 1.13233. Under yarrow-standard, X is uniform, P(E = 1 | yang) = 3/8, P(E = 1 | yin) = 1/8, P(Y line yang) = 3/8, I(X;Y) ≈ 1.23261, I(X;E) ≈ 0.37367. Under both, each line changes with probability 1/4.

**V2.** Under yarrow-uniform, P(6) = 77/1612, P(9) = 5957/26832 and P(primary yang) = 14565731/29112720; under yarrow-binomial the probabilities agree with 1/16, 5/16, 7/16, 3/16 to about 10⁻⁶.

**V3.** Conditional on the premise that, for uniform independent bits and independent symmetric noise of crossover r, every Boolean function f has I(f(input); output) ≤ 1 − h₂(r): under coins, every Boolean question about X carries at most 1 − h₂(1/4) ≈ 0.188722 bits about Y, and vice versa; a single line attains it. (Check the transfer, not the premise.)

**V4.** Under the symmetric channel, for every 0 < p < 1/2: I(T(X);Y) > I(B(X);Y) > I(G(X);Y). At p = 1/4 the values are approximately 0.566166, 0.378621, 0.136698.

**V5.** As p → 0, I(λ;Y) = 3 − β(λ) p log₂(1/p) + O(p), with β the mean number of single-line changes altering the label: β(T) = 3, β(B) = 4, β(G) = 6. As ρ = 1 − 2p → 0, I(λ;Y) = W₁(λ) ρ²/(2 ln 2) + O(ρ⁴), with W₁(λ) = Σ_k ‖s(A_k)‖²/(64|A_k|), s_i(A) = Σ_{x∈A} (−1)^{x_i}: W₁(T) = 3, W₁(B) = 13/8, W₁(G) = 0. For every 8-subset A of {0,1}⁶, ‖s(A)‖² ≤ 192 with equality exactly for three-dimensional coordinate subcubes; hence among balanced labels β ≥ 3 and W₁ ≤ 3, both attained by partitions into coordinate subcubes.
