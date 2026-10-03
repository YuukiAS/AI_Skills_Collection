# Project Instructions Editor — Dependent Execution Resume v0.1

Status: DRAFT_FOR_RECOVERY_CRITIC_REVIEW

本提示词只有在独立 Critic 对 recovery Plan v0.1 + 本 Resume Contract 给出 PASS 后，才可由用户发送给当前 exact task Executor。用户实际发送本正文时，才授权本次 current-main synchronization 与后续 bounded recovery。

## Resume 正文

继续执行现有任务：

repo:
YuukiAS/AI_Skills_Collection

task_key:
project-instructions-editor--standalone-skill-implementation

exact branch:
work/project-instructions-editor--standalone-skill-implementation

exact worktree:
../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

继续遵守：

docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md

当前 recovery 只处理 current-main drift，不重新设计产品或 Gate。

### 1. 核实最新 main 和 exact worktree

在 exact worktree：

- 核实 git rev-parse --show-toplevel；
- 核实 git branch --show-current；
- 核实 origin identity；
- 核实 worktree clean；
- git fetch origin main；
- 读取最新 origin/main 的 VERSION、workflow-core version、tests/test_candidate_plugin_replay.py relevant timeout。

若 main 已从 Planner 观察值继续前进，使用最新 main，不回退。

当前 Planner 观察值仅作为 reference：

origin/main = 4ce1946ba047ea200c4ab41ae824de999ef535ed
VERSION = 5.4.1
workflow-core = 0.5
shared replay timeout = 3

如果 latest main VERSION 不再是 5.4.1，停止 release-target reconciliation 并返回 Planner做最小 version amendment。

### 2. 同步 exact branch

不要 rebase。
不要 force push。
不要创建 successor branch。
不要新 clone。
不要改 remote。

如果 local exact task branch 落后于其同名 remote，先只做普通 fast-forward 到 remote task branch。

然后在 exact task branch：

git merge origin/main

这是本 Resume 明确授权的 ordinary non-force history-preserving merge。

如果 merge 有冲突，只解决为同时保留：

1. latest current-main 正式状态；
2. 已批准 Project Instructions Editor candidate 内容。

不得借 merge 修改无关 shared behavior。

### 3. 冲突处理硬边界

current main 拥有：

- workflow-core source / version / generated payload；
- 所有中央 plugin current versions；
- shared replay tests；
- current-main release history；
- 与 Project Instructions Editor 无关的 current-main source。

Project Instructions Editor task 拥有：

- skills/core/codex-system/project-instructions-editor/**；
- focused contract test；
- standalone baseline 的该 Skill entry；
- standalone card/icon；
- generated registry/catalog/provenance 中该 Skill identity；
- 5.5.0 candidate addition；
- task-local evidence history。

tests/test_candidate_plugin_replay.py 必须继承 latest current-main value，不保留 Project Instructions Editor task-specific timeout diff。

对 generated files：
先解决 source authority，再运行 current generators，不手工选择旧 generated output。

### 4. VERSION_DRIFT reconciliation

如果 merge 时 latest main 仍是 5.4.1：

Repository bump decision:
MINOR

candidate target:
5.5.0

standalone project-instructions-editor:
0.1

central plugins:
NO_BUMP for this task

必须保留：

- 5.4.1 release history；
- workflow-core 0.5；
- 其他 current-main central plugin state。

旧 candidate 的 5.4.0 / workflow-core 0.4 假设不得回流。

候选最终应表达：

5.4.1 -> 5.5.0

README Project Instructions Editor 卡片允许只做一个 bounded reader-facing cleanup：
把 live setting / canonical source 一类混合英文改成自然中文“当前设置、既有决定、事实来源和字符预算”。
不要改 README 其他无关内容。

### 5. Reconcile candidate-owned content

重新协调：

- Skill source/reference/evals/assets；
- focused tests；
- standalone baseline；
- registry/catalog/provenance；
- README；
- VERSION；
- CHANGELOG；
- required generated parity。

运行 approved implementation Plan 的 deterministic/full validation。

至少：

python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests

以及 current approved icon/generated checks。

无关 shared test failure 不在本任务顺手修。

### 6. Freeze new candidate C2

只有 candidate-owned content 全部稳定后，才创建新的 final candidate commit：

FINAL_CANDIDATE_COMMIT=C2

旧 candidate：

227bb9dbc5e35d546822d27d7985d4d81c371d1c

只作历史，不承担新的 final Gate PASS。

### 7. 从 C2 重跑全部 Gate evidence

严格：

C2
-> install from C2
-> G1
-> G2
-> G3
-> G4 full packet
-> zip from C2
-> evidence-only commits
-> EVIDENCE_HEAD=E2
-> prove C2..E2 has no candidate-owned changes
-> independent Reviewer

不得直接继承旧 C 的 PASS。

### 8. R2 / G1 near-miss closure

G1 必须在 relevant neighboring owners 实际可发现的 normal environment 中用 fresh sessions 运行。

至少覆盖：

ordinary Chinese prose -> chinese-prose
ordinary writing fidelity -> writing-fidelity
scientific/technical structural rewrite -> scientific-rewrite
AI_Skills_Collection maintenance -> ai-skills-core / ai-skills-repository-maintainer
complex workflow/control -> workflow-core / codex-workflow-protocol
generic agent/system prompt -> not project-instructions-editor
global Custom Instructions -> not project-instructions-editor

每个 case 记录：

- natural unnamed prompt；
- fresh session identity；
- actual loaded/selected owner；
- full user-visible output；
- project-instructions-editor 是否误触发。

静态 trigger JSON 不算 G1 evidence。

### 9. R1 / G4 full-input closure

旧 G4 输入没有足够证据时，不猜测旧 session。

在 C2 上重新跑一个运行前冻结的 public-safe complete case。

G4_COMPLETE_TASK_PACKET.md 必须逐字保存：

- exact natural user request；
- full live Project-setting baseline；
- targeted history；
- explicit nightly-build deletion/rejection evidence；
- exact budget；
- exact headroom；
- all canonical source contents；
- actual AGENTS.md content；
- source identities / SHA-256；
- fresh session/runtime identity；
- complete runtime output；
- actual output character count；
- NON_INDEPENDENT_SELF_CHECK；
- G4_READY_FOR_INDEPENDENT_REVIEW=YES。

Executor 不得声明 G4=PASS。

### 10. G2/G3 same-candidate rerun

G2 与 G3 必须由 C2 runtime 重新产生证据。

不能把旧 candidate G2/G3 PASS 直接标成 C2 PASS。

保留 approved capability claims，不重新设计任务族。

### 11. Package and evidence identity

portable zip 必须从 exact C2 runtime tree 生成：

private/exports/project-instructions-editor-v0.1.zip

MANIFEST 记录：

FINAL_CANDIDATE_COMMIT=C2
zip SHA-256
archive file list
runtime Skill-tree identity/hash
generation method
new Gate session identities

C2 后只允许 results/project-instructions-editor--standalone-skill-implementation/** evidence commits。

形成：

EVIDENCE_HEAD=E2

并实际保存：

git diff --name-status C2..E2

证明没有 candidate-owned changes。

若有 candidate-owned变化：
不要交 Reviewer；形成新 candidate并按 blast radius重新跑 Gate。

### 12. 最终 Executor 状态

只有满足全部条件后报告：

FINAL_CANDIDATE_COMMIT=C2
EVIDENCE_HEAD=E2
G1=PASS
G2=PASS
G3=PASS
G4_READY_FOR_INDEPENDENT_REVIEW=YES
G4=NOT_CLAIMED_BY_EXECUTOR
IMPLEMENTATION_OVERALL=NOT_CLAIMED_BY_EXECUTOR
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES

然后停止，交独立 Critic/Reviewer重新做 G4 与 overall implementation review。

### 13. 权限边界

本 Resume 授权：

- exact task branch/worktree；
- ordinary non-force merge origin/main into exact task branch；
- 必要 conflict resolution；
- approved candidate-owned reconciliation；
- deterministic/full tests；
- task-local install / fresh Codex Gate runs；
- public-safe evidence；
- portable zip；
- task-owned commits；
- ordinary non-force exact-branch publication。

不授权：

- merge task branch 回 main；
- advance release；
- tag / GitHub Release / publish；
- paid API/model review；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin 专属 behavior redesign；
- Bridge Kit changes；
- rebase + force push / force push；
- remote remap；
- destructive Git；
- watcher/daemon/database/ledger/state machine。

如果需要扩大这些边界，停止并返回 Planner。
