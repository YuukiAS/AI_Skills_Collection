---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 023_research_presentation_deck_design_system_integration
status: AWAIT_HUMAN_DECISION
---

# 023 Research Presentation Deck Design-System Integration — Final Report

## 当前结论

023 尚不能 PASS。第一轮发现的核心问题——deck design profile 只是记录文件、没有真正驱动 renderer——已经被明显修复，但第二轮审核确认该问题仍未完全闭合：字体、字号、颜色、annotation leader 与 equation role 已经真正 profile-driven；spacing、caption treatment 与 image-panel treatment 仍有一部分只是 profile metadata，实际页面继续依赖固定字面坐标/行为。

真实 GitHub CI 已通过，因此当前阻断不是 CI 或工程可运行性，而是 023 冻结目标本身尚未完整成立。由于本任务已经使用两轮正式 review，按 Reviewed Handoff 规则必须进入人工决策点，不能自动开启第三轮返修，也不能提前进入 deck-rhythm 或真实 holdout。

## What this task solved

023 solved the first multi-page integration step for the reference-calibrated
research-presentation pipeline: it created two coherent 4-page editable PPTX
engineering mini-decks, rendered them through LibreOffice to PDF/PNG, preserved
composition diversity, and established a deck design profile that partially
drives native PPTX output.

This does not mean 023 passed. The task is still at `AWAIT_HUMAN_DECISION`
because the deck design profile has not fully become the executable renderer
contract required by the frozen Plan.

## What changed

The implementation added a renderer-neutral deck profile, task-owned generated
PPTX/PDF/PNG artifacts, per-slide identity manifests, mechanical QA, a combined
review PDF, and profile-token mutation regression evidence. The round-1 repair
changed the renderer so font, type scale, color roles, annotation leader width,
and equation highlight / leader roles are read from
`profile["locked_properties"]` instead of being only audit metadata.

## New capabilities / behavior

The repository can now generate controlled multi-page research-presentation
PPTX fixtures where a shared design profile coexists with page-local
composition geometry. The profile mutation regression proves that changing
`accent` and `title_pt` changes the native PPTX XML while preserving the
page-local geometry signature.

## Example usage

Current task-owned review artifact:

```text
results/023_research_presentation_deck_design_system_integration/REVIEW_PACK.pdf
```

Current deterministic validators:

```bash
python skills/tools/documents-media/presentations/shared/scripts/generate_deck_design_system_integration.py
python skills/tools/documents-media/presentations/shared/scripts/validate_deck_design_system_integration.py
```

These commands are regression fixtures only. They are not a one-shot
quality-holdout workflow and do not establish `ONE_SHOT_QUALITY_PASS`.

## Regression and remaining limitations

Regression evidence shows editable PPTX generation, real render, mechanical QA,
composition diversity, anti-meta leakage checks, source/plugin mirror checks,
and partial profile-driven rendering all work.

Remaining limitation: spacing, caption treatment, and image-panel treatment are
still only partially executable design-profile inputs. Because this is the same
F-023-01 blocker after two formal reviews, 023 must remain at the human gate
until the user explicitly authorizes a strictly bounded recovery.

## 已经完成的能力

023 已建立两套 coherent 4-page engineering mini-decks，并通过同一 shared integration path 生成真实 editable PPTX，再经 LibreOffice 真实渲染为 PDF/PNG。统计与医学影像两套 fixture 都保持至少三种 major composition families，019 source geometry、020 semantic compatibility 与 022 equation / medical-image visual-finish layer 没有被统一模板覆盖。

Round-1 repair 也已经证明 design profile 不再完全是旁路：`fonts.primary`、`type_scale.*`、`color_roles.*`、annotation leader width，以及 equation highlight/leader role 现在由 profile 读取。新增 mutation regression 修改 `accent` 与 `title_pt` 后，native PPTX XML identity 改变，而 page-local geometry signature 不变。这说明“profile 控视觉语言、composition 控几何”的分层已经部分成立。

## 尚未闭合的核心差距

冻结 Plan 把 typography、palette、spacing、caption/annotation、chart/diagram/image/equation treatment 都定义为 deck-wide locked properties。当前实现里，spacing 的 `outer_margin/object_gap/annotation_gap/panel_label_gap` 仍没有成为 renderer 输入；title/caption bbox、panel label offset 等仍是固定字面坐标。`image_panel.label_position/legend_binding/container_role` 与 `caption.position/style` 也仍主要是说明性字段，没有完整驱动 native PPTX 绘制行为。

因此目前的 profile 是“部分可执行、部分描述”的混合体。若现在进入真实 one-shot holdout，修改完整设计语言仍可能需要改 renderer 代码，而不是只换一个 design profile；这违背 023 本身要建立的 renderer-neutral deck design system layer。

## 第二轮为什么仍判 REVISE

第一轮要求的不是“证明任意一个 profile token 能改变 PPTX”，而是让当前已经冻结为 design-system contract 的核心视觉 token 成为真实输入。第二轮 repair 对字体、字号、颜色和部分 annotation/equation treatment 做到了这一点，但 mutation regression 只覆盖 `accent` 与 `title_pt`，没有覆盖剩余 spacing / caption / image-panel contract。

所以本轮不是新增审美要求，而是同一个 F-023-01 尚未完整 closure。

## CI 与验证状态

current handoff tip `ed0fd9256788d59800b6aa09374fea4bbb7af23b` 的 `reviewed-handoff/ci-summary=success`，对应 GitHub Actions run `32647316171`。Executor 记录的 Presentation targeted tests、全库 tests、skills validation、marketplace validation/check/path-report、Reviewed Handoff validation 与 `git diff --check` 均通过。

当前问题与 CI 无关。

## 如果继续，最小建议

建议用户授权一次严格限定的 023 recovery，而不是放宽目标或绕过 review limit。恢复任务只需要做两件事：

1. 让 renderer 真正消费现有 profile 中仍未执行的 spacing、caption treatment 和 image-panel treatment；如果某字段本质只能作为说明，则把它从 executable locked contract 中明确拆出，而不是继续假装是 renderer token。
2. 增加覆盖这些剩余类别的 mutation regression，证明改变一个 spacing 或 image/caption token 会改变 native PPTX/rendered identity，但 page-local geometry/layout family 仍由 composition layer 保持稳定。

恢复不得修改 reference corpus、019 composition records、020 candidate search、021/022 comparative reviewer，不得开始 contact-sheet rhythm QA、真实 holdout 或 Beamer holdout。

恢复完成并重新通过真实 CI 后，应由独立 Planner 做一次 recovery closure；不能把它伪造成 REVIEW_3。

## 当前长期项目状态

`REFERENCE_CALIBRATED_ONE_SHOT_QUALITY` 仍未完成，长期 `PROGRAM_MATURE=false`。

023 之前的链路已经成立：reference composition representation、reference-calibrated candidate search、anonymous comparative review、candidate visual-finish repair 都已通过。当前必须先把 deck-wide design profile 的执行语义补完整，之后才能进入正式 contact-sheet / deck-rhythm QA，再往后才是两个真实 holdout one-shot benchmark。

## Technical appendix

- Task: `023_research_presentation_deck_design_system_integration`
- Status: `AWAIT_HUMAN_DECISION`
- Human gate reason: `REVIEW_LIMIT`
- Initial implementation commit: `4ac8a553e7c5383e7ac53f0c7da7ee182e088068`
- Repair implementation commit: `1ca5c01df418518f52a287bad1c3d90db63587cc`
- Handoff tip: `ed0fd9256788d59800b6aa09374fea4bbb7af23b`
- CI: success, run `32647316171`
- Review artifacts: `REVIEW_1.md`, `REVIEW_2.md`
