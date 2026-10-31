---
id: brief-ASN-0010
assignment: ASN-0010
context_mode: targeted
contains: exact source scope, formal pilot and unresolved extension; no claim of independent verification
created: 2026-10-31
---
# Information under line changes: source and application contract

All prior results here are reported. The external theorem was read in source but its proof was not audited by this programme. The pilot was performed in a continuing full-context Codex conversation. It is not independent of the supplied encoding. Novelty of the application has not been checked.

## Formal model and imported theorem

Let X be uniform on {0,1}^{2k}; coordinates are independent. Let Y=X xor E with all noise bits independent Bernoulli(p), independent of X, 0≤p≤1/2. Write X=(L,U), G=L xor U, q=2p(1−p). The source theorem in the supplied manuscript's Corollary `main:ck` implies I(f(X);Y)≤1−h₂(p) for any Boolean f, with attainment by a coordinate. It also refines the bound using Boolean output bias; it does not permit a biased input law or an asymmetric transition merely by changing p.

The pilot's transfer proof claims I(g(G(X));Y)=I(g(G(X));G(Y)) and hence, conditional on the source theorem, an optimum 1−h₂(q) for every Boolean g. Check this reduction before building on it.

## Six-line comparison

Use bottom-to-top six-bit words, xor coordinatewise. The specified difference set is

    000000,100000,110000,111000,111100,111110,111010,000010.

For each x choose the unique d with G(d)=G(x). Then x xor d=(B,B) defines a three-bit base B. B and G are independent uniform labels. This encodes the formal palace construction used by earlier reports; its correspondence to a cited traditional table remains unverified.

From exact integer posterior masses with numerical entropy, the pilot reports:

| p | I(B(X);Y) | I(G(X);Y) | Best Boolean summary of G |
|---|---|---|---|
| 1/8 | 1.103576694734 | 0.726364612385 | 0.242121537462 |
| 1/4 | 0.378621055176 | 0.136697991225 | 0.045565997075 |

All values are bits. The full G formula is 3[1−h₂(q)]. A raw trigram retains 3[1−h₂(p)] and does better at these parameters. Do not infer a universal multi-bit optimum by summing binary bounds: joint information must be analyzed as joint information.

## The unanswered question

Does the base/difference comparison persist throughout 0<p<1/2, and is there an informative structural reason? Can an optimum or obstruction be proved for a precisely defined symmetry-compatible family of observables? Compare with elementary raw-coordinate and alternative-partition baselines. Start with one precise extension; do not search many observable classes and report only the winner.

An asymmetric channel with flip probabilities a and b is a distinct model, potentially relevant after a procedure is cited. It may destroy uniformity or symmetry. State which claims survive by direct argument and which no longer follow from the imported theorem. Actual coin/yarrow probabilities are not supplied here.


## Already excluded proof route

A subsequent exact author check found that universal pointwise majorization of the difference posterior by the base posterior fails. At p=1/8, Y=0, the sorted posteriors are (301,49,49,49,43,7,7,7)/512 and (15625,4375,4375,4375,1225,1225,1225,343)/32768. Their top-four masses are 7/8 and 14375/16384, respectively, in the wrong order for that majorization. This does not refute an average-information comparison. Do not repeat that sufficient-condition route as stated; seek another argument or a counterexample to the actual question.
