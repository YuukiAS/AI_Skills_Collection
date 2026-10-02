# Critic Prompt — Project Instructions Editor Implementation Package v0.2

你现在负责对 `project-instructions-editor` standalone Skill 的 implementation execution package 做独立 Critic 审查。

这是 execution-ready review，不是重新设计产品。最终产品/架构 design freeze 已 PASS。

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
execution-ready implementation package review

approved design freeze:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md

design-freeze Critic PASS:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md

design-freeze review commit:
bf9add585924e93ab8844bb59a366f1cd4f837d6

implementation Plan:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md

canonical Goal:
docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md

Kickoff Draft:
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_1.md

implementation package commit:
eece8a8bd89c84559a1d1b8d079fef4b5e4bb9ae

tracking:
Issue #93

user authorization:
implementation phase explicitly opened

READY_FOR_CODEX=NO
```

如果 package commit 之后 `main` 只有无关 docs/evidence drift，读取最新真实 main，不要回退。若出现直接改变 Skill taxonomy、version policy、normal-entry surface 或 frozen product contract 的新事实，再按真实影响处理。

## 必须读取

实际读取 latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/SKILL_AUTHORING.md`
- `docs/skill-todos/project-instructions-editor.md`

主要审查：

- Implementation Plan v0.1
- Goal v0.1
- Kickoff Draft v0.1

只按需要复核 approved design freeze，不重新打开已批准产品架构。

还应按需读取当前 standalone Skill 先例、`skill-creator`、standalone baseline tests、current `VERSION` / README / CHANGELOG。

## 审查目标

只有当同版 Plan + Goal + Kickoff 都足够让 Codex 在冻结范围内直接实现，并且授权边界、Gate、恢复和停止条件都清楚时，才能：

```text
READY_FOR_CODEX=YES
```

否则 REVISE。

## 1. Source placement / taxonomy

Planner 冻结：

```text
skills/core/codex-system/project-instructions-editor/
```

理由是它是跨 Project、跨领域的 system-support standalone Skill，不属于 writing 或 research communication，也不值得新建 taxonomy。

请检查这是否符合 current repo taxonomy，是否有更成熟且明显更正确的现有路径。

只有真实 taxonomy/trigger/install 风险才阻塞，不要为了目录审美重开产品设计。

## 2. Skill structure / capability metadata

计划 source：

```text
SKILL.md
agents/openai.yaml
references/editor-contract.md
evals/trigger_queries.json
assets/app-facing.svg
```

无 runtime script。

frontmatter 冻结：

```text
version = 0.1
provenance = user-authored
trusted = false
requires_network = false
writes_files = false
executes_code = false
secrets_needed = []
recommended_scope = global
```

检查：

- 与 frozen product 是否一致；
- `requires_network=false` + unavailable-source degradation 是否诚实；
- `writes_files=false` 是否与“输出 setting candidate，而非自动改 Project UI/repo”一致；
- global scope 是否符合跨 Project reusable capability；
- reference split 是否有助于保持 SKILL.md 简洁，而不是过重。

## 3. Natural normal entry

设计要求普通用户自然请求触发，不点名 Skill。

Plan 要求 current schema 下允许 implicit invocation，同时明确：

- static `allow_implicit_invocation=true` 不能单独证明能力；
- description + trigger eval 不能替代 fresh installed invocation；
- near-miss owner 必须保持。

检查这是否与 current Skill authoring/runtime contract一致。

特别检查它是否会变成过宽的“所有 instruction/prompt 请求都触发”，以及 generic system/agent prompt、global Custom Instructions、普通文字润色是否被充分排除。

## 4. Implementation scope / anti-overengineering

检查 v0.1 是否保持最小：

- instruction/reference Skill；
- 无 script/database/ledger/watcher/state machine；
- helper 如果未来确实必需必须回 Planner，而不是 Executor自行加 runtime capability；
- 不创建 Plugin/profile。

若当前 frozen capability 明显必须依赖 deterministic helper 才能真实工作，请给直接因果证据；不要仅因“更稳”新增代码层。

## 5. Four Capability Gates

### G1 Normal entry / routing

必须是实际 installed final candidate + fresh normal Codex invocation，不能 forced route 冒充。

### G2 Core editing semantics

必须覆盖三 edit modes、输入降级、ownership/enforcement、locator、protected absence、budget、bounded/full/no-op。

### G3 Fidelity / authority / should-not-change

必须直接保护 mandatory/optional、authorization、安全、evidence strength、uncertainty、exact identifiers、user deletion/correction、unrelated scope 和 near-miss owner。

### G4 Representative complete task + qualitative final artifact

必须在完整代表性 Project setting 上评同一个 final candidate，Reviewer 读取完整 inputs/source/output，并包含风险匹配 fresh generalization。

检查：

- 四 Gate 是否仍与 design freeze 完全一致；
- 是否有重复或漏掉的能力；
- Gate 4 是否合理承载 complete/long + final candidate + qualitative/fresh；
- A–L 是否仍是 regression bank；
- 是否有机械 tests/route receipts 冒充产品能力的漏洞。

不要机械增加 Gate。

## 6. Representative evidence / privacy

Plan 优先使用 repo 已保存的真实 historical Project evidence + public-safe equivalents。

不要求用户提供私有 live Project setting，不把私有 thread/settings commit 到 repo。

检查这样是否仍足以证明 frozen product claims；若某 capability 必须通过 private data 才能验证，请说明为什么 public-safe evidence 不能证明，并给最小关闭条件。

## 7. ChatGPT / Codex surface boundary

当前 OpenAI 官方文档说明 ChatGPT Skills 的直接创建/安装/自动使用取决于 eligible workspace/product surface；Plan 因此把当前 required normal-entry release evidence限定为 AI_Skills/Codex standalone install + fresh session，不把当前用户 ChatGPT Pro upload 当 required Gate，也不创建 Plugin wrapper。

请独立核查最新官方事实，并判断：

- 这是否是诚实且最小的 v0.1 release claim；
- 是否违背冻结的“编辑 ChatGPT Project instructions”产品语义；
- 是否应该把 Skill package 的 ChatGPT workspace兼容性只保留为结构兼容声明，而非未经验证的 runtime claim。

如果官方事实已经变化，引用最新证据并给最小修订。

## 8. Tests / generated parity

检查 Plan 的 mechanical validation 是否覆盖：

- source frontmatter；
- agents metadata；
- trigger eval shape；
- registry/catalog/provenance；
- standalone baseline；
- central Marketplace topology 不变；
- full repository tests；
- task-local install smoke。

这些只能是 mechanical evidence，不得替代 G1–G4。

## 9. Version / release candidate

当前 main planning baseline：

`VERSION = 5.4.0`

Planner proposal：

```text
Repository bump decision: MINOR
5.4.0 -> 5.5.0 if main still 5.4.0
project-instructions-editor = standalone 0.1
all central plugins = NO_BUMP
```

理由：collection 获得新的正式可安装 standalone user capability；已有 `project-thread-handoff` 新 standalone capability 先例曾触发 repository MINOR。

检查 version policy 是否直接支持该判断。

如果不支持，给出明确 policy evidence；不要因为“新文件不一定大”或“standalone不是 plugin”做感觉判断。

Plan 已设置 `VERSION_DRIFT`：若 kickoff 时 main 不再是 5.4.0，Executor停止 version/release metadata部分返回 Planner，不自行猜新版本。

## 10. README / package / release boundary

Plan 允许准备：

- README standalone card；
- VERSION/CHANGELOG release candidate；
- generated registry/catalog/provenance；
- portable zip；
- evidence。

但 Executor stop point 是：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

禁止：

- merge main；
- advance release；
- tag/GitHub Release/publish；
- 声称 5.5.0 已发布。

检查这个边界是否足够避免“实现自审后直接发布”。

## 11. Exact branch/worktree / authorization

计划 exact identity：

```text
task_key = project-instructions-editor--standalone-skill-implementation
branch = work/project-instructions-editor--standalone-skill-implementation
worktree = ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation
```

本任务明确采用人工 Planner -> Executor -> 独立 Reviewer，不创建 watcher。

Kickoff 只有用户实际发送后才授权：

- exact branch/worktree；
- frozen source/docs/tests/generated/release-candidate/results；
- local tests；
- task-local install/fresh Codex smoke；
- public-safe regression；
- zip；
- ordinary commit / non-force branch push。

不授权 main merge、release、paid API、private data external transmission、live ChatGPT account mutation、central Plugin source、Bridge write、destructive Git。

检查权限边界是否完整且不过宽。

## 12. Positive completion / stop condition

Executor 的最高 claim：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

不是：

```text
RELEASED
PRODUCTION_READY
5.5.0_PUBLISHED
```

检查 Goal 是否把真正产品行为与 tests/CI/file-existence 区分开，并且 independent Reviewer 能拿到完整 source/evidence/artifact。

## 13. Maintenance state

Issue #93 当前应继续：

```text
state=open
maintenance-track
kind:new-capability
scope:standalone-skill
area:standalone-skill
```

Project 目标：

```text
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md
```

如果当前 surface 无 GitHub Project mutation，输出 exact pending mutation，不要求用户手工拖卡片。

Issue reader-facing copy 在真实调用 Clear Writing 前不得实质改写；无入口时：

```text
CLEAR_WRITING_UNAVAILABLE
```

## 14. PASS / REVISE

如果同版 Plan + Goal + Kickoff 都满足 execution-ready：

```text
CRITIC_RESULT=PASS
APPROVED_PROPOSAL_PATH=docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md
APPROVED_GOAL_PATH=docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_1.md
APPROVED_COMMIT=eece8a8bd89c84559a1d1b8d079fef4b5e4bb9ae
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

并按照 Critic Role Contract **逐字输出 approved Kickoff 正文**，不要 PASS 后重新设计另一份 prompt。

如果 Kickoff 的范围、Gate、版本、权限、恢复或 stop point 需要实质修改，必须：

```text
CRITIC_RESULT=REVISE
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
```

每个 blocker 提供稳定编号、对应要求、直接证据、因果风险和最小关闭条件。

不要用“还可以更完整”或实现期正常代码选择阻塞。
