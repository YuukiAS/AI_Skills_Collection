# Presentations — Independent Execution and Review Architecture

Date: 2026-10-06  
Status: **P0 ARCHITECTURE DECISION / PROMOTE WITH HISTORY-LOCK CONVERGENCE WORK**  
Primary evidence: STAT5060 Tutorial 01 repeated visible-deck regressions and three governance implementations that returned executor PASS before independent review found blocking defects.

## 1. Decision

Presentation production must separate **authoring/execution**, **deterministic validation**, **rendered-artifact review**, and **human acceptance** into different trust domains.

The executor that changes the deck or its governance implementation may not be the authority that declares the result accepted.

The required high-level route is:

```text
Planner / frozen authority
-> Executor candidate commit
-> Independent deterministic validator
-> Independent rendered-artifact reviewer
-> Acceptance aggregator
-> User delta review
-> Human lock
```

The executor may run local smoke tests for debugging, but its strongest completion state is:

```text
READY_FOR_INDEPENDENT_VALIDATION = YES
```

It may not issue the final deterministic PASS, visual PASS, human PASS, or release PASS for its own candidate.

## 2. Why file separation is not enough

Separate `materialize.py` and `validate.py` files do not establish independence when the same executor:

- writes both files;
- writes the fixtures;
- chooses the accepted controls;
- runs the tests;
- interprets the results;
- edits the validator until the candidate passes.

This is the failure mode seen in the STAT5060 recovery cycle.

Independence is a **runtime and authority property**, not a filename property.

## 3. Trust domains

### 3.1 Planner / ChatGPT

Owns:

- source interpretation;
- page jobs and semantic structure;
- visible-copy authority;
- feedback lifecycle and supersession;
- page ancestry;
- layout archetype choice;
- lock and unlock decisions;
- acceptance-standard changes.

Planner authority is immutable to downstream executors.

### 3.2 Executor Codex

Owns:

- faithful implementation of the frozen specification;
- build and rendering;
- deterministic implementation details;
- reproducibility;
- source/result manifests;
- bounded diffs;
- local smoke tests.

Executor does **not** own:

- new audience-visible content;
- semantic repairs to Planner authority;
- changes to the acceptance standard;
- final validation of its own work;
- human-visible PASS claims.

### 3.3 Independent deterministic validator

Runs only after the executor has stopped writing the candidate.

Preferred execution order:

1. **fresh CI / fresh process / clean checkout** at the candidate commit;
2. **fresh read-only Codex subagent** with artifact-only inputs when CI/process isolation is unavailable;
3. same executor process only for debugging, never for authoritative acceptance.

The validator must:

- use a pre-existing, version-pinned validation runtime;
- have read-only access to Planner authority and candidate artifacts;
- have no permission to edit candidate, tests, fixtures, or authority;
- receive no executor scratchpad, self-review narrative, expected failure list, or hidden answer key;
- resolve the candidate by exact repository/commit/hash;
- run production detectors, accepted controls, historical regression replay, and protected-path checks;
- emit machine-readable evidence and a deterministic verdict.

The authoritative validator cannot be authored or modified in the same bounded deck-revision task.

### 3.4 Independent rendered-artifact reviewer

A separate fresh GPT Work/reviewer run inspects the final render after deterministic validation passes.

It receives:

- exact artifact binary/render;
- page IDs and review scope;
- frozen visible-copy/layout contract;
- relevant source anchors;
- reviewer rubric.

It does not receive:

- executor completion narrative;
- expected human-rejection answers;
- “what was fixed” prose that can prime the review;
- permission to reinterpret deterministic failures.

It reviews hierarchy, reading path, whitespace, semantic proximity, audience effort, visual consistency, and pedagogical sufficiency.

### 3.5 Acceptance aggregator

A small deterministic aggregator combines:

- deterministic validator result;
- rendered reviewer result;
- unresolved NOT_INDEPENDENTLY_VERIFIED gates;
- current human locks;
- current delta scope.

It cannot convert a failure into PASS.

### 3.6 User

The user sees only the bounded delta after the previous layers pass.

Explicit user acceptance immediately creates an immutable page/component lock until a named unlock is issued.

## 4. Subagent policy

A subagent can provide useful review separation, but “a subagent exists” is not sufficient independence.

A Codex subagent is acceptable for deterministic or rendered review only if all of the following hold:

- fresh context;
- no executor chain-of-thought or scratchpad;
- no answer key;
- exact artifact/commit binding;
- read-only candidate and authority;
- validator/reviewer runtime fixed before the candidate task;
- no ability to edit tests or acceptance rules;
- output is persisted and hash-bound.

If those conditions cannot be guaranteed, prefer an external process or CI job.

The outer orchestrator, not the executor, launches the independent reviewer.

## 5. Candidate/evidence commit protocol

Use two trust-separated commits for substantial revision runs.

### Commit A — candidate

Contains only the executor's bounded implementation and generated audience artifacts/evidence required by the frozen production specification.

Executor stops after A and reports:

```text
CANDIDATE_COMMIT = A
READY_FOR_INDEPENDENT_VALIDATION = YES
```

### Commit B — validation evidence

Created by the independent validation stage or evidence publisher.

It contains only:

- validator report;
- detector coverage;
- candidate hashes;
- source/authority hashes;
- review scope;
- rendered-review references;
- acceptance aggregation.

B names A as its reviewed subject.

The validator verifies the actual remote branch state rather than trusting executor-supplied SHA strings.

## 6. Validation runtime immutability

For ordinary presentation production, the validator runtime is a dependency, not a deliverable.

A candidate task may not modify:

- validator code;
- detector catalog;
- historical regression fixtures;
- reviewer prompt;
- acceptance aggregator;
- quality thresholds.

If a genuine validator defect is found:

1. stop the candidate task;
2. repair the validator in the presentations plugin;
3. independently review the validator change;
4. version/release the validator;
5. rerun the candidate from the frozen candidate commit.

This prevents “edit the test until my candidate passes.”

## 7. Historical rejection corpus

Human-rejected real decks are holdout/regression assets.

Required classes include:

- template/header/footer regressions;
- page-lock violations;
- whitespace and semantic-proximity failures;
- count/rate/offset under-explanation;
- Bayesian-content deletion;
- wrong page ancestry;
- audience-visible internal/provenance language;
- code/PDF-copyability defects;
- evidence self-certification failures.

The executor does not receive expected finding lists for blind reviewer calibration.

A small sentinel subset may be used for capability calibration; the rest remains holdout evidence.

## 8. Honest detector states

Every required detector has one of:

- `EXECUTED_PASS`: real production input existed and passed;
- `EXECUTED_FAIL`: real production input existed and failed;
- `SPEC_READY_NOT_EXECUTED`: detector and hook are frozen but the needed candidate artifact does not yet exist;
- `BLOCKED`: implementation or evidence is missing.

Future visible-copy/render detectors must not be reported as PASS during governance-only work.

## 9. Monotone revision contract

For existing-deck revision:

```text
open_pages_next <= open_pages_current
locked_pages_next >= locked_pages_current
unrelated_changes = 0
```

A round may modify only the explicit allowlist.

The review package contains:

- changed pages;
- minimal context pages;
- affected shared components;
- feedback IDs addressed;
- proof that all other locks remain unchanged.

The user should never need to re-review the whole deck merely because one page changed.

## 10. Escalation rule after repeated control-plane failure

Do not continue indefinitely with V5/V6/V7 bounded patches.

If the current STAT5060 V4 governance repair again exhibits a **new P0 self-certification class**, such as:

- fixture-specific test bypass;
- validator edited to match the candidate;
- production hook not actually used;
- fake/stale evidence identity;
- protected-path proof that is not derived;
- another globally valid but semantically wrong mapping accepted;

then:

```text
PROJECT_LOCAL_GOVERNANCE_PATCHING = STOP
VISIBLE_COPY_FREEZE = BLOCKED
```

The next action is a generic validator rebuild in `AI_Skills_Collection`, not a STAT5060 V5 patch.

That rebuild must:

1. preserve the frozen STAT5060 authority and candidate history unchanged;
2. implement a standalone, pre-versioned validator package/runtime;
3. use black-box interfaces from candidate commit + authority bundle -> evidence;
4. run in fresh process/CI with read-only candidate access;
5. replay V1/V2/V3 governance failures and rejected presentation artifacts;
6. include at least one unrelated deck;
7. pass a held-out rejection corpus not exposed to the executor;
8. receive independent Critic/Planner review before reuse in STAT5060.

Only after that generic validator is released may STAT5060 resume at the exact-copy stage.

A simple implementation typo that does not reveal a new trust-boundary failure may receive one narrowly bounded correction; a new self-certification class triggers the rebuild rule above.

## 11. Promotion gate

The generic presentations workflow is not mature until a real deck demonstrates all of:

- executor cannot declare its own final acceptance;
- independent validator runs after executor stop on exact candidate commit;
- validator runtime is immutable during the candidate task;
- accepted controls and negative mutations run through the same production hooks;
- no fixture-name branches;
- blind rendered review is isolated from executor narrative and answer keys;
- locks grow monotonically across two to four user review rounds;
- unrelated pages remain byte/pixel stable where required;
- one unrelated deck succeeds under the same workflow;
- a held-out historical rejected artifact is still rejected.

## 12. Boundary

STAT5060-specific page IDs, exact comments, course content and numerical values remain course-repository fixtures.

The generic plugin owns trust separation, validator immutability, independent execution transport, evidence binding, blind review and monotone convergence.
