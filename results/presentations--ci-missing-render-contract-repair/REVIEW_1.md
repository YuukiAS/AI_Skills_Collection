---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: presentations--ci-missing-render-contract-repair
review_round: 1
decision: PASS
implementation_commit: bb74e18f44428a12f1fea11b98bf30c10af94040
---

# Presentations CI missing-render contract repair — implementation review

## Decision

**PASS。PROCESS PASS；本任务所冻结的 portability behavior PASS。**

本轮实际审查了冻结 `PLAN.md`、真实实现 diff、`RESULT.md`、GitHub CI `39108825156` 的 job/step 和 `codex-marketplace` 日志，而不是只采信 Executor 汇报。

实现严格落在批准范围内：

- `compile_pdf()` 在无 TeX engine 时先返回 `BLOCKED_MISSING_TEX_ENGINE`，同时保留非 materializing font probe 作为 secondary evidence；
- engine 存在但 canonical font resource 缺失时，仍返回 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`；
- Stage 3 与 production-entry validator 仅在显式 `--allow-missing-render` 下新增接受该 canonical-font missing 环境状态；
- strict validation 对相同缺失状态仍 fail closed；
- `BLOCKED_FONT_RESOURCE_TOKEN_MISSING` 仍不在 allowlist；
- 没有改字体策略、模板、视觉行为、CI provisioning、Clear Writing、routing、版本或 changelog。

新增测试用 deterministic mock 分别覆盖 no-engine/no-font 与 engine/no-font，不依赖 runner 恰好安装什么，也没有用 skip/关键词存在性冒充行为验证。

## Scope verification

`base_commit..implementation_commit` 的 production 变化仅为：

- 三份批准的 Presentations source script；
- 三份正式 generated mirror；
- `tests/test_presentations.py`。

其他新增文件均为本 task 的 REQUEST/PLAN/design/Goal/Kickoff/Critic review 等控制或证据文件。implementation commit 后到 reviewer handoff head 只更新 `CURRENT.json` 与 `RESULT.md`，没有二次修改 production source。

Source/generated 三对脚本在实现后保持 byte-identical。

## CI and regression evidence

GitHub Actions run `39108825156`：

- head branch：`reviewed/presentations--ci-missing-render-contract-repair`
- CI head：`e89b0fffffd9d8c65472d5d017dd56a0adf74ccd`
- conclusion：PASS
- `codex-marketplace`：PASS
- Linux editable install：PASS
- Windows editable install：PASS
- Windows sparse checkout：PASS

`codex-marketplace` 日志直接显示：

- 只安装 Python presentation regression dependencies；没有安装 TeX 或 private canonical font bundle；
- full repository tests：`344 / 344 PASS`；
- Marketplace write / validate / path-report / check：PASS；
- skills validate：PASS；
- generated-file cleanliness：PASS。

Executor 另记录：

- focused dependency-state + 原三项 CI failure regressions：`6 / 6 PASS`；
- full `tests/test_presentations.py`：`48 / 48 PASS`；
- second Marketplace clean/idempotent check：PASS；
- `git diff --check`：PASS。

以上证据足以证明本 task 的 portability regression 已关闭。

## Product boundary

本 PASS **只证明**：

- 最小主机的 missing-render typed state 合同一致；
- `--allow-missing-render` 能正确区分环境缺失与产品/source defect；
- strict production render acceptance 没有被放宽；
- 该 Presentations 外部 CI blocker 已具备被 Clear Writing 消费的条件。

本 PASS **不证明**：

- Presentations 视觉质量或 release readiness；
- Issue #98 broader shared-core/two-skin 工作完成；
- 真实 deck render 已通过；
- Clear Writing 产品或 Web gate 已通过。

## Next step

本 task 已满足独立 Reviewer gate。下一步只应把这个 exact repair 合法集成到当前 `main`，随后让 `clear-writing--scientific-explanation-readability-repair` 消费该 main 并重跑其 unchanged required full CI。不得借本 PASS 启动 broader Presentations work。
