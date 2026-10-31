---
id: brief-ASN-0001-phase1
assignment: ASN-0001
context_mode: targeted
contains: claim statements and definitions only; no proofs, evidence, or assessments of significance
created: 2026-10-31
---
# Claims to Verify (Phase 1: statements and definitions only)

The claims below were reported by an earlier investigation in this program. **None has been independently verified.** You receive only their statements and the definitions they use. The original reasoning and evidence will be supplied later, after you have recorded your own derivations.

## Conventions used by these claims

You may work in any representation you prefer, but you must check the claims as stated in this one.

- **Encoding.** A hexagram is a word x = (x₁, …, x₆) with entries in {0, 1}, read from bottom (x₁) to top (x₆), with unbroken (yang) = 1 and broken (yin) = 0. Addition ⊕ is coordinatewise mod 2.
- **R (reversal):** R(x₁, …, x₆) = (x₆, …, x₁), the figure turned upside down.
- **C (complement):** C(x) = x ⊕ 111111, every line changed.
- **σ:** σ(x) = R(x) if R(x) ≠ x, and σ(x) = C(x) otherwise.
- **Trigrams:** x = (l, u) with lower trigram l = (x₁, x₂, x₃) and upper trigram u = (x₄, x₅, x₆).
- **P:** the set of eight doubled-trigram hexagrams {(t, t)}.
- **φ:** φ(x) = l ⊕ u ∈ {0,1}³. Its three positions are called earth (bottom), man (middle), heaven (top).
- **Palace procedure (as stated by the earlier investigation, attributed to Jing Fang).** Start from a doubled trigram b = (t, t). Generations 1 to 5 flip lines {1}, {1,2}, {1,2,3}, {1,2,3,4}, {1,2,3,4,5} of b, cumulatively from the bottom. The "wandering soul" (游魂) then reverts line 4 of the 5th-generation figure. The "returning soul" (歸魂) then restores the lower trigram to that of b. This gives eight difference vectors d (hexagram = b ⊕ d):

| Label | d (x₁…x₆) |
|---|---|
| pure (本宮) | 000000 |
| 1st generation | 100000 |
| 2nd generation | 110000 |
| 3rd generation | 111000 |
| 4th generation | 111100 |
| 5th generation | 111110 |
| wandering soul | 111010 |
| returning soul | 000010 |

  D denotes this set of eight vectors. The palace of b is {b ⊕ d : d ∈ D}.

## Claims

**C-0001.** σ is an involution on {0,1}⁶ with no fixed points.

**C-0002.** In the received (King Wen) order, the 32 consecutive pairs {2k−1, 2k}, k = 1, …, 32, are exactly the orbits of σ. Equivalently, 28 pairs consist of a hexagram and its reversal, and the 8 hexagrams fixed by R (numbers 1, 2, 27, 28, 29, 30, 61, 62) form the other 4 pairs, each a hexagram and its complement.

**C-0016.** φ maps D bijectively onto {0,1}³. Hence every hexagram can be written uniquely as b ⊕ d with b ∈ P and d ∈ D; the eight palaces partition the 64 hexagrams; and each palace contains exactly one hexagram with each value of φ.

**C-0017.** (a) The procedure above is the Jing Fang eight-palace construction, and D correctly encodes it. (b) The palace and generation assignments it produces agree with the traditional palace tables for all 64 hexagrams.

**C-0018.** A hexagram's generation depends only on φ(x), that is, on which trigram positions differ between lower and upper trigram, as follows:

| Positions that differ | Generation |
|---|---|
| none | pure (generation line 6) |
| earth only | 1st |
| earth, man | 2nd |
| all three | 3rd |
| man, heaven | 4th |
| heaven only | 5th |
| earth, heaven | wandering soul |
| man only | returning soul |

This table coincides with the traditional mnemonic 天同二世天变五，地同四世地变初，本宫六世三世异，人同游魂人变归.

**C-0019.** φ(Rx) is the reversal of the word φ(x). Consequently, reversing a hexagram swaps generations 1 ↔ 5 and 2 ↔ 4, and preserves pure, 3rd-generation, wandering-soul and returning-soul status. In particular, across all 28 pairs {x, Rx} with Rx ≠ x, the traditional palace tables show generations related in this way.

**C-0026 (restricted to the claims above).** Each of the claims above holds equally if the labels are swapped (yin = 1, yang = 0).

## What to produce in phase 1

For each claim: your precise restatement (noting any ambiguity), your own derivation or computation, and a provisional verdict. For C-0002, C-0017, C-0018 and C-0019, write out in full the transcription you use of the received order and of the palace tables (all 64 hexagrams, with palace and generation), and state its source. Then stop and wait for phase 2.
