# Additional proof attempt — 2026-10-31

This supplements the frozen report without changing it. Status: **reported**, full-context author computation, not independent verification.

A tempting route toward an all-noise inequality in L2 would show that each base-label posterior majorizes the difference-label posterior. Schur concavity would then compare their conditional entropies pointwise. This sufficient condition fails.

With the same formal D, p=1/8 and Y=000000, the sorted base posterior is

    (301,49,49,49,43,7,7,7)/512,

while the sorted difference posterior is

    (15625,4375,4375,4375,1225,1225,1225,343)/32768.

The top-four masses are 7/8=14336/16384 and 14375/16384. The required inequality is reversed. The exact rational check was executed in Python 3.9.6; code is in `code/majorization-counterexample.py`. An earlier floating-point probe suggested this failure; the displayed instance was then checked with rational arithmetic.

**Scope:** this excludes a proof by universal pointwise majorization in this direction. It does not refute the all-noise *average entropy* comparison, a different coupling argument, a parameter-restricted majorization statement, or a different observable class. The numerical comparison in L2 remains a separate observation.

Next: pursue an average-information inequality, a different structural representation, or a direct counterexample search. Do not spend another run trying to prove this excluded universal sufficient condition as stated.
