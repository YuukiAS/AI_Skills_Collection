# 024 Research Presentation Product Contract Reset — Final Report

## What this task solved

本轮解决的是 Research Presentation 产品入口与长期目标互相矛盾的问题。此前普通科研组会、paper talk 或 research update 在未指定格式时仍默认走 editable PPTX/Slides，而新的长期目标已经明确要求第一成熟路线使用 canonical CUHK Beamer source 生成 `.tex + PDF`。024 现已把正式 skill、共享路由、默认 deck-plan 输出和回归测试统一到同一个产品合同。

## What changed

实际变化不是只改说明文字。普通 research deck-plan 的默认输出已经从 `pptx + editable` 改成 `tex + source-editable`；显式 PowerPoint、`.pptx`、editable、Slides 或后续手工编辑请求仍会稳定覆盖默认，继续进入 editable Presentation/Slides。Exact CUHK 的 canonical source 现在明确绑定到 `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/`，而 `design-tokens.json`、derived Beamer convenience scaffold 和 PPTX reference scaffold 被明确限制为 non-exact/test 辅助层。

## New capabilities / behavior

这带来了一个此前没有的真实能力：后续 Stage 2–4 即使把 reference retrieval、科研构图和 CUHK scientific layouts 做好，普通用户入口也不会继续被旧的 PPTX 默认路由绕开。换句话说，后续能力已经有了正确的 production landing path。

本任务明确拒绝了几个不属于 Stage 1 的方向：没有恢复 023 的低层 PPTX renderer，没有新增 scientific layouts/macros，没有扩 reference corpus，没有修改 Terra core，也没有提前跑真实 statistics / medical-imaging holdout。这些都留给后续独立 bounded task。

## Regression and remaining limitations

回归风险目前主要来自一个边界：默认 research adapter 已改为 TeX，因此任何依赖其旧 `pptx` 默认值的外部调用如果没有显式声明 output，会看到行为变化。但这正是当前 Program Goal 要求的产品合同变化；显式 `output="pptx"` 的兼容路径已经由测试覆盖。

## Example usage

一个直接例子：用户只说“把这篇 paper 做成组会汇报”，且没有指定 PowerPoint，现在应进入 exact CUHK Beamer 路线并产出 source-editable `.tex` 与 PDF；如果用户明确说“我要可编辑 PPTX，后面还要自己改”，则仍进入 editable Presentation/Slides。

## Technical appendix

Implementation commit: `01886bd84841a388f034f504ca8e3b640f267796`.

独立审核确认当前真实 CI 已通过：`reviewed-handoff/ci-summary=success`，对应 GitHub Actions run `32692720867`。

Executor 本地记录通过：Presentation targeted tests、120 个全库 unittest、skills validation、Codex marketplace write/validate/check/path-report、Reviewed Handoff validation 与 `git diff --check`。

024 只关闭 Stage 1 — Product Contract Reset。长期 `PROGRAM_MATURE=false`，最终双真实 paper holdout 与用户人工验收尚未开始。
