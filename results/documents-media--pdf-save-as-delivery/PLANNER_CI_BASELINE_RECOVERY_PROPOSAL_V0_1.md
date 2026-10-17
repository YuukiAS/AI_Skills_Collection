# PDF 首次交付 — CI 基线恢复 Proposal v0.1

Status: **READY FOR INDEPENDENT CRITIC REVIEW / NOT YET A FROZEN PLAN REVISION**  
Date: 2026-10-16  
Task: `documents-media--pdf-save-as-delivery`  
Branch: `reviewed/documents-media--pdf-save-as-delivery`  
Current Plan: `automation/reviewed_handoff/tasks/documents-media--pdf-save-as-delivery/PLAN.md`  
Current implementation commit: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`  
Current branch tip checked: `eb1c788e5cce9ef3e42c7710bd61a399a789913f`  
Current main checked: `362a8cab6991120a79600352d070926e2602dcbd`  
Implementation review: `results/documents-media--pdf-save-as-delivery/REVIEW_1.md`  
CI run: `38706208966`

## 1. Incident classification

This is not a new PDF product defect and does not reopen the approved delivery architecture.

D1–D3 product evidence has been completed for the current final candidate. The later D1 delivery event is recorded at:

`results/documents-media--pdf-save-as-delivery/D1_DELIVERY_EVENT.md`

The only remaining Reviewer blocker is the frozen Plan requirement that the repository-wide required GitHub CI be fully green.

The current task branch cannot legally repair the failing owners because the frozen scope explicitly forbids unrelated cross-plugin / publication-layer repair.

## 2. Direct evidence

GitHub Actions run `38706208966` on the task branch has:

- Windows sparse checkout: PASS
- Linux editable-install smoke: PASS
- Windows editable-install smoke: PASS
- `codex-marketplace`: FAIL during the full repository unit-test step

The four failing tests are:

1. `test_central_plugins_have_exactly_one_source_only_todo_inbox`
2. `test_generated_layer_matches_source_config`
3. `test_plugin_changelogs_match_marketplace_set_and_versions`
4. `test_research_presentation_todo_consolidation_and_promotions`

None is a `render-chinese-math-pdf` target regression.

The current `main` is `362a8cab6991120a79600352d070926e2602dcbd`. Its tracked file
`results/project-instructions-editor--standalone-skill-implementation/SURFACE_CONSOLIDATION_REPAIR_RESULT.md`
already records the same four repository-wide failures as pre-existing unrelated generated/TODO drift and explicitly declines to repair them inside another bounded standalone-skill task.

Current-main search still exposes the extra presentation TODO surfaces involved in the first and third failures, and current `main` has not integrated a baseline repair. Comparing this task branch with current `main` also shows that the main-side changes since this task's base are unrelated Slurm/Clear-Writing documents, not a repair of these failure owners.

Therefore “wait for upstream to become green and then rerun” currently has no identified owner, issue, or integrated fix and would leave this task indefinitely stalled.

## 3. Planner response to REVIEW_1

### CI blocker — PARTIAL_ACCEPT

Accept:
- The current frozen Plan literally requires required GitHub CI PASS.
- The Reviewer correctly cannot reinterpret a red required workflow as PASS.
- The task must not modify unrelated plugin/publication owners just to make CI green.

Do not accept the proposed recovery as sufficient:
- “Wait for an upstream legal repair” is not an executable recovery at present because current `main` still contains the same baseline drift and no matching repair issue was found.
- Re-running the same required workflow without a baseline repair will only consume time and potentially the second review round without producing new evidence.

### D1 blocker — CLOSED BY NEW EVIDENCE, NO PLAN CHANGE

The later first-completion delivery event at branch tip `eb1c788e...` closes the D1 observation gap without changing production source. The response led with the real final PDF entry for the same 43,853-byte candidate, and no second request was required. This evidence must be rechecked by the next Reviewer; it does not require a product repair.

## 4. Minimal recovery decision

Use the task's one legal Planner revision only to repair the **CI acceptance semantics**. Do not change D1–D3, product scope, renderer, version intent, privacy boundaries, or release candidate bytes.

Proposed revision after Critic PASS:

1. Set Reviewed Handoff machine routing to:
   - `ci_required=false`
   - `ci_status=NOT_REQUIRED`
   This prevents the workflow controller from requiring an impossible all-green repository-wide job before independent review.

2. Replace the old “repository-wide CI must be completely green” positive-completion clause with a **broad differential regression gate** because this candidate changes release/generated metadata while current main is already red.

3. The differential gate must use the same environment/commands for current-main baseline and the exact final candidate and must prove:
   - target PDF/standalone tests PASS on the candidate;
   - platform install/sparse-checkout smoke evidence remains PASS;
   - full-suite failing test IDs on the candidate introduce **no new failing test** relative to current main;
   - publication/generated-layer difference paths on the candidate introduce **no new difference owned by this PDF task** relative to current main;
   - changed-file analysis confirms this task did not modify the unrelated failure-owner sources merely to hide the baseline;
   - any candidate-only failure or worsened generated/publication difference remains blocking.

4. Store the exact comparison as:
   `results/documents-media--pdf-save-as-delivery/CI_BASELINE_DIFFERENTIAL.md`
   binding:
   - current-main SHA;
   - final candidate SHA;
   - commands/environment;
   - baseline failure set;
   - candidate failure set;
   - baseline generated/publication difference set;
   - candidate difference set;
   - candidate-minus-baseline deltas.

5. The existing GitHub run `38706208966` remains evidence and is not rewritten as PASS. Its three successful platform jobs remain valid process evidence; its failed full-suite job remains a truthful record of repository baseline debt.

6. After the differential gate passes, the same final candidate goes directly to independent REVIEW_2. The Reviewer must:
   - recheck D1 delivery event;
   - recheck D2/D3;
   - check the differential broad-regression evidence;
   - reject any attempt to call baseline debt “fixed”;
   - PASS only if this task adds no new regression and all PDF capability gates remain satisfied.

7. Do not create a successor, do not repair the unrelated baseline in this task, do not add a third review round, and do not alter Bridge Kit / Slurm / other plugins.

## 5. Why this is not a CI waiver

This amendment does not say “ignore CI because the change looks small.”

The broad failure surface remains observable. The difference is that when `main` itself is already red for unrelated owners, this bounded task is judged on **regression introduced by the candidate**, rather than being forced to repair unrelated repository debt it is forbidden to touch.

This is narrower than fixing the whole repository but stronger than target-only unit tests because the same full-suite and generated/publication surfaces are still compared against current main.

## 6. Release and integration boundary

No release ref is authorized by this recovery.

The candidate may only proceed to independent implementation review after the revised differential gate passes. Integration/release closure must still re-read current `main`, version policy, CHANGELOG, issue #101, and any then-current repository baseline state.

If current main becomes green before this recovery is executed, prefer the stronger normal path: update safely to that repaired baseline and run the ordinary required CI instead of using the differential exception.

If the differential comparison shows this candidate worsens any repository-wide failure, the recovery fails and the task remains REVISE.

## 7. Workflow state and review budget

Current state before this proposal:

```text
state = REVISE
review_round = 1
plan_revision = 0
ci_status = FAIL
next_action = RUN_CODEX_REPAIR
```

Because the only remaining repair requires changing the frozen acceptance contract, automatic Codex repair must not run yet. The task should wait for Planner/Critic recovery review without consuming REVIEW_2.

After independent Critic PASS, Planner may use the single revision budget:

```text
plan_revision: 0 -> 1
state: NEEDS_GPT_PLANNER -> PLAN_FROZEN
ci_required: true -> false
ci_status: FAIL -> NOT_REQUIRED
next_action: RUN_CODEX_EXECUTOR
```

Review history remains intact:
- `review_round=1`
- `last_review_decision=REVISE`
- existing `REVIEW_1.md` unchanged.

## 8. Maintenance tracking

Issue #101 remains open and Project lifecycle remains `DOING`. This recovery does not imply DONE.

Reader-facing Issue copy should eventually be updated to say the product D1–D3 evidence is complete and the task is undergoing one bounded CI-baseline contract recovery before REVIEW_2. This surface currently lacks the repository-mandated real Clear Writing invocation and GitHub Project mutation tool, so no reader-facing Issue/Project mutation is claimed here.

## 9. Critic decision requested

The independent Critic should decide only whether this one-time CI-baseline recovery is an acceptable replacement for the impossible full-green gate.

Critic should REVISE if:
- the differential evidence can hide a candidate-caused regression;
- setting `ci_required=false` would bypass evidence the Reviewer needs;
- current-main baseline equivalence is not sufficiently reproducible;
- release/integration would be incorrectly declared complete while repository-wide debt remains.

Critic should PASS if the amended gate preserves broad regression coverage while preventing unrelated pre-existing main failures from forcing this task to violate its frozen scope.
