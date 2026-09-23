# workflow-core Changelog

## Unreleased

No pending released changes.

## 0.3 - 2026-09-22

Before:

- Verified Workflow described source discovery, specialist routing, verification
  and status reporting, but did not carry the 056 Product Delivery Discipline as
  a normal production-entry behavior.
- Agent-resolvable source/environment/test issues could be mistaken for user
  questions, and broad green tests could be overclaimed as user-ready evidence.

After:

- Added W1-W5 delivery discipline: acceptance review admission with applicable
  vertical/post-action closure, HUMAN_ONLY dependency triage, evidence-surface
  fidelity, repeat-failure circuit breaker, and change-impact protection.
- Required Default-mode HUMAN_ONLY gates to use durable transcript wait/resume
  semantics, with no dependent execution and recoverable achieved=no reporting
  at the legal run boundary.
- Strengthened existing Source Discovery enforcement: reuse verified local
  canonical source or task-owned worktrees before network cloning, protect
  unrelated dirty work, and avoid remote remapping as a source-discovery fix.

## 0.2 - 2026-09-20

Before:

- Reusable workflow task templates still showed numbered task keys as the default new-task shape.
- Verified Workflow did not explicitly separate machine task identity from human labels, UI titles, or plugin display names.
- Release gate selection guidance did not spell out regression-bank-first execution, narrow-gate eligibility, broad/full fallback triggers, or final-candidate evidence binding.

After:

- New workflow tasks defer to the workflow owner's canonical task-key contract and use semantic `<scope-token>--<goal-token>` keys for Bridge / Reviewed Handoff creation, while legacy numbered keys remain compatibility-only.
- Human labels, sidebar titles, thread names, and plugin `display_name` values are presentation metadata and cannot generate or override machine task keys.
- Release planning maps known regressions to existing gates first, runs cheap deterministic regression-bank checks before expensive/fresh review, escalates shared-runtime/routing/Marketplace/artifact/credential/cross-plugin changes to broad/full gates, and binds release claims to one final candidate.

## 0.1 - 2026-08-30

Initial independent plugin baseline in AI_Skills_Collection repository `5.0.0`.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
