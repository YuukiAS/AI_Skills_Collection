---
task_key: presentations_historical_validator_pilot_repair_v3
status: READY
controller_mode: true
task_type: cross_repo_validator_repair
primary_repository: YuukiAS/AI_Skills_Collection
fixture_repository: YuukiAS/STAT5060-TA
slide_production_allowed: false
gpt_work_routine_qa_allowed: false
user_routine_qa_allowed: false
---

# Historical Presentation Validator Pilot Repair Goal V3

## 1. Objective

Repair the validator control plane and rendered-review mechanism after V2 audit
FAIL.

The exact STAT5060 Planner authority is:

`docs/frozen/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_PILOT_REPAIR_SPEC_V3.md`

The exact implementation audit is:

`docs/reviews/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_IMPLEMENTATION_AUDIT_V2.md`

Do not modify Tutorial slides or audience artifacts.

## 2. Mandatory workflow

Read in full:

1. presentation-end-to-end-pre-execution-runbook.md
2. pre-execution-cumulative-acceptance-contract.md
3. rendered-artifact-positive-ancestry-acceptance-contract.md
4. authoring-production-workflow.md
5. chatgpt-web-authoring-contract.md
6. anti-shortcut-production-contract.md
7. independent-review-contract.md

## 3. Non-negotiable architecture

The generic Python validator core is deterministic infrastructure only.

It may:

- extract page/render features;
- emit typed deterministic findings/warnings;
- build reviewer packets;
- validate reviewer-row schema and image hashes;
- aggregate independently authored reviewer rows.

It may not author rendered visual verdicts itself.

A final rendered-review row is valid only when produced by a fresh read-only
reviewer context that actually receives and inspects the exact PNG.

A deterministic function that says “whole-slide PNG opened” after PIL extraction
does not satisfy this contract.

## 4. Reviewer workers

Parent Controller launches fresh reviewer workers by artifact or disjoint artifact
chunk.

Reviewer input:

- exact immutable candidate/page PNG and SHA;
- normalized page role/job;
- applicable guard requirements and evidence contracts;
- protected-object description/positive-ancestor reference when applicable;
- deterministic measurements as advisory evidence;
- no expected PASS/REVISE label;
- no prior validator verdict;
- no Producer scratchpad.

Reviewer output is persisted separately from detector output and includes explicit
PASS/REVISE/N/A/BLOCKED status for every applicable review dimension.

If the runtime cannot actually inspect pixels, output
`BLOCKED_RENDER_REVIEW_RUNTIME`.

## 5. Deterministic core repair

Implement the V3 STAT spec, including:

- detector applicability compiler;
- body-only geometry excluding shared shell;
- scientific-object region/readability support;
- high-precision text collision support;
- role-aware whitespace/object scale;
- role-aware Q/A requirements;
- project-supplied forbidden-identifier rules;
- protected-object reviewer packet support;
- exact generic-core version/commit binding;
- real test-run evidence.

Soft geometry signals are warnings for image review unless a calibrated hard
contract exists.

## 6. Historical guard closure

Every active historical guard applicable to a page must be assigned one explicit
verification owner:

```text
DETERMINISTIC
RENDERED_REVIEWER
STAT5060_SPECIFIC
NUMERICAL
BLOCKED
```

Persist one closure row per feedback/guard requirement.

No PASS with an uncovered mandatory guard.

The generic core remains project-agnostic. Course-specific guard implementations
stay in STAT5060.

## 7. Calibration separation

Maintain three different evaluation products:

1. human-history sentinel replay;
2. blind fresh-image-review comparison;
3. future Critic page oracle.

Do not collapse them into one “ground truth”.

Blind CSV vocabulary is PASS/FAIL. Normalize FAIL to REVISE for comparison.

When blind review conflicts with direct human history, report the conflict and
preserve human authority. Do not tune the detector to erase the historical guard.

## 8. V13 sentinel

Parent/Auditor evaluation must independently replay the V13 known failure
mechanisms named in the STAT V3 specification, including:

- P18 dense/readability;
- P23 prior-table scale + lower void;
- P25 unfinished composition;
- P26 numerical source/scale;
- P28 peer composition + lower void;
- P30 protected mechanism diagram deletion;
- P33 top-cluster/large void;
- P34 predictive-panel scale/proximity.

A page merely returning some unrelated REVISE does not count as replay PASS.

## 9. Tests

Tests must call exact production functions.

Persist:

- command;
- exit code;
- generic core commit;
- detector registry;
- positive test per implemented detector;
- negative test per implemented detector;
- coverage matrix.

The acceptance report may not hard-code test coverage or reviewer independence
as PASS constants.

## 10. Repair loop

After implementation candidate freeze:

1. fresh deterministic audit;
2. fresh rendered reviewer workers;
3. human-history sentinel replay;
4. blind-review comparison;
5. classify mismatch root mechanisms;
6. route only class/root mechanism to fresh Producer;
7. freeze new candidate;
8. repeat with fresh reviewers.

Do not expose hidden page answer keys to Producers.

Maximum ordinary repair cycles: 3. Repeated class twice requires mechanism
rewrite.

## 11. Completion

Push exact generic and STAT candidate commits before reporting.

Required completion block:

```text
RESULT = PILOT_REPAIR_V3_READY_FOR_INDEPENDENT_AUDIT
RENDERED_REVIEW_INDEPENDENT = YES
RENDERED_REVIEW_SELF_GENERATED_BY_DETECTOR_CORE = NO
BLIND_FAIL_ROWS_PRESERVED = YES
HUMAN_HISTORY_CONFLICTS_REPORTED = YES
HISTORICAL_GUARD_CLOSURE = PASS
V13_HARD_REPLAY = PASS
P26_NUMERICAL_VALIDATION = PASS | BLOCKED_WITH_EXPLICIT_SOURCE_GAP
PASS_WITH_UNCLOSED_GUARD = 0
GENERIC_CORE_IDENTITY_BOUND = YES
TEST_COVERAGE_EVIDENCE = PASS
USER_ROUTINE_QA_USED = NO
GPT_WORK_USED_AS_ROUTINE_QA = NO
VALIDATOR_ACCEPTED = NO
V14_PRODUCTION_ALLOWED = NO
NEXT_ACTION = FRESH_IMPLEMENTATION_AUDIT_V3
```
