# Presentations Stage 1 Execution Package v1.1 — Execution-Ready Critic Re-Review

**Review stage:** `STAGE1_EXECUTION_READY_RE_REVIEW`  
**Target repo:** `YuukiAS/AI_Skills_Collection`  
**Target plugin/domain:** `presentations`  
**Task key:** `presentations--stage1-front-door-two-template-foundation`  
**Reviewed package:** `results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md`  
**Reviewed package commit:** `049847f4638bb339229c748d3b8f97bd41fae72d`  
**Current AI_Skills main inspected:** `1df71c3b3fe0a890ed419765c851805241709c0c`  
**Current Bridge Kit main inspected:** `54bf116c38638753a0579b5f18c19fc6c0239fd6`  
**Prior execution-ready review:** `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md @ c4fd2c64b3211529a61a33e5f80eb7afc2e2960a`  
**Verdict:** **REVISE**

## 1. 用户可读闭环结论

上一轮两个 stable blocker 都已经被 v1.1 正确关闭：

- `PRES-S1-ER-F01 = CLOSED`：first bootstrap 后不再直接进入 production implementation；Plan / Goal / Kickoff 三件套都冻结了 Planner-owned `AI_BRIDGE_REVIEWED_PLAN_V2` transaction，初次 freeze 保持 `plan_revision=0`，只有 `PLAN_FROZEN / RUN_CODEX_EXECUTOR` 后 Executor 才能开始改 Presentations。
- `PRES-S1-ER-F02 = CLOSED`：三件套的 exact bootstrap command 都已经加入 `--ci-required`，并且后续强制 `WAITING_FOR_CI / ci_status=PENDING`，真实 GitHub CI PASS 以后才能进入 implementation review；没有加入 Text/Visual review flag，也没有引入 paid review。

但是在这次 re-review 时，Bridge Kit 最新 main 已经暴露并记录了一个新的跨 repo 通用缺口：**brand-new Reviewed task 的 first remote publication 当前没有可用的 bounded normal entry。**

这不是把旧 blocker 换名字，也不是重新打开 Presentations 架构。它是上一轮之后出现并被 Bridge repo 明确记录的新事实，因此符合“new fact”新增 blocker 条件。

当前 Presentations v1.1 Kickoff 正确要求：
`bootstrap -> commit/publish REQUEST/CURRENT -> external Planner -> PLAN_FROZEN`，
而且明确禁止 raw push / alternate branch / Bridge workaround。

但当前 Bridge `publish-current-branch` 只支持已经存在、已经 tracking 的同名远端分支；全新 Reviewed branch 首次发布会失败。Bridge 自己已经把这个问题记录为 `docs/TODO_REVIEWED_HANDOFF_FIRST_REMOTE_PUBLICATION.md`，并且最新设计 Plan 仍是 **design-only / not implemented**。

因此这个 package 现在可以正确 bootstrap，也可以正确停在 `PLAN_REQUESTED`，但无法通过它自己允许的 normal entry 把 first-bootstrap metadata 发布给外部 Planner。也就是说：F01/F02 都关闭了，但整包当前仍不能 truthfully 标成 `READY_FOR_CODEX=YES`。

## 2. Stable blocker re-check

### PRES-S1-ER-F01 = CLOSED

v1.1 Plan / Goal / Kickoff 一致冻结：

```text
approved Kickoff
-> exact task bootstrap
-> PLAN_REQUESTED / RUN_GPT_PLANNER
-> only REQUEST/CURRENT control metadata may be published
-> Executor/product implementation stops
-> external GPT Planner reads approved package + task state + current PLAN template
-> Planner writes AI_BRIDGE_REVIEWED_PLAN_V2
-> Planner self-check
-> PLAN_REQUESTED -> PLAN_FROZEN
-> next_action = RUN_CODEX_EXECUTOR
-> plan_revision = 0
-> publish Planner transaction
-> only then Executor starts Stage 1
```

Current Bridge source independently confirms:
- bootstrap initializes `PLAN_REQUESTED`;
- `next_action = RUN_GPT_PLANNER`;
- new/frozen Plan must validate as current V2 before `PLAN_FROZEN`;
- `plan_revision` increments only on `NEEDS_GPT_PLANNER -> PLAN_FROZEN`, not on the initial `PLAN_REQUESTED -> PLAN_FROZEN`;
- `PLAN_FROZEN` routes to `RUN_CODEX_EXECUTOR`;
- later worktree recovery can use artifact-bound `materialize-worktree --mode resume`.

Kickoff explicitly forbids Executor from writing/freezing task-local Plan, forbids production source edits before `PLAN_FROZEN`, and treats external Planner wait as normal waiting.

No direct regression found.

### PRES-S1-ER-F02 = CLOSED

Plan / Goal / Kickoff exact bootstrap command all include:

```text
--ci-required
```

Current Bridge source confirms this initializes:

```text
CURRENT.ci_required = true
CURRENT.ci_status = PENDING
```

and enforces:

```text
EXECUTING
-> WAITING_FOR_CI
ci_status = PENDING
-> real GitHub CI
-> CI PASS
-> READY_FOR_GPT_REVIEW / implementation review
```

A CI-required task cannot legally skip directly from `EXECUTING` to `READY_FOR_GPT_REVIEW`.

v1.1 also correctly states RESULT prose cannot override CURRENT CI machine truth.

No `--visual-review-required`, no `--text-review-required`, and no paid review authority were added.

No direct regression found.

## 3. New blocking finding

### PRES-S1-ER-F03 — Current Bridge cannot perform the required first remote publication through an approved bounded normal entry

**Requirement**

The approved Stage 1 chronology requires first-bootstrap `REQUEST.md` / `CURRENT.json` to become remotely readable so the external GPT Planner can perform the task-local V2 Plan transaction. The Kickoff explicitly requires that this publication use the current authorized bounded route and forbids raw push, alternate branch/worktree, or Bridge mutation workaround.

The wider project contract also requires that once the user has authorized the exact task/branch/worktree, the first ordinary non-force publication of that exact reviewed branch must not require a second user authorization; if Bridge cannot do that, the generic Bridge gap must be found before execution rather than worked around in the consumer repo.

**Direct evidence**

Latest Bridge Kit main:

`YuukiAS/GPT_Codex_AI_Bridge_Kit @ 54bf116c38638753a0579b5f18c19fc6c0239fd6`

now contains:

`docs/TODO_REVIEWED_HANDOFF_FIRST_REMOTE_PUBLICATION.md`

which records a real AI_Skills Reviewed task where first bootstrap succeeded locally but `publish-current-branch` returned:

`UPSTREAM_REMOTE_MISMATCH`

because a brand-new reviewed branch has no existing same-name remote branch/upstream.

The same TODO explicitly concludes the gap belongs to Bridge Kit, not the consumer repo.

Current Bridge also contains:

`docs/design/reviewed_handoff_first_remote_publication_plan_v0.1_2026-09-29.md`

which proposes a future narrow:

`ai-bridge reviewed-handoff task publish-first`

but the document status is:

`READY FOR INDEPENDENT CRITIC REVIEW / DESIGN ONLY`

and current Bridge source/CLI does not yet expose `publish-first`.

Code search on current main finds `publish-first` only in that design Plan, not production implementation.

**Causal risk**

If the user sends the current Presentations v1.1 Kickoff now:

1. bootstrap can succeed and create the exact local reviewed branch/worktree;
2. task will correctly stop at `PLAN_REQUESTED / RUN_GPT_PLANNER`;
3. the package then requires first-bootstrap control metadata publication;
4. the existing bounded publisher cannot create the new remote branch;
5. raw first push is explicitly forbidden by the package and would reintroduce the repeated-authorization/workaround problem the Bridge contract is supposed to eliminate;
6. therefore the external Planner cannot legally receive the task state and the execution cannot reach `PLAN_FROZEN`.

This is a deterministic current control-plane blocker, not an ordinary possible implementation bug.

**Minimum closure condition**

Do not change Presentations product architecture or add a consumer-specific workaround.

Close this blocker only after Bridge Kit has a Critic-approved, implemented, tested, actually installed/available bounded first-publication normal entry for a brand-new Reviewed task that:

- derives the exact reviewed branch from task identity;
- publishes only the exact same-name branch non-force;
- validates repo/task/worktree/base/remote/transport/lineage;
- does not allow arbitrary new branch/refspec/force/tag/delete behavior;
- proves remote SHA == captured local HEAD;
- requires no second user approval after the already approved exact Kickoff.

Then re-review the Presentations execution package against that **actual current Bridge command/semantics**.

If the final Bridge command differs from the generic wording currently used in Presentations v1.1, update Plan/Goal/Kickoff consistently. If the current v1.1 wording already correctly delegates to the new current bounded route, no product-scope redesign is required.

Do not solve F03 by:
- raw `git push -u`;
- manual second approval as the normal path;
- consumer-specific Git wrapper;
- widening `publish-current-branch`;
- changing branch/worktree;
- modifying Presentations product scope.

## 4. Direct regression check from v1.1 repairs

No direct regression from the F01/F02 fixes was found in the already-approved Stage 1 product semantics.

Still preserved:
- unified Presentations front door;
- research no-format -> CUHK Beamer;
- teaching no-format -> course-standard Beamer;
- business no-format -> editable PPTX/Slides;
- explicit PPTX/Slides -> official editable adapter;
- existing/local edit preserves format/template;
- local-edit fast path;
- external locked template stays pass-through;
- plan-only does not claim artifact completion;
- exactly two built-in templates;
- exact Chapter1 direct-read/hash/fail-closed contract;
- G1 natural installed-candidate requirement;
- G5 actual source consumption + visual fidelity remain non-compensating;
- generated layer remains generator-only;
- Stage 2–6 stay out of scope;
- #44–#48 stay unpromoted;
- Bridge mutation remains out of the Presentations task;
- NO_BUMP / NO_RELEASE / no main integration remain unchanged.

## 5. Verdict

```text
PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = STILL_OPEN

RESULT = REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY_RE_REVIEW

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md

REVIEWED_PACKAGE_COMMIT =
049847f4638bb339229c748d3b8f97bd41fae72d

APPROVED_PROPOSAL_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md

PLANNER_RESPONSE =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_1.md
@ 95c1f8a14a58613306a72a3a2010b942bbc235a9

CONTROL_CHRONOLOGY_VERDICT = PASS_F01_CLOSED
CI_REQUIRED_VERDICT = PASS_F02_CLOSED
PRODUCT_SCOPE_REGRESSION_VERDICT = PASS_NO_DIRECT_REGRESSION
AUTHORIZATION_VERDICT = REVISE_FIRST_REMOTE_PUBLICATION_NORMAL_ENTRY_UNAVAILABLE
RECOVERY_VERDICT = PASS_FAIL_CLOSED_NO_CONSUMER_WORKAROUND

READY_FOR_CODEX = NO
```

No approved Codex Kickoff is emitted while F03 remains open.

## 6. Maintenance Board pending mutation

Project sync is not claimed from this Critic surface.

Exact pending mutation:

```text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#48
Status = DOING

Current execution anchor =
  results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V2.md
  @ <this review commit>

Next action =
  Resolve generic Bridge first-remote-publication capability in
  YuukiAS/GPT_Codex_AI_Bridge_Kit;
  then re-review Presentations Stage 1 v1.1 against the implemented current Bridge entry.

Resolution commit = unset
Source maturity/status = unchanged
Issues remain open
Do not mark PROMOTED/DONE or close issues.
```

## 7. Next handoff

```text
NEXT_HANDOFF=PLANNER
```

The Planner should not redesign Presentations or create a consumer-local workaround. The next decision is dependency handling: bind Presentations Stage 1 to the generic Bridge first-publication blocker, let the Bridge Planner/Critic close that cross-repo capability, then return to this execution package for a narrow F03 re-review.
