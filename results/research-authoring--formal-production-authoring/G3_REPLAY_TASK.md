# G3 Final Candidate Manuscript Package Task

Use the installed `research-writing` candidate through its normal formal manuscript and LaTeX production entry.

This is the frozen G3 manuscript-production task. The source repository is read-only. Treat the provided `runtime_input/` files as the complete materialized source/authority subset.

Read the provided files:

- `TASK_IDENTITY.md`;
- `VENUE_PROJECT_AUTHORITY.md`;
- `PACKAGE_SUBSET.md`;
- `G3_RUBRIC.md`;
- `REVIEWER_ACCESS.md`;
- `MATERIALIZED_G3_SOURCE_SUBSET.json`;
- `AGENTS.md`;
- `README.md`;
- `PAPER_STATUS.md`;
- `RESULTS_TRUTH.md`;
- `METHOD_TRUTH.md`;
- `CLAIM_LEDGER.md`;
- `review/AUTHOR_DECISIONS.md`;
- `submission/mosaic.tex`;
- `submission/refs.bib`;
- `submission/llncs.cls`;
- `submission/splncs04.bst`;
- `submission/figures/fig1_original_redraw.pdf`.

Write exactly the required package subset under `outputs/G3_PACKAGE/`:

1. `mosaic.tex`;
2. `refs.bib`;
3. `figures/fig1_original_redraw.pdf`;
4. `llncs.cls`;
5. `splncs04.bst`;
6. `SUBMISSION_MANIFEST.md`.

If your environment can compile PDF, also write `mosaic.pdf`; if not, write all buildable sources and explain the expected build route in the manifest. Do not create unrelated sidecar files.

Task requirements:

- produce a clean, double-blind CARE 2026 LNCS submission package;
- bring the manuscript within the frozen <=12 page limit including references;
- keep LNCS class/style unchanged;
- do not invent, strengthen, or reassign scientific claims;
- preserve `RESULTS_TRUTH`, `METHOD_TRUTH`, `CLAIM_LEDGER`, and `AUTHOR_DECISIONS` boundaries;
- do not reintroduce unsupported edema rows, unsupported ablations, SOTA claims, cross-center robustness claims, or unresolved provenance as active claims;
- preserve valid citations, figure identity, labels, and cross-references;
- include the required data-origin/citation/acknowledgment statement according to frozen project authority;
- do not submit anywhere.

In `SUBMISSION_MANIFEST.md`, record:

- source repository and ref;
- output package identity;
- build route;
- expected page limit and page-control changes;
- double-blind check;
- LNCS template unchanged check;
- data-origin/declaration check;
- citation/figure/cross-reference status;
- known limitations that remain;
- statement that no live submission occurred.
