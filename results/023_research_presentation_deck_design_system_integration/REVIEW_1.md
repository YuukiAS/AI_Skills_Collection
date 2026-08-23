---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 023_research_presentation_deck_design_system_integration
review_round: 1
decision: REVISE
implementation_commit: 4ac8a553e7c5383e7ac53f0c7da7ee182e088068
---

# GPT Review

## Decision

`REVISE`。

023 已经完成了多页 PPTX、真实 LibreOffice 渲染、两套 4 页工程 mini-deck、composition diversity、anti-meta gate 与 CI closure；真实 GitHub Actions run `32646153501` 已 `success`。当前 blocker 不是 CI，也不是 019–022 的 reference geometry / semantic compatibility 回退，而是冻结 Plan 最核心的“deck design profile 真正控制多页视觉语言”目前还没有成立。

当前实现生成了完整的 `RESEARCH_DECK_DESIGN_PROFILE_V1`，也把同一个 `locked_properties_sha256` 写进每页 manifest；但实际 PPTX renderer 并没有从 `profile["locked_properties"]` 读取字体、字号、颜色、间距、annotation、equation、image-panel 等视觉 token。相反，这些值仍然在生成脚本中以模块常量和函数参数重复硬编码。因此现在只能证明“profile JSON 与页面使用了相同的一组值”，不能证明“页面由 profile 驱动”。这会让 design profile 退化为审计旁路，而不是 023 要建立的共享设计系统层。

## Blocking finding

### F-023-01 — Deck design profile 尚未成为 renderer 的真实输入

**冻结依据**：PLAN 的 Frozen objective / Section 1–2 / Acceptance gates 1、3 明确要求建立 renderer-neutral deck design profile，并由 profile 锁定 typography、palette、spacing、caption/annotation、chart/diagram/image/equation treatment；同时 page-local composition 继续由 matched composition record 决定。换言之，profile 必须控制视觉语言，而不是只被序列化和记录 SHA。

**真实 observed evidence**：

- `deck_design_profile.json` 确实声明了 `fonts.primary=Aptos`、`title_pt=27`、`caption_pt=10`、颜色角色、spacing、annotation leader、image/equation/caption treatment 等完整 locked properties。
- 但 renderer 的 `add_text()` 直接写死 `run.font.name = "Aptos"`；`add_slide_bg()` 直接读取模块常量 `BG`；`add_footer()` 直接使用 `size=10` 与 `MUTED`；`add_equation_slide()` / `add_plot_slide()` / `add_flow_slide()` / `add_medical_slide()` 又直接写死 `size=27/13/10/9`、`ACCENT/WARNING/LINE/MUTED/INK` 等常量。传入这些函数的 `profile` 没有用于计算这些视觉属性，只在 `slide_manifest()` 中记录 `profile_id` 与 `locked_properties_sha256`。
- validator 目前只检查 profile 字段存在、所有 slide 的 locked SHA 相同、render/PNG/PPTX 有效和 composition diversity；它没有证明“修改 profile token 会改变 native PPTX/rendered output”。因此当前 regression 可以在 profile 与 renderer 实际脱钩时仍然 PASS。

**为什么阻断**：如果 profile 不是 renderer 的真实输入，后续所谓 design-system locking 无法复用到新的 one-shot deck；任何字体、色彩、caption、annotation 或 equation treatment 的改变仍需要修改 renderer 代码。这样 023 就没有真正建立“deck-wide design system layer”，也无法为下一步 deck-rhythm / real holdout 提供可信基础。

**最小修复**：

1. 不扩大 023 scope，不改 019 composition records、不改 comparative reviewer、不做 holdout。
2. 让 shared multi-page renderer 从 `profile["locked_properties"]` 读取并应用至少当前已经冻结的核心视觉 token：字体、type scale、color roles、spacing、annotation leader、caption、image-panel、equation treatment；模块常量可以作为 profile 构造默认值，但最终页面绘制不能绕过 profile 再直接读取同一组常量。
3. 保持 page-local bbox / layout family / panel count / annotation target 继续来自现有 composition/candidate geometry，不把 profile 变成统一模板。
4. 增加一个确定性 regression：复制当前 profile，修改至少一个 deck-wide token（建议 primary font 或 accent color / title size 中一个不会破坏结构的 token），重新生成受控 fixture，验证 native PPTX/XML 或 rendered identity 确实发生对应变化；同时 primary bbox / layout family 保持不变。该测试用于证明“profile 控视觉语言、composition 控几何”。
5. 重新生成两套 mini-deck 与真实 render，更新 identity manifest / mechanical QA，并保持至少 3 个 major composition families、anti-meta gate 与现有 019/020/022 regression 全部通过。

**修复后需要看到的 evidence**：

- renderer 对 locked visual properties 的读取路径可直接从代码确认；
- profile-token mutation regression PASS，并同时证明 page-local geometry 未变化；
- 两套 editable PPTX -> PDF/PNG real render 继续成功；
- current-tip required CI PASS；
- 没有新增 reference corpus、reviewer、holdout、Beamer 或长期完成声明。

## Non-blocking notes

当前实现已经把工程 fixture 与最终 holdout 明确分开，也没有把 021/022 某个 candidate strategy 写成全局 winner；这一点符合冻结边界。两套 manifest 也都显示至少 3 个 major composition families，且 source-derived geometry 仍保留，因此本轮不要求重新设计构图搜索层。

正式 contact-sheet / deck-rhythm comparative QA 仍属于下一 bounded task，不应在本次 repair 中顺便实现。

## CI

Handoff tip `295bf4f83805d9b1e5cf1a6c0988218eb146041a` 对应 GitHub Actions run `32646153501` 已完成且 `conclusion=success`。CI blocker 已关闭；本次 `REVISE` 仅针对冻结的 design-profile integration 语义。
