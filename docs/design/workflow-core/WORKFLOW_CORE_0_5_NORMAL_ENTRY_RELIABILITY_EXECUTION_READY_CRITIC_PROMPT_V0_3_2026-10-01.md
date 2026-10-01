# workflow-core 0.5 — Execution-ready Critic Review Prompt v0.3

你继续作为 AI Research Stack 的独立 Critic thread。

Proposal V0.5 已获 DESIGN PASS。现在只审查一个普通 bounded implementation execution package 是否真的可交给 Codex；不要重新设计 architecture，也不要启动 implementation。

## Active Review Context

- target_repo: YuukiAS/AI_Skills_Collection
- target_plugin_or_domain: workflow-core
- design_topic_or_task_key: workflow-core--normal-entry-reliability
- source_branch_or_ref: main
- review_stage: EXECUTION_READY_REVIEW_R3
- approved Proposal:
  docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
- approved Proposal commit:
  7c5a04a1142bdcbbd707f9c998b1a9ce64df66e1
- Execution Plan:
  docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_3_2026-10-01.md
- Canonical Goal:
  docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_3_2026-10-01.md
- Kickoff Draft:
  docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_3_2026-10-01.md
- exact package commit containing Proposal + Plan + Goal + Kickoff:
  4e3a696ca3b99b0f9820dbf1ce919248539f7ee8
- old v0.1/v0.2 execution packages:
  SUPERSEDED / NOT EXECUTABLE
- implementation:
  NOT STARTED
- branch/worktree:
  NONE CREATED / NONE AUTHORIZED until user sends approved Kickoff

只审 package commit 4e3a696ca3b99b0f9820dbf1ce919248539f7ee8。后续 main 漂移不是本 review object。

## 1. 必须读取

从最新 main 读取当前 rules：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md

从 package commit读取：

- approved Proposal V0.5
- Execution Plan V0.3
- Canonical Goal V0.3
- Kickoff Draft V0.3

必要时读取：

- docs/plugin-todos/workflow-core.md
- workflow-core current source
- .github/workflows/codex-marketplace.yml
- candidate replay implementation

Bridge只用于 owner boundary / current bounded route reality check，不要求 Bridge 0.10先完成。

## 2. ER3-A — execution topology 是否真正简化

确认 package 已完全放弃：

- Reviewed task
- CURRENT.json
- PLAN_FROZEN
- Reviewed watcher
- Scheduled Reviewer state machine
- Stage A/B
- 第二套 state/schema/controller
- 中途 pre-final Critic

冻结 topology 应是：

~~~
one ordinary task branch/worktree
-> source-first implementation
-> cheap deterministic tests
-> known regressions
-> targeted G1/G2/G3
-> unrelated should-not-change
-> stable 0.4 qualification
-> exactly-once 0.5 + repo PATCH
-> one final candidate
-> final G1-G6 + broad CI
-> one independent final Critic
-> release closure
~~~

判断普通 code/test/fixture repair 留给 Codex，只有 architecture/Gate/scope/version/authority semantics变化才回 Planner/Critic，是否符合 Planner/Critic contracts。

若 Reviewed Handoff 在这个 refinement 中没有不可替代需求，不得因为“更规范”要求恢复旧 control layer。

## 3. ER3-B — exact ordinary branch/worktree 与 authorization

Package 冻结：

- canonical checkout:
  /home/yuukias/AI_Skills_Collection
- branch:
  work/workflow-core--normal-entry-reliability
- worktree:
  /home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability

Critic检查：

- future Kickoff只授权这个 exact branch/worktree；
- 创建前 fetch origin main + drift preflight 是否足够；
- relevant main drift是否会正确停回 Planner；
- exact worktree创建被 Host/sandbox拒绝时是否 fail closed，而不是换 /tmp/clone/branch；
- 是否存在任何旧 Reviewed task identity泄漏。

Critic PASS 本身不得创建 branch/worktree。

## 4. ER3-C — source / maintenance scope

确认 package 忠实执行 Proposal V0.5：

Production source优先限于：

- workflow protocol SKILL.md
- references/escalation-rules.md
- agents/openai.yaml
- evals/trigger_queries.json
- necessary target regression tests
- canonical generated workflow-core payload
- release阶段必要 version/changelog/README/registry/catalog/Marketplace metadata

默认不改 verification-matrix.md / task-template.md；若真正需要则回 Planner。

确认明确使用 workflow-core + ai-skills-core maintenance companion，且 source read不能冒充 production plugin consumption。

确认不把 Bridge/Host Policy/publisher、Longleaf、STAT5060、render/statistics/browser specialist、#7/#8/#9/#10专属逻辑纳入 implementation。

## 5. ER3-D — qualification 与 exactly-once version bump

0.4 qualification只需要：

- old environment/render regression coverage；
- new approval/route regression coverage；
- targeted G1/G2/G3；
- unrelated should-not-change；
- actual candidate plugin consumption；
- generated parity。

只有 qualification PASS 后才允许：

- workflow-core 0.4 -> 0.5 exactly once；
- repository执行时真实正式版本 -> next PATCH。

检查 qualification不是release claim；workflow-core若不再是0.4会停止；并行 main drift/version conflict会停止而不是猜；maturity不变。

## 6. ER3-E — final candidate identity 与 evidence-only commits

Plan允许：

- 先冻结 FINAL_CANDIDATE_COMMIT；
- Gate evidence后续用 evidence-only commit保存；
- evidence绑定 exact final candidate；
- evidence-only HEAD不得修改 production source/generated/version payload；
- evidence HEAD不能冒充 final candidate。

检查这是否满足 same-final-candidate policy。

任何 production/eval criterion/Gate input/generated/version change都必须产生新candidate并重新完整跑G1-G6。

## 7. ER3-F — G1-G5 忠实度

逐项确认：

- G1：trigger precision、contextual positive、specialist-contained hard negative、simple negative。
- G2：specialist-first + least-privilege normal entry；workspace内可完成时不主动 escalation；optional cleanup不进 required path。
- G3：six-dimension + privilege-non-increasing recovery；approval四类归因；bounded route不raw fallback；W4 circuit breaker；effect-scoped truth。
- G4：同一run、同一final candidate的 inseparable capability-discovery normal entry + true absent contrast。
- G5：W1-W5、0.4 Reviewed routing、source/generated/version parity、specialist-contained negative、adjacent negative、合法lower-privilege recovery、risk-matched broad local regression。

不得因 execution package把 #7/#8/#9/#10专属机制重新塞回来。

## 8. ER3-G — G6 production-compatible evidence

冻结链：

~~~
ordinary complex task
-> workflow-core actual implicit consumption
-> repo-local build/check uses workspace-write normal entry
-> optional cleanup does not escalate
-> canonical/bounded publication route runs
-> safe deterministic authority/transport preflight blocker
-> existing local artifact/commit identity remains valid
-> no raw/broader privileged fallback
-> no second same-class approval-sensitive retry without new information
-> only publication effect remains blocked
~~~

检查：

- actual candidate plugin consumption必须真实观察；
- fixture是真实task-local Git repo/artifact/commit，不是mock object；
- local build/check真实执行；
- bounded publication调用执行时实际production/canonical entry；
- blocker安全、deterministic、pre-network，不随机追逐Auto-review；
- route identity执行时记录，不pin Proposal旧Bridge main SHA；
- actual child/tool trace证明bounded route调用、no raw fallback、no second same-class retry；
- artifact hash/commit identity before/after直接检查；
- mock/helper/self-report/source grep被排除为G6 PASS。

如果 package仍可通过 helper/mock伪造G6，必须 REVISE。

Bridge 0.10 implementation不得成为G6 prerequisite；若当前bounded route有owner bug，workflow-core只验证reaction。

## 9. ER3-H — broad local + remote CI lifecycle

Current codex-marketplace workflow只有 pull_request / workflow_dispatch。

Package选择：

1. final candidate先本地完整G1-G6 + broad local；
2. evidence-only commit不改production；
3. 为CI第一次远端发布 exact task branch时，未来Kickoff显式授权一次 ordinary non-force first publication；
4. 不创建PR；
5. exact task branch调用现有 workflow_dispatch；
6. 后续publication优先current canonical bounded current-branch publisher；
7. bounded publisher失败不得raw fallback。

重点判断：

- first publication是事先冻结、exact branch、current-user授权的 planned effect，不是 bounded publisher失败后的fallback；
- 权限是否足够收窄；
- CI产品failure会产生新candidate并完整重跑G1-G6；
- infra-only failure且candidate不变允许只重试CI；
- bounded route failure只阻塞publication/CI effect并保留local成果；
- package不把Bridge 0.10成功设为前置条件。

如果 first publication仍缺不可推导authority或违反repo当前Git contract，应 REVISE并给最小关闭条件。

## 10. ER3-I — final Critic 与 integration/release

implementation期间只有一个 independent Critic checkpoint：

G1-G6 + broad CI 完成后的 final-candidate Critic。

没有中途 pre-final Critic。

Final Critic PASS前不得：

- integration to main
- formal release
- complete/released claim

Kickoff可条件授权同范围 final closure，但真正执行必须看到 final Critic PASS。

Integration preflight处理 main drift；target/shared generator/version/release竞争修改则回 Planner。无关main变化只有在 workflow-core production payload仍与final candidate byte-equivalent时才能整合。

## 11. ER3-J — effect-scoped publication failure

required publication/release失败时：

~~~
candidate/Gates = PASS
publication/release = BLOCKED
overall complete/released = NO
~~~

确认：

- local artifacts/commit/Gate evidence保持有效；
- 不重跑不受影响步骤；
- 不把publication失败改写成build/Gate失败；
- 不raw fallback；
- 不在本task修Bridge。

optional cleanup/publication只有在Goal本来不要求时才可不阻塞overall completion。

## 12. ER3-K — Bridge identity boundary

Package只把以下作为design-review背景，不当runtime pin：

- formal release = 9dad0ba4bfa54e251f345091c5151ae991251ec9
- release version = 0.9.3
- Critic核实时 current main = ec06fcf01627a874a2582a477fda9761ea03b314
- release ->该main无runtime Python source diff
- Bridge 0.10由另一thread处理

执行时只记录实际 canonical bounded route identity。

确认 Proposal V0.5中旧7df05b98...没有被带成 execution requirement。

## 13. ER3-L — Kickoff authorization envelope

逐字审 Kickoff v0.3。

未来用户发送后允许：

- exact ordinary branch/worktree创建；
- task-owned commits；
- zero-paid local tests/candidate replay/G1-G6；
- exact task branch zero-paid CI；
- 一次 exact ordinary non-force first publication，仅用于建立该task branch remote/CI；
- qualification PASS后的exactly-once plugin/repo version mutation；
- final G1-G6 + CI + final Critic PASS后的canonical bounded integration/release/smoke。

不得授权：

- paid API
- force/destructive Git
- branch deletion
- worktree remove/prune
- stable tag creation/move
- arbitrary branch/worktree
- Bridge/Host Policy/publisher mutation
- Longleaf/STAT5060/render-specialist mutation
- consumer-machine adaptation
- scope/Gate/architecture expansion

若 canonical bounded route失败，raw/broader fallback仍禁止。

## 14. Version boundary

当前：

~~~
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
implementation = NOT STARTED
branch/worktree = NONE CREATED
maturity = unchanged
paid API = NOT AUTHORIZED
~~~

Critic review不得改变这些状态。

## 15. 输出要求

给出 RESULT = PASS 或 RESULT = REVISE。

若 REVISE：

- stable finding ID；
- requirement/source；
- direct evidence；
- causal risk；
- minimum closure condition；
- owner；
- 按 Critic Role Contract自动生成完整Planner返修prompt。

若 PASS：

1. 先用自然中文说明 ordinary bounded topology、branch/worktree/authorization、qualification -> exactly-once bump -> one final candidate、G1-G6、broad CI/publication blocker及未授权边界。
2. 明确 READY_FOR_CODEX=YES。
3. PASS只批准 package commit 4e3a696ca3b99b0f9820dbf1ce919248539f7ee8。
4. implementation/release仍未开始。
5. 按 Critic Role Contract逐字输出 package commit中的 Kickoff v0.3：

~~~
APPROVED_PROPOSAL_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
APPROVED_PLAN_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_3_2026-10-01.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_3_2026-10-01.md
APPROVED_KICKOFF_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_3_2026-10-01.md
APPROVED_COMMIT=4e3a696ca3b99b0f9820dbf1ce919248539f7ee8
READY_FOR_CODEX=YES
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim Kickoff v0.3 from package commit>
=== APPROVED CODEX KICKOFF END ===
~~~

不要在PASS后另写一份语义不同的Kickoff。
