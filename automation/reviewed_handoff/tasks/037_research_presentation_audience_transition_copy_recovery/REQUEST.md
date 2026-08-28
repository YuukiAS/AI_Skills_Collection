---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 037_research_presentation_audience_transition_copy_recovery
---

# Reviewed Handoff Request — 037_research_presentation_audience_transition_copy_recovery

## Objective

关闭 Stage 4 当前剩余的一个窄范围 audience-facing presentation blocker：正常 production engineering deck 的医学影像页顶部仍直接显示 `Workstream transition` 与 `independent workstream; no causal bridge asserted.`。这类措辞是在向制作系统/审稿流程解释“这里为什么换研究方向”，不是成熟博士组会中面向听众的科研叙述；Program Goal 已明确禁止将 workflow / implementation / 制作型元语言带到 audience-facing slide。

036 已独立 PASS，实验设计页与下一实验页的投影尺度和 source-grounding 均已关闭，并获得真实 CI 与 fresh item-level Terra PASS。037 不重开 036，也不重做已通过页面；只把独立 workstream 的可见切换改成科学、自然、source-grounded 的 audience copy / structural cue，同时继续避免虚构两个研究方向之间的因果关系。

## User-provided inputs

- `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Stage 4、Final Quality Gates 与 Quality-Preserving Continuation Policy。
- 032 已通过的 multi-workstream grouping / continuity 机制与回归。
- 036 的两轮 REVIEW、FINAL_REPORT、真实 CI、fresh Terra 与当前实际 `main.tex`；其中医学页的 same-case Input/GT/Prediction/Error、ROI zoom 和 TP/FP/FN 语义保持正确且冻结。
- 当前 shared/plugin normal production generator、storyline/workstream metadata、exact CUHK Beamer route 与 task-local Visual Review contract。

## User constraints

- 037 是 036 之后的独立 bounded quality-preserving recovery；不得修改 036 terminal history、不得制造第三轮 036 review。
- 只处理 audience-facing workstream transition copy / cue。必须保留统计主线与医学影像方向彼此独立的真实语义，也不得暗示不存在的因果、方法继承或共同结论。
- 不得继续把 `Workstream transition`、`independent workstream`、`no causal bridge asserted`、workflow/QA/provenance 等制作或控制语言直接展示给听众；独立性应优先通过 section title、科学主题标题、版式分隔或来源支持的科研上下文自然表达。
- 生产实现必须由当前 workstream/page-job/source metadata 驱动，不得为当前 `Segmentation robustness` 标题、页号、engineering fixture 或 test ID 写 special case。
- 保留 medical same-case images、ROI、TP/FP/FN legend、CUHK identity、gold selection、render identity、deck rhythm/quality loop、一次 repair budget，以及 slides 2–6 已通过的科学内容和视觉行为。
- shared skill source 与 Codex marketplace mirror 必须保持 parity。
- 修改实际 audience pixels 后，必须通过现有 task-local Visual Review contract 获取 fresh item-level evidence；至少医学页与整套 contact sheet 需要重新审查，且不得用旧 PASS 替代新 evidence。
- 不运行 Stage 5 双-paper holdout，不扩 corpus，不新增外部素材，不降低成熟组会视觉门槛。
- 这是机械可解的 presentation-language gap，不需要用户决策；若 bounded mechanism 暴露新的不同 blocker，再按 Program Goal 路由，不在 037 内无限扩 scope。
