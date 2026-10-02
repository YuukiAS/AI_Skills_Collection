# AI Skills Maintenance Board — Final Closure Goal v0.2

Repository: YuukiAS/AI_Skills_Collection
Canonical task: repo--maintenance-board-lifecycle
Tracking Issue: #4
Package version: v0.2
Supersedes: v0.1 final-closure package
Approved semantic amendment: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
Approved proposal commit: 515c42623c55f368eb84a1628839459afa909c09
v6.1 Critic result: PASS
Final v7 closure commit: 700234d7e94bb5613f951b8adeb7155d3b15ec3f
Plan: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
Status: READY_FOR_EXECUTION_CRITIC_REVIEW

This Goal is executable only after independent execution-ready Critic PASS and the user sends the approved Kickoff.

## Exact task identity

repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = execution-time latest origin/main
primary_environment = Longleaf_Codex

No successor task.

## Current required set

CURRENT_REQUIRED_SET =
- AI Research Stack ChatGPT Project instructions
- Longleaf_Codex

States:
- AI Research Stack ChatGPT Project instructions = PASS
- Longleaf_Codex = PASS

Not required for Issue #4 current closure:
- CUHK_Workstation_WSL_Codex
- Longleaf_Backup_Codex
- Windows Workstation
- Legion

This is a current product-boundary decision under approved v6.1, not an outage-based PASS/N/A shortcut.

## Required canonical policy implementation

Modify only current normative truth in:

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

§14:
replace fixed-five default with actual normal-entry + explicitly promised fallback selection.

§15:
keep per-current-consumer Maintainer boundary and make aggregate truth quantity-neutral.

§16:
keep generic all-required-consumers closure unchanged.

Do not rewrite historical Proposal/Review/Goal/Kickoff evidence.

## Historical handoff preservation

Keep historical five-consumer evidence in:

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

Append current truth:

CURRENT_REQUIRED_SET
- Project instructions = PASS
- Longleaf_Codex = PASS

CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS
- CUHK_Workstation_WSL_Codex
- Longleaf_Backup_Codex
- Workstation
- Legion

## Final evidence

Create:

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md
results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json
results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md

Required truth:

CURRENT_REQUIRED_SET_FROZEN = YES
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
FINAL_REMAINING_CONSUMER = NONE
ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES

## Implementation sequence

1. create exact branch/worktree;
2. implement v6.1 canonical policy;
3. append current handoff truth;
4. write final evidence;
5. run metadata audit;
6. verify v7 closure commit ancestry;
7. verify #93 current tracking/source backlink;
8. README check;
9. prepare Clear Writing Issue #4 final draft;
10. independent implementation Reviewer PASS;
11. ordinary non-force integrate reviewed changes to latest main;
12. verify remote main;
13. use exact integrated evidence commit as Issue #4 Resolution commit;
14. invoke Clear Writing;
15. update Issue #4 final truth;
16. write Project Resolution commit;
17. close #4 completed;
18. verify Project DONE / Area=repo / exact Resolution commit;
19. run final metadata audit;
20. latest-main and clean-workspace readback.

No machine handoff remains.

## Final Issue #4 truth

Issue #4 must state:

- central Maintenance Board complete;
- v7 complete;
- required-consumer semantics are evidence-backed rather than fixed-five;
- CURRENT_REQUIRED_SET = Project instructions + Longleaf_Codex;
- both PASS;
- WSL / Longleaf_Backup / Windows Workstation / Legion are historical evidence, not current closure prerequisites;
- user manual Kanban maintenance is not required;
- Resolution commit and durable evidence are visible;
- next action = none.

## Normal-use acceptance

Use existing real evidence only:

- #92 completed v7;
- #93 real tracked standalone-skill Issue;
- #94 existing pre-admission smoke;
- latest metadata audit;
- actual Project readback;
- open-only auto-add.

Do not create another synthetic Issue.

## Version / scope

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

Forbidden:
- production plugin source changes;
- v7 redesign/rerun;
- machine adaptation;
- new Project field/lifecycle;
- machine registry/controller/watcher/daemon/database;
- new Skill/Plugin/Profile;
- Bridge Kit mutation;
- successor task.

## Successful final output

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
