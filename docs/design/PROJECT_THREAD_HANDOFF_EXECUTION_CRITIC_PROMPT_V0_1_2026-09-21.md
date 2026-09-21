# Project Thread Handoff — Execution-Ready Critic Review v0.1

你继续作为 AI Research Stack 的长期独立 Critic，对 standalone Skill
`Project Thread Handoff` 的同版 execution package 做 execution-ready review。

本轮不要实现代码，不要创建 branch/worktree，不要启动 Codex Executor，不要上传 Skill，
不要调用 paid API/evaluator，不要修改 production source。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
standalone Skill / science communication

design_topic_or_task_key:
`science-communication--project-thread-handoff`

source_branch_or_ref:
`main`

review_stage:
`EXECUTION_READY_PACKAGE_REVIEW`

approved design:
`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md`

approved design version:
`V3`

approved design commit:
`164f028b76da265b117e42cfbda1563cd4abb809`

design Critic result:
`PRE_IMPLEMENTATION_DESIGN_PASS=YES`

execution package commit:
`e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06`

Implementation Plan:
`docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_1_2026-09-21.md` v0.1

Canonical Goal:
`docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_1.md` v0.1

Kickoff Draft:
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_1.md` v0.1

planned exact implementation branch:
`reviewed/science-communication--project-thread-handoff`

planned exact task-owned worktree:
`../AI_Skills_Collection-science-communication-project-thread-handoff`

prior blocker status:
- `PTH-01 = CLOSED`
- `PTH-02 = CLOSED`
- `PTH-03 = CLOSED`
- `PTH-04 = WITHDRAWN / NOT A BLOCKER`

不要无新直接证据重新打开已经关闭的 V3 architecture。

## 1. Mandatory reads

按 `CRITIC_ROLE_CONTRACT.md` 先读取 latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/SKILL_AUTHORING.md`

然后读取 exact reviewed objects：

- V3 Proposal @ `164f028b76da265b117e42cfbda1563cd4abb809`
- Plan v0.1 @ `e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06`
- Goal v0.1 @ `e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06`
- Kickoff v0.1 @ `e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06`

先检查 package commit 之后 latest main 是否只有无关 docs/evidence drift。不要因为 Critic handoff
文件或别的 task docs 推进 main 就机械 REVISE；只有 production/version/release/Skill-contract
语义 overlap 才需要重新判断。

## 2. Review question A — package 是否忠实实现 V3

确认 Plan / Goal / Kickoff 没有重新设计：

- standalone Skill vs Plugin；
- name / slug / taxonomy；
- authority / recency；
- thread-only delta；
- CARE role；
- canonical locator；
- no repo write；
- no opt-in write；
- Bridge Kit boundary；
- no database/CURRENT/history/state machine；
- one invocation -> one initialization Prompt；
- minimum sufficient information；
- ChatGPT regular Chat / Work / Codex surface separation。

任何新增机制都必须能回指 V3；否则 REVISE。

## 3. Review question B — execution identity 是否 exact

检查：

Task key：
`science-communication--project-thread-handoff`

Branch：
`reviewed/science-communication--project-thread-handoff`

Worktree：
`../AI_Skills_Collection-science-communication-project-thread-handoff`

是否符合 current AGENTS semantic task identity 与 exact branch/worktree current-user-visible
authorization contract。

特别检查：

- worktree 是否相对 verified canonical repo root，而非任意 cwd；
- occupied/mismatched path 是否 fail closed；
- 是否禁止 /tmp clone / 第二个 worktree / 临场换 branch；
- ordinary non-force push 是否只限 exact task branch；
- Kickoff 是否足以在用户实际发送后形成 bounded authorization；
- 是否错误授权 main merge/release/tag/publish。

## 4. Review question C — source scope 是否完整但不过重

允许：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/   # only if minimally necessary
```

以及现有 generator 产生的 registry/catalog/provenance/domain docs、repository version/changelog/README
candidate closure、task results 和 upload zip。

检查是否存在：

- 为了测试方便新增 scripts/schema/state；
- 把 standalone Skill 复制进中央 Plugin；
- 修改 Bridge Kit；
- 修改 CAT-TRACE/DII/CardiacNexus；
- 新 automation/watcher；
- 不必要的新 distribution system。

## 5. Review question D — G1 / G2 / G3 是否被 Goal 真正冻结

只允许三个 Gate。

### G1

必须最终证明：

- source/generated/provenance/registry/catalog parity；
- agents/openai.yaml 正确；
- upload-ready final package；
- target Pro account 安装；
- target ChatGPT regular Chat 有真实显式 Skill entry；
- explicit-only boundary。

不要把 Codex `$skill` 当成 ChatGPT G1。

### G2

必须是真实 target consumption：

- current user Pro；
- ChatGPT regular Chat；
- 已存在较长 DII thread；
- final candidate 已安装；
- Skill 直接消费 current thread context；
- 用户不重新粘贴历史；
- DII/CARE 语义、latest-user precedence、thread-only delta、locator、single Prompt、
  no confirmation、no repo write 全部直接观察。

如果 regular Chat 无法调用、只能 Work/Codex、或 Skill 无法消费 current thread：

`G2=FAIL`

检查 Plan/Goal/Kickoff 是否明确要求停止回 Planner/Critic，禁止换 surface 维持 PASS。

### G3

CAT-TRACE + CardiacNexus representative regression：

- superseded decision 不复活；
- repo facts 与 thread cognition 分工正确；
- 不 hardcode DII/CARE；
- 不依赖 Bridge Kit。

确认 G3 在用户介入前完成，不要求用户做额外 UI smoke。

不要增加 G4/G5，除非你能指出 V3 三 Gate 完全覆盖不到的直接用户可见能力风险。

## 6. Review question E — 用户只在最后一次 acceptance session 介入

确认 Executor 在找用户前必须完成：

- production source；
- metadata；
- trigger eval；
- contract tests；
- source-first generated parity；
- full relevant tests；
- G3；
- version/README/changelog candidate closure；
- upload-ready zip；
- local archive validation；
- final candidate freeze；
- candidate commit + push；
- remote tip verification。

之后用户计划内只做一次：

1. 上传/安装 final candidate；
2. 回已有 DII regular Chat；
3. 用实际 UI 显式入口调用一次 Project Thread Handoff。

同一 session 内完成 G1 target observation + G2 replay。

请重点攻击：
是否还有正常开发问题会在用户上传后才第一次被发现、但本可在 pre-user validation 中发现；
如果有，要求最小关闭。不要为“更保险”增加第二轮计划内上传/验收。

Target-only runtime failure 发生时允许真实 FAIL + recovery，但不得改写第一次失败或无限 retry。

## 7. Review question F — upload artifact 与 privacy

Planned export：

`private/exports/project-thread-handoff-v1.zip`

结构：

```text
project-thread-handoff/
├── SKILL.md
├── agents/openai.yaml
└── evals/trigger_queries.json
```

当前 OpenAI Skill upload/API contract允许 directory upload或一个仅含单一顶层目录的 zip；Plan 选择
单顶层 zip 用于 target UI upload。

检查：

- package 是否在用户操作前完整；
- 是否本地解包验证；
- 是否 SHA-256 + file list 写入 MANIFEST；
- 是否错误把 tests/results/design docs 打入 Skill package；
- 是否只留 /tmp；
- 是否在 target acceptance 前提前清理 worktree/export。

Privacy：

`target-surface-acceptance.md` 只能存 non-sensitive receipt，不得把 DII/CAT-TRACE/CardiacNexus
私有 thread 全文或完整敏感 handoff Prompt推到公开 repo。

如果 final Critic 需要更直接的 qualitative evidence，只允许一次最小 redacted output/screenshot
handoff；不得要求用户重新安装/重新跑来解决 reviewer transport。

## 8. Review question G — version / README 是否符合 policy

Planner 已实际读取 current version policy，并冻结：

Repository bump decision：
`MINOR`

Planning baseline：
`5.0.6 -> 5.1.0`

理由：
新增正式 standalone user workflow，使 collection 获得此前不存在的长期 Chat thread handoff
repository-level capability。

所有中央 Plugin：
`NO_BUMP`

请独立判断这是否符合
`PLUGIN_VERSIONING_AND_CHANGELOGS.md`。

同时检查 recovery：

- version 修改前重读 `origin/main:VERSION`；
- 如果不再是 5.0.6，必须 `VERSION_DRIFT` 返回 Planner；
- 不得覆盖并行 release；
- branch candidate version 不等于 release 已发生。

README：

- root README 因 repo version + 新用户能力需要最小更新；
- skills README 显式检查，但 taxonomy 已足够时记录
  `README checked: no update required`。

检查是否过度或遗漏。

## 9. Review question H — completion / recovery 是否诚实

确认 Kickoff 不允许把：

- source created；
- tests green；
- zip created；
- G3；
- branch push；
- Codex compatibility

写成整体 ready。

用户 target acceptance 前最多：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

只要 G1/G2 未完成：

`PROJECT_THREAD_HANDOFF_V1_READY != YES`

总体 ready 还需要同一 final candidate 的 G1+G2+G3、独立 final review 与后续合法
integration/release closure。

## 10. Authorization envelope

检查 Kickoff 是否只授权：

- exact branch/worktree；
- frozen source/docs/tests/generated/version/README/changelog/results edits；
- deterministic tests；
- zip generation；
- task-owned commits；
- ordinary non-force push exact branch；
- public docs read。

确认它没有代用户授权：

- ChatGPT account upload/install；
- main merge/tag/release/publish；
- paid evaluator/API；
- external private-data upload；
- Bridge Kit write；
- target research repo write；
- central Plugin source write；
- automation/watcher；
- destructive Git/force push/remote remap。

## 11. Output requirements

先用自然中文说明：

- Plan 是否忠实 V3；
- Goal 是否完整冻结 G1/G2/G3；
- Kickoff authorization 是否 exact/bounded；
- 用户是否只在 final candidate 后介入一次；
- version/README/generated parity/recovery 是否可执行；
- 三份文件是否同版、同 package commit、无语义漂移。

然后：

`VERDICT = PASS | REVISE`

若 REVISE：

每条 blocker 必须包含：

- stable finding ID；
- requirement；
- direct evidence；
- causal risk；
- minimum closure；
- owner。

不要重开已关闭的 PTH-01～PTH-04，除非 package 新引入直接回归。
按 Critic Role Contract 自动输出 `NEXT_HANDOFF=PLANNER` 的完整 prompt。

若 PASS：

这将是 execution-ready PASS。必须按
`CRITIC_ROLE_CONTRACT.md §6.1`：

```text
APPROVED_PROPOSAL_PATH=docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md
APPROVED_PLAN_PATH=docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_1_2026-09-21.md
APPROVED_GOAL_PATH=docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_1.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_1.md
APPROVED_COMMIT=e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

然后逐字输出 package commit 中已经审过的 Kickoff 正文，不要临场改写一个语义不同的新 prompt。

PASS 只批准 implementation package；不执行 Skill、不 merge main、不上传 ChatGPT Skill、不授权 paid call，
也不代表 G1/G2 已经通过。
