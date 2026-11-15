# Public mutations

The mutation and boundary cases invoke the same parser, Git validators and
layout functions used by the CLI. [Public results](PUBLIC_RESULTS.json)
records 85 executed subtests, including positive controls, boundary values,
negative mutations and the two unrelated Beamer renders. It is a subtest count
rather than a count of distinct semantic failure classes.

| Audit findings | Production mechanism exercised |
| --- | --- |
| AUD1-P1-001 | Reject duplicate mapping keys before materialization and repeated record IDs |
| AUD1-P1-002, AUD3-P1-001 | Compare complete source tuples and reject linked path/blob substitutions, stale immutable blobs, and omitted blob fields |
| AUD1-P1-003 | Resolve relocation decision by its ID and check object, action and destination |
| AUD1-P1-004, AUD2-P1-003 | Reject incomplete global review and invalid or incorrect artifact digest values |
| AUD1-P1-005, AUD2-P1-004 | Resolve historical objects without requiring the candidate to be checked out or substituting nearby evidence |
| AUD2-P1-001 | Compare complete ordered feedback records, including provenance and target fields |
| AUD2-P1-002 | Compare complete component records in addition to checking the page-consumer inverse |
| AUD3-P1-002 | Require matching lock evidence and independently resolve both Git blobs |
| AUD3-P1-003 | Require baseline commit, candidate commit and candidate tree |

The boundary suite probes both sides of font, spacing, body rail, Q/A,
navigation and shaft thresholds. The archived controls add observed body rail
and section width failures. The fixture harness picks deidentified roles;
production checks do not receive archive names or expected verdicts.

[Coverage](COVERAGE.json) lists 14 layout/source hooks and five integrity hooks
registered by the CLI. Its AST scan reports zero known fixture-related
selectors in conditionals. That limited scan does not prove semantic
independence from arbitrary magic values or measure holdout coverage.
