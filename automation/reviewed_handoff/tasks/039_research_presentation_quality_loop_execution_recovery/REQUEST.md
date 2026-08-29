---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 039_research_presentation_quality_loop_execution_recovery
---

# Reviewed Handoff Request — 039_research_presentation_quality_loop_execution_recovery

## Objective

关闭 038 首次双真实论文 holdout 暴露出的唯一通用恢复缺口：Stage 4 已经存在的 bounded quality loop 能够读取 item-level visual blocker，但当前 consumer 只接受 finding 自带的 `repair_intent`；真实 Terra finding 没有这个字段，因此两套 deck 都在 repair count 为 0 时 `QUALITY_LOOP_FAIL_NO_WINNER`。进一步独立检查发现，现有 `RESCALE_PRIMARY_OBJECT` 与 `REPAIR_ANNOTATION_LEGEND` 只给 spec 写 hint，仓库没有生产渲染消费者证明这些 hint 会改变实际 pixels。

039 不是继续修 brms 或 MedSAM，也不是重新做 Stage 5。它只把现有 task-local Visual Review contract 与现有一次 bounded repair 机制补成真正可执行、可验证、仍然 fail-closed 的通用闭环。038 两篇论文及其像素永久保持失败 holdout 历史，不得作为 039 的调优 fixture。

## User-provided inputs

- `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Quality-Preserving Continuation Policy、Stage 4 contract 与 Stage 5 unseen replacement 规则。
- 038 的 `REVIEW_1.md`、`REVIEW_2.md`、`FINAL_REPORT.md`、两套 `quality_loop_state.json`、Round-1 archived Terra item/page-level evidence 与真实生成 `main.tex`。
- 当前 `deck_quality_loop.py`、normal production entrypoint、Stage-3 executable layouts、gold selection/capacity system 与 task-local Visual Review contract。
- 既有 Stage 3–4 engineering/non-holdout fixtures 与 regression corpus；这些可用于 039，但不得引入 038 的论文内容作为 tuning data。

## User constraints

- 保留 038 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE` 历史，不制造第三轮 review，不把 038 事后改成 PASS。
- 不使用 Bürkner 2017 brms、Ma et al. 2024 MedSAM 的 title/DOI/figure/table/image/crop/page wording 作为 039 regression fixture、gold、rule source 或 tuning exemplar。038 evidence 只能用于定义 blocker class。
- 继续使用现有 Visual Review evidence contract、现有 quality-loop state 与单次 repair budget；除非现有 schema/runtime 无法表达，否则禁止另造状态机。
- Terra finding 缺少 `repair_intent` 时，不得机械全部放行。只允许从结构化 `requirement_id`、target item/page job 与已存在的 finding fields 推导有限、确定、source-faithful 的 repair family；无法唯一安全映射的 finding 必须继续 no-winner/fail closed。
- repair directive 必须真实影响 render-input / rendered pixels，而不是只改变 JSON state。任何新增/已有 intent 都必须有 production consumer 与前后 identity evidence。
- 至少覆盖 038 暴露的通用 blocker classes：audience-facing internal/meta copy、figure/caption/supporting-copy overlap、undersized table/primary scientific object、process/next-step diagram collision、medical annotation/legend obstruction。
- audience-copy repair 不得发明新科学 claim。应优先删除内部制作短语并回落到同一 page job 已有的 source-grounded `key_message`/annotation/caption/scientific object；若无法无歧义恢复，fail closed。
- medical repair 只允许改变 layout/callout/legend placement/crop framing；不得生成、涂改或重绘医学像素和 mask。
- 保留 exact CUHK、gold/reference trace、source fidelity、双层 render identity、一轮 repair 上限、unknown/unsafe fail-closed 与 shared/plugin parity。
- 039 必须使用与 038 无关的 non-holdout regression bundle/page set 验证。可以构造 public-safe/synthetic stress fixture，但必须覆盖真实容量压力，不得只做字符串 unit test。
- 修改 audience pixels 后必须取得 fresh task-local Terra item/page-level evidence；至少 stress pages 与 contact sheet 均需达到现有 mature doctoral group-meeting / strong paper-talk bar。
- 039 PASS 后才允许 Planner 选择新的 statistics/methodology 与 medical-imaging unseen papers创建下一次 Stage 5 验收；当前两篇不得重测。
- 这是唯一、质量保持、范围明确的机械恢复路线，不需要用户产品决策。若 039 自己两轮后仍暴露新的不同 blocker，再按 Program Goal 路由，禁止无限 task chain。
