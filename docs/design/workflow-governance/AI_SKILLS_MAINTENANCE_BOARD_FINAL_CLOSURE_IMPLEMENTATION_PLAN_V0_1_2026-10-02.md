# AI Skills Maintenance Board — Final Closure Implementation Plan v0.1

Date: 2026-10-02
Repository: YuukiAS/AI_Skills_Collection
Canonical task: repo--maintenance-board-lifecycle
Tracking Issue: #4
Package version: v0.1
Planner baseline: main@700234d7e94bb5613f951b8adeb7155d3b15ec3f
Final v7 closure commit: 700234d7e94bb5613f951b8adeb7155d3b15ec3f
Approved v6.1 Proposal: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
Approved v6.1 Proposal commit: 515c42623c55f368eb84a1628839459afa909c09
Approved v6.1 Critic review: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md
v6.1 Critic result: PASS
Status: READY_FOR_EXECUTION_CRITIC_REVIEW
This Plan does not authorize execution.

## 1. Final product target

This is the last governance closure task for the Maintenance Board.

v7 has already proved the normal daily path:

- open-only maintenance-track Project admission;
- searchable Issue taxonomy;
- Issue Forms intake;
- bounded pre-admission Action;
- canonical source tracking:#N integrity;
- duplicate false-DONE repair;
- metadata audit PASS;
- search acceptance PASS;
- stale-safety PASS;
- real Issue #93 entered the board and its source backlink was repaired;
- users do not need to drag Project cards manually.

This final task does not redesign v7. It only:

1. implements the already-approved v6.1 required-consumer semantics in the current canonical board policy;
2. replaces stale Issue #4 five-machine truth with the current evidence-backed required set;
3. preserves historical consumer handoff evidence while adding current truth;
4. verifies the one remaining current required consumer;
5. closes Issue #4 and the Maintenance Board project truthfully.

## 2. Exact execution identity

Longleaf stage uses the existing canonical task identity:

repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = execution-time latest origin/main
primary_environment = Longleaf_Codex

At package preparation time, the remote reviewed/repo--maintenance-board-lifecycle branch is absent. The future approved Kickoff may create that exact branch from execution-time latest origin/main; this is not a successor task.

The relative worktree is resolved once from the current canonical checkout and recorded before mutation. No /tmp, alternate branch/worktree, dirty checkout, force push or history rewrite is authorized.

The final WSL consumer handoff reuses the same task branch after the Longleaf stage has integrated once. On WSL the current canonical checkout evidenced by latest main is:

/home/yuukias/AI_Skills_Collection

and the exact WSL worktree is:

/home/yuukias/AI_Skills_Collection-repo--maintenance-board-lifecycle

## 3. Current evidence-backed required set

Freeze:

CURRENT_REQUIRED_SET =
- AI Research Stack ChatGPT Project instructions
- Longleaf_Codex
- CUHK_Workstation_WSL_Codex

Current status:

| Consumer / normal entry | Status | Direct evidence |
| --- | --- | --- |
| AI Research Stack ChatGPT Project instructions | PASS | results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md records user-confirmed semantic installation of the board trigger and no-manual-Kanban contract. |
| Longleaf_Codex | PASS | v7 execution explicitly used Longleaf_Codex as primary environment; Issue #92 records Stage A on Longleaf; V7_FINAL_CLOSURE.md proves the resulting real Project/Issue/source/audit path completed, including #93 source backlink repair and METADATA_AUDIT violation_count=0. |
| CUHK_Workstation_WSL_Codex | PENDING | historical handoff maps this consumer to /home/yuukias/AI_Skills_Collection; latest main still contains real normal-entry workflow evidence using that canonical checkout in results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md. Therefore WSL remains a current real repo normal-entry environment, not merely an installed machine. It has not yet freshly consumed the latest post-v7 board contract. |

### 3.1 Why WSL remains required

This is not retention merely because an old five-machine list named WSL.

Latest current evidence shows actual AI_Skills normal-entry work using the WSL canonical checkout /home/yuukias/AI_Skills_Collection, and CONSUMER_HANDOFFS.md identifies that path as CUHK_Workstation_WSL_Codex.

Therefore the current completion claim still includes WSL as a real normal-entry consumer.

The outage does not make it PASS or N/A. It leaves exactly one bounded pending consumer.

### 3.2 Why the other historical machines are not required

The following are historical handoff / machine-update evidence, not current Issue #4 closure prerequisites:

- Longleaf_Backup_Codex;
- Windows Workstation;
- Legion.

No current Maintenance Board contract directly promises these as normal-entry or fallback environments. Their presence in the older five-machine handoff or in the independent AI Skills Maintainer machine-update matrix is insufficient under approved v6.1 semantics.

No explicit fallback promise was found for Longleaf_Backup_Codex; the display name “Backup” is not a product contract.

Thus:

CURRENT_REQUIRED_MACHINE_CONSUMERS =
- Longleaf_Codex
- CUHK_Workstation_WSL_Codex

FINAL_REMAINING_CONSUMER = CUHK_Workstation_WSL_Codex

## 4. Canonical policy implementation

Modify only current normative truth in:

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

Historical Proposals / Reviews / Goals / Kickoffs remain unchanged.

### 4.1 §14

Remove the global fixed-five default.

Replace it with the approved v6.1 contract:

- for machine-consumed workflow/shared maintenance mechanisms, required consumers are the actual normal-entry consumers and explicitly promised fallback environments necessary for the tracked item’s frozen completion claim;
- a machine is not required merely because AI Skills Maintainer is installed, because it appeared in another product’s machine-update matrix, because it has Codex, or because it can clone the repo;
- fallback is required only when explicitly promised by the tracked product contract;
- at ADAPTING cutover, freeze the evidence-backed required set and exact locators;
- ambiguity keeps the item ADAPTING and returns Planner;
- do not add environments “for safety” and do not omit explicitly promised environments;
- future optional environments do not retroactively enlarge a valid frozen DONE contract.

Per-consumer evidence remains the existing generic evidence contract.

### 4.2 §15

Keep:

- AI Skills Maintainer is a per-current-consumer executor;
- it is not a cross-machine controller;
- it is not a machine registry owner;
- it is not a credential broker.

Replace the fixed-five aggregate sentence with quantity-neutral truth:

当前 tracked item 的 required-consumer 聚合真值属于 tracking Issue / Project lifecycle。

### 4.3 §16

Keep current generic final-DONE rule unchanged:

all required consumers PASS/N/A
+ durable evidence
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE

Search the current canonical policy for any additional normative fixed-five sentence that contradicts §§14–16 and make only the quantity-neutral convergence needed by v6.1. Do not rewrite unrelated v7, lifecycle, intake, taxonomy or BOARD-01 rules.

## 5. Historical vs current consumer evidence

Keep:

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

Do not delete or rewrite the existing five-consumer handoff matrix.

Append a clearly labeled current section:

CURRENT_REQUIRED_SET — 2026-10-02

It must explicitly distinguish:

HISTORICAL_HANDOFF_MATRIX

The existing five-consumer material remains historical evidence of the previous contract and prior discovery state.

CURRENT_REQUIRED_SET

AI Research Stack ChatGPT Project instructions = PASS
Longleaf_Codex = PASS
CUHK_Workstation_WSL_Codex = PENDING

CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS

Longleaf_Backup_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Workstation = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Legion = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT

The section must link the direct evidence used to freeze each decision.

## 6. New final-closure evidence

Create under results/repo--maintenance-board-lifecycle/ at least:

FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md
FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json
FINAL_CLOSURE_STATUS_2026-10-02.md

The required-set evidence records:

- current latest main;
- approved v6.1 Proposal/review locators;
- v7 closure commit;
- evidence table from §3;
- CURRENT_REQUIRED_SET;
- PASS / PENDING;
- absence of explicit fallback promise for excluded historical consumers;
- exact remaining consumer.

Before the WSL handoff:

CURRENT_REQUIRED_SET_FROZEN = YES
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
CUHK_WORKSTATION_WSL_CODEX = PENDING
ALL_REQUIRED_CONSUMERS = NOT_YET_PASS_OR_NA
ISSUE_4_STATUS = ADAPTING
FINAL_REMAINING_CONSUMER = CUHK_Workstation_WSL_Codex

## 7. Longleaf implementation stage

After execution-ready Critic PASS and user Kickoff:

### 7.1 Source/repo work

On Longleaf:

1. create/reuse exact task branch/worktree from latest main;
2. implement only:
   - canonical policy v6.1 convergence;
   - CONSUMER_HANDOFFS.md current-truth section;
   - final required-set evidence;
3. run git diff --check;
4. run the existing Maintenance Board metadata audit against latest live state;
5. README closure check;
6. verify no production plugin source/version/profile/Marketplace changes.

### 7.2 Independent implementation review

Before main integration, an independent Reviewer must inspect:

- exact canonical policy §§14–16 diff;
- no historical artifact rewrite;
- current required-set evidence;
- WSL-required conclusion and direct evidence;
- excluded historical consumer reasoning;
- CONSUMER_HANDOFFS.md history preservation;
- final WSL prompt;
- Issue #4 proposed current-truth draft;
- version / README decision.

Required result:

FINAL_CLOSURE_IMPLEMENTATION_REVIEW = PASS
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex
FINAL_REMAINING_CONSUMER = CUHK_Workstation_WSL_Codex
MAIN_INTEGRATION_AUTHORIZED = YES

### 7.3 Main integration and current Issue #4 truth

After Reviewer PASS:

1. ordinary non-force integrate reviewed repo changes to latest main;
2. verify remote main;
3. invoke Clear Writing before modifying Issue #4 reader-facing copy;
4. update Issue #4 current truth to state:
   - central implementation complete;
   - v7 complete;
   - canonical required-consumer semantics now evidence-backed;
   - current exact required set;
   - Project instructions PASS;
   - Longleaf PASS;
   - WSL is the only pending consumer;
   - Longleaf_Backup / Workstation / Legion are historical handoff evidence, not current closure prerequisites;
   - next action is exactly the frozen WSL one-shot handoff;
5. keep Project #4 Status = ADAPTING, Area = repo, Issue open;
6. read back Issue #4 and Project state.

Do not wait for WSL before performing these Longleaf-side actions.

## 8. Longleaf PASS evidence

No new Longleaf machine adaptation is required.

The final implementation may freeze Longleaf_Codex = PASS from existing direct v7 evidence only if execution-time readback confirms these artifacts remain current and uncontradicted:

- Issue #92 records v7 execution on Longleaf;
- v7 final closure commit is 700234d7e94bb5613f951b8adeb7155d3b15ec3f;
- V7_FINAL_CLOSURE.md reports complete real board behavior;
- latest METADATA_AUDIT.json is ok=true, violation_count=0;
- #93 is a real tracked Issue with Project DOING / standalone-skill and canonical source backlinks;
- #94 proved pre-admission behavior without entering the Project.

If execution-time evidence contradicts this, stop Planner/Reviewer rather than rerun v7 automatically.

## 9. Final remaining WSL handoff

Because WSL remains a current normal-entry consumer, the package includes an exact one-shot prompt:

docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_REMAINING_CONSUMER_CUHK_WSL_V0_1.md

The user should send it once after the Workstation/WSL environment is available.

It must not require another design decision.

### 9.1 Preconditions

The WSL action must verify:

- canonical checkout: /home/yuukias/AI_Skills_Collection;
- latest origin/main;
- latest main includes implemented v6.1 §§14–16 semantics;
- CONSUMER_HANDOFFS.md current section says only WSL remains pending;
- Issue #4 is open / ADAPTING;
- v7 remains complete;
- Longleaf and Project-instructions PASS evidence is already durable.

If any precondition is false, stop with exact drift; do not rerun Longleaf/v7.

### 9.2 Normal-entry consumption verification

The WSL action must verify a fresh ordinary Codex repo entry consumes the current Maintenance Board contract.

Preferred bounded smoke:

- from the current WSL AI_Skills_Collection environment, run one fresh read-only codex exec;
- request it to read the repository normal-entry instructions and current board policy and report:
  - active auto-add predicate;
  - evidence-backed required-consumer selection rule;
  - current Issue #4 remaining-consumer truth;
- do not allow that smoke to mutate repo or GitHub state.

PASS requires the fresh process to consume latest current repo policy, not an old installed snapshot or machine-update matrix.

Record session/request/output identity in durable evidence.

### 9.3 WSL consumer evidence

Create:

results/repo--maintenance-board-lifecycle/FINAL_CONSUMER_CUHK_WORKSTATION_WSL_CODEX_2026-10-02.md
results/repo--maintenance-board-lifecycle/FINAL_CONSUMER_CUHK_WORKSTATION_WSL_CODEX_2026-10-02.json

Required:

CONSUMER = CUHK_Workstation_WSL_Codex
STATUS = PASS
LATEST_MAIN = <exact SHA>
NORMAL_ENTRY_CONSUMED_BOARD_CONTRACT = YES
FRESH_SESSION = <identity>
REQUIRED_SET_MATCH = YES

No AI Skills machine-update rerun is required merely for this board closure.

### 9.4 Same-task branch continuation

Reuse reviewed/repo--maintenance-board-lifecycle.

On WSL:

1. fetch latest main and the existing task branch;
2. ensure the task branch is an ancestor/compatible continuation of main;
3. fast-forward the task branch to latest main when legal;
4. materialize exact WSL worktree /home/yuukias/AI_Skills_Collection-repo--maintenance-board-lifecycle;
5. add only final consumer / closure evidence and current handoff status;
6. ordinary non-force push;
7. ordinary non-force integrate final closure evidence to main;
8. verify remote main.

No successor task is created.

## 10. Automatic aggregate closure after WSL PASS

After WSL evidence is integrated to main, the same WSL action must complete Issue #4 aggregate closure without rerunning Longleaf or v7.

Required sequence:

1. update the current section of CONSUMER_HANDOFFS.md: Project instructions PASS; Longleaf PASS; WSL PASS; all required consumers PASS;
2. update FINAL_CLOSURE_STATUS_2026-10-02.md;
3. run existing Maintenance Board metadata audit;
4. verify Issue #4 open / ADAPTING before final close, Project Area = repo, labels correct, v7 normal-entry evidence still valid;
5. README check;
6. commit and integrate the final aggregate evidence to main;
7. use that exact integrated evidence commit as Resolution commit;
8. invoke Clear Writing;
9. update Issue #4 final reader-facing copy;
10. write Project Resolution commit;
11. close Issue #4 with state reason completed;
12. verify issue-closed workflow yields Project Status DONE;
13. verify Issue #4 remains in Project History with Area=repo and exact Resolution commit;
14. final latest-main readback;
15. verify task workspace clean.

No further Planner or design judgment is required if all frozen preconditions hold.

## 11. Final Issue #4 copy contract

Before final close, Issue #4 must clearly say:

- Maintenance Board central implementation is complete;
- v7 Issue maturity is complete;
- current canonical consumer semantics are evidence-backed, not fixed-five;
- CURRENT_REQUIRED_SET is AI Research Stack ChatGPT Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex;
- all three are PASS;
- Longleaf_Backup_Codex, Windows Workstation, and Legion are historical handoff/machine-update evidence, not current closure prerequisites;
- users do not manually maintain Kanban;
- final Resolution commit and durable evidence locators are visible.

Do not delete history; replace stale current-progress/next-action prose with current truth after Clear Writing.

## 12. Final normal-use acceptance

Do not create new synthetic Issues.

Use existing real evidence:

- #92 v7 completed;
- #93 real standalone-skill tracking Issue with Project Status DOING, Project Area standalone-skill, canonical source backlinks;
- #94 existing pre-admission smoke only as historical acceptance evidence;
- latest metadata audit PASS;
- actual Project readback;
- open-only auto-add current contract.

Final product claim:

real project feedback
-> canonical TODO
-> tracking:#N when admitted
-> GitHub Issue + Project
-> Project lifecycle / Area
-> Planner/Critic/Maintainer/Codex proactive sync
-> truthful DONE/non-completion handling

This does not mean a bot guesses lifecycle. It means normal maintenance roles and built-in GitHub admission/closure automation keep the existing sources of truth synchronized.

## 13. Final integrity gate

Immediately before closing Issue #4 verify:

- canonical policy §§14–16 are the approved v6.1 semantics;
- v7 closure commit exists in latest-main ancestry;
- Project auto-add is open-only;
- metadata audit passes with zero violations;
- #93 remains correctly tracked;
- duplicate/non-completion Issues are not false-DONE;
- Issue #4 current required set matches this Plan;
- all current required consumers are PASS/N/A;
- README check complete;
- no unrelated repo changes;
- no production plugin source changes;
- repository/plugin versions unchanged.

## 14. Failure recovery

Longleaf stage:
- current main conflicts with v6.1 amendment -> stop and return Planner/Critic;
- new direct evidence changes the required-set determination -> stop; do not close #4;
- implementation Reviewer REVISE -> repair within this package and re-review;
- Project mutation surface unavailable -> preserve exact pending mutation; do not ask user to drag Kanban.

WSL stage:
- WSL unavailable -> remain ADAPTING; all Longleaf work stays valid;
- latest main / required-set preconditions mismatch -> stop with exact drift;
- fresh normal entry fails to consume latest board contract -> WSL remains pending; no aggregate close;
- GitHub Project write permission missing -> report exact bounded blocker; do not claim closure;
- metadata audit fails -> no close;
- Resolution commit cannot be read back -> no close;
- issue-close does not produce Project DONE -> report exact Project inconsistency; do not fabricate completion.

Do not rerun Longleaf/v7 merely because WSL was temporarily unavailable.

## 15. Version and prohibited scope

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

Forbidden:

- production plugin source mutation;
- v7 redesign;
- new lifecycle/Project field;
- machine registry;
- cross-machine controller;
- watcher/daemon/scheduled reconciler/database;
- new Skill/Plugin/Profile;
- Bridge Kit modification;
- successor task.

## 16. Final required output after successful closure

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
