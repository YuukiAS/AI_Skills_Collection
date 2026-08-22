---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 016_statistical_method_group_meeting_benchmark
review_round: 2
decision: REVISE
implementation_commit: 7e3a4658909781d34899f6ad0b7d784648f1ac50
---

# GPT Review

## Decision

`REVISE`。

本轮不能进入 Presentation quality PASS。原因不是当前五页视觉内容被重新判差，而是 016 revised implementation 的必需 GitHub CI 在当前 handoff tip 上明确失败。按照 Reviewed Handoff 协议，CI failure 与普通 Reviewer finding 共用同一 review-round 预算；016 已经使用过第一轮审核，因此这次明确的 CI failure 构成第二轮 `REVISE`，必须进入人工决策点，不能自动开启第三轮。

## Evidence reviewed

### 真实 CI

当前 handoff tip：`e43a364fcbbecb56e13aa8d6d515ec24374dbac5`。

`reviewed-handoff/ci-summary` 当前为 `failure`，指向 GitHub Actions run `32575849316`。该 run 的 `Codex Marketplace` job 失败，而 Windows sparse checkout 与 Linux/Windows editable-install smoke 均通过。

失败发生在 `python3 -m unittest discover -s tests`。Presentation regression 进入：

`tests/fixtures/presentations/statistical_method_group_meeting/generate_statistical_method_group_meeting_benchmark.py`

后，在模块导入阶段报：

```text
ModuleNotFoundError: No module named 'matplotlib'
```

当前 workflow 已成功安装并验证 Pillow 与 `python-pptx`；本次新的失败说明统计 benchmark generator 的 CI/test dependency contract 仍不完整，干净 runner 中没有安装 `matplotlib`。

### 当前视觉证据

当前 revised implementation 已产生新的真实 PPTX/PDF/PNG identity。最新 tracked `VISUAL_REVIEW.json` 使用 `gpt-5.6-terra`，五页均为 `PASS`，没有 blocking finding；其 rubric 已覆盖数学排版、内部元语言泄漏、AI-template 痕迹、视觉成熟度、投影可读性与 reference-informed quality。Executor 结果也记录：核心公式已改为真实数学渲染，audience-facing RRL/provenance/QA 元语言已删除，reference-design audit 与 deterministic anti-leak / math-source gate 已建立。

这些证据说明 revised Presentation implementation 已经完成了实质质量重构，但在必需 CI 失败关闭之前，Planner 不得把 Terra PASS 或本地测试自报替代为最终 PASS。

## Blocking finding

### F-016-02 — 干净 CI runner 缺少 statistical Presentation regression 的 `matplotlib` 依赖

**冻结依据**：Revised PLAN 的 Local validation / CI 与 acceptance gates 要求真实 GitHub CI PASS；deterministic simulation、result figure、math/render pipeline 必须在标准验证链上可重复执行。

**真实证据**：GitHub Actions run `32575849316` 的 `codex-marketplace` job 在全库单元测试中导入 statistical benchmark generator 时直接因 `matplotlib` 缺失退出。Pillow 与 `python-pptx` 已成功安装并通过 import probe，因此不是此前依赖问题的重复假象，而是当前 generator 新增的第三方绘图依赖没有进入 CI/test dependency contract。

**最小修复**：只补齐 Presentation regression 的测试依赖声明/安装，使干净 GitHub runner 能导入并运行当前 statistical benchmark generator。应一次性核对该 generator 的实际第三方顶层导入，避免继续按 `ImportError` 一个包一个包补；不得修改 016 的 DGP、simulation 数值、当前五页内容、Terra rubric、reference corpus 或 revised Plan。

**复验条件**：

- 干净 runner 能导入 statistical benchmark generator 所需第三方包；
- `python3 -m unittest discover -s tests` 通过；
- 后续 marketplace generate/validate/check、skills validate/audit 继续执行并通过；
- current-tip `reviewed-handoff/ci-summary` 变为 `success`。

## Review-limit consequence

这是 016 的第二轮 `REVISE`。根据仓库协议，不得自动开启第三轮 Codex repair。需要人工决定是否授权一次纯机械的 CI/test dependency recovery。若授权，建议像此前 Phase A recovery 一样把依赖修复与 016 的内容质量结论分离，保留本任务两轮审核历史，不把机械依赖问题伪装成 Presentation content regression。
