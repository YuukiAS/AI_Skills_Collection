---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 036_research_presentation_process_page_projection_recovery
---

# Reviewed Handoff Request — 036_research_presentation_process_page_projection_recovery

## Objective

关闭 035 第二轮 fresh Terra 暴露的唯一剩余 Stage 4 视觉 blocker：共享 `EXPERIMENT_DESIGN` 与 `NEXT_EXPERIMENT` process-page layout 在当前真实整套 deck 中仍存在投影尺度不足和无效留白，导致两个 item 及 `deck_contact_sheet` 未达到 mature doctoral group-meeting / strong conference-talk bar。

这不是 035 引入的 regression：当前 slide 4 / slide 6 像素与 034 曾 PASS 的像素完全一致；但 Program Goal 要求用当前 fresh item-level evidence 判断成熟度，不能用旧 PASS 覆盖新的真实质量发现。035 的 generic-model source-grounding 已关闭并冻结保护，不在本任务重做。

## User-provided inputs

- `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Stage 4、Final Quality Gates 与 Quality-Preserving Continuation Policy。
- `035_research_presentation_generic_model_support_recovery` 的 PLAN、两轮 REVIEW、FINAL_REPORT、真实 CI、当前 render/pixel identities 与 fresh Terra evidence。
- 当前 shared/plugin research-presentation production/layout code、Stage 4 engineering regression bundle 与既有 task-local Visual Review contract。

## User constraints

- 保留 035 的 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE` 历史，不创建第三轮。
- 只处理共享 `EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` process-page 的投影尺度、留白利用和必要的 source-backed reflow；不得重做 035 model source-grounding、032 storyline、Stage 2 gold、Stage 3 其他 layout、CUHK identity、medical semantics、dual identity 或 deck-quality-loop 状态机。
- 不降低成熟视觉门槛，不用 034 的旧 PASS 覆盖当前 fresh Terra `REVISE`。
- 不新增无来源科学内容，不用 generic cards/box-arrow/filler 填空；若一页容量无法在成熟投影字号下容纳现有内容，应走现有 capacity/no-winner/split 机制，而不是缩小字体强塞。
- 修复必须按 page-job/general layout semantics 实现，不得按当前 clustered fixture 的标题、术语、页号或 test ID 写死。
- shared skill source 与 Codex marketplace mirror 必须保持 parity。
- 当前 engineering pixels 改变后，必须使用现有 task-local Visual Review contract 获取与新 identity 绑定的 fresh item/contact-sheet evidence；缺 evidence 时等待且不消耗 review round。
- 不运行 Stage 5 holdout，不扩 corpus，不新增外部素材。
- 这不是用户产品/科学选择，不需要用户介入；若本 bounded mechanism 仍无法关闭同一 blocker，再按 Program Goal 判断下一步，不在 036 内无限重试。
