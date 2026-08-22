---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 013_presentation_todo_consolidation
status: AWAIT_HUMAN_DECISION
---

# 013 Presentation TODO Consolidation — Final Report

## 本轮已经解决了什么

013 已完成 TODO consolidation 的实现阶段：`research-presentations/TODO.md` 中原有开放规则被系统分成 `ALREADY_IMPLEMENTED`、`PROMOTE_NOW`、`KEEP_BACKLOG`、`DUPLICATE_OR_SUPERSEDED` 四类；冻结计划允许提升的三类通用规则已经进入 active presentation guidance，并补了相应 regression coverage 与 generated/plugin mirror 一致性检查。Executor 的本地 targeted/full tests、skills validation、marketplace validation 和 Reviewed Handoff validation 均曾通过。

本 task 没有越界进入后续 Phase B/C：没有扩 source corpus、没有 Source Scout、没有修改 Terra 四页 regression、没有启动统计/生统或医学影像 benchmark，也没有调用新的 Terra visual review。

## 为什么现在不能 PASS

冻结计划要求真实 GitHub CI 通过后才能做最终独立实现审核。第一轮 GitHub CI 暴露 Presentation regression generator 的 CI 测试环境缺少 Pillow；Reviewer 要求只修复测试环境/依赖声明，不动 TODO 语义或 Presentation 输出。

第一轮返修后，Pillow 的安装步骤已经成功，但新的干净 runner 又在同一 generator 的 `from pptx import Presentation` 处失败，报 `ModuleNotFoundError: No module named 'pptx'`。这说明当前 CI 依赖不是只有一个孤立的 Pillow 缺失，而是 Presentation regression 的测试依赖没有作为完整集合被仓库/工作流表达。

当前失败证据绑定 main tip `50f38341ba63265b8c714afe14e51e2f62e7a674`：`reviewed-handoff/ci-summary=failure`，GitHub Actions run `32550559050`。其中 Windows sparse checkout 和两个 editable-install smoke 通过；`codex-marketplace` job 在全库测试阶段因缺少 `python-pptx` 失败，后续 marketplace/skills 步骤未执行。

## 为什么停止自动返修

Reviewed Handoff 规定单个 bounded task 最多两轮 review。013 已经历：

1. 第一轮 `REVISE`：缺少 Pillow；
2. 第二轮 `REVISE`：Pillow 已补，但仍缺 `python-pptx`，说明 CI/test dependency repair 尚未完整闭合。

因此不能自动开启第三轮，也不能通过另建 task 绕过同一个尚未关闭的 CI blocker。本 task 必须进入人工决策点。

## 如果继续，最小建议

建议用户允许一次人工授权的 dependency repair，把 Presentation regression generator 在干净 CI 中需要的测试依赖作为完整、可维护的集合声明/安装，而不是继续一次补一个 ImportError。修复仍应严格限制在 CI/test dependency contract，不修改 TODO 分类语义、当前 Terra 四页内容、source corpus 或后续 benchmark。

完成依赖修复后，应重新运行真实 GitHub CI；只有 `Codex Marketplace` 的全库测试、后续 marketplace generation/validation、skills validation/audit 等实际完成并通过，013 才值得重新进入内容级独立审核。

## 当前能力与剩余风险

当前 TODO consolidation 的代码/文档改动已经存在，并有本地验证；但它还没有获得真实 CI 闭环后的最终 Planner PASS。主要剩余风险不是规则分类本身，而是仓库标准 CI 尚不能完整复现 Presentation regression 的依赖环境。

在 013 被人工处理并重新闭环前，Presentation improvement cycle 不得进入 Terra blocker repair、统计/生统 benchmark 或医学影像 benchmark。
