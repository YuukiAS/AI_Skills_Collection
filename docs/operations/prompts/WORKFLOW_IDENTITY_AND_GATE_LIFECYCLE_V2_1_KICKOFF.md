# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Codex Kickoff Draft v2.1

- Execution package version: `v2.1`
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Status: `DRAFT_NOT_AUTHORIZED`
- Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md`
- Goal: `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md`
- Approved design: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md` v2.1
- Design PASS: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_CRITIC_REVIEW_2026-09-20.md`
- This draft becomes execution authorization only if an independent Critic passes this exact Plan + Goal + Kickoff package and the user then sends the approved text below.

## Kickoff

你现在执行 **工作流命名与插件回归机制完善（AI_Skills + Bridge）**。

先读取：

- `YuukiAS/AI_Skills_Collection` 最新 `main` 的 `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- 本任务 Proposal v2.1、Implementation Plan v2.1、Canonical Goal v2.1
- Proposal 的 v2.1 Critic PASS
- `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 `AGENTS.md` 与 Goal/Plan 指定的 task-key source/tests

不要重新设计已批准架构。按 Goal/Plan v2.1 实现。

### 1. 当前用户授权边界

如果我发送这段获批 Kickoff，我明确授权本轮在以下**精确范围**执行。

#### AI_Skills_Collection

允许：

- 从 kickoff-time verified compatible `origin/main` 创建 exact branch  
  `reviewed/cross-repo--workflow-identity-gate-lifecycle`
- 创建 task-owned worktree  
  `/tmp/ai-skills-workflow-identity-gate-lifecycle`
- 只修改 Goal/Plan 批准的：
  - `AGENTS.md`
  - Planner/Critic contracts
  - `PLUGIN_CAPABILITY_GATE_POLICY.md`
  - workflow-core / `codex-workflow-protocol` source 与必要 references
  - AI Skills Maintainer source
  - affected tests
  - canonical Marketplace/generator source
  - generated Marketplace/plugin payload
  - affected TODO/changelog/version/release metadata
  - task-owned repo evidence/results
- 运行 Goal 指定的 focused/full tests、generator/validation/audit
- 运行最多 **2 次** public-safe candidate plugin replay：一次 Verified Workflow、一次 AI Skills Maintainer；可在合法 bounded repair 后只重跑对应失败 replay，不得追加新样本追赢家
- ordinary non-force push 到这个 exact reviewed branch
- 读取 GitHub CI/check 状态

#### GPT_Codex_AI_Bridge_Kit

允许：

- 从 kickoff-time verified compatible `origin/main` 创建 exact branch  
  `reviewed/cross-repo--workflow-identity-gate-lifecycle`
- 创建 task-owned worktree  
  `/tmp/bridge-workflow-identity-gate-lifecycle`
- 只修改 Goal/Plan 批准的：
  - canonical task-key lexical helper/validation source
  - Reviewed Handoff canonical task creation
  - generic workspace validation consumers
  - task-key propagation consumers where required
  - normal authoring docs/templates that still teach new numeric task creation
  - affected tests
  - Bridge version/changelog/docs surfaces
  - task-owned repo evidence/results
- 在 isolated temporary fixture Git repos 中运行 semantic/legacy normal-entry tests
- 运行 focused/full Bridge unit tests
- ordinary non-force push 到这个 exact reviewed branch
- 读取 GitHub CI/check 状态

### 2. 明确不授权

本轮不授权：

- 创建任何 successor task 或 0xx task；
- 在两个真实 repo 中伪造 semantic Reviewed Handoff `CURRENT.json` 来绕过 pre-change parser；
- 修改 001–057 历史 task/result/branch/evidence；
- 修改 056 Plan/Goal/Kickoff 或把本任务和 056 合并执行；
- 修改任何 domain plugin 的专业行为；
- 新增第二 task-key parser、task `display_name` schema、registry、database、ledger、controller、watcher、state machine、title service；
- docs directory reorganization；
- 修改真实 `$CODEX_HOME` / Host Policy；
- 使用 private user data 做 replay；
- OpenAI Responses API、Terra、Visual/Text paid review 或其他额外付费 API；
- 新 provider/account/credential；
- 回显任何 token/secret/credential；
- PR；
- merge 到 `main`；
- tag / GitHub Release / package publish / deploy；
- 修改 remote/upstream；
- force push / rebase / reset / clean / restore unrelated user work；
- 删除 branch/tag；
- 任何 Goal 未明确授权的 live-global side effect。

GitHub 正常 fetch/push、现有 Codex identity 的 bounded candidate plugin replay，以及本地 isolated test repo 不属于新增 provider 授权；不得借此扩大到其他外部服务。

### 3. Preflight：先核 source/version，再创建 branch

在任何 production mutation 前核对：

```text
AI_Skills expected:
Repository 5.0.5
workflow-core 0.1
ai-skills-core 0.2

Bridge expected:
0.8.3
```

并确认当前相关 source 没有被 056 或其他任务实质推进。

若版本槽/source 已发生相关漂移：

```text
STOP_BEFORE_MUTATION=YES
NEXT_OWNER=GPT_PLANNER
```

不要创建 task branches/worktrees后再猜怎么适配；不要自行选新的版本号。

### 4. Cutover bootstrap

这个任务本身正要实现 semantic canonical creation。

因此：

- 不用旧 numeric task key bootstrap；
- 不在真实 AI_Skills/Bridge repo 手写 semantic Reviewed Handoff task control files；
- 用本 approved Goal/Plan/Kickoff + exact semantic Git branches执行；
- Bridge candidate 支持 semantic creation 后，只在 isolated fixture repo 通过正式 `ai-bridge reviewed-handoff task init` 验证 G1/G4。

### 5. 实现要求

#### Bridge

只实现：

- semantic/legacy lexical validation；
- one canonical lexical authority；
- canonical new creation semantic-only；
- generic validation legacy + semantic；
- collision fail closed；
- task/result/branch/CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT/Text Review/Visual Review/runner 等 identity propagation；
- normal authoring guidance切换到 semantic new-task default；
- legacy examples/history保留；
- 版本候选 `0.8.4`，前提是 preflight tuple未漂移。

Bridge 不理解 AI_Skills plugin slug/scope ownership，不新增 workflow state/schema。

#### AI_Skills

只实现：

- scope precedence；
- stable Gate taxonomy + growing regression bank lifecycle；
- Gate merge/split/retirement obligation preservation；
- cheap deterministic bank first；
- approved narrow eligibility；
- mandatory broad/full fallback；
- same-final-candidate；
- grader/eval semantics handling；
- human-readable short label vs technical locator；
- workflow-core 最小执行语义；
- AI Skills Maintainer 最小 maintenance closure；
- source/generated parity；
- version/changelog closure。

workflow-core 不实现 parser；domain plugin 保留专业判断。

本任务 release selection 固定：

`BROAD_FULL_FALLBACK`

### 6. G1–G7 与 tests/replay

完整执行 Goal 中 G1–G7。

Bridge 至少证明：

- semantic canonical creation PASS；
- malformed/collision/new numeric creation FAIL；
- legacy + semantic coexistence generic validation PASS；
- semantic key 无损传播所有 mandatory consumer；
- full unit suite PASS。

AI_Skills 至少证明：

- scope precedence；
- Gate lifecycle；
- mandatory broad/full triggers；
- same-final-candidate；
- human label / technical locator separation；
- no governance bloat；
- generator/source parity；
- full unit suite PASS；
- 最多两次 approved candidate plugin replay。

Mechanical PASS 不能替代 replay/独立 review。

### 7. Candidate/version freeze

如果 preflight tuple不变，目标 candidate slots 是：

```text
AI_Skills repository: 5.0.5 -> 5.0.6
workflow-core:        0.1 -> 0.2
ai-skills-core:       0.2 -> 0.3
all other plugins:    NO_BUMP

Bridge:               0.8.3 -> 0.8.4
```

完成 production source、generated payload、versions 后冻结：

```text
AI_SKILLS_FINAL_CANDIDATE_COMMIT=<sha>
BRIDGE_FINAL_CANDIDATE_COMMIT=<sha>
```

所有 release-critical evidence必须绑定这个 exact tuple。

任何后续 production/source/generated/version/acceptance-semantic变化都使旧 tuple失效；不得拼证据。

### 8. Evidence 和 push

需要后续独立 review 的 evidence 必须留在对应 repo，不能只在 `/tmp`。

完成后：

1. 检查 task-owned diff；
2. 跑完 Goal 要求的 focused/full validation；
3. commit task-owned changes；
4. ordinary non-force push 两个 exact reviewed branches；
5. 验证 remote tips == intended local candidate SHAs；
6. working tree clean，或只剩明确记录的 unrelated pre-existing changes；
7. 输出自然中文 handoff。

### 9. 停止点

本轮到以下位置停止：

`NEXT_OWNER=INDEPENDENT_IMPLEMENTATION_REVIEW`

不要 merge main，不发布，不部署，不删 branch，不声称整个 release/production 已完成。

最终先用人类短名称说明“用户现在获得了什么”，再在技术附录给 technical task key、branch、candidate SHA、version、G1–G7、tests/replay evidence。
