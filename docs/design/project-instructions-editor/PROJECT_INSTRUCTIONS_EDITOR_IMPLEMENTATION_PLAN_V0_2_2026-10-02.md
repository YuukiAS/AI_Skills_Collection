# Project Instructions Editor — Implementation Plan v0.2

Date: 2026-10-02  
Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Task key: `project-instructions-editor--standalone-skill-implementation`  
Supersedes: `PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md`  
Approved architecture: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`  
Approved design freeze: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`  
Design-freeze Critic PASS: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md`  
Design-freeze review commit: `bf9add585924e93ab8844bb59a366f1cd4f837d6`  
Prior execution review: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-02.md`  
Prior execution review commit: `ee852eff9278fda18952f687dda12bd787f01f72`  
Canonical Goal: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md`  
Kickoff Draft: `docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md`  
Tracking: #93

```text
USER_AUTHORIZED_IMPLEMENTATION_PHASE=YES
READY_FOR_CODEX=NO
```

本 Plan 是 v0.1 的完整替代版本，只关闭 execution-contract blockers E1/E2。已由 v0.1 Critic 明确 PASS 的 source placement、metadata、normal entry、四个 Gate family、ChatGPT/Codex surface 边界、版本判断、授权边界均保持不变。

只有独立 Critic 对本 Plan、同版 Goal 和 Kickoff 给出 execution-ready PASS，且用户随后实际发送 approved Kickoff，才允许 Codex 开始 implementation。

## 0. Planner 对 E1/E2 的正式回应

### E1 — ACCEPT

v0.1 对 G4 的 owner 写法确实自相矛盾：一方面要求独立 Reviewer 才能给完整产物的定性 PASS，另一方面又让 Executor 在交 Reviewer 前“完成 G1–G4”。

v0.2 统一为：

- Executor owns:
  - final candidate implementation；
  - G1 PASS；
  - G2 PASS；
  - G3 PASS；
  - G4 所需完整代表性 input/source/output packet；
  - 非独立 self-check（仅诊断，不是 G4 PASS）；
- Executor 对 G4 的最大状态：
  `G4_READY_FOR_INDEPENDENT_REVIEW=YES`；
- Executor 达到上述状态即可：
  `FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES`；
- 独立 Reviewer owns:
  - 完整 final Skill source；
  - exact candidate identity；
  - G1–G3 evidence；
  - G4 full packet；
  - 完整 user artifact；
  - README/VERSION/CHANGELOG/package identity；
  - `G4=PASS|REVISE`；
  - implementation overall `PASS|REVISE`。

四个 Gate taxonomy 不变，不新增 G5。

v0.2 使用 Executor-owned `G4_COMPLETE_TASK_PACKET.md`，Reviewer 后续写 `G4_COMPLETE_TASK_REVIEW.md`，避免文件名和 owner 混淆。

### E2 — ACCEPT

v0.1 的“先跑 Gate，再 freeze/commit final candidate”不能证明所有证据绑定同一候选。

v0.2 冻结无循环顺序：

1. 完成全部 candidate-owned 内容；
2. deterministic preflight/tests 修到稳定；
3. 创建 exact candidate commit `C`；
4. 从 `C` 安装 standalone Skill；
5. 只在 `C` 上运行 G1–G3，并生成 G4 packet；
6. portable zip 必须由 `C` 的 runtime Skill tree 生成；
7. `C` 之后只能提交 evidence-only 文件；
8. Reviewer handoff 明确：
   - `FINAL_CANDIDATE_COMMIT=C`
   - `EVIDENCE_HEAD=E`
9. 必须证明 `C..E` 没有 candidate-owned 内容变化；
10. 若 `C` 后 candidate-owned 内容发生变化：
    - 旧 Gate evidence 失效；
    - 创建新 candidate commit `C2`；
    - 按 blast radius 重跑相应 Gate；
    - 不得跨 candidate 拼 PASS。

## 1. 实现目标

实现新的 standalone Skill：`project-instructions-editor`。

普通用户在已安装该 Skill 的真实正常入口中，用自然语言要求创建、修改、压缩、同步或重构长期 ChatGPT Project instructions 时，模型按冻结合同：

- 选择 preservation-sensitive / greenfield / explicit reset；
- 根据 live setting、相关历史、canonical source、字符预算做语义 placement；
- 区分 semantic ownership 与 effective enforcement；
- 默认 bounded edit；
- 保护 protected absence、权限/安全/证据强度和 exact identifiers；
- 缺输入时诚实降级；
- 支持 no-op；
- 输出比例化、可审查、必要时可直接复制的 setting。

不得退化成中文润色器、禁词表、字符评分器或 generic prompt optimizer。

## 2. Exact execution identity

```text
task_key = project-instructions-editor--standalone-skill-implementation
branch = work/project-instructions-editor--standalone-skill-implementation
worktree = ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation
```

worktree 以 verified canonical `AI_Skills_Collection` checkout root 的父目录为基准，basename 必须精确匹配。

本任务采用人工 Planner -> Codex Executor -> 独立 Critic/Reviewer，不启用 watcher、daemon 或自动任务链。

用户实际发送 approved Kickoff 后，才授权创建/复用上述 exact branch/worktree，并授权该分支普通 task-owned commit 与 ordinary non-force push。

## 3. Latest-main preflight

Executor 开始前必须：

1. `git fetch origin main`；
2. 核实 canonical repo、origin、`origin/main`；
3. 读取 current：
   - `AGENTS.md`
   - `docs/SKILL_AUTHORING.md`
   - `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
   - `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
   - `docs/skill-todos/project-instructions-editor.md`
   - current standalone baseline/tests
   - current `skill-creator` / `agents/openai.yaml` contract；
4. 核实 design-freeze PASS 仍在 history；
5. 核实 current `origin/main:VERSION`。

无关 docs/evidence drift 可以继续。

如果出现直接改变冻结产品合同、Skill metadata/taxonomy、版本策略或正常入口语义的新事实，停止并返回 Planner/Critic；Executor 不得自行重设计。

## 4. Source placement 与最小 Skill 结构

### 4.1 Canonical path

冻结路径：

```text
skills/core/codex-system/project-instructions-editor/
```

理由保持 v0.1 Critic PASS：

- 跨 Project、跨领域；
- 属于 system-support standalone Skill；
- 不属于 writing domain；
- 不属于 research communication；
- 不为一个 Skill 新增 taxonomy/domain。

### 4.2 Required files

默认新增：

```text
skills/core/codex-system/project-instructions-editor/
├── SKILL.md
├── agents/openai.yaml
├── references/editor-contract.md
├── evals/trigger_queries.json
└── assets/app-facing.svg
```

同时：

```text
tests/test_project_instructions_editor_contract.py
tests/test_standalone_skill_baselines.py
```

只有 focused tests 真正需要时才新增最小：

```text
tests/fixtures/project_instructions_editor/
```

不新增 `scripts/`。v0.1/v0.2 均为 instruction/reference Skill。

如果实现证明 deterministic helper 是冻结能力成立的必要条件，停止并返回 Planner/Critic；Executor 不自行扩大 runtime capability。

## 5. Skill metadata contract

最终 `SKILL.md` frontmatter 至少：

```yaml
name: project-instructions-editor
description: <具体说明何时编辑长期 ChatGPT Project instructions，并排除普通润色、generic prompt、global Custom Instructions 等 near-miss>
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

允许 current repo 标准字段，例如 `last_reviewed`、`profile_tags`。

冻结解释：

- `requires_network=false`：Skill 自身没有硬网络依赖；history/source 不可达时按合同降级；
- `writes_files=false`：产品输出 setting candidate/advice，不自动修改 Project UI/repo；
- `executes_code=false`：核心判断不依赖执行代码；
- `recommended_scope=global`：跨 Project 可复用。

不得依赖 scaffold/default 自动补 capability metadata。

## 6. agents/openai.yaml 与 normal entry

按 current repo 的 `skill-creator` / generation contract 生成合法 interface metadata。

冻结：

- natural normal entry 必须允许 implicit invocation；
- current schema 下 `policy.allow_implicit_invocation` 不得为 `false`；
- description 必须同时覆盖 positive trigger 与 near-miss；
- 用户不需要点名 Skill；
- `allow_implicit_invocation=true`、description、trigger JSON、route receipt 都不能单独证明 G1。

## 7. SKILL.md 与 reference 分工

### 7.1 SKILL.md

保持精炼，只放：

- trigger/near-miss；
- 三 edit modes；
- 输入与降级；
- 核心 reasoning sequence；
- bounded edit 默认；
- protected absence；
- locator 前置约束；
- no-op；
- output contract；
- 何时读取 `references/editor-contract.md`。

不得复制设计历史、Critic review 或大量回归故事。

### 7.2 references/editor-contract.md

承载稳定详细合同：

- preservation-sensitive / greenfield / explicit reset；
- live/history/canonical source/budget；
- semantic ownership vs effective enforcement；
- locator substitution；
- protected absence；
- bounded/full rewrite；
- semantic invariants；
- proportional delivery；
- A–L regression bank 的抽象 task families / should-not-change。

reference 不是数据库、ledger 或状态文件。

## 8. Trigger eval contract

`evals/trigger_queries.json` 覆盖自然正例、反例、near-miss，不固定机械数量。

正例至少跨：

- bounded existing-setting edit；
- finite-budget compression；
- canonical locator/sync；
- greenfield；
- explicit reset/full rewrite。

near-miss 至少覆盖：

- 普通中文润色；
- 普通写作保真；
- scientific/technical structural rewrite；
- AI_Skills_Collection repo maintenance；
- complex workflow/control；
- generic system/agent prompt；
- global Custom Instructions。

不得通过“请使用 project-instructions-editor”冒充 normal entry。

## 9. Candidate-owned 内容

E2 为了绑定 exact final candidate，v0.2 明确 candidate-owned surface。

在 candidate commit `C` 形成前必须完成并稳定：

### 9.1 Runtime source

```text
skills/core/codex-system/project-instructions-editor/**
```

### 9.2 Product tests / baseline declarations

```text
tests/test_project_instructions_editor_contract.py
tests/test_standalone_skill_baselines.py
tests/fixtures/project_instructions_editor/**   # only if actually added
```

### 9.3 Generated identity / catalog / provenance

按现有 generator 实际产生的相关文件，包括：

- `registry.json`
- `docs/SKILL_CATALOG.md`
- 对应 domain/catalog generated page；
- `docs/SKILL_PROVENANCE.md`
- `docs/skill_provenance_audit.json`
- icon/contact-sheet 或其他 current standalone generated identity artifacts（若 generator/测试要求）。

### 9.4 Release-candidate metadata

```text
VERSION
README.md
CHANGELOG.md
```

以及任何当前 repo 版本 parity source，但**不**修改中央 Plugin version/changelog。

以上统称 `CANDIDATE_OWNED_CONTENT`。

## 10. Deterministic preflight 与 candidate freeze

在形成 `C` 之前：

1. 完成 source；
2. source-first 生成 registry/catalog/provenance；
3. 完成 README/VERSION/CHANGELOG candidate；
4. 完成 tests/baseline；
5. 运行 deterministic validation；
6. 修复所有 implementation defect；
7. 确认 candidate-owned tree 稳定。

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

这些 preflight 只能证明机械/实现稳定性，不是 G1–G4 产品 PASS。

preflight 稳定后：

```text
create exact candidate commit C
FINAL_CANDIDATE_COMMIT=C
```

`C` 必须包含全部 `CANDIDATE_OWNED_CONTENT`。

## 11. Candidate commit C 后的禁止变化

`C` 形成后，直到独立 Reviewer decision：

不得修改：

- Skill source/reference/evals/assets；
- generated registry/catalog/provenance/runtime identity；
- README/VERSION/CHANGELOG release candidate；
- standalone baseline/test contract；
- 任何其他 candidate-owned release content。

`C` 后允许新增/修改的 tracked 文件只能位于：

```text
results/project-instructions-editor--standalone-skill-implementation/**
```

且属于：

- Gate evidence；
- RESULT；
- MANIFEST；
- review handoff；
- Reviewer result/final report（由对应 owner 后续写）。

portable zip 位于 `private/exports/`，不作为 candidate-owned tracked source，也不得反向修改 runtime source。

如果 `C` 后 candidate-owned 内容变化：

1. 旧 Gate evidence 标记 stale / 不可用于 final PASS；
2. 修复 candidate-owned 内容；
3. 创建新 exact candidate commit `C2`；
4. 按 blast radius 重跑相应 Gate；
5. 所有 final PASS evidence 必须绑定最新 candidate；
6. 不跨 `C` / `C2` 拼 PASS。

## 12. Capability Gate Matrix

A–L 仍是 regression/task-family bank，不机械变 12 个 Gate。

### G1 — Normal entry / routing boundary

**Owner before independent review**：Executor。

**Claim**：final candidate 从真实安装后的 fresh normal Codex session 被自然、未点名 Skill 的 Project-instruction 请求触发；near-miss 保持正确 owner。

**Evidence**：

- 从 exact `C` 安装；
- fresh session；
- natural unnamed positive requests；
- near-miss outputs；
- installed identity 能回指 `C`。

**Failure**：

- 只能 forced invocation；
- near-miss 被抢；
- installed runtime 不是 `C`；
- 静态 route receipt 冒充实际 invocation。

### G2 — Core Project editing semantics

**Owner before independent review**：Executor。

覆盖：

- 三 edit modes；
- live/history/source/budget；
- missing-input degradation；
- ownership/enforcement；
- locator；
- protected absence；
- bounded/full/no-op。

使用 A/B/E/F/G/H/I/J/K 中按风险选取的真实 repo evidence / public-safe equivalent。

所有输出必须由 exact `C` runtime 产生。

### G3 — Fidelity / authority / should-not-change

**Owner before independent review**：Executor。

直接验证：

- mandatory/optional；
- authorization；
- safety/permission；
- evidence strength；
- uncertainty；
- exact identifiers；
- explicit deletion/correction；
- unrelated scope；
- near-miss owner。

使用 baseline/source/output 对照；输出绑定 `C`。

### G4 — Representative complete task + qualitative final artifact

**Executor ownership**：

- 从 exact `C` 运行代表性完整任务；
- 冻结完整 input/source/output；
- 生成 public-safe full packet；
- 可以做 self-check，发现明显 implementation defect 时回到 candidate repair；
- self-check 不是独立 qualitative PASS。

Executor 最大状态：

```text
G4_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor-owned evidence：

```text
results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_PACKET.md
```

packet 必须给 Reviewer：

- exact `FINAL_CANDIDATE_COMMIT=C`；
- representative complete inputs；
- fixed source/ref；
- full output；
- long/multi-scope case；
- risk-matched fresh public-safe case（在开发回归稳定后冻结）；
- artifact locators；
- self-check 明确标记为 non-independent / non-PASS。

**Independent Reviewer ownership**：

Reviewer 读取：

- final Skill source @ `C`；
- exact runtime/package identity；
- G1–G3 evidence；
- G4 packet；
- 完整 user artifact；
- README/VERSION/CHANGELOG candidate；
- `C -> EVIDENCE_HEAD` candidate-immutability proof。

Reviewer 才能写：

```text
G4=PASS|REVISE
IMPLEMENTATION_OVERALL=PASS|REVISE
```

Reviewer-owned file：

```text
results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_REVIEW.md
```

四 Gate taxonomy 不变，不新增 G5。

## 13. G1–G4 执行顺序

严格顺序：

```text
candidate-owned implementation
-> deterministic preflight
-> FINAL_CANDIDATE_COMMIT=C
-> install runtime from C
-> G1
-> G2
-> G3
-> generate G4 complete task packet
-> generate zip from C runtime tree
-> evidence-only commit(s)
-> EVIDENCE_HEAD=E
-> prove C..E candidate-owned diff is empty
-> independent Reviewer
```

G1–G3 可以在发现 candidate defect 时 FAIL，并触发 candidate repair；一旦 candidate-owned 内容修复，必须生成新 candidate commit，不把旧 PASS 带到新 candidate。

## 14. Exact candidate identity / evidence-head proof

Executor handoff 必须同时报告：

```text
FINAL_CANDIDATE_COMMIT=<C>
EVIDENCE_HEAD=<E>
```

并提供可复核的 proof：

```text
diff C..E
=> only results/project-instructions-editor--standalone-skill-implementation/**
```

不得仅凭 prose 声称“source没改”。

至少保存：

- `git diff --name-status C..E` 或等价；
- candidate-owned allowlist/deny check；
- runtime Skill tree hash 或 package manifest；
- installed runtime identity。

如果 `C..E` 出现任何 candidate-owned file，handoff 不得声称 candidate immutable。

## 15. Portable package

portable package：

```text
private/exports/project-instructions-editor-v0.1.zip
```

必须从 exact candidate commit `C` 的 runtime Skill tree 生成，而不是从可能包含后续 evidence changes 的模糊工作树状态生成。

允许使用 `git archive`、从 `C` 只读 materialization 或等价 deterministic route。

MANIFEST 记录：

```text
FINAL_CANDIDATE_COMMIT=C
zip SHA-256
archive file list
runtime Skill-tree identity/hash
generation method
```

zip 只含 Skill runtime 目录，不含 tests/results/design docs。

## 16. ChatGPT 与 Codex surface boundary

保持 v0.1 Critic 已 PASS 的边界。

required production normal-entry evidence：

```text
AI_Skills / Codex standalone install
+ fresh normal Codex session
```

保持 OpenAI Skill directory structure compatibility。

不创建 ChatGPT Plugin wrapper，不要求当前用户做 ChatGPT workspace upload，不宣称所有 ChatGPT account 都能直接安装/auto-use。

该 distribution/evidence 边界不改变“编辑 ChatGPT Project instructions”的产品语义。

## 17. Representative inputs 与 privacy

优先使用 repo 已保存：

- `docs/skill-todos/project-instructions-editor.md`；
- `PROJECT_INSTRUCTIONS_EDITOR_REAL_PROJECT_REGRESSION_LESSONS_2026-10-01.md`；
- frozen A–L task families；
- public-safe equivalents。

不得把私有 Project thread/settings 提交到公开 repo。

fresh case 在 candidate 稳定后冻结，不从输出反向挑题。

## 18. Version / README / release candidate

v0.1 Critic 已接受：

```text
Repository bump decision: MINOR
Expected candidate if origin/main remains 5.4.0: 5.4.0 -> 5.5.0
project-instructions-editor standalone: 0.1
all central plugins: NO_BUMP
```

Executor 修改 release-candidate metadata 前必须重新读 current `origin/main:VERSION`。

若仍为 `5.4.0`，candidate target `5.5.0`。

若已变化：

```text
VERSION_DRIFT
```

停止 version/release metadata，返回 Planner做最小 amendment；不得自行猜新版本。

Formal candidate-owned metadata包括：

- `VERSION` 与 required parity sources；
- root `CHANGELOG.md`；
- root `README.md` standalone card；
- standalone baseline tests；
- generated registry/catalog/provenance；
- 必要 icon/contact-sheet/generated audits。

不修改 central Plugin version/changelog，不新增 profile。

## 19. Evidence paths 与 ownership

Executor-owned：

```text
results/project-instructions-editor--standalone-skill-implementation/
├── RESULT.md
├── MANIFEST.md
├── G1_NORMAL_ENTRY.md
├── G2_CORE_SEMANTICS.md
├── G3_FIDELITY.md
└── G4_COMPLETE_TASK_PACKET.md
```

Reviewer-owned：

```text
results/project-instructions-editor--standalone-skill-implementation/
├── G4_COMPLETE_TASK_REVIEW.md
└── IMPLEMENTATION_REVIEW.md        # if Reviewer uses a separate overall review file
```

`FINAL_REPORT.md` 只在后续 review/closure 合法形成最终结论时写，不由 Executor在独立 review 前伪造 overall PASS。

## 20. Executor positive completion / stop point

Executor 阶段真正完成条件：

- candidate-owned content complete；
- deterministic preflight PASS；
- exact `FINAL_CANDIDATE_COMMIT=C` exists；
- G1 PASS on `C`；
- G2 PASS on `C`；
- G3 PASS on `C`；
- G4 full packet complete on `C`；
- `G4_READY_FOR_INDEPENDENT_REVIEW=YES`；
- portable zip generated from `C`；
- evidence committed；
- `EVIDENCE_HEAD=E` exists；
- `C..E` only evidence-only paths；
- exact branch pushed；
- remote tip verified；
- Reviewer can access all evidence.

Executor 最大 claim：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor 不得声明：

```text
G4=PASS
IMPLEMENTATION_OVERALL=PASS
RELEASED
PRODUCTION_READY
5.5.0_PUBLISHED
```

## 21. Independent Reviewer completion

独立 Reviewer 才负责：

1. 验证 `FINAL_CANDIDATE_COMMIT=C`；
2. 验证 `EVIDENCE_HEAD=E`；
3. 检查 `C..E` candidate-owned content未变化；
4. 审 G1–G3 evidence；
5. 阅读 G4 full packet 的完整 inputs/source/output；
6. 检查完整 user artifact；
7. 检查 README/VERSION/CHANGELOG/package identity；
8. 给：
   - `G4=PASS|REVISE`
   - `IMPLEMENTATION_OVERALL=PASS|REVISE`。

如果 Reviewer REVISE 只需 evidence fix 且不改变 candidate-owned 内容，可在 `C` 上补 evidence。

如果 Reviewer finding 要修改 candidate-owned 内容：

- 当前 `C` 的相关 Gate evidence失效；
- 返回 Executor产生 `C2`；
- 按 blast radius 重跑相应 Gate；
- 新 Reviewer 只以最新 candidate evidence做 final PASS。

## 22. User action / authorization boundary

用户后续实际发送 Critic-approved Kickoff 后，授权：

- exact branch/worktree；
- frozen source/docs/tests/generated/release-candidate/results edits；
- deterministic local tests；
- task-local standalone install/fresh Codex smoke；
- public-safe normal-entry/regression；
- portable zip；
- task-owned commits；
- ordinary non-force push exact task branch。

不授权：

- merge `main`；
- advance formal `release`；
- tag/GitHub Release/publish；
- paid API/model reviewer；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin source changes；
- Bridge Kit changes；
- force push / remote remap / destructive Git；
- watcher/daemon/database/ledger/state machine。

## 23. Maintenance state

Canonical tracking：

```text
tracking: #93
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

当前 Planner surface 无 GitHub Project field mutation，以上为 exact pending mutation，不声称已同步，也不要求用户手工维护。

Issue #93 reader-facing copy 仍落后于 implementation stage。当前没有可验证 Clear Writing invocation：

```text
CLEAR_WRITING_UNAVAILABLE
```

因此本轮不修改 Issue body。

## 24. Critic execution-ready review

Critic 本轮只需优先复核 E1/E2 是否关闭，并确认其他 v0.1 PASS 项没有回归。

### E1 closure check

- Executor only G1–G3 PASS；
- G4 Executor state only `READY_FOR_INDEPENDENT_REVIEW`；
- independent Reviewer owns G4 qualitative PASS/REVISE；
- no G5。

### E2 closure check

- candidate-owned content在 `C` 前完成；
- Gate运行绑定 `C`；
- zip来自 `C`；
- C 后只有 evidence-only commits；
- handoff带 `C` + `E`；
- 可证明 `C..E` 无 candidate-owned diff；
- candidate-owned change => new `C2` + stale old evidence + risk-matched rerun；
- no cross-candidate PASS stitching。

若同版 Plan + Goal + Kickoff execution-ready：

```text
READY_FOR_CODEX=YES
```

否则：

```text
READY_FOR_CODEX=NO
```
