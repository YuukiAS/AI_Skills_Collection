---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 025_research_presentation_gold_scientific_composition_library
---

# 025 Gold Scientific Composition Library — Final Report

## 本轮解决了什么

025 已经把 Stage 2 从“普通 inspected reference 列表”推进成真正可被 production 选择和消费的 Gold Scientific Composition Library。当前 9 条 gold records 都来自既有 inspected/downloaded corpus，并且每条都经过 025 专用真实像素审查达到 item-level `PASS`；被判 `REVISE` 的页面继续保留为普通参考，不会因为覆盖需要被强行提升。

同时，运行时链路已经证明 gold 不只是内部 ID：selector 会按 scientific job、domain、scientific object、density/panel capacity 做兼容筛选，recipe builder 会实际读取 source-derived geometry、hierarchy、reading flow 与 annotation/panel relations。两个 deterministic probes 都证明了 `selected -> consumed -> output affected`，且 alternate 现在必须经过与 production 相同的 compatibility gate。

## 实际新增能力

当前系统已经具备：

- 9 条有真实 rendered-pixel 成熟度证据的 production gold composition records；
- 明确的 rights/reuse boundary，不把 donor pixels、logo 或 branding 当可复用资产；
- gold schema、validator、selector 和 renderer-neutral composition recipe builder；
- statistics/biostatistics 与 medical-imaging 两类 deterministic runtime consumption proof；
- admitted / rejected reference 的完整 admission report 与 reviewer-input identity binding；
- source/plugin mirror 和对应 regression tests。

这意味着 Stage 3 不再需要从一个未经筛选的 reference pool 自由猜 layout，而可以消费一组经过成熟度和兼容性双重约束的 composition recipes。

## 被拒绝的方案与原因

第一轮发现原 10 条 gold 中多条只有 metadata / 019 composition evidence，没有真实 item-level pixel maturity evidence，因此不能作为 production gold。随后 025 专用 Terra 对第一批 13 页只准入 `RRL-019` 与 `RRL-013`，包括旧任务里曾表现较好的 `RRL-028` 也被当前 admission-specific review 判为 `REVISE`。本轮遵守新 evidence 的优先级，没有拿旧 judgement 覆盖它。

统计 runtime probe 原先还通过 `force_gold_id` 绕过兼容性门槛制造 alternate；这一做法已经移除。现在 forced record 也必须通过正常 selector compatibility check，不兼容时直接拒绝。

## 当前未关闭的问题

唯一剩余 blocker 是冻结 Plan 要求的 `discussion / next experiment` gold coverage。

Plan Revision 1 已允许在现有 inspected/downloaded corpus 中做一次有界 recovery：新增送审最多 20 页。该额度已经用满，但没有任何 discussion / next-experiment 页面达到 025 production-gold item-level `PASS`。因此当前不能在不改变合同的情况下继续自动修 025。

这不是 CI、selector 或 recipe 实现失败，而是 reference coverage 与 mature-bar 同时约束后的真实内容缺口。

## 推荐的人工作品决策

推荐保持当前成熟度门槛不变，授权一个新的、严格限定的 Stage 2 coverage recovery task：只为 `discussion / next experiment` 缺口做小规模外部 source scouting / intake / real-pixel admission；保留 025 已建立的 9 条 gold 与全部历史 evidence，不重跑已经通过的部分。该 recovery PASS 后再进入 Stage 3 — Executable CUHK Scientific Layout System。

如果用户更希望直接推进，也可以明确接受“discussion / next experiment 暂无 production gold”这一已知 coverage gap，并授权 Planner 放宽 Stage 2 coverage contract；这是产品质量标准变化，不能由 Planner 自动决定。

## Regression 风险

当前 9 条 gold 和运行时选择/消费链路本身没有发现新的 regression。真正风险在于如果忽略 coverage gap 直接进入 Stage 3，后续 discussion / next-experiment 页面可能重新退化为无参考约束的自由布局，这正是本轮希望避免的失败模式。

## 可直接理解的使用例子

给一个 biostatistics quantitative-result page job，selector 会选出经过像素级准入的 `GSC-014`；如果屏蔽它，同一 selector 会选择同样兼容但构图不同的 `GSC-015`。recipe builder 会把两条 reference 的不同 primary bbox、visual hierarchy、alignment 和 reading flow 转成不同 renderer-neutral constraints，而不是只换一个 reference ID。

给一个 medical-image comparison page job，selector 会优先选择图像组合作为主体的 `GSC-008`；屏蔽后会选择同领域、同任务兼容的 `GSC-004` application-task composition。两条都通过当前 gold admission，但它们给下游 Stage 3 的对象尺度、panel/hierarchy 和 reading flow 约束不同。

## 技术附录

- implementation commit: `d6fafda2819d406c88a2f363a22bdfd9564989cf`
- handoff CI locator: `9054368082dfacdf995a772115c0cef091273ab9`
- CI: `reviewed-handoff/ci-summary = success`
- GitHub Actions run: `32721702586`
- final gold count: 9
- targeted Presentation tests: 25 passed
- full unittest discovery: 121 passed
- skills / marketplace / Reviewed Handoff validation: passed
- review rounds used: 2 / 2
- plan revisions used: 1 / 1

025 当前不是 PASS；已达到 review limit，等待人工决定下一步 coverage 策略。