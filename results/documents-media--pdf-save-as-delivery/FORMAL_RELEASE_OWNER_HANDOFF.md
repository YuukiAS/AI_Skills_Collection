# Formal Release Owner Handoff — PDF Save-as Delivery

## Current truth

The bounded PDF task itself is complete at the product/reviewer layer:

- Reviewed Handoff state: `PASS`
- REVIEW_2: `PASS`
- D1/D2/D3: `PASS`
- broad main-vs-candidate differential regression: `PASS`
- final PDF first-completion delivery event: observed and bound to the accepted final candidate
- tracking Issue: #101 remains open / DOING only because formal integration/release closure is not complete

This task is **not** a product BLOCKED state and must not reopen PDF implementation or create REVIEW_3.

## Why formal release is not owned here

Latest checked formal refs during integration preflight:

- `origin/release = 06d135d8a6ee62cd41abb40fc5771fcef7f8db25` (formal repository 5.4.4)
- `origin/main = 362a8cab6991120a79600352d070926e2602dcbd`

`origin/release..origin/main` contains unrelated class-C production/generated drift. A fresh repository-level classification found 35 production/release-relevant paths, including Project Instructions Editor source/tests and generated Presentations / Research Authoring payloads. The PDF task is forbidden to absorb, revert, cherry-pick around, or silently release those owners.

The release-channel owner is the existing AI Skills Maintainer capability:

`ai-skills-repository-maintainer`

per:

`skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`

and:

`skills/core/codex-system/machine-update-orchestrator/references/formal-release-and-update-impact.md`.

Only a separately authorized formal release closure may advance the AI_Skills `release` ref.

## PDF task identities to preserve

- task branch: `reviewed/documents-media--pdf-save-as-delivery`
- accepted PDF implementation: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- REVIEW_2 PASS commit: `c06bcac136a0bcc87e400c17bc3789299c7551c4`
- integration preflight evidence: `results/documents-media--pdf-save-as-delivery/INTEGRATION_RELEASE_PREFLIGHT.md`
- accepted standalone skill intent: `render-chinese-math-pdf 0.2 -> 0.3`
- accepted PDF final artifact SHA-256:
  `5e51c6873d8ff64ee68fd49b45dd881a043b48073496ca7987fbc06696f35d50`
- Issue #101: keep open / DOING until truthful formal integration/release closure

## Correct recovery

Do not keep the PDF Executor/Reviewer alive waiting for unrelated repository work.

A future **explicitly authorized formal AI_Skills release task** owned by
`ai-skills-repository-maintainer` must:

1. refresh exact `origin/release` and `origin/main`;
2. inventory all class-C production/generated changes between them;
3. prove which of those changes have their own completed review/release evidence;
4. construct one coherent formal repository release candidate rather than letting the PDF task silently absorb unrelated work;
5. apply the repository version/changelog/generated-parity contract;
6. validate the exact formal release candidate;
7. advance `release` only through the fast-forward-only formal producer path when the entire release candidate is truthfully closed;
8. then return to Issue #101 / this task only for the mechanical final integration/release closure and task-branch cleanup.

If `release` advances compatibly before that owner handoff runs, rerun the existing PDF integration preflight directly; no new PDF Planner/Critic/product review is required merely because the formal baseline advanced.

## Do not claim

Do not claim that the unrelated class-C drift is fixed, approved, or release-ready merely because the PDF task is PASS.

Do not move `main` or `release` from this PDF task.

Do not create a successor PDF task.

Do not reopen D1–D3 or REVIEW_2 without new contrary evidence.
