# AI Skills Maintenance Board — Stage B Auto-Add Recovery Plan v0.4

Date: 2026-10-01
Task: repo--maintenance-board-issue-maturity
Repository: YuukiAS/AI_Skills_Collection
Existing branch: reviewed/repo--maintenance-board-issue-maturity
Primary environment: Longleaf_Codex
Recovery blocker: DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE
Current task evidence head: 5f227072be31d36fd96fb59980e856244da11b26
Status: READY_FOR_INDEPENDENT_CRITIC_REVIEW

## 1. Planner conclusion

Select recovery option A.

Change the Maintenance Project built-in auto-add filter from:

is:issue label:maintenance-track

to:

is:issue is:open label:maintenance-track

Then remove the 11 known CLOSED / DUPLICATE items from the Project one final time
and verify they remain absent.

Do not remove maintenance-track from historical duplicates and do not add a
compensating Action/watcher/controller.

## 2. Root-cause assessment

ROOT_CAUSE = CONFIRMED_FOR_RECOVERY

Direct repository evidence proves:

- all 11 affected Issues remain CLOSED / DUPLICATE;
- all retain maintenance-track;
- the earlier lifecycle repair removed them from the Project;
- taxonomy migration updated Issue labels;
- after those Issue updates, the 11 Issues appeared again in AI Skills
  Maintenance with Status DONE;
- the final audit now fails only on those 11 false-DONE items.

Current GitHub documentation states that Project auto-add evaluates items when
they are created or updated and adds them when they match the configured filter.
The auto-add filter supports is:open and is:issue. Its documented reason values
are completed, reopened and "not planned"; duplicate is not a supported reason
value.

Therefore the current broad filter still matches a closed maintenance-track
Issue after a later Issue update. The observed re-add after taxonomy label
updates is consistent with the documented built-in workflow behavior.

GitHub documents auto-add as an add operation. It does not document it as a
reconciler that removes an already-added item when the item stops matching.
The separate removal/archive behavior belongs to other Project operations.
The recovery must therefore both narrow future admission and remove the current
11 false-DONE items once.

Official references checked:
- GitHub Docs: Adding items automatically
- GitHub Docs: Filtering projects
- GitHub GraphQL Projects reference

## 3. Alternatives

### A. Open-only Project auto-add — SELECTED

Filter:

is:issue is:open label:maintenance-track

Benefits:

- active tracked Issues continue to enter the Project automatically;
- closed duplicate/non-completion Issues no longer match future update-triggered
  auto-add;
- maintenance-track can remain durable historical tracking metadata;
- existing completed DONE/History items are not removed by changing an add-only
  filter;
- a reopened tracked Issue is open again and can match auto-add on the reopened
  update;
- no new bot, Action, daemon, token, database or compensation loop.

### B. Remove maintenance-track from duplicate/non-completion Issues — REJECTED

This would overload maintenance-track with two meanings: formal historical
tracking and current-open admission. It would discard useful searchable
historical tracking metadata and would change the already established
source-to-Issue/history contract merely to work around a Project filter.

### C. Compensating Action/watcher/controller — REJECTED

A background process that repeatedly deletes false-DONE items would fight the
built-in auto-add workflow instead of fixing its admission predicate. It would
add race conditions, Project credentials and a new control plane without user
value.

## 4. Exact canonical policy amendment

Modify only the current canonical policy:

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

Do not rewrite historical Proposals, Goals, Kickoffs or Reviews.

In the admission/false-DONE section, replace the old broad auto-add contract:

is:issue label:maintenance-track

with the exact active-admission contract:

is:issue is:open label:maintenance-track

Add the following normative distinction.

### Active admission

Open tracked Issues are eligible for automatic Project admission:

is:issue is:open label:maintenance-track

maintenance-track remains the formal tracking/admission label.

### Historical completed items

A completed Issue already present in the Project remains DONE/History after
closure. The auto-add workflow is not the mechanism for re-creating completed
History items after they have been removed.

Changing the auto-add filter must not remove existing completed Project items.

### Non-completion closed items

Duplicate / not-planned / rejected / superseded closed Issues must not be
represented as Project DONE.

After truthful non-completion closure they are removed/archived according to the
canonical false-DONE rule and remain out of the Project.

They may retain maintenance-track as historical tracking metadata. Because they
are closed, they no longer match the active-admission auto-add filter.

### Reopened tracked items

If a maintenance-track Issue is later truthfully reopened, it becomes open and
again satisfies the active-admission predicate. The built-in auto-add workflow
may therefore restore it to the Project.

### Closure workflow

The existing issue-closed -> DONE workflow remains unchanged.

The existing rule still requires non-completion items to be removed from the
Project before/at truthful non-completion closure so they do not represent DONE.

No Project Status semantics change.

## 5. Exact Project workflow mutation

Target Project:

owner = YuukiAS
project = AI Skills Maintenance
project number = 5
linked repository = YuukiAS/AI_Skills_Collection

Target the existing enabled built-in Auto-add to project workflow for this
repository.

Before mutation capture durable evidence:

results/repo--maintenance-board-issue-maturity/STAGE_B_AUTO_ADD_PRE_CHANGE.md

Record at least:

- Project identity;
- workflow name/number if exposed;
- enabled state;
- selected repository;
- exact visible current filter;
- readback method/surface.

Expected current filter:

is:issue label:maintenance-track

Change only the filter to:

is:issue is:open label:maintenance-track

Keep:

- same Project;
- same repository;
- workflow enabled;
- issue closed -> DONE workflow unchanged;
- Pull request merged -> DONE unchanged/disabled under BOARD-01;
- no new duplicated auto-add workflow;
- no auto-archive workflow.

After mutation create:

results/repo--maintenance-board-issue-maturity/STAGE_B_AUTO_ADD_POST_CHANGE.md

It must show the exact new filter and enabled state.

## 6. Mutation surface

Prefer a currently supported UI-capable GPT/Work surface to make and read back
the one Project workflow filter change.

Longleaf_Codex continues to own all repository, evidence, GraphQL/API, Issue
migration, audit and search work.

Current official GitHub documentation describes editing the auto-add filter in
the Project Workflows UI. The documented ProjectV2Workflow GraphQL object exposes
workflow identity/enabled metadata but not the filter body, and no documented
filter-update mutation was found in the current public Projects GraphQL
reference checked for this recovery.

Therefore, if no supported UI-capable automation surface is available at
execution time, allow exactly one HUMAN_ONLY UI handoff:

1. Open the AI Skills Maintenance Project.
2. Open the Project menu -> Workflows.
3. Select the existing Auto-add to project workflow.
4. Click Edit.
5. Keep repository YuukiAS/AI_Skills_Collection.
6. Replace the filter with exactly:
   is:issue is:open label:maintenance-track
7. Save and turn on workflow.

After the user confirms that single UI action, the same Goal resumes
automatically. The user must not be asked to perform the duplicate cleanup,
migration, audit or later acceptance work.

Workstation recovery is not a prerequisite.

## 7. Workflow-mutation rollback

The Project workflow change is a small transaction.

Before mutation the exact old filter/enabled state must be captured.

If the new filter cannot be saved or exact UI readback cannot confirm it:

- do not remove any of the 11 duplicate Project items;
- restore the exact previous filter/enabled state if any partial workflow change
  occurred;
- read back the rollback;
- stop.

No canonical policy change is integrated to main while workflow mutation is
unverified.

## 8. Exact 11-Issue repair

Only after the new auto-add filter is visibly confirmed:

Affected Issues:

#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72

For each:

- verify state = CLOSED;
- verify state reason = DUPLICATE;
- verify maintenance-track remains present;
- verify reviewed taxonomy labels remain present;
- remove its current Project item from AI Skills Maintenance;
- do not reopen/re-close;
- do not edit title/body;
- do not change source TODO maturity/evidence/tracking:#N;
- do not change taxonomy classification;
- verify the Issue has no item in AI Skills Maintenance.

Write:

results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_REPAIR_V0_4.json

with before/after Project membership for all 11.

## 9. Verification that closed duplicates stay out

Acceptance requires three layers.

### 9.1 Exact workflow UI readback

The visible filter must be exactly:

is:issue is:open label:maintenance-track

### 9.2 All-11 absence readback

After removing the 11 items and allowing a bounded automation-settling period,
read back all 11 and prove:

- CLOSED / DUPLICATE unchanged;
- maintenance-track retained;
- taxonomy labels retained;
- no AI Skills Maintenance Project item.

### 9.3 Representative update-trigger probe

Use #52 as the sentinel, without changing lifecycle or source truth.

Before the probe snapshot its v7 taxonomy labels.

Generate a real Issue update by temporarily removing and then restoring exactly
one already-reviewed v7 taxonomy label on #52:

kind:enhancement

Then verify:

- final Issue label set exactly equals the pre-probe set;
- Issue remains CLOSED / DUPLICATE;
- maintenance-track never changes;
- after a bounded automation-settling period, #52 remains absent from AI Skills
  Maintenance;
- all other ten duplicates also remain absent.

This directly exercises the same class of Issue-update event that exposed the
bug while leaving final taxonomy unchanged.

If the sentinel is re-added, stop. Do not proceed to audit or invent a
compensating bot.

## 10. Completed History preservation

Before and after the filter mutation, snapshot all currently closed COMPLETED
maintenance-track Project items that are represented as DONE/History.

After the filter change and duplicate cleanup verify:

- the completed items remain in AI Skills Maintenance;
- their Project Status remains DONE;
- existing Resolution commit values remain unchanged;
- no completed History item disappeared merely because the auto-add filter
  became open-only.

The filter change itself must not remove existing Project items.

## 11. Reopened tracked Issue semantics

No historical Issue needs to be reopened for this recovery test.

The canonical contract is:

- a reopened maintenance-track Issue becomes open;
- the auto-add workflow evaluates created/updated items;
- is:open + maintenance-track therefore makes it eligible for automatic
  Project admission again.

Do not reopen one of the historical duplicates merely to prove this point.

## 12. Full audit gate

After the filter fix, 11-item removal and sentinel update probe:

Run the existing deterministic metadata audit unchanged.

Required:

METADATA_AUDIT.ok = true
violation_count = 0

No grandfathering, suppression or audit-rule weakening is authorized.

If the audit still fails, stop before Forms/Action/Search acceptance and return
Planner/Reviewer with exact violations.

## 13. Branch / main integration boundary

Current facts:

- v7 functional source is already integrated to main;
- taxonomy migration is already complete;
- this recovery requires one new canonical-policy amendment only.

Prepare the policy amendment and recovery evidence on the existing task branch:

reviewed/repo--maintenance-board-issue-maturity

Do not replay or re-integrate already published v7 functional source.

Required sequence:

1. independent Critic PASS on this v0.4 recovery package;
2. prepare the exact policy diff on the existing task branch;
3. verify latest-main drift does not conflict;
4. mutate/read back the Project auto-add workflow to the open-only filter;
5. repair/read back the 11 duplicates and run the sentinel update probe;
6. full metadata audit PASS;
7. only then ordinary non-force integrate the exact reviewed policy amendment
   and recovery evidence into latest main;
8. verify remote main contains the policy amendment.

If external recovery fails before step 6, main policy remains unchanged and the
recovery transaction is rolled back where necessary.

After successful policy integration, do not undo the open-only filter merely
because a later unrelated Forms/Action/Search acceptance gate fails.

## 14. Recovery rollback after duplicate removal

If the 11-item repair partially fails before the full recovery readback:

- re-add any already-removed duplicate Issues to the same Project;
- restore their exact pre-recovery Project Area / Status / Resolution values;
- restore the old auto-add filter:
  is:issue label:maintenance-track
- verify the restored pre-recovery state;
- stop.

This rollback returns to the known false-DONE baseline only to avoid a partial
mixed state. It is not a valid completion state; the audit remains blocked.

If rollback itself leaves residual drift, report a hard blocker.

Once the new filter + all-11 removal + sentinel probe + full audit have all
passed, the recovery is committed and should not be rolled back for unrelated
later Stage B acceptance failures.

## 15. Remaining Stage B continuation

After:

- workflow filter readback PASS;
- 11 duplicate absence PASS;
- sentinel update probe PASS;
- completed History preservation PASS;
- full metadata audit PASS;
- policy amendment integrated to main;

resume the existing Stage B remaining gates without replaying earlier work:

1. live Issue Forms chooser acceptance;
2. pre-admission Action smoke;
3. GitHub search usability acceptance;
4. stale-safety check if not already final;
5. README closure;
6. update Issue #92 reader-facing closure evidence with Clear Writing;
7. record Resolution commit;
8. close Issue #92 completed;
9. verify Project DONE.

Do not rerun taxonomy migration or G7 label cutover.

If only the live Issue chooser UI cannot be read from Longleaf, keep the
existing bounded final UI handoff rule. Workstation is not a prerequisite.

## 16. No new control plane

This recovery does not add:

- bot;
- daemon;
- watcher;
- compensating GitHub Action;
- scheduled Project reconciler;
- database/registry;
- new Project field;
- new lifecycle label.

## 17. Version / plugin boundary

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

Reason: this is a Maintenance Board Project workflow/policy repair and does not
change production plugin runtime, package or profile behavior.

## 18. Planner result

DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE = ACCEPTED
SELECTED_RECOVERY = A_OPEN_ONLY_AUTO_ADD
AUTO_ADD_FILTER_BEFORE = is:issue label:maintenance-track
AUTO_ADD_FILTER_AFTER = is:issue is:open label:maintenance-track
MAINTENANCE_TRACK_REMOVED_FROM_DUPLICATES = NO
COMPENSATING_BOT_OR_ACTION = NO
ISSUE_CLOSED_TO_DONE_WORKFLOW_CHANGED = NO
COMPLETED_HISTORY_PRESERVED = YES_REQUIRED
DUPLICATE_REPAIR = REMOVE_ONCE_AFTER_FILTER_CHANGE
AUDIT_CONTRACT_CHANGED = NO
V6_1_IMPLEMENTED = NO
REPOSITORY_BUMP = NONE
ALL_PLUGINS = NO_BUMP
