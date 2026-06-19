# Output contracts and validation checklist

## Stable identifiers

- `eid` is the canonical subject identifier.
- Visit-specific context should come from the file location or an explicit field, not by overloading `eid`.

## CSV expectations

- Column names should remain stable across batches.
- Units should be encoded in the column label when practical.
- Aggregated CSV should be sorted by `eid`.
- Duplicate `eid` rows should be treated as a validation problem, not silently accepted.

## NPZ expectations

- Keys should be readable and unit-aware.
- Important timing markers such as ED/ES should be explicit.
- Downstream code should not need to guess key semantics from position.

## QC expectations

- Visualization paths should be deterministic.
- Feature-tracking or landmark outputs should be clearly separated from final phenotype tables.
- If a QC file is required for manual review, avoid renaming it without a migration note.

## Minimum validation questions

- Did any column name change?
- Did any unit change?
- Can old downstream notebooks still find the file?
- Can aggregation detect incomplete shards?
- Does documentation still match the code?
