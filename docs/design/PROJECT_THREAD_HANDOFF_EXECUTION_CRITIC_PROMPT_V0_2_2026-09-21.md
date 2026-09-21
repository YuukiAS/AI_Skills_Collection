# Project Thread Handoff — Execution-Ready Critic Recheck v0.2

你继续作为 AI Research Stack 的长期独立 Critic，只复核
`Project Thread Handoff` execution package v0.2 对唯一 blocker `PTH-05` 的关闭情况，
以及 v0.2 是否意外引入新的直接风险。

不要实现 Skill，不要创建 branch/worktree，不要启动 Codex，不要上传 Skill，不要修改 production source。

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
`EXECUTION_PACKAGE_RECHECK_AFTER_PTH_05`

Approved V3 Proposal:
`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md`

Approved V3 commit:
`164f028b76da265b117e42cfbda1563cd4abb809`

Prior reviewed execution package:
v0.1 @ `e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06`

Prior Critic verdict:
`REVISE`

Only blocker:
`PTH-05 — Read-only Skill frontmatter 没有被冻结`

Current reviewed execution package:
v0.2 @ `451e8b32c8d3f2521372f591ff3e2d90968f297e`

Implementation Plan v0.2:
`docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_2_2026-09-21.md`

Canonical Goal v0.2:
`docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_2.md`

Kickoff Draft v0.2:
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_2.md`

Exact task key:
`science-communication--project-thread-handoff`

Exact implementation branch:
`reviewed/science-communication--project-thread-handoff`

Exact task-owned worktree:
`../AI_Skills_Collection-science-communication-project-thread-handoff`

Existing architecture findings remain:

- `PTH-01 = CLOSED`
- `PTH-02 = CLOSED`
- `PTH-03 = CLOSED`
- `PTH-04 = WITHDRAWN / NOT A BLOCKER`

除非 v0.2 自己引入新的直接回归，不得重新打开这些 finding。

## 1. Mandatory reads

按 Critic Role Contract 读取 latest main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/SKILL_AUTHORING.md`
- `scripts/skills.py` 中 `command_new`
- `scripts/skill_utils.py` 中 `skill_record`

然后读取：

- approved V3 Proposal；
- v0.2 Plan；
- v0.2 Goal；
- v0.2 Kickoff。

先核对 package commit 之后 latest main drift。若只是本 Critic handoff 或其他无关 docs/evidence，
不得因此 REVISE。

## 2. 优先复核 PTH-05

上一轮直接风险：

- current new-Skill scaffold 默认 `writes_files: true`；
- registry record 对缺失 `writes_files` 的 fallback 也是 `True`；
- v0.1 没有冻结 SKILL.md frontmatter capability metadata；
- 因而正文虽写 no repo write，正式 registry/catalog 仍可能错误声明 writable。

v0.2 现在要求最终
`skills/science/communication/project-thread-handoff/SKILL.md`
显式至少具有：

```yaml
name: project-thread-handoff
description: <具体 explicit long-thread handoff trigger boundary；排除 ordinary summary>
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: false
secrets_needed: []
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers
```

请逐项核对 Plan / Goal / Kickoff 是否一致冻结这些 capability values。

特别检查：

1. `writes_files: false` 是否必须显式出现，而不是依赖 default；
2. `requires_network: false` 是否与 Skill 只生成聊天 Prompt 的能力一致；
3. `executes_code: false` 是否冻结；
4. `secrets_needed: []` 是否冻结；
5. `provenance: user-authored` + `metadata.skill-author` 是否符合当前 authoring contract；
6. `allow_implicit_invocation: false` 是否仍然**不**进入普通 SKILL.md frontmatter，只留在
   `agents/openai.yaml -> policy`。

## 3. Focused test 是否真正关闭 generated-identity 风险

v0.2 要求
`tests/test_project_thread_handoff_contract.py`
至少检查：

- name；
- status；
- provenance；
- trusted；
- requires_network；
- writes_files；
- executes_code；
- empty secrets_needed；
- recommended_scope；
- metadata.skill-author；
- SKILL.md 不含 allow_implicit_invocation；
- agents/openai.yaml policy.allow_implicit_invocation=false。

并且 registry 生成后必须核对正式 record：

```text
provenance = user-authored
requires_network = false
writes_files = false
executes_code = false
secrets_needed = []
```

请判断：

- 这是否足以防止 scaffold/default 让错误 metadata 机械 PASS；
- 是否仍有一个明显遗漏的 capability field 会使正式 identity 与 V3 read-only contract 冲突；
- 是否不需要为此新增 schema/script/Gate。

不要把“还能多测几个字段”本身变成 blocker；只有会导致用户可见/正式 registry identity 错误的真实缺口才阻塞。

## 4. 只检查 v0.2 amendment impact

确认 v0.2 没有改变已经接受的：

- standalone Skill；
- exact task / branch / worktree；
- source scope；
- G1/G2/G3；
- target Pro regular Chat normal entry；
- Work/Codex 不替代 regular Chat；
- one final user target-surface acceptance session；
- upload zip contract；
- privacy/redacted evidence；
- final candidate freeze；
- G1/G2 failure route；
- repository bump decision `MINOR`；
- planning baseline `5.0.6 -> 5.1.0`；
- all central plugins `NO_BUMP`；
- root README minimal update；
- skills README explicit check；
- source-first registry/catalog/provenance/generated parity；
- Marketplace topology must not absorb standalone Skill；
- full relevant tests；
- no main merge/tag/release/publish；
- no paid evaluator；
- no account upload authorization；
- ordinary non-force push exact task branch only。

不要重新讨论 version class；上一轮 Critic 已接受它，除非 v0.2 metadata change产生新的直接 version-policy冲突。

## 5. 三份文件 identity

确认：

Plan：
`docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_2_2026-09-21.md`

Goal：
`docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_2.md`

Kickoff：
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_2.md`

全部：

- version = v0.2；
- reviewed package commit =
  `451e8b32c8d3f2521372f591ff3e2d90968f297e`；
- 同 task identity；
- 同 exact branch/worktree；
- 同 G1/G2/G3；
- 同 version decision；
- 同 user-action/privacy/recovery boundary；
- 只增加 PTH-05 metadata freeze/test protection。

## 6. Output

先用自然中文说明：

- PTH-05 是否已经真实关闭；
- frontmatter metadata 与 generated registry identity 是否现在一致可保护；
- v0.2 是否只做了 bounded amendment；
- 是否出现任何由 v0.2 引入的新 direct risk。

然后：

`VERDICT = PASS | REVISE`

`PTH-05 = CLOSED | OPEN`

如果 REVISE：

- 优先只围绕 PTH-05 未关闭部分；
- 新 blocker 必须来自 v0.2 amendment 引入的真实直接风险；
- 每条给 stable finding ID / requirement / direct evidence / causal risk / minimum closure / owner；
- 不换措辞移动终点；
- 按 Critic Role Contract 自动给 `NEXT_HANDOFF=PLANNER` 与完整 COPY TO PLANNER prompt。

如果 PASS：

这是 execution-ready PASS。

由于本 execution review 已正式出现过 REVISE，先按
`CRITIC_ROLE_CONTRACT.md §6.3`
用正常中文给 closure explanation，说明：

- PTH-05 如何关闭；
- 哪些 layer 被修改（仅 execution package metadata contract/test requirement）；
- 哪些 layer 没改（V3 architecture/Gates/version/user flow）；
- PASS 证明什么、不证明什么。

然后输出：

```text
APPROVED_PROPOSAL_PATH=docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md
APPROVED_PLAN_PATH=docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_2_2026-09-21.md
APPROVED_GOAL_PATH=docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_2.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_2.md
APPROVED_COMMIT=451e8b32c8d3f2521372f591ff3e2d90968f297e
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

最后逐字输出 package commit 中
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_2.md`
的 Kickoff 正文。

不得在 PASS 后临场写一个语义不同的新 Kickoff。

PASS 只批准 implementation package，不执行 Skill、不 merge main、不上传 ChatGPT Skill、
不授权 paid call，也不表示 G1/G2 已经通过。
