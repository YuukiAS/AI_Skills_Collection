# AI Skills Maintenance Board — Issue Maturity v7 Execution-ready Critic Review v0.1

- Date: 2026-10-01
- Review stage: `EXECUTION_READY_REVIEW_V7_V0_1`
- Result: `REVISE`
- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: repository maintenance / plugin refinement workflow
- design_topic_or_task_key: `repo--maintenance-board-issue-maturity`
- human_label: Maintenance Board Issues 成熟化
- package_snapshot_commit: `ab4967abd6d8f1c3323b9c8074fdbe606eb083c9`
- approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`
- approved design commit: `3d091421c7afe8d4f90687ef6e0ce2686bcaf426`
- reviewed Plan: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_1_2026-10-01.md`
- reviewed Goal: `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_1.md`
- reviewed Kickoff: `docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_1.md`

## 1. Overall assessment

The v0.1 package is directionally sound and preserves the approved v7 architecture.

Accepted without reopening:

- `kind:* / scope:* / area:*` are searchable taxonomy only, not a second lifecycle;
- canonical TODO remains problem/evidence/maturity + `tracking: #N`;
- Project Status remains the only lifecycle and Project Area remains the primary owner;
- two Issue Forms plus the blank route are proportionate;
- the tiny pre-admission Action closes the intentional blank/API intake gap without becoming a triage bot;
- `issues: opened` plus `issues: write` is the correct narrow permission shape for adding an existing triage label;
- migration classification is frozen and independently reviewed before live taxonomy mutation;
- ambiguous `kind` fails closed before any Issue-label migration;
- the audit helper is read-only and does not become a reconciler/state machine;
- native sub-issues/dependencies are used narrowly;
- stale auto-close, custom triagebot, PR path labeler, CODEOWNERS, Dependabot and scheduled Project audit remain correctly deferred;
- v6.1 remains independent;
- repository/plugin version decisions remain `NONE / NO_BUMP`, with direct Action safety/live acceptance replacing an irrelevant production Plugin Capability Gate.

Current repo inspection also confirms no existing `.github/ISSUE_TEMPLATE` directory and no current workflow path collision with `.github/workflows/maintenance-board-intake.yml`.

Representative live Issues #4, #5, #35, #63 and #86 currently carry only `maintenance-track`, so the proposed taxonomy migration addresses a real GitHub Issues usability gap.

However, the package has one execution blocker in the label/Form/Action cutover order and rollback evidence.

## 2. Stable blocker

### BOARD-V7-LABEL-CUTOVER-01 — publish labels before Forms/Action, and preserve pre-existing label definitions for rollback

**Requirement**

The live intake path must never be published in a state where its required labels do not yet exist. Any label-definition reconciliation must also be reversible.

**Direct evidence**

The v0.1 Plan §13 / Goal §12 / Kickoff Stage B currently sequence:

1. integrate reviewed branch to `main`;
2. verify remote `main`;
3. create/reconcile exact v7 label definitions;
4. migrate Issues;
5. run live Forms/Action acceptance.

But the reviewed branch contains both Issue Forms and `.github/workflows/maintenance-board-intake.yml`.

GitHub's current official Issue Forms documentation states that a form's default label is only added if that label already exists in the repository:

https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms

GitHub's current official issue-labeling workflow example likewise uses `issues: write` with `gh issue edit --add-label` and explicitly states that the target label must already exist:

https://docs.github.com/en/actions/tutorials/manage-your-work/add-labels-to-issues

Therefore, once the reviewed branch lands on default `main`, the new Forms and intake Action become live before `triage:needed` and `kind:new-capability` are guaranteed to exist. A human/API Issue opened in that publication window can lose the form default labels and/or make the Action fail.

The same package authorizes reconciliation of same-named compatible labels with exact colors/descriptions, but `ROLLBACK_SNAPSHOT.md` currently records Issue label membership and only the names of labels created/reconciled. It does not freeze the pre-v7 existence/color/description of any same-named label that may be reconciled. If such a label pre-exists and is changed, the rollback contract cannot restore its prior definition reliably.

**Causal risk**

This creates two concrete failure modes:

1. the normal intake path can be temporarily broken at the exact moment v7 is published, contradicting the purpose of the maturity upgrade;
2. rollback can delete or fail to restore a pre-existing compatible label definition after a `--force` reconcile.

Both are avoidable with a small ordering/evidence correction and do not require architecture changes.

**Minimum close condition**

Revise Plan / Goal / Kickoff only as follows:

1. keep Stage A unchanged: no live v7 taxonomy label mutation before independent implementation Reviewer PASS;
2. after Reviewer PASS and latest-main drift check, but **before publishing the Forms/Action to default main**, snapshot the repository-level definitions for every exact v7 label:
   - whether it exists;
   - current color;
   - current description;
3. fail closed on incompatible same-name semantics exactly as already specified;
4. create/reconcile the exact v7 labels before integrating the branch that publishes the Forms/Action;
5. if label creation/reconciliation fails, do not integrate the Forms/Action;
6. then integrate the reviewed branch to main, verify remote main, migrate existing tracked Issues, and run live acceptance;
7. rollback must:
   - delete only labels that v7 created from absence;
   - restore prior color/description for labels that existed before v7 and were reconciled;
   - never alter `maintenance-track`;
8. update G7 / Stage B wording consistently in Plan, Goal and Kickoff.

No redesign of taxonomy, Forms, Action logic, migration classification, audit, hierarchy, v6.1 independence or version policy is required.

## 3. Other execution checks

### Taxonomy and source of truth

PASS.

No lifecycle or maturity labels are introduced. `area:*` is explicitly a search mirror and Project Area wins on drift. This avoids a second owner/lifecycle source.

### Forms and tiny Action

PASS subject to BOARD-V7-LABEL-CUTOVER-01.

The Action has real value because blank and programmatic Issue creation remain intentionally supported. It only guarantees pre-admission visibility and does not classify/admit/close.

The proposed `issues: opened` + `issues: write` boundary matches GitHub's own supported pattern for `gh issue edit --add-label`. No checkout, body execution, repo secrets or broader token permission is needed.

### Migration / ambiguity / independent review

PASS.

The complete migration table and pre-migration snapshot exist before any existing-Issue taxonomy mutation, and independent Reviewer review is mandatory. Genuine ambiguity stops the whole taxonomy migration before partial mutation. That is appropriately fail-closed for a one-time semantic backfill.

### Audit

PASS.

The helper is specified as read-only, returns machine-readable evidence, exits non-zero on violations, and has no scheduled mutation/reconciliation path. It is an audit, not a hidden state machine.

### Live acceptance

PASS after the cutover-order repair.

Live chooser visibility, a real non-tracked intake Issue, real Action run/readback, real search results, live metadata audit and stale-safety check prove actual GitHub behavior instead of config existence.

### v6.1 independence

PASS.

v7 does not implement or alter §§14–16 required-consumer semantics. Semantic overlap returns Planner/Critic rather than silently merging the two tasks.

### Version / Gate

PASS.

The task changes repository maintenance metadata, GitHub contributor intake configuration, a bounded repo Action and read-only audit tooling. It does not alter production plugin runtime/package/profile behavior, so `Repository bump = NONE`, all plugins `NO_BUMP`, and no production Plugin Capability Gate Matrix are appropriate.

### Branch / worktree / mutation authority

PASS.

The exact reviewed branch/worktree and GitHub mutation envelope are bounded. Existing maintenance Issue state, Project Status/Area, TODO maturity/evidence and `tracking:#N` are outside taxonomy migration authority.

## 4. Current execution-environment note

The user's current workstation outage does not create a v7 architecture blocker.

v7 is repository/GitHub governance work and does not require Maintenance Board machine-consumer adaptation. The package can be executed from the current `Longleaf_Codex` environment provided its GitHub/Project credentials pass the normal preflight.

Do not wait for `Workstation` or `CUHK_Workstation_WSL_Codex` for Stage A, classification, Reviewer handoff, label migration, Action smoke, metadata audit or GitHub search.

The only potentially UI-specific acceptance is the live Issue chooser readback. If `Longleaf_Codex` cannot provide a supported live chooser readback after all other gates are complete, isolate that as one final bounded acceptance handoff; do not replay the migration or make workstation recovery a prerequisite for the rest of v7.

This is an execution-routing clarification from the user's current instruction, not a new consumer/adaptation requirement.

## 5. Final fields

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V7_V0_1
PACKAGE_SNAPSHOT_COMMIT = ab4967abd6d8f1c3323b9c8074fdbe606eb083c9
READY_FOR_CODEX = NO
STABLE_BLOCKERS = BOARD-V7-LABEL-CUTOVER-01
NEXT_HANDOFF = PLANNER
```

## 6. Planner repair prompt

```text
你现在只返修 AI Skills Maintenance Board Issue Maturity v7 execution package v0.1 的唯一 stable blocker。

Repository:
YuukiAS/AI_Skills_Collection

Task:
repo--maintenance-board-issue-maturity

Review stage:
EXECUTION_PACKAGE_REVISION

Reviewed package snapshot:
ab4967abd6d8f1c3323b9c8074fdbe606eb083c9

Approved design:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
commit:
3d091421c7afe8d4f90687ef6e0ce2686bcaf426

Reviewed Plan:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_1_2026-10-01.md

Reviewed Goal:
docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_1.md

Reviewed Kickoff:
docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_1.md

Critic review:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-01.md

Stable blocker:
BOARD-V7-LABEL-CUTOVER-01

已接受、不重新设计：

- kind/scope/area taxonomy 与 source-of-truth split；
- 两个 Issue Forms + blank route；
- tiny pre-admission Action；
- issues:opened + issues:write；
- migration classification before live mutation；
- ambiguous kind fail closed；
- read-only metadata audit；
- native sub-issues/dependencies only；
- live Forms/Action/search/audit acceptance；
- stale auto-close forbidden；
- v6.1 independence；
- Repository bump NONE / all plugins NO_BUMP / no production Plugin Capability Gate；
- exact branch/worktree 与现有 GitHub mutation scope。

只修 label cutover / rollback：

1. Stage A仍禁止live v7 taxonomy label mutation，必须等independent implementation Reviewer PASS。
2. Reviewer PASS + latest-main drift check 后，在发布 Forms/Action 到 default main 之前：
   - snapshot每个exact v7 label的repo-level current definition：
     existence / color / description；
   - incompatible same-name semantics -> fail closed；
   - create/reconcile exact v7 labels。
3. 任何label create/reconcile失败 -> 不得integrate Forms/Action。
4. labels ready后才ordinary non-force integrate reviewed branch到main。
5. 然后才：
   - verify remote main；
   - apply reviewed classification；
   - live audit；
   - live Forms/Action/search acceptance；
   - closure。
6. rollback：
   - v7前不存在的label才能删除；
   - v7前已存在且被reconcile的label恢复原color/description；
   - maintenance-track永不改变。
7. Plan / Goal / Kickoff / G7 / failure-recovery措辞必须一致。

同时吸收用户当前执行环境约束，但不要扩大架构：

- primary execution environment优先 Longleaf_Codex；
- 不得因为 Workstation / CUHK_Workstation_WSL_Codex 当前掉线而阻塞 Stage A、classification、review、GitHub migration、Action smoke、audit 或 search；
- v7不是machine-consumer adaptation，不需要等工位恢复；
- 如果Longleaf_Codex最后无法完成“live Issue chooser supported UI readback”，只把这一项隔离成最后一个 bounded acceptance handoff；不得要求重跑前面的migration/review，也不得把工位作为整个v7的前置条件。

不要修改approved v7 architecture，不实现v6.1，不启动Codex，不创建labels/Issues/Project mutation。

提交完整新版 Plan / Goal / Kickoff，并自动生成下一轮 execution-ready Critic prompt，绑定exact新package commit。
```
