# workflow-core 0.5 — Execution-ready Critic Re-review Prompt v0.4

你继续作为 AI Research Stack 的独立 Critic thread，对 workflow-core / Verified Workflow 0.5 ordinary bounded implementation execution package 做最小 R4 复核。

这不是新的 design review。Proposal V0.5 已获 DESIGN PASS，G1–G6、qualification/version/final-candidate architecture 与其余 execution package内容已通过。上一轮 execution-ready review 只有两个 blocker：

- WC05-ER3-F01 — sibling worktree不是 execution-ready normal entry
- WC05-ER3-F02 — first publication必须建立 bounded publisher 后续需要的 upstream

本轮只优先复核这两个 blocker及 v0.4 为关闭它们直接引入的回归。不得重新设计 Proposal V0.5，不得恢复 Reviewed Handoff，不得启动 Codex。

## Active Review Context

- target_repo: YuukiAS/AI_Skills_Collection
- target_plugin_or_domain: workflow-core
- design_topic_or_task_key: workflow-core--normal-entry-reliability
- source_branch_or_ref: main
- review_stage: EXECUTION_READY_REVIEW_R4
- approved Proposal:
  docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
- approved Proposal commit:
  7c5a04a1142bdcbbd707f9c998b1a9ce64df66e1
- revised Plan:
  docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md
- revised Goal:
  docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_4_2026-10-01.md
- revised Kickoff:
  docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_4_2026-10-01.md
- exact package commit containing Proposal + Plan + Goal + Kickoff:
  314b28289ee92d4115396fd3c486a4100741692f
- previous reviewed package:
  4e3a696ca3b99b0f9820dbf1ce919248539f7ee8
- previous execution-ready result:
  REVISE
- implementation:
  NOT STARTED
- branch:
  NONE CREATED / NONE AUTHORIZED until user sends approved Kickoff

只审 package commit 314b28289ee92d4115396fd3c486a4100741692f。后续 main 漂移不属于本 review object。

## 1. 最小读取范围

从最新 main 读取当前 rules：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md

从 package commit读取：

- Proposal V0.5
- Execution Plan V0.4
- Canonical Goal V0.4
- Kickoff Draft V0.4

为复核 F02，再独立读取 Bridge Kit formal release 0.9.3 的 ai_bridge_kit/host.py bounded publisher preconditions，确认 current-branch publisher对：

- branch.<branch>.remote = origin
- branch.<branch>.merge = refs/heads/<branch>

的真实要求。

不要把 Bridge runtime modification纳入本task。

## 2. WC05-ER3-F01 — canonical checkout + exact ordinary branch

v0.4 已删除强制 sibling worktree。

Frozen execution identity现在只有：

- canonical checkout:
  /home/yuukias/AI_Skills_Collection
- exact branch:
  work/workflow-core--normal-entry-reliability

执行直接发生在 canonical checkout 本身。

branch mutation前必须按顺序：

1. git fetch origin main；
2. 读取 post-fetch origin/main；
3. 确认 approved package commit是origin/main祖先；
4. 检查 canonical checkout current ownership，不能被另一个任务占用；
5. working tree必须clean；无法安全保留的 unrelated dirty work -> mutation前停止；
6. local exact branch和remote same-name branch必须不存在且无ref conflict；
7. 检查main drift；target/shared generator/version/Gate contract实质漂移 ->回Planner；
8. only then创建并切换 exact branch。

Kickoff只授权一次 exact branch create/switch，不授权任意branch。

请重点判断：

- 这是否真正避开 canonical TODO #11 已知 sibling-worktree/sandbox failure shape；
- 是否仍有隐藏要求创建 sibling worktree/second clone；
- canonical checkout被占用或dirty时是否正确fail closed；
- 是否会为了隔离而自动改用 /tmp、second clone、sibling worktree或更高权限route；
- branch create/switch authority是否足够bounded。

如果仍存在 sibling worktree dependency，F01未关闭。

## 3. WC05-ER3-F02 — first publication + upstream binding

Bridge 0.9.3 bounded current-branch publisher要求 current branch 已经：

- remote = origin
- merge = refs/heads/<same branch>

v0.4 将 first publication冻结在 final candidate形成后、final G1–G6开始前。

preflight必须证明：

- working tree clean；
- exact current branch；
- remote exact branch不存在；
- remote identity正确；
- local HEAD = FINAL_CANDIDATE_COMMIT；
- no force/tags/other refspec。

唯一允许的 first-publication shape是当前Git合同下与下式等价的 exact same-name ordinary non-force publication：

git push --set-upstream origin work/workflow-core--normal-entry-reliability

该一次动作必须同时：

- only create origin/work/workflow-core--normal-entry-reliability；
- establish branch.work/workflow-core--normal-entry-reliability.remote = origin；
- establish branch.work/workflow-core--normal-entry-reliability.merge = refs/heads/work/workflow-core--normal-entry-reliability；
- verify remote OID = FINAL_CANDIDATE_COMMIT。

请判断：

- 这是在任何publisher failure前就冻结、且未来由current-user Kickoff明确授权的 planned first-publication effect，而不是 fallback；
- 权限是否精确到 one repo / one branch / one same-name non-force publication；
- no force/no tags/no other branch/refspec是否明确；
- first publication失败是否只阻塞publication/remote-CI effect并保留local candidate；
- failure后是否明确禁止换raw command shape、force、remote、branch或更高权限route；
- G6是否会在upstream未建立时正确不能宣称PASS。

## 4. first publication 与 G6 / final candidate identity

v0.4 把 first publication移动到：

final candidate frozen
-> exact first publication/upstream
-> same final candidate G1-G6

请判断这是否保持 same-final-candidate contract：

- first publication只改变remote/upstream binding，不改变production candidate；
- remote OID必须精确等于 FINAL_CANDIDATE_COMMIT；
- G1-G6仍直接验证同一个FINAL_CANDIDATE_COMMIT；
-任何production/eval/generated/version变化仍会产生新candidate并要求完整重跑G1-G6。

F02不能因为“remote branch已经存在”就放宽 final candidate identity。

## 5. 后续 publication contract

first publication成功后：

- 所有后续 task-branch publication必须使用执行时 canonical bounded current-branch publisher；
- expected repo必须是 YuukiAS/AI_Skills_Collection；
- expected branch必须是 work/workflow-core--normal-entry-reliability；
- 禁止raw git push、force、tags、其他branch/refspec；
- bounded publisher失败 -> publication/CI handoff blocked；
- local candidate/Gate evidence保持有效；
- no raw/broader fallback；
-不在本task修Bridge。

请确认这正是 F02 所需的完整 closure，而不是只建立 upstream 后又允许 raw push继续。

## 6. Broad CI coherence

v0.4 保持：

- final candidate G1-G6 + broad local PASS；
- evidence-only commits不得改production；
- evidence-only publication走canonical bounded publisher；
- exact task branch workflow_dispatch运行codex-marketplace.yml；
- CI记录workflow head与FINAL_CANDIDATE_COMMIT production-tree equivalence。

请检查 first publication提前后，没有破坏 broad CI / same-final-candidate evidence：

- CI product failure -> new final candidate ->完整重跑G1-G6；
- infra-only failure且candidate不变 ->只重试CI；
- evidence-only HEAD不能冒充final candidate；
- bounded publication failure只阻塞publication/CI effect。

## 7. 其余已通过内容只允许回归检查

只有 v0.4 直接引入回归时才能重新打开：

- ordinary bounded implementation topology；
- no Reviewed Handoff / no Stage A/B / no mid pre-final Critic；
- workflow-core + ai-skills-core；
- source/generated scope；
- G1–G6 semantics；
- G6 actual candidate consumption / actual tool trace / real local Git artifact/commit；
- qualification PASS后exactly-once 0.4 -> 0.5；
- repository execution-time current release -> next PATCH；
- one final candidate；
- broad local + workflow_dispatch CI；
- one independent final Critic；
- effect-scoped truth；
- no paid API；
- no Bridge/Host Policy mutation；
- no Longleaf/STAT5060/specialist mutation；
- no consumer-machine adaptation；
- no destructive Git；
- maturity unchanged。

不要因为本轮解决branch/upstream而重新引入Reviewed Handoff。

## 8. Kickoff authorization envelope

逐字审 Kickoff v0.4。

未来用户发送后应只授权：

- canonical checkout中的 exact branch create/switch；
- task-owned commits；
- zero-paid tests/replay/G1-G6；
- qualification PASS后的exactly-once plugin/repo version mutation；
- final candidate冻结后一次 exact:
  git push --set-upstream origin work/workflow-core--normal-entry-reliability
- 该动作建立only exact remote branch + upstream；
- 后续task-branch publication only canonical bounded publisher；
- final G1-G6 + CI + final Critic PASS后的bounded integration/release/smoke。

不得授权：

- sibling worktree / second clone / /tmp replacement；
- arbitrary branch；
- paid API；
- force/destructive Git；
- branch deletion/arbitrary cleanup；
- stable tag create/move；
- Bridge/Host Policy/publisher mutation；
- Longleaf/STAT5060/render-specialist mutation；
- consumer-machine adaptation；
- scope/Gate/architecture expansion。

## 9. Version boundary

当前：

workflow-core = 0.4 / NO_BUMP
repository bump = NONE
implementation = NOT STARTED
branch = NONE CREATED
maturity = unchanged
paid API = NOT AUTHORIZED

Critic review本身不得改变这些状态。

## 10. 输出要求

给出：

RESULT = PASS

或

RESULT = REVISE

若 REVISE：

- 优先沿用 WC05-ER3-F01 / WC05-ER3-F02；
- 只有v0.4直接引入的新风险才新增finding；
- 每个blocker写 requirement/source、direct evidence、causal risk、minimum closure condition、owner；
- 按 Critic Role Contract自动生成完整Planner返修prompt。

若 PASS：

1. 先用正常中文说明：
   - F01如何通过canonical checkout + exact branch关闭；
   - F02如何通过one-time same-name first publication + upstream binding关闭；
   - why first publication is planned authorization rather than fallback；
   - why later bounded publisher failure still cannot raw fallback；
   - why final-candidate/G1-G6/broad CI architecture remains unchanged。
2. 明确 WC05-ER3-F01 = CLOSED、WC05-ER3-F02 = CLOSED。
3. 明确 READY_FOR_CODEX=YES。
4. PASS只批准 package commit 314b28289ee92d4115396fd3c486a4100741692f。
5. implementation/release仍未开始。
6. 按 Critic Role Contract逐字输出 package commit中的 Kickoff v0.4：

APPROVED_PROPOSAL_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
APPROVED_PLAN_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_4_2026-10-01.md
APPROVED_KICKOFF_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_4_2026-10-01.md
APPROVED_COMMIT=314b28289ee92d4115396fd3c486a4100741692f
READY_FOR_CODEX=YES
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim Kickoff v0.4 from package commit>
=== APPROVED CODEX KICKOFF END ===

不要在PASS后另写一份语义不同的Kickoff。
