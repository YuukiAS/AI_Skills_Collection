---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 025_research_presentation_gold_scientific_composition_library
review_round: 2
decision: REVISE
implementation_commit: d6fafda2819d406c88a2f363a22bdfd9564989cf
---

# 025 Gold Scientific Composition Library — Review 2

## Decision

`REVISE`

Revision 1 实质关闭了 REVIEW_1 的两个实现级 blocker，但 025 仍不能 PASS，因为冻结 Plan 明确要求的主要 scientific-job coverage 尚未完整成立，而本轮有界现有库筛选已经用满允许的新增送审上限。按照 Plan Revision 1 的路由规则，这一缺口不能通过降低成熟度门槛、继续无界筛现有库或擅自外部扩 corpus 解决，必须进入人工决策。

## 已关闭的 REVIEW_1 blocker

### 1. Gold admission 已改为逐条真实像素级准入

当前 gold index 为 9 条记录，每条都有 025 admission-specific 的 `gpt-5.6-terra` item-level `PASS`、真实 reviewer-input SHA、visual-review evidence id/path 与 identity binding。原第一批被判 `REVISE` 的 `RRL-028` 等页面没有被旧 evidence 覆盖，也没有为凑覆盖被强行纳入。

`gold_admission_report.json` 现在完整列出 9 条 admitted gold 与被拒绝候选，不再把两个 runtime baseline ID 冒充整套 admission list。

### 2. Runtime alternate 不再绕过 semantic compatibility

`build_gold_composition_recipe.py` 的 `force_gold_id` 路径现在调用与 production selector 相同的 compatibility check；不兼容 record 会直接报错，不再生成 `score=999` 或 `forced compatible probe`。

两个 deterministic runtime probes 均由正常 selector 产生 baseline，并通过屏蔽 baseline 后再次调用同一 selector得到 alternate：

- biostatistics quantitative-result：`GSC-014 -> GSC-015`；
- medical-image comparison：`GSC-008 -> GSC-004`。

trace 保存了真实 compatibility reasons、excluded candidates，以及 source-derived bbox / hierarchy / relations 被 recipe builder 消费后造成的 recipe 差异。因此 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 已经成立。

## Blocking finding — 冻结的主要 scientific-job coverage 仍缺 discussion / next experiment

### Plan basis

原 Plan §2 与 Acceptance Gate 2 要求 gold set 覆盖后续真实 paper deck 的主要 scientific jobs，其中明确包括 `discussion / next experiment`。Plan Revision 1 没有删除这一门槛；其 Revision acceptance 明确要求第二轮仍看到“主要 scientific-job coverage 是由实际 admitted gold 支撑的”。同时 Bounded candidate expansion 第 5 条规定：有界筛选后如果仍不能满足主要 coverage，不得降低门槛或外部扩库，而应明确 coverage limitation 并路由回 Planner / human decision。

### Observed evidence

Revision 1 已在现有 inspected/downloaded corpus 中额外送审 20 个候选，达到该 revision 允许的新增送审总量上限。最终 9 条 gold 已覆盖 motivation/research question、method/experiment design、数学/统计结果、uncertainty/comparison、negative result/model check、medical-image visual comparison 等用途，但 admission report 与 RESULT 均明确记录：

`No discussion / next-experiment page reached item-level PASS in the bounded existing-corpus screen.`

因此当前缺口不是 Executor 忘了跑 selector，而是现有 bounded corpus 中没有页面同时满足该 scientific job 与当前 production-gold 成熟度门槛。

### Why blocking

如果现在直接 PASS 025，就等于在第二轮审核中静默放宽冻结的 Stage 2 coverage contract。随后 Stage 3 会把一个已知缺少 discussion / next-experiment gold reference 的库固化成 executable CUHK layout system，与本轮“先建立成熟 gold，再实现 renderer”的顺序冲突。

### Minimal resolution requiring human choice

推荐：保持当前 mature-bar 不变，授权一个新的、严格限定的 Stage 2 coverage recovery task，只针对 `discussion / next experiment` 缺口做小规模外部 source scouting / intake / pixel admission；当前 025 历史与 9 条已通过 gold 保持不变。新 recovery 关闭后再进入 Stage 3。

另一种选择是用户明确放宽 Stage 2 coverage requirement，接受 discussion / next-experiment 暂无 gold 并继续 Stage 3；这属于产品/质量合同变更，Planner 不应自行决定。

## CI / regression

当前 handoff tip `9054368082dfacdf995a772115c0cef091273ab9` 的 `reviewed-handoff/ci-summary` 为 `success`，对应 GitHub Actions run `32721702586`。没有 CI blocker。

没有发现外部扩 corpus、Stage 3 renderer 实现、023 recovery、final holdout 或 Terra core 修改等 scope creep。

## Review-limit consequence

本 task 已使用两轮正式 review。根据 Reviewed Handoff，不创建 `REVIEW_3`，不再自动返修 025；进入人工决策点。