# Project Instructions Editor — Implementation Kickoff v0.2

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Supersedes: `PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_1.md`

本提示词只有在独立 Critic 对同版 Implementation Plan v0.2 + Goal v0.2 + Kickoff v0.2 给出 `READY_FOR_CODEX=YES` 后，才可由用户直接发送给 Codex。用户实际发送本正文时，才形成当前 implementation authorization。

## Kickoff 正文

执行 `project-instructions-editor--standalone-skill-implementation`，实现已经冻结并通过独立 Critic 的 standalone Skill `project-instructions-editor`。

严格读取并遵守：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`
- `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md`
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

先从 canonical checkout 核实：

- `git rev-parse --show-toplevel`
- origin identity
- `git fetch origin main`

如果 exact worktree 已存在，只有 repo identity 与 exact branch 都匹配才可复用；不匹配则停止，不换另一个路径、branch 或 clone。

### 2. Latest-main preflight

读取 current `origin/main`：

- `AGENTS.md`
- `docs/SKILL_AUTHORING.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/skill-todos/project-instructions-editor.md`
- current standalone Skill baseline/tests
- current `skill-creator` / `agents/openai.yaml` contract

确认 design-freeze PASS 仍在 current history。

无关 docs/evidence drift 可继续。若出现与冻结产品语义、Skill taxonomy/metadata、version/release contract 直接冲突的新事实，停止并返回 Planner/Critic。

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

只有 focused tests 真需要时，才增加最小 public-safe fixture。

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

description 必须清楚表达“编辑长期 ChatGPT Project instructions”的自然 trigger，并排除普通中文润色、generic system/agent prompt、global Custom Instructions 等 near-miss。

不要依赖 scaffold/default 自动补 capability metadata。

### 5. Natural routing

按 current repo schema 生成 `agents/openai.yaml`。

normal entry 必须允许 implicit invocation；`policy.allow_implicit_invocation` 不得为 `false`。

但以下都不能单独算 G1 PASS：

- static `true`;
- description;
- trigger JSON;
- route receipt;
- forced invocation.

必须实际从 exact final candidate 安装后，在 fresh normal Codex session 用自然未点名请求验证。

### 6. 实现冻结语义

必须实现：

- preservation-sensitive / greenfield / explicit reset；
- preservation-sensitive full replacement 的 live baseline 门禁；
- targeted history + honest degradation；
- protected absence；
- current request / live setting / canonical source / budget 分工；
- semantic ownership vs effective enforcement；
- locator lookup-before-action 边界；
- bounded edit 默认；
- full rewrite 的真实触发边界；
- no-op；
- exact identifier protection；
- authorization / safety / evidence-strength / uncertainty preservation；
- proportional user delivery。

不要将真实失败样本变成：

- banned-word table；
- 英文比例；
- 固定字符比例；
- 固定段落数；
- 固定标题数；
- 固定公式数；
- keyword scorer。

### 7. 先完成全部 candidate-owned 内容

在任何 G1/G2/G3/G4 packet 之前，先完成并稳定以下 candidate-owned content：

1. Skill source/reference/evals/assets；
2. focused test / standalone baseline declarations；
3. generated registry/catalog/provenance/runtime identity；
4. README release candidate；
5. VERSION release candidate；
6. CHANGELOG release candidate；
7. current repo 要求的其他 release-candidate parity content。

完成 source 后使用现有 generator，禁止手改 generated source of truth。

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

普通 implementation defect 在这里修到稳定。

这些 deterministic checks 是 candidate preflight，不是产品 Gate PASS。

### 8. Version / README candidate

开始 release-candidate metadata 前重新读取 `origin/main:VERSION`。

当前已批准 planning decision：

```text
Repository bump decision: MINOR
expected if main remains 5.4.0: 5.4.0 -> 5.5.0
all central plugins: NO_BUMP
project-instructions-editor: initial standalone version 0.1
```

如果 current `origin/main` 已不是 `5.4.0`：

```text
VERSION_DRIFT
```

停止 version/release metadata部分并返回 Planner；不要自行猜新 target version。

若无 drift，准备但不发布：

- VERSION/parity sources；
- root CHANGELOG；
- README standalone Skill card；
- standalone baseline；
- generated registry/catalog/provenance；
- 必要 generated icon/audit artifacts。

不要修改 central Plugin version/changelog，不新增 profile。

### 9. Freeze exact candidate commit C

只有当全部 candidate-owned content 完成且 deterministic preflight稳定后，创建 exact candidate commit：

```text
FINAL_CANDIDATE_COMMIT=C
```

`C` 必须包含全部 candidate-owned content。

从这一刻开始，直到独立 Reviewer decision，不得修改：

- Skill source/reference/evals/assets；
- generated registry/catalog/provenance/runtime identity；
- README/VERSION/CHANGELOG candidate；
- standalone baseline/test contract；
- 其他 candidate-owned release content。

### 10. 从 exact C 安装并运行 G1–G3

从 `FINAL_CANDIDATE_COMMIT=C` 安装 standalone Skill。

必须确保实际 installed runtime identity 可回指 `C`，然后在 fresh normal Codex session 运行。

#### G1 — Normal entry / routing

Executor owns G1 PASS。

证明：

- natural unnamed Project-instruction request 触发；
- near-miss 保持 frozen owner；
- installed runtime 确实来自 `C`。

#### G2 — Core Project editing semantics

Executor owns G2 PASS。

覆盖：

- three edit modes；
- live/history/source/budget；
- missing-input degradation；
- ownership/enforcement；
- locator；
- protected absence；
- bounded/full/no-op。

所有 outputs 必须由 `C` runtime 产生。

#### G3 — Fidelity / authority / should-not-change

Executor owns G3 PASS。

直接对照 baseline/source/output 检查：

- mandatory/optional；
- authorization；
- safety/permission；
- evidence strength；
- uncertainty；
- exact identifiers；
- explicit deletion/correction；
- unrelated scope；
- near-miss owner。

所有 outputs 必须由 `C` runtime 产生。

如果 G1–G3 暴露 candidate-owned defect，不能在 `C` 上继续改 source 后沿用旧 Gate PASS。必须：

1. 修复 candidate-owned content；
2. 创建新 candidate `C2`；
3. 将旧相关 evidence 视为 stale；
4. 按 blast radius 重跑相应 Gate；
5. final handoff 只绑定最新 candidate。

不得跨 candidate 拼 PASS。

### 11. G4 只准备完整 packet，不由 Executor 判 PASS

四个 Gate taxonomy 不变，不新增 G5。

Executor 对 G4 只负责：

- 从 exact `C` 运行代表性完整任务；
- 冻结完整 input/source/output；
- long/multi-scope representative case；
- fixed source/ref；
- risk-matched fresh public-safe case；
- 完整 user artifact；
- 必要 self-check。

写：

```text
results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_PACKET.md
```

self-check 必须明确：

```text
NON_INDEPENDENT_SELF_CHECK
NOT_G4_PASS
```

Executor 对 G4 的最高状态：

```text
G4_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor 不得写：

```text
G4=PASS
IMPLEMENTATION_OVERALL=PASS
```

后续独立 Reviewer 才读取完整 final Skill source、candidate identity、G1–G3 evidence、G4 packet、完整 user artifact、README/VERSION/CHANGELOG/package identity，并写：

```text
G4=PASS|REVISE
IMPLEMENTATION_OVERALL=PASS|REVISE
```

Reviewer-owned review 文件：

```text
results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_REVIEW.md
```

### 12. Portable package 必须来自 C

生成：

`private/exports/project-instructions-editor-v0.1.zip`

必须从 exact candidate commit `C` 的 runtime Skill tree 生成，不从模糊 current worktree 状态打包。

可以使用 `git archive`、只读 materialization 或等价 deterministic route。

zip 只含 Skill runtime directory，不含 tests/results/design docs。

MANIFEST 必须记录：

```text
FINAL_CANDIDATE_COMMIT=C
zip SHA-256
archive file list
runtime Skill-tree identity/hash
generation method
```

### 13. Evidence-only commits

`C` 之后允许提交的 tracked 文件只能位于：

```text
results/project-instructions-editor--standalone-skill-implementation/**
```

Executor-owned：

```text
RESULT.md
MANIFEST.md
G1_NORMAL_ENTRY.md
G2_CORE_SEMANTICS.md
G3_FIDELITY.md
G4_COMPLETE_TASK_PACKET.md
```

完成 evidence 后形成：

```text
EVIDENCE_HEAD=E
```

必须保存可复核 proof：

```text
git diff --name-status C..E
```

或等价 evidence，证明 `C..E` 只有上述 evidence/result/handoff 路径。

如果 `C..E` 出现任何 candidate-owned file：

- 不得声称 candidate immutable；
- 当前相关 Gate evidence 不得用于 final PASS；
- 修复后生成新 candidate并按 blast radius重跑。

### 14. ChatGPT / Codex surface boundary

required production normal-entry evidence 继续使用：

```text
AI_Skills / Codex standalone install
+ fresh normal Codex session
```

保持 OpenAI Skill directory structure compatibility。

不要声称当前用户 ChatGPT Pro regular Chat 能直接安装/auto-use standalone Skill，不创建 Plugin wrapper，不要求用户做 ChatGPT account upload。

### 15. Evidence / privacy

使用 repo 已保存的真实历史 evidence 与 public-safe equivalents。

不得 commit 私有 ChatGPT Project threads/settings。

不允许 paid API/model review。

### 16. Push and stop

当且仅当以下成立：

```text
FINAL_CANDIDATE_COMMIT=C
G1=PASS
G2=PASS
G3=PASS
G4_READY_FOR_INDEPENDENT_REVIEW=YES
EVIDENCE_HEAD=E
```

且：

- portable zip来自 C；
- `C..E` candidate-owned diff为空；
- exact branch已 ordinary non-force push；
- remote tip已验证；
- Reviewer能访问完整 evidence；

才允许报告：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

同时明确给 Reviewer：

```text
FINAL_CANDIDATE_COMMIT=C
EVIDENCE_HEAD=E
```

不要 merge `main`；
不要 advance `release`；
不要 tag；
不要 GitHub Release；
不要 publish；
不要声明 `5.5.0` 已发布。

### 17. Authorization boundary

本消息授权：

- exact branch/worktree；
- frozen source/docs/tests/generated/release-candidate/results edits；
- deterministic tests；
- task-local standalone install/fresh Codex smoke；
- public-safe regression；
- portable zip；
- task-owned commits；
- ordinary non-force push exact branch。

不授权：

- main merge；
- release ref/tag/GitHub Release；
- paid API/model reviewer；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin source changes；
- Bridge Kit changes；
- force push / remote remap / destructive Git；
- watcher/daemon/database/ledger/state machine。

如果任何一步需要扩大这些边界，停止并返回 Planner。
