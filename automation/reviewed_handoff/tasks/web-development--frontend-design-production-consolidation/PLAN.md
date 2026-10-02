---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: web-development--frontend-design-production-consolidation
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan — Frontend Design Production Consolidation

## Objective and value

Implement the already approved Frontend Design Production Consolidation for the existing `web-development` / Frontend Design production plugin, without reopening architecture.

Canonical semantic authority for this task is:

- Architecture: `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md` @ `effa02b4e7e02f012ea24bda1683857609a09fe1`
- Execution Plan v0.3: `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_3_2026-09-28.md`
- Canonical Goal v0.3: `docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_3.md`
- Kickoff v0.3: `docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_3.md`
- Approved package commit: `7d441a9997d6cff2e292066de202321a54bef2b8`
- Durable execution-ready Critic PASS: `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-28.md` @ `3bb85d32a18e2e4aa01503b4fb17b22c48e869ad`, with `RESULT=PASS` and `READY_FOR_CODEX=YES`

The existing task identity remains:

- branch: `reviewed/web-development--frontend-design-production-consolidation`
- canonical sibling worktree: `/home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation`
- base branch: `main`
- base commit recorded by CURRENT: `9d1923d2002c529352ad6464599e7da08eb6787c`

The bootstrap `REQUEST.md` Objective still contains superseded v0.1 / `/tmp` wording from the first bootstrap. That stale Objective is historical bootstrap context only. The current user instruction plus the approved v0.3 package and durable Critic PASS above are the governing execution authority. Do not recreate the old `/tmp` worktree and do not treat v0.1 as implementation authority.

The value of this task is an actually usable normal Frontend Design entry: ordinary frontend work should enter one production coordinator, scale its process to the task, respect the real design authority and target surface, and catch routine P1/P2 visual or interaction failures before the user becomes first-line QA.

## Frozen decisions

These decisions are already approved and Codex must not reinvent them.

1. `frontend-visual-systems` is the only generic production coordinator for normal Frontend Design work.
2. The shared aggregate generator gains one minimal opt-in coordinator-first mode:
   - `routing_mode = coordinator-first`
   - `coordinator_artifact_id = system`
   - aggregates that do not opt in retain their existing choose-one behavior.
3. Do not create a new orchestrator Skill, plugin, workflow, state machine, ledger, or alternate frontend architecture.
4. The main Frontend aggregate routes through the coordinator and may delegate to:
   - `product-ux-planning`
   - `visual-direction`
   - `design-system-tokens`
   - `figma-design-to-code`
   - `motion-interaction`
   - `responsive-accessibility-review`
   - `webapp-testing`
   - `research-product-frontend`
5. `product-ux-planning` is a generic coordinator delegate. It must not remain owned only by a peer research aggregate that can bypass the coordinator.
6. `research-product-frontend` remains a research-specific specialist source; its canonical Skill is retained, but it is not a second generic owner.
7. `frontend-reference-research` remains a narrow explicit entry and is not replaced by the coordinator.
8. `webapp-testing` is a narrow browser evidence companion, not a design owner.
9. `implementation-react-tailwind` remains a downstream builder/profile capability, not part of the Frontend Design ownership aggregate. A discovered design gap returns to P0/P1.
10. Preserve the approved delivery loop:
    - P0: product/state contract
    - P1: design authority + whole-screen direction
    - P2: implementation handoff
    - P3: actual-surface convergence + producer self-QA
    - P4: whole-product taste + independent confirmation when required
11. Preserve gates F-A / F-B / F-C / F-D:
    - F-A: product/state/design-authority coverage
    - F-B: design-system coherence
    - F-C: actual-surface/evidence fidelity
    - F-D: producer self-QA and independent-review admission
12. Preserve scale-down:
    - S1 targeted/local fix
    - S2 bounded UI change
    - S3 product/redesign
    - design authority and target surface are orthogonal modifiers, not extra size classes.
13. Design authority may be canonical Figma, another durable authority, or current production grammar where appropriate. Figma is conditional authority, not mandatory for every frontend task. No-Figma work must remain a normal supported path.
14. Preserve browser vs native-WebView evidence boundaries. Browser evidence proves browser behavior; native claims need native evidence appropriate to the claim.
15. Preserve producer severity:
    - P1 blocks or risks core flow, state correctness, or evidence truth.
    - P2 is a substantial visible confusion/friction/hierarchy/consistency defect.
    - P3 is deferrable polish.
    Producer self-QA is admission to independent review, not independent quality proof.
16. Preserve handoff action reachability: when a handoff asks the user to click/select/expand/save/authorize a control and the producer can safely exercise it, verify visibility, enabled state, real interaction, expected next state or user-only boundary, and no obvious P2 before handing it to the user.
17. Preserve whole-product taste as observable judgment, not a mechanical keyword/test gate.
18. Preserve retained semantics:
    - #52: icon source/registry/component, generic-vs-brand split, optical normalization, accessibility/theme, third-party source/license/provenance.
    - #62: design authority → implementation → actual surface → F-D admission → confirmation; applies with or without Figma.
    - #69: interaction causality belongs to F-C; ordinary browser locator/actionability + postcondition is enough unless there is a competing route/control-path claim.
19. The current real-project replay set is exactly Bobbio, Lucerna, Asteria. Do not add Mica for ChatGPT, SeminarArc, or a synthetic fourth project to chase maturity.
20. Compatibility/regression evidence is not automatically plugin-originated capability evidence. Repo-local rules that already give the answer count as compatibility unless the normal Frontend coordinator independently makes a generic P0/P1/P3/F-D decision not directly supplied by that repo.
21. `web-development` maturity remains `unclassified` in this task.
22. Current release baseline is repository `5.3.0`, `web-development 0.2`. If that baseline remains, successful production release closure is repository `5.3.1` and `web-development 0.3`, with all other central plugins `NO_BUMP`. If canonical main has a formal release advance first, follow the existing version policy using the then-current compatible repository PATCH and next two-part `web-development` version. There is no legal completed-production path with `NO_BUMP`.
23. Existing branch/worktree are reused. Do not second-bootstrap, raw-add, move, remove, or recreate the task worktree. If it later needs rematerialization, only use the current artifact-bound `materialize-worktree --mode resume` contract.
24. Do not modify Bridge Kit.

## Positive completion

This task is positively complete only when one same final Frontend Design candidate demonstrates all of the following user-visible/repository-observable outcomes:

1. A normal Frontend Design request enters the generated `frontend-visual-systems` coordinator first rather than a generic choose-one specialist route.
2. The coordinator correctly selects task scale, design authority, target surface, and needed delegates, while S1/local fixes remain light-weight and S3 redesigns receive the full closure path.
3. The generated production payload actually encodes coordinator-first routing; this is not satisfied by source prose alone.
4. Existing non-opt-in aggregates preserve their prior choose-one semantics and the shared generator does not cause unrelated Marketplace/plugin drift.
5. Canonical-Figma, other-durable-authority, and no-Figma cases all remain usable; browser-only work is not forced through native gates and native claims are not justified by browser fixtures.
6. Producer self-QA removes routine P1/P2 defects before independent review/user handoff, including safe handoff-action reachability where applicable.
7. Ownership remains coherent: product UX, whole-screen direction, design tokens/components/icons, Figma handoff, motion, responsive/accessibility, browser evidence, and research-specific UI constraints are handled by their approved owners rather than duplicated into a giant coordinator rule wall.
8. The Bobbio, Lucerna, and Asteria read-only replays use the production candidate through the normal coordinator entry, preserve project authority, record coordinator→delegate source consumption, and report capability attribution honestly.
9. The same final candidate passes all G1–G7 evidence and regression requirements, full required repository validation/CI, version/changelog/README/generated parity closure, and the independent implementation review path.
10. No forbidden scope is changed.

Tests, schemas, generated-file existence, CI, or replay plumbing alone do not establish completion. The maximum claim supported by this Plan is that the released Frontend Design production entry implements and survives the approved coordinator-first workflow and the three frozen real-project compatibility/attribution replays. This task does not support a claim that `web-development` has advanced beyond `unclassified` maturity, nor that every future frontend platform has been validated.

## Non-substitutable semantics

The following semantics cannot be weakened or silently substituted:

- Normal generic Frontend Design entry must be coordinator-first in the generated production plugin; a source-only checklist, `workflow_notes`, prompt convention, or choose-one aggregate is not equivalent.
- The coordinator must be the existing `frontend-visual-systems` Skill; do not substitute a new orchestrator.
- Default aggregate behavior outside the explicit Frontend coordinator-first opt-in must remain choose-one.
- S1/S2/S3 scale-down must remain real; tiny/local fixes cannot be forced through a full P0–P4 ceremony.
- Figma must remain conditional. A no-Figma project must still complete through another durable authority or, for appropriate S1/limited S2 cases, current production grammar.
- Browser/native evidence scope must match the claim. Browser fixtures cannot substitute for native evidence where the claim is native.
- Handoff action reachability cannot be deferred to the user when the action can be safely pre-exercised by the producer.
- Producer `P1=0/P2=0` without exact-candidate/evidence binding is not sufficient admission evidence.
- Independent review remains mandatory for substantive redesign, baseline/release capability gates, major canonical-design convergence, major native user-flow milestones, or whole-product hierarchy/interaction-model changes.
- #52, #62, and #69 semantics above must survive implementation.
- Bobbio/Lucerna/Asteria repo-local rules must not be relabeled as plugin-originated maturity evidence.
- The three replay prompts/refs/rubrics must be frozen before final replay; do not adaptively replace failed examples.
- Final release evidence must come from the same final candidate; do not splice winning evidence from different commits.
- Completed production behavior change requires the approved release bump; recovery docs alone do not bump.
- Current task branch/worktree identity and Bridge role ownership are fixed. Executor cannot rewrite this PLAN or self-authorize a new Planner decision.

## Implementation scope

Implement only the approved bounded production refinement.

Allowed production source areas:

- `skills/tools/frontend/frontend-visual-systems/**`
- `skills/tools/frontend/product-ux-planning/**`
- `skills/tools/frontend/visual-direction/**`
- `skills/tools/frontend/design-system-tokens/**`
- `skills/tools/frontend/figma-design-to-code/**`
- `skills/tools/frontend/motion-interaction/**`
- `skills/tools/frontend/responsive-accessibility-review/**`
- `skills/tools/frontend/webapp-testing/**`
- `skills/tools/frontend/research-product-frontend/**`
- `skills/tools/frontend/implementation-react-tailwind/**` only if needed for the approved downstream handoff boundary
- `scripts/build_codex_marketplace.py`
- `scripts/codex_marketplace_config.json`
- directly necessary tests and repo-safe fixtures

Generated layer may change only through the existing generator:

- `.agents/plugins/marketplace.json`
- `plugins/codex/plugins/**`

Task evidence and eventual release closure may use:

- `results/web-development--frontend-design-production-consolidation/**`
- `docs/plugin-changelogs/web-development.md`
- `CHANGELOG.md`
- `README.md`
- `VERSION`
- directly related version/parity tests
- `docs/plugin-todos/web-development.md` only when later closure rules actually permit TODO mutation; do not close #52–#72 merely because Executor implementation/tests pass.

Specific implementation ownership:

- coordinator: P0–P4, F-A–F-D, S1–S3, authority/surface classification, delegate routing, repair routing, admission/convergence
- product UX: product job, primary states, actionability/lifecycle, normal-vs-diagnostic boundary, visible metric/ranking semantics
- visual direction: whole-screen freeze/composition and observable taste questions
- design-system tokens: component craftsmanship, #52 icon sourcing/registry/provenance, semantic typography/color/status grammar
- Figma handoff: conditional design authority, completeness, round-trip, final convergence
- motion: motion intent vs runtime latency/jank boundary; no universal cross-project numeric budget is invented
- responsive/accessibility: applicable P1 constraints and P3 closure
- webapp testing: browser evidence companion and F-C boundary; never native design authority
- research product frontend: domain-specific research UI constraints only
- React/Tailwind implementation skill: downstream implementation boundary only

Generator implementation is the approved minimal opt-in extension:

```text
routing_mode = coordinator-first
coordinator_artifact_id = system
```

For `web-development`, the main Frontend aggregate contains the coordinator plus the approved delegates above. The current separate research aggregate must no longer provide a generic peer route that bypasses the coordinator, while the canonical research specialist source remains available as a delegate. `frontend-reference-research` remains a narrow explicit entry.

Do not merge/rebase main into this task merely to copy planning documents into the branch. The task-local PLAN is the frozen runtime contract; canonical package/critic commits above are immutable authority locators.

## Acceptance and regression gates

The exact final candidate must pass all seven approved gates. Gate names and semantics are frozen.

### G1 — Normal Entry / Coordinator Routing

Prove the generated main Frontend aggregate is coordinator-first with coordinator artifact `system`; normal generic UI requests cannot bypass the coordinator through the research specialist; `webapp-testing` is reachable only as evidence companion; `implementation-react-tailwind` is not promoted to design owner. Record real coordinator/delegate source consumption in candidate replay.

### G2 — Coordinator Decision / Scale / Authority

Freeze deterministic regressions for at least:

- S1 browser local fix using current grammar without forced Figma/independent review
- S2 bounded UI change with durable authority
- S3 redesign using full P0–P4
- canonical-Figma material design change
- no-Figma durable-authority completion
- native-WebView evidence matched to native claim
- implementation drift that should not force design-source churn

These development regressions may prove implementation behavior but do not count toward maturity.

### G3 — Visual-System / Ownership Fidelity

Preserve the approved owner semantics including #52, #55/#66/#68/#71/#72, #57/#59, #58/#60/#61, #62, #63/#64/#65/#70, #54, and #69. Qualitative design/taste claims require actual content/surface judgment; mechanical keyword/file checks are insufficient.

### G4 — Evidence Fidelity / Producer Admission

Cover at least:

- screenshot does not prove click
- browser fixture does not prove native behavior
- normal browser locator/actionability + postcondition does not require extra handler instrumentation
- competing route/control-path claims require stronger causality evidence
- handoff action reachability to the safe user-only boundary
- P1/P2/P3 producer verdict bound to exact candidate/surface/state evidence
- local fixes may use producer self-QA when allowed
- redesign/release/major canonical/native milestones require independent review

### G5 — Shared Generator Should-Not-Change / Generated Parity

Because shared Marketplace generation changes, prove:

- non-opt-in aggregates retain the original choose-one workflow
- invalid/missing coordinator artifact configuration fails closed
- aggregate metadata union/scope/secrets/path-budget/nested-source rename/determinism do not regress
- no unintended semantic change appears in other central plugin generated payloads
- registry/catalog/Marketplace generated parity passes
- the full existing unittest suite passes

At minimum run the approved broad validation sequence:

```text
python scripts/skills.py registry --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py catalog --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest discover -s tests
```

### G6 — Bobbio / Lucerna / Asteria Real Replay + Attribution

Use only Bobbio, Lucerna, Asteria.

For every final replay:

- use the same final candidate and formal candidate plugin identity
- enter through normal Frontend Design coordinator
- use a neutral prompt that does not restate the generic rule being tested
- freeze exact project ref/prompt/rubric before final replay
- keep target projects read-only
- record coordinator→delegate route/source consumption
- store raw response, candidate identity, project ref, adjudication
- record:
  - `REPO_LOCAL_RULE_GAVE_ANSWER`
  - `COORDINATOR_GENERIC_DECISION_OBSERVED`
  - `COUNTS_AS_COMPATIBILITY`
  - `COUNTS_AS_PLUGIN_CAPABILITY`
  - evidence locator

Bobbio: respect its canonical Figma and existing P1/P2/native self-QA rules; those pre-existing answers are compatibility.

Lucerna: at the frozen ref, read at least `AGENTS.md`, `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`, `docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`, and `docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`. Existing project-local product/UI/action/self-QA answers are compatibility. Keep the 01052 handoff-action-reachability regression, but count plugin capability only where the coordinator independently makes a generic decision not directly supplied by Lucerna authority.

Asteria: respect accepted concepts and developer visual self-QA; use it primarily for browser/no-Figma should-not-overreach compatibility.

If all three only prove compatibility, G6 may still pass as compatibility/regression, and maturity remains `unclassified`.

### G7 — Final Candidate / Release Metadata / Human-Facing Closure

Do not bump versions at the start of implementation. After implementation + known regressions + broad compatibility stabilize and before final-candidate freeze:

- reread the current version policy and then-current canonical release metadata
- if baseline is still repository `5.3.0`, `web-development 0.2`, bump exactly once to repository `5.3.1`, `web-development 0.3`
- if a formal main release has advanced, use the then-current compatible repository PATCH and next two-part `web-development` version
- all other central plugins remain `NO_BUMP`
- maturity remains `unclassified`
- synchronize `web-development` changelog, root CHANGELOG, README, VERSION, version tests, generated manifests
- regenerate, then freeze final candidate
- rerun G1–G7 on that same versioned final candidate
- if later review requires repair, keep the same already-selected release version; do not bump again

README closure is mandatory.

Because `CURRENT.ci_required=true`, Executor handoff after a valid implementation/result commit must follow the Reviewed Handoff CI path: publish the exact reviewed branch with `ci_status=PENDING` and enter `WAITING_FOR_CI`, not bypass CI directly to Reviewer. The later Reviewer must inspect the frozen Plan, real implementation diff, required CI, replays/evidence, and final candidate.

## Natural-language usage / routing expectations

Representative normal-use expectations after implementation:

- “Redesign this dashboard/page” → normal Frontend Design entry → coordinator → S3 when it is a true redesign → product/visual/tokens/Figma or non-Figma authority/delegates as needed → actual-surface QA → independent confirmation.
- “Implement this canonical Figma screen” → coordinator recognizes Figma authority and delegates Figma handoff; project semantics still come from the project, not Figma.
- “Fix the spacing/alignment on this existing button” → coordinator classifies S1 and uses current production grammar; do not force a full redesign ceremony.
- “Review this native tray UI before asking me to click Choose folder” → native evidence boundary + producer self-QA + safe handoff-action reachability before user handoff.
- “Plan a research-product interface” → coordinator first performs generic product/authority/surface classification, then delegates research-specific constraints to `research-product-frontend`; the specialist does not bypass the coordinator.
- “Review this browser product with no Figma file” → no-Figma path is normal; use current durable authority and browser evidence, without inventing native/Figma gates.

## Out of scope

Do not:

- redesign or amend Frontend Design Proposal v0.3
- create another orchestrator Skill/plugin/workflow
- modify Bridge Kit, Host Policy, or execpolicy
- modify Clear Writing / `writing-style` production behavior
- implement the deferred Product UI Copy content-architecture work
- implement writing-style #17, #20, or #13
- perform CUHK Date Product UI Copy naturalness work
- modify Bobbio, Lucerna, Asteria, Mica for ChatGPT, or SeminarArc source
- add a fourth synthetic/real replay merely to chase maturity
- promote `web-development` maturity
- use paid reviewer/API/Terra without separate authorization
- introduce new credential/provider/private-data scope
- force push, rebase/history rewrite, delete the branch, or perform destructive Git recovery
- create another task/branch/worktree or second-bootstrap this task
- merge to `main`, update the release ref, create a PR, or perform final integration without later explicit authorization
- close #52–#72 merely because implementation/tests pass
- use mechanical tests/CI/generated parity as a substitute for actual qualitative frontend/evidence review
