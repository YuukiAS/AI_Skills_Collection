# Canonical Goal — workflow-core 0.5 normal-entry reliability v0.4

状态：DRAFT FOR EXECUTION-READY CRITIC
Approved Proposal：
docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
Approved Proposal commit：
7c5a04a1142bdcbbd707f9c998b1a9ce64df66e1
Execution Plan：
docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md

## Objective

以一个普通 bounded implementation完成 workflow-core 0.5：

1. 保持 trigger precision；
2. 实现 specialist-first + least-privilege normal-entry selection；
3. 实现 six-dimension + privilege-non-increasing approval-aware recovery；
4. 强化 W4 approval-rejection circuit breaker；
5. 保持 effect-scoped evidence truth。

最终完成要求：同一个 version-bumped final candidate直接通过G1-G6、broad CI、独立 final Critic与canonical release closure。

## Exact execution identity

未来Kickoff只授权：

- canonical checkout：`/home/yuukias/AI_Skills_Collection`
- exact branch：`work/workflow-core--normal-entry-reliability`

不使用 sibling worktree，也不使用 Reviewed Handoff。

branch mutation前必须完成：`git fetch origin main`、post-fetch drift检查、canonical checkout ownership/cleanliness检查、local/remote exact branch absence检查。只有全部通过后，才允许在 canonical checkout本身创建并切换 exact branch。

canonical checkout若被其他任务占用、存在无法安全保留的 unrelated dirty work、exact branch冲突或 branch create/switch被拒绝，则 mutation前停止回 Planner。不得换 `/tmp`、second clone、sibling worktree、其他branch或更高权限route。


## Required maintenance companions

执行必须真实消费：

- workflow-core
- ai-skills-core / AI Skills Maintainer

source read不能冒充plugin consumption。

## Frozen source scope

优先只改：

- skills/core/codex-system/codex-workflow-protocol/SKILL.md
- skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md
- skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml
- skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json
- 必要target regression tests
- canonical generated workflow-core payload
- release阶段必要version/changelog/README/registry/catalog/Marketplace metadata

禁止修改Bridge/Host Policy/publisher、Longleaf、STAT5060、domain specialists或#7/#8/#9/#10专属production logic。

## Required sequence

~~~
exact ordinary branch
-> source-first implementation
-> cheap deterministic tests
-> known regression bank
-> targeted G1/G2/G3 iteration
-> unrelated should-not-change
-> stable 0.4 qualification candidate
-> qualification PASS
-> exactly-once workflow-core 0.4 -> 0.5
-> repository current release -> next PATCH
-> canonical regenerate
-> freeze one final candidate
-> exact first publication + same-name origin upstream binding
-> same final candidate G1-G6
-> broad local verification
-> exact task branch publication + broad GitHub CI
-> independent final-candidate Critic
-> canonical integration/release closure
~~~

没有中途pre-final Critic。普通bug/test/fixture repair由Codex在冻结Plan内处理。

## Qualification boundary

0.4 qualification candidate必须证明：

- 旧 environment/render regression被覆盖；
- 新 approval/route regression被覆盖；
- targeted G1/G2/G3 PASS；
- unrelated should-not-change PASS；
- candidate plugin真实消费；
- generated parity PASS。

qualification不是release claim，不提前要求完整G1-G6。

## Version boundary

开始：

~~~
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
maturity = unchanged
~~~

qualification PASS后才允许：

- workflow-core 0.4 -> 0.5 exactly once；
- repository从执行时真实正式版本推进一个PATCH。

bump后任何production修复都会产生新final candidate并要求完整重跑G1-G6。

## Final Gates

按 Plan §8直接执行G1-G6。

G4必须same-run inseparable capability-discovery chain。

G6必须具备：

- actual candidate implicit consumption；
- real local repo/artifact/commit；
- workspace-write normal local operations；
- actual execution-time canonical bounded publication entry；
- safe deterministic authority/transport preflight blocker；
- actual command/tool trace；
- artifact/commit identity before/after；
- no raw/broader fallback；
- no same-class approval-sensitive retry without new information；
- only publication effect blocked。

mock/helper/self-report/source grep不能构成G6 PASS。

Bridge 0.10成功不是本Goal前置条件；只记录执行时真实bounded route identity。

## First publication + broad CI

final candidate冻结后、开始final G1-G6前，先确认 remote exact branch不存在，并执行一次Kickoff预先授权的 exact same-name ordinary non-force first publication，等价 command shape：

`git push --set-upstream origin work/workflow-core--normal-entry-reliability`

该一次动作必须同时创建 `origin/work/workflow-core--normal-entry-reliability` 并建立 current branch的 `origin` upstream。禁止 force、tags、其他branch/refspec。

这一次 first publication是事先冻结的planned effect，不是 bounded publisher失败后的fallback。

first publication成功后，所有后续task-branch publication只允许使用当时 canonical bounded current-branch publisher。bounded publisher失败不得raw push fallback。

final candidate本地G1-G6与full local checks PASS后，使用上述已建立的exact task branch和upstream发布evidence-only commits，随后通过当前repo `codex-marketplace.yml` 的 `workflow_dispatch` 运行broad CI。

CI产品失败 -> 新candidate -> 完整重跑G1-G6。  
CI基础设施失败且candidate不变 ->只重试受影响CI。

任何 publication failure只阻塞publication/CI effect并保留local candidate；overall release complete=NO。


## Final Critic

G1-G6 + broad CI全部PASS后才交独立final-candidate Critic。

Critic PASS之前不集成main、不release、不宣布complete。

Critic PASS后，按Kickoff已授权bounded envelope继续canonical integration/release，无需重复索取同一范围授权。

## Completion truth

required publication/release失败：

~~~
final candidate quality/gates = PASS
publication/release = BLOCKED
overall complete/released = NO
~~~

不得反向否定已通过local/Gate evidence，也不得raw fallback。

## Forbidden

- Reviewed Handoff/control state
- paid API
- force/destructive Git
- Bridge mutation
- Longleaf/STAT5060/render-specialist mutation
- consumer-machine adaptation
- task-specific hardcode
- cross-candidate evidence stitching
- 未批准的scope/Gate/version/authority变化

未满足全部frozen completion criteria不得报告complete/released。
