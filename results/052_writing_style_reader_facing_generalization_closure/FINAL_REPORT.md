# Final Report

## What this task solved

052 closes the two reader-facing defects left after 051 was stopped. Standalone Chinese or Chinese-dominant scientific/technical rewrites now state the technical content directly instead of narrating that they are rewriting a source, while legitimate scholarly attribution remains allowed. Independent Text Review packets now keep task/gate/recovery/candidate/reviewer wrapper information out of the reviewed prose body and place that identity in metadata instead.

The bounded product and review evidence now passes. This is not yet integrated to `main`: the frozen Plan requires one final human artifact decision after GPT Reviewer PASS.

## What changed

The heavy `scientific-rewrite` route, its Chinese realization/fidelity companion skills, and the generated `writing-style` plugin payload were updated to enforce a contextual reader-facing source-process rule. The helper mechanically rejects obvious standalone source-process framing while the skill contract distinguishes that failure from valid literature attribution and from user-requested comparison/review/provenance tasks.

Reviewed Handoff Executor/Reviewer guidance was also tightened so candidate-only Text Review plaintext uses natural document titles and excludes workflow wrappers. The 052 task additionally records the two frozen fresh holdouts, Bloom known-regression replay, unrelated regressions, the single Terra Text Review, release CI, version closure, and production install/routing smoke.

`writing-style` is prepared as version 0.2. Source/generated parity is intact for the reviewed skill payload and helper.

## New capabilities / behavior

A user can now ask for a long Chinese scientific or technical rewrite and receive a standalone explanation that talks about the method, formula, limitation, comparison, or attribution itself rather than saying things such as “原文指出”“根据给定材料” or “源文说明”. If the source genuinely attributes a claim to an author or paper, normal scholarly attribution remains valid.

The final independent review surface also behaves as intended: the reviewer sees only the real candidate documents under natural titles, while task ids, hashes, run ids, Gate labels, candidate/recovery labels, and Planner/Reviewer/Executor metadata stay outside the reader-facing plaintext.

## Deliberately not adopted / unchanged

051 remains stopped, not released, and historically failed its final Text Review. 052 does not rewrite 051 into PASS, reuse its paid-review budget, or treat the 051 Bloom result as a fresh holdout; Bloom is only a known regression.

052 does not add a new Bridge/runtime/Host Policy mechanism, does not rename `writing-style`, does not create an adaptive third holdout, and does not authorize a second Terra review. The source-process rule is not presented as universal writing-quality proof and does not suppress legitimate scholarly attribution or explicit source-comparison tasks.

## Example usage

A natural request is:

> 把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢。

For a normal standalone rewrite, the result should say the scientific content directly. For example, instead of “原文指出 FFT 能把复杂度降到……”，the candidate should simply explain that FFT reduces direct DFT computation from `O(N^2)` to `O(N log N)` and then state the relevant conditions or caveats.

If the user explicitly asks to compare a source, review a manuscript, trace provenance, or explain what an author wrote, source-oriented framing remains permitted because it is then part of the requested task rather than leakage.

## Regression and remaining limitations

The Bloom known regression passes as a historical failure replay, and the two fresh holdouts were frozen as a complete two-item batch before generation. They come from different public-safe document families: official Python `re` documentation and a technical encyclopedia article on FFT. Both final candidates were independently inspected in this review and are self-contained reader-facing technical prose without the two targeted leakage classes.

The single final `gpt-5.6-terra` Text Review returned PASS with zero blocking findings. Exactly one paid 052 call was actually consumed, automatic retry was 0, the worst-case reservation was USD 0.056690, and actual model cost was USD 0.010434. Full Codex Marketplace release CI completed successfully, and production smoke installed the 052 `writing-style` 0.2 identity, exercised ordinary routing, then restored the previous live 0.1 install.

The remaining limitation is intentional: this evidence supports only the bounded 052 reader-facing closure. It does not establish universal rewrite quality across arbitrary genres or languages. Final human ACCEPT and integration to the then-current `main` remain pending.

## Technical appendix

- Task branch: `reviewed/052_writing_style_reader_facing_generalization_closure`
- Reviewed implementation commit: `92ad279a11653486e726ed8cadb57bed5523af65`
- GPT review: `results/052_writing_style_reader_facing_generalization_closure/REVIEW_1.md`
- Bloom known regression: `results/052_writing_style_reader_facing_generalization_closure/known_regression/bloom_known_regression_manifest.json`
- Fresh holdout batch: `results/052_writing_style_reader_facing_generalization_closure/fresh_holdouts/fresh_holdout_batch_manifest.json`
- Final Text Review manifest: `results/052_writing_style_reader_facing_generalization_closure/text_review/text_inputs.json`
- Final Text Review evidence: `results/052_writing_style_reader_facing_generalization_closure/text_review/TEXT_REVIEW.json`
- Terra decision: PASS; blocking findings: 0
- Paid review calls actually consumed: 1; automatic paid retry: 0
- Worst-case reservation: USD 0.056690; actual model cost: USD 0.010434
- Release CI: Codex Marketplace workflow run `34492443098`, conclusion `success`
- Prepared plugin version: `writing-style` 0.2
- Production smoke: `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/smoke_verification.json`
- Production smoke result: install/upgrade PASS, ordinary routing PASS, previous production marketplace/plugin restored
- Required remaining gates: final human ACCEPT, integration to latest `main`
