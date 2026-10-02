# Project Instructions Editor — Implementation Kickoff v0.1

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW

本提示词只有在独立 Critic 对同版 Implementation Plan + Goal + Kickoff 给出 `READY_FOR_CODEX=YES` 后，才可由用户直接发送给 Codex。用户实际发送时，才形成当前 implementation authorization。

## Kickoff 正文

执行 `project-instructions-editor--standalone-skill-implementation`，实现已经冻结并通过独立 Critic 的 standalone Skill `project-instructions-editor`。

严格读取并遵守：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md`
- `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md`

不要重新设计产品合同。

### 1. Exact branch / worktree authorization

Repository：

`YuukiAS/AI_Skills_Collection`

Exact branch：

`work/project-instructions-editor--standalone-skill-implementation`

Exact task-owned worktree：

`../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation`

我明确授权本任务创建/复用上面唯一 exact branch/worktree，并在该分支进行 task-owned edits、commits 与 ordinary non-force push。

先从 canonical checkout 核实 `git rev-parse --show-toplevel`、origin identity，并 `git fetch origin main`。

如果 exact worktree 已存在，只有 repo identity 与 exact branch 都匹配才复用；不匹配就停止，不换另一个路径/branch/clone。

### 2. Latest-main preflight

读取 current `origin/main` 的：

- `AGENTS.md`
- `docs/SKILL_AUTHORING.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/skill-todos/project-instructions-editor.md`
- 当前 standalone Skill baseline/tests
- 当前 `skill-creator` / `agents/openai.yaml` contract

确认 design-freeze PASS 仍在 current history。

无关 docs/evidence drift 可以继续；若出现与冻结产品语义、Skill taxonomy/metadata、version/release contract 直接冲突的新事实，停止并返回 Planner/Critic。

### 3. 只实现冻结范围

Canonical source：

```text
skills/core/codex-system/project-instructions-editor/
├── SKILL.md
├── agents/openai.yaml
├── references/editor-contract.md
├── evals/trigger_queries.json
└── assets/app-facing.svg
```

新增：

`tests/test_project_instructions_editor_contract.py`

更新：

`tests/test_standalone_skill_baselines.py`

只有 focused tests 确实需要时，才增加最小 public-safe fixture。

不要创建 runtime scripts、Plugin、profile、MCP、database、ledger、watcher、daemon、history state machine 或第二套 Project control plane。

### 4. Frontmatter capability

最终 Skill 必须显式保持：

```yaml
name: project-instructions-editor
status: active
version: "0.1"
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: false
secrets_needed: []
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
metadata:
  skill-author: AI Skills Collection maintainers
```

description 必须清楚表达“编辑长期 ChatGPT Project instructions”的自然 trigger，同时排除普通中文润色、generic system/agent prompt、global Custom Instructions 等 near-miss。

不要依赖 scaffold/default 自动补 capability metadata。

### 5. Natural routing

按 current repo schema 生成 `agents/openai.yaml`。

normal entry 必须允许 implicit invocation；`policy.allow_implicit_invocation` 不得是 `false`。

但是静态 `true`、description、trigger JSON、route receipt 都不能冒充 G1 PASS。必须做实际安装后的 fresh normal invocation。

### 6. 实现冻结语义

必须实现：

- preservation-sensitive / greenfield / explicit reset；
- preservation-sensitive full replacement 的 live baseline 门禁；
- targeted history + honest degradation；
- protected absence；
- canonical source / live setting / current request / budget 分工；
- semantic ownership vs effective enforcement；
- locator lookup-before-action 边界；
- bounded edit 默认；
- full rewrite 真实触发边界；
- no-op；
- exact identifier protection；
- authorization/safety/evidence-strength/uncertainty preservation；
- proportional user delivery。

不要将真实失败样本变成禁词表、英文字数阈值、固定段落/标题/公式数或机械评分器。

### 7. G1–G4

严格按 Implementation Plan 的四个 Gate family 验证同一 final candidate：

- G1：normal entry / routing boundary；
- G2：core Project editing semantics；
- G3：fidelity / authority / should-not-change；
- G4：representative complete task + qualitative final artifact。

A–L 是 regression/task-family bank，不是 12 个 Gate。

G4 必须让独立 Reviewer 后续能看到完整输入/source 和完整输出；字符数、diff、关键词、route receipt、tests 不能替代。

### 8. ChatGPT surface boundary

当前正式 required normal-entry evidence 使用 AI_Skills/Codex standalone install + fresh Codex session。

保持 Skill 包为 OpenAI Skill 目录结构，但不要声称当前用户的 ChatGPT Pro regular Chat 可以直接安装/自动调用 standalone Skill，也不要因此创建 Plugin wrapper。

不要求用户做 ChatGPT account upload。

### 9. Source-first validation

完成 source 后用现有 generator 刷新 registry/catalog/provenance 等 generated outputs，禁止手改 generated source of truth。

至少运行：

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests
```

并完成 task-local standalone install + fresh-session normal-entry验证。

普通实现/测试问题在冻结 scope 内自行修完再继续，不把半成品交给用户。

### 10. Version / README / candidate closure

开始 release-candidate metadata 前重新读取 `origin/main:VERSION`。

当前 planning decision：

```text
Repository bump decision: MINOR
expected if main remains 5.4.0: 5.4.0 -> 5.5.0
all central plugins: NO_BUMP
project-instructions-editor: initial standalone version 0.1
```

若 main 已不是 `5.4.0`：

```text
VERSION_DRIFT
```

停止 version/release metadata 部分并返回 Planner；不要自行猜 target version。

若无 drift，准备但不发布 release candidate：

- VERSION/parity sources；
- root CHANGELOG；
- README standalone Skill card；
- standalone baseline tests；
- generated registry/catalog/provenance；
- 必要 generated icon/audit artifacts。

不要修改 central Plugin version/changelog，不新增 profile。

### 11. Evidence / portable package

写：

```text
results/project-instructions-editor--standalone-skill-implementation/
  RESULT.md
  MANIFEST.md
  G1_NORMAL_ENTRY.md
  G2_CORE_SEMANTICS.md
  G3_FIDELITY.md
  G4_COMPLETE_TASK_REVIEW.md
```

生成：

`private/exports/project-instructions-editor-v0.1.zip`

zip 只含 Skill runtime 目录。记录 SHA-256 与 file list；不要把 tests/results/design docs 放入包内。

不得把私有 ChatGPT Project threads/settings 提交到公开 repo。

### 12. Push and stop

完成所有实现、生成、测试、G1–G4、release-candidate metadata、package 和 evidence 后：

- freeze exact final candidate；
- commit；
- ordinary non-force push exact task branch；
- 核对 remote branch tip；
- 不 merge `main`；
- 不 advance `release`；
- 不 tag / GitHub Release / publish。

停止在：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

然后给出完整 independent Reviewer/Critic handoff，包括 final commit、Gate evidence 路径和完整产物定位。

### 13. Authorization boundary

本消息授权：

- exact branch/worktree；
- 冻结 source/docs/tests/generated/release-candidate/results 范围；
- deterministic tests；
- task-local standalone install/fresh Codex smoke；
- public-safe regression；
- portable zip；
- task-owned commit；
- ordinary non-force push exact branch。

不授权：

- merge main；
- release ref/tag/GitHub Release；
- paid API/model reviewer；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin source changes；
- Bridge Kit changes；
- force push / remote remap / destructive Git；
- watcher/daemon/database/ledger/state machine。

如果任何一步需要扩大这些边界，停止并返回 Planner。
