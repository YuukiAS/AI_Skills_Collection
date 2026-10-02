# Canonical Goal — workflow-core 0.5 normal-entry reliability v0.2

状态：DRAFT FOR EXECUTION-READY CRITIC  
Authority：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md` @ `de66a18123059f76fd0ead4aa715f84ad066c62b`  
Execution Plan：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_2_2026-10-01.md`

## Objective

在不改变 V0.4 architecture 的前提下，实现并验证：

1. 精确且克制的 normal-entry trigger；
2. specialist-first targeted capability discovery；
3. 六维全满足、fail-closed fallback equivalence。

最终完成要求仍是 version-bumped 同一 final candidate 真实通过 G1–G5，并完成 independent review 与受控 release closure。

## Execution topology

使用两个**串行** Reviewed Handoff task，共用一个总体 Goal与candidate lineage；不用新 workflow/state/schema/watcher。

### Stage A

- task：`workflow-core--normal-entry-reliability`
- branch：`reviewed/workflow-core--normal-entry-reliability`
- worktree：`/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- `ci_required=true`

作用：source-first implementation + development replay + broad regression +真实 consumption evidence。  
禁止 version bump、main integration、release。

Stage A合法链：

```text
git fetch --all --prune
-> Bridge task bootstrap
-> PLAN_REQUESTED
-> AI Research Stack Planner materializes PLAN_V2
-> PLAN_FROZEN
-> Codex Executor
-> WAITING_FOR_CI
-> Reviewed Reviewer owns CI transaction
-> READY_FOR_GPT_REVIEW
-> Reviewed Reviewer real review
-> PASS / AWAIT_HUMAN_DECISION
-> AI Research Stack pre-final Critic (read-only)
```

Critic PASS不修改 Stage A state；它只授权进入 Stage B setup。Critic REVISE返回 Planner，不用假 REVISE唤醒 Executor。

### Stage B

仅在 Stage A Reviewed Reviewer PASS + pre-final Critic PASS 后创建：

- task：`workflow-core--normal-entry-reliability-release`
- branch：`reviewed/workflow-core--normal-entry-reliability-release`
- worktree：继续使用同一已验证物理 worktree
- base：exact Stage A approved tip
- `ci_required=true`

Stage B branch从 exact Stage A tip创建/切换；随后使用 Bridge `task init` 初始化新 task，在首个 metadata commit把 REQUEST reviewed-worktree locator绑定为 exact worktree，再用 `publish-first` 发布 branch。它不是从 main重新 bootstrap，也不改 Stage A CURRENT。

Stage B合法链：

```text
new Stage B PLAN_REQUESTED
-> AI Research Stack Planner materializes PLAN_V2
-> PLAN_FROZEN
-> Codex Executor:
   0.4 qualification G1-G5
   -> if PASS, exactly-once 0.5 + repo PATCH
   -> regenerate
   -> final candidate G1-G5
   -> broad tests/evidence
-> WAITING_FOR_CI
-> Reviewed Reviewer owns CI transaction
-> READY_FOR_GPT_REVIEW
-> Reviewed Reviewer final review
-> PASS / AWAIT_HUMAN_DECISION
-> AI Research Stack final Critic (read-only)
-> exact final integration/release
```

## Owner contract

- AI Research Stack Planner：Bridge Planner transaction + package authority。
- AI Research Stack Critic：pre-final/final只读 checkpoint，不改 CURRENT。
- Reviewed Handoff Reviewer：读取真实 GitHub CI并拥有 Reviewer transaction。
- Codex Executor：实现 frozen Stage PLAN并交棒，不伪造 Planner/Reviewer decision。

若 exact task-bound Scheduled Planner/Reviewer 在执行 preflight真实存在并绑定正确 task+branch，可以使用；否则使用 Plan §7 的人工 canonical prompt handoff。generic watcher不得冒充 task-bound automation。

每个 Bridge PLAN必须明确：

```text
Maintenance companion: ai-skills-core
Domain owner: workflow-core
```

## G1–G5

G1–G5 semantics与 Approved Proposal V0.4完全一致。

- G1：implicit/contextual positive + specialist-contained hard negative + simple negative；
- G2：specialist-first targeted discovery；
- G3：六维 equivalence逐项 evidence；
- G4：single-run positive chain + true-absent fail-closed；
- G5：0.3/0.4 regressions + adjacent negative + parity + broad tests/CI。

source string/schema/tests数量不能代替真实 production consumption；不同candidate/run不能拼G4。

## Version boundary

开始：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
implementation = NOT STARTED
maturity = unchanged
```

Stage A不得 bump。

Stage B只有 0.4 qualification G1–G5全部 PASS后，才允许：

- workflow-core `0.4 -> 0.5` exactly once；
- repository从届时真实正式版本推进一个 PATCH。

bump后必须冻结新 final candidate并重新直接通过完整G1–G5。

## Publication contract in manual mode

不依赖 generic watcher。

Executor完成合法 handoff commit、working tree clean后，只允许 exact current reviewed branch 使用：

`ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch <exact branch>`

Stage A first metadata publication和Stage B first metadata publication分别使用各自合法 `publish-first` 路径。

Planner/Reviewer的GitHub connector transaction直接写当前 exact remote branch；本地下一角色继续前先按 current contract同步并验证。

## Forbidden scope

不得修改：

- Longleaf `/users` / module / conda / TeX；
- STAT5060；
- render specialist；
- Bridge runtime / Host Policy；
- #7/#8/#9/#10专属逻辑；
- 新workflow/state/schema/watcher/daemon；
- consumer machines。

不得调用paid API。

不得删除 reviewed branches，不得 remove/prune worktree，不得 arbitrary cleanup/force/destructive Git。

## Final release boundary

只有 Stage B final candidate G1–G5 + CI + Reviewed Reviewer + final Critic全 PASS后才允许：

- exact final candidate integration到 canonical `main`；
- ordinary non-force publication；
- repository PATCH formal release；
- canonical contract需要时 fast-forward-only `release` ref closure；
- exact production identity/install-update smoke。

cleanup不属于本 Goal。

## Stop conditions

出现下列任一项返回 Planner/Critic：

- 需要改变V0.4/G1–G5；
- Reviewed state/role handoff不能按Plan合法执行；
- 需要假REVISE/假PASS才能推进；
- Stage B不能从 exact Stage A lineage合法初始化；
-需要Bridge/Host Policy改动；
- candidate lineage/version target不清楚；
- paid API成为必要条件；
- task-specific hardcode。

未满足全部 completion criteria不得声称 complete/released。
