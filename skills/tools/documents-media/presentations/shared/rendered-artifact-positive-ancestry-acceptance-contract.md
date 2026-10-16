# Rendered-Artifact and Positive-Visual-Ancestry Acceptance Contract

Status: **CANONICAL / MANDATORY FOR EVERY NON-TRIVIAL RENDERED PRESENTATION**

This contract governs the part of presentation quality that source checks and prebuild Critic review cannot certify: what the exact rendered pages actually look like and whether previously successful visual structures were preserved.

It exists because a deck can satisfy page count, exact copy, formulas, and build checks while still failing as a presentation.

---

## 1. Core principle

A prebuild specification PASS is permission to produce, not permission to release.

A rendered candidate passes only when:

1. every page image has been reviewed at whole-slide scale;
2. every render-dependent historical guard has been evaluated against the exact candidate;
3. positive visual ancestors and mandatory visual objects are preserved or explicitly retired;
4. numerical charts and figures agree with their underlying quantities;
5. the final aesthetic/reader-effort gate passes;
6. the evidence is bound to the exact artifact bytes.

---

## 2. Exact candidate identity

Every review bundle must include:

```text
repository
branch
source_commit
candidate_version
pdf_or_pptx_path
pdf_or_pptx_sha256
page_count
per_page_png_paths
per_page_png_sha256
contact_sheet_path
contact_sheet_sha256
render_engine
render_settings
```

A source or audience-byte change creates a new candidate identity. Reviews of the prior candidate do not automatically transfer.

---

## 3. Positive visual ancestry

Every non-trivial page/component must declare:

```text
stable_page_or_component_id
best_content_ancestor
best_visual_ancestor
negative_ancestors
mandatory_visual_objects
mandatory_visual_relationships
preserve_geometry_or_composition_features
minimum_readability_or_scale_expectation
allowed_changes
forbidden_deletions_or_substitutions
retirement_authority_if_any
```

Examples of mandatory visual objects:

- teaching diagram;
- large primary plot;
- comparison table;
- paired code/output composition;
- title/closing shell;
- Question/Answer rule grammar;
- method flow or algorithm schematic.

A Producer may redraw or improve a protected object, but may not silently delete it and replace it with prose.

---

## 4. Render-dependent historical closure

Every historical item in `RENDER_PENDING` must receive one row in the exact-candidate closure matrix:

```text
feedback_id
candidate_version
candidate_sha256
stable_page_id
physical_page
page_png_sha256
historical_artifact_and_page
historical_requirement
positive_visual_ancestor_if_any
render_evidence_locator
reviewer
verdict = PASS | FAIL | BLOCKED
finding_or_pass_reason
```

Rules:

- `RENDER_PENDING` is open until this row exists and passes.
- A global statement such as “all history consumed” is not sufficient.
- A visual requirement cannot be closed from source code or extracted text alone.
- A row may become `RESOLVED_IN_RENDER` only for the exact candidate whose image was inspected.

---

## 5. Mandatory per-page render review

For major/full-deck work, the rendered Auditor must produce exactly one review row per page:

| Field | Requirement |
|---|---|
| PageID / physical page | Exact current identity |
| PNG hash | Binds review to the exact image |
| Page job | What the audience should learn/do |
| Active historical guards | Explicit IDs/classes |
| Positive visual ancestor | Exact prior artifact/page or `NEW_AUTHORISED_COMPOSITION` |
| Mandatory visual objects | Present, missing, changed |
| Copy fidelity | Exact and student/audience appropriate |
| Reading path | Clear or broken |
| Primary-object scale | Adequate or too small |
| Typography | Projection-readable and within tokens |
| Whitespace | Deliberate or meaningless |
| Semantic proximity | Evidence and interpretation adjacent |
| Shared components | Header/footer/Q&A/table/code/caption consistency |
| Numerical/figure validation | Underlying quantity and label checked |
| Verdict | PASS / P0 / P1 / P2 |
| Evidence | Crop, measurement, or direct page observation |

A claimed full-deck PASS without all page rows is invalid.

---

## 6. Whole-slide and contact-sheet review

Both views are mandatory.

### Whole-slide view checks

- local hierarchy;
- text and object readability;
- Q/A geometry;
- evidence proximity;
- clipping, crowding, and whitespace;
- caption/source roles;
- precise page-level historical issues.

### Contact-sheet view checks

- deck rhythm;
- abrupt density changes;
- repeated half-empty pages;
- repeated tiny-object layouts;
- inconsistent shell/component geometry;
- visual monotony;
- section pacing;
- pages that look unfinished relative to neighbours.

A page may look acceptable in isolation and still fail in sequence.

---

## 7. Whitespace and scale gate

Whitespace is not automatically bad. It fails when it coexists with an underused teaching object or unreadable content.

Hard review triggers include:

- large unused lower region while the primary object is visibly small;
- text shrunk below approved tokens while body space remains;
- a table/figure/code block occupying a minor fraction of the body without pedagogical reason;
- result or interpretation pushed far from evidence;
- one short column creating a large void beside/under a dense column;
- a page looking visibly unfinished.

The Auditor must either justify the whitespace as intentional or fail the page.

Automated occupancy metrics may support review, but cannot replace whole-slide judgment.

---

## 8. Typography floor

Each deck must define role-based typography tokens for:

- frame title;
- body;
- subheading;
- table;
- code;
- caption;
- source;
- equations and labels.

Rules:

- page-local shrinking below the token floor is forbidden;
- dense pages must use a better composition, approved split, or Planner escalation;
- fitting content by making everything smaller is not compliance;
- a page may not be called PASS merely because text does not overflow.

---

## 9. No deletion-as-repair

The following shortcut is forbidden:

```text
historical object is difficult to repair
-> delete the object
-> replace it with prose
-> claim the page job is preserved
```

Deletion requires explicit Planner authority naming:

- the retired object;
- the replacement teaching function;
- affected historical guards;
- why the positive visual ancestor is no longer binding.

Without that authority, missing protected objects are a hard failure.

---

## 10. Numerical visual validation

Rendered charts, traces, posterior plots, residual plots, and diagnostic figures must be validated against the actual quantity displayed.

Required checks:

- variable identity;
- units and scale;
- pre/post-warmup or filtering stage;
- axis and legend labels;
- consistency with nearby numerical summaries;
- consistency with source data/code;
- absence of unexplained spikes, impossible values, or mismatched transformations.

A visually clean but numerically wrong figure is a P0 failure.

---

## 11. Internal proof is mandatory even when hidden from the user

For failed-version recovery and materially new visual systems:

1. produce real-content component proofs;
2. produce high-risk page proofs;
3. review and repair them internally;
4. only then produce the full deck.

The user may choose not to see intermediate proofs. That choice does not authorize skipping them.

Proof evidence must include exact artifact/image identities and reviewer outcomes.

---

## 12. Reviewer independence and scope integrity

The Producer cannot issue final rendered acceptance.

A rendered review is authoritative only when:

- reviewer context is fresh/read-only;
- exact candidate identity is supplied;
- all required pages are actually inspected;
- review scope is explicit;
- page rows and render-pending closure rows are persisted;
- the reviewer cannot edit the candidate or gates;
- the reviewer does not rely only on Producer completion prose.

A sampled-page review cannot declare a full-deck PASS.

---

## 13. GPT Work final gate

For major/recovery decks, GPT Work receives:

- exact final PDF/PPTX identity;
- all page images;
- full contact sheet;
- positive visual ancestry matrix;
- cumulative visual guards;
- high-risk-page list;
- Codex deterministic/rendered review reports.

It independently judges:

- visual quality;
- reader effort;
- naturalness;
- hierarchy;
- whitespace;
- object scale;
- evidence proximity;
- whole-deck rhythm;
- recurrence of historical visual failures.

GPT Work cannot override a deterministic, numerical, or history-coverage failure.

---

## 14. Hard-fail conditions

Any of the following blocks delivery:

- missing page review rows;
- unresolved mandatory `RENDER_PENDING` items;
- protected visual object deleted without authority;
- widespread tiny-object / large-void pages;
- page-local font shrinking below tokens;
- suspicious numerical figure not validated;
- source bytes changed after review;
- candidate hash mismatch;
- scoped review presented as global PASS;
- absent or non-independent GPT Work review where required;
- the user is the first reviewer to identify obvious full-deck defects.

---

## 15. Required final evidence block

```text
CANDIDATE_ID =
SOURCE_COMMIT =
ARTIFACT_SHA256 =
PAGE_COUNT =
PAGE_REVIEW_ROWS = N/N
RENDER_PENDING_ROWS_REVIEWED = N/N
POSITIVE_VISUAL_OBJECT_LOSSES = 0
NUMERICAL_FIGURE_VALIDATION_ERRORS = 0
TYPOGRAPHY_FLOOR_ERRORS = 0
MEANINGLESS_WHITESPACE_FAILURES = 0
SHARED_COMPONENT_REGRESSIONS = 0
DETERMINISTIC_AUDITOR = PASS
RENDERED_AUDITOR = PASS
GPT_WORK = PASS | NOT_REQUIRED
OPEN_P0 = 0
OPEN_P1 = 0
OPEN_P2 = 0
READY_FOR_USER_REVIEW = YES
```

If any value is missing, inferred, stale, or bound to another candidate, the artifact is not ready.