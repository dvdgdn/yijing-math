# INV-0004 computations

Exploratory and computer-assisted computation for INV-0004 (full context, context-exposed). Not verification code for any other investigation; it does not import from `compute/experiments/INV-0003/`.

| Script | Does | Output |
|---|---|---|
| `divination_information.py` | Line-value laws of four procedure models and their primary→changed channels. Courtade–Kumar bound table for the coins model. Exhaustive Boolean scans for n ≤ 4. Six-line local searches. Label structure (trigram, palace, generation) and endpoint coefficients. Computer-assisted proof of the all-noise ordering. Balanced-label searches. Independent recomputation of INV-0003 L1–L6. | `investigations/INV-0004-divination-information-bounds/results.json` |

Run (Python 3.9+, standard library only, about 35 s):

```bash
python3 -I compute/experiments/INV-0004/divination_information.py --out /tmp/inv0004-check.json --nmax 4 --starts 60 --iters 60000 --restarts 4 --seed 20261031
```

The frozen run used exactly these parameters and wrote to the investigation folder. Write reproductions to a fresh path. Probabilities and grid masses are exact rationals. Information values use binary64 logarithms. Local searches are seeded.
