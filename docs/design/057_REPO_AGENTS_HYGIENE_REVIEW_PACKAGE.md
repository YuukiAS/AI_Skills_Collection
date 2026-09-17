# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_INTEGRATION_RECOVERY_CRITIC_REVIEW`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Approved design proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Approved bounded versioning amendment: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Implementation Plan/Goal v0.2: executed and independently reviewed
- Final reviewed implementation evidence: `E3 = 745281b70322b8508e43e59a5bdef70529749ea5`
- Final reviewed implementation manifest: `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`
- Prior Integration Plan/Goal/Kickoff: v0.2, execution attempted then blocked by local canonical-checkout preflight
- Current recovery proposal: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md`
- Current recovery Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_CRITIC_PROMPT_2026-09-17.md`
- Stage: lighter per-repo integration recovery review

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

The reviewed implementation tuple remains frozen and is not being reopened.

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

## Integration package history

Integration v0.1 was REVISE on `C057-G1-CLEAN-CANONICAL-WORKTREE-GATE`.

Integration v0.2 closed that design blocker by requiring every canonical local checkout to be clean before any cross-repo push. Critic later approved that package and the user sent the approved integration Kickoff.

During real execution, the globally coupled clean-canonical-checkout rule blocked repeatedly on **unrelated local state**, not candidate drift:

- AI_Skills ordinary local `main` is stale/diverged with unrelated old 044 commits and must not be reset/rebased/cleaned for 057;
- Bridge ordinary local `main` has a pre-existing `.gitignore` modification and must not be stashed/reset/cleaned/committed for 057.

No canonical integration push was performed by that blocked run.

## Recovery direction now under review

Planner proposes replacing only the local integration execution surface:

1. **Five current fast-forward repos** — Bridge, Bobbio, Mica, Asteria, SeminarArc:
   - do not use/clean canonical local checkout;
   - verify exact reviewed remote ref and remote canonical ancestry;
   - push the exact immutable reviewed SHA directly to the canonical remote branch without force;
   - remote non-fast-forward rejection remains the concurrent-advancement guard.

2. **Two diverged repos** — Lucerna, AI_Skills:
   - do not repair/use problematic canonical local checkout;
   - use the existing reviewed 057 worktree only if that worktree itself is clean;
   - detach at current `origin/main`, make the already-approved no-manual-edit mechanical merge, push `HEAD:main`, then switch back to the reviewed branch;
   - no new branch/worktree.

3. Execute **repo by repo**, not as a globally coupled all-repo preflight. Partial integration remains truthful and already accepted as a possible cross-repo outcome.

The proposal includes seven exact repo-specific prompts so one Critic review can approve the whole recovery set; it should not require seven separate architecture/recovery reviews.

## Current remote facts rechecked for recovery drafting

- AI_Skills remote `main = d73684fe59f2866d551fcbfae750cada4b3fd4ae`; reviewed branch = `M3` exactly; histories diverged, with M3-side changes limited to `results/057_repo_agents_hygiene/*`.
- Bridge remote `main = cb77b1cc5a1fce097a38066d2db452291e359852`; reviewed branch = `e1d6b781...`; exact fast-forward remains valid.
- Bobbio `develop` -> exact candidate: fast-forward.
- Mica `main` -> exact candidate: fast-forward.
- Asteria `main` -> exact candidate: fast-forward.
- SeminarArc `main` -> exact candidate: fast-forward.
- Lucerna current remote `main` has advanced beyond the 057 base, but main-side post-base changes still do not modify the reviewed candidate path `AGENTS.md`; reviewed branch remains exact `41cd1297...`.

Execution must still fetch current refs in each repo prompt. A repo whose preconditions no longer hold stops independently.

## Frozen boundaries

Unchanged:

- no candidate content mutation;
- no I1-I6/H1-H9 rerun;
- no Bridge 363-test rerun merely for integration;
- Bridge stays `0.8.3` source-only: no tag/release/package publish/deploy/Host install/`0.8.4`;
- no CUHK Date mutation;
- no branch deletion/PR/force/rebase/squash/cherry-pick/history rewrite;
- no cleanup/stash/reset of unrelated user work;
- no paid API;
- no 056 mutation/execution during 057 integration;
- after 057 integration: bounded 056 source-drift revalidation.

## Hard boundary

The per-repo recovery prompts are not authorized until an independent Critic reviews the exact recovery proposal and returns:

```text
RESULT = PASS
READY_FOR_PER_REPO_INTEGRATION = YES
```

If PASS, the user may send the approved repo prompts independently. No repo prompt should be rewritten after PASS unless its remote preconditions have materially changed.

`NEXT_HANDOFF = CRITIC`
