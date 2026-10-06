# Independent Review Contract

This shared contract applies to non-trivial presentation planning, production, and revision.

It separates three different review jobs:

1. **prebuild Critic** — judges whether the Planner specification is ready;
2. **postbuild deterministic/rendered review** — judges the exact candidate artifact;
3. **GPT Work final gate** — judges aesthetics, reader effort, and whole-deck communication on the exact immutable render.

These jobs are not interchangeable.

## 1. Prebuild Critic gate

### 1.1 When required

A fresh read-only prebuild Critic is mandatory for:

- failed-version recovery;
- major revision;
- substantial high-risk new teaching/research/decision decks;
- any revision changing page count, section order, page jobs, shared shell, layout archetypes, broad visible copy, or scientific/pedagogical meaning;
- any case where a closed historical guard has recurred or the Planner may have misread cumulative feedback.

A bounded minor revision may skip a separate Critic only when:

- page count, section order, page jobs, shell, and archetypes remain unchanged;
- scope is normally at most three pages and one already-defined component;
- copy changes are local and source-supported;
- no closed guard has recurred;
- ChatGPT Planner freezes the exact allowlist, locks, and active guard bundle.

If uncertain, classify as major.

### 1.2 What the Critic reviews

The Critic receives read-only Planner authority and source/history evidence. It must verify:

- exact source and historical-feedback consumption;
- page count and sequence;
- every page job and required/forbidden object;
- content correctness and audience sufficiency;
- student/audience versus presenter/instructor/internal boundary;
- visible-copy completeness;
- layout/archetype suitability;
- historical-regression protection;
- the proposed autonomous Codex Controller and review loop.

It returns:

- `PASS`; or
- `REVISE` with a bounded Planner-amendment list; or
- `BLOCKED_HISTORY_NOT_CONSUMED` / source-equivalent block.

The Critic does not author slides or repair the specification itself.

A major Planner amendment after Critic review requires a fresh Critic pass before production.

## 2. Executor trust separation

The agent/process that edits a candidate deck or its acceptance implementation is the **executor**. It may build, render, run smoke checks, and prepare evidence, but it may not authoritatively accept its own candidate.

The strongest executor completion state is:

```text
READY_FOR_INDEPENDENT_VALIDATION = YES
```

Do not report final `PASS`, release readiness, or human acceptance from executor self-review.

## 3. Authoritative deterministic validation

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

## 4. Subagent requirements

A subagent is independent only when all of these hold:

- fresh context;
- artifact/commit-bound input;
- read-only candidate and authority;
- no expected human-rejection answer key;
- no permission to edit tests, detector code, or gates;
- no access to executor chain-of-thought/scratchpad;
- persisted output with exact artifact identity.

If these cannot be guaranteed, do not treat the subagent as authoritative validation.

## 5. Independent rendered-artifact review

After deterministic validation passes, run a separate blind rendered review.

The reviewer receives:

- exact final render;
- PageIDs and review scope;
- frozen copy/layout/component contract;
- relevant source anchors and active guards;
- review rubric.

Do not provide executor completion prose or expected failure answers.

Rendered review covers:

- hierarchy and reading path;
- scientific/decision object scale;
- whitespace and semantic proximity;
- audience language;
- visual consistency and whole-deck rhythm;
- pedagogical or decision sufficiency;
- historical visual recurrence.

A rendered reviewer cannot override deterministic failures.

## 6. GPT Work final gate

GPT Work is the final independent aesthetic, reader-effort, and communication review for formal decks.

### Major/new/recovery candidate

GPT Work reviews all pages and the full contact sheet on the exact immutable candidate.

### Minor bounded revision

GPT Work may review only:

- changed pages;
- affected shared-component consumers;
- minimum context pages;
- the full contact sheet;

provided page count, section order, shell, page jobs, and archetypes remain locked. Final release still requires one complete whole-deck regression.

GPT Work:

- does not implement fixes;
- does not change scientific/statistical meaning;
- does not override deterministic failures;
- returns `PASS` or `REVISE` with page/component-scoped findings;
- on `REVISE`, routes findings back through a fresh Producer and then a fresh deterministic/rendered review before another GPT Work pass.

## 7. Acceptance aggregation

Final presentation acceptance is the conjunction of:

- required prebuild Critic PASS;
- deterministic validation PASS;
- no unresolved mandatory `NOT_INDEPENDENTLY_VERIFIED` gate;
- rendered-artifact review PASS;
- GPT Work PASS when required;
- required user/human decisions PASS;
- all previous locks preserved.

The aggregator cannot convert a failure to PASS.

## 8. Revision monotonicity

For existing-deck revision:

```text
open_pages_next <= open_pages_current
locked_pages_next >= locked_pages_current
unrelated_changes = 0
```

Only explicitly authorized pages/components may change. User review should receive changed pages plus minimal context, not a full-deck re-annotation request.

## 9. Repeated-control-failure escalation

If an implementation round reveals a new P0 self-certification class—test-specific bypass, validator edited to fit the candidate, stale/fake evidence identity, production hook not used, or protected-path proof not derived—do not continue indefinite project-local patch versions.

Freeze the candidate and authority, move validator repair to the presentations plugin, independently review/version the validator, replay historical failures plus an unrelated deck, then return to the frozen candidate.

A simple mechanical defect may receive one bounded correction; a new trust-boundary failure triggers the generic rebuild route.
