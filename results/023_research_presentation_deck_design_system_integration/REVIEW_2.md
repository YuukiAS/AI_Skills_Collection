---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 023_research_presentation_deck_design_system_integration
review_round: 2
decision: REVISE
implementation_commit: 1ca5c01df418518f52a287bad1c3d90db63587cc
---

# GPT Review

## Decision

`REVISE`。

本轮 repair 已经实质关闭了 F-023-01 的一部分：当前 renderer 确实从 `profile["locked_properties"]` 读取字体、字号、颜色角色、annotation leader width，以及 equation 的 highlight / leader color role；profile-token mutation regression 也证明修改 `color_roles.accent` 与 `type_scale.title_pt` 会改变 native PPTX XML，同时 page-local geometry signature 保持不变。current handoff tip `ed0fd9256788d59800b6aa09374fea4bbb7af23b` 的 `reviewed-handoff/ci-summary=success`，对应 GitHub Actions run `32647316171`，因此 CI blocker 已关闭。

但是，第一轮冻结的同一个 blocker 仍未完整关闭：Frozen Plan 与 REVIEW_1 明确要求 deck design profile 锁定并驱动 typography、palette、**spacing**、caption/annotation、chart/diagram/image/equation treatment；当前 repair 仍有一部分这些“locked properties”只存在于 profile JSON 中，没有成为 renderer 的真实输入。由于这是第二轮审核，不能自动开启第三轮返修。

## Blocking finding

### F-023-01 — Deck design profile 仍只部分驱动 renderer

**冻结依据**：PLAN 的 Frozen objective、Section 1–2、Acceptance gate 1/3，以及 REVIEW_1 的最小修复第 2 项，都要求 profile 真正控制 deck-wide 视觉语言，其中明确包括 spacing、caption、image-panel 和 equation/annotation treatment；page-local bbox / layout family 继续由 composition layer 控制。

**已关闭的部分**：

- `add_text()` 已从 profile 读取 `fonts.primary`、`type_scale.*` 与 `color_roles.*`；
- slide background、annotation leader、equation highlight / leader 已读取 profile role / width；
- mutation regression 把 `accent` 改为 `#8A2C69`、`title_pt` 改为 `29`，native PPTX XML SHA 确实改变，而 geometry signature 保持相同；
- 两套 mini-deck 的 real render / mechanical QA 与 current-tip CI 均继续通过。

**仍未关闭的部分**：

1. `locked_properties.spacing` 中的 `outer_margin`、`object_gap`、`annotation_gap`、`panel_label_gap` 仍只在 `deck_design_profile()` 中声明。实际 `title_bbox()`、`caption_bbox()`、medical panel label 的位置和若干 annotation offset 继续使用固定字面坐标；renderer 没有读取这些 spacing token。
2. `locked_properties.image_panel` 的 `label_position`、`legend_binding`、`container_role` 仍主要是描述性 metadata。实际 medical panel label 使用固定 `bbox["y"] - 0.045`，border 只读取通用 `color_roles.line`，没有读取 `image_panel` treatment 来决定这些行为。
3. `locked_properties.caption.position/style` 也没有进入排版决策；`add_footer()` 仍调用固定 `caption_bbox()`，只从 profile 读取 caption 字号和 muted color。也就是说 caption 的视觉 token 部分生效，但 caption treatment 本身仍是旁路声明。
4. 当前 mutation regression 只变异 `accent` 与 `title_pt`，因此能证明“部分 profile token 驱动输出”，但不能证明 Frozen Plan 要求的 spacing / caption / image-panel treatment 已经成为共享 renderer 输入。

**为什么仍然阻断**：023 的目标不是得到一个包含很多字段的 profile 文件，而是建立可复用的 deck-wide design-system layer。如果 spacing、caption、image-panel 等字段仍需改 renderer 常量/字面坐标才能生效，那么新的 one-shot deck 仍不能只通过 profile 改变完整视觉语言；这会让 profile 继续处于“部分可执行、部分审计说明”的混合状态，不能作为下一阶段 deck-rhythm 与真实 holdout 的可信基础。

**最小需要修复的内容**：

- 不改变 019 composition records、020 semantic compatibility、021/022 comparative reviewer/candidate 机制，不开始 holdout；
- 让 renderer 至少真正读取并应用现有 profile 中的 spacing、caption treatment 与 image-panel treatment；可以把 profile 中无法执行、只具说明性质的字段明确移出 `locked_properties` executable contract，但不能继续把它们标为 locked renderer tokens 却不消费；
- 增加一个覆盖上述剩余类别的 mutation regression，证明改变一个 spacing 或 image/caption treatment token 会改变 native PPTX/rendered identity，同时 page-local composition geometry / layout family 不被统一覆盖；
- 保持两套 editable PPTX、real render、mechanical QA、composition diversity、anti-meta gate 和 required CI 全部通过。

## Review-limit consequence

这是 023 的第二轮正式审核。第一轮已针对同一个 F-023-01 要求 profile 成为 renderer 的真实输入；第二轮 repair 已部分关闭，但 spacing / caption / image-panel executable contract 仍未闭环。因此按照 Reviewed Handoff 规则，当前 task 必须进入 `AWAIT_HUMAN_DECISION`，不得自动开启第三轮修复，也不得提前创建 contact-sheet / deck-rhythm QA task。

## CI

current handoff tip `ed0fd9256788d59800b6aa09374fea4bbb7af23b` 的 `reviewed-handoff/ci-summary=success`，target run `32647316171`。CI 已通过；本次 `REVISE` 只针对 Frozen Plan 中 design-profile integration 语义未完全闭合。
