# Slurm Workflows — Final Critic Review R3

日期：2026-10-04  
角色：AI Research Stack 独立 Critic  
审查阶段：FINAL_IMPLEMENTATION_REVIEW_R3

## 审查对象

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `hpc--slurm-race-policy-bounded-opt-in`
- Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
- Exact product candidate: `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- Locator-repair branch tip: `520fd159737c63b2aabdddb43a8e491219fff897`
- GitHub CI: run `37187784359`, exact head SHA `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- Prior blockers:
  - `RACE-B1_COMPLETE_BOUNDED_GATE` — closed in R2
  - `CTL-B1_CURRENT_IMPLEMENTATION_LOCATOR` — this round

本轮只复核 `CTL-B1` 以及 locator-only repair 是否引入直接 blocker。不重新审查已经通过的 Slurm 产品语义。

## 结果

```text
RESULT = PASS

RACE-B1_COMPLETE_BOUNDED_GATE = CLOSED
CTL-B1_CURRENT_IMPLEMENTATION_LOCATOR = CLOSED

READY_FOR_FINAL_INTEGRATION_RELEASE_CLOSURE = YES
```

## CTL-B1 已关闭

当前 reviewed branch tip `520fd159...` 中：

`automation/reviewed_handoff/tasks/hpc--slurm-race-policy-bounded-opt-in/CURRENT.json`

已经正确记录：

```json
{
  "state": "READY_FOR_GPT_REVIEW",
  "ci_status": "PASS",
  "implementation_commit": "5a3dc447da2ea429ba2d229b0301c378be9e8018",
  "next_action": "WAIT_FINAL_CRITIC",
  "review_round": 0,
  "plan_revision": 0
}
```

这与当前真实产品 candidate、RESULT 和 GitHub CI head SHA 完全一致。

从 product candidate `5a3dc447...` 到 locator-repair tip `520fd159...` 的变化只有：

- `CURRENT.json` 的 implementation locator；
- Final Critic R2 review；
- RESULT / Issue progress evidence。

没有 Slurm production source、tests、VERSION、README、CHANGELOG、registry/catalog/generated release surface 变化。因此：

- product candidate identity不变；
- 331-test local full-suite evidence仍然有效；
- GitHub CI run `37187784359` 仍然有效；
- 不需要重跑 CI。

## 产品 closure

上一轮 R2 已确认，且本轮没有产品 bytes 变化：

- site-policy helper只表达 eligibility，不再返回最终 race authorization；
- final ALLOW只能来自完整 bounded gate；
- exactly two distinct routes；
- full frozen workload/scientific contract identity；
- `workload_scope_digest` mismatch fail closed；
- GPU / memory / CPU / walltime hard resource contract；
- closed winner/tie policy；
- `keep_both` / unknown policy fail closed；
- H100/A100只有在 frozen workload允许两类 accelerator时才能通过；
- installed normal-entry race smoke直接消费安装后的 helper；
- Longleaf/CUHK仍为 `disabled_by_default`；
- `REAL_SLURM_MUTATION = NO`。

因此此前 REVISE 暴露的两个问题已经全部关闭，不再存在 Slurm product repair。

## Version / release identity

当前 formal `release` 仍为：

- repository `5.4.3`
- `slurm-workflows 0.3`
- commit `03b0281b1f7fbd29621faa6298cd1db2578a0ffc`

当前 candidate保持：

- repository target `5.4.4`
- `slurm-workflows 0.4`
- central Plugins `NO_BUMP`
- Bridge Kit `NO CHANGE`

版本决策仍成立。

## 当前 main drift 与最终发布约束

本轮审查时 current main 已前进到 `eec20c75bc80fe10b0cfa1379b95ac25f73478b2`。

从 candidate base `818b7e643...` 到 current main 的新增内容主要是 Project Instructions Editor 文档，但同时已经出现与 Slurm 无关的 Presentations production source 变化：

- `skills/tools/documents-media/presentations/shared/font-policy.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- 对应 generated plugin payload。

这些不是当前 Slurm `5.4.4` release 的批准内容。

因此 Final Critic PASS 不授权把“当前 main 整棵 tree”机械作为 `release 5.4.4` 发布对象。

最小且正确的 closure 边界是：

1. formal `5.4.4` release必须继续绑定已经通过 exact-SHA CI 的 Slurm reviewed release line，不得把 current-main 上尚未属于本 release 的 Presentations production drift顺带发布；
2. current-main 的无关新内容可以在 main integration 时保留；
3. release ref推进前必须证明其目标 commit相对 formal `5.4.3` 只包含本 `5.4.4` 已批准 release scope及允许的历史/internal docs；
4. release target必须是 current `origin/release` 的后代并通过 canonical fast-forward-only producer；
5. 随后将该已发布 Slurm release closure普通 non-force整合进 latest main，使 release commit成为 main 的祖先；
6. 如果执行时 formal release baseline又前进，或出现与 Slurm/shared release surfaces直接冲突的新 release-critical drift，停止并重新 late-bind，不得猜。

这不是产品 REVISE；这是最终 release isolation preflight。

## Tracking

Issue #96 当前仍：

- OPEN
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`

canonical TODO仍有 `tracking: #96`。

在 formal `0.4` central release完成前保持 DOING 是正确的。

由于本次能力的真实触发来源是 DII，正式 central release后还需要完成 DII 当前 consumer 的 normal-entry安装/加载与只读验证。按 Maintenance Board 的 consumer-adaptation语义，应在 central release后根据 Issue #96 当前 completion contract决定进入 ADAPTING；在 DII consumer仍未加载 `slurm-workflows 0.4` 时，不应提前把“DII 已可正常消费最新版 Skill”描述为完成。

## 最终字段

```text
RESULT = PASS

PASS_OBJECT = 5a3dc447da2ea429ba2d229b0301c378be9e8018
LOCATOR_REPAIR_TIP = 520fd159737c63b2aabdddb43a8e491219fff897

RACE-B1_COMPLETE_BOUNDED_GATE = CLOSED
CTL-B1_CURRENT_IMPLEMENTATION_LOCATOR = CLOSED

RACE_POLICY_TRUTH_TABLE = PASS
FULL_SCIENTIFIC_CONTRACT_IDENTITY = PASS
HARD_RESOURCE_CONTRACT = PASS
CANCELLATION_POLICY_VALIDATION = PASS
INSTALLED_NORMAL_ENTRY_RACE = PASS
LOCAL_FULL_SUITE = PASS
GITHUB_CI_EXACT_SHA = PASS

TARGET_REPOSITORY_VERSION = 5.4.4
SLURM_WORKFLOWS_VERSION = 0.4
CENTRAL_PLUGINS = NO_BUMP
BRIDGE_KIT = NO_CHANGE
REAL_SLURM_MUTATION = NO

PRODUCT_REPAIR_REQUIRED = NO
CI_RERUN_REQUIRED = NO
READY_FOR_FINAL_INTEGRATION_RELEASE_CLOSURE = YES
```

本 PASS 证明 `slurm-workflows 0.4` candidate 已满足冻结产品合同并可进入正式 release closure。它不授权把 unrelated current-main Presentations production drift并入 `5.4.4` release，也不证明 DII consumer 已安装/加载 `0.4`。
