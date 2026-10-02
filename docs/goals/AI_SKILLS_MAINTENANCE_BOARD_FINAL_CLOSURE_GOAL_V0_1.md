# AI Skills Maintenance Board — Final Closure Goal v0.1

Repository: YuukiAS/AI_Skills_Collection
Canonical task: repo--maintenance-board-lifecycle
Tracking Issue: #4
Package version: v0.1
Approved semantic amendment: AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
Approved proposal commit: 515c42623c55f368eb84a1628839459afa909c09
v6.1 Critic result: PASS
Final v7 closure commit: 700234d7e94bb5613f951b8adeb7155d3b15ec3f
Implementation Plan:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md
Status: READY_FOR_EXECUTION_CRITIC_REVIEW

This Goal is executable only after independent execution-ready Critic PASS and the user sends the approved Kickoff.

## 1. Exact task identity

repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = execution-time latest origin/main
primary_environment = Longleaf_Codex

No successor task.

## 2. Exact current required set

Freeze:

CURRENT_REQUIRED_SET =
- AI Research Stack ChatGPT Project instructions
- Longleaf_Codex
- CUHK_Workstation_WSL_Codex

Current states:

- AI Research Stack ChatGPT Project instructions = PASS
- Longleaf_Codex = PASS
- CUHK_Workstation_WSL_Codex = PENDING

Not required for Issue #4 current closure:

- Longleaf_Backup_Codex
- Windows Workstation
- Legion

Reason:

- v6.1 requires actual normal-entry consumers / explicit fallback promises, not an inherited machine matrix;
- Project instructions are already user-confirmed installed;
- v7 ran through Longleaf as the real board execution environment and completed the normal Project/source/audit path;
- latest main still contains actual normal-entry work using /home/yuukias/AI_Skills_Collection, mapped by the historical handoff to CUHK_Workstation_WSL_Codex;
- no current board contract explicitly promises Longleaf_Backup, Windows Workstation or Legion as normal/fallback entries.

FINAL_REMAINING_CONSUMER = CUHK_Workstation_WSL_Codex

## 3. Canonical policy target

Implement approved v6.1 only in current normative policy:

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

Required:

- §14: replace fixed-five required set with evidence-backed actual normal-entry / explicitly promised fallback selection;
- §15: keep per-current-consumer Maintainer boundary and replace fixed-five aggregate wording with quantity-neutral required-consumer aggregate truth;
- §16: keep generic all-required-consumers closure unchanged;
- converge any other current normative fixed-five sentence in the same canonical file if it directly contradicts v6.1;
- leave historical design/review/execution artifacts unchanged.

Do not redesign v7 or Project lifecycle.

## 4. Historical handoff preservation

Keep the full existing history in:

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

Append current truth with explicit separation:

HISTORICAL_HANDOFF_MATRIX
CURRENT_REQUIRED_SET
CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS

Current section must record direct evidence for each set member and status.

## 5. Final closure evidence

Create:

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md
results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json
results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md

Before WSL PASS:

CURRENT_REQUIRED_SET_FROZEN = YES
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
CUHK_WORKSTATION_WSL_CODEX = PENDING
ALL_REQUIRED_CONSUMERS = NOT_YET_PASS_OR_NA
ISSUE_4_STATUS = ADAPTING

## 6. Longleaf stage

After Critic PASS and user Kickoff:

1. create exact branch/worktree from latest main;
2. implement canonical v6.1 policy change;
3. append current handoff truth;
4. write required-set evidence;
5. prepare the approved final WSL prompt;
6. run current metadata audit and board integrity readback;
7. README check;
8. prepare Clear Writing Issue #4 current-truth draft;
9. independent implementation Reviewer PASS;
10. ordinary non-force integrate repo changes to main;
11. verify remote main;
12. apply Clear Writing Issue #4 update;
13. keep Issue #4 open, Project ADAPTING / repo;
14. read back current truth.

Do not wait for WSL before completing these steps.

## 7. Longleaf PASS proof

No Longleaf rerun is required if latest evidence remains current:

- Issue #92 records v7 execution on Longleaf;
- v7 closure commit 700234d7e94bb5613f951b8adeb7155d3b15ec3f;
- V7_FINAL_CLOSURE = COMPLETE;
- metadata audit = PASS / zero violations;
- #93 is real Project DOING / standalone-skill with canonical backlinks;
- #94 proved pre-admission behavior.

Contradiction -> stop Planner/Reviewer, do not silently retain PASS.

## 8. Final WSL one-shot

Approved prompt path:

docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_REMAINING_CONSUMER_CUHK_WSL_V0_1.md

The user sends it once after the Workstation/WSL environment returns.

The action must:

- verify /home/yuukias/AI_Skills_Collection and latest main;
- verify canonical v6.1 policy already on main;
- verify current handoff says only WSL is pending;
- run one fresh ordinary read-only Codex normal-entry smoke against latest repo;
- prove the fresh entry consumes the board contract;
- write durable WSL PASS evidence;
- update current consumer aggregate to all PASS;
- integrate final evidence to main;
- run final metadata/board/README checks;
- use the final evidence commit as Issue #4 Resolution commit;
- invoke Clear Writing;
- update and close Issue #4 completed;
- verify Project #4 DONE / repo / exact Resolution commit;
- verify latest main and clean workspace.

It must not rerun Longleaf or v7.

## 9. WSL evidence files

Required:

results/repo--maintenance-board-lifecycle/FINAL_CONSUMER_CUHK_WORKSTATION_WSL_CODEX_2026-10-02.md
results/repo--maintenance-board-lifecycle/FINAL_CONSUMER_CUHK_WORKSTATION_WSL_CODEX_2026-10-02.json

Required truth:

CONSUMER = CUHK_Workstation_WSL_Codex
STATUS = PASS
NORMAL_ENTRY_CONSUMED_BOARD_CONTRACT = YES
LATEST_MAIN = <exact SHA>
FRESH_SESSION = <identity>
REQUIRED_SET_MATCH = YES

No AI Skills Maintainer machine-update campaign is required merely for this closure.

## 10. Final Issue #4 truth

Final copy must state:

- central Maintenance Board complete;
- v7 complete;
- required-consumer contract is evidence-backed, not fixed-five;
- CURRENT_REQUIRED_SET contains exactly Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex;
- all required consumers PASS;
- Longleaf_Backup / Windows Workstation / Legion are historical handoff/machine-update evidence, not current prerequisites;
- normal Kanban entry works without user card dragging;
- final Resolution commit and evidence are visible.

Clear Writing is mandatory before reader-facing mutation.

## 11. Final board integrity

Before close:

- current policy §§14–16 match approved v6.1;
- v7 closure commit is in latest-main ancestry;
- auto-add remains is:issue is:open label:maintenance-track;
- metadata audit zero violations;
- #93 remains correctly tracked;
- duplicates/non-completion are not false-DONE;
- all current required consumers PASS/N/A;
- README check complete;
- repository/plugin versions unchanged;
- no production plugin source changes.

## 12. Failure boundary

If WSL is still unavailable:
- leave Issue #4 ADAPTING;
- do not undo Longleaf-side policy/current-truth work;
- wait only for the one frozen WSL handoff.

If WSL fresh normal entry does not consume latest contract:
- WSL remains pending;
- no Issue #4 close.

If latest current evidence changes the required-set contract:
- stop before closure;
- return Planner/Critic.

No user manual Kanban mutation is permitted.

## 13. Version / non-goals

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

Forbidden:
- production plugin source changes;
- v7 redesign/replay;
- new lifecycle/Project fields;
- machine registry/controller/watcher/daemon/database;
- new skill/plugin/profile;
- Bridge Kit mutation;
- successor task.

## 14. Successful final output

MAINTENANCE_BOARD_PROJECT = COMPLETE
ISSUE_4 = CLOSED_COMPLETED
PROJECT_4_STATUS = DONE
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
V6_1_CANONICAL_POLICY = IMPLEMENTED
V7 = COMPLETE
KANBAN_NORMAL_ENTRY = PASS
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO
README_CHECK = <PASS result>
REPOSITORY_BUMP = NONE
PLUGIN_BUMP = NONE
