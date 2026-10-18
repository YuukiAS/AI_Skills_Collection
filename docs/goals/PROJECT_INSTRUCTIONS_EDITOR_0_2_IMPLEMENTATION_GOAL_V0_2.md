# Goal — Project Instructions Editor 0.2 Bounded Implementation v0.2

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
READY_FOR_CODEX: NO  
Task key: `project-instructions-editor--0.2-baseline-diff-contract`  
Canonical Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_2_IMPLEMENTATION_PLAN_V0_2_2026-10-18.md`  
Supersedes: `PROJECT_INSTRUCTIONS_EDITOR_0_2_IMPLEMENTATION_GOAL_V0_1.md`  
Target repo: `YuukiAS/AI_Skills_Collection`  
Execution branch after approval: `reviewed/project-instructions-editor--0.2-baseline-diff-contract`  
Execution worktree after approval: `../AI_Skills_Collection-project-instructions-editor--0.2-baseline-diff-contract`

## Objective

Implement the already-approved PIE 0.2 incremental product contract without reopening PIE 0.1 architecture.

The finished candidate must keep all PIE 0.1 semantic editing behavior and add:

1. a hard user-supplied complete-current-setting gate before any PIE analysis/editing;
2. explicit-empty greenfield compatibility;
3. explicit-reset baseline provenance without restoring old semantic-preservation obligations;
4. mandatory human-readable Markdown change preview for every real change;
5. mandatory complete clean final Project setting for every real change;
6. one baseline/delta/final truth chain satisfying `E(B)=C`.

Do not implement Clear Writing as a PIE runtime dependency. Do not revive C7-C11 finalizer mechanisms.

## Critic blocker closure

The prior package received `REVISE` with stable blocker `PIE02-ER1`.

Planner disposition: `ACCEPT`.

The correction is evidence staging only. Public-safe / fixture normal-entry checks in this Goal are development / pre-final diagnostics and may never be reported as final G1 PASS. Final G1 PASS is reserved for the later approved real ChatGPT Web / Project acceptance using exact `FINAL_CANDIDATE_COMMIT=C`. The same live acceptance first proves the no-baseline normal entry, then supplies complete B + real edit request to produce the live R + clean C artifact for G4 review.

No fifth Gate or new workflow is created.

## Preflight

Before candidate-owned source mutation:

1. fetch latest `origin/main`;
2. read current `AGENTS.md`, this Goal, the canonical Plan, current PIE `SKILL.md`, `references/editor-contract.md`, focused tests/evals, `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`, and `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`;
3. confirm no active branch already owns `project-instructions-editor--0.2-baseline-diff-contract`;
4. create/use the exact approved branch/worktree above from the approved current-main base;
5. verify the current production PIE version is still `0.1`; if not, stop with `SOURCE_DRIFT` and return to Planner;
6. verify current formal `release` state but do not infer the future repository bump from `main` alone.

### Tracking bootstrap

Issue #93 must remain closed.

The new 0.2 tracking target is:

```text
title = Project Instructions Editor 0.2：真实基线与可审阅修改预览
labels =
  maintenance-track
  kind:enhancement
  scope:standalone-skill
  area:standalone-skill
Project Status = DOING
Project Area = standalone-skill
Resolution commit = blank
canonical source = docs/skill-todos/project-instructions-editor.md
tracking backlink = tracking: #<new issue number>
```

Before creating or substantively writing the reader-facing Issue copy, make a real invocation of the installed Clear Writing / `writing-style` capability as required by repository policy. This is repository maintenance only, not a PIE runtime dependency.

If the execution surface cannot truly invoke Clear Writing, do not fake the call and do not create reader-facing copy. Record the exact pending Issue/Project mutation. If Issue creation/backlink is legal but Project-field mutation is unavailable, complete the legal parts and record the exact pending Project mutation. Do not ask the user to drag cards or fill locators manually.

## Candidate-owned production changes

### 1. `skills/core/codex-system/project-instructions-editor/SKILL.md`

Implement all of the following while preserving the 0.1 semantic contracts:

- version `0.1 -> 0.2`;
- remove the old description semantics that editing can proceed “even if the live setting is missing”;
- after routing into PIE, make the complete user-supplied current baseline gate the first edit precondition;
- exact missing-baseline response:

  `请提供当前完整 Project setting 原文。PIE 不会根据 Project 上下文、Memory、历史聊天、仓库文件、部分 instructions 或模型推断重建当前 setting。`

- exact accepted-baseline receipt:

  `已收到当前完整 Project setting 原文；本轮以该原文作为唯一当前 baseline。`

- explicit empty setting counts as complete greenfield baseline;
- explicit reset still requires the user baseline, but reset removes only old Project-setting semantic-preservation obligations;
- old Project context, Memory, old settings, summaries, stale candidates, repository candidates and partial instructions cannot become the left-hand baseline;
- every real change must produce both a readable Markdown preview and the complete clean final setting;
- inline default: `~~旧~~**新**`;
- large replacement may use whole-sentence/paragraph/section deletion + addition when that is clearer;
- no Git `+/-`, no code diff block, no “删除/新增” machine labels;
- no-op does not manufacture a fake diff;
- preview is derived after semantic candidate/final consistency, not used as a second semantic editor;
- preserve the 0.1 formal runtime route and all should-not-change invariants.

### 2. `skills/core/codex-system/project-instructions-editor/references/editor-contract.md`

Add the detailed stable 0.2 contract:

- baseline provenance gate;
- obvious-partial-input handling;
- greenfield / reset compatibility;
- B→C→E/R ordering;
- preview granularity rules;
- full clean final requirement;
- phantom-deletion protection;
- preview/final mismatch recovery;
- `E(B)=C` consistency requirement;
- no persistent patch ledger/state;
- no Clear Writing / finalizer / external diff runtime dependency.

Remove only 0.1 text that directly conflicts with the new hard baseline gate. Do not delete unrelated 0.1 contracts.

### 3. `skills/core/codex-system/project-instructions-editor/evals/trigger_queries.json`

Preserve near-miss routing and add/adjust positive examples so the bank covers:

- a natural Project-setting edit request with no baseline;
- an explicitly empty setting;
- a preservation-sensitive edit with the full setting supplied;
- explicit reset with the full current setting supplied;
- compression/sync without naming the Skill.

Trigger examples do not themselves prove the baseline behavior; they only prove routing coverage.

### 4. `skills/core/codex-system/project-instructions-editor/agents/openai.yaml`

Only make the minimum wording changes needed to align short description/default prompt with the 0.2 user-supplied-baseline contract.

Keep:

```text
allow_implicit_invocation: true
```

Do not add another app, model, service, or dependency.

## Focused tests

Update `tests/test_project_instructions_editor_contract.py` and `tests/test_standalone_skill_baselines.py`.

Required deterministic assertions include:

- PIE version `0.2`;
- exact missing-baseline and baseline-receipt strings;
- no old “live setting missing” continuation claim;
- explicit-empty greenfield and reset-baseline semantics;
- Markdown preview + clean final dual output contract;
- inline and large-replacement display rules;
- same-baseline/same-delta consistency;
- no-op exception;
- preservation of 0.1 semantic invariants;
- no scripts/runtime helpers;
- rejected finalizer/reader-baseline mechanisms remain absent;
- `allow_implicit_invocation: true`;
- standalone skill remains outside central Marketplace topology.

Use Python standard library only for any test-time B→C diff helper. No helper becomes a PIE runtime dependency.

## Documentation and generated parity

Update only what the 0.2 release candidate actually changes:

- `README.md`: PIE v0.2 and concise user-facing capability wording;
- `CHANGELOG.md -> Unreleased`: PIE `0.1 -> 0.2`, current implementation task repository bump `NONE`, future formal repository bump deferred to release preflight;
- `docs/skill-todos/project-instructions-editor.md`: a bounded 0.2 canonical entry with real `tracking: #N` when that Issue exists;
- registry/catalog/provenance through the existing generators.

Any README mutation requires a real Clear Writing invocation before completion. Do not modify Clear Writing production source.

Do not manually edit generated central Marketplace payloads. PIE remains a standalone Skill.

## Capability Gates

Use exactly the four existing PIE gate families.

### G1 — Normal entry / routing

During this implementation Goal, run public-safe / fixture requests only as development / pre-final evidence:

- unnamed Project-setting edit request routes toward PIE behavior;
- missing baseline returns only the frozen request and no edit analysis;
- near-miss tasks remain with their owners.

Record this only as:

```text
G1_DEVELOPMENT_EVIDENCE=PASS | FAIL
G1_FINAL_LIVE=PENDING
```

Do not report final `G1=PASS` in this Goal.

Final G1 release PASS belongs to the later separately authorized live Web acceptance. It must:

1. load exact `FINAL_CANDIDATE_COMMIT=C` into the existing PRIVATE / USER-scope PIE wrapper;
2. start from a fresh real ChatGPT Web / Project normal entry;
3. send a natural Project-setting edit request without naming PIE and without a baseline;
4. receive only the frozen exact missing-baseline message, with no analysis/edit attempt;
5. only then continue with complete B + real edit request.

Only that live step may set `G1_FINAL_LIVE=PASS`.

### G2 — Core editing

Cover, on the same candidate:

- preservation-sensitive small inline change;
- explicit-empty greenfield;
- baseline + explicit reset;
- large paragraph/section rewrite with coarser preview;
- no-op;
- existing 0.1 locator/budget/ownership/enforcement behavior.

### G3 — Fidelity / should-not-change

Freeze at least these regressions:

- stale/old text contains a sentence absent from B: no phantom deletion;
- unchanged B rules remain in C;
- mandatory/optional, authorization, safety, privacy, evidence strength, role ownership, exact identifiers and protected absence remain correct;
- store full B, user request, preview R and clean C in the review packet;
- compare B→C with a deterministic standard-library diff as supporting evidence and independently review whether R faithfully represents the real changes and `E(B)=C`.

Static string tests cannot by themselves PASS G3.

### G4 — Representative complete task + qualitative final artifact

Prepare a complete public-safe **pre-final** G4 packet from the frozen final candidate C containing:

- full user request;
- full user-supplied baseline B;
- any required canonical source;
- full Markdown preview R;
- full clean final C;
- candidate identity.

This packet makes G4 ready for independent pre-final review; it is not final live G4 PASS.

Stop before any live ChatGPT wrapper mutation unless the later approved stage explicitly authorizes it.

The later real Web acceptance must update the existing PRIVATE / USER-scope PIE wrapper with exact C rather than create a second wrapper. After the same acceptance establishes final G1 with the no-baseline request, it must then supply complete B + real requested delta and capture the resulting live R + clean C for independent G4 qualitative adjudication.

## Final candidate discipline

After development tests/replays pass, freeze:

`FINAL_CANDIDATE_COMMIT=C`

Then rerun `G1_DEVELOPMENT_EVIDENCE`, G2 and G3 from C and build the G4 pre-final packet from C.

At this stage:
- G2/G3 may be final implementation-stage PASS;
- `G1_FINAL_LIVE` must remain `PENDING`;
- G4 remains pre-final packet ready, not final live PASS.

Evidence-only commits after C may produce `EVIDENCE_HEAD=E`. Before review, prove C..E contains no candidate-owned changes. Any candidate-owned mutation after C invalidates stale evidence and requires a new C plus blast-radius-matched reruns.

## Required validation

At minimum:

```text
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
```

Run additional narrow tests required by changed generated/doc surfaces. Do not repair unrelated current-main drift as part of this task.

## Version / release boundary

During implementation:

```text
Repository bump decision: NONE
project-instructions-editor standalone candidate: 0.1 -> 0.2
all central plugins: NO_BUMP
release ref mutation: NO
```

At formal release, re-read `origin/release` and `PLUGIN_VERSIONING_AND_CHANGELOGS.md`.

Do not assume PATCH. At Planner observation time, `release@39e2f20c53a07936f8dc5a289f3af41a83943b75` is repository `5.4.5` and does not contain PIE. If that remains true, formal PIE introduction may require a repository MINOR; if a prior formal release has already introduced PIE, 0.2 is an existing-capability improvement and will normally be PATCH.

## Explicit non-goals

Do not:

- alter PIE 0.1 semantic architecture outside the frozen delta;
- add a database, ledger, state machine, complex AST, runtime diff service or runtime script;
- add a central Plugin or new Profile;
- integrate Clear Writing into PIE runtime;
- modify Clear Writing source;
- revive C7-C11 finalization mechanisms;
- edit actual user Project settings;
- edit global Custom Instructions;
- use paid/external models or APIs;
- mutate Bridge Kit;
- reopen Issue #93;
- decide the final repository release version during implementation;
- perform live private wrapper update/publication in this Goal.

## Stop conditions

Stop and return to Planner/Reviewer if:

- source PIE is no longer 0.1 before implementation;
- approved product delta cannot be implemented without changing a frozen 0.1 architecture decision;
- a new runtime dependency appears necessary;
- tracking/README rules would require a fake Clear Writing invocation;
- candidate implementation cannot preserve the 0.1 should-not-change set;
- release-relevant evidence would require stitching multiple candidate commits;
- a real failure shows the four-gate taxonomy is insufficient and a fifth gate would be required.

## Completion output

Executor must report:

- changed candidate-owned files;
- exact tracking Issue/backlink state or exact pending mutation;
- tests/generators run and results;
- G1 development/pre-final evidence locator and explicit `G1_FINAL_LIVE=PENDING`;
- G2/G3 evidence locators;
- G4 pre-final packet locator;
- `FINAL_CANDIDATE_COMMIT=C`;
- `EVIDENCE_HEAD=E`;
- proof C..E has no candidate-owned change;
- version/release disposition;
- README Clear Writing evidence;
- remaining blockers.

Executor does not declare release DONE and does not run the real private Web acceptance.

Expected terminal state:

```text
G1_DEVELOPMENT_EVIDENCE=PASS
G1_FINAL_LIVE=PENDING
G2=PASS
G3=PASS
G4_PREFINAL_PACKET_READY=YES
G4_FINAL_LIVE=PENDING
READY_FOR_INDEPENDENT_IMPLEMENTATION_REVIEW=YES
READY_FOR_LIVE_WEB_ACCEPTANCE=NO
READY_FOR_RELEASE=NO
```

The later live-acceptance stage, not this Goal, owns the transition to `G1_FINAL_LIVE=PASS` and the production G4 artifact.
