# AI Skills Maintenance Board — Final Closure Execution Critic Prompt v0.1

你是 AI Research Stack 的独立 Critic。

当前只审 Maintenance Board 最终 closure implementation package v0.1 是否可执行、真实、不过重，并决定是否 READY_FOR_CODEX。

不要执行 mutation，不修改 Project / Issue #4 / canonical policy，不做 machine adaptation，不启动 Executor，不重跑 v7。

## Active Review Context

target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / governance closure
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills Maintenance Board 最终收口
review_stage = FINAL_CLOSURE_EXECUTION_READY_REVIEW_V0_1
source_branch_or_ref = main
execution_branch = reviewed/repo--maintenance-board-lifecycle
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
package_snapshot_commit = 2ddb7533234564a4731286aaf4bcddd8b8c45e6d

## Approved semantic authority

v6.1 Proposal:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md

Reviewed Proposal commit:
515c42623c55f368eb84a1628839459afa909c09

v6.1 Critic review:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md

Critic result:
PASS

Do not reopen v6.1 required-consumer architecture without new direct evidence.

## Current completed capability

v7 final closure commit:
700234d7e94bb5613f951b8adeb7155d3b15ec3f

v7 is already complete. Do not redesign or rerun it.

## Exact package

Plan:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md

Goal:
docs/goals/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_GOAL_V0_1.md

Kickoff:
docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_KICKOFF_V0_1.md

Final WSL continuation prompt:
docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_REMAINING_CONSUMER_CUHK_WSL_V0_1.md

All four coexist in exact package snapshot:
2ddb7533234564a4731286aaf4bcddd8b8c45e6d

## 必须读取 latest main

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- approved v6.1 Proposal
- v6.1 Critic PASS
- results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md
- results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md
- Issue #4 live state
- results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md
- results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json
- Issue #92 / #93 / #94 as needed
- results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md
- results/ai-skills-core--machine-update-orchestration/CUHK_WORKSTATION_WSL_CODEX_MACHINE_SYNC_2026-09-29.md only as consumer-identity corroboration, not as board-contract PASS

Then read the exact package snapshot files above.

## 1. Canonical v6.1 implementation

Package changes only current normative truth:

§14:
fixed-five -> actual normal-entry + explicitly promised fallback required set.

§15:
keep per-current-consumer Maintainer boundary; replace fixed-five aggregate truth with quantity-neutral required-consumer aggregate truth.

§16:
generic all-required-consumers closure unchanged.

Historical v4/v5/v6/v7 design/review artifacts remain historical.

Check:
- this exactly implements approved v6.1;
- it does not rewrite history;
- it does not alter v7 taxonomy/intake/lifecycle;
- any extra fixed-five normative wording in the current canonical policy is converged only if directly contradictory.

## 2. CURRENT_REQUIRED_SET — critical review

Planner freezes:

CURRENT_REQUIRED_SET =
1. AI Research Stack ChatGPT Project instructions
2. Longleaf_Codex
3. CUHK_Workstation_WSL_Codex

States:
- Project instructions = PASS
- Longleaf_Codex = PASS
- CUHK_Workstation_WSL_Codex = PENDING

Historical non-required:
- Longleaf_Backup_Codex
- Windows Workstation
- Legion

Independently judge this against approved v6.1.

### 2.1 Project instructions

Evidence:
results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md

It records user-confirmed semantic installation of the board trigger and the no-manual-Kanban contract.

Check whether it is correct to include this already-satisfied normal-entry surface in the exact current set.

### 2.2 Longleaf_Codex

Evidence:
- Issue #92 says v7 Stage A executed on Longleaf_Codex;
- v7 execution package/recovery designated Longleaf_Codex primary environment;
- final v7 closure proves actual Project/Issue/source/audit behavior;
- #93 source backlink repair + Project tracking + metadata audit zero violations were completed on that execution line.

Check whether this is enough direct current evidence to freeze Longleaf_Codex = PASS without rerunning Longleaf.

Do not require a redundant machine-update campaign unless a missing board-specific claim actually requires it.

### 2.3 CUHK_Workstation_WSL_Codex

Historical handoff maps:
/home/yuukias/AI_Skills_Collection
to:
CUHK_Workstation_WSL_Codex

Latest main contains actual normal-entry workflow execution evidence at the same canonical checkout:
results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md

The package therefore treats WSL as a current real normal-entry consumer, not a stale machine-matrix row.

It remains PENDING because the latest post-v7 board contract has not been freshly consumed there.

Check whether this direct current evidence is sufficient to keep WSL required.

Do not remove it merely because the machine is currently offline.

### 2.4 Excluded historical machines

For Longleaf_Backup_Codex / Windows Workstation / Legion, current package finds no direct Maintenance Board normal-entry or explicit fallback promise.

Their AI Skills Maintainer machine-update evidence is not sufficient under v6.1.

Check whether any latest-main current product contract directly contradicts that exclusion.

If you think one is required, cite the exact current normal-entry/fallback contract; do not rely on the old five-machine default.

## 3. One remaining WSL handoff

Package freezes:

FINAL_REMAINING_CONSUMER = CUHK_Workstation_WSL_Codex

The Longleaf stage completes all repo/policy/evidence/Issue-current-truth work first and leaves #4 ADAPTING.

Only WSL remains later.

Check this satisfies the user requirement not to block all closure work on the outage.

## 4. Final WSL prompt

Review the exact WSL prompt in the package.

It must:

- run once after WSL returns;
- verify latest main and v6.1 current truth;
- verify only WSL remains pending;
- use exact canonical checkout /home/yuukias/AI_Skills_Collection;
- run one fresh ordinary read-only Codex repo-entry smoke;
- prove the fresh normal entry consumes latest board contract;
- save durable PASS evidence;
- reuse the same canonical task/branch, not a successor;
- not rerun Longleaf;
- not rerun v7;
- after WSL PASS, automatically finish aggregate closure;
- use a final evidence commit as Resolution commit;
- Clear Writing final Issue #4;
- close #4 completed and verify Project DONE.

Check whether the fresh normal-entry smoke is bounded and actually tests board-contract consumption rather than machine-update capability.

## 5. Historical CONSUMER_HANDOFFS

Package preserves old five-consumer content and appends a clearly labeled current section.

Check this preserves provenance while preventing stale historical handoff text from being mistaken for current closure truth.

## 6. Issue #4 reader truth

Longleaf stage, after implementation review and main integration, will Clear-Write Issue #4 to say:

- central implementation complete;
- v7 complete;
- v6.1 evidence-backed consumer contract implemented;
- exact current required set;
- Project instructions PASS;
- Longleaf PASS;
- WSL only pending;
- Longleaf_Backup / Workstation / Legion historical, not prerequisites.

It stays open / ADAPTING until WSL PASS.

Check this is the truthful intermediate state.

## 7. Final closure mechanics

After WSL PASS the same one-shot action:

- updates current handoff status;
- writes final closure evidence;
- runs metadata audit;
- README check;
- integrates final evidence to main;
- uses the exact final evidence commit as Resolution commit;
- invokes Clear Writing;
- updates Issue #4;
- writes Project Resolution commit;
- closes #4 completed;
- verifies Project DONE / Area=repo / Resolution commit;
- verifies latest main and clean workspace.

Check that this is mechanically sufficient and does not require another design round.

## 8. Normal-use acceptance

No new synthetic Issue.

Package relies on:
- #92 completed v7;
- #93 real tracked standalone-skill maintenance;
- #94 existing pre-admission smoke;
- latest metadata audit;
- actual Project readback;
- open-only auto-add.

Check whether this is sufficient to support:
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO

This claim means normal maintenance roles + GitHub built-ins synchronize the existing sources of truth. It does not claim a bot autonomously guesses lifecycle.

## 9. Branch / worktree / authorization

Longleaf:
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle

At package prep that remote branch is absent, so approved Kickoff may recreate the same canonical task branch from latest main.

WSL:
same branch
canonical checkout = /home/yuukias/AI_Skills_Collection
worktree = /home/yuukias/AI_Skills_Collection-repo--maintenance-board-lifecycle

Check that this remains one canonical task rather than a successor.

## 10. Review / integration gates

Package requires independent implementation review of actual Longleaf diff/evidence before main integration.

Then:
- integrate policy/current-set evidence;
- update Issue #4 current truth;
- wait only for WSL if offline.

WSL prompt is already part of this Critic-reviewed package.

Check whether this is enough independent review without adding another architecture loop.

## 11. Failure safety

Check:

- WSL offline -> leave ADAPTING, Longleaf work remains valid;
- required-set evidence changes -> stop, no close;
- fresh WSL normal entry fails -> WSL pending;
- Project write permission missing -> no false closure;
- audit failure -> no close;
- Resolution commit readback failure -> no close;
- issue-close fails to produce DONE -> report blocker.

No rerun Longleaf/v7.

## 12. Version / prohibited scope

Expected:

Repository bump = NONE
all plugins = NO_BUMP
Production Plugin Capability Gate = NOT REQUIRED

Forbidden:
- production plugin source mutation;
- v7 redesign;
- new Project field/lifecycle;
- machine registry/controller/watcher/daemon/database;
- new Skill/Plugin/Profile;
- Bridge Kit mutation;
- successor task.

Independently verify this remains policy-only/governance closure.

## Output

If revision is required:

RESULT = REVISE
REVIEW_STAGE = FINAL_CLOSURE_EXECUTION_READY_REVIEW_V0_1
PACKAGE_SNAPSHOT_COMMIT = 2ddb7533234564a4731286aaf4bcddd8b8c45e6d
READY_FOR_CODEX = NO

Give stable blocker IDs, direct evidence, causal risk and minimum close condition.
Do not reopen v7 or v6.1 without new direct evidence.

If PASS:

First explain in natural Chinese:

- exact current required-set judgment;
- why Longleaf is PASS;
- why WSL is still required/pending or, if you disagree, direct contrary evidence;
- why Longleaf_Backup/Workstation/Legion are not current prerequisites;
- canonical policy convergence;
- one-shot WSL closure safety;
- normal-use/no-manual-Kanban claim;
- what PASS proves and does not prove.

Then output:

RESULT = PASS
REVIEW_STAGE = FINAL_CLOSURE_EXECUTION_READY_REVIEW_V0_1
PACKAGE_SNAPSHOT_COMMIT = 2ddb7533234564a4731286aaf4bcddd8b8c45e6d
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_GOAL_V0_1.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_KICKOFF_V0_1.md
APPROVED_FINAL_WSL_PROMPT_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_REMAINING_CONSUMER_CUHK_WSL_V0_1.md
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex
FINAL_REMAINING_CONSUMER = CUHK_Workstation_WSL_Codex
NEW_BLOCKERS = NONE
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX

Then reproduce the exact reviewed Longleaf Kickoff from package snapshot.
Do not rewrite the WSL prompt; approve it by exact path/hash as part of the package.

## Review-file authorization

用户发送本 prompt，即授权你只在 latest main 新增：

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-02.md

并 ordinary non-force push。

除此之外禁止修改:
- Plan / Goal / Kickoff / WSL prompt;
- canonical board policy;
- CONSUMER_HANDOFFS;
- Issue #4 / Project;
- machine state;
- production source;
- any other repo.
