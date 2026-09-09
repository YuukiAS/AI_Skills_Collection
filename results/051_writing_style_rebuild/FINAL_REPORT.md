# Final Report

## What this task solved

Task 051 has produced and frozen a real successor candidate for the existing `writing-style` plugin's heavy Chinese scientific/technical rewrite path. The candidate is exercised through the ordinary installed-plugin route rather than a forced internal subskill call, and the production architecture keeps host Codex as the generation owner while preserving the frozen meaning-realization, structural-fidelity, repair-boundary, and no-paid-generation constraints.

The work is not yet eligible for final PASS or integration. Gate 6 independent Text Review returned `REVISE`, so this report records the exact human decision now required before any further repair or evaluation can occur.

## What changed

The implementation candidate is frozen at `ee8dd6edda2a2e4dd8f3210504225a56432b11a0`. It adds the heavy Chinese `scientific-rewrite` production path, updates Chinese realization and structural fidelity behavior, adds deterministic rewrite support, keeps generated plugin payloads in parity, and retains the repo-local candidate replay helper/documentation used to prove real candidate consumption.

Gate 2 ordinary installed-plugin routing passed. Gate 3 A/B/C known-regression candidate text was previously accepted by the user and its render-only defects were repaired without changing the hash-bound candidate text. Gate 4 complete private-report generation/render evidence passed and the independent Text Review also marked Gate 4 `PASS`. Gate 5 used a pre-frozen public-safe holdout and completed without holdout replacement or holdout-specific tuning, but the independent Text Review marked its reader-facing artifact `REVISE`.

The combined Gate 4/5 human qualitative gate was accepted before Gate 6, which authorized the single independent Text Review call already performed. No Gate 7 final CI, release/version closure, install/upgrade smoke, GPT Reviewer PASS, or integration has been performed yet.

## New capabilities / behavior

The frozen candidate can route a normal long Chinese source-faithful rewrite request into the new heavy path without the user naming `scientific-rewrite`, Meaning Map, Reader Plan, `REALIZE_MEANING`, stage packets, or validators. The route preserves the existing light Chinese polish, fidelity-only, and English `scientific-prose` paths rather than collapsing them into the heavy rewrite path.

The candidate also proves the intended process separation: raw-source understanding and semantic audit remain source-aware, formal realization does not re-present raw source prose as its drafting surface, targeted repair packets are structured rather than source-quotation based, assembly is not given global raw-source rewrite authority, and production generation records no paid external model calls.

## Deliberately not adopted / unchanged

051 does not rename the `writing-style` plugin, does not introduce a second generation runtime, does not restore per-stage paid generation, does not use fixed-size heavy chunking as the semantic planner, does not treat arbitrary Latin spans as exact identities, and does not turn the candidate replay helper into a generic runtime manager or another workflow state machine.

The failed frozen holdout is not being replaced or chased automatically. The accepted Gate 3 A/B text is not being silently edited after the fact. No second independent paid Text Review call is being made automatically. These are intentional stops required by the frozen Plan and Reviewed Handoff contract.

## Example usage

A normal user-facing request that the candidate is intended to support is:

> 把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢；不要逐句翻译，也不要总结掉内容。

Another valid heavy-route request is:

> 内容都对，但现在像项目备忘录。按原意重新讲清楚，让第一次看的研究者能顺着读下去，正式算法名和数据集名保留。

Short local polishing, fidelity-only checking, and English scientific prose remain on their existing routes rather than entering this heavy path.

## Regression and remaining limitations

Gate 6 independent Text Review is valid and returned `REVISE` with three blocking findings:

1. Gate 3 A contains unfinished/truncated reader-facing text and internal editing notes such as material-missing explanations.
2. Gate 3 B contains multiple truncation notices, missing numbering, and source-condition explanations that break continuity and expose internal handling.
3. Gate 5 mixes the reader-facing research summary with review-workflow state, CI/test metadata, commit identifiers, model labels, and file paths, so it is not a clean reader artifact.

Gate 3 C and Gate 4 passed the same independent review. The findings therefore do not invalidate the already-proven ordinary routing mechanism, but they do block the frozen Plan's final product/artifact acceptance claim.

Automatic recovery is not authorized. Repairing Gate 3 A/B would change text that was previously accepted and hash-bound, which the Plan explicitly says reopens human/Planner decision. Gate 5 is a frozen holdout batch; the Plan explicitly says a failed holdout is a failed batch and that consuming a later fresh batch requires a new explicit human decision. The one allowed Planner revision has already been used (`plan_revision=1`, `max_plan_revisions=1`).

The Text Review manifest records authorization for exactly one candidate-only private review call, maximum one call and USD 0.25 reserved cost. That authorized call has been consumed. The resulting evidence embeds a broader campaign contract (`max_paid_calls=2`, USD 0.50 campaign ceiling), but that metadata does not supersede the narrower user authorization or frozen Plan. No second paid review may be sent unless the user explicitly authorizes the recovery path and its additional review call.

The required human decision is therefore whether to authorize a bounded recovery cycle that (a) permits repair/regeneration of Gate 3 A/B despite the earlier text acceptance, (b) treats the current Gate 5 batch as failed and permits one newly frozen fresh holdout batch without holdout-specific tuning or adaptive chasing, and (c) permits exactly one additional candidate-only independent Text Review call under the same provider/privacy boundary with no automatic retry and an additional worst-case reservation ceiling of USD 0.25. If this recovery is not authorized, 051 cannot truthfully reach final PASS under the current acceptance contract.

Gate 7 final CI remains pending by design because the artifact gate has not closed. Required final checks still include focused and unrelated regressions, source/generated parity, candidate replay workflow consistency, version/changelog/release preflight, explicit heavyweight integration/release CI on the task branch, and real install/upgrade plus ordinary black-box heavy-routing smoke. These must run only after an authorized artifact recovery succeeds.

## Technical appendix

- Task branch: `reviewed/051_writing_style_rebuild`
- Frozen implementation commit: `ee8dd6edda2a2e4dd8f3210504225a56432b11a0`
- Frozen Plan revision: `1` of maximum `1`
- Current required CI status before this human gate: `PENDING`; Gate 7 final CI not started
- Gate 6 Text Review decision: `REVISE`
- Text Review evidence: `results/051_writing_style_rebuild/text_review/TEXT_REVIEW.json`
- Text Review manifest: `results/051_writing_style_rebuild/text_review/text_inputs.json`
- Text Review workflow run: `34360618786`
- Text Review actual model cost: USD 0.066460; reserved worst-case cost for the consumed call: USD 0.116207
- Gate 3 accepted-text evidence and render QA: `results/051_writing_style_rebuild/RESULT.md`
- Gate 5 frozen holdout manifest: `results/051_writing_style_rebuild/gate5_holdout_manifest.json`
- Gate 4/5 combined human acceptance is recorded in `results/051_writing_style_rebuild/RESULT.md`
- No production implementation file is modified by this Planner transaction.
