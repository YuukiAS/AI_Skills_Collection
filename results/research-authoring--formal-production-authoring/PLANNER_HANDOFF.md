# Planner Handoff - Missing Final Task Freeze

Task: `research-authoring--formal-production-authoring`
Branch: `work/research-authoring--formal-production-authoring`
Current HEAD: `95c689c05ee22833bd32a942218b17bc949ed020`
Candidate commit C0: `1c37c0715aca0096606f24e56192b7857e72bbd6`
Evidence commit: `95c689c05ee22833bd32a942218b17bc949ed020`

## Current State

Implementation, generated parity, deterministic validation, profile install smoke, and development replay are complete.

Final G1-G4 evidence has not started. No final fresh G2/G3/G4 task has been consumed.

The current stop is intentional and required by the user/Kickoff constraint:

```ini
PREFINAL_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
BLOCKER=G2_G3_EXACT_REAL_FINAL_TASKS_NOT_FROZEN
```

## Completed Evidence

- Candidate source/generation commit: `1c37c0715aca0096606f24e56192b7857e72bbd6`
- Evidence/status commit: `95c689c05ee22833bd32a942218b17bc949ed020`
- Validation: `results/research-authoring--formal-production-authoring/VALIDATION.md`
- Development replay: `results/research-authoring--formal-production-authoring/DEVELOPMENT_REPLAY.md`
- G4 offline wrapper package:
  - `private/exports/research-authoring--formal-production-authoring/wrapper/WRAPPER_COMPOSITION.md`
  - `private/exports/research-authoring--formal-production-authoring/wrapper/MANIFEST.md`
  - `private/exports/research-authoring--formal-production-authoring/wrapper/research-authoring-wrapper-0.1.0-candidate-1c37c071.tar.gz`
  - SHA256: `83c5848e325430d10667e82777ad1da008350f6c2e0a238a2051574922e632c6`

## Why Planner Is Needed

Implementation Plan v0.1 requires pre-final packet freeze before Critic admission:

- G2 exact real report-family task identity;
- G2 Phase 1 raw-evidence input scope;
- G2 Phase 2 evidence/decision delta identity;
- G2 Reviewer rubric;
- G3 exact real manuscript task identity;
- G3 venue/project authority;
- G3 required package subset and Reviewer rubric;
- G4 reused exact task from G2 or G3.

Those objects are not present in this worktree or Issue #99. Executor cannot synthesize them without violating the approved architecture, because:

- G2 must be a real report-family two-phase task, not a synthetic fixture or already-clean report;
- G3 must be a real manuscript task not used for 059 product tuning;
- old DII/CAT-TRACE materials and presentation paper holdouts are development/regression references unless Critic explicitly approves a specific fresh task;
- final fresh evidence cannot be consumed before pre-final Critic PASS.

## Required Planner Output

Planner should provide one of the following.

### Option A - Freeze Real Final Tasks

Provide a task-owned artifact bundle under:

```text
private/exports/research-authoring--formal-production-authoring/final_tasks/
```

Minimum required files:

```text
G2/
  PHASE1_RAW_SCOPE.md
  PHASE1_INPUT_MANIFEST.md
  PHASE2_DELTA.md
  G2_RUBRIC.md
  REVIEWER_ACCESS.md
G3/
  TASK_IDENTITY.md
  VENUE_PROJECT_AUTHORITY.md
  PACKAGE_SUBSET.md
  G3_RUBRIC.md
  REVIEWER_ACCESS.md
G4/
  REUSED_TASK_DECISION.md
  CHAT_CODEX_HANDOFF_RUBRIC.md
```

Each manifest should include exact file paths or durable external locators, hashes where practical, privacy/access notes, and a statement that the task/delta has not been used to tune 059 product behavior.

After this, Executor can update `PREFINAL_GATE_FREEZE.md`, run only admissibility checks, and hand to pre-final Critic without starting final gates.

### Option B - Approve Existing Specific Material

If Planner/Critic believes an existing repo material is eligible as final fresh evidence, name it exactly and justify eligibility against the 059 constraints:

- exact path/commit/locator;
- why it was not used for 059 product tuning;
- which Gate it serves;
- how Reviewer gets full source/render/artifact access;
- why it is not merely development regression.

Without that explicit approval, Executor must continue treating existing DII/CAT-TRACE/presentation artifacts as development or structure-reference material only.

### Option C - Revise Plan

If no real G2/G3 task can be provided, Planner must revise the execution plan or return to Critic. Executor should not redesign G1-G4 or substitute synthetic evidence.

## Copy-Paste Prompt For Planner

```text
Review branch `work/research-authoring--formal-production-authoring` at `95c689c05ee22833bd32a942218b17bc949ed020`.

The Research Authoring 0.3 implementation candidate C0 is `1c37c0715aca0096606f24e56192b7857e72bbd6`. Deterministic validation, full tests, profile install smoke, development replay, and offline G4 wrapper package are complete. Final G1-G4 evidence has not started.

Executor cannot truthfully claim `PREFINAL_CANDIDATE_READY=YES` because G2 and G3 exact real final tasks are not frozen:
- G2 needs one real report-family two-stage task with Phase 1 raw evidence and Phase 2 pre-frozen delta invisible to Phase 1.
- G3 needs one real manuscript production task not used for 059 product tuning, with venue/project authority and package subset.

Please either:
1. provide/freeze the required task-owned artifact bundle under `private/exports/research-authoring--formal-production-authoring/final_tasks/`;
2. explicitly approve an existing exact material as final fresh evidence with eligibility rationale; or
3. revise/return the Plan to Critic.

Do not ask Executor to synthesize final evidence or consume final G1-G4 before pre-final Critic PASS.
```
