# Canonical Goal — workflow-core 0.5 normal-entry reliability v0.1

状态：DRAFT FOR EXECUTION-READY CRITIC
Authority：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md` @ `de66a18123059f76fd0ead4aa715f84ad066c62b`
Execution Plan：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_1_2026-10-01.md`

## Objective

在 `YuukiAS/AI_Skills_Collection` 中实现并验证 workflow-core 0.5 的三个已批准能力：

1. 精确且克制的 normal-entry trigger；
2. specialist-first targeted capability discovery；
3. 六维全满足、fail-closed fallback equivalence。

最终目标不是“文件改完/测试绿”，而是同一最终候选在真实 production-compatible normal entry 中通过 G1–G5，并完成受控 release closure。

## Frozen execution identity

采用 Reviewed Handoff：

- canonical checkout：`/home/yuukias/AI_Skills_Collection`
- task key：`workflow-core--normal-entry-reliability`
- branch：`reviewed/workflow-core--normal-entry-reliability`
- worktree：`/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- base：执行时 post-sync `origin/main`
- `ci_required=true`
- paid review：NO
- text/visual review：NO

必须使用 Bridge canonical bootstrap/resume；禁止 raw worktree fallback、`/tmp` substitute、second clone、remote remap。

若 exact checkout/worktree/Bridge capability 不成立，停止并返回 Planner；不得自行改 locator。

## Required maintenance routing

实现时显式使用 workflow-core 与 AI Skills Maintainer / ai-skills-core，并记录真实 installed/loaded identity。source-tree read 不能替代 production invocation。

## Allowed production files

仅限 Execution Plan §4 列出的 workflow-core source、对应 generated payload、target regression tests、task evidence，以及冻结 release 阶段需要的 workflow-core/repository version/changelog/README/generated metadata。

默认禁止修改 `verification-matrix.md`、`task-template.md`；若确实需要，返回 Planner。

## Non-substitutable semantics

- complex specialist-contained task 必须保持 workflow-core hard negative；
- capability discovery 必须先消费适用 specialist / canonical project route；
- PATH/package/optional-mode 单点失败不能证明 capability absent；
- fallback 六维必须全部正面证明保持；
- 任一 UNKNOWN/CHANGED 禁止 automatic fallback；
- specialist 明确禁止的 fallback 不得绕过；
- 不允许 task-specific production hardcode；
- 不允许 source string/schema/test count 冒充真实 invocation；
- 不允许不同 candidate/run 拼 G4；
- 不允许通过降低 quality/evidence/safety/artifact identity 来求 PASS。

## G1–G5 completion

按 Execution Plan §8 执行。

尤其 G4 positive 必须单次 final-candidate run 直接观察：

```text
ordinary prompt
-> workflow-core implicit consumption
-> specialist actual consumption
-> targeted capability discovery
-> correct route
-> no non-equivalent fallback
-> bounded expected outcome
```

G4 absent contrast 必须在真正无合法 capability 时 fail closed。

所有 release-critical gate evidence 最终绑定同一个 version-bumped final candidate。

## Required sequence

1. exact Reviewed preflight/bootstrap；
2. source-first implementation；
3. regenerate + cheap deterministic regression；
4. development replay，仍保持 workflow-core 0.4；
5. pre-final Critic；
6. qualification G1–G5；
7. 仅 qualification PASS 后允许 `0.4 -> 0.5` 与 repository PATCH metadata；
8. 重新生成并冻结 final candidate；
9. 同一 final candidate 重新直接通过 G1–G5；
10. independent final review；
11. exact-candidate integration/release closure + production identity smoke。

若 repository formal release 在 version mutation 前已变化，从当时真实版本推进一个 PATCH；若无法无歧义整合，返回 Planner。

## Version boundary

开始时：
- workflow-core = `0.4 / NO_BUMP`
- repository = `5.4.0` package-prep baseline / no current bump
- maturity unchanged

只有 Goal 中规定的 qualification 通过后才允许 bump；release claim 必须由 bump 后 final candidate重新通过全部 release gates。

## Forbidden scope

不得修改或接管：
- Longleaf `/users`、module、conda、TeX architecture；
- STAT5060 source；
- render specialist production source；
- Bridge Kit runtime / Host Policy；
- #7/#8/#9/#10 专属逻辑；
- 新 workflow/state/schema/watcher/daemon；
- consumer machines；
- paid API。

## Stop conditions

出现 Execution Plan §9 任一项立即停止并返回 Planner/Critic。不得用 fallback 绕过 blocker。

## Evidence / report

所有 durable evidence 写入 `results/workflow-core--normal-entry-reliability/`。

最终报告必须给出 exact final candidate identity、G1–G5 result、actual consumption evidence、original-regression replay、hard-negative evidence、true-absent evidence、broad regression、version/changelog/generated parity、CI/release closure、skipped checks/residual risk，以及 Maintenance Board pending/adaptation truth。

未满足所有 frozen completion criteria 时不得报告 complete/released。
