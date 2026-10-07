---
task_key: presentations_historical_validator_pilot_repair_v2
status: READY
controller_mode: true
task_type: cross_repo_validator_repair
primary_repository: YuukiAS/AI_Skills_Collection
fixture_repository: YuukiAS/STAT5060-TA
slide_production_allowed: false
gpt_work_routine_qa_allowed: false
user_routine_qa_allowed: false
---

# Historical Presentation Validator Pilot Repair Goal V2

## 1. Goal

Repair the validator mechanism itself. Do not build or modify Tutorial slides.

The V1 bootstrap candidate is a negative implementation fixture. Its published
implementation audit has P0/P1 failures and its 515-row result is not accepted
evidence of a real rendered review.

The repaired pilot must produce page-level PASS/REVISE from:

- exact rendered page evidence;
- normalized page/job/component authority;
- applicable non-verdict historical guards;
- deterministic checks that only claim what their inputs support;
- independent rendered-page reviewers that actually inspect the PNG.

This is still a pilot. Do not expand into a full Presentation-plugin rewrite.

## 2. Mandatory read

Read in full, in this order:

1. `presentation-end-to-end-pre-execution-runbook.md`
2. `pre-execution-cumulative-acceptance-contract.md`
3. `rendered-artifact-positive-ancestry-acceptance-contract.md`
4. `authoring-production-workflow.md`
5. `chatgpt-web-authoring-contract.md`
6. `anti-shortcut-production-contract.md`
7. `independent-review-contract.md`

Then read the current STAT5060 repair specification, V1 implementation audit,
fresh-page-review progress, current historical corpus inventory, current page
maps and V13 recovery authority.

## 3. Known V1 defects that must be treated as root mechanisms

At minimum close these classes:

- rendered review was synthesized from deterministic features instead of actual
  whole-slide image inspection;
- generic production validator did not exist in AI_Skills_Collection;
- page feature extraction was too shallow for claimed semantic conclusions;
- PASS was default fallthrough from “no detector fired”;
- protected-object detection used page-id/word-count/occupancy heuristics;
- historical replay used hard-coded artifact/page locators;
- anti-fitting scan was regex-only and missed page-specific branches;
- production tests did not exercise production detectors;
- ordinary defect classes were missing;
- evidence metadata was not regenerated against exact published candidate bytes;
- detector inventory overstated actual implemented capability.

The current Planner repair specification may add further findings. Those are
equally binding.

## 4. Architecture

Use one Parent Controller with separate workspaces/contexts:

```text
Parent Controller
├─ Generic Producer A
│  └─ AI_Skills_Collection validator_v1 core + public synthetic tests
├─ STAT5060 Adapter Producer B
│  └─ corpus mapping, guard compiler, course-specific contracts
├─ public tests
├─ freeze immutable candidate commits
├─ fresh deterministic Auditor
├─ fresh rendered Reviewer workers
│  └─ exact PNG inspection, no expected verdict labels
├─ Parent-only blind calibration
│  └─ compare with available independent fresh-page-review rows
├─ class-only repair packets
├─ fresh Producer repair
└─ fresh rerun
```

Neither Producer receives the independent fresh-page-review PASS/FAIL rows.

The Parent may read those rows only after candidate freeze and may route back only
the failure class/root mechanism, not artifact/page answer keys.

## 5. Real generic core — narrow scope only

Create an actual implementation under:

`plugins/codex/plugins/presentations/shared/validator_v1/`

Required capabilities for this pilot:

- typed/versioned schemas for page features, findings, review packets, review rows
  and page aggregation;
- exact artifact/page identity and hashes;
- PDF text/span/block geometry using PyMuPDF or equivalent;
- embedded image/drawing/object-region extraction;
- connected/body region geometry;
- text collision/overlap candidates;
- typography warnings;
- primary-object/whitespace interaction support;
- peer-layout and reading-path geometry support;
- Question/Answer geometry support;
- table/code/figure region candidates;
- code-output and evidence-interpretation proximity support;
- shell-region integrity support;
- positive-ancestry/protected-object reviewer packets;
- generic internal/production-identifier warning support;
- AST/static anti-fitting scan;
- public synthetic positive and negative tests.

A detector may be listed as implemented only when production code and direct
production-function tests exist.

Do not promote anything beyond `REUSABLE_CANDIDATE` in this Goal.

## 6. Deterministic evidence discipline

Deterministic extraction supports review; it does not replace it.

Explicitly forbidden equivalences:

```text
whole-body bbox              != primary object
overall median word height   != figure-internal readability
word count + occupancy       != diagram existence
page-job string              != plot existence
PNG hash                     != image inspection
absence of finding           != PASS
```

Every detector must expose:

```text
detector_id
implementation_status
observable_inputs
finding_class
positive_control
negative_control
production_function
reuse_classification
```

## 7. STAT5060 adapter

Keep in `STAT5060-TA`:

- exact corpus inventory;
- artifact/physical-page -> stable PageID mapping;
- page jobs and component roles;
- historical guard compilation;
- protected Tutorial object descriptions;
- exact numerical contracts;
- assessment/HW/project audience boundaries;
- Tutorial-specific forbidden production identifiers.

The adapter may configure generic detector inputs but may not suppress findings,
change generic thresholds by version, or encode expected PASS/REVISE.

### Mandatory mapping validation

Before any page verdict is produced, audit every artifact mapping against the
actual rendered/source page identity.

For each mapped page persist:

```text
artifact_id
physical_page
stable_page_id
expected_page_job
visible_title_or_semantic_fingerprint
mapping_evidence
mapping_verdict = PASS | REVISE
```

A stale map blocks page-level aggregation.

In particular, the V13 mapping must be repaired and verified against its actual
38-page order. Do not reuse the V08 template blindly.

## 8. Fresh rendered-page review is authoritative for ordinary visual defects

A rendered Reviewer worker receives:

- exact page PNG path + SHA-256;
- page job/component role;
- normalized non-verdict guard requirements;
- protected visual-object descriptions if applicable;
- deterministic region measurements as hints;
- no historical PASS/FAIL label;
- no prior validator verdict.

The worker must actually open the image using the runtime image-viewing
capability.

If image pixels cannot be inspected, return:

`BLOCKED_RENDER_REVIEW_RUNTIME`

Do not synthesize a review from feature counters.

Each row must contain:

```text
artifact_id
physical_page
page_png_sha256
reviewer_context_id
review_scope = WHOLE_SLIDE

checks:
  shell
  typography
  scientific_object_internal_readability
  primary_object_scale
  whitespace
  reading_path
  peer_layout
  q_a_geometry
  evidence_interpretation_proximity
  code_output_proximity
  protected_object
  internal_identifier_or_markup_leak
  audience_boundary

problem_locations[]
positive_visible_evidence[]
negative_visible_evidence[]
overall_visual_verdict = PASS | REVISE | BLOCKED
substantive_observation
```

Every applicable check must be explicitly PASS or REVISE. Non-applicable checks
must be marked N/A with a reason.

A PASS page requires positive visual evidence. There is no PASS fallthrough.

### Reviewer worker granularity

Use fresh read-only reviewer workers by artifact or bounded artifact chunk.
Prefer one fresh context per artifact; if a 46-page artifact is too large, split
it into two disjoint chunks. Each page receives exactly one canonical review row.

The Parent must run lexical/template-duplication diagnostics over reviewer
observations and fail the review if rows collapse into canned boilerplate that
could have been written without seeing the image.

## 9. Ordinary defect classes that must be closed before GPT Work/user

At minimum the combined deterministic + rendered-review mechanism must catch:

- wrong two-column semantics;
- peer-column imbalance;
- primary object too small with large unused space;
- dense unreadable page;
- page-local typography below floor;
- figure/table/code internal text unreadability;
- text collision/overlap;
- orphaned prose / broken reading path / value-unit separation;
- code-output detachment;
- evidence-interpretation separation;
- Q/A geometry break;
- shell/title/header/footer/closing regression;
- protected diagram deletion;
- diagram replaced by prose;
- student-visible production/internal identifiers;
- raw markup leakage;
- course-specific assessment answer scaffolding;
- missing substantive rendered review evidence.

These are upstream responsibilities. Do not defer them to GPT Work or the user.

## 10. Public tests

Public tests must call the same production functions used on real pages.

For every implemented detector family include:

- at least one compliant positive;
- at least one negative/mutated case;
- boundary case where practical.

The test suite must directly exercise production functions for:

- text collision;
- typography;
- object-scale/whitespace interaction;
- peer/reading-path geometry;
- Q/A geometry;
- scientific-object internal readability support;
- code/output proximity;
- evidence/interpretation proximity;
- shell integrity;
- internal identifier warning;
- protected-object review packet construction;
- page aggregation;
- AST anti-fitting scan.

A smoke test that only counts corpus rows does not count as detector coverage.

## 11. Anti-answer-fitting

Run an AST/import/literal scan over generic production code and fail on:

- STAT5060 literals;
- historical artifact/version names;
- PageIDs;
- feedback IDs;
- historical filenames/hashes;
- fixture/test/mutation IDs in production branches;
- expected verdict labels used for control flow;
- page-number-specific verdict logic;
- hidden fresh-review imports.

The STAT5060 adapter may contain course mappings and PageIDs, but may not contain
version/page -> expected verdict lookup or use historical verdicts to suppress or
reclassify generic findings.

Historical positive/negative replay locators belong only in Parent/Auditor
evaluation fixtures, never production detector logic.

## 12. Numerical visual scope

Do not mark every page with stable PageID `T01-STORED-DRAWS` as numerically
blocked.

A numerical block must come from an explicit artifact/page numerical contract or
from observed inconsistency.

For this Tutorial, the V13 suspicious trace is course-specific and must bind to
the correct physical page after mapping repair.

Other historical trace pages may PASS visual review if their exact numerical
contract/evidence is not violated.

## 13. Parent-only blind calibration

After candidate freeze, read the current independent blind review under:

`docs/recovery/2026-27/tutorial-01/fresh-page-review-v1/`

Use only rows currently completed in `PROGRESS.json`.

Do not reveal those row verdicts/locations to Producers.

Compute:

```text
BLIND_ROWS_AVAILABLE
BLIND_REVISE_ROWS
BLIND_PASS_ROWS
TRUE_REVISE
TRUE_PASS
FALSE_PASS
FALSE_REVISE
REVISE_RECALL
REVISE_PRECISION
AGREEMENT
MISMATCH_CLASSES
```

Raw accuracy alone is forbidden because PASS dominates the corpus.

For a mismatch, route back only the failure class/root mechanism and create a new
generic/public regression fixture that is not the hidden historical page.

Maximum ordinary repair cycles: 3. Repeated class twice -> rewrite the mechanism,
not another threshold patch.

## 14. Required evidence

Generic repository:

```text
plugins/codex/plugins/presentations/shared/validator_v1/
docs/reviews/PRESENTATIONS_HISTORICAL_VALIDATOR_PILOT_REPAIR_AUDIT_V2.md
```

STAT5060 repository:

```text
scripts/presentation_validation/tutorial01_validator_adapter_v1/
tests/presentation_validation/tutorial01_public/
results/tutorial-01-validator-v1/repair-v2/
docs/reviews/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_REPAIR_REPORT_V2.md
```

Evidence bundle must include:

```text
mapping_audit.json
page_features.jsonl
deterministic_findings.jsonl
render_review_packets.jsonl
rendered_review_rows.jsonl
page_results.jsonl
coverage_report.json
detector_coverage.json
static_anti_fitting_report.json
reviewer_duplication_diagnostics.json
blind_calibration_report.json
fresh_deterministic_audit.md
fresh_rendered_review_audit.md
repair_acceptance_report.md
```

## 15. Repair-round completion gate

This Goal does not declare the validator finally accepted.

It may complete only when:

```text
RESULT = PILOT_REPAIR_CANDIDATE_READY_FOR_NEXT_INDEPENDENT_AUDIT
GENERIC_CORE_IMPLEMENTED = YES
STAT5060_ADAPTER_SEPARATED = YES
ALL_CURRENT_MAIN_ARTIFACTS_EXECUTED = YES
ALL_CURRENT_MAIN_PAGES_REVIEWED = YES
MISSING_PAGE_ROWS = 0
DUPLICATE_PAGE_ROWS = 0
MAPPING_AUDIT = PASS
V13_MAPPING_AUDIT = PASS
V13_STORED_DRAWS_PHYSICAL_PAGE = 26
PASS_FALLTHROUGH_ROWS = 0
RENDERED_REVIEW_GENUINE = YES
RENDERED_REVIEW_RUNTIME_BLOCKS = 0
REVIEWER_DUPLICATION_DIAGNOSTICS = PASS
PRODUCTION_DETECTOR_TEST_COVERAGE = PASS
AST_ANTI_FITTING = PASS
GENERIC_CORE_PROJECT_SPECIFIC_BRANCHES = 0
BLIND_ROWS_AVAILABLE = <n>
FALSE_PASS = <n>
FALSE_REVISE = <n>
REVISE_RECALL = <value>
REVISE_PRECISION = <value>
USER_ROUTINE_QA_USED = NO
GPT_WORK_USED_AS_ROUTINE_QA = NO
REUSE_CLASSIFICATION_COMPLETE = YES
VALIDATOR_ACCEPTED = NO
V14_PRODUCTION_ALLOWED = NO
NEXT_ACTION = FRESH_IMPLEMENTATION_AUDIT_V2
```

Do not call this Goal complete while implementation/evidence exists only in a
temporary worktree. Push exact audited candidate commits to both remote branches
and refetch them before reporting completion.
