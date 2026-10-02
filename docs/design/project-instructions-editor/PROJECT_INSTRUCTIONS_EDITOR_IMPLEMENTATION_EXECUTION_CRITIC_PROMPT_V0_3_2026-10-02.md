# Critic Prompt — Project Instructions Editor Implementation Package v0.2

你现在负责对 `project-instructions-editor` standalone Skill 的 implementation execution package v0.2 做独立 Critic 复核。

这不是重新设计产品。
最终产品/架构 design freeze 已 PASS。
上一轮 execution-ready review 只留下 E1/E2 两个 blocker。

## Active Review Context

```text
target_repo:
YuukiAS/AI_Skills_Collection

target_plugin_or_domain:
standalone Skill / project-instructions-editor

design_topic_or_task_key:
project-instructions-editor--standalone-skill-implementation

source_branch_or_ref:
main

review_stage:
execution-ready implementation package v0.2 review

approved design freeze:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md

design-freeze Critic PASS:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md

prior implementation Critic review:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-02.md

prior Critic result:
REVISE

stable blockers:
E1
E2

implementation Plan v0.2:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md

canonical Goal v0.2:
docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md

Kickoff v0.2:
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md

v0.2 package commit:
bc191c2875ced0a2a551258bddeeb2d819161f25

tracking:
Issue #93

USER_AUTHORIZED_IMPLEMENTATION_PHASE=YES
READY_FOR_CODEX=NO
```

如果 package commit 后 `main` 只有 tracking/handoff/docs-only drift，使用最新真实 main，不回退。

## 必须读取

先读取 latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/SKILL_AUTHORING.md`
- `docs/skill-todos/project-instructions-editor.md`

必须读取：

- v0.2 Plan
- v0.2 Goal
- v0.2 Kickoff
- v0.1 Critic review

按需要复核 approved design freeze。

核对 latest `VERSION`、Issue #93 当前真实状态。

不要重新打开 v0.1 Critic 已经 PASS 的产品/source/version/surface/authorization判断，除非 v0.2 引入了真实回归或出现新直接事实。

## Planner disposition

```text
E1=ACCEPT
E2=ACCEPT
```

v0.2 只修这两项。

## E1 closure — G4 ownership / stop point

v0.2 现在明确：

### Executor owns

- final candidate implementation；
- G1 PASS；
- G2 PASS；
- G3 PASS；
- 从 exact final candidate 生成 G4 完整代表性 input/source/output packet；
- 非独立 self-check。

Executor-owned G4 file：

```text
results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_PACKET.md
```

Executor 的最大 G4 状态：

```text
G4_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor 可以在此基础上达到：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

但不得给：

```text
G4=PASS
IMPLEMENTATION_OVERALL=PASS
```

### Independent Reviewer owns

Reviewer 必须读取：

- final Skill source；
- exact candidate identity；
- G1–G3 evidence；
- G4 complete packet；
- 完整 user artifact；
- README/VERSION/CHANGELOG candidate；
- package identity；
- candidate immutability proof。

Reviewer-owned G4 review：

```text
results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_REVIEW.md
```

Reviewer 才给：

```text
G4=PASS|REVISE
IMPLEMENTATION_OVERALL=PASS|REVISE
```

四个 Gate taxonomy 不变。
没有新增 G5。

请优先判断 E1 是否已经完全关闭：

- 是否还存在 Executor 自评 G4 PASS 的文字；
- 是否 stop point 仍要求一个尚未发生的 independent review；
- Goal/Plan/Kickoff 三者 owner 是否一致；
- packet/review file 是否不再混淆。

如果关闭，明确：

```text
E1=CLOSED
```

## E2 closure — exact final candidate identity

v0.2 冻结的 sequence：

```text
finish all candidate-owned content
-> deterministic preflight/tests
-> create FINAL_CANDIDATE_COMMIT=C
-> install standalone Skill from C
-> G1 on C
-> G2 on C
-> G3 on C
-> G4 complete task packet from C
-> portable zip from C runtime tree
-> evidence-only commit(s)
-> EVIDENCE_HEAD=E
-> prove C..E contains no candidate-owned changes
-> independent Reviewer
```

### Candidate-owned content

在 `C` 前完成并冻结：

- Skill source/reference/evals/assets；
- focused test / standalone baseline；
- generated registry/catalog/provenance/runtime identity；
- README candidate；
- VERSION candidate；
- CHANGELOG candidate；
- current repo required release parity content。

### C 后允许内容

tracked changes 只能位于：

```text
results/project-instructions-editor--standalone-skill-implementation/**
```

并且只能是 evidence/result/review-handoff/reviewer files。

portable zip 不得反向修改 source。

### Reviewer handoff identity

必须同时给：

```text
FINAL_CANDIDATE_COMMIT=C
EVIDENCE_HEAD=E
```

并保存可复核：

```text
git diff --name-status C..E
```

或等价 proof，证明 candidate-owned files没有变化。

### Candidate change after C

如果任何 candidate-owned content 在 `C` 后变化：

- 旧相关 Gate evidence stale；
- 创建新 candidate `C2`；
- 按 blast radius 重跑相应 Gate；
- final review只绑定最新 candidate；
- 禁止跨 candidate 拼 PASS。

### Portable package

zip 必须从 exact `C` runtime Skill tree 生成。

MANIFEST 记录：

- `C`
- zip SHA-256
- archive file list
- runtime tree identity/hash
- generation method。

请优先判断 E2 是否关闭：

- Gate 是否全部绑定 exact candidate；
- 是否还存在 Gate 后才形成 final candidate commit 的倒置顺序；
- `C..E` proof 是否足够直接；
- evidence-only allowlist 是否清楚；
- candidate change后的 stale/rerun 规则是否防止 PASS stitching。

如果关闭，明确：

```text
E2=CLOSED
```

## 已经通过的内容只做回归检查

上一轮已 PASS：

- source path:
  `skills/core/codex-system/project-instructions-editor/`
- standalone version `0.1`
- `requires_network=false`
- `writes_files=false`
- `executes_code=false`
- `recommended_scope=global`
- natural implicit normal entry
- frozen near-miss owners
- preservation-sensitive / greenfield / explicit reset
- protected absence
- bounded edit default
- effective enforcement
- no-op
- proportional delivery
- G1/G2/G3/G4 四个 capability family
- ChatGPT/Codex surface boundary
- public-safe evidence policy
- no Plugin wrapper
- repository MINOR
- `5.4.0 -> 5.5.0` if no VERSION drift
- central plugins `NO_BUMP`
- exact branch/worktree
- no paid API
- no private Project data external transmission
- no main merge/release/tag/publish during Executor stage

只检查 v0.2 是否意外回归这些内容，不移动终点。

## Capability taxonomy

仍然只有：

```text
G1 = Normal entry / routing boundary
G2 = Core Project editing semantics
G3 = Fidelity / authority / should-not-change
G4 = Representative complete task + qualitative final artifact
```

A–L 仍是 regression/task-family bank。

不要因为 owner 拆分而新增第五 Gate。

## Version

上一轮已接受：

```text
Repository bump decision = MINOR
if kickoff-time origin/main VERSION == 5.4.0:
candidate = 5.5.0

project-instructions-editor standalone = 0.1
all central plugins = NO_BUMP
```

如果 current latest main 仍是 `5.4.0`，不重新争论该判断。

Kickoff 时若 VERSION drift：

```text
VERSION_DRIFT
```

返回 Planner，Executor 不自行猜版本。

## ChatGPT / Codex surface

不要重新研究或扩大 surface。

required production normal-entry evidence继续：

```text
AI_Skills / Codex standalone install
+ fresh normal Codex session
```

不要求 ChatGPT Pro Skill upload，不创建 Plugin wrapper。

## Authorization

v0.2 Kickoff 仍只授权：

- exact branch/worktree；
- frozen source/docs/tests/generated/release-candidate/results；
- deterministic tests；
- task-local standalone install/fresh Codex smoke；
- public-safe regression；
- portable zip；
- task-owned commits；
- ordinary non-force push exact branch。

不授权：

- main merge；
- release ref/tag/GitHub Release；
- paid review；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin source；
- Bridge Kit；
- destructive Git；
- watcher/daemon/database/ledger/state machine。

## Maintenance state

Issue #93 应继续：

```text
state = open
maintenance-track
kind:new-capability
scope:standalone-skill
area:standalone-skill
```

Project target：

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
```

如果当前没有 Project field mutation surface：
记录 exact pending mutation，不声称同步，不要求用户手工拖卡片。

Issue reader-facing copy只有真实调用 Clear Writing 后可改。
没有 invocation surface：

```text
CLEAR_WRITING_UNAVAILABLE
```

## PASS / REVISE

如果 E1/E2 已关闭，且 v0.1 已 PASS 内容无回归：

```text
CRITIC_RESULT=PASS
E1=CLOSED
E2=CLOSED
APPROVED_PLAN_PATH=docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
APPROVED_GOAL_PATH=docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md
APPROVED_PACKAGE_COMMIT=bc191c2875ced0a2a551258bddeeb2d819161f25
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

并按 Critic Role Contract 在回复末尾**逐字输出已经审过的 v0.2 Kickoff 正文**，不要 PASS 后另写一份不同 prompt。

如果 REVISE：

```text
CRITIC_RESULT=REVISE
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
```

只允许因：

- E1/E2 尚未真正关闭；
- v0.2 引入新直接 execution risk；
- 或出现新的 current source contradiction。

每个 blocker 必须给稳定 ID、对应要求、直接证据、因果风险、最小关闭条件。

不要用实现期正常文件/代码选择或“还能更详细”阻塞。
