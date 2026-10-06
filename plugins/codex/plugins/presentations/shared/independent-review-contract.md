# Independent Review Contract

This shared contract applies to non-trivial presentation production and revision tasks.

## Trust separation

The agent/process that edits a candidate deck or its acceptance implementation is the **executor**. It may build, render, run smoke checks, and prepare evidence, but it may not authoritatively accept its own candidate.

The strongest executor completion state is:

```text
READY_FOR_INDEPENDENT_VALIDATION = YES
```

Do not report final `PASS`, release readiness, or human acceptance from executor self-review.

## Authoritative deterministic validation

Run deterministic acceptance only after the executor stops writing the candidate.

Preferred transport:

1. fresh CI job or fresh process on a clean checkout of the exact candidate commit;
2. fresh read-only subagent with isolated context when process/CI separation is unavailable;
3. same executor process only for debugging, never as authoritative acceptance.

The authoritative validator must:

- bind to exact repository, commit, artifact hashes, and authority hashes;
- use a pre-existing version-pinned validator/detector runtime;
- treat Planner/user authority as read-only;
- have no permission to change candidate source, fixtures, detectors, thresholds, or acceptance rules;
- receive no executor scratchpad or self-review narrative;
- execute the same production detector functions for real validation, accepted controls, and negative mutations;
- reject fixture-name branches and magic-value-only predicates;
- persist machine-readable evidence.

If a validator defect is found, stop the deck task and repair/version the validator separately before rerunning the frozen candidate.

## Subagent requirements

A subagent is independent only when all of these hold:

- fresh context;
- artifact/commit-bound input;
- read-only candidate and authority;
- no expected human-rejection answer key;
- no permission to edit tests, detector code, or gates;
- no access to executor chain-of-thought/scratchpad;
- persisted output with exact artifact identity.

If these cannot be guaranteed, do not treat the subagent as authoritative validation.

## Rendered-artifact review

After deterministic validation passes, run a separate blind rendered review.

The reviewer receives the final render, page IDs, frozen copy/layout contract, relevant source anchors, and review rubric. Do not provide executor completion prose or expected failure answers.

Rendered review covers hierarchy, reading path, whitespace, semantic proximity, audience effort, visual consistency, and pedagogical/decision sufficiency.

A rendered reviewer cannot override deterministic failures.

## Acceptance aggregation

Final presentation acceptance is the conjunction of:

- deterministic validation PASS;
- no unresolved mandatory `NOT_INDEPENDENTLY_VERIFIED` gate;
- rendered-artifact review PASS;
- required user/human decisions PASS;
- all previously locked pages/components preserved.

The aggregator cannot convert a failure to PASS.

## Revision monotonicity

For existing-deck revision:

```text
open_pages_next <= open_pages_current
locked_pages_next >= locked_pages_current
unrelated_changes = 0
```

Only explicitly authorized pages/components may change. User review should receive changed pages plus minimal context, not a full-deck re-annotation request.

## Repeated-control-failure escalation

If an implementation round reveals a new P0 self-certification class—test-specific bypass, validator edited to fit the candidate, stale/fake evidence identity, production hook not used, or protected-path proof not derived—do not continue indefinite project-local patch versions.

Freeze the candidate and authority, move validator repair to the presentations plugin, rebuild/review the generic validator independently, replay historical failures plus an unrelated deck, then return to the frozen candidate.

A simple mechanical defect may receive one bounded correction; a new trust-boundary failure triggers the generic rebuild route.
