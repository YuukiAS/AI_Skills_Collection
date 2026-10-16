# Presentations TODO — Production Detector Authenticity and Evidence Binding

Date: 2026-10-06  
Status: **P0 DESIGN INPUT / PROMOTE WITH HISTORY-LOCK CONVERGENCE WORK**  
Primary evidence: independent review of STAT5060 Tutorial 01 governance V3 at commit `48d76637fc4f25dcc94fc1190926f0ea09bbfd39`

## 1. Why this TODO exists

The third STAT5060 recovery implementation corrected the frozen annotation totals, structured direct-decision intake, Planner-source mutation checks and base-to-local audience diff. It still returned `PASS` while several core invariants were not actually enforced.

The remaining failure is more specific than a weak checklist:

> A system can expose separate materializer and validator files, realistic-looking fixtures and correct headline metrics while the tests still bypass the production invariant.

Observed examples:

- persisted row validation checked that target IDs were globally valid, but did not compare them with the exact allowed stable/component targets for each historical artifact page;
- negative ancestry tests branched on fixture names rather than calling the persisted-registry ancestry validator;
- positive controls asserted constants stored in JSON rather than passing accepted real inputs through production detectors;
- persisted `git_blob_sha` values were file paths because `git rev-parse <path>` was used instead of resolving `<commit>:<path>`;
- the validator used the same defective object helper and self-certified the path strings;
- final and remote commit arguments were checked only for 40-hex syntax, not against local HEAD or the actual remote branch;
- a no-audience-change flag was hard-coded even though the surrounding proof was presented as derived;
- the frozen detector catalog was not used to prove implementation and test coverage for every required detector family.

## 2. Production-hook requirement

Each detector must have one production function and one declared production validation hook:

```text
detector_id
implementation_function
production_hook
accepted_control_ids[]
negative_mutation_ids[]
phase_state
```

Fixtures and controls call that same function. A test-only predicate does not count as a detector.

Forbidden patterns:

- branching on fixture name or fixture ID;
- implementing one predicate inside the mutation runner but not the real validator;
- checking only global ID validity when the invariant is artifact/page-specific;
- storing an expected answer inside the fixture and comparing it without reading authority;
- reporting a future-artifact detector as PASS when no candidate artifact exists.

## 3. Accepted controls must execute the detector

A positive control is not a constant assertion such as:

```python
assert counts == {"objects": 193, "highlights": 187, "text": 6}
```

The accepted source/registry/candidate must pass through the same detector used in production and negative tests.

Required evidence per executable detector:

- accepted real input identity;
- detector invocation;
- result and evidence output;
- at least two distinct negative mutations where the domain permits;
- zero fixture-name branches.

## 4. Row-level ancestry means allowed-target enforcement

For each feedback row, validation must compare:

```text
raw artifact filename
+ exact artifact lineage ID
+ raw historical page/region
+ overlay historical page/region
+ persisted target set
+ exact allowed stable_targets/component_targets/disposition
```

A target may be globally valid and still invalid for the specific historical page. Checking only that a page-map record exists is insufficient.

The production row validator must also handle:

- artifact-wide/global feedback;
- structured direct decisions;
- unresolved source-gap records;
- ambiguous historical version labels;
- exact raw-page versus overlay-page disagreement.

## 5. Git object identity must be an object ID

A persisted field named `git_blob_sha` must contain the committed blob object ID, not a path or ref string.

Required resolution:

```text
git rev-parse <commit>:<path>
```

or an equivalent object lookup. Validation requires 40 lowercase hex characters and an independent object comparison.

The following pattern is invalid:

```text
git rev-parse <path>
```

because Git may echo the path rather than resolve a blob.

## 6. Final/remote evidence without self-reference

A commit cannot reliably contain its own SHA. Do not solve evidence binding by storing a placeholder and checking only that user-supplied strings look like SHAs.

Use a two-commit protocol:

1. implementation commit `A` contains code and derivatives;
2. evidence commit `B` names `A` as the reviewed subject and contains only evidence/report artifacts;
3. runtime validation at `B` verifies local and actual remote branch head, subject ancestry, source identities and start-to-`B` protected paths.

No file needs to contain its own commit SHA.

## 7. Detector coverage matrix

The workflow must load the frozen detector catalog and generate one exact coverage row per detector:

```text
detector_id
implementation_function
production_hook
phase_state
accepted_controls[]
negative_mutations[]
fixture_name_branch_count
magic_value_or_phrase_dependency_count
```

Allowed phase states:

- `EXECUTED_PASS` — real production input exists and the detector passed;
- `SPEC_READY_NOT_EXECUTED` — detector schema/hook is frozen but no candidate artifact exists yet;
- `BLOCKED` — required implementation or authority is missing.

A future copy/render detector may not be reported as PASS during governance-only work.

## 8. Complete derivative fidelity

Independent validation covers every field, not only headline rows:

- exact unique ID set and record count;
- top-level schema/status/source identity;
- all page, row, component and gate fields;
- list/JSON mirror consistency;
- exact mandatory source path/role/immutability set;
- missing, extra and reordered records where order is authoritative.

## 9. Generic promotion consequences

The presentations history/lock system is not promotable until a real deck proves:

1. row-level allowed-target ancestry through the production validator;
2. accepted controls and negative mutations use the same detector functions;
3. no fixture-name branches or magic-value-only predicates;
4. actual committed Git object identities;
5. final local/remote evidence binding through a non-self-referential protocol;
6. exact detector-catalog coverage with honest phase states;
7. complete derivative fidelity;
8. zero protected-path changes from base to actual remote head.

## 10. Boundary

STAT5060 identifiers and exact feedback remain course-repository fixtures. Generic runtime should implement production-hook identity, accepted-control execution, object identity, two-commit evidence binding and detector coverage without embedding course-specific content.
