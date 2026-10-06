# Presentations Validator V1 — Frozen Specification

Date: 2026-10-06  
Status: **FROZEN PLANNER AUTHORITY**  
Owner: Presentations control plane  
Implementation repository: `YuukiAS/AI_Skills_Collection`

## 1. Purpose

Build a generic, versioned, read-only validator for non-trivial presentation creation and revision.

The validator exists because candidate executors repeatedly optimized proxies—counts, fixture totals, self-authored evidence and locally convenient mappings—while the intended presentation constraints were not enforced.

The validator must be reusable across teaching, research and business decks. Course/project-specific PageIDs, feedback text and numerical values remain external authority fixtures.

## 2. Trust boundary

The candidate executor and the authoritative validator are different trust domains.

For validator implementation itself:

- the implementation executor may write code and public tests;
- it may run local smoke/public tests;
- it may not see the Planner-held black-box acceptance pack;
- it may not declare the validator accepted;
- its strongest completion state is `READY_FOR_INDEPENDENT_VALIDATION`;
- a fresh process/session runs hidden acceptance after the executor stops.

For ordinary deck work after release:

- the released validator is a pinned dependency;
- a deck executor cannot modify validator code, detector catalog, thresholds, fixtures or acceptance semantics in the same task;
- validator defects stop the deck task and are repaired/released separately.

## 3. Required package boundary

Implement under one standalone package root:

```text
plugins/codex/plugins/presentations/shared/validator_v1/
```

Required public entry point:

```text
python -m presentations_validator_v1 validate \
  --authority-bundle <directory> \
  --candidate-bundle <directory> \
  --repo <repository-path> \
  --out <evidence.json>
```

The production package must not import project-local STAT5060 scripts.

## 4. Input model

### 4.1 Authority bundle

The authority bundle is immutable and separately hashed. It contains, as applicable:

```text
authority_manifest.json
artifact_lineage.json
feedback_authority.jsonl
page_authority.json
component_authority.json
acceptance_gate_authority.json
lock_ledger.json
round_scope.json
visible_copy_authority.json
required_object_registry.json
validator_policy.json
```

The validator derives all expected values from this bundle. It must never treat candidate-provided `expected_*`, `allowed_*`, copied authority fields or executor summaries as authority.

### 4.2 Candidate bundle

The candidate bundle contains claims and evidence only:

```text
candidate_manifest.json
patch_manifest.json
derived_feedback_registry.jsonl
derived_page_registry.json
derived_component_registry.json
derived_gate_registry.json
source_identity_manifest.json
render_identity_manifest.json
review_scope.json
```

Candidate fields may be checked for fidelity but never used to expand authority.

### 4.3 Repository binding

The bundle must bind:

```text
repository identity
baseline commit
candidate commit
candidate tree
actual local head when applicable
actual remote head when required
source and artifact blob identities
```

Git object IDs are resolved independently as `<commit>:<path>` or an equivalent object lookup and must be 40 lowercase hexadecimal characters.

## 5. Core validation invariants

### 5.1 Exact authority coverage

- exact record counts and unique ID sets;
- no missing, extra or duplicate feedback/direct-decision/page/component/gate/lock records;
- raw provenance fields remain byte-for-byte stable where specified;
- lifecycle vocabulary and supersession graph are valid and acyclic.

### 5.2 Row ancestry

For every feedback/direct-decision row, derive allowed targets only from immutable authority:

```text
exact artifact identity
+ historical page/region
+ authority disposition
-> allowed stable page/component target set
```

Required properties:

- global validity of a PageID is insufficient;
- candidate-copied allowed-target fields are ignored for authority;
- direct decisions use their structured target authority;
- source-gap rows use their structured disposition and cannot acquire an invented page;
- coordinated mutation of target and candidate-copied allowed fields must still fail;
- ambiguous version labels fail.

### 5.3 Round scope and locks

- every changed source/render object maps to an authorised PageID/component;
- modified IDs are a subset of the round allowlist;
- round-frozen and human-locked objects remain unchanged at the required semantic/copy/layout/body/component layers;
- shared-component changes automatically place every consumer page in deterministic regression scope;
- candidate claims of unchanged locks are independently verified.

### 5.4 Required-object preservation

- every required teaching/scientific/decision object remains present;
- deletion, merge, compression or relocation requires an explicit authority record;
- overflow, whitespace, build difficulty or page-count pressure never authorizes semantic deletion.

### 5.5 Exact copy and role fidelity

When visible-copy authority exists:

- all audience-visible strings, including figure/table/diagram/code text and PDF text layer, match approved copy after only explicitly permitted typesetting transforms;
- no executor-authored prose, title, caption, transition, warning, example or prerequisite is accepted;
- text roles are preserved.

### 5.6 Page/component/gate fidelity

- all top-level and record-level fields are independently compared with authority;
- JSON/list mirror fields are canonical and consistent;
- component consumers equal the exact inverse of page bindings;
- cumulative acceptance gates preserve every unretired predecessor requirement;
- missing, extra or reordered records fail where order is authoritative.

### 5.7 Protected-path and Git evidence

- compare baseline to candidate using changed paths and blob identities;
- clean worktree is never proof of no change;
- local/remote state is resolved from the repository, not trusted from CLI strings alone;
- evidence reports are bound to the exact candidate commit/tree;
- evidence status must be final, not pending or placeholder-bearing;
- implementation/evidence commit protocols, when used, verify exact allowed paths in the evidence commit.

### 5.8 Review-scope integrity

- reviewed and unreviewed requirements are explicit;
- scoped review cannot produce a global PASS when mandatory global requirements remain unreviewed;
- `NOT_INDEPENDENTLY_VERIFIED` is distinct from artifact failure and still blocks release where mandatory.

## 6. Production detector architecture

Each detector is registered by stable detector ID with:

```text
implementation function
input schema
production validation hook
phase state
accepted-control IDs
negative-mutation classes
evidence outputs
```

Allowed phase states:

- `EXECUTED_PASS`
- `EXECUTED_FAIL`
- `SPEC_READY_NOT_EXECUTED`
- `BLOCKED`

Rules:

- production detector functions never receive fixture/test names;
- no fixture-ID, mutation-ID, known bad value, phrase or hash branch;
- accepted controls, public mutations, hidden mutations and real candidate validation call the same production function;
- candidate and expected authority are separate inputs;
- coordinated multi-field mutations are expected;
- at least two semantically distinct negative mutation classes exist per executable detector where applicable;
- distinct IDs with identical canonical payloads do not count as distinct mutations.

## 7. Mutation and coverage integrity

The validator implementation must expose a mutation-testing API used by public and hidden tests.

Coverage evidence must be derived, not self-declared:

- detector registry is introspected at runtime;
- production-hook registration is checked from code/runtime objects;
- fixture-name branch count is derived by AST/static inspection of production modules;
- magic-value/phrase dependency checks are derived by AST/static inspection plus mutation replay;
- mutation distinctness uses canonical payload hashes and semantic mutation-class IDs;
- coverage cannot be satisfied by writing literal zeroes to CSV.

## 8. Evidence schema

The output evidence must include:

```text
validator version and code identity
authority bundle identity
candidate commit/tree/artifact identities
executed detector rows and phase states
review scope
all failures with target IDs and source authority
protected-path diff evidence
lock comparison evidence
mutation/accepted-control execution summary
unverified mandatory gates
final deterministic verdict
```

The output must not contain placeholders such as `<commit>` and must not retain a `PENDING` status at final validation.

## 9. Public tests and hidden acceptance

The executor writes public unit/property tests sufficient to document interfaces and major invariants.

Authoritative acceptance uses an external Planner-held black-box pack that is not committed to the executor branch. It includes:

- coordinated multi-field mutations;
- candidate/self-mirror tampering;
- evidence-binding and source-manifest mutations;
- lock/scope violations;
- historical-regression replay;
- at least one unrelated deck fixture.

The exact hidden payloads and expected findings are not part of the implementation prompt.

## 10. STAT5060 replay adapter

Provide a generic adapter/configuration, not course-specific detector code, that can ingest the frozen STAT5060 authority and replay subjects:

```text
START = 2c56ccb1d0e3a38ea7143541dc67b19b1b41733d
IMPLEMENTATION_A = 427cd1167540b23a616d3c0034d70451e1b968d8
EVIDENCE_B = a255e716cf7a846208a62edc82132c3752a16417
```

The adapter may map file locations into the generic bundle schema. It may not embed expected V4 failure answers in production detector code.

## 11. Executor deliverables

The implementation executor must produce:

- package source and schemas;
- CLI;
- public tests and property tests;
- generic fixture builders;
- STAT5060 bundle adapter;
- one synthetic unrelated example bundle;
- documentation;
- exact changed-file manifest;
- candidate commit.

It must not modify:

- this frozen specification;
- anti-shortcut or independent-review contracts;
- existing presentation deck artifacts;
- STAT5060 course authority;
- hidden acceptance material.

## 12. Completion semantics

Allowed executor result:

```text
RESULT = CANDIDATE_READY / STOP / FAIL
CANDIDATE_COMMIT = <sha>
READY_FOR_INDEPENDENT_VALIDATION = YES/NO
```

Forbidden executor claims:

```text
VALIDATOR_ACCEPTED = YES
PRODUCTION_READY = YES
STAT5060_READY_FOR_COPY_FREEZE = YES
```

Only an independent fresh validation run may accept the validator release.
