# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_INTEGRATION_PACKAGE_CRITIC_R2`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Approved design proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Approved bounded versioning amendment: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Implementation Plan/Goal v0.2: executed and independently reviewed
- Final reviewed implementation evidence: `E3 = 745281b70322b8508e43e59a5bdef70529749ea5`
- Final reviewed implementation manifest: `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`
- Integration Plan: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.2
- Integration Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md` v0.2
- Integration Kickoff Draft: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md` v0.2
- Integration Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_CRITIC_PROMPT_2026-09-17.md`
- Stage: separately approved integration package R2

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

## Integration package review history

### v0.1

Package commit:

`0d84bf541800c1b0bc39d8f15c0a17f72905b1fd`

Critic decision:

```text
RESULT = REVISE
READY_FOR_INTEGRATION_CODEX = NO
```

Only stable blocker:

`C057-G1-CLEAN-CANONICAL-WORKTREE-GATE`

The already-reviewed integration architecture was otherwise accepted:

- Bridge/Bobbio/Mica/Asteria/SeminarArc = exact `FF_ONLY` cases;
- AI_Skills/Lucerna = exact clean mechanical merge cases;
- no squash/rebase/cherry-pick/force/history rewrite;
- truthful partial-integration recovery;
- Bridge `0.8.3` source-only boundary;
- no repeated 363 tests/H1–H9;
- no 056 mutation.

### v0.2 response — C057-G1 ACCEPT

v0.2 changes only preflight/recovery semantics.

Before any canonical merge/push, every mutable repo's selected canonical checkout must prove:

- correct canonical branch/HEAD;
- no unfinished merge/rebase/cherry-pick/revert/bisect or equivalent Git operation;
- no pre-existing staged index changes;
- no pre-existing unstaged tracked changes;
- no untracked path conflicting with candidate paths, merge outputs, or checkout/merge targets.

Observable status such as `git status --porcelain` must be recorded.

Dirty/staged user work is a stop condition. Integration may not stash, reset, clean, commit, relocate, overwrite, or absorb that work. Conflicting/ambiguous untracked files are also a stop condition.

The gate applies to fast-forward cases as well as AI_Skills/Lucerna clean merges, and all repos must pass it before the first canonical push. Therefore `git merge --abort` for the diverged cases starts from a known-clean recovery baseline rather than unknown local modifications.

No exact tuple, target branch, merge strategy, push order, Bridge boundary, validation scope, or 056 boundary changed.

## Current integration strategy frozen for R2

- exact reviewed SHAs only;
- `FF_ONLY`: Bridge/Bobbio/Mica/Asteria/SeminarArc;
- `CLEAN_MERGE`: AI_Skills/Lucerna, only after non-overlap + clean canonical checkout/index preflight;
- all repo preflight before first canonical push;
- no automatic dirty-work manipulation;
- no task-branch deletion or PR;
- CUHK Date unchanged;
- Bridge `0.8.3` source integration only, no tag/release/package publish/deploy/Host install/`0.8.4`;
- successful integration leads only to bounded 056 source-drift revalidation.

## Hard boundary

This package remains a review object. No canonical merge/push is authorized by this file.

Only if independent Critic returns:

```text
RESULT = PASS
READY_FOR_INTEGRATION_CODEX = YES
```

for the exact integration v0.2 Plan + Goal + Kickoff may the user send the approved Integration Kickoff and authorize canonical integration.

`NEXT_HANDOFF = CRITIC`
