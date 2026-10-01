# AI Skills Maintenance Board — Issue Maturity Execution-ready Critic Prompt v0.2

你是 AI Research Stack 的独立 Critic thread。

当前只复核 v7 execution package v0.2 是否关闭上一轮唯一 stable blocker
`BOARD-V7-LABEL-CUTOVER-01`。不要重新设计已经通过的 taxonomy、Forms、
pre-admission Action、migration classification、audit、hierarchy、stale policy、
v6.1 independence、version policy 或 branch/worktree architecture。

本轮只读审查，不执行、不创建 labels/Issues/Project mutation、不修改
`.github` / source、不启动 Codex、不实现 v6.1、不执行 machine adaptation。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-issue-maturity
human_label = Maintenance Board Issues 成熟化
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW_V7_V0_2
package_version = v0.2
package_snapshot_commit = 957a06a45f6f74d4cb7b85e9181fd38045f8aa7d
execution_branch = reviewed/repo--maintenance-board-issue-maturity
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
primary_execution_environment = Longleaf_Codex
```

## Approved design

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`

commit:

`3d091421c7afe8d4f90687ef6e0ce2686bcaf426`

Design Critic result: `PASS`, supplied by the user for this execution-package line.

## Previous execution review

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-01.md`

commit:

`c78c653c097fea7b9efd33e00ccf08cd324f454d`

Stable blocker:

`BOARD-V7-LABEL-CUTOVER-01`

The previous review explicitly accepted the rest of the v0.1 architecture.

## Exact v0.2 package

Plan:

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_2_2026-10-01.md`

Goal:

`docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_2.md`

Kickoff Draft:

`docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_2.md`

All three coexist in exact package snapshot:

`957a06a45f6f74d4cb7b85e9181fd38045f8aa7d`

v0.1 is superseded and must not be sent to Codex.

## 必须先实际读取

latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved v7 Proposal
- previous v0.1 execution Critic review

exact snapshot `957a06a...`:

- v0.2 Plan
- v0.2 Goal
- v0.2 Kickoff

按需读取 current GitHub label / `.github` reality only to assess feasibility;
do not mutate anything.

## 已接受、不要重开的内容

Keep:

- approved kind/scope/area/triage/integration taxonomy;
- canonical TODO vs Project Status/Area vs labels source-of-truth split;
- two Forms + blank Issue route;
- tiny pre-admission `issues:opened` + `issues:write` Action;
- classification before live mutation;
- ambiguous kind fail closed;
- read-only metadata audit;
- native sub-issues/dependencies only;
- live Forms / Action / search / audit acceptance;
- stale auto-close forbidden;
- v6.1 independent;
- `Repository bump = NONE`;
- all plugins `NO_BUMP`;
- no production Plugin Capability Gate Matrix;
- exact branch/worktree and existing GitHub mutation envelope.

No new direct evidence -> do not move these endpoints.

## BOARD-V7-LABEL-CUTOVER-01 repair

Previous package incorrectly published Forms/Action to default main before their
required labels were guaranteed to exist.

v0.2 now requires:

```text
Stage A functional candidate
-> independent implementation Reviewer PASS
-> latest-main drift check
-> snapshot every exact v7 repo-level label definition
-> reject incompatible same-name semantics
-> create/reconcile all exact v7 labels
-> live readback labels ready
-> only then integrate Forms/Action/audit/policy to main
-> migrate Issues
-> live acceptance
```

Please verify this exact ordering in Plan / Goal / Kickoff.

## 1. Stage A remains mutation-bounded

Before independent Reviewer PASS:

- no live v7 taxonomy label create/reconcile;
- no existing-Issue taxonomy migration;
- no Issue state change;
- no Project Status/Area change;
- no source TODO maturity/evidence/`tracking:#N` change.

Stage A may still create/reuse the task's own v7 tracking Issue under the
already-approved mutation scope.

Check that v0.2 did not accidentally authorize label cutover early.

## 2. Pre-cutover label-definition snapshot

After Reviewer PASS + latest-main drift check, but before default-main
publication, v0.2 requires:

`results/repo--maintenance-board-issue-maturity/PRE_CUTOVER_LABEL_DEFINITIONS.json`

For every exact v7 label:

- name;
- existed before v7;
- current color;
- current description;
- semantic compatibility = ABSENT / COMPATIBLE / INCOMPATIBLE.

It also snapshots `maintenance-track` as protected baseline but never mutates
it.

Check whether this captures exactly the evidence needed for safe reconcile and
rollback.

## 3. Same-name compatibility

v0.2 allows:

- absent -> create approved exact definition;
- semantically compatible existing label -> reconcile approved
  color/description;
- semantically incompatible existing label -> fail closed before any mutation.

No incompatible `--force`.

Judge whether "semantically compatible" is sufficiently bounded or whether a
minimum evidence rule is needed. Do not require a taxonomy database.

## 4. Labels before Forms/Action publication

All exact v7 labels must exist and read back correctly before ordinary non-force
main integration publishes:

- the two Issue Forms;
- `maintenance-board-intake.yml`.

Any create/reconcile/readback failure means:

- no main integration;
- no Forms/Action publication.

This directly addresses the GitHub behavior noted in the prior review: default
form labels / Action label mutation require the label to already exist.

## 5. Provenance-aware rollback

For each exact v7 label:

- absent before v7 -> rollback may delete only that newly created label;
- existed before v7 and definition changed -> restore exact prior
  color/description;
- existed and was not changed -> leave unchanged;
- `maintenance-track` -> never change/delete/redefine.

A partial label-cutover failure must rollback prior mutations before stopping.

If rollback readback fails, stop with exact residual drift and do not publish
Forms/Action.

Check Plan / Goal / Kickoff are consistent on this.

## 6. Cutover evidence after Reviewer PASS

v0.2 permits a post-review evidence-only commit under:

`results/repo--maintenance-board-issue-maturity/**`

for label snapshot/journal evidence.

Functional files must remain byte-identical to the Reviewer-PASS candidate.
Any functional diff requires re-review.

Judge whether this preserves independent implementation review while allowing
live cutover evidence to be durable.

## 7. G7 consistency

Plan explicitly names:

`G7 — pre-publication label cutover`

Goal and Kickoff must enforce the same sequence and failure behavior.

Check specifically:

- snapshot first;
- compatibility check;
- create/reconcile;
- readback;
- rollback on failure;
- only then main integration.

If any one of Plan / Goal / Kickoff still says integrate-main before labels,
the blocker is not closed.

## 8. Environment routing

v0.2 freezes:

`primary_environment = Longleaf_Codex`

and explicitly says Workstation / `CUHK_Workstation_WSL_Codex` outage does
not block:

- Stage A;
- classification;
- review;
- G7 label cutover;
- Issue taxonomy migration;
- Action smoke;
- audit;
- search.

v7 is repo/GitHub governance, not machine-consumer adaptation.

Check this is only execution routing and does not change architecture or machine
authorization.

## 9. Final chooser UI exception

If Longleaf cannot provide a supported live Issue chooser UI readback after all
other gates:

- isolate only chooser readback as a final bounded acceptance handoff;
- use any supported UI-capable surface;
- do not replay classification/review/cutover/migration/Action/audit/search;
- do not make Workstation recovery a prerequisite;
- do not claim Forms live acceptance until chooser readback completes.

Check this is a bounded acceptance recovery, not a silent proxy PASS.

## 10. Existing accepted taxonomy / migration architecture

Confirm v0.2 did not regress:

- Project Area authoritative; `area:*` mirror only;
- exactly one kind/scope/area on admitted Issues;
- no lifecycle labels;
- complete classification before migration;
- ambiguous kind stops all live taxonomy migration;
- migration changes only v7 labels on existing Issues;
- no reopen/close existing Issues;
- no Project Status/Area mutation;
- no source TODO/`tracking:#N` mutation.

## 11. Audit / Forms / Action / search

Previously PASS subject to cutover ordering.

Ensure v0.2 still requires real live evidence, not config/test receipts:

- actual labels;
- actual Issue migration;
- actual Project Area comparison;
- live chooser;
- real Action run;
- acceptance Issue readback;
- real search;
- live audit;
- stale-safety readback.

## 12. v6.1 independence

v7 must not implement or alter #4 required-consumer semantics.

If v6.1 lands before v7 integration, preserve it.
If same-file semantic drift conflicts, return Planner/Critic.

Check no v0.2 cutover repair changes this.

## 13. Version / Gate / README

Expected:

```text
Repository bump = NONE
Affected plugins = all NO_BUMP
Production Plugin Capability Gate Matrix = NOT REQUIRED
README checked: no update required (expected, closure check still required)
```

Independently verify no new production-plugin behavior was introduced by v0.2.

## 14. Failure recovery

Specifically recheck:

- label snapshot unavailable -> no labels / no main integration;
- incompatible same-name -> no mutation / no main integration;
- partial cutover failure -> provenance-aware rollback;
- rollback failure -> exact residual drift blocker;
- functional source diff after Reviewer -> re-review;
- Workstation/WSL offline -> continue Longleaf path;
- Longleaf chooser UI unavailable -> isolate only final chooser acceptance.

No new daemon/controller/registry should appear.

## 15. Expected output

If `BOARD-V7-LABEL-CUTOVER-01` is still open:

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V7_V0_2
PACKAGE_SNAPSHOT_COMMIT = 957a06a45f6f74d4cb7b85e9181fd38045f8aa7d
READY_FOR_CODEX = NO
RECHECKED_BLOCKERS = BOARD-V7-LABEL-CUTOVER-01
```

Give direct evidence, causal risk and minimum close condition. Do not reopen
previously accepted design without new evidence.

Then generate a complete Planner repair prompt.

If the blocker is closed and package is execution-ready:

first explain naturally:

- label publication ordering;
- rollback provenance;
- Stage A / G7 / Stage B boundary;
- Longleaf execution routing;
- bounded chooser UI fallback;
- preservation of accepted v7 architecture;
- what PASS proves and does not prove.

Then output:

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_V7_V0_2
PACKAGE_SNAPSHOT_COMMIT = 957a06a45f6f74d4cb7b85e9181fd38045f8aa7d
RECHECKED_BLOCKERS = BOARD-V7-LABEL-CUTOVER-01
CLOSED_BLOCKERS = BOARD-V7-LABEL-CUTOVER-01
NEW_BLOCKERS = NONE
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_2_2026-10-01.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_2.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_2.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```

Then reproduce the exact reviewed v0.2 Kickoff from package snapshot; do not
write a different replacement.

## Review-file authorization

用户发送本 prompt，即授权你只在 latest main 新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_2_2026-10-01.md`

并 ordinary non-force push。

除此之外禁止修改：

- Proposal / Plan / Goal / Kickoff;
- canonical board policy;
- Issues / Project / labels;
- `.github`;
- scripts/tests;
- plugin source;
- machine state;
- any other repo.
