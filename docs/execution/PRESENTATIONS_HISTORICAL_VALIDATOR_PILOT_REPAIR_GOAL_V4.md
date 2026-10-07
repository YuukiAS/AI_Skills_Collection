---
task_key: presentations_historical_validator_pilot_repair_v4
status: READY
controller_mode: true
task_type: cross_repo_validator_repair
primary_repository: YuukiAS/AI_Skills_Collection
fixture_repository: YuukiAS/STAT5060-TA
slide_production_allowed: false
gpt_work_routine_qa_allowed: false
user_routine_qa_allowed: false
---

# Historical Presentation Validator Pilot Repair Goal V4

## 1. Objective

Repair the validator after V3 audit FAIL.

Do not edit Tutorial slides or audience artifacts.

The exact STAT5060 Planner authority is:

`docs/frozen/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_PILOT_REPAIR_SPEC_V4.md`

The binding audit is:

`docs/reviews/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_IMPLEMENTATION_AUDIT_V3.md`

V4 remains a pilot. Do not expand into a broad Presentation-plugin rewrite.

## 2. Mandatory workflow read

Before implementation, read in full:

1. presentation-end-to-end-pre-execution-runbook.md
2. pre-execution-cumulative-acceptance-contract.md
3. rendered-artifact-positive-ancestry-acceptance-contract.md
4. authoring-production-workflow.md
5. chatgpt-web-authoring-contract.md
6. anti-shortcut-production-contract.md
7. independent-review-contract.md

## 3. Control-plane correction

Use:

```text
Parent Controller
├─ Generic Producer
├─ STAT5060 Adapter Producer
├─ immutable candidate freeze
├─ fresh visual reviewer workers
├─ fresh semantic/guard reviewer workers
├─ deterministic/numerical checks
├─ Parent-only Phase-A / Phase-B / sentinel evaluation
├─ class-only repair packets
└─ fresh rerun
```

Expected historical verdicts never enter Producer or reviewer contexts.

## 4. Generic reusable candidate

Keep the generic core narrow.

Generic responsibilities:

- reviewer packet schema;
- reviewer row schema validation;
- reviewer provenance validation;
- artifact/page/hash identity;
- PDF/render feature extraction;
- deterministic evidence/warnings;
- visual reviewer orchestration contract;
- semantic/guard reviewer orchestration contract;
- keyed guard-closure schema;
- aggregation;
- anti-fitting;
- test/evidence registry.

Do not put STAT5060 PageIDs, feedback IDs, course policy, P26 values, historical
sentinel answers or administrative rules into generic production code.

## 5. Reviewer blindness

Remove exact historical page/failure expectations from:

- reviewer instructions;
- reviewer inputs;
- production controller modules;
- generic code.

The Parent may create/load hidden replay expectations only after reviewer output
freezes.

Normalized positive requirements are allowed. Expected verdicts are not.

## 6. Reviewer provenance

A reviewer row is valid only if matched to a persisted manifest.

Validate:

- reviewer_run_id;
- exact assigned pages;
- exact PNG hashes;
- fresh/read-only flags;
- image runtime;
- start/end metadata;
- output path/hash;
- one-to-one row ownership.

Self-declared row metadata is insufficient.

## 7. Strict evidence schema

Use JSON-schema or equivalent strict validation.

Array fields must be arrays.

Reject malformed evidence types rather than coercing them.

## 8. Visual and semantic review roles

Visual reviewer owns rendered composition/readability/protected-object checks.

Semantic/guard reviewer owns:

- first-use and sequence;
- interpretation completeness;
- notation/definition linkage;
- code correctness/copyability;
- audience/assessment boundary;
- visible identity/scope;
- normalized project guard requirements.

Both remain answer-key blind.

## 9. Guard closure

The STAT adapter supplies each applicable normalized requirement and authority
scope.

Return exactly one closure per page + unique guard requirement, with provenance
feedback IDs grouped into one array.

No blanket PASS.

No page PASS with an applicable mandatory guard unresolved.

## 10. Authority scope

Support minimal scope classes:

```text
CURRENT_FORWARD_GUARD
HISTORICAL_REPLAY_ONLY
INSTRUCTOR_ONLY
SUPERSEDED
```

Current forward production and historical replay must not contaminate one another.

## 11. Numerical contracts

Generic core supplies numerical-validation interfaces/schemas only.

STAT5060 owns P26 source binding and computation.

P26 must be computed from the actual posterior source, not emitted from known
history.

## 12. Parent-only evaluation

After freeze, compute separately:

- Phase-A blind probe;
- currently completed Phase-B history-reconciled probe;
- hidden historical sentinel replay.

Do not expose page answer keys to Producers/reviewers.

Route back only mismatch class/root mechanism.

Maximum ordinary repair cycles: 3.

## 13. Anti-fitting

Scan:

- AST;
- constants/dictionaries;
- imported JSON/YAML evaluation fixtures;
- reviewer instruction text;
- generated reviewer inputs.

Fail on exact historical page -> answer mappings in Producer/reviewer-visible
surfaces.

## 14. Tests

Every implemented detector/validator mechanism requires:

- production function exercised;
- positive test PASS;
- negative test PASS.

Also test:

- reviewer-manifest binding;
- malformed schema;
- lifecycle/scope filtering;
- keyed guard closure;
- Phase-B metrics;
- anti-fitting constant-map detection;
- P26 numerical source computation interface.

Persist the real command and exit code.

## 15. Completion

Push exact generic + STAT candidates and evidence, then refetch.

Required completion block:

```text
RESULT = PILOT_REPAIR_V4_READY_FOR_INDEPENDENT_AUDIT
REVIEWER_PROVENANCE_VALIDATION = PASS
RENDERED_REVIEW_BLINDNESS = PASS
SEMANTIC_GUARD_REVIEW = PASS
REVIEWER_EVIDENCE_SCHEMA = PASS
GUARD_LIFECYCLE_SCOPE = PASS
KEYED_GUARD_CLOSURE = PASS
PASS_WITH_UNCLOSED_GUARD = 0
P26_NUMERICAL_SOURCE_VALIDATION = PASS | BLOCKED_WITH_EXPLICIT_SOURCE_GAP
ANTI_ANSWER_FITTING = PASS
TEST_COVERAGE_EVIDENCE = PASS
PHASE_A_METRICS_REPORTED = YES
PHASE_B_METRICS_REPORTED = YES
PHASE_B_FALSE_PASS = 0
PHASE_B_FALSE_REVISE = 0
USER_ROUTINE_QA_USED = NO
GPT_WORK_USED_AS_ROUTINE_QA = NO
VALIDATOR_ACCEPTED = NO
V14_PRODUCTION_ALLOWED = NO
NEXT_ACTION = FRESH_IMPLEMENTATION_AUDIT_V4
```

If the exact Phase-B match cannot be reached without answer leakage after three
class-only repair cycles, return `NEEDS_GPT_PLANNER`. Do not relax the gate.
