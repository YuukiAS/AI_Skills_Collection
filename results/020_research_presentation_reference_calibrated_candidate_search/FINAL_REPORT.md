---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 020_research_presentation_reference_calibrated_candidate_search
final_decision: PASS
implementation_commit: 59147c7aff097cff91d103a8ec28d2297a4306a8
---

# 020 Research Presentation Reference-Calibrated Candidate Search — Final Report

## 结论

020 已在第二轮独立审核中 PASS。它完成了新一轮 Presentation 质量链路中的第二个核心节点：系统现在不仅能读取 019 的优秀页面构图记录，还能让同一份科研内容基于这些真实 composition records 产生三个内部候选方向，并保留可审计的 source-to-candidate geometry transfer。

这仍不是“高质量 PPT 已经解决”。020 只证明 **reference -> composition -> candidate** 这条链路已经真实成立；下一步必须做相对视觉审查，判断这些候选与真正成熟科研 slide 相比到底差多少。

## What this task solved

019 之后最大的风险是：reference library 虽然有 structured geometry，但 generator 仍可能只读一个 family name，然后继续使用自己的固定布局习惯。020 现在关闭了这个风险。

同一 scientific content 会内部生成三类候选：

- reference-faithful；
- alternative composition；
- controlled wildcard。

三者使用相同 scientific content 和 neutral preview skin，差异主要来自 source-derived geometry、region topology 和 reading flow，而不是简单换色。

## What changed

仓库新增了：

- candidate request / manifest schema；
- reference-calibrated candidate generator；
- candidate-manifest validator；
- 两个受控 regression requests；
- 每个 request 的三个真实 PNG candidate previews；
- internal comparison sheets；
- implementation report；
- source/generated plugin mirror；
- Presentation regression tests。

第一轮审核后，生成器进一步完成两项关键修复：

1. candidate bbox 真正由 selected source record 的 normalized regions 派生，而不是按 family 使用固定坐标；
2. wildcard/alternative source selection 增加 scientific-job compatibility gate，composition distance 只能在语义兼容 pool 中工作。

## New capabilities / behavior

当前 candidate engine 已经能够：

- 动态消费 019 composition selector/index；
- 根据 source title / primary / equation / secondary / legend geometry 派生 candidate regions；
- 对 source primary region 做 split / scale / translate / reorder；
- 在 manifest 中保存真实 geometry transfer trace；
- 在兼容 source pool 中选择 alternative / wildcard；
- 对同一 content 生成三个 geometry/signature/preview SHA 不同的候选；
- 使用真实 equation asset 与真实 synthetic medical-image assets，而不是 wireframe；
- 保持 audience-facing pixels 不暴露 candidate strategy、RRL、repo path 或 QA/provenance。

## 第一轮返修关闭情况

### Source geometry 真实进入布局计算

第一轮发现 candidate geometry 实际仍由 family-specific 固定 bbox 决定。修复后，selected reference regions 已进入 bbox 推导。

回归测试直接验证：同属 `aligned-multi-panel` 的 RRL-022 与 RRL-013 因 source primary geometry 不同，会产生不同 candidate primary bboxes。

### Wildcard 语义兼容性

第一轮发现 medical-image wildcard 会因为通用 token overlap 选择无关 Bayesian model page。修复后：

- medical-image request 只接受真正的 medical-image comparison composition；
- estimator / equation request 只接受 equation-compatible composition；
- generic stopwords 不再构成进入 candidate pool 的理由；
- distance 只在通过 compatibility gate 的 records 中排序。

当前 medical request 只使用 RRL-022 与 RRL-013；无关的 RRL-034 已退出 selection。

## Regression examples

统计 request 使用 cluster-robust sandwich covariance 的真实 rendered equation，生成 equation-dominant、split-visual-explanation 与 source-derived reordered-callout 三个方向。

医学影像 request 使用同一 synthetic lesion image / overlay / prediction / error assets，生成两种由不同真实 aligned-multi-panel reference geometry 派生的构图，以及一个由兼容 source geometry 重组出的 focus-callout 方向。

旧 synthetic assets 在这里仍只承担 candidate-engine regression content，不是 gold design baseline。

## Scope boundaries

020 没有：

- 修改 active `research-presentations/SKILL.md`；
- 扩 reference corpus；
- 修改 019 composition records；
- 修改 Terra / Bridge Kit；
- 修改 PPTX / Beamer renderer；
- 做 candidate winner selection；
- 锁定 deck-wide design system；
- 做 full-deck rhythm QA；
- 做真实 statistical / medical-imaging holdout；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## CI

最终 handoff tip `0b1c3aacfd09d017ad4ca2d3d406b78b0d59d428` 的 `reviewed-handoff/ci-summary=success`，GitHub Actions run `32630920085` 成功。

Executor 记录的 candidate validator、targeted Presentation tests、全库 115 tests、skills validation、Codex marketplace validation、Reviewed Handoff validation 与 `git diff --check` 均通过。

## Regression and remaining limitations

020 现在能保证“候选确实不同且确实来自 reference geometry”，但不能回答“哪个候选更好”，更不能证明任何一个候选已经接近成熟教授组会或顶会 oral。

当前仍缺：

- candidate 与真实优秀 reference renders 的相对视觉评审；
- 不强制 best-of-three 的 quality-gap gate；
- deck-wide design-system locking；
- contact-sheet / deck-rhythm QA；
- 真实统计 holdout one-shot；
- 真实医学影像 holdout one-shot；
- 必要时的独立 Beamer holdout。

## Example usage

后续 comparative review task 可以直接读取 020 的 candidate manifests，拿到三个 candidate preview SHA、source reference IDs、source geometry 与 transfer trace，再加载匹配的 canonical inspected reference renders 做匿名相对视觉比较。

## 下一步

下一 bounded task 应只实现 **comparative reference-calibrated visual review**：把 generated candidate previews 与匹配的真实 inspected reference renders 放进同一视觉审查包，匿名化作者/来源信息，绑定实际送审 reference render 的 SHA，并要求视觉 reviewer 判断 candidate 与 mature reference 之间的差距。

该 reviewer 必须允许“没有任何 candidate 达标”的结论，不能因为三个候选中总有一个相对最好，就把 best-of-bad 当作最终方向。

长期 `PROGRAM_MATURE=false`，本轮 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY` 仍未完成。

## Technical appendix

- implementation commit: `59147c7aff097cff91d103a8ec28d2297a4306a8`
- final handoff tip: `0b1c3aacfd09d017ad4ca2d3d406b78b0d59d428`
- required CI: PASS
- GitHub Actions run: `32630920085`
- Planner review: `REVIEW_2 = PASS`
