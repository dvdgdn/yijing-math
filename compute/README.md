# Computation

Code for verifying claims and for computational experiments. Standards are in [`methods/standards.md`](../methods/standards.md) §3–4.

This README must stay free of research findings. Code in the subdirectories may contain findings and is not minimal-safe.

## Layout

| Directory | Contents |
|---|---|
| `verification/INV-NNNN/` | Code and outputs produced by, or used to check, a verification investigation. One folder per investigation. |
| `experiments/INV-NNNN/` or `experiments/<topic>/` | Exploratory computation. Label it as exploratory. |

Code supplied by an investigator as part of a report is saved verbatim in the investigation folder (`investigations/INV-NNNN-slug/code/`). Copy it here only if it is run or adapted, and record the origin.

## Conventions

- **Standard library only** by default (Python 3.9 or later). If a script needs a third-party package, say why in its folder's README and pin the version.
- **Self-contained scripts.** Each folder has a short README listing what each script does, its inputs (with dataset versions from `data/`), its outputs, and how to run it.
- **Record outputs.** Save the output of every run that a ledger record cites, or its SHA-256 if large, together with the date and Python version.
- **Randomness.** Fix and record seeds and sample sizes, and report Monte Carlo uncertainty.
- **Independence.** Verification code is written independently of the code it checks. Do not import from another investigation's folder when verifying that investigation's claims.

## No shared library yet

There is deliberately no shared mathematical library. If one becomes useful (for example, a checked encoding of a dataset), it gets its own folder with tests and provenance. Verifiers should still write their own implementations when checking claims that were derived with it.
