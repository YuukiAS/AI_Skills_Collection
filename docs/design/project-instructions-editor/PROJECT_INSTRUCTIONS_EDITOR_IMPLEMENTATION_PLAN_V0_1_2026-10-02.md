# Project Instructions Editor — Implementation Plan v0.1

Date: 2026-10-02  
Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Task key: `project-instructions-editor--standalone-skill-implementation`  
Approved architecture: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`  
Approved design freeze: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`  
Design-freeze Critic PASS: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md`  
Design-freeze review commit: `bf9add585924e93ab8844bb59a366f1cd4f837d6`  
Canonical Goal: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md`  
Kickoff Draft: `docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_1.md`  
Tracking: #93

```text
USER_AUTHORIZED_IMPLEMENTATION_PHASE=YES
READY_FOR_CODEX=NO
```

本 Plan 把已经冻结的产品合同转换为可执行实现合同。只有独立 Critic 对本 Plan、同版 Goal 和 Kickoff Draft 给出 execution-ready PASS，且用户随后实际发送 approved Kickoff，才允许 Codex 开始实现。

## 1. 实现目标

实现一个新的 standalone Skill：`project-instructions-editor`。

实现完成后，普通用户在已安装该 Skill 的真实正常入口中，用自然语言要求创建、修改、压缩、同步或重构长期 ChatGPT Project instructions 时，模型能够按冻结产品合同：

- 正确选择 preservation-sensitive / greenfield / explicit reset；
- 根据 live setting、相关历史、canonical source 与实际字符预算做语义 placement；
- 区分 semantic ownership 与 effective enforcement；
- 默认做 bounded edit；
- 保护 protected absence、权限/安全/证据强度和 exact identifiers；
- 缺输入时诚实降级；
- 支持 no-op；
- 给出比例化、可审查、必要时可直接复制的完整 setting。

实现不能退化成中文润色器、禁词表、字符评分器或通用 prompt optimizer。

## 2. Exact execution identity

实现任务固定为：

```text
task_key = project-instructions-editor--standalone-skill-implementation
branch = work/project-instructions-editor--standalone-skill-implementation
worktree = ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation
```

worktree 以 verified canonical `AI_Skills_Collection` checkout root 的父目录为基准，basename 必须精确匹配上面名称。

本任务采用**人工 Planner -> Codex Executor -> 独立 Critic/Reviewer**交接，不启用 watcher、daemon 或自动任务链。实现结束后 Codex 停在独立 review 前，不自动 merge `main`、不自动 release。

用户实际发送 approved Kickoff 后，才授权创建/复用上述 exact branch/worktree，以及该分支上的普通 task-owned commit 和 ordinary non-force push。

## 3. Latest-main preflight

Executor 开始前必须：

1. `git fetch origin main`；
2. 核实 canonical repo、origin、当前 `origin/main`；
3. 读取 current `AGENTS.md`、`docs/SKILL_AUTHORING.md`、`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`、Capability Gate policy、canonical TODO；
4. 核实 design-freeze PASS 仍在 history；
5. 核实当前 Skill metadata / `agents/openai.yaml` contract 与 standalone baseline tests；
6. 核实 `origin/main:VERSION`。

如果只是无关 docs/evidence drift，继续。

如果出现直接改变冻结产品合同、Skill metadata contract、standalone taxonomy、版本策略或正常入口语义的新事实，停止并返回 Planner/Critic；不得由 Executor自行重设计。

## 4. Source placement 与最小 Skill 结构

### 4.1 Canonical path

冻结实现路径：

```text
skills/core/codex-system/project-instructions-editor/
```

理由：

- 这是跨 Project、跨领域的系统级 support Skill；
- 不属于 writing domain，也不属于 research communication；
- 现有 `skills/core/codex-system/` 已承载全局工作流、仓库维护、项目 Skill 安装等系统支持能力；
- 不为一个 Skill 新建 taxonomy/domain。

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

同时新增/修改：

```text
tests/test_project_instructions_editor_contract.py
tests/test_standalone_skill_baselines.py
```

只有真实测试需要时，才可新增：

```text
tests/fixtures/project_instructions_editor/
```

不新增 `scripts/`。v0.1 是 instruction/reference Skill；字符计数/diff 若宿主已有能力可使用，但不为此创建独立 runtime/helper。

如果实现中证明没有 deterministic helper 就无法满足冻结能力，不得临时新增执行脚本并改变 capability metadata；返回 Planner/Critic。

## 5. Skill metadata contract

最终 `SKILL.md` frontmatter 至少必须显式保持：

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

解释：

- `requires_network: false` 表示 Skill 自身没有硬网络依赖；canonical source/history 不可达时按冻结降级，不伪造事实；
- `writes_files: false`：核心产品输出是 Project-setting edit/candidate，不自动修改 repo 或 ChatGPT Project setting；
- `executes_code: false`：核心语义判断不依赖代码；
- `recommended_scope: global`：该能力应跨 Project 可复用，不要求每个目标 Project 重新定义一份。

不得把 `allow_implicit_invocation` 作为普通 `SKILL.md` capability metadata。

## 6. agents/openai.yaml 与 normal entry

`agents/openai.yaml` 必须包含与 Skill 一致的用户界面元数据，例如：

```text
display_name = Project Instructions Editor
short_description = Safely update long-lived Project instructions
```

具体 YAML 结构使用当前 repo 的 `skill-creator` / `generate_openai_yaml.py` contract 生成，不手造不兼容 schema。

normal-entry 是冻结产品能力，因此：

- `policy.allow_implicit_invocation` 必须允许自然路由；按当前 schema 可显式为 `true`；
- description 是主要 discovery surface，必须同时写清 positive trigger 与 near-miss 边界；
- 不能靠用户点名 Skill 才 PASS；
- `allow_implicit_invocation: true`、trigger JSON、route receipt 或关键词命中都不能单独证明 Gate 1。

## 7. SKILL.md 与 reference 分工

### 7.1 SKILL.md

保持精炼，优先包含：

- trigger/near-miss boundary；
- 三 edit modes 的选择；
- 输入取得与缺失降级；
- 一条短核心推理链；
- bounded edit 默认；
- protected absence；
- locator 前置约束；
- no-op；
- output contract；
- 何时读取 `references/editor-contract.md`。

不要复制整个设计历史、Critic review、A–L 全文或大量回归故事。

### 7.2 references/editor-contract.md

承载实现需要的稳定详细合同：

- preservation-sensitive / greenfield / explicit reset；
- live/history/canonical source/budget；
- semantic ownership vs effective enforcement；
- locator substitution；
- protected absence；
- bounded/full rewrite；
- semantic invariants；
- proportional delivery；
- A–L regression bank 的抽象任务族与 should-not-change 原则。

reference 不得变成数据库、ledger 或任务状态文件。

## 8. Trigger eval contract

`evals/trigger_queries.json` 必须覆盖自然正例、反例和 near-miss，但当前 Plan 不固定样本数量。

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

Eval 文案不得直接提示 intended route rationale，也不得通过“请使用 project-instructions-editor”冒充 normal entry。

## 9. Deterministic tests 与 generated parity

新增 `tests/test_project_instructions_editor_contract.py`，机械保护至少包括：

- frontmatter capability metadata；
- version `0.1`；
- global recommended scope；
- `writes_files=false` / `executes_code=false` / no secrets；
- `agents/openai.yaml` normal-entry policy；
- trigger eval positive/negative/near-miss shape；
- reference locator 存在；
- 禁止 scripts/database/ledger/history-state runtime surfaces；
- registry record 与 source metadata 一致；
- Skill 不进入中央 Plugin Marketplace topology。

更新 `tests/test_standalone_skill_baselines.py`，加入：

- `project-instructions-editor`；
- expected standalone version `0.1`；
- icon identity；
- README standalone card；
- central plugin versions保持不变。

source 完成后只使用现有生成器刷新 derived artifacts。至少执行：

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

若当前 repo 有 icon/contact-sheet 或其他 standalone baseline generator，使用已有 generator 更新，不手改 generated output。

## 10. Capability Gate Matrix

A–L 是 regression/task-family bank，不机械变成 12 个 Gate。正式 implementation 使用四个 Gate family。

### G1 — Normal entry / routing boundary

**Capability / claim**  
普通用户从真实安装后的正常入口，以自然 Project-instruction 编辑请求触发正确 Skill；near-miss 保持原 owner。

**Why distinct**  
核心编辑逻辑即使正确，若用户触发不到或抢错写作/流程任务，产品仍不可用。

**Normal entry**  
从任务分支 final candidate 安装 standalone Skill 到隔离的真实 Codex skills target，开启 fresh session，以不点名 Skill 的自然请求调用。

**Evidence**  
实际 installed identity、fresh-session normal invocation、positive route + near-miss outputs。强制调用只可作诊断。

**Failure**  
只能 forced invocation；near-miss 被抢；装载 identity 不等于 final candidate；静态 receipt 代替真实 invocation。

**Regression boundary**  
`chinese-prose`、`writing-fidelity`、`scientific-rewrite`、`workflow-core`、`ai-skills-core` 的合法入口不被破坏。

**Final candidate**  
必须由同一 final candidate 直接通过。

### G2 — Core Project editing semantics

**Capability / claim**  
Skill 正确执行冻结的 Project-setting 专业判断。

必须覆盖：

- preservation-sensitive / greenfield / explicit reset；
- live setting / history / canonical source / budget；
- missing-input degradation；
- semantic ownership / effective enforcement；
- locator；
- bounded/full/no-op；
- protected absence。

**Evidence**  
A/B/E/F/G/H/I/J/K 中按风险选取的真实历史材料或 public-safe equivalents，完整输入与完整输出；Reviewer 能看到判断所依据的 source。

**Failure**  
旧 Candidate 冒充 live baseline；缺输入仍给 false-safe replacement；recent scope 吞预算；global/repo ownership 导致 Project hard control 失效；old-only absent rule 复活；无意义 full rewrite。

**Final candidate**  
release claim 必须来自同一 final candidate。

### G3 — Fidelity / authority / should-not-change

**Capability / claim**  
完成目标修改的同时不削弱未授权治理语义。

**Evidence**  
针对 mandatory/optional、authorization、安全、证据强度、不确定性、exact identifiers、explicit deletion/correction、unrelated scope 的 old-bad/new-good 对照；C/D/J/K 与代表性 should-not-change。

**Failure**  
目标 edit 看似成功，但权限/安全/强制性/证据结论被弱化，或旧删除规则复活，或 near-miss owner 被改变。

**Final candidate**  
同一 final candidate。

### G4 — Representative complete task + qualitative final artifact

**Capability / claim**  
完整产品在代表性长期 Project setting 上成立，不是 clause-level 测试拼接。

**Evidence**  
至少一个完整历史 Project-setting family（优先使用 repo 已保存的 AI Research Stack Reference/回归证据）以及一个不同类型 public-safe complete case；冻结 source/ref；从 normal entry 到完整 setting/no-op/advice；独立 Reviewer 读取完整输入、baseline/source 与完整输出做定性审查。

**Fresh/generalization**  
已知回归用于开发；final candidate 稳定后按风险冻结 fresh public-safe task，不固定机械样本数。

**Failure**  
局部 tests 全绿但完整 setting 失衡、语义漂移、不可直接使用，或 Reviewer只看 diff/字符数/摘要。

**Final candidate**  
必须绑定同一 final candidate，不拼接不同 commit 的 Gate PASS。

## 11. ChatGPT 与 Codex surface claim

当前官方 OpenAI 文档说明，ChatGPT Skills 的直接创建/安装/自动使用面向符合条件的 Business、Enterprise、Healthcare、Edu workspace，且不同产品/surface 可用性不同。当前 release 不应把 ChatGPT workspace upload/auto-use 宣称为所有账户都可用。外部核查依据为 OpenAI Help Center《Skills in ChatGPT》和 OpenAI Academy《Using skills》（均于 2026-10-02 核查）。

因此 v0.1 的 required normal-entry production evidence 冻结为：

- AI_Skills_Collection / Codex standalone Skill 安装与 fresh normal invocation；
- Skill package 保持 OpenAI Skill 目录结构兼容；
- 不创建 ChatGPT Plugin wrapper；
- 不要求当前用户账户做 ChatGPT workspace upload 作为 release Gate；
- 若未来 eligible workspace 可用，可追加真实 ChatGPT surface evidence，但不能拿它替代当前 Codex release evidence，也不能反向改变 Skill 产品合同。

这是 distribution/evidence 边界，不重新打开冻结的 Project-editor产品语义。

## 12. Representative inputs 与 privacy

优先复用仓库已经保存的真实设计/回归材料：

- `docs/skill-todos/project-instructions-editor.md` 中公开 Reference/真实回归摘要；
- `PROJECT_INSTRUCTIONS_EDITOR_REAL_PROJECT_REGRESSION_LESSONS_2026-10-01.md`；
- approved design freeze 中的 A–L task families。

不得把用户私有 Project thread、课程受限材料或未公开 setting 为了测试提交到公开 repo。

如果需要 fresh case，使用 public-safe 新任务并在 freeze 后评审；不能从最终输出反向挑题。

## 13. Final qualitative review

G4 不能由 deterministic tests 替代。

实现分支在：

- source 完成；
- generated parity；
- focused/full tests；
- G1–G3；
- final candidate freeze；
- G4 representative outputs；

之后，必须交独立 Critic/Reviewer读取：

- final Skill source；
- trigger eval；
- required references；
- exact final candidate commit；
- Gate evidence；
- G4 完整输入与完整输出；
- README/version/changelog candidate diff。

Reviewer 给 PASS/REVISE。REVISE 只允许在冻结合同内修复；如果需要改变产品职责、edit mode、owner boundary、Gate capability claim 或发布路线，返回 Planner。

## 14. Version / README / release candidate

当前 repository release 为 `5.4.0`。

本 Skill 是此前不存在的新正式 standalone user capability。按当前版本政策与 Project Thread Handoff 先例：

```text
Repository bump decision: MINOR
Expected candidate: 5.4.0 -> 5.5.0
Reason: collection gains a new installable standalone capability for safely editing long-lived ChatGPT Project instructions.

Affected central plugins:
- all: NO_BUMP

Standalone skill:
- project-instructions-editor: initial version 0.1
```

Executor 修改 release candidate metadata 前必须重新读取 current `origin/main:VERSION`。

若仍是 `5.4.0`，候选目标为 `5.5.0`。

若并行 release 已改变 repository version：

```text
VERSION_DRIFT
```

停止版本/release metadata 部分并返回 Planner做最小 version-target amendment；不要自行猜新版本。

Formal candidate 必须同步：

- `VERSION` 与 repository version parity sources；
- root `CHANGELOG.md`；
- root `README.md` standalone Skill card；
- standalone baseline tests；
- generated registry/catalog/provenance；
- 必要 icon contact sheet/generated audits。

不修改任何 central plugin version/changelog。

不新增 profile，除非未来另有独立需求。

## 15. Portable package

在 final candidate freeze 前生成可审 portable package：

```text
private/exports/project-instructions-editor-v0.1.zip
```

只包含 Skill runtime 目录，不包含 repo tests/results/design docs。

该 zip 是可交付/可审 artifact，不等于 ChatGPT 当前账户安装成功，也不是新的 Plugin。

记录 archive SHA-256 与 file list 到：

```text
results/project-instructions-editor--standalone-skill-implementation/MANIFEST.md
```

## 16. Evidence paths

实现 evidence 使用：

```text
results/project-instructions-editor--standalone-skill-implementation/
├── RESULT.md
├── MANIFEST.md
├── G1_NORMAL_ENTRY.md
├── G2_CORE_SEMANTICS.md
├── G3_FIDELITY.md
├── G4_COMPLETE_TASK_REVIEW.md
└── FINAL_REPORT.md              # 只有后续 Reviewer/closure 才最终成立
```

允许保存 public-safe input/output fixtures/evidence。私有 Project settings 不得进入公开 repo。

## 17. Stop point and integration boundary

本 implementation Goal 在 Executor 阶段完成时，必须达到：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

并满足：

- final candidate commit；
- exact branch pushed；
- G1–G4 evidence complete；
- release candidate metadata complete；
- package complete；
- tests/CI required by current repo complete；
- Reviewer 能访问完整 evidence。

Executor **不得**：

- merge `main`；
- advance formal `release` ref；
- tag / GitHub Release / publish；
- 宣称 repository `5.5.0` 已发布；
- 修改 central Plugin source；
- 创建 Plugin wrapper；
- 开启 paid API review；
- 修改 Bridge Kit；
- 新建 watcher/daemon/database/ledger/state machine。

独立 review PASS 后，integration/release closure 仍按当前 repo policy执行；若只剩机械且已授权的正常 integration，可在后续同一任务继续，但不能由 Executor预先冒充 PASS。

## 18. User action / authorization boundary

本任务不需要用户提供私有 Project setting，也不要求用户做 ChatGPT Skill upload。

用户实际发送 Critic-approved Kickoff 后，授权范围包括：

- exact branch/worktree；
- source/docs/tests/generated/release-candidate/result files；
- deterministic local tests；
- task-local standalone install/fresh Codex smoke；
- public-safe normal-entry and regression runs；
- portable zip；
- ordinary task-owned commits；
- ordinary non-force push exact task branch。

不授权：

- main merge；
- release ref/tag/GitHub Release；
- paid model/API；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin source change；
- Bridge Kit write；
- destructive Git/force push/remote remap。

## 19. Critic execution-ready review

Critic 必须同时审：

1. 本 Implementation Plan v0.1；
2. `PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md`；
3. `PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_1.md`。

重点检查：

- implementation path/taxonomy 是否最小且不误归 writing；
- metadata `writes_files=false` / `executes_code=false` / global scope 是否与冻结产品一致；
- implicit normal-entry 与 near-miss 是否可验证；
- reference split 是否不过重；
- 四 Gate 是否覆盖真实能力且不重复；
- ChatGPT surface claim 是否诚实；
- 5.5.0 MINOR 判断是否符合当前 version policy；
- Executor stop point 是否避免未审就 merge/release；
- Kickoff 授权是否恰好覆盖实现、没有扩大 destructive/paid/live-account 权限。

```text
READY_FOR_CODEX=NO
```
