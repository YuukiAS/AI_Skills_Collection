# Final Report

## What this task solved

Frontend Design no longer starts generic UI work by choosing among peer specialist workflows. The production `web-development` plugin now has one normal coordinator-first entry: it enters `frontend-visual-systems`, classifies task scale, design authority, target surface and evidence needs, and then selects only the delegates needed for that job.

This removes the main failure mode the task was designed to fix: specialist routes such as research-product frontend planning can no longer bypass the generic Frontend Design coordinator.

## What changed

The shared Marketplace generator now supports a minimal opt-in `coordinator-first` aggregate mode. Aggregates that do not opt in retain their original choose-one behavior.

For `web-development`:

- `frontend-visual-systems` is the coordinator;
- product UX, visual direction, tokens, Figma handoff, motion, responsive/accessibility review, browser testing and research-product frontend are delegates;
- the former peer generic research route is removed from the active generated plugin surface while its canonical source remains available as a specialist delegate;
- `frontend-reference-research` remains a narrow explicit entry;
- `implementation-react-tailwind` remains downstream and is not promoted to design owner.

The source skills also now preserve the approved scale, authority, browser/native evidence, producer-admission and handoff-reachability boundaries.

Release metadata was closed as repository `5.3.1` and `web-development 0.3`; all other central plugin versions remain unchanged and maturity remains `unclassified`.

## New capabilities / behavior

A normal Frontend Design request can now:

- enter one coordinator before specialist routing;
- distinguish a tiny S1 fix from a bounded S2 change or an S3 redesign;
- use canonical Figma when it is authoritative without making Figma mandatory for every project;
- complete no-Figma work through another durable authority/current production grammar where appropriate;
- keep browser evidence separate from native-WebView claims;
- require producer self-QA and safe handoff-action reachability before the user becomes first-line QA;
- use research-product frontend guidance without bypassing generic product/authority/surface classification.

The shared generator can express this behavior for opted-in aggregates without changing the default behavior of unrelated plugins.

## Deliberately not adopted / unchanged

The task did not add a new orchestrator Skill, plugin, workflow, state machine, ledger or Bridge Kit mechanism.

It did not modify Bobbio, Lucerna or Asteria. Their frozen sources were used read-only for compatibility/attribution replay.

It did not add a fourth synthetic project to force a maturity upgrade. All three real-project replays counted as compatibility/regression only, so `web-development` maturity correctly remains `unclassified`.

Clear Writing, Product UI Copy and the deferred writing-style items remain out of scope.

## Example usage

- “Redesign this dashboard” now enters the coordinator first and can be classified as a full redesign before visual/product specialists are selected.
- “Implement this canonical Figma screen” uses Figma as the design authority while project semantics still come from the project.
- “Fix the spacing on this existing button” can remain an S1 local repair without being forced through a full redesign process.
- “Review this native tray UI before asking me to click Choose folder” keeps native evidence and handoff-action reachability requirements instead of treating browser evidence as sufficient.
- “Plan a research-product interface” reaches research-specific guidance only after the generic coordinator has classified the task.

## Regression and remaining limitations

The final candidate passed targeted coordinator/generator tests, the 056 Frontend regressions, registry/validation/audit/catalog generation, the full unittest suite, candidate plugin replay, Bobbio/Lucerna/Asteria read-only replay, generated parity checks and the required GitHub CI workflow.

The three real-project replays prove compatibility/regression only. They do not establish a maturity promotion or universal frontend quality across all future projects.

One evidence status document contains a stale narrative command locator, while the canonical replay run JSON and final-candidate identity record the actual candidate used. This does not change the production payload or the review decision.

No merge to `main`, release-ref mutation or TODO closure is authorized by this review. Those remain a later integration decision.

## Technical appendix

Task:
`web-development--frontend-design-production-consolidation`

Reviewed branch:
`reviewed/web-development--frontend-design-production-consolidation`

Frozen implementation locator:
`256e9cbe9f674db5e934d49ba1cc784363a51507`

Production implementation commit:
`1bb4650d8192d829b850abaccee53773ef50e091`

G6 replay evidence commit:
`df01fac271e030f9259a1510034380e2ec422f76`

CI handoff / reviewed branch tip:
`df35fb70f99a644a2a572f9918a2d871947c9f7a`

GitHub Actions:
`Codex Marketplace` run `36374574654`

CI jobs:
- `codex-marketplace`: PASS
- `windows-sparse-checkout`: PASS
- `editable-install-smoke (ubuntu-latest)`: PASS
- `editable-install-smoke (windows-latest)`: PASS

Key evidence:
- `results/web-development--frontend-design-production-consolidation/validation/validation_summary.md`
- `results/web-development--frontend-design-production-consolidation/validation/generated_diff_and_hashes.md`
- `results/web-development--frontend-design-production-consolidation/final_candidate_identity.json`
- `results/web-development--frontend-design-production-consolidation/replay/candidate_routing_decisions.md`
- `results/web-development--frontend-design-production-consolidation/replay/candidate_source_evidence.json`
- `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.md`
- `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.json`
- `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_source_consumption.json`

Review decision:
`PROCESS PASS` and `PRODUCT / ARTIFACT PASS`.
