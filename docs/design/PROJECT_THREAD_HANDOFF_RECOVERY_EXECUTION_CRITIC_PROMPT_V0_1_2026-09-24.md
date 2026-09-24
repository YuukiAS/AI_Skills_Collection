# Project Thread Handoff Recovery — Execution-Ready Critic Review v0.1

你继续作为 AI Research Stack 的长期独立 Critic，对 standalone Skill
`Project Thread Handoff` V0.2 same-Project recovery refinement 做 execution-ready review。

不要实现 source，不要创建 branch/worktree，不要启动 Codex Executor，不要更新 personal Plugin，
不要调用 paid API，不要 merge main。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
standalone Skill / science communication

design_topic_or_task_key:
`science-communication--project-thread-handoff-recovery`

source_branch_or_ref:
`main`

review_stage:
`EXECUTION_READY_PACKAGE_REVIEW`

Approved V5 Proposal:
`docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md`

Approved V5 commit:
`df0ca1ab809cf53b0d14901782bbf1a0d8a70642`

Design result:
`PRE_IMPLEMENTATION_DESIGN_PASS=YES`

Execution package version:
`v0.1`

Implementation Plan:
`docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-09-24.md`

Canonical Goal:
`docs/goals/PROJECT_THREAD_HANDOFF_RECOVERY_GOAL_V0_1.md`

Kickoff Draft:
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_RECOVERY_KICKOFF_V0_1.md`

Execution package commit:
`69209fed4f7e5d7aa2526f12d7db17c6aa4be62e`

Exact implementation branch:
`reviewed/science-communication--project-thread-handoff-recovery`

Exact task-owned worktree:
`../AI_Skills_Collection-science-communication-project-thread-handoff-recovery`

Prior design blocker:
`PTH-06 = CLOSED`

不要无新 direct evidence 重新打开已通过的 V5 architecture。

## 1. Mandatory reads

按 current Critic Role Contract 读取 latest main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/SKILL_AUTHORING.md`

然后读取 exact review objects：

- V5 Proposal @ `df0ca1ab809cf53b0d14901782bbf1a0d8a70642`
- Plan v0.1 @ `69209fed4f7e5d7aa2526f12d7db17c6aa4be62e`
- Goal v0.1 @ `69209fed4f7e5d7aa2526f12d7db17c6aa4be62e`
- Kickoff v0.1 @ `69209fed4f7e5d7aa2526f12d7db17c6aa4be62e`

先检查 package commit 后 latest main drift。若只是其他 task docs/TODO/evidence，不得机械 REVISE。
只有 Project Thread Handoff source/version/icon/distribution、Skill contract、version slot 或 shared generated
semantics直接 overlap 才重新判断。

## 2. Package identity

确认 Plan / Goal / Kickoff：

- version一致 = v0.1；
- 同 task key；
- 同 branch/worktree；
- 同 V5 authority；
- 同 G1/G2/G3；
- 同 Skill/repository version decision；
- 同 personal-wrapper/icon boundary；
- 同 privacy/failure/completion semantics；
- 无语义漂移。

## 3. PTH-06 provenance 是否完整进入 execution package

V5 已通过的核心要求必须在 Plan/Goal/Kickoff可执行：

- authority不由底层是否叫 Memory 决定；
- identifiable target past chat才是 target-thread evidence；
- generic Saved Memory/profile/unsourced recall不能替代；
- route-changing claim必须 target-chat-backed；
- strong vs limited recovery claim分开；
- missing critical provenance -> fail closed；
- 最多一次必要 clarification；
- 不发明 conversation lookup API / transcript API。

请重点检查 Goal/Kickoff没有把 provenance要求弱化成“模型觉得恢复对了”。

## 4. Product semantics fidelity

确认仍是一个 Skill、两个 explicit mode。

Mode A：
- current thread -> one initialization Prompt -> stop。

Mode B：
- same Project new thread；
- target old conversation semantic recovery；
- hydrate current new thread；
- `Recover X and continue Y` 可同一回复继续 Y。

不得新建第二 Recovery Skill、MCP、database、CURRENT、history、browser extension、external API、
Bridge Kit dependency或 transcript system。

## 5. Source scope / metadata / generated parity

允许修改的主要 source必须和 Goal一致：

- `skills/science/communication/project-thread-handoff/SKILL.md`
- `agents/openai.yaml`
- `evals/trigger_queries.json`
- focused tests/public-safe fixtures
- Project Thread Handoff-specific Plugin update prompt
- standalone baseline test
- version/README/changelog/generated parity
- task results

Canonical icon：
`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

必须保持 bytes不变。

确认：
- `allow_implicit_invocation=false` 仍只在 `agents/openai.yaml`；
- read-only Skill identity不回归；
- standalone Skill不会被 generator复制进中央 Marketplace Plugin；
- central Plugin production source不修改。

## 6. Gate Matrix

只允许 G1/G2/G3。

### G1 — Distribution / Explicit Invocation / Visual Identity

必须证明：
- Skill 0.2 source/generated parity；
- explicit-only；
- existing PRIVATE / USER-scope skills-only wrapper identity preserved；
- no MCP；
- canonical icon reused / bundled byte-equivalent；
- target Pro regular Chat explicit invocation。

### G2 — Current-Thread Handoff Regression

同一 final candidate在 regular Chat真实长 thread验证：
- current context；
- authority/recency；
- entity role；
- thread-only delta；
- locator；
- exactly one Prompt；
- no second confirmation；
- no repo write；
- DII/CARE regression；
- no project-name hardcode。

### G3 — Same-Project Recovery / Generalization + Provenance

同一 final candidate在 `AI Research Stack` Project新 thread恢复真实 Bridge/SSH old conversation。

关键条件：
- 用户不重贴完整旧回答；
- recovered Bridge/SSH semantics正确；
- target old conversation本身作为 identifiable past-chat provenance出现；
- user/Reviewer能判断就是目标 conversation；
- generic Memory/profile/unsourced recall不能替代；
- key route-changing claim无 provenance -> G3 strong PASS = NO；
- final claim仅：
  `target-conversation-backed semantic recovery verified; no observed cross-project substitution`
- 不声称 absolute isolation/raw transcript/transcript-level fidelity。

确认 G1/G2/G3全部绑定同一个 final candidate，不新增 G4/G5。

## 7. Target locator / cross-Project boundary

确认：
- title/topic/date/unique phrase/task clue只是 retrieval/candidate-identification clue；
- 没有 source provenance时不能宣称唯一定位；
- 多个真实候选且选错会改 route时最多一次 clarification；
- default-memory Project membership本身不是 provenance；
- Project外/无法归因 context不能成为 recovery authority；
- 不要求另一个私有 Project做 leakage test；
- 不要求用户切 project-only memory。

## 8. Existing personal Plugin wrapper

当前 regular Chat verified distribution是 existing PRIVATE / USER-scope / skills-only personal wrapper。

Package必须做到：

- existing identity only；
- no create-new fallback；
- exact reviewed final-candidate commit可作为 pre-integration source；
- no MCP/connector/database/app/state/external API；
- canonical icon byte-equivalent；
- composerIcon/logo优先 canonical icon；
- SVG不支持时才 deterministic conversion，no redesign；
- optimistic concurrency guard保留；
- private Plugin ID/URL/version/release id不进 public repo。

请特别判断“先从 reviewed final candidate更新 wrapper做 target gates，后续 main integration保持 Skill bytes
byte-equivalent”是否正确，是否避免了“先未验收 merge main”与“验收后再重复更新 wrapper”。

## 9. Version / README / changelog

已通过 design：

- standalone Skill `0.1 -> 0.2`
- repository `5.1.0 -> 5.1.1 PATCH`
- central Plugins `NO_BUMP`
- private wrapper执行时读取 current version/release id后 compatible increment

检查 recovery：
- kickoff-time `origin/main:VERSION != 5.1.0` -> VERSION_DRIFT -> Planner；
- 不自行猜新 version；
- root README standalone card更新为 v0.2并简述 same-Project recovery；
- skills README explicit check；
- root CHANGELOG记录 V0.2。

不要无新 evidence重开版本类别。

## 10. Exact branch/worktree / Host recovery

检查：

task：
`science-communication--project-thread-handoff-recovery`

branch：
`reviewed/science-communication--project-thread-handoff-recovery`

worktree：
`../AI_Skills_Collection-science-communication-project-thread-handoff-recovery`

是否符合 current AGENTS semantic task identity。

Known Host fallback：
若 sandbox拒绝 exact sibling worktree creation，Executor不得换 path/branch或绕过；只报告
`NEEDS_HUMAN_WORKTREE_BOOTSTRAP` + one exact command，用户 sandbox外创建后 same-task resume。

请判断这是否是当前已知环境缺口的最小合法恢复，而不是重新设计 task。

## 11. User-action minimization / target acceptance

用户介入前必须完成：

- source；
- tests；
- generated parity；
- public-safe regressions；
- version/README/changelog candidate closure；
- icon hash；
- candidate freeze；
- commit/push exact branch；
- remote verification；
- wrapper update handoff inputs。

然后一次 target-surface session：
1. update existing wrapper to exact candidate；
2. G1；
3. Mode A G2；
4. Mode B Bridge/SSH G3；
5. target-source provenance observation。

不得要求重复安装或创建新 Plugin。Work/Codex不能替代 regular Chat。

## 12. Privacy / evidence

确认 public repo不提交：

- old thread全文；
- complete private recovery output；
- unrelated Memory Sources；
- private Plugin ID/URL；
- Project transcript dump。

只保存 minimal redacted provenance/criterion receipts。Reviewer若需要 provenance，只允许最小 redacted
screenshot/receipt，不为了 evidence transport要求用户重跑完整 G3。

## 13. Authorization envelope

用户未来发送 approved Kickoff后只授权：

- exact task/branch/worktree；
- frozen source/tests/fixtures/generated/version/README/changelog/results edits；
- deterministic tests；
- ordinary task commits；
- ordinary non-force exact task branch push；
- package/hash generation；
- public docs read。

不授权：

- main merge/tag/release/publish；
- paid API；
- new Plugin；
- MCP/database/external API；
- Bridge Kit/target research repo write；
- destructive/force Git；
- unrelated private data upload。

Existing personal Plugin update在 final target session走正常 ChatGPT-side account confirmation；
repo Kickoff不能冒充平台确认。

## 14. Completion semantics

确认：

- pre-target最多 `FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`
- G1/G2/G3未 same-final-candidate PASS：
  `PROJECT_THREAD_HANDOFF_V0_2_READY != YES`
- overall ready仍需 independent final review + separate authorized integration/release closure
- integrated main Skill bytes必须与 accepted candidate一致。

## 15. Output

先用自然中文判断：

1. Plan是否忠实V5；
2. PTH-06是否完整进入 Goal/Kickoff；
3. G1/G2/G3是否 same-final-candidate且可执行；
4. wrapper/icon/version/privacy合同是否一致；
5. branch/worktree与known Host recovery是否 bounded；
6. 用户是否只在 final candidate后参与一次 target session；
7. 是否存在 implementation前必须关闭的新 blocker。

然后：

`VERDICT = PASS | REVISE`

如果 REVISE：

每条 blocker给：
- stable finding ID
- requirement
- direct evidence
- causal risk
- minimum closure
- owner

不要无新 evidence重新打开已通过的 V5 design。
按 Critic Role Contract自动输出 `NEXT_HANDOFF=PLANNER` 和完整 COPY TO PLANNER prompt。

如果 PASS：

这是 execution-ready PASS。输出：

```text
APPROVED_PROPOSAL_PATH=docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md
APPROVED_PLAN_PATH=docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-09-24.md
APPROVED_GOAL_PATH=docs/goals/PROJECT_THREAD_HANDOFF_RECOVERY_GOAL_V0_1.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PROJECT_THREAD_HANDOFF_RECOVERY_KICKOFF_V0_1.md
APPROVED_COMMIT=69209fed4f7e5d7aa2526f12d7db17c6aa4be62e
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

然后逐字输出 package commit `69209fed4f7e5d7aa2526f12d7db17c6aa4be62e` 中
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_RECOVERY_KICKOFF_V0_1.md`
的 Kickoff 正文。

不得在 PASS 后临场改写语义不同的新 Kickoff。

PASS只批准 implementation package；不执行 Skill、不更新 personal Plugin、不 merge main、不授权 paid call，
也不表示 G1/G2/G3已经通过。
