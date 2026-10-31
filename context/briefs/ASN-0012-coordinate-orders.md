---
id: brief-ASN-0012
assignment: ASN-0012
context_mode: targeted
contains: coordinate-sweep model, finite pilot and limitations of imported mixing bounds
created: 2026-10-31
---
# Local coordinate transformations and joint order structure

Take positions V={0,1}^d with distinct labels. A coordinate-i layer independently swaps each pair {x,x xor e_i} with probability 1/2. A sweep visits i=1,…,d. In the supplied Thorp manuscript §2 this corresponds, in a moving frame, to d physical shuffles with a cyclic coordinate rotation.

At d=6 every label has an exactly uniform position after one sweep. But a sweep uses only 192 fair bits, so its full-permutation law has support at most 2^192, giving TV distance from uniform on S64 at least 1−2^192/64!. The pilot checks all one-card marginal distributions exactly. This finite statement is reported, not independently verified by this programme.

The source's principal upper-mixing result is asymptotic, explicitly not a numerical guarantee at d=6. Another companion states an all-dyadic moment bound with an unspecified absolute power in its theorem. Unless a usable constant is extracted and checked, no finite burn-in may be inferred from either statement.

There is no claim that this is an attested Yijing construction. It is an explicit comparison mechanism using a selected local grammar. Edge transpositions generate the whole symmetric group, so unrestricted generatability cannot explain an ordering. A useful question must concern bounded depth, a short fixed program, retained joint information, or consequences not selected by fitting the target order. A different order of six deterministic coordinate layers is not a genuinely different grammar unless its effect is justified.
