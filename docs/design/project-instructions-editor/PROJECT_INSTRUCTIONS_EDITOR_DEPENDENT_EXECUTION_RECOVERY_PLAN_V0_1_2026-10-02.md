# Project Instructions Editor — Dependent Execution Recovery Plan v0.1

Date: 2026-10-02
Status: DRAFT_FOR_RECOVERY_CRITIC_REVIEW
Repository: YuukiAS/AI_Skills_Collection
Task key: project-instructions-editor--standalone-skill-implementation
Exact execution branch: work/project-instructions-editor--standalone-skill-implementation
Exact worktree locator: ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation
Approved implementation Plan: docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
Approved Goal: docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md
Approved Kickoff: docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md
Current blocker evidence: results/project-instructions-editor--standalone-skill-implementation/R3_PRECHECK_BLOCKER.md
Critic blocker review: results/project-instructions-editor--standalone-skill-implementation/DEPENDENT_EXECUTION_BLOCKER_REVIEW.md
Critic blocker-review commit: ebbebee0c42f93d362811594a829bc336a481e8f
Tracking: #93

PRODUCT_DESIGN_REOPEN=NO
VERSION_DRIFT=YES
R1=OPEN
R2=OPEN
R3=SUPERSEDED_BY_CURRENT_MAIN_SYNC
READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

本文件不是新的产品 Proposal，也不修改四个 Capability Gate。它只恢复已经批准的 implementation 在 current-main drift 后的可执行基线。

## 1. 当前真实状态

本轮 Planner 重新核对：

origin/main = 4ce1946ba047ea200c4ab41ae824de999ef535ed
main VERSION = 5.4.1
main workflow-core = 0.5
main tests/test_candidate_plugin_replay.py relevant timeout = 3
exact remote task branch HEAD = ebbebee0c42f93d362811594a829bc336a481e8f
merge base = 98721a202bc557c0b9c0800e66e50cab466bfba2

当前 task branch 相对 main 已经 diverged。GitHub 当前观察为 task branch ahead 8 / behind 14。

branch 当前仍带旧候选的 release identity：

branch VERSION = 5.5.0
branch workflow-core = 0.4
branch shared replay timeout = 0.5

因此不能继续把旧 branch 内容当 current-main-based release candidate。

Planner 当前 GitHub surface 可以核实 branch identity；exact worktree 的本机路径来自当前 task blocker evidence。恢复执行前 Executor 必须在本机再次用 git rev-parse --show-toplevel、git branch --show-current 和 origin identity 直接核实 exact worktree，不得仅依赖本文件。

## 2. 原 R3 的新归因

原 R3 不是“0.5 必须永远正确”。

current main 已经由正式 workflow-core 工作把 shared replay timeout 改为 3。本任务不拥有该共享测试策略，因此：

R3=SUPERSEDED_BY_CURRENT_MAIN_SYNC

恢复后的正确条件是：Project Instructions Editor task 对 tests/test_candidate_plugin_replay.py 不再拥有 task-specific timeout diff。

Executor 不得在本任务内重新决定 0.5、2 或 3 哪个更合理。同步 current main 后直接继承 current-main value。

若恢复执行时 main 又改变该值，同样继承最新 current-main value，不在本任务重新设计 shared replay behavior。

## 3. VERSION_DRIFT 的最小修正

approved implementation package 的 release type 仍然有效：

Repository bump decision: MINOR
project-instructions-editor standalone: 0.1
all central plugins: NO_BUMP

发生变化的是 release baseline，而不是 release 类型。

当前 main = 5.4.1。

所以若 Critic PASS 后恢复执行时 origin/main:VERSION 仍为 5.4.1：

candidate target = 5.5.0
release delta = 5.4.1 -> 5.5.0

必须保留 current main 已经正式存在的：

- repository 5.4.1 release history；
- workflow-core 0.5；
- current-main central plugin versions；
- current-main shared tests；
- current-main generated/plugin source facts。

旧 candidate 中的 5.4.0 baseline、workflow-core 0.4 等不得覆盖 current main。

如果恢复执行时 main VERSION 再次变化，Executor 不自行推导新 target；返回 Planner做新的最小 version-target amendment。

## 4. 唯一批准的 branch synchronization route

不 rebase，不 force push，不创建 successor branch，不新 clone，不改 remote。

恢复时继续：

branch = work/project-instructions-editor--standalone-skill-implementation
worktree = ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

Critic PASS 后、用户实际发送 approved Resume Contract 后，授权的同步路线是：

1. 在 exact worktree 核实 repo / branch / origin identity；
2. 要求 worktree clean；若 dirty，先判断 ownership，不自动 stash/reset/restore；
3. git fetch origin main；
4. 核实 remote exact task branch 与当前本地 task branch，不改 upstream；
5. 若 local task branch 只落后于其同名 remote task branch，先普通 fast-forward 到同名 remote HEAD；
6. 在 exact task branch 上执行 ordinary non-force history-preserving merge：git merge origin/main；
7. 只处理必要冲突；
8. 普通 commit；
9. 后续使用已授权 exact branch 的 bounded non-force publication route；不得 force push。

这条路线保留已有 task history 和 current main history，不改写已推送 task branch。

## 5. 冲突解决边界

merge conflict 只允许为了同时保留两类事实：

1. current main 正式状态；
2. 已批准 Project Instructions Editor candidate 内容。

不得借 merge 做无关 cleanup 或 shared behavior redesign。

### 5.1 current main 优先的 shared content

以下内容以恢复执行时 current origin/main 为 authority：

- workflow-core source / generated plugin / version；
- scripts/codex_marketplace_config.json 中所有中央 plugin current versions；
- tests/test_candidate_plugin_replay.py shared timeout 与其他 shared replay behavior；
- current-main 已正式发布的 release history；
- 其他与 Project Instructions Editor 无关的 main changes。

特别是 tests/test_candidate_plugin_replay.py 不得保留 task-specific timeout diff。若 main 仍为 3，merge 后就是 3。

### 5.2 Project Instructions Editor task 保留的 candidate content

继续保留：

- skills/core/codex-system/project-instructions-editor/**；
- focused Project Instructions Editor contract test；
- standalone baseline 中该 Skill 的正式 entry；
- standalone card / icon identity；
- generated registry/catalog/provenance 中该 Skill identity；
- release candidate 5.5.0 entry；
- Project Instructions Editor 自己的 task evidence/result history。

### 5.3 双方都修改的 release/generated 文件

预计可能重叠：

- VERSION；
- README.md；
- CHANGELOG.md；
- registry.json；
- docs/SKILL_CATALOG.md；
- provenance/generated audit files；
- standalone/version baseline tests；
- icon/contact-sheet identity files。

处理原则：

1. 先保留 current-main source facts；
2. 再保留 Project Instructions Editor source addition；
3. generated 文件不靠手工选择旧版/新版维持，source 对齐后用 current generator 重新生成；
4. candidate release metadata 最终表达 current main 5.4.1 完整历史之上的 5.5.0 candidate；
5. central plugin versions必须来自 current main，特别是 workflow-core 0.5。

## 6. Candidate-owned reconciliation

main merge 完成后，在形成新 candidate 前重新协调：

- Skill source/reference/evals/assets；
- focused test；
- standalone baseline；
- registry/catalog/provenance；
- README；
- VERSION；
- CHANGELOG；
- required generated parity。

若 main 仍为 5.4.1，候选必须满足：

VERSION = 5.5.0
README repository candidate = 5.5.0
CHANGELOG keeps 5.4.1 release history and adds/preserves 5.5.0 candidate entry
workflow-core = 0.5
all other central plugin versions = current-main values
project-instructions-editor = standalone 0.1
central plugins = NO_BUMP for this task

README 新 Skill 卡片允许做 Critic 已明确标为 non-blocking 的同范围文案修正：“当前设置、既有决定、事实来源和字符预算”。不得借此改写 README 其他内容。

## 7. Deterministic validation 与 C2 formation

完成 merge、冲突处理、source/generated reconciliation 后，先运行 approved Plan 中的全部 deterministic/full validation。

至少继续包括：

python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests

如果 current repo 还有 approved implementation 已要求的 icon/generated checks，同样运行。

测试失败时：

- Project Instructions Editor scope 内 defect：在批准范围内修复；
- main merge/release parity defect：只做使 current-main facts 与 approved candidate 共存所需的最小修复；
- 无关 shared behavior defect：停止并回 Planner/Critic，不在本任务顺手修。

全部 candidate-owned 内容稳定后才创建新的：

FINAL_CANDIDATE_COMMIT=C2

旧 227bb9dbc5e35d546822d27d7985d4d81c371d1c 只保留为历史候选，不能继续承担 final PASS。

## 8. Gate rerun boundary

因为 candidate-owned baseline 已变化，不能把旧 C 的 Gate PASS 直接拼到 C2。

严格恢复顺序保持 approved v0.2 contract：

C2
-> install from C2
-> G1 on C2
-> G2 on C2
-> G3 on C2
-> G4 full packet from C2
-> zip from C2
-> evidence-only commits
-> EVIDENCE_HEAD=E2
-> prove C2..E2 has no candidate-owned changes
-> independent Reviewer

四个 Capability Gate 的 capability claim、owner 和 taxonomy全部不变。

## 9. R1 仍 OPEN：G4 完整输入

G4 必须重新提供一份 public-safe、在运行前冻结、可独立检查的完整 packet。

至少逐字保存：

- exact natural user request；
- full live Project-setting baseline；
- relevant targeted history；
- explicit deletion/rejection evidence，包含 nightly-build deletion；
- exact character budget；
- exact headroom；
- all canonical source contents；
- actual AGENTS.md source内容或 repo-safe exact copy + stable hash；
- 每个 source identity/hash；
- fresh session/runtime identity；
- complete runtime output；
- output length；
- non-independent Executor self-check boundary。

Executor 只能声明：

G4_READY_FOR_INDEPENDENT_REVIEW=YES
G4=NOT_CLAIMED_BY_EXECUTOR

独立 Reviewer 才给 G4 qualitative PASS/REVISE。

如果旧 G4 exact inputs 没有完整保存，不补写/猜测旧输入；直接在 C2 上重新跑一个运行前冻结的 public-safe complete case。

## 10. R2 仍 OPEN：真实 near-miss owner routing

G1 必须在相关邻近 owner 实际可发现的 normal environment 中运行 fresh sessions。

至少覆盖：

ordinary Chinese prose -> chinese-prose
ordinary writing fidelity -> writing-fidelity
scientific / technical document structural rewrite -> scientific-rewrite
AI_Skills_Collection maintenance -> ai-skills-core / ai-skills-repository-maintainer
complex workflow / control -> workflow-core / codex-workflow-protocol
generic agent/system prompt -> not project-instructions-editor
global Custom Instructions -> not project-instructions-editor

每个 case 保存：

- natural unnamed prompt；
- fresh session identity；
- actual loaded/selected owner；
- user-visible output；
- project-instructions-editor 是否误触发。

静态 trigger JSON、description、route receipt不能替代 runtime evidence。

## 11. E2 与 independent review

C2 后不得再修改 candidate-owned content。

portable zip 必须来自 C2 runtime tree。

后续只允许 evidence-only commits，形成：

EVIDENCE_HEAD=E2

handoff 必须证明 git diff --name-status C2..E2 只包含：

results/project-instructions-editor--standalone-skill-implementation/**

若 C2 后出现任何 candidate-owned 变化：

- 旧相关 Gate evidence失效；
- 形成新 candidate；
- 按 blast radius重跑；
- 不跨 candidate 拼 PASS。

最终 Executor 状态仍只能是：

FINAL_CANDIDATE_COMMIT=C2
EVIDENCE_HEAD=E2
G1=PASS
G2=PASS
G3=PASS
G4_READY_FOR_INDEPENDENT_REVIEW=YES
G4=NOT_CLAIMED_BY_EXECUTOR
IMPLEMENTATION_OVERALL=NOT_CLAIMED_BY_EXECUTOR
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES

然后交独立 Reviewer重新做 G4 / overall implementation review。

## 12. 权限与禁止事项

本 recovery 不增加产品或副作用权限。

Critic PASS 后，用户实际发送 approved Resume Contract 才授权：

- exact task branch/worktree 内的 main synchronization；
- ordinary non-force merge origin/main 到 exact task branch；
- 仅为 current-main + approved candidate 共存所需的冲突处理；
- candidate-owned reconciliation；
- deterministic/full tests；
- task-local install/fresh Codex Gate runs；
- public-safe evidence；
- portable zip；
- task-owned commits；
- ordinary non-force exact-branch publication。

仍不授权：

- merge task branch 回 main；
- advance release；
- tag / GitHub Release / publish；
- paid API/model review；
- private Project data external transmission；
- live ChatGPT account mutation；
- central Plugin 专属行为改造；
- Bridge Kit 修改；
- rebase + force push / force push；
- remote remap；
- destructive Git；
- watcher/daemon/database/ledger/state machine。

## 13. Maintenance state

Canonical tracking remains: tracking: #93

Target Project state remains:

Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md

当前 Planner surface 没有 GitHub Project field mutation能力，因此这是 exact pending mutation，不声称已同步，也不要求用户手工维护。

Issue reader-facing copy 仍要求真实调用 Clear Writing。当前无可验证 invocation surface：

CLEAR_WRITING_UNAVAILABLE

本轮不修改 Issue body。

## 14. Recovery stop condition

本 recovery Plan 本身不执行 merge，不运行 Gate，不创建 C2。

Critic PASS 前保持：

READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

Critic 只需审 current-main synchronization、VERSION_DRIFT、conflict boundary、C2 formation 和 R1/R2 continuation 是否足够且没有扩大产品设计。
