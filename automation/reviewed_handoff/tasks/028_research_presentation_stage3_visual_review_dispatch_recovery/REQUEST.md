---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 028_research_presentation_stage3_visual_review_dispatch_recovery
---

# 028 Research Presentation Stage 3 Visual-Review Dispatch Recovery — Request

## Why this task exists

Stage 3 主任务 `027_research_presentation_executable_cuhk_scientific_layout_system` 已完成 REVIEW_1 的页面修复，并生成了新的 canonical CUHK PDF、六张主要内容页 PNG 与新的 task-local `visual_inputs.json`。真实 Codex Marketplace CI 已通过，机械编译/render 证据也有效。

但 027 当前不能进入第二轮独立审核，因为新的 Terra 视觉证据实际上没有产生。GitHub Actions run `32820700238` 虽然 top-level `conclusion=success`，真实 job log 明确显示它由普通 `push` 触发，`AI_BRIDGE_VISUAL_REVIEW_MANIFEST` 与 `AI_BRIDGE_VISUAL_REVIEW_OUTPUT` 均为空，因此 live visual review 被显式 skip，`Commit visual review evidence` 也被跳过。仓库现有 `VISUAL_REVIEW.json` 仍绑定返修前旧像素，而当前 `visual_inputs.json` 已绑定一组新的 PNG SHA。

这不是页面质量失败，也不是需要用户选择的产品语义问题。027 已经使用唯一一次 Plan revision，且冻结规则明确要求“缺少新的 visual evidence 时等待，不消耗 review_round”。因此创建本 task 作为严格限定的控制面 recovery，只执行已经冻结在 027 Plan revision 1 中的显式 `workflow_dispatch` 通路，不修改 Stage 3 业务实现，不消耗 027 第二轮 review。

## Product outcome

完成后，027 应获得一份由 repository secret 通路真实运行 `gpt-5.6-terra` 产生、并与当前返修后六张 rendered PNG identity 一致的 task-local `VISUAL_REVIEW.json`。028 本身不判断这些页面应该 PASS 还是 REVISE；它只恢复缺失的可信视觉证据。随后 Scheduled GPT Reviewer 回到 027，读取 item/page-level judgement 后进行第二轮独立审核。

## Scope

本 recovery 只允许：

- 使用现有 `.github/workflows/ai-bridge-visual-review.yml` 的 `workflow_dispatch` 输入；
- 传入 027 已跟踪的 manifest/output 路径；
- 等待真实 GitHub Actions run 完成并核对其没有 skip live visual review；
- fast-forward 获取 GitHub Actions 写回的新版 `VISUAL_REVIEW.json`；
- 校验新版 evidence 与当前 `visual_inputs.json` 六个 PNG identity 一致；
- 写 028 自己的 RESULT / handoff evidence。

本 recovery 不允许：

- 修改 027 的 PLAN / REVIEW_1 / CURRENT / frozen quality bar；
- 修改 Stage 3 renderer、layout primitives、gold library、canonical CUHK theme 或六张当前 rendered pixels；
- 重新生成页面以“追上”旧 Terra evidence；
- 把 push-triggered workflow 的 top-level success 当作视觉质量 evidence；
- 自行判断 027 PASS/REVISE；
- 创建 Stage 4 或运行 Stage 5 holdout；
- 降低 Terra item/page-level mature-talk 门槛。
