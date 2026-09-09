# Final Report

## What this task solved

Task 051 has produced a real successor candidate for the existing `writing-style` plugin's heavy Chinese scientific/technical rewrite path and proved that a normal installed-plugin request can route into the new heavy path without forcing the user to name internal implementation stages. The task also established repo-local candidate replay evidence, known-regression replay, complete-report replay, fresh-holdout evaluation, and independent Text Review evidence.

The task is not eligible for final PASS or integration. The user-authorized bounded recovery was executed, but its newly frozen fresh holdout failed the second independent Text Review. The recovery budget and authorization for this cycle are now exhausted, so the Scheduled Planner must return to a real human decision rather than silently opening a third holdout or another paid review.

## What changed

The current recovery implementation candidate is frozen at `2690de2cbc3d4ffb0741ecb80297a569647051f2`. The earlier production behavior candidate `ee8dd6edda2a2e4dd8f3210504225a56432b11a0` had already established ordinary heavy-route behavior. The recovery candidate adds a generic reader-facing guard against workflow/CI/commit/path leakage and replays Gate 3 A/B from complete source context without changing Gate 3 C.

The authorized recovery regenerated Gate 3 A/B through the normal production route, retained Gate 4, froze one new fresh Gate 5 holdout, and consumed exactly one additional independent Text Review call. The second Text Review passed recovered Gate 3 A/B, existing Gate 3 C, and Gate 4, but returned `REVISE` for the new Gate 5 holdout.

No final CI, release/version closure, install/upgrade smoke, GPT Reviewer PASS, or integration has been started after this failure.

## New capabilities / behavior

The candidate continues to demonstrate the intended heavy Chinese rewrite architecture: ordinary long Chinese source-faithful rewrite requests route to `scientific-rewrite`; short/local Chinese polish, fidelity-only work, and English `scientific-prose` remain separate; host Codex remains the generation owner; formal realization is meaning-driven rather than raw-source paragraph paraphrase; structured semantic audit/repair remains separated from drafting; and production generation does not use paid external generation calls.

The recovery also shows that the previously identified Gate 3 A/B truncation/internal-note defects can be corrected when complete source context is available. The second Text Review explicitly passed the recovered Gate 3 A/B artifacts, Gate 3 C, and Gate 4.

## Deliberately not adopted / unchanged

051 still does not rename the `writing-style` plugin, introduce a second generation runtime, restore per-stage paid generation, use fixed-size heavy chunking as the semantic planner, treat arbitrary Latin spans as exact identities, or turn candidate replay into another workflow/runtime manager.

The failed recovery holdout is not being repaired, reused, replaced, or chased automatically. No third holdout is being selected. No third paid Text Review call is being sent. No final CI or integration is being started from a failed product/artifact gate. These stops are deliberate consequences of the frozen holdout policy and the bounded human authorization already consumed.

## Example usage

A normal user-facing request the candidate is intended to support is:

> 把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢；不要逐句翻译，也不要总结掉内容。

Another valid request is:

> 内容都对，但现在像项目备忘录。按原意重新讲清楚，让第一次看的研究者能顺着读下去，正式算法名和数据集名保留。

Short local polishing, fidelity-only checking, and English scientific prose remain on their existing routes.

## Regression and remaining limitations

The latest independent Text Review is valid and returned `REVISE`. It passed the recovered Gate 3 A/B artifacts, Gate 3 C, and Gate 4. It found two blocking problems only in the newly frozen Gate 5 recovery holdout:

1. The reader-facing candidate contains an explicit source-missing/recovery note rather than only normal article prose.
2. The candidate ends immediately after introducing the state-space model, before the promised equations and matrix definitions, leaving the final artifact materially incomplete.

The failed recovery holdout source is the frozen Kalman-filter excerpt recorded in `results/051_writing_style_rebuild/recovery/new_holdout_manifest.json`. The batch is therefore failed under the frozen unseen/holdout policy. Its failure cannot be erased by editing that holdout, replacing it inside the same batch, or drawing another item automatically.

The user had explicitly authorized one bounded recovery after the first Text Review failure: generic non-holdout repair, one new frozen fresh holdout, and exactly one additional candidate-only Text Review under the same privacy/provider boundary. That authorization has now been fully consumed. The current Plan is already at `plan_revision=1` with `max_plan_revisions=1`, so Scheduled GPT cannot silently revise the acceptance contract again.

A further attempt is possible only through a fresh human decision. The defensible recovery would first prove a generic incomplete-source/reader-facing-boundary repair on non-holdout material, then freeze one new complete-source holdout batch before evaluation, and then run exactly one additional independent Text Review. That would be a new authorization; it is not pre-authorized by the current recovery cycle. The alternative is to stop 051 and record that it did not reach the frozen final generalization/product PASS bar.

Required final CI remains pending by design. If a later human-authorized recovery succeeds, final closure still requires focused and unrelated regressions, source/generated parity, candidate replay workflow consistency, version/changelog/release preflight, explicit heavyweight integration/release CI on the task branch, real install/upgrade smoke, ordinary black-box heavy-routing smoke, GPT Reviewer PASS, and integration to the then-current `main`.

## Technical appendix

- Task branch: `reviewed/051_writing_style_rebuild`
- Current recovery implementation commit: `2690de2cbc3d4ffb0741ecb80297a569647051f2`
- Earlier production behavior candidate: `ee8dd6edda2a2e4dd8f3210504225a56432b11a0`
- Frozen Plan revision: `1` of maximum `1`
- Current CI status: `PENDING`; final release/integration CI has not started
- Latest Text Review evidence: `results/051_writing_style_rebuild/text_review/TEXT_REVIEW.json`
- Latest Text Review decision: `REVISE`
- Latest Text Review workflow run: `34374037235`
- Latest Text Review paid call number: `2`
- Latest Text Review actual model cost: USD 0.064988
- Latest Text Review blocking findings: `2`
- Recovery fresh-holdout manifest: `results/051_writing_style_rebuild/recovery/new_holdout_manifest.json`
- Recovery status before this Planner transaction: `ADDITIONAL_TEXT_REVIEW_REVISE_NEW_HOLDOUT_FAILED_STOP_NO_THIRD_HOLDOUT`
- No production implementation file is modified by this Planner transaction.
