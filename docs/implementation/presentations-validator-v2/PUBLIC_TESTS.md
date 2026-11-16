# Public regression

The candidate run imported Validator V2 from the generated Presentations
payload. The runtime used Python 3.12.4, PyMuPDF 1.28.2 and PyYAML 6.0.3.
Unittest ran 33 tests with zero failures, errors or skips. The
[raw test log](PUBLIC_TEST_LOG.txt) and [machine-readable records](PUBLIC_RESULTS.json)
bind the result to the code digest in [coverage](COVERAGE.json).

| Evidence | Result |
| --- | --- |
| Git authority, identity, scope and historical binding | Positive and mutated bundle tests passed |
| Synthetic layout boundaries | Font, spacing, rail, captions, Q/A, columns, footer, navigation, table, diagram, closing and density tests passed |
| Real PDF input and protected pixels | PDF binding, unassigned objects, source scan, scoped raster changes and forbidden text masking tested |
| Unrelated teaching and research | Both Beamer sources compiled with XeLaTeX and yielded no deterministic fail with review still required |
| Frozen V19 and archived V18 | Exact PDF hashes verified before extracting a text-free slice. The V19 slice had no objective failure for tested checks. Both V18 layout defect classes produced failures |
| Existing Presentations entry points | Four route and existing-deck review tests passed |
| Marketplace generation | `--validate --check --path-report --json` exited 0. The path portion is stored in [MARKETPLACE_CHECK.json](MARKETPLACE_CHECK.json) |

The archived slice is in `tests/fixtures/archived_geometry.json` under the
package. It records the exact oracle tree source by commit, both PDF Git blob
IDs, PDF SHA-256 values, physical page 39, font metrics, bounds and frame
counts. The V18 archive was referenced in the same tree as the frozen V19
oracle. V18 section counts came from the exact `V18_SECTION_NEGATIVE_CONTROL.json`
blob in that tree. No course copy is stored in the slice.

The legacy replay uses [LEGACY_REPLAY_CONFIG.json](LEGACY_REPLAY_CONFIG.json).
The actual CLI returned exit 2 when the exact V4 review file was absent. This
shows that the adapter did not substitute other review files.
