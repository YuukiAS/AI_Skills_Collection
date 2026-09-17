# 057 Repo AGENTS Hygiene — Integration Goal

- Task key: `057_repo_agents_hygiene`
- Integration package version: `v0.1`
- Status: `AWAITING_INTEGRATION_CRITIC_REVIEW`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.1
- Kickoff: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md` v0.1

This Goal is not executable until independent Critic reviews this exact integration Plan + Goal + Kickoff, returns `READY_FOR_INTEGRATION_CODEX=YES`, and the user then sends the approved Kickoff.

## 1. Frozen integration target

Integrate only this reviewed tuple into canonical branches:

- AI_Skills M3: `24051588d13f07e7f71e0edf5a723aca36754ed5` (contains E3 `745281b70322b8508e43e59a5bdef70529749ea5`)
- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5` -> `main`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004` -> `develop`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829` -> `main`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970` -> `main`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90` -> `main`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be` -> `main`
- CUHK Date `711fab75f044b7ad31e5ff8610c076f902ccc949`: inspect-only; no mutation

Do not modify candidate content or create replacement candidate commits.

## 2. Preflight contract

Before any canonical push:

- fetch canonical and existing `reviewed/057_repo_agents_hygiene` refs for every repo;
- verify reviewed branch head equals the exact reviewed candidate SHA (AI_Skills reviewed branch = M3);
- verify canonical branch identity/freshness and detect relevant drift;
- confirm all planned fast-forwards remain true ancestors;
- for AI_Skills/Lucerna or any still-diverged repo, confirm changed-path/authority overlap remains absent and a clean mechanical merge is possible.

Any relevant semantic drift, overlapping candidate path change, merge conflict, or reviewed-branch head drift stops integration and returns to Planner/Critic. No manual content repair is authorized.

## 3. Merge contract

### Fast-forward only when possible

Bridge, Bobbio, Mica, Asteria and SeminarArc are planning-time fast-forward cases. Use the exact reviewed SHA and `git merge --ff-only`.

If fast-forward is no longer possible at execution time, do not silently choose another strategy; re-evaluate under the drift rule.

### Existing divergence

AI_Skills and Lucerna currently have unrelated canonical advancements. Integrate with a merge commit only if preflight confirms no relevant overlap/conflict.

Use `--no-ff --no-commit` first, inspect the mechanical result, run `git diff --cached --check`, and commit only if no manual content changes are needed. Conflict => abort and return.

No squash, rebase or cherry-pick of reviewed commits.

## 4. Bridge boundary

Bridge `0.8.3` source integration to `main` is allowed only after approved Kickoff. It does not authorize tag, GitHub Release, package publish, deployment, Host Policy install/update, or `0.8.4` bump.

## 5. Completion evidence

After each push report:

- canonical branch old head;
- canonical branch new head;
- exact reviewed candidate reachability;
- integration mode (`FF_ONLY` or `CLEAN_MERGE`);
- `git diff --check` result where applicable;
- no-extra-file / no-manual-content-change confirmation.

For fast-forward repos, new canonical head must equal the exact candidate SHA.

For merge repos, the new merge commit must preserve the exact reviewed candidate as ancestor and contain no manual reconciliation.

Do not add a new integration-result commit to any target repo merely to record status. The Executor handoff reports integration evidence; the next bounded 056 revalidation records the then-current canonical refs.

## 6. Prohibitions

Do not:

- edit any 057 candidate content;
- modify CUHK Date;
- start or amend 056;
- delete reviewed branches;
- create new branches/worktrees/PRs;
- force push/rebase/squash/cherry-pick/history-rewrite;
- tag/release/publish/deploy Bridge;
- run paid APIs;
- create new workflow/state/schema/ledger/controller/watcher.

## 7. Recovery

- relevant drift/conflict before merge -> stop before mutation;
- merge conflict -> abort merge and stop;
- push rejection due remote advancement -> fetch, never force, and re-evaluate;
- partial cross-repo success -> keep successful published integrations, report exact state, do not rewrite history to simulate atomicity.

## 8. End state

After all canonical integrations are verified:

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`

057 integration itself must not perform 056 changes.
