# The Yijing as structure over GF(2)⁶: several independent layers, no single core

**Short answer:** I find no single mathematical core. There are at least four structures, each exact, and they belong to different textual layers. What unifies them is a symmetry property, not a common theory. The pre-Han layers respect a two-element reversal symmetry, and the Han palace system provably breaks it. The strongest worked result is that the Han "eight palaces" are transversals of a coset decomposition. From that, a traditional mnemonic for locating the "generation line" follows as a theorem, along with a new reflection law. All claims below were checked by exhaustive computation over the 64 hexagrams.

## 1. Object and layers

The layers are kept separate:

- **(a) Configurations.** These are the 64 hexagrams.
- **(b) Relations among them.** These are pairing, the nuclear hexagram, and trigram decomposition.
- **(c) Orderings.** The received King Wen order (1–64, upper canon 1–30, lower canon 31–64) is the main object. The Shao Yong/"Fuxi" binary order and the Mawangdui silk order are separate objects.
- **(d) Procedures.** The main one is the Jing Fang (Han) eight-palace construction.
- **(e) Text.** Judgments and line statements are bracketed entirely.

**Encoding.** A hexagram is a word x = (x₁,…,x₆) in GF(2)⁶, read bottom to top, with yang = 1. Two operations matter:

- **R** reverses the word, x ↦ (x₆,…,x₁). Physically, this is the figure seen from the other side of the table.
- **C** complements every line, x ↦ x ⊕ 111111.

Trigram decomposition is x = (l, u). The lower and upper trigrams l and u are each in GF(2)³.

## 2. Representation choices

The yin/yang labels are arbitrary. Every result below is C-equivariant, so swapping 0 and 1 changes nothing.

Line order is not arbitrary. The lines are physically stacked, so position and adjacency are given by the object itself. Every interesting result depends on position, and that dependence is earned.

Numerical encoding is weak. "Hexagram as binary number" privileges one line as most significant. Only the Shao Yong order uses that choice, and there it is just the definition of the order.

Hamming distance (the number of lines that differ) is natural for line-changing procedures. It plays no explanatory role elsewhere.

## 3. Competing hypotheses

- **H0, baseline.** The 64 words are the cube Q₆ with no further structure, and the King Wen order is arbitrary once pairs are fixed.
- **H1, binary positional.** Shao Yong's order is base-2 counting. This is true by construction and explains nothing about King Wen.
- **H2, symmetry quotient.** The Klein four-group V = ⟨R, C⟩ acts on Q₆, and the King Wen order is built on V-orbit data.
- **H3, metric sequence.** Hamming distances between consecutive hexagrams carry design, for example the known observation that no step changes exactly 5 lines.
- **H4, linear dynamics (proposed framework).** The nuclear map N(x) = (x₂,x₃,x₄,x₃,x₄,x₅) is treated as a GF(2)-linear operator whose dynamics organize the sequence.
- **H5, coset geometry.** Han procedures are coset constructions relative to the subspace P = {(t,t)} of the eight doubled trigrams.
- **Ambitious conjecture.** Every traditional structure is a V-equivariant affine operator on GF(2)⁶, so the Yijing would be a representation of V with a positional grading.

## 4. Results

**Theorem 1 (pairing).** Define σ(x) = R(x) if R(x) ≠ x, and σ(x) = C(x) otherwise. Then σ is a fixed-point-free involution, because C preserves palindromes and has no fixed points. The 32 King Wen pairs are exactly the orbits of σ, which I checked for all 32. The 8 palindromes (1, 2, 27, 28, 29, 30, 61, 62) give 4 complement pairs, and the other 28 pairs are reversals.

**Theorem 2 (canon balance).** Quotienting by R gives 36 "figures": 28 reversal pairs plus 8 palindromes. Each canon contains exactly 18 figures.

This explains the odd 30/34 split. If the upper canon holds p palindrome pairs and r reversal pairs, balance requires 2p + r = 18. The upper canon then has 2p + 2r = 36 − 2p hexagrams. With p = 3 (pairs 1/2, 27/28, 29/30), that gives 30.

A second observation was not used to build this. The upper canon holds exactly the four doubled trigrams whose trigram is itself a palindrome: Qian, Kun, Kan, Li (1, 2, 29, 30). The lower canon holds the four whose trigram is not: Zhen, Gen, Xun, Dui (51, 52, 57, 58).

**Theorem 3 (nuclear operator).** N is linear and commutes with both R and C. It satisfies N⁴ = N², so its minimal polynomial is t²(t+1)².

By Fitting's lemma, GF(2)⁶ splits as ker N² ⊕ A:
- ker N² = {x₃ = x₄ = 0}, of dimension 4;
- A = {000000, 111111, 101010, 010101}, the words of period dividing 2.

Every hexagram enters A within two steps. On A, N fixes Qian and Kun and swaps Jiji and Weiji. In King Wen numbering, A is exactly {1, 2, 63, 64}: the first and last pairs of the sequence.

Under a null model that shuffles the 32 pairs and their orientations, both attractor pairs land at the two ends with probability 0.0021. If we condition on Qian/Kun opening the sequence, the probability is 1/31.

**But H4 fails beyond the endpoints.** Two statistics test it:
- *Same canon:* how many hexagrams have their nuclear hexagram in the same canon. King Wen scores 38 against a null p of 0.29.
- *Nearby pair:* how many have their nuclear hexagram in the same or an adjacent pair. King Wen scores 6 against a null p of 0.87.

So the sequence does not track N. The endpoint fact is equally explained by a competitor: "period-2 words" equals "all lines in correct position, or all incorrect, or constant." The real object singled out is the subspace A. N is one of several operators that pick it out.

**H3 is not earned.** Within-pair distances are always even, which is forced because R changes lines in mirror pairs. Between pairs, the distances are 1:2, 2:8, 3:13, 4:7, 6:1, with no 5. Under pair-shuffling, the chance of no 5 is 0.043. That is before correcting for the many statistics one could have tested, so it is not significant.

## 5. Strongest worked result: the palaces are a coset transversal

Jing Fang's procedure starts from a doubled trigram b = (t,t). It then flips lines cumulatively from the bottom:

- generations 1–5 flip lines {1}, {1,2}, …, {1,…,5};
- the "wandering soul" then reverts line 4;
- the "returning soul" restores the lower trigram.

This gives eight difference vectors: D = {000000, 100000, 110000, 111000, 111100, 111110, 111010, 000010}.

**Theorem 4.** Let φ(x) = l ⊕ u, the lower trigram XOR the upper. Then φ maps D bijectively onto GF(2)³. Hence D is a transversal of P in GF(2)⁶, and the 64 hexagrams split uniquely as b + d with b ∈ P and d ∈ D. The palaces therefore partition the 64, and each palace contains exactly one hexagram of each φ-value.

*Proof.*
1. The prefix flips give φ = 000, 100, 110, 111, 011, 001, which are six distinct values.
2. The wandering soul (111010) gives 101, and the returning soul (000010) gives 010. These are the two missing values.
3. P = ker φ, so x ↦ φ(x) identifies the cosets of P. Writing x = b + d, d is the unique element of D with φ(d) = φ(x), and b = x ⊕ d. ∎

**Corollary A (a reconstruction not used to build the theory).** A hexagram's generation, and so its "generation line" (世爻), depends only on which trigram positions agree. Call the positions earth (bottom), man (middle) and heaven (top).

| Positions that differ | Generation (世) | Traditional mnemonic |
|---|---|---|
| none | pure, line 6 | 本宫六世 |
| earth only | 1st | 地变初 |
| earth, man | 2nd | 天同二世 |
| all three | 3rd | 三世异 |
| man, heaven | 4th | 地同四世 |
| heaven only | 5th | 天变五 |
| earth, heaven | wandering soul | 人同游魂 |
| man only | returning soul | 人变归 |

This table is exactly the traditional mnemonic (天同二世天变五，地同四世地变初，本宫六世三世异，人同游魂人变归). The mnemonic is the map GF(2)⁶/P → D, written in words.

**Corollary B (a new consequence).** Since φ(Rx) = reverse(φ(x)), reversing a hexagram swaps generations 1↔5 and 2↔4. Pure, 3rd, wandering and returning hexagrams keep their status.

*Worked example.*
- Zhun (3) = Zhen below Kan, so φ = 100 ⊕ 010 = 110: 2nd generation. Its base is x ⊕ 110000 = Kan palace.
- Its King Wen partner Meng (4) = Kan below Gen, so φ = 011: 4th generation. Its base is x ⊕ 111100 = Li palace.

Both match the traditional palace tables, and 2↔4 is as Corollary B predicts.

## 6. Is the depth earned?

**Theorems 1 and 2.** These use few premises (σ and one cut) and explain one non-obvious number, 30. The trigram-palindrome split of the doubled hexagrams came free. Within the pair-shuffling model, the canon balance itself is not rare, with about a 22% chance of p = 3 in the first 15 pairs. So what it explains is why the cut is at 30, not why the order looks the way it does.

**Theorem 3.** This is real linear algebra, but it is inevitable once N is defined. The only contingent fact is that A sits at the ends.

**Theorem 4.** This is the deepest result. From a local, step-by-step rule, a global partition follows, and it is not automatic that the two soul moves fill the gaps exactly. It also reconstructs an independent traditional rule and yields Corollary B. Any transversal would generate some mnemonic, so the distinctive fact is that a cumulative bottom-up rule lands on a transversal at all.

**Generalization.** For 2k lines there are (2^{2k} + 2^k)/2 figures, and a nuclear map generalizes with attractors at the period-2 words. Six lines is not mathematically special. What is distinctive is which choices the texts made.

**The ambitious conjecture is refuted, and the refutation is informative.** The King Wen pairing and N commute with R. Jing Fang's D does not: Corollary B is precisely the trace of the broken symmetry. A revised version survives as a conjecture: the pre-Han layers are R-equivariant, while Han constructions break R down to the trigram split (l, u). The Mawangdui order, organized by upper trigram, also breaks R.

## 7. Decisive checks, weakest assumption, next step

**Decisive checks.**
- Corollary B commits us to a checkable claim: across all 28 reversal pairs, generations reflect 1↔5 and 2↔4 in every standard palace table. A single counterexample would mean my statement of the procedure is wrong.
- The stratification conjecture predicts that pair structure appears in every early ordering that respects R. If the Chu bamboo manuscript, wherever its order is recoverable, breaks pairs, the conjecture fails.

**Weakest assumption.** The null model. Shuffling pairs treats the received order as one designed object chosen from equally likely alternatives. If the order accreted over time, or if constraints I haven't modeled were operating, all the p-values are miscalibrated. Note also that historical intention is a separate claim: Theorem 4 shows the procedure is a transversal, not that Jing Fang knew it.

**Most informative next step.** Build a fixed, pre-registered grammar of simple operators and statistics. Then run every historically attested ordering and procedure (King Wen, Mawangdui, the Chu manuscript, Jing Fang, Shao Yong) through it and classify each by its symmetry group. That would turn the R-equivariance stratification from a pattern I noticed into a tested claim, and it would properly account for the many encodings one is free to search across.

Value of further work is high relative to current confidence. The theorems are certain. The claim that they reveal design is moderate at best for H2 and the endpoint fact, and not supported for H3.
