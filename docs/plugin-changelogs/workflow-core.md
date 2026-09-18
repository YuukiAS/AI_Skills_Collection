# workflow-core Changelog

## Unreleased

No pending released changes.

## 0.2 - 2026-09-18

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

## 0.1 - 2026-08-30

Initial independent plugin baseline in AI_Skills_Collection repository `5.0.0`.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
