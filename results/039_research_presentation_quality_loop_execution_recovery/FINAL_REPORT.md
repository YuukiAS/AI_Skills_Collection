# Final Report

## What this task solved

039 repaired the concrete generic blocker exposed by the first Stage 5 real-paper holdout: the shipped deck-quality loop can now consume structured visual-review findings that do not contain an internal `repair_intent`, map only unambiguous problem categories into the existing bounded repair vocabulary, and make those repairs affect the actual production layout and rendered pixels.

Before this recovery, the 038 holdouts received clear Terra findings but the consumer selected no repair because it expected a field that the real review contract did not provide. Some nominal repair paths also wrote hints that had no downstream visual consumer. The result was a nominal quality loop that safely stopped but could not exercise the one allowed source-faithful repair.

## What changed

The recovery retained the existing Visual Review contract and the existing one-cycle quality-loop state machine. Structured findings are normalized from their requirement/category, target logical page and scientific object into a small safe set of existing repair intents only when the mapping is unambiguous. Unknown or unsafe findings still fail closed.

The corresponding layout consumers now make bounded changes that are visible in the final render for the covered classes: removal of internal audience-facing meta copy, annotation/legend separation, primary scientific-object rescaling, compatible process-diagram reflow, and reservation of non-obstructive medical legend/callout space. Source claims, CUHK identity, gold scoring and medical source pixels remain protected.

A task-local unrelated-domain stress bundle exercised all five classes in one normal-quality-loop run. The state records exactly one repair cycle, changed render-input identity and changed rendered-pixel identity, demonstrating that the repair is not merely metadata.

## New capabilities / behavior

The first Planner review found one separate presentation-surface regression in the stress harness: the title slide exposed the engineering label `Stage 4 Quality Loop Repair Stress Update`. This did not invalidate the quality-loop execution mechanism, but it prevented the complete stress deck from meeting the same audience-facing bar used elsewhere in the Program.

The bounded revision changed only the stress input title to `Calibrating uncertainty in clustered data and testing segmentation robustness`, added a regression excluding the old engineering title, and regenerated the task-local outputs. It did not weaken or remove any of the five stress findings and did not change normal production behavior.

The durable new behavior is that a real structured Visual Review finding can now flow into one bounded, source-faithful production repair and produce changed render-input and rendered-pixel identities, while unknown or unsafe findings still fail closed.

## Deliberately not adopted / unchanged

039 did not continue repairing brms, MedSAM or any other Stage 5 holdout. It did not change the frozen source semantics, CUHK identity, gold scoring, medical source pixels, production entrypoint or one-repair budget. It did not treat the non-holdout stress deck as final program acceptance.

The failed 038 papers remain consumed failure evidence and remain disqualified from future unseen PASS claims.

## Example usage

普通用户仍按正常方式请求生成科研组会汇报。若最终页面出现明确、结构化且可安全修复的问题，例如内部制作语言外露、图注/legend 遮挡、主科研对象过小、流程图碰撞或医学图像 legend 阻挡，系统可以在已经 shipped 的一次 bounded repair 内尝试通用修复。

如果 visual finding 不明确、需要改 source claim、需要生成医学像素、需要第二次 repair 或需要 holdout-specific 规则，系统仍应 no-winner / fail closed，而不是悄悄调参到通过。

## Regression and remaining limitations

Real GitHub CI passed for the revised published handoff. Fresh task-local Visual Review evidence was generated after publication and is bound to implementation `a1f58f55d7eff78271d698a4a0aebe9a1a9658ff`, render-input identity `2528a8f9eee53188ba6e1a7875aaa37cbaaaed6d75e8ae3cc7de99eb010bcc79`, and rendered-pixel identity `a9c6e3eda7bf063605941fe49c94017b9ff19bc3a90c45b51d3b205477518e24`.

Planner review 2 read the item-level visual decisions. The model, main result, experiment-design, negative-result, next-experiment and medical-imaging pages all pass, and the full deck contact sheet also passes. The contact-sheet judgement explicitly confirms that the scientific title is now audience-facing and that the deck has coherent mature-talk rhythm without the previous engineering-title leakage. No blocking visual finding remains.

Task 039 therefore passes on its second and final allowed review.

039 is a generic non-holdout recovery and cannot substitute for Stage 5. The failed 038 Bürkner/brms and MedSAM decks remain preserved as genuine first unseen-test failures and remain disqualified from future unseen-holdout claims. They were not used as training examples inside 039.

The Program remains open. A new Stage 5 task must use two replacement real papers that have not participated in exemplar extraction, rule distillation, tuning or earlier holdout attempts, freeze their source bundles before first render, invoke the normal production entrypoint, and require fresh item/page-level plus full-deck visual review. Even if both pass Terra and Planner, final Program closure still requires the user's explicit acceptance of both rendered decks.

## Technical appendix

- `results/039_research_presentation_quality_loop_execution_recovery/generated/quality_loop_state.json`
- `results/039_research_presentation_quality_loop_execution_recovery/visual_review/visual_inputs.json`
- `results/039_research_presentation_quality_loop_execution_recovery/visual_review/VISUAL_REVIEW.json`
- `results/039_research_presentation_quality_loop_execution_recovery/generated/deck_contact_sheet.png`
- `results/039_research_presentation_quality_loop_execution_recovery/REVIEW_1.md`
- `results/039_research_presentation_quality_loop_execution_recovery/REVIEW_2.md`

Final implementation commit: `a1f58f55d7eff78271d698a4a0aebe9a1a9658ff`.
