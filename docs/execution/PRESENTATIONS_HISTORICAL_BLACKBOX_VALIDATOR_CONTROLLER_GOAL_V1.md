---
task_key: presentations_historical_blackbox_validator_v1
status: READY
controller_mode: true
task_type: cross_repo_validator_build_and_acceptance
primary_repository: YuukiAS/AI_Skills_Collection
primary_branch: work/presentation-historical-blackbox-validator-v1
fixture_repository: YuukiAS/STAT5060-TA
fixture_branch: work/stat5060--tutorial-01-v2
user_routine_qa_allowed: false
slide_production_allowed: false
---

# Autonomous Controller Goal — Historical Black-Box Presentation Validator V1

The user starts this Goal once. The Parent Controller owns implementation,
black-box evaluation, automatic repair, fresh re-evaluation and the final
mechanism Critic. Do not ask the user to relay intermediate outputs or manually
launch reviewers.

## 1. Exact start-state preflight

The launch prompt supplies exact remote HEADs for both repositories. Verify them.
Only safe fast-forward is allowed. Do not reset, rebase, merge unrelated work or
choose a different baseline.

Read in full:

### Generic authority

- `plugins/codex/plugins/presentations/shared/presentation-end-to-end-pre-execution-runbook.md`;
- `plugins/codex/plugins/presentations/shared/pre-execution-cumulative-acceptance-contract.md`;
- `plugins/codex/plugins/presentations/shared/rendered-artifact-positive-ancestry-acceptance-contract.md`;
- `plugins/codex/plugins/presentations/shared/historical-blackbox-render-validator-spec.md`;
- `docs/design/PRESENTATIONS_RENDER_REGRESSION_POSTMORTEM_AND_HARDENING_2026-10-07.md`.

### STAT5060 adapter authority

- `docs/frozen/2026-27/STAT5060_TUTORIAL_01_V1_V13_BLACKBOX_VALIDATION_SPEC_V1.md`;
- `docs/frozen/2026-27/STAT5060_TUTORIAL_01_V14_PAGE_BY_PAGE_VISUAL_REPAIR_FREEZE_V1.yaml`;
- current Tutorial recovery manifest;
- 193-row feedback authority, direct decisions, page lineage and version manifests;
- V1–V13 sources/PDFs/renders/evidence;
- V13 human rejection and recovery plan.

Emit a read manifest before implementation.

## 2. Hard boundary

```text
SLIDE_SOURCE_EDIT_ALLOWED = NO
THEME_EDIT_ALLOWED = NO
FIGURE_EDIT_ALLOWED = NO
PDF_AUDIENCE_ARTIFACT_EDIT_ALLOWED = NO
RENDER_REPLACEMENT_ALLOWED = NO
V14_CREATION_ALLOWED = NO
FROZEN_AUTHORITY_EDIT_ALLOWED = NO
VALIDATOR_IMPLEMENTATION_ALLOWED = YES
READ_ONLY_HISTORICAL_RENDERING_FOR_TESTS = YES
```

Rendering a historical source/PDF into an isolated test-output directory is
allowed. Modifying or replacing the historical artifact is not.

## 3. Trust-separated topology

Use distinct fresh contexts/workspaces:

```text
Parent Controller
├─ Generic Producer A — generic core only, no STAT5060 repository access
├─ Adapter Producer B — STAT5060 inventory/adapter only, no generic detector edits
├─ Public test run
├─ freeze candidate commits
├─ Parent generates hidden holdout/mutation pack outside both producer workspaces
├─ Fresh read-only Auditor — full corpus + hidden pack
├─ Fresh Mechanism Critic — architecture/evidence review
├─ automatic root-mechanism repair if required
└─ new fresh Auditor + new fresh Critic
```

A same-context Producer self-review is debugging only.

## 4. Generic Producer A isolation

Create an isolated or sparse workspace containing only:

- the generic validator specification;
- generic presentation contracts;
- normalized schemas;
- public synthetic fixtures;
- generic package/test paths.

Do not provide access to:

- `YuukiAS/STAT5060-TA`;
- historical expected outcomes;
- hidden holdout selection;
- hidden mutation seeds;
- course PageIDs/feedback IDs/version labels.

Allowed generic implementation root:

`plugins/codex/plugins/presentations/shared/validator_v1/`

Allowed generic public tests:

`plugins/codex/plugins/presentations/shared/validator_v1/tests_public/`

Generic Producer may not edit the frozen specifications or other presentation
runtime contracts.

Generic Producer completion is only:

```text
GENERIC_CANDIDATE_COMMIT = <sha>
READY_FOR_ADAPTER_AND_BLACKBOX = YES
GENERIC_VALIDATOR_ACCEPTED = NO
```

## 5. Adapter Producer B boundary

Adapter Producer may read STAT5060 authority and historical artifact manifests.
It implements only:

- corpus discovery;
- historical artifact/page mapping;
- PageID/page-job/guard normalization;
- positive visual ancestry normalization;
- numerical claim contracts;
- mapping generic findings back to course PageIDs/feedback IDs;
- evidence/result serialization.

Allowed STAT5060 paths:

```text
scripts/presentation_validation/tutorial01_validator_adapter_v1/
tests/presentation_validation/tutorial01_public/
results/tutorial-01-validator-v1/public/
docs/reviews/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_IMPLEMENTATION_REPORT_V1.md
```

Adapter Producer may not:

- edit generic detector logic;
- encode expected PASS/FAIL by version;
- suppress generic findings;
- edit slide/theme/figure/PDF/render paths;
- edit frozen Planner authority.

Adapter completion is only:

```text
ADAPTER_CANDIDATE_COMMIT = <sha>
READY_FOR_BLACKBOX = YES
VALIDATOR_ACCEPTED = NO
```

## 6. Public implementation requirements

Implement the detector families required by the generic specification.

Every detector must expose one production function used by:

- real artifact validation;
- public positive controls;
- public negative controls;
- hidden holdout/mutations.

Public tests must include compliant controls and generalized mutations, but not
the hidden historical answers.

The generic core API must not accept artifact/version/PageID/feedback-ID strings
as control-flow inputs.

## 7. Historical corpus execution

The Adapter must discover and execute every materialised Tutorial artifact,
including at minimum:

```text
V01 V02 V03 V04 V05 V06 V07
later V08 38-page artifact
V09 18-page proof
human-rejected component/golden proof
V10 V11 V12 V13
early V3/V4/V5/V6/V7 artifacts
Rich V1/V2
Student V04 and later Student V07
```

For each artifact:

- bind exact identity and hash;
- verify/produce page renders in isolated output;
- run every applicable generic detector;
- apply course mapping/guards;
- emit per-page and per-guard findings;
- never treat manifest status as the detector verdict.

All artifacts must be executed. Missing/unrenderable artifacts are BLOCKED, not
silently skipped.

## 8. Parent-owned hidden pack

Only after both producer candidates freeze, Parent creates a hidden temporary
pack outside both producer repositories/workspaces.

It contains:

- randomly selected held-out historical artifacts/pages;
- expected failure classes derived from immutable human review evidence;
- scoped historical positive controls;
- randomized/metamorphic mutations;
- coordinated mutations that change multiple fields together;
- threshold-boundary cases;
- one unrelated presentation bundle.

Do not reveal pack contents, seeds or expected outcomes to either Producer.

Hash the hidden pack before the Auditor run. The final evidence may publish the
pack hash and summarized results. Future reruns use a fresh seed/pack.

## 9. Hidden mutations

At minimum include randomized instances of:

- small primary object plus large empty body;
- interpretation moved far from evidence;
- one peer column shortened to create a void;
- protected diagram deletion with prose retained;
- diagram replacement by generic boxes;
- table/code text reduced below floor;
- output detached from its code panel;
- Question/Answer rule deletion or block leakage;
- title/header/footer/navigation/page-number removal;
- section-name abbreviation;
- mathematical glyph transliteration;
- plotted variable/unit/warmup/filter/scale corruption;
- stale evidence and wrong candidate hashes;
- representative-page review promoted to full-deck PASS;
- `READY_FOR_GPT_WORK` promoted to `READY_FOR_USER_REVIEW`.

## 10. Static anti-fitting audit

Before black-box execution, run static analysis over the generic core and fail on:

- STAT5060/course/version/PageID/feedback-ID literals;
- historical filenames/hashes;
- expected verdict strings used in detector branches;
- fixture/test/mutation ID branches;
- hidden-oracle/test-only imports;
- candidate-provided expected/allowed fields expanding authority;
- unversioned thresholds or unexplained magic constants.

The course adapter is allowed project literals but not detector suppression or
version-based verdict lookup.

## 11. Fresh Auditor

Launch a fresh read-only Auditor with:

- exact generic and adapter candidate commits;
- both repositories read-only;
- hidden pack and expected outcomes;
- full historical corpus;
- no permission to edit code, tests, authority or artifacts.

Auditor must independently run:

- static anti-fitting scan;
- public controls;
- hidden controls/mutations;
- all historical artifacts;
- unrelated deck;
- evidence-completeness checks.

It must verify “good passes” and “bad fails precisely,” not only deck-level
rejection.

Auditor findings use:

```text
ID
SEVERITY
DETECTOR
ARTIFACT
PAGE
EXPECTED_CLASS
OBSERVED_CLASS
EVIDENCE
ROOT_MECHANISM
GENERIC_OR_PROJECT_SPECIFIC
REQUIRED_REPAIR
```

## 12. Fresh Mechanism Critic

After Auditor execution, launch a new read-only Critic using:

`docs/reviews/prompts/PRESENTATIONS_HISTORICAL_BLACKBOX_VALIDATOR_CRITIC_PROMPT_V1.md`

The Critic reviews:

- architecture and trust separation;
- anti-fitting proof;
- corpus completeness;
- positive/negative balance;
- false pass/fail risk;
- finding precision;
- generic/project-specific separation;
- hidden pack integrity;
- all required outputs;
- whether the mechanism is strong enough to unblock V14 planning.

## 13. Automatic repair loop

If Auditor or Critic returns any P0/P1/P2:

1. persist finding packet;
2. classify generic-core versus adapter defect;
3. launch a fresh appropriate Producer with only the finding class, not hidden
   expected values;
4. repair root mechanism;
5. add public regression coverage for the class;
6. freeze new candidate commits;
7. generate a new hidden seed/pack;
8. launch new fresh Auditor;
9. launch new fresh Critic.

Do not ask the user for routine QA.

Maximum ordinary cycles: 3. If the same class recurs twice, rewrite the responsible
mechanism instead of patching the example. If the frozen architecture itself is
insufficient, stop with `NEEDS_GPT_PLANNER` and name the exact unresolved decision.

## 14. Required outputs

Generic repository:

```text
plugins/codex/plugins/presentations/shared/validator_v1/
docs/reviews/PRESENTATIONS_HISTORICAL_BLACKBOX_VALIDATOR_AUDIT_V1.md
docs/reviews/PRESENTATIONS_HISTORICAL_BLACKBOX_VALIDATOR_CRITIC_V1.md
```

STAT5060 repository:

```text
scripts/presentation_validation/tutorial01_validator_adapter_v1/
results/tutorial-01-validator-v1/
docs/reviews/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_IMPLEMENTATION_REPORT_V1.md
```

Evidence bundle must contain all files required by the frozen validation spec.

## 15. Final acceptance

Final success requires:

```text
RESULT = VALIDATOR_ACCEPTED
ALL_DISCOVERED_HISTORICAL_ARTIFACTS_EXECUTED = YES
V01_THROUGH_V13_COVERED = YES
GENERIC_CORE_PROJECT_SPECIFIC_BRANCHES = 0
FIXTURE_NAME_BRANCHES = 0
HIDDEN_ORACLE_IMPORTS = 0
PUBLIC_POSITIVE_FALSE_FAILURES = 0
PUBLIC_NEGATIVE_MISSES = 0
HIDDEN_POSITIVE_FALSE_FAILURES = 0
HIDDEN_NEGATIVE_MISSES = 0
HISTORICAL_P0_P1_FALSE_NEGATIVES = 0
RELEASE_FALSE_PASSES = 0
FINDING_PRECISION = PASS
UNRELATED_DECK_GENERALISATION = PASS
FRESH_AUDITOR = PASS
MECHANISM_CRITIC = PASS
GENERIC_SPECIFIC_OWNERSHIP_MATRIX = PASS
USER_ROUTINE_QA_USED = NO
V14_SLIDE_PRODUCTION_ALLOWED = NO
NEXT_ACTION = CHATGPT_FREEZE_VALIDATOR_ACCEPTANCE_AND_P26_NUMERICAL_REPAIR
```

Even after validator acceptance, this Goal does not create V14 or edit slides.
