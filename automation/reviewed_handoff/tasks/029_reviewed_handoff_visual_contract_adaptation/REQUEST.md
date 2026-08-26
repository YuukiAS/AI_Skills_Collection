---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 029_reviewed_handoff_visual_contract_adaptation
---

# 029 Reviewed Handoff Visual Contract Consumer Adaptation — Request

## Why this task exists

027 的第二轮 fresh Terra evidence 已确认 Stage 3 仍有四个真实视觉成熟度 blocker，因此后续必须创建新的 bounded Stage 3 business recovery。与此同时，027/028 暴露了一个可机械解决的 consumer gap：Bridge Kit 已经支持 `CURRENT.visual_review_required`、task-local manifest/evidence path 与 `waiting_visual_review_evidence`，但 AI_Skills_Collection 当前 `.github/workflows/ai-bridge-visual-review.yml` 的 push 路径仍只读取 repository-level vars；没有 task-local inputs 时会以 top-level success 静默 skip live review。

这个 gap 已经真实导致 027 返修像素发布后没有自动产生 fresh Terra evidence，随后不得不额外创建 028 做显式 `workflow_dispatch` recovery。若直接进入下一轮视觉返修而不修 consumer wiring，同类控制面 recovery 很可能重复出现。

这不是新的产品/科学选择，也不降低 Presentation 质量门槛。它只是把 AI_Skills_Collection consumer 接到 Bridge Kit 已经存在的 task-local Visual Review contract 上，避免视觉型 Reviewed Handoff 再次依赖 repository-level 固定 vars 或人工 dispatch。

## Product outcome

完成后，新的视觉型 Reviewed Handoff task 只要在 `CURRENT.json` 声明 task-local visual-review contract，并把真实 render + `visual_inputs.json` 发布到 main，GitHub Actions 就能在 push 后自动发现唯一待审 task、使用其 manifest/evidence path 运行 live Visual Review，并把 evidence 写回。无待审 task 时正常 no-op；存在歧义或非法 manifest 时 fail closed，不选择错误 task。

029 PASS 后才创建 Stage 3 的下一项业务 recovery，使其直接使用这个 contract，而不是再复制 027/028 的显式 dispatch workaround。

## Scope

只允许修改 AI_Skills_Collection 的 Reviewed Handoff visual-review consumer wiring、必要的确定性 helper/tests 与对应文档说明。不得修改 Presentation 页面、Stage 2 gold、027/028 历史结论、Bridge Kit 源仓库、Terra 核心语义或 Reviewed Handoff 状态机。
