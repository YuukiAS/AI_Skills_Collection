---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 013_presentation_todo_consolidation
review_round: 1
decision: REVISE
implementation_commit: 5f3263fff41401f569cbc78e8fa71de9b8ff56ba
---

# GPT Review

## Decision

`REVISE`。

013 的 TODO consolidation 实现已经交付，但本轮冻结计划明确要求在进入独立实现复核前通过真实 GitHub CI。当前 `main` 的 CI 汇总状态为 failure，且失败 run 与本任务 handoff commit 绑定，因此还不能进入 Phase B，也不能把 013 判为 PASS。

这次阻断不是 TODO 分类语义本身已经被证明错误，而是仓库的标准全库测试在 GitHub Actions 环境中无法完成：Presentation regression generator 运行时依赖 Pillow，但 `Codex Marketplace` 的测试环境没有提供 `PIL`。

## Blocking findings

### F-013-CI-01 — GitHub CI 缺少 Presentation regression 的运行时依赖

- **冻结计划 / 回归依据**：`PLAN.md` 的 Acceptance gate 8 要求运行全库相关验证，并且 `ci_required=true`；只有真实 GitHub CI/check 通过后才允许进入 GPT review。
- **真实观察证据**：当前 handoff commit `35e53a5966638a868f94e522f759c7a748e911da` 的 `reviewed-handoff/ci-summary` 为 `failure`，定位到 GitHub Actions run `32539905527`。其中 `windows-sparse-checkout`、两个 `editable-install-smoke` 均成功，但 `codex-marketplace` job 在第一步全库单元测试失败。失败测试是 `test_presentations.PresentationSharedTests.test_research_group_meeting_regression_generator_outputs_artifacts`；其子进程执行 `generate_research_group_meeting_regression.py` 时在 `from PIL import Image, ImageDraw, ImageFont` 报 `ModuleNotFoundError: No module named 'PIL'`，因此 110 个测试中 1 个失败，后续 marketplace 生成/校验步骤全部被跳过。
- **为什么阻断**：本任务新增/维护的 Presentation regression contract 必须能在仓库标准 CI 环境中重复运行。当前本地验证通过而 CI 缺失 Pillow，说明测试环境依赖没有被仓库/工作流完整表达；在这个缺口关闭前，不能声称本轮 regression gate 已经通过。
- **最小修复**：只修复测试运行环境/依赖声明，使 `Codex Marketplace` 的标准全库测试在干净 GitHub runner 上能导入 Pillow 并执行现有 Presentation generator。优先采用仓库现有依赖管理或 CI bootstrap 的最小一致方案；不要借此修改 013 的 TODO 分类语义、Presentation generator 输出、Terra 四页内容、source corpus 或后续 benchmark。
- **复验条件**：新的 handoff commit 上，`Codex Marketplace` 的 `Test Codex marketplace builder` 必须通过，后续 marketplace generation/validation、skills validation/audit 能继续执行；同时保持 `tests.test_presentations`、全库 tests、generated/plugin mirror 一致性和 Reviewed Handoff validation 通过。真实 CI 汇总恢复为 success 后，再进入 013 的独立内容 review。

## Non-blocking notes

当前没有新增的内容级 blocker。`RESULT.md` 所述 183 项 TODO 分类与三类规则 promotion 尚未在本轮做最终独立 PASS 审核；该审核应在 CI 修复并重新通过后进行，不能被此次 CI 环境问题替代。
