---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 043_research_presentation_real_visual_repair_challenge_recovery
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

042 established a shared finite scientific-object semantic compatibility layer and fresh Terra confirmed that its final non-holdout production deck remains visually mature, but the task reached its one Plan-revision boundary without exercising the frozen live repair gate: the staged initial Terra review returned no substantive blocking finding, so the consumer correctly performed zero repairs. Repeating the same 042 fixture-changing action would violate its stop condition and risk an open-ended search for a convenient failure.

043 therefore uses a **new bounded validation mechanism**: a small pre-frozen visual challenge bank, built only from independent public-safe/non-holdout material, whose complete contents and initial pixel identities are frozen before any challenge Terra result is read. The goal is not to make a deliberately bad deck pass. The goal is to demonstrate, under the unchanged mature visual rubric, that at least one real substantive-page Terra finding can be recognized through the shared 042 canonical role, mapped into an already-shipped safe repair family, executed within the existing single repair cycle, and produce genuinely changed final pixels that then meet the normal mature-talk bar.

This task is generic recovery only. It does not rerun 041 and does not authorize a new Stage 5 holdout batch. If 043 passes, the next Program transition is the required user human gate before any fresh four-paper batch is consumed.

## Frozen decisions

- **042 terminal history remains terminal.** Do not modify 042 `REQUEST/PLAN/REVIEW/FINAL_REPORT`, do not create a second 042 Plan revision, and do not reinterpret its all-PASS initial Terra as live-repair evidence.
- **041 remains an immutable failed holdout batch.** TMB, DESeq2, cardiac-ultrasound and RETFound are consumed. Their titles, DOI, authors,正文、figures/images, page-specific object names, rendered pixels and source bundles are forbidden as 043 fixture or tuning material.
- **Production behavior under test is frozen before challenge review.** 043 must not change mature gold membership/scoring, the canonical semantic-role family, selector hard constraints, quality-loop repair vocabulary/mapping, CUHK layout quality bar, source-fidelity rules or the single-cycle budget before or after seeing initial Terra. If real challenge evidence exposes a product-code defect that requires changing those mechanisms, 043 stops and reports the new blocker for a separate bounded recovery.
- **Exactly three challenge variants form the finite search space.** They must all be generated, published/tracked and identity-frozen before the first challenge Terra result is consumed:
  1. `Q_SCALE`: an aliased quantitative-source-object page whose source-faithful presentation content creates a credible projection-scale/readability challenge for the existing `RESCALE_PRIMARY_OBJECT` family.
  2. `Q_SUPPORT`: an aliased quantitative-source-object page whose source-faithful caption/support density creates a credible separation/collision challenge for the existing `REPAIR_ANNOTATION_LEGEND` family.
  3. `PROCESS_REFLOW`: an aliased process/decision object whose source-faithful labels create a credible diagram-label/collision challenge for the existing `SWAP_COMPATIBLE_GOLD_LAYOUT` family.
- Challenge construction may alter only task-local non-holdout input material and validation harness data. It may not hand-edit final render pixels, inject a fake Terra decision, weaken the visual rubric, force a gold ID, or directly set a repair hint/directive in production input.
- Each variant must use neutral aliases unrelated to all consumed holdouts and must still pass source-fidelity/mechanical production validation. The challenge must arise from legitimate input density/object detail handled by the normal production route, not from corrupt files, hidden text, malformed TeX or intentionally broken compilation.
- **No adaptive challenge chasing.** Once the three initial variants are frozen, their source bundle, page specs, challenge category, manifest bindings and initial rendered pixels cannot be changed based on Terra. Zero supported findings across all three is a legitimate terminal failure and must not trigger a fourth variant or an edited retry inside 043.
- **Real Terra chooses whether a repair is permitted.** A variant is repair-eligible only if task-local item-level Terra identifies a substantive-page blocking finding whose target and requirement unambiguously map, through existing 042 canonical semantics and current shipped mapper, to that variant's predeclared existing repair family. A top-level package result alone is insufficient.
- **Deterministic priority if several variants are eligible:** `Q_SCALE` first, then `Q_SUPPORT`, then `PROCESS_REFLOW`. This priority is frozen before visual results so the Executor cannot cherry-pick the easiest-looking winner after review.
- The selected variant may execute **exactly one existing quality-loop repair cycle**. Multiple cycles, new repair intents, hand-authored `repair_intent`, or direct manual editing of generated TeX/layout after Terra are forbidden.
- Repair success requires real effect: pre/post render-input identity, rendered-pixel identity and the selected target page hash must all change. Metadata-only changes do not count.
- Fresh final Terra must review the repaired target page and its complete deck/contact sheet under the same mature doctoral-group-meeting / strong paper-talk rubric and show no blocking finding. Other substantive pages in that deck must not regress.
- Existing Bridge Kit task-local Visual Review evidence contract remains authoritative. If local Executor lacks the GitHub Actions secret, it may stage the **already fully frozen three-variant initial challenge package** as `NEEDS_GPT_PLANNER` for watcher publication; that staging is not PASS and consumes no review round. After publication, the Plan is not revised: the next Executor run may trigger the existing `AI Bridge Visual Review` workflow on the tracked manifest. No new state machine or secret channel is allowed.
- 043 may have at most two independent GPT review rounds and at most one Plan revision under the standing Reviewed Handoff schema. No third review.

## Implementation scope

1. **Build a task-local pre-frozen challenge bank**
   - Create a 043 task-local public-safe/non-holdout source bundle or three task-local bundles using existing repository-safe synthetic/public fixtures that are not derived from 041.
   - The three variants must share the normal `research-presentations` production entrypoint and exact CUHK route. They may differ only in the task-local scientific content/density needed for the three predeclared challenge classes.
   - Use neutral scientific-object aliases so the challenge also exercises the 042 shared canonical semantic layer. Record, for every target page, the raw alias, canonical role, page job, source-evidence IDs and expected existing repair family without encoding a repair directive into production input.

2. **Freeze all initial challenge identities before visual feedback**
   - Generate all three complete decks via the normal one-call production path before consuming any challenge Terra result.
   - Record a task-local `challenge_index.json` or equivalent containing the three immutable variant IDs, source/input hashes, build-manifest hashes, render-input identities, rendered-pixel identities, target logical IDs/page hashes, canonical roles and predeclared family labels.
   - Build one task-local Visual Review manifest that exposes the three target pages and enough per-deck contact-sheet context for mature visual judgement. All paths/hashes in the manifest must bind to the initial frozen challenge artifacts.
   - Add a guard proving that no challenge source/test/production change contains 041 holdout identifiers or uses 041 artifacts as inputs.

3. **Obtain real initial Terra and apply the frozen selection rule**
   - Use the existing GitHub Actions Visual Review path. Do not hand-write or mutate `VISUAL_REVIEW.json`.
   - Read item-level decisions, observations and blocking findings for each target/deck. Confirm that any eligible finding identifies a substantive page and not merely an engineering title, manifest issue, missing asset or top-level packaging condition.
   - Evaluate the variants in the frozen order `Q_SCALE -> Q_SUPPORT -> PROCESS_REFLOW`. Choose the first variant whose real finding safely maps through the existing consumer to its predeclared repair family. If none qualify, stop 043 with preserved evidence; do not edit/reseed the bank.

4. **Exercise exactly one shipped repair cycle**
   - Feed the untouched real Terra evidence to the existing quality-loop consumer. The selected directive must be inferred by shipped code from structured finding + target + canonical role; no manual intent injection is permitted.
   - Execute the normal downstream repair/render path once. Record the selected directive, `repair_cycle_count=1`, pre/post render-input identities, pre/post rendered-pixel identities and selected target page hashes.
   - Assert that the selected target's render input and pixels changed and that source claims, scientific assets, exact CUHK identity and non-target source evidence remain protected.

5. **Fresh final visual review and regression evidence**
   - Publish/track the repaired selected deck through the same existing task-local Visual Review contract and obtain fresh final Terra bound to the repaired identities.
   - Final Terra must explicitly PASS the repaired substantive page and its deck contact sheet at the mature-talk bar, with no audience-facing workflow/test language and no new clipping/collision/readability blocker.
   - Run targeted semantic-normalizer/selector/quality-loop tests, normal production-entry validation, full presentation regressions, mirror parity, skill/marketplace validation, Reviewed Handoff validation and real GitHub CI.
   - Reviewer must independently inspect the real diff, initial/final manifests, challenge freeze record, quality-loop state, relevant rendered pixels/contact sheet, item-level Terra observations and CI rather than trusting `RESULT.md`.

## Acceptance and regression gates

043 may PASS only if all of the following are true:

1. **Finite pre-freeze is proven.** All three challenge variants, source/input hashes and initial pixel identities were tracked before the first challenge Terra result was consumed; repository history shows no post-Terra challenge-content edits.
2. **No holdout contamination.** 041 content/identifiers/artifacts are absent from challenge construction and no consumed holdout is rerun or used as a tuning fixture.
3. **Production mechanism stayed frozen.** No mature gold membership/scoring, semantic-role vocabulary, safe-repair mapping/vocabulary, selector hard constraints, visual rubric or quality threshold was changed after 042 merely to satisfy 043.
4. **A real substantive finding exists.** Initial task-local Terra, not a synthetic review fixture, reports at least one blocking substantive-page finding in the three-variant bank and provides item-level observations sufficient to judge it.
5. **Shared semantic mapping is exercised.** The chosen finding's target page carries a neutral raw alias but resolves through the 042 shared canonical role to the already-shipped existing repair family; no hand-added internal intent is used.
6. **Exactly one real repair cycle runs.** `repair_cycle_count=1`; the selected directive belongs to existing frozen vocabulary; a second cycle does not occur.
7. **Pixels really change.** Pre/post render-input identity, rendered-pixel identity and the selected target page hash are all different, and the change is attributable to the shipped repair path rather than manual output editing.
8. **Final visual quality passes.** Fresh final item/page-level Terra explicitly passes the repaired target and complete selected-deck contact sheet at mature doctoral-group-meeting / strong paper-talk quality with zero blocking finding; non-target substantive pages do not regress.
9. **Fail-closed behavior remains.** Unknown/ambiguous semantic roles and truly incompatible page-function/domain/panel/capacity combinations still no-winner/fail closed in tests.
10. **Repository regression passes.** Shared/plugin parity, targeted tests, normal production entry, full presentation/unit validation, Reviewed Handoff validation and required real GitHub CI all pass.

Hard stop conditions:

- If all three pre-frozen variants receive no safely repairable real substantive-page Terra finding, 043 fails with that evidence; do not create or modify a fourth challenge inside this task.
- If initial Terra finding requires a new repair family, new gold, semantic-role expansion, quality-bar change or product-code fix, stop and route that newly identified blocker to a separate bounded recovery; do not tune production inside the challenge.
- If the one allowed repair does not change real pixels or final Terra remains blocked, 043 fails within its normal review budget; do not execute a second repair.

## Natural-language usage / routing expectations

This recovery is not a new user-facing command. Its value is to validate a production behavior the ordinary user already expects: when a one-call research presentation contains a clearly identifiable, safely repairable projection problem, the system should be able to use its real visual-review feedback once, make a bounded source-faithful correction, and return better pixels without asking the user to hand-edit a slide.

A successful 043 still does not authorize the next real-paper batch automatically. It means the generic recovery prompted by 041 has enough evidence to be presented to the user. The Program must then enter the required human decision gate before spending another fresh four-paper unseen batch.

## Out of scope

- Any new Stage 5 paper selection, acquisition, source-bundle freeze or holdout rendering.
- Reopening or beautifying 038/041 failed holdouts.
- Adding mature gold records, scouting new presentation references or changing gold quality thresholds.
- Expanding the canonical scientific-object ontology beyond what 042 already shipped.
- Adding new repair intents, second repair cycles, general fallback cards or unrestricted layout search.
- Changing the Terra rubric, suppressing legitimate findings, manually editing final pixels/TeX after review, or treating synthetic review JSON as real visual evidence.
- Redesigning the exact CUHK template or unrelated presentation features.
