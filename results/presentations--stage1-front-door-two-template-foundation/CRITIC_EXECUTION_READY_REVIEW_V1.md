# Presentations Stage 1 Execution Package v1.0 — Execution-Ready Critic Review

**Review stage:** `STAGE1_EXECUTION_READY`  
**Target repo:** `YuukiAS/AI_Skills_Collection`  
**Target plugin/domain:** `presentations`  
**Task key:** `presentations--stage1-front-door-two-template-foundation`  
**Reviewed package:** `results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_0.md`  
**Reviewed package commit:** `ccc6a1153d6ef3b41d1bc118e0dac454b11151d9`  
**Current main inspected before this review:** `8d342887e9a9f85ab2908510cd240c9c508b4c6e`  
**Verdict:** **REVISE**

## 1. 用户可读结论

Stage 1 的产品范围、G1/G5、private reference、source/generated 边界和 release boundary 基本已经可以执行；当前不能给 `READY_FOR_CODEX=YES`，原因集中在 **Reviewed Handoff 启动时序**，不是 presentations 架构本身。

我对照了最新 Bridge Kit `main` 的实际实现，而不是旧设计文档。当前 `reviewed-handoff task bootstrap` 会且只会创建 exact reviewed branch/worktree、`REQUEST.md`、`CURRENT.json`，随后任务处于：

```text
PLAN_REQUESTED
RUN_GPT_PLANNER
```

新任务必须由 GPT Planner 在 task-local worktree 中写当前 `AI_BRIDGE_REVIEWED_PLAN_V2` 的 `PLAN.md`，合法推进到：

```text
PLAN_FROZEN
RUN_CODEX_EXECUTOR
```

之后 Executor 才能开始 production implementation。

当前 Stage 1 Plan / Goal / Kickoff 在 bootstrap 后直接进入 implementation sequence，没有冻结这一步 Planner-owned transaction。因此用户现在若直接发送 Kickoff，Codex 要么违反 Bridge 当前角色/状态合同直接改 production，要么在 `PLAN_REQUESTED` 正确停下但无法按 Kickoff完成 Stage 1。

同时 Stage 1 明确要求真实 GitHub CI，但 Kickoff 的 bootstrap 命令没有 `--ci-required`。当前 Bridge source 的默认值是 `false`，因此新 task 会被初始化为 `ci_required=false`，和 package 自己要求的 CI gate 冲突。

只需要修这两个 execution-control blocker。Stage 1 的产品设计、routing matrix、G1/G5、Chapter1 fail-closed、generated-only 和 NO_BUMP/NO_RELEASE 边界不需要重做。

## 2. Package identity

Git compare 已确认：

`ccc6a1153d6ef3b41d1bc118e0dac454b11151d9 -> 8d342887e9a9f85ab2908510cd240c9c508b4c6e`

只新增：

`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REQUEST_V1.md`

Stage 1 Plan / Goal / Kickoff 没有在 approval snapshot 后变化，因此本轮审查对象稳定。

## 3. Reviewed Handoff current-source verification

Latest Bridge Kit inspected:

`YuukiAS/GPT_Codex_AI_Bridge_Kit @ 60c3dbe8a3649dc78af5f1124c6bdc555ce2aef1`

Current source confirms:

1. `task bootstrap` has repo-local cwd semantics;
2. caller supplies `--task-key`, `--expected-repo`, `--expected-base-commit`, optional task metadata flags;
3. there is no caller `--branch`, `--expected-worktree`, `--expected-base-ref` or `--target` on the bootstrap command;
4. branch is deterministically `reviewed/<task_key>`;
5. sibling worktree is deterministically `<repo-parent>/<repo-dir>-<task_key>`;
6. `expected-base-commit` must equal the current post-sync `refs/remotes/origin/main` OID;
7. bootstrap rejects existing local/remote task branch and noncanonical fetch profile;
8. raw `git worktree add` is not the normal fallback;
9. current Host Policy has a bounded allow rule for the hardened repo-local `task bootstrap`;
10. bootstrap creates only first task artifacts and initializes state to `PLAN_REQUESTED / RUN_GPT_PLANNER`.

Therefore the package's bootstrap CLI syntax and derived task topology are correct. The missing piece is the mandatory post-bootstrap Planner transaction.

## 4. Blocking findings

### PRES-S1-ER-F01 — Missing first-bootstrap Planner transaction before production implementation

**Requirement**

The Kickoff freezes Reviewed Handoff semantics, so it must obey the current Bridge normal entry. New Reviewed tasks cannot let Executor implement production while `CURRENT.state=PLAN_REQUESTED`; current Bridge requires a task-local V2 Plan and legal `PLAN_FROZEN / RUN_CODEX_EXECUTOR` transition first.

**Direct evidence**

Current Bridge source `bootstrap_task_worktree()` calls `_initialize_task_files()`, which initializes:

```text
state = PLAN_REQUESTED
next_action = RUN_GPT_PLANNER
```

Latest `templates/reviewed_handoff/README.md` states new/re-frozen Plans use `AI_BRIDGE_REVIEWED_PLAN_V2`.

Current AI_Skills execution packages already consume this contract explicitly: after first bootstrap, Executor work stops; GPT Planner reads `REQUEST.md`/`CURRENT.json` + approved package, writes task-local V2 `PLAN.md`, transitions to `PLAN_FROZEN / RUN_CODEX_EXECUTOR`, publishes that Planner transaction, and only then Executor implementation resumes.

By contrast, the Presentations Stage 1 Kickoff runs `task bootstrap` and then immediately instructs “Implement only Stage 1”; the Goal implementation sequence similarly proceeds from bootstrap directly to source implementation. It never freezes the required task-local Planner transaction.

**Causal risk**

If Codex follows the Kickoff literally, it can mutate production source under `PLAN_REQUESTED`, bypassing the Reviewed Handoff authority boundary. If it instead obeys current Bridge state ownership, it stops after bootstrap and the user-visible Goal cannot continue from the approved Kickoff. Either path makes the execution package non-executable as written.

**Minimum closure condition**

Submit a complete Stage 1 execution package v1.1 in which Plan + Goal + Kickoff consistently freeze this chronology:

1. from canonical repo, bootstrap the exact new task;
2. confirm exact sibling worktree and `PLAN_REQUESTED / RUN_GPT_PLANNER`;
3. commit/publish only first-bootstrap task-owned `REQUEST.md`/`CURRENT.json` when required for the external Planner to read them;
4. stop Executor/product implementation;
5. GPT Planner reads the approved architecture, Stage 1 execution Plan/Goal, execution-ready Critic review, current task `REQUEST/CURRENT`, and current `automation/reviewed_handoff/templates/PLAN.md`;
6. Planner writes task-local `AI_BRIDGE_REVIEWED_PLAN_V2` without redesigning Stage 1;
7. Planner validates and legally advances to `PLAN_FROZEN / RUN_CODEX_EXECUTOR`, with initial `plan_revision=0`;
8. publish the Planner transaction;
9. only then may Executor resume Stage 1 implementation.

Executor must never write/freeze its own task-local Plan. Existing-task recovery later must use artifact-bound `materialize-worktree --mode resume`, not second bootstrap.

---

### PRES-S1-ER-F02 — Mandatory CI is not enabled by the bootstrap command

**Requirement**

The Stage 1 package itself requires real GitHub CI because it changes Marketplace routing, source skills, shared routing, profile exposure, generated plugin payload and template source. The Reviewed Handoff task must therefore be initialized with CI required so its machine state and later transitions enforce the same contract.

**Direct evidence**

Stage 1 Goal/Plan require real GitHub CI and distinguish CI from G1/G5 product evidence.

Current Bridge CLI defines:

```text
task bootstrap --ci-required
```

as an opt-in flag. Without it, `ci_required` defaults to `false`, and `_initialize_task_files()` writes:

```text
ci_required = false
ci_status = NOT_REQUIRED
```

The reviewed Stage 1 Plan, Goal and Kickoff bootstrap command currently omit `--ci-required`.

**Causal risk**

The task would be born with machine truth “CI not required” while the frozen Stage 1 contract says GitHub CI is mandatory. Later `RESULT.md` prose cannot repair that mismatch, and Reviewed Handoff could legally take a non-CI transition path even though the product package requires CI.

**Minimum closure condition**

Add `--ci-required` to the exact bootstrap command in the revised Plan, Goal and Kickoff, and preserve the normal Reviewed Handoff CI chronology:

```text
implementation candidate published
-> WAITING_FOR_CI / ci_status=PENDING
-> real GitHub checks
-> only then external implementation review / next legal transition
```

Do not enable paid Text Review or Visual Review merely to fix this finding.

## 5. Scope / product gate findings

### Scope

PASS at design level. The package stays inside Stage 1:
- unified front door/routing;
- Marketplace/source-skill/shared routing/profile;
- local-edit fast path;
- editable business preservation;
- CUHK canonical adapter foundation;
- course-standard reconstruction;
- generated-only regeneration;
- G1/G5.

It explicitly excludes Stage 2–6, universal IR, third template, new top-level skill/plugin, implicit-invocation hack, geometry engine, #44–#48 promotion, Bridge changes, paid review, production release/install, version bump and main integration.

### G1

The product evidence standard is strong enough:
- exact committed candidate;
- fresh supported runtime;
- natural requests;
- actual candidate consumption, not helper receipt;
- Beamer source/PDF/render;
- real official editable surface for editable branches;
- truthful `BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE` if that supported surface is unavailable.

Current OpenAI product documentation supports the underlying feasibility: installed plugins/skills can be used in supported ChatGPT/Codex surfaces, but availability differs by product surface/workspace. Therefore the package is correct not to assume that the repo-local candidate replay helper itself proves the editable adapter. The execution task must use a supported surface or fail closed.

### G5 / Chapter1

The package correctly does not claim fidelity before implementation.

It freezes:
- exact filename/hash/pages;
- direct Executor + Reviewer access;
- no reconstruction from Planner prose/screenshot/OCR summary/memory;
- no copying course content/highlights;
- private file no commit/push;
- durable private evidence before worktree cleanup;
- non-compensating A: source consumed / B: visual fidelity.

No execution-package blocker is created merely because the Stage 1 render does not exist yet.

The actual presence of the exact Chapter1 file on the future execution machine has not been independently verified by this Critic. The package correctly classifies absence/hash mismatch as `BLOCKED_REFERENCE_UNAVAILABLE`. Before the user sends the revised approved Kickoff, placing/attaching the exact file at an authorized reachable source will avoid an immediate fail-closed stop, but this is not a new product decision.

### Source/generated/packaging

PASS. The primary source scope is bounded. Generated mirrors remain generator-only.

The conditional generator exception is acceptably narrow: only direct proof that the existing generic shared-payload mechanism cannot package the template permits the smallest generic compatibility fix; a second/presentation-specific generator is forbidden.

Current generator source already recursively copies configured shared payloads, so there is no present evidence that this exception will be needed.

### Regression

PASS. The package correctly requires targeted presentation tests, marketplace generation/parity, skills validation, full/risk-matched repo regression, Reviewed Handoff validation, `git diff --check`, real CI, G1 and G5. CI/tests are not allowed to substitute for product gates.

### Release / version

PASS. Stage 1 is explicitly an unreleased intermediate candidate on a reviewed branch, with:

```text
Repository bump decision = NONE
presentations = NO_BUMP
maturity = unchanged
no production install/release
no main integration
```

This is consistent with current version policy. If partial Stage 1 behavior would be exposed through a production distribution surface, the package correctly requires stopping before integration rather than silently shipping an unchanged version.

## 6. External targeted check

Current OpenAI documentation still supports the package's basic normal-entry premise:
- plugins package skills/capabilities and installed plugins can be used in supported ChatGPT/Codex surfaces;
- in supported Codex task views, users can select installed plugins;
- skills can be automatically used when helpful, but availability/install/sync differ by product and surface;
- local/repo marketplaces are supported testing/distribution sources, also with surface-dependent availability.

This means G1 is realistically testable, but the package is right to treat the official editable adapter as a surface-dependent capability and fail closed rather than fake it.

Current CTAN still reports Beamer 3.78 (2026-08-20) and Tagged PDF unsupported; no runtime fact surfaced that invalidates the approved Beamer adapter foundation.

## 7. Non-blocking notes

### N1 — Candidate replay is identity/consumption evidence, not the entire G1 adapter proof

The repo-local candidate replay helper uses a pinned Codex CLI, `--ignore-user-config`, a temporary candidate marketplace and an ephemeral child. It is suitable for exact candidate loading and skill-consumption evidence. It should not be stretched into proof that an external/official editable Presentation/Slides adapter exists on that same child surface.

The current package already says this; no change is required unless the revised package accidentally weakens it.

### N2 — Do not add visual-review automation merely because G5 is visual

G5 requires independent pixel-level qualitative review, but the current package does not authorize paid review. That can be satisfied by the implementation Reviewer directly receiving the private Chapter1 reference plus candidate renders through an authorized accessible route. Do not mechanically enable a paid visual-review mechanism in the bootstrap.

## 8. Verdict

```text
RESULT = REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_0.md

REVIEWED_PACKAGE_COMMIT =
ccc6a1153d6ef3b41d1bc118e0dac454b11151d9

APPROVED_PROPOSAL_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_0_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_0.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_0.md

SCOPE_VERDICT = PASS
AUTHORIZATION_VERDICT = REVISE_REVIEWED_HANDOFF_CHRONOLOGY
NORMAL_ENTRY_G1_VERDICT = PASS_GATE_DESIGN_EXECUTION_EVIDENCE_PENDING
TEMPLATE_G5_VERDICT = PASS_GATE_DESIGN_EXECUTION_EVIDENCE_PENDING
PRIVATE_REFERENCE_VERDICT = PASS_FAIL_CLOSED_ACCESS_CONTRACT
REGRESSION_VERDICT = REVISE_CI_REQUIRED_NOT_BOUND_TO_TASK_STATE
RECOVERY_VERDICT = PASS
RELEASE_BOUNDARY_VERDICT = PASS

READY_FOR_CODEX = NO
```

No approved Codex Kickoff is emitted because the reviewed Kickoff requires substantive workflow correction.

## 9. Maintenance Board pending mutation

This Critic surface does not expose the Project mutation surface required to update `AI Skills Maintenance`; Project sync is **not claimed**.

Exact pending mutation:

```text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#48
Status = DOING

Current execution anchor =
  results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md
  @ <this review commit>

Next action =
  Planner submits complete Stage 1 execution package v1.1 closing:
  PRES-S1-ER-F01
  PRES-S1-ER-F02
  then independent execution-ready Critic re-review.

Resolution commit = unset
Source maturity/status = unchanged
Issues remain open
Do not mark PROMOTED/DONE or close issues.
```

## 10. Next handoff

```text
NEXT_HANDOFF=PLANNER
```

Planner should revise the full package, not provide a patch-only reply. The presentations product architecture, G1/G5 semantics, routing matrix, private-reference contract, source/generated boundary, recovery and NO_RELEASE boundary should remain unchanged except where needed to make the current Reviewed Handoff chronology and CI state internally consistent.
