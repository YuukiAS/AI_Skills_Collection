---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 013_presentation_todo_consolidation
review_round: 2
decision: REVISE
implementation_commit: 525eae3faad63c332b53c0961d73a86cf952478a
---

# GPT Review

## Decision

`REVISE`。

第一轮已经把 013 的阻断收敛为“GitHub Actions 的 Presentation regression 测试环境缺少运行依赖”。Executor 的最小返修成功补上了 Pillow，并且新 workflow 中依赖安装步骤本身已经通过；但同一个标准全库测试随后在同一 generator 的下一项未声明依赖 `python-pptx` 上再次失败。由于这是第二轮 review，按 Reviewed Handoff 的两轮上限，本 task 不能继续自动返修，必须进入 human gate。

## Blocking findings

### F-013-CI-02 — Presentation regression 的 CI 依赖仍未完整表达

- **冻结计划 / 回归依据**：`PLAN.md` Acceptance gate 8 要求当前 Presentation/Marketplace/全库验证在真实 GitHub CI 中通过；第一轮 `F-013-CI-01` 已明确要求修复“测试运行环境/依赖声明”，使 `Codex Marketplace` 的标准全库测试能在干净 runner 上执行现有 Presentation generator。
- **真实观察证据**：当前 main tip `50f38341ba63265b8c714afe14e51e2f62e7a674` 的 commit status `reviewed-handoff/ci-summary` 为 `failure`，指向 GitHub Actions run `32550559050`。该 run 中 `windows-sparse-checkout` 与两个 `editable-install-smoke` 均通过；`codex-marketplace` job 的新增 `Install Codex marketplace test dependencies` 步骤成功安装 `Pillow>=10`，但随后 `python3 -m unittest discover -s tests` 仍失败。唯一失败测试仍是 `test_research_group_meeting_regression_generator_outputs_artifacts`，这次 generator 在 `from pptx import Presentation` 报 `ModuleNotFoundError: No module named 'pptx'`，111 个测试中 1 个失败，后续 marketplace generation/validation、skills validation/audit 因前序失败被跳过。
- **为什么阻断**：第一轮修复只补了最先暴露的 Pillow，而没有把该 Presentation regression generator 在干净 CI 中需要的测试依赖完整声明出来。冻结计划要求的是可重复运行的真实 regression gate，不是逐个追着 ImportError 打补丁。
- **最小修复方向**：如果用户允许继续，应把该 generator/Presentation regression 所需的测试依赖作为一个完整、可维护的 CI/test dependency 集合声明并安装，至少覆盖当前真实导入链，而不是继续一次只补一个包；仍不得修改 TODO 分类语义、四页 Terra 内容、source corpus 或后续 benchmark 来绕过本 CI 问题。
- **复验条件**：干净 GitHub runner 上 `Test Codex marketplace builder` 完整通过，后续 marketplace generation/validation、skills validation/audit 能实际执行并通过；同时保持现有 Presentation targeted tests、generated/plugin mirror 一致性和 Reviewed Handoff validation 通过。

## Review-limit decision

本轮是第 2/2 次 review，仍为 `REVISE`。因此必须设置 `review_limit_reached=true`，进入 `AWAIT_HUMAN_DECISION`，不得自动开启第三轮 repair，也不得新建另一个 task 来规避同一未关闭的 CI blocker。

## Non-blocking notes

013 的 TODO consolidation 内容本身仍未完成最终独立 PASS 审核；当前第二轮依然被 CI gate 截住。现有证据没有显示 TODO 分类语义已经错误，但在标准 CI 恢复前不能宣称 013 完成，也不能进入 Phase B。
