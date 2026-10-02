# AI Skills Maintenance Board — Final Closure Implementation Plan v0.2

Date: 2026-10-02
Repository: YuukiAS/AI_Skills_Collection
Canonical task: repo--maintenance-board-lifecycle
Tracking Issue: #4
Package version: v0.2
Supersedes: v0.1 final-closure package
Planner baseline: current latest main
Final v7 closure commit: 700234d7e94bb5613f951b8adeb7155d3b15ec3f
Approved v6.1 Proposal: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
Approved v6.1 Proposal commit: 515c42623c55f368eb84a1628839459afa909c09
Approved v6.1 Critic review: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md
v6.1 Critic result: PASS
Status: READY_FOR_EXECUTION_CRITIC_REVIEW
This Plan does not authorize execution.

## 1. Correction to v0.1

v0.1 over-interpreted historical WSL usage evidence as a current Issue #4 closure requirement.

That was wrong.

The current user/product contract explicitly says the Workstation/WSL environment is not to be part of this final closure. Under approved v6.1 semantics, required consumers are defined by the tracked item's current actual normal-entry / explicitly promised fallback contract, not by historical machine presence or by the fact that a machine can host AI_Skills work.

There is no new current product promise that Issue #4 requires CUHK_Workstation_WSL_Codex for closure.

Therefore v0.2 freezes:

CURRENT_REQUIRED_SET =
- AI Research Stack ChatGPT Project instructions
- Longleaf_Codex

CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS =
- CUHK_Workstation_WSL_Codex
- Longleaf_Backup_Codex
- Windows Workstation
- Legion

CUHK_Workstation_WSL_Codex is not marked PASS or N/A. It is simply not part of the current Issue #4 completion contract.

## 2. Final product target

This is the last governance closure task for the Maintenance Board.

v7 already proves the normal daily path:

- open-only maintenance-track Project admission;
- Issue taxonomy;
- Forms intake;
- pre-admission Action;
- canonical tracking:#N integrity;
- duplicate false-DONE repair;
- metadata audit PASS;
- search acceptance PASS;
- stale safety PASS;
- real Issue #93 tracking and source backlink;
- user does not manually drag Kanban cards.

This final task only:

1. implements approved v6.1 current consumer semantics;
2. updates Issue #4 from stale fixed-five truth to current evidence-backed truth;
3. preserves historical handoff evidence;
4. verifies current required consumers are already satisfied;
5. closes Issue #4 and the Maintenance Board project.

No machine adaptation remains.

## 3. Exact execution identity

repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = execution-time latest origin/main
primary_environment = Longleaf_Codex

At package preparation time the remote reviewed/repo--maintenance-board-lifecycle branch may be absent. The approved Kickoff may create that exact branch from latest origin/main. This is the same canonical task, not a successor.

No alternate branch/worktree, /tmp fallback, dirty canonical checkout, force push or history rewrite.

## 4. Current required set

CURRENT_REQUIRED_SET =
1. AI Research Stack ChatGPT Project instructions
2. Longleaf_Codex

### 4.1 Project instructions = PASS

Direct evidence:
results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md

It records user-confirmed semantic installation of the Maintenance Board trigger, including proactive synchronization and no manual Kanban maintenance.

### 4.2 Longleaf_Codex = PASS

Direct evidence:
- Issue #92 records v7 execution on Longleaf_Codex;
- v7 packages and recovery explicitly used Longleaf_Codex as primary execution environment;
- final v7 closure commit = 700234d7e94bb5613f951b8adeb7155d3b15ec3f;
- results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md = COMPLETE;
- latest metadata audit = PASS / zero violations;
- #93 real tracking path and source backlink passed;
- #94 pre-admission smoke passed.

No new Longleaf machine adaptation or machine-update campaign is required.

### 4.3 Why WSL is not required

Historical evidence proves CUHK_Workstation_WSL_Codex existed and previously ran AI_Skills work.

That is not enough under v6.1.

The current user/product contract explicitly excludes Workstation/WSL from this final Maintenance Board closure. No current Maintenance Board normal-entry or fallback promise requires Issue #4 to wait for WSL.

Therefore:
CUHK_Workstation_WSL_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT

This is not PASS.
This is not N/A due outage.
This is a current scope determination under v6.1.

The same applies to:
Longleaf_Backup_Codex
Windows Workstation
Legion

## 5. Canonical policy implementation

Modify only current normative truth in:

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

### §14

Replace fixed-five default with approved v6.1:

- required consumers are actual normal-entry consumers and explicitly promised fallback environments needed for the tracked item's frozen completion claim;
- a machine is not required merely because AI Skills Maintainer is installed, it appeared in another machine-update matrix, it has Codex, or it can clone the repo;
- fallback is required only when explicitly promised;
- ADAPTING freezes the evidence-backed set;
- ambiguity keeps the item ADAPTING and returns Planner;
- do not add environments "for safety";
- do not omit an explicitly promised environment.

### §15

Keep per-current-consumer Maintainer boundary.

Replace fixed-five aggregate truth with:

当前 tracked item 的 required-consumer 聚合真值属于 tracking Issue / Project lifecycle。

### §16

Keep unchanged:

all required consumers PASS/N/A
+ durable evidence
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE

Converge any other current normative fixed-five wording in the canonical file only where directly inconsistent with v6.1.

Do not rewrite historical Proposal/Review/Goal/Kickoff artifacts.

## 6. CONSUMER_HANDOFFS history preservation

Keep:

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

Do not delete historical five-consumer evidence.

Append a clearly labeled current section:

HISTORICAL_HANDOFF_MATRIX

The existing five-machine material is historical evidence only.

CURRENT_REQUIRED_SET — 2026-10-02

AI Research Stack ChatGPT Project instructions = PASS
Longleaf_Codex = PASS

CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS

CUHK_Workstation_WSL_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Longleaf_Backup_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Workstation = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Legion = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT

## 7. Final closure evidence

Create:

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md
results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json
results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md

Required truth:

CURRENT_REQUIRED_SET_FROZEN = YES
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES
FINAL_REMAINING_CONSUMER = NONE

## 8. Implementation stage

After execution-ready Critic PASS and user Kickoff:

1. create exact task branch/worktree from latest main;
2. implement canonical v6.1 policy change;
3. append current truth to CONSUMER_HANDOFFS.md;
4. write final required-set/closure evidence;
5. run git diff --check;
6. run current Maintenance Board metadata audit;
7. verify v7 final closure commit ancestry;
8. verify #93 current tracking/source backlink;
9. README closure check;
10. prepare Clear Writing draft for Issue #4 final closure;
11. independent implementation Reviewer.

No Workstation/WSL access is needed or allowed as a prerequisite.

## 9. Independent implementation review

Reviewer must inspect:

- exact §§14–16 canonical diff;
- historical evidence preserved;
- current required-set evidence;
- Project instructions PASS evidence;
- Longleaf PASS evidence;
- WSL/Backup/Workstation/Legion exclusion as current non-required historical consumers;
- Issue #4 final reader-facing draft;
- metadata audit;
- README/version decision.

Required result:

FINAL_CLOSURE_IMPLEMENTATION_REVIEW = PASS
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES
MAIN_INTEGRATION_AUTHORIZED = YES

## 10. Final integration and Issue #4 closure

After Reviewer PASS:

1. ordinary non-force integrate reviewed branch to latest main;
2. verify remote main;
3. use the exact integrated final-evidence commit as Issue #4 Resolution commit;
4. invoke Clear Writing before Issue #4 mutation;
5. update Issue #4 current/final truth:
   - central Maintenance Board complete;
   - v7 complete;
   - fixed-five semantics replaced by evidence-backed v6.1;
   - CURRENT_REQUIRED_SET = Project instructions + Longleaf_Codex;
   - both PASS;
   - WSL / Longleaf_Backup / Windows Workstation / Legion are historical evidence, not current closure prerequisites;
   - users do not manually maintain Kanban;
   - Resolution commit + durable evidence visible;
   - next action = none;
6. write Project #4 Resolution commit;
7. close Issue #4 as completed;
8. verify issue-closed workflow yields Project DONE;
9. verify Project Area=repo;
10. verify exact Resolution commit;
11. run final metadata audit;
12. final latest-main readback;
13. verify workspace clean.

No machine handoff remains.

## 11. Final normal-use acceptance

Do not create new synthetic Issues.

Use:

- #92 v7 completed;
- #93 real standalone-skill tracked Issue;
- #94 existing pre-admission smoke;
- latest metadata audit;
- actual Project readback;
- open-only auto-add contract.

Final claim:

real project feedback
-> canonical TODO
-> tracking:#N when admitted
-> Issue + Project
-> Area + lifecycle
-> proactive Planner/Critic/Maintainer/Codex synchronization
-> truthful DONE/non-completion

USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO

This does not mean a bot guesses lifecycle.

## 12. Failure recovery

- latest main conflicts with v6.1 -> stop Planner/Critic;
- new direct evidence creates an explicit current fallback/normal-entry promise -> stop before #4 close;
- implementation Reviewer REVISE -> repair/re-review within this package;
- metadata audit failure -> no close;
- Project Resolution commit readback failure -> no close;
- issue close does not produce Project DONE -> report blocker, do not fabricate completion;
- Project mutation surface unavailable -> exact pending mutation for Project-capable executor; do not ask user to drag Kanban.

Do not wait for Workstation/WSL.

## 13. Version / forbidden scope

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

Forbidden:
- production plugin source mutation;
- v7 redesign/rerun;
- machine adaptation;
- new Project field/lifecycle;
- machine registry/controller/watcher/daemon/database;
- new Skill/Plugin/Profile;
- Bridge Kit modification;
- successor task.

## 14. Final successful output

MAINTENANCE_BOARD_PROJECT = COMPLETE
ISSUE_4 = CLOSED_COMPLETED
PROJECT_4_STATUS = DONE
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
V6_1_CANONICAL_POLICY = IMPLEMENTED
V7 = COMPLETE
KANBAN_NORMAL_ENTRY = PASS
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO
README_CHECK = <PASS result>
REPOSITORY_BUMP = NONE
PLUGIN_BUMP = NONE
