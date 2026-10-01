# Maintenance Board v7 — Stage B Auto-Add Recovery Critic Prompt v0.4

你是 AI Research Stack 的独立 Critic。

当前只审 Stage B blocker：

DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE

不要重新设计 v7 taxonomy / Forms / Action / hierarchy / audit / v6.1 / Longleaf route。
不要执行 Project workflow mutation，不删除 Project items，不继续 Stage B。

Repository:
YuukiAS/AI_Skills_Collection

Task:
repo--maintenance-board-issue-maturity

Existing task branch:
reviewed/repo--maintenance-board-issue-maturity

Current blocker evidence head:
5f227072be31d36fd96fb59980e856244da11b26

Exact v0.4 recovery package snapshot:
135c5271e31ab9f88fb796332499677a515d0565

Plan:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_PLAN_V0_4_2026-10-01.md

Goal:
docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_GOAL_V0_4.md

Kickoff:
docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_KICKOFF_V0_4.md

Prior v0.3 Critic PASS:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_3_2026-10-01.md
commit:
d665a2bd14737bd38fc38918ca9e6602fe715357

## 必须先读取

latest main:
- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- v7 v0.3 Plan / Goal / Kickoff / Critic review

blocker evidence at current task branch/evidence head:
- results/repo--maintenance-board-issue-maturity/STAGE_B_BLOCKER_HANDOFF.md
- results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_AUTOMATION_READD_BLOCKER.json
- results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_AUTOMATION_READD_CONTINUATION_READBACK.json

exact v0.4 snapshot:
- Plan
- Goal
- Kickoff

## External check required

Independently verify current official GitHub documentation for Project auto-add.

At minimum confirm or refute:

1. built-in auto-add evaluates matching repository items when they are created or updated;
2. auto-add supports is:open and is:issue filters;
3. documented auto-add reason values are completed, reopened and "not planned", not duplicate;
4. auto-add is documented as an add workflow, not a continuous auto-remove reconciler;
5. current official configuration guidance edits the auto-add filter through Project -> Workflows UI;
6. whether a documented public API currently exists for directly updating the built-in auto-add filter body.

Prefer:
- GitHub Docs: Adding items automatically
- GitHub Docs: Filtering projects
- GitHub GraphQL Projects reference

Do not infer unsupported API capability.

## Accepted facts / do not reopen

Current live state already proves:

- G7 PASS;
- v7 functional source integrated to main;
- taxonomy migration completed for all 86 maintenance-track Issues;
- completed Resolution commit repairs preserved;
- exactly 11 duplicate false-DONE audit violations remain:
  #52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72;
- each remains CLOSED / DUPLICATE + maintenance-track;
- each was previously removed and later reappeared in Project after Issue taxonomy updates;
- audit contract remains strict.

Do not reopen taxonomy classification, Forms, Action, hierarchy, v6.1, version policy or machine-consumer architecture.

## Three recovery alternatives

### A — open-only built-in auto-add

Change:

is:issue label:maintenance-track

to:

is:issue is:open label:maintenance-track

Keep maintenance-track on historical duplicate Issues.

### B — remove maintenance-track on non-completion close

Rejected by Planner because it changes the established historical tracking/admission metadata contract to work around the Project filter.

### C — compensating Action/watcher/controller

Rejected because it fights built-in auto-add after the fact and adds race/credential/control-plane complexity.

Critic must compare A/B/C and confirm A is the smallest correct route unless direct evidence contradicts it.

## Review questions

### C1 — root cause

Does the combination of:

- observed removal;
- later taxonomy label updates;
- reappearance of the same closed maintenance-track Issues;
- GitHub auto-add "created or updated" semantics;
- broad filter lacking is:open

support the root-cause conclusion strongly enough for recovery?

Do not require proof of undocumented internal implementation if documented semantics + direct live chronology are sufficient.

### C2 — exact canonical policy

Should current canonical policy change its active auto-add contract to exactly:

is:issue is:open label:maintenance-track

with explicit distinction:

- active open admission;
- historical completed DONE/History already in Project;
- closed non-completion removed and retained outside Project;
- maintenance-track retained as historical tracking metadata;
- reopened tracked Issue becomes eligible again?

Check that this does not create a second lifecycle.

### C3 — completed History

GitHub auto-add is an add workflow, not a documented removal reconciler.

Does narrowing the filter leave already-present completed DONE/History items intact?

Package also requires explicit before/after readback of completed History rather than assuming it.

### C4 — issue-closed -> DONE

v0.4 keeps the existing issue-closed -> DONE workflow unchanged.

Check this remains compatible with canonical semantics because non-completion items are removed from Project and then excluded from re-add by is:open.

### C5 — exact UI mutation

Package targets only the existing enabled Auto-add to project workflow for:

YuukiAS/AI_Skills_Collection

and changes only the filter.

If no documented API for the filter body exists, package allows:

- preferred supported UI-capable GPT/Work surface;
- otherwise one exact HUMAN_ONLY UI handoff;
- Longleaf resumes all later work.

Check this is sufficiently bounded and does not make Workstation recovery a prerequisite.

### C6 — current 11 duplicate repair

After filter readback PASS:

- remove exactly #52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72 once;
- keep CLOSED / DUPLICATE;
- keep maintenance-track;
- keep taxonomy labels;
- no source/tracking/lifecycle edits;
- verify Project absence.

Check this is the truthful minimal repair.

### C7 — update-trigger acceptance

Package uses #52 as a representative sentinel:

- remove existing kind:enhancement;
- restore it immediately;
- final labels equal original;
- state and maintenance-track unchanged;
- after automation settles, #52 and all other duplicates remain out of Project.

This intentionally triggers Issue updates after the new filter.

Judge whether this is a sufficiently direct regression check without reopening Issues or adding a compensating mechanism.

If you prefer a different equally bounded update probe, require only the minimum change and explain why.

### C8 — reopened semantics

Package does not reopen historical Issues for testing.

It freezes the semantic expectation that a truthfully reopened maintenance-track Issue is open again and therefore eligible for auto-add.

Check whether official auto-add/update semantics support this without a destructive live reopen test.

### C9 — rollback

Before mutation:
- old filter/enabled state saved;
- duplicate Project metadata saved.

If workflow mutation fails:
- restore old filter;
- remove no duplicates.

If duplicate cleanup partially fails:
- restore removed duplicates' prior Project fields;
- restore old broad filter;
- verify rollback.

After new filter + all-11 absence + sentinel + full audit PASS:
- recovery becomes committed;
- later unrelated acceptance failure does not roll it back.

Check this avoids partial mixed state.

### C10 — branch/main boundary

Current v7 functional source is already on main.

Package requires:

1. policy amendment prepared on existing task branch;
2. latest-main drift check;
3. external Project filter fix;
4. 11 repair + probe;
5. full audit PASS;
6. only then integrate exact reviewed policy amendment + recovery evidence to latest main.

No replay of G7 or taxonomy migration.

Check this preserves runtime truth before publishing the canonical policy change.

### C11 — remaining Stage B

After recovery, continue only:

- Forms chooser acceptance;
- pre-admission Action smoke;
- search acceptance;
- stale-safety readback;
- README closure;
- Issue #92 Clear-Writing closure evidence;
- Resolution commit;
- close #92 completed;
- Project DONE verification.

No earlier migration/review replay.

### C12 — no new control plane / version

Confirm:

- no bot/daemon/watcher/controller/database;
- no v6.1 implementation;
- no production plugin source change;
- Repository bump NONE;
- all plugins NO_BUMP;
- no production Plugin Capability Gate.

## Output

If REVISE:

RESULT = REVISE
REVIEW_STAGE = STAGE_B_AUTO_ADD_RECOVERY_REVIEW_V0_4
PACKAGE_SNAPSHOT_COMMIT = 135c5271e31ab9f88fb796332499677a515d0565
READY_FOR_CODEX = NO
BLOCKER = <stable blocker id>

Give direct evidence, causal risk and minimum close condition.
Do not reopen accepted v7 architecture without new evidence.

If PASS:

First explain in natural Chinese:

- root cause assessment;
- A/B/C comparison;
- active-admission policy semantics;
- completed History preservation;
- reopened semantics;
- UI-only boundary;
- 11-Issue repair and update probe;
- rollback and main integration boundary;
- what PASS proves and does not prove.

Then output:

RESULT = PASS
REVIEW_STAGE = STAGE_B_AUTO_ADD_RECOVERY_REVIEW_V0_4
PACKAGE_SNAPSHOT_COMMIT = 135c5271e31ab9f88fb796332499677a515d0565
SELECTED_RECOVERY = A_OPEN_ONLY_AUTO_ADD
NEW_BLOCKERS = NONE
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_PLAN_V0_4_2026-10-01.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_GOAL_V0_4.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_KICKOFF_V0_4.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX

Then reproduce the exact reviewed Kickoff from package snapshot.

## Review file authorization

用户发送本 prompt，即授权你只在 latest main 新增：

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_CRITIC_REVIEW_V0_4_2026-10-01.md

并 ordinary non-force push。

除此之外禁止修改 Project workflow / Project items / Issues / labels / canonical policy / .github / scripts / source。
