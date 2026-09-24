---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: workflow-core--reviewed-first-bootstrap-normal-entry
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Complete the already approved AI_Skills consumer side of Bridge 0.9.1 Reviewed
Handoff first-bootstrap recovery. Verified Workflow should route brand-new
Reviewed tasks through the canonical Bridge bootstrap entry and route existing
tasks through Bridge resume/materialization, without raw Git fallback.

## Frozen decisions

- Bridge commit `a41c2e32c630aaf2a200ca336f04c4ea31650786` is the validated
  recovery candidate.
- AI_Skills base main is `b725c7e5d812732f34f2704509eecbd095388ca8`.
- Canonical source owner is
  `skills/core/codex-system/codex-workflow-protocol/SKILL.md`.
- Brand-new Reviewed task route:
  `ai-bridge reviewed-handoff task bootstrap`.
- Existing local or exact reviewed remote task route:
  `ai-bridge reviewed-handoff materialize-worktree --mode resume`.
- Missing or old Bridge capability/version/policy support must fail early
  before substantive implementation.

## Positive completion

The repository-visible outcome is a workflow-core release candidate whose
source and generated Marketplace payload carry the routing contract, whose
version/changelog/README/repository release metadata are consistent, and whose
candidate replay proves the generated plugin payload is loaded by normal
candidate replay.

The maximum claim scope is workflow-core consumer routing. This does not claim
new Bridge mechanics, main integration, tag/release publication, or workflow-core
production installation outside this candidate branch.

## Non-substitutable semantics

- Do not use raw `git worktree add` as a normal fallback.
- Do not use alternate worktrees, `/tmp` replacement paths, second clones,
  remote remaps, or locally forged REQUEST/CURRENT metadata.
- Do not implement Bridge-owned Git mechanics in workflow-core.
- Do not add another root `AGENTS.md` synonym for an already covered policy.

## Implementation scope

Allowed files are workflow-core source/generation outputs, routing tests,
version/release metadata, README/root changelog, workflow-core changelog, and
task-local evidence under
`results/workflow-core--reviewed-first-bootstrap-normal-entry/`.

## Acceptance and regression gates

- Source and generated workflow-core payload contain the bootstrap/resume/early
  fail routing contract.
- Marketplace config and generated plugin manifest show `workflow-core 0.4`.
- Repository release metadata shows `5.1.1` PATCH.
- Targeted workflow-core/Marketplace/version tests pass.
- Generated layer validation passes.
- Candidate replay proves `workflow-core@ai-skills-candidate` v0.4 was loaded
  from commit `c17214449d8ca8761664ff15d49140c692a0fcb1`.
- FB-G4 remote-only/idempotent resume uses Bridge `materialize-worktree --mode
  resume` and does not pollute canonical main.
- Full unittest residual failures, if any, must be reported with attribution.

## Natural-language usage / routing expectations

- "Start this exact new Reviewed task" means use Bridge task bootstrap when the
  task is truly absent.
- "Resume this existing Reviewed task" means use Bridge materialize-worktree
  resume when local metadata or exact reviewed remote metadata exists.
- "Bridge is too old or missing this command" means stop before implementation
  and report an actionable capability blocker.

## Out of scope

No Bridge source changes, Host Policy changes, main integration, release/tag,
PR creation, branch deletion, paid API, workflow-core redesign, new workflow
state/schema, raw Git fallback, or root AGENTS rule duplication.
