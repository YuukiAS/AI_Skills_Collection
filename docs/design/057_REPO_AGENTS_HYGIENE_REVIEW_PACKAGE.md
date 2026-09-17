# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_INTEGRATION_PACKAGE_CRITIC_REVIEW`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Approved design proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Approved bounded versioning amendment: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Implementation Plan/Goal v0.2: already executed and independently reviewed
- Final reviewed implementation evidence: `E3 = 745281b70322b8508e43e59a5bdef70529749ea5`
- Final reviewed implementation manifest: `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`
- Integration Plan: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.1
- Integration Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md` v0.1
- Integration Kickoff Draft: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md` v0.1
- Stage: separately approved integration preparation

## Implementation review closure

Independent Critic accepted the repaired final implementation tuple and closed:

- C057-I1 Bridge H8 raw-byte preservation
- C057-I2 Bridge version/Lite closure
- C057-I3 Mica testing consolidation
- C057-I4 Asteria map conversion
- C057-I5 SeminarArc map conversion
- Bobbio consolidation
- C057-I6 historical M SHA mismatch
- H1–H9 final implementation review

Critic returned `READY_FOR_INTEGRATION = YES`. This authorizes Planner to prepare integration only; it does not authorize canonical merge/release.

## Exact reviewed tuple

- AI_Skills E3: `745281b70322b8508e43e59a5bdef70529749ea5`
- AI_Skills M3: `24051588d13f07e7f71e0edf5a723aca36754ed5`
- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date inspected only: `711fab75f044b7ad31e5ff8610c076f902ccc949`

## Current integration reality at Planner drafting

Current canonical branches were rechecked before drafting integration v0.1:

- Bridge main `cb77b1cc...` -> exact reviewed candidate is a pure fast-forward.
- Bobbio develop `0811116a...` -> pure fast-forward.
- Mica main `aa4ce525...` -> pure fast-forward.
- Asteria main `166791c2...` -> pure fast-forward.
- SeminarArc main `71c59d39...` -> pure fast-forward.
- Lucerna main `852a4a8c...` has advanced since the 057 base; exact reviewed candidate changes only `AGENTS.md`, while current post-base changes do not touch `AGENTS.md`; current evidence supports a clean merge commit with no manual reconciliation.
- AI_Skills main `c82f9a3c...` has advanced since the 057 base; exact M3 branch adds only `results/057_repo_agents_hygiene/*`, while current-main post-base changes are in planning/TODO docs; current evidence supports a clean merge commit with no manual reconciliation.

Execution must re-fetch all canonical refs. Relevant drift/conflict is a stop condition, not authorization to modify reviewed content.

## Integration strategy

- Use exact reviewed SHAs, not rewritten equivalents.
- Fast-forward cases use `git merge --ff-only <EXACT_SHA>`.
- AI_Skills/Lucerna use `git merge --no-ff --no-commit <EXACT_SHA>` only if execution-time preflight still proves a clean, non-overlapping mechanical merge; inspect before committing. Any conflict or relevant semantic drift => abort/stop.
- No squash/rebase/cherry-pick/force push/history rewrite.
- No task-branch deletion.
- CUHK Date remains unchanged.

## Bridge boundary

Bridge `0.8.3` may become canonical source metadata on `main` only through approved integration. Integration does not authorize tag, GitHub Release, package publication, deployment, Host Policy installation/update, or a `0.8.4` bump.

## Relationship to 056

After approved 057 integration:

`Planner bounded 056 source-drift revalidation -> remove 057-completed duplicate work -> refresh exact refs/Bridge version slot -> narrow Critic review -> only then execute amended 056 package`.

Integration must not edit or execute 056.

## Hard boundary

This package is still a review object. No canonical merge/push has been authorized by this file.

Only if independent Critic returns both:

```text
RESULT = PASS
READY_FOR_INTEGRATION_CODEX = YES
```

for the exact integration v0.1 Plan + Goal + Kickoff may the user send the approved Integration Kickoff and authorize the merges.

`NEXT_HANDOFF = CRITIC`
