# Presentations Core TODO — History Preflight, Accepted-Page Locks, Shared Geometry, and Mathematical Figure Text

Date: 2026-10-06  
Status: P0 CORE WORKFLOW TODO  
Evidence source: repeated STAT5060 Tutorial 01 regressions through V08

## 1. Why this is core

Long-running presentation revision failed even after human-feedback ledgers and review standards existed. The missing pieces were operational:

- the executor did not have to report how many historical issues it actually read;
- pages outside the bounded scope could still be rewritten incidentally;
- a page previously accepted by the human could be changed again by later Codex work;
- shared components such as footer and Question/Answer geometry repeatedly regressed;
- reviewers could say `PASS` without naming the historical guards they checked;
- figure generators could render mathematical variables as English transliterations such as `eta`.

These are generic presentation-production failures, not STAT5060-specific content.

## 2. P0 — Mandatory history-count preflight before any edit

Every existing-deck revision must stop before editing and report:

```text
HISTORY_REGISTRY_VERSION =
HISTORICAL_FEEDBACK_RECORDS_EXPECTED =
HISTORICAL_FEEDBACK_RECORDS_READ =
HUMAN_REJECTION_SOURCES_EXPECTED =
HUMAN_REJECTION_SOURCES_READ =
INSTRUCTOR/SPEAKER_FEEDBACK_RECORDS_REPRESENTED =
CURRENT_ROUND_FEEDBACK_ITEMS_READ =
UNRESOLVED_FEEDBACK_CONFLICTS =
```

If counts differ or conflicts remain:

```text
STOP = HISTORY_PREFLIGHT_FAILED
```

The report must distinguish:

- `ACTIVE`
- `SUPERSEDED`
- `RETIRED`
- `INSTRUCTOR_ONLY`
- `RESOLVED_BUT_GUARDED`

Loading a file is not enough; the revision must state the currently effective decision.

### Promotion gate

A fixture with one omitted historical item or one unresolved conflict must fail before source modification.

## 3. P0 — Every round must declare modify and do-not-change scopes

Every revision package must explicitly include:

1. all historical authority read;
2. current-round feedback;
3. pages/components to modify;
4. human-locked pages/components;
5. round-frozen pages/components;
6. shared components authorised for change;
7. shared components forbidden from change.

A missing do-not-change list is a hard failure.

Pages outside the current scope are `ROUND_FROZEN`; broad cleanup, formatter rewrites, macro substitution, or incidental reflow are forbidden.

## 4. P0 — Human-PASS page lock

Once a human explicitly marks a page PASS, the page receives a stable semantic ID and becomes immutable.

The lock record stores:

- stable page ID;
- source frame hash;
- visible-text hash;
- asset/figure hashes;
- statistical-object identity;
- whole-slide render hash;
- body-region render hash;
- approval date/source;
- allowed exceptions.

Executor must not change:

- wording;
- formulas;
- figures;
- tables;
- body layout;
- local typography/spacing;
- captions;
- page-level source.

Unlock requires explicit human authorisation naming the stable ID and scope.

### Shared header/footer exception

A locked page may be rerendered after an explicitly authorised shared header/footer change. The body region must remain unchanged under a frozen mask. Any body difference is a lock violation.

### Promotion gate

Modify an unrelated page in a test deck and verify the locked page source/body pixels remain identical. Inject a body change and ensure the build stops.

## 5. P0 — Shared component locks

Shared visual components require their own locks and regression suites:

- header/miniframe system;
- footer/navigation/page number;
- Question block;
- Answer block;
- caption roles;
- code style;
- table style.

Once human-approved, no project/page may reimplement them locally.

A shared-component change must:

- name the component ID;
- name every consuming page;
- rerender every consumer;
- compare against representative accepted fixtures;
- receive explicit human approval before relocking.

## 6. P0 — Question/Answer accent-rule alignment is a geometric invariant

The accent rule is retained; the problem is alignment, not existence.

Required behavior:

- Question and Answer both use an accent rule.
- The rule top aligns with the optical top of the rendered label/text block.
- The rule must not protrude upward above `Question` or `Answer`.
- The rule bottom aligns with the final rendered line of the block.
- At 1920×1080, optical top/bottom mismatch target is within approximately 1–2 px.
- Multi-paragraph Answer content uses one Answer block and one continuous rule unless the approved copy explicitly creates separate answers.
- One shared macro owns the geometry; no page-local rule drawing.
- Test one-line and multi-line Question/Answer blocks.

This requirement must remain active like footer alignment: future redesigns may not silently drop it.

## 7. P0 — Heterogeneous top-row optical alignment

When a row combines unlike objects such as image, prose, and table, equal container coordinates do not guarantee optical alignment.

Required workflow:

- identify the intended top anchor;
- compare visible image top, prose cap-height/top, and table top rule/header group;
- decide which object should move based on downstream space and reading path;
- record the decision in the page plan;
- validate whole-slide pixel deltas.

Tables often appear lower because the top rule/header group includes internal spacing. Do not automatically lower the image/prose to match; raise the table when that preserves useful body space.

## 8. P0 — Peer formulas require fixed semantic anchors

For two peer model/formula columns:

- subheadings share top anchor;
- formula regions use equal fixed-height boxes;
- principal equation baselines align within the calibrated tolerance;
- subsequent table/content begins below the common formula-region bottom;
- line wrapping in one heading may not push its equation down independently.

Once a human accepts the page, this geometry becomes a page lock.

## 9. P0 — Mathematical variables inside figures use mathematical glyphs

Scientific figure labels and annotations must use actual mathematical typesetting.

Reject English transliterations where a mathematical symbol is intended:

- `eta` instead of `η` / `$\eta$`;
- `beta` instead of `β` / `$\beta$`;
- `kappa` instead of `κ` / `$\kappa$`;
- `mu` instead of `μ` / `$\mu$`;
- `Rhat` instead of approved `\hat R` or natural `R-hat` wording.

Requirements:

- Matplotlib labels/annotations use mathtext/LaTeX strings;
- subscripts/superscripts use mathematical notation;
- figure typography is consistent with slide mathematics;
- source and final rendered pixels are checked;
- figure text extraction is checked where the backend exposes it;
- generic English words remain ordinary text; only mathematical variables require math glyphs.

### Promotion gate

Known fixtures containing `eta`, `beta`, and `kappa` as variable transliterations must fail; regenerated `$\eta$`, `$\beta$`, `$\kappa$` figures pass.

## 10. P0 — Page PASS must prove historical-guard consumption

A page review row must include:

```text
page_id
historical_guard_ids
lifecycle/effective decision
current rendered evidence
verdict
```

`HISTORY_LOADED=YES` is not equivalent to `RELEVANT_GUARDS_RESOLVED=YES`.

If applicable historical guards exist but the reviewer lists none, PASS is invalid.

## 11. P0 — Revision completion report

Every round must finish with:

```text
HISTORICAL_RECORDS_READ = expected/actual
CURRENT_ROUND_ITEMS_CLOSED = expected/actual
HUMAN_LOCKED_PAGE_VIOLATIONS = 0
ROUND_FROZEN_PAGE_VIOLATIONS = 0
SHARED_COMPONENT_LOCK_VIOLATIONS = 0
UNAUTHORISED_PAGE_CHANGES = 0
```

Only after these pass can audience-quality review begin.

## 12. Do not hard-code course-specific content

Do not encode STAT5060 page numbers, model examples, or exact feedback counts in generic runtime.

The plugin should support a project-supplied authority index, stable page IDs, lock ledger, revision scope, and mathematical-figure symbol policy.
