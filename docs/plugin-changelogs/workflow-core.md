# workflow-core Changelog

## Unreleased

No pending released changes.

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
