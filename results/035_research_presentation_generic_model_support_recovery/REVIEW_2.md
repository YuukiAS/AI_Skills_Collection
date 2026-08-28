---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 035_research_presentation_generic_model_support_recovery
review_round: 2
decision: REVISE
implementation_commit: d44adaef2949d18843d5c8b22b78357345e3ab62
---

# GPT Review

## Decision

REVISE。

035 原始 blocker 已经关闭，而且这次不是 Executor 自报：共享 `STATISTICAL_MODEL` supporting copy 已改为消费当前 spec/source fields，unrelated Cox regression 经过同一共享路径，当前模型页没有恢复 clustered-calibration hardcode；真实 GitHub `Codex Marketplace` CI 已通过。fresh task-local Terra 也与 implementation `d44adaef...`、当前 render-input identity、rendered-pixel identity 和 contact sheet 一致，并继续把 `slide_2_statistical_model` 判为 item-level `PASS`。

但是 035 frozen Plan 的 acceptance gate 10 明确要求当前 pixels 改变后 `slide_2_statistical_model` **与** `deck_contact_sheet` 都必须 item-level `PASS`。本轮 fresh Terra 将 `slide_4_experiment_design`、`slide_6_next_experiment` 和 `deck_contact_sheet` 判为 `REVISE`：实验设计页的中央流程明显偏小并留下大面积无效留白；下一实验页的失败证据、比较器标签和决策规则在投影尺度下仍偏小；整套 contact sheet 因这两个 process pages 的密度/尺度下陷，未达到持续稳定的成熟博士组会标准。因此 035 不能 PASS。

同时，这个 finding 不能在 035 内继续扩大返修范围。Review 1 已明确冻结 slide 3–7，并规定若模型页最小重平衡后 contact-sheet 仍由未变化页面阻塞，应交回 Planner 路由，而不是偷偷修改这些页面。当前 slide 4 与 slide 6 的 PNG SHA-256 分别为 `e1775c71...` 与 `0fc4574e...`，与 034 fresh Terra 曾判 PASS 的对应像素完全一致；这证明它们不是 035 引入的 regression，但最新同一成熟 rubric 对当前整套 deck 的 item-level 判断已经明确暴露了投影尺度缺口。Stage 4 的冻结质量政策要求保留较高门槛，不能用旧 PASS 覆盖新的真实审查结果。

这是第二轮审核，因此 035 到此停止，不创建第三轮。剩余问题已经从“模型页 source-grounding”转变为“共享 experiment-design / next-experiment process-page projection scale”，属于范围清楚、可以用不同实现机制关闭的质量保持 recovery 候选。

## Blocking findings

### 1. 当前完整 deck 的两个 process pages 仍未达到 fresh item-level mature projection bar

**Plan / regression boundary**

- 035 Plan acceptance gate 10：pixels 改变时，模型页和 `deck_contact_sheet` 都必须 fresh item-level PASS。
- 035 Review 1：只允许模型页内的最小重平衡；若 contact sheet 继续被 unchanged slide 6 阻塞，不得在 035 内越界修改 slide 3–7。
- Program Goal：Stage 4 必须实际完成 page-level + deck-level visual review；不能用旧 evidence、top-level workflow success 或 mechanical PASS 替代当前 item-level mature bar。

**Observed evidence**

- `slide_2_statistical_model`: fresh Terra `PASS`；公式仍为主对象，supporting model components / interpretation 是 source-specific，并且无内部制作语言。
- `slide_4_experiment_design`: fresh Terra `REVISE`；中央 DGP → center hierarchy → interval procedures → endpoints pipeline 相对画布明显过小，上下留白过多，右侧 endpoint / connector annotations 在投影尺度下偏小。
- `slide_6_next_experiment`: fresh Terra `REVISE`；failure evidence、sampling choices、CR2 / wild-cluster comparator labels 与 decision-rule copy 都是 source-specific，但细节字号与图元尺度偏小。
- `deck_contact_sheet`: fresh Terra `REVISE`；故事线、构图交替和 result → failure → next-experiment 节奏均成立，但 slides 4 / 6 形成可见的 density / scale dips，使整套 deck 尚未稳定达到 strong projection-ready group-meeting bar。
- slides 4 / 6 当前 SHA 与 034 证据完全一致，说明这不是 035 新 regression；但最新 fresh review 已把此前未稳定识别的质量缺口显式化。

**Minimal repair**

035 内不再修复。若按 Program Goal 自动续接 recovery，新 task 应只针对共享 `EXPERIMENT_DESIGN` 与 `NEXT_EXPERIMENT` process-page layout/emission 做 bounded projection-scale 修复：放大现有 source-backed diagram/object、缩短或重排已有 copy、利用现有纵向空间，提高连接器与标签投影可读性；不得添加无来源科研内容、不得改故事线、不得修改已 PASS 的 model/result/failure/medical 页面，也不得降低 Terra bar。

该 recovery 必须用 page-job/general layout semantics 实现，而不是按当前 clustered fixture 的标题、术语或页号写死。若单页内容容量无法在一页达到成熟投影尺度，可使用现有 layout/capacity contract 做 no-winner / split-page 决策，但不得通过缩小字体强塞。

**Required closure evidence**

- shared/plugin parity 与 targeted/full presentation regressions通过；
- 真实 GitHub CI PASS；
- 新 render identity 与 pixel identity 绑定当前实现；
- fresh Terra 对 `slide_4_experiment_design`、`slide_6_next_experiment` 和 `deck_contact_sheet` item-level PASS；
- `slide_2_statistical_model` 继续 source-driven 且无 clustered hardcode regression；result / failure / medical pages、032 storyline、exact CUHK identity 和一次 repair/fail-closed contract 无回归。

## Non-blocking notes

- 035 的原始 generic-model source-grounding目标已经真实完成，不应在后续 recovery 中重写该机制。
- 最新 Terra 仍明确认可整套 deck 的研究主线、独立 medical workstream transition、不同 scientific-object 类型之间的构图变化，以及无内部 workflow/meta language；后续只需修投影尺度，不需要重做 deck 叙事或视觉身份。
- 034 对相同 slides 4 / 6 像素曾给 PASS，035 fresh Terra 给 REVISE。该差异应保留为审查历史；Stage 4 closure 采用当前更严格的 fresh evidence，而不是选择性引用较旧 PASS。
