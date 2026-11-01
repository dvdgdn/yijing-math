# INV-0008 computations

Source work for INV-0008: cited working transcriptions built from hash-pinned Wikisource snapshots. Run with Python 3.9 or later, standard library only.

| Script | Does | Output |
|---|---|---|
| `fetch_sources.py` | Snapshots the listed Wikisource pages through the MediaWiki API into a new directory. Writes a manifest with revision IDs, timestamps, SHA-256 and permanent `oldid` URLs. | `investigations/INV-0008-cited-source-baselines/sources/` |
| `build_baselines.py` | Parses the snapshots, never the network, into the received-order, eight-palace and procedure-text datasets. Records every witness comparison and parse decision. Verifies each snapshot hash against the manifest. | `data/*.v1.csv`, `investigations/INV-0008-cited-source-baselines/build-results.json` |
| `compare_prior.py` | Run after the datasets were frozen. Compares them with INV-0005's saved phase-1 transcriptions and recomputes checkable source-dependent ledger statements. | `investigations/INV-0008-cited-source-baselines/comparison-results.json` |

Rebuild from the frozen snapshot into a fresh path. The rebuild is byte-identical to the frozen files:

```bash
python3 -I compute/experiments/INV-0008/build_baselines.py \
  --sources investigations/INV-0008-cited-source-baselines/sources \
  --order-csv /tmp/order.csv --palace-csv /tmp/palaces.csv \
  --procedure-csv /tmp/procedure.csv --out /tmp/build.json
```

A new `fetch_sources.py` run retrieves the current revisions, which may have changed since the frozen snapshot. To retrieve the frozen revisions, use the `permanent_url` values in the manifest.
