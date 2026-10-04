# Slurm Workflows — Final Critic Review R2

日期：2026-10-04  
角色：AI Research Stack 独立 Critic  
审查阶段：FINAL_IMPLEMENTATION_REVIEW_R2

## 审查对象

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `hpc--slurm-race-policy-bounded-opt-in`
- Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
- Exact product candidate: `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- Evidence/control tip: `aed738017237c2a5779866968d59e5bf7272571f`
- Prior blocker: `RACE-B1_COMPLETE_BOUNDED_GATE`

本轮只复核上一轮 RACE-B1 及修复引入的直接 blocker，不重新扩展产品审查。

## 结果

```text
RESULT = REVISE

RACE-B1_COMPLETE_BOUNDED_GATE = CLOSED
CTL-B1_CURRENT_IMPLEMENTATION_LOCATOR = OPEN

READY_FOR_FINAL_INTEGRATION = NO
```

产品修复已经通过；当前只剩一个 Reviewed Handoff control-plane locator 不一致。该问题不要求修改产品代码、不要求重跑本地 full suite，也不要求重跑 GitHub CI。

## RACE-B1 已关闭

### eligibility 不再冒充最终授权

`duplicate_race_decision()` 现在始终返回 `allowed=False`，并把满足 site-policy + user opt-in 的情况标为 `eligible=True` / `requires_bounded_contract=True`。

因此低层 authority helper 不能再单独形成最终 race authorization。

### 完整 scientific/workload contract identity

`_normalized_workload_contract()` 现在比较完整 frozen workload contract，只排除明确 route-only 字段。

新增回归直接证明未枚举 scientific field（如 augmentation）变化会 DENY，`workload_scope_digest` mismatch 也会 DENY。

### hard resource contract

正式 bounded gate 会检查 workload contract 中的 hard resource requirements，包括 GPU count/type、memory、CPU、walltime 等。

回归覆盖 memory、CPU、GPU downgrade。

### closed cancellation semantics

当前只接受：

- `winner_rule = first_running_job`
- `running_tie_policy = keep_lowest_job_id_cancel_other`
- `cancel_loser = true`

`keep_both`、任意未知 winner/tie rule、缺失 cancellation contract 均 fail closed。

### exactly two distinct routes

正式 gate要求 exactly two candidates，并检查 route identity；相同 route duplicate 会 DENY。

### installed normal-entry evidence

新增 `test_g6_installed_normal_entry_duplicate_race_bounded_gate`：

- 从安装后的 `slurm-workflows/scripts/slurm_routing.py` 加载 helper；
- `disabled_by_default + explicit opt-in + safe bounded contract` -> ALLOW；
- unsafe `running_tie_policy = keep_both` -> DENY。

因此上一轮的 normal-entry 缺口已关闭。

### exact-SHA CI

GitHub Actions run `37187784359` 已独立核实：

- workflow: `Codex Marketplace`
- event: `workflow_dispatch`
- head SHA: `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- conclusion: `success`

以下 required jobs 全部成功：

- `codex-marketplace`
- `windows-sparse-checkout`
- `editable-install-smoke (ubuntu-latest)`
- `editable-install-smoke (windows-latest)`

旧 run `37185949083` 没有被用于给新 candidate 背书。

## CTL-B1 — CURRENT.json 仍指向旧 implementation candidate

### Requirement

Reviewed Handoff 的 `READY_FOR_GPT_REVIEW` 状态必须携带当前实现的 `implementation_commit` locator。

该 locator用于后续 Reviewer / Final Critic 确认自己审的是当前实现，而不是旧 candidate。旧 implementation locator只能作为历史上下文，不能继续充当当前 review target。

### Direct evidence

在 exact product candidate `5a3dc447...` 和当前 reviewed branch tip `aed7380...` 上：

`automation/reviewed_handoff/tasks/hpc--slurm-race-policy-bounded-opt-in/CURRENT.json`

仍为：

```json
{
  "state": "READY_FOR_GPT_REVIEW",
  "ci_status": "PASS",
  "implementation_commit": "cf9bfe16d526811525395d66e05035736e6ecc23",
  "next_action": "WAIT_FINAL_CRITIC"
}
```

但当前真实 product candidate、RESULT 和 GitHub CI 都已经绑定：

`5a3dc447da2ea429ba2d229b0301c378be9e8018`

所以 durable workflow state仍指向上一轮被 REVISE 的旧 candidate。

### Causal risk

如果现在直接 PASS 并进入 integration：

- repository 的正式 Reviewed Handoff truth仍会说当前实现是旧 `cf9bfe...`；
- 后续自动 Reviewer / watcher /审计会把新的 `5a3dc447...` 当成与 CURRENT 不一致的实现；
- 会造成“产品已经修好，但控制面仍指向旧实现”的假 closure。

### Minimum closure

只做一个 control-plane repair：

1. 将当前 task 的 `CURRENT.json -> implementation_commit` 更新为：
   `5a3dc447da2ea429ba2d229b0301c378be9e8018`
2. 保持：
   - `state = READY_FOR_GPT_REVIEW`
   - `ci_status = PASS`
   - `next_action = WAIT_FINAL_CRITIC`
   - `review_round = 0`
   - `plan_revision = 0`
3. 重新运行 task/workflow schema validation。
4. commit + ordinary non-force publish reviewed branch。
5. 返回新的 branch tip 给 Final Critic。

这是 control-plane locator 修复，不改变 product candidate bytes。

因此：

- 不重跑 331-test full suite；
- 不重跑 GitHub CI；
- 不修改 VERSION / README / CHANGELOG；
- 不改 Issue #96 lifecycle；
- 不修改 Slurm source/tests；
- 不执行真实 Slurm mutation。

## Main/release drift

当前正式 release仍为 repository `5.4.3` / `slurm-workflows 0.3`。

当前 main 相对本 candidate base仅新增一份无关的 Project Instructions Editor 设计文档，不触及 Slurm source、shared runtime、version/generated surfaces或 release-critical tests，因此不是 blocker。

## 最终字段

```text
RESULT = REVISE

FINAL_CANDIDATE = 5a3dc447da2ea429ba2d229b0301c378be9e8018
EVIDENCE_TIP = aed738017237c2a5779866968d59e5bf7272571f

RACE_POLICY_TRUTH_TABLE = PASS
FULL_SCIENTIFIC_CONTRACT_IDENTITY = PASS
HARD_RESOURCE_CONTRACT = PASS
CANCELLATION_POLICY_VALIDATION = PASS
INSTALLED_NORMAL_ENTRY_RACE = PASS
LOCAL_FULL_SUITE = PASS
GITHUB_CI_EXACT_SHA = PASS

RACE-B1_COMPLETE_BOUNDED_GATE = CLOSED
CTL-B1_CURRENT_IMPLEMENTATION_LOCATOR = OPEN

PRODUCT_REPAIR_REQUIRED = NO
CI_RERUN_REQUIRED = NO
PLANNER_REENTRY_REQUIRED = NO
REAL_SLURM_MUTATION_REQUIRED = NO
BRIDGE_CHANGE_REQUIRED = NO

READY_FOR_FINAL_INTEGRATION = NO
```
