# 057 Repo AGENTS Hygiene — Integration Goal

- Task key: `057_repo_agents_hygiene`
- Integration package version: `v0.2`
- Status: `AWAITING_INTEGRATION_CRITIC_R2`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.2
- Kickoff: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md` v0.2
- Stable blocker addressed: `C057-G1-CLEAN-CANONICAL-WORKTREE-GATE`

This Goal is not executable until independent Critic reviews this exact v0.2 integration Plan + Goal + Kickoff, returns `READY_FOR_INTEGRATION_CODEX=YES`, and the user then sends the approved Kickoff.

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

## 2. Unified preflight before any canonical push

All mutable repos must complete preflight before the first canonical push.

For each repo:

- fetch canonical and existing `reviewed/057_repo_agents_hygiene` refs;
- verify reviewed branch head equals the exact reviewed candidate SHA (AI_Skills reviewed branch = M3);
- verify canonical branch identity/freshness and detect relevant drift;
- confirm the approved integration relation remains valid (`FF_ONLY` or `CLEAN_MERGE`);
- compare merge base and candidate/current changed paths as needed.

Relevant semantic drift, overlapping candidate-path change, reviewed-branch head drift, or merge conflict stops integration and returns to Planner/Critic. No candidate repair is authorized.

### Clean canonical checkout/index gate

The exact canonical checkout selected for integration must additionally prove:

- checked-out branch and HEAD are the intended canonical branch/head;
- no merge/rebase/cherry-pick/revert/bisect or equivalent unfinished Git operation is active;
- index has no pre-existing staged changes;
- tracked working tree has no pre-existing unstaged changes;
- untracked files do not conflict with candidate paths, merge outputs, or checkout/merge targets.

Record `git status --porcelain` or equivalent observable evidence.

If unrelated dirty/staged user work is present, do not stash, reset, clean, commit, move, overwrite, or include it in integration. Stop that repo and report the exact dirty state. Conflicting or ambiguous untracked files also stop the repo; do not delete them.

This gate applies to fast-forward repos and clean-merge repos alike.

## 3. Merge contract

### Fast-forward cases

Bridge, Bobbio, Mica, Asteria and SeminarArc remain frozen `FF_ONLY` cases. If current canonical is still an ancestor of the exact reviewed candidate and the clean-state gate passes, use:

`git merge --ff-only <EXACT_REVIEWED_SHA>`

If fast-forward is no longer possible, stop rather than changing strategy.

### Existing divergence

AI_Skills and Lucerna remain `CLEAN_MERGE` cases only when execution-time preflight confirms non-overlap and a clean canonical checkout/index.

Use `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`, then inspect the staged result and run `git diff --cached --check`.

Commit only if the result is fully mechanical, the exact candidate is preserved, no unrelated/pre-existing content entered the index, and no manual reconciliation is needed.

Conflict or semantic uncertainty => `git merge --abort` and stop. The clean-state gate must pass before starting so abort has a credible recovery baseline.

No squash, rebase, cherry-pick, force push, or history rewrite.

## 4. Push order and partial-integration contract

Complete all source/drift/identity/clean-worktree preflights across all mutable repos before the first push.

Keep the frozen push order:

1. Bobbio
2. Mica
3. Asteria
4. SeminarArc
5. Lucerna
6. Bridge
7. AI_Skills

If a remote advances after preflight and push is rejected, fetch and stop that repo. Never force push.

If earlier repos already integrated successfully, keep that published history and report truthful partial integration; do not rewrite history to simulate atomicity.

## 5. Bridge boundary

Bridge `0.8.3` source integration to `main` is allowed only after approved Kickoff. It does not authorize tag, GitHub Release, package publish, deployment, Host Policy install/update, branch deletion, or `0.8.4` bump.

## 6. Completion evidence

After each successful integration report:

- canonical old head;
- canonical new head;
- exact reviewed candidate reachability;
- integration mode (`FF_ONLY` or `CLEAN_MERGE`);
- relevant `git diff --check` result;
- no-extra-file / no-manual-content-change confirmation;
- clean-state preflight evidence recorded before merge.

For `FF_ONLY`, new canonical head must equal the exact candidate SHA.

For `CLEAN_MERGE`, the merge commit must contain the exact reviewed candidate in ancestry and must not contain manual or unrelated content.

Do not add integration-result commits to target repos merely to record status.

Implementation/H1–H9 already passed; do not rerun Bridge 363 tests, H1–H9, product tests, GPT Work, or paid checks unless a newly observed canonical drift invalidates the reviewed evidence. Such drift is a stop condition, not authorization to restart development.

## 7. Prohibitions

Do not:

- edit any reviewed candidate content;
- modify CUHK Date;
- start or amend 056;
- delete reviewed branches;
- create new branches/worktrees/PRs;
- force push/rebase/squash/cherry-pick/history-rewrite;
- stash/reset/clean/commit unrelated local work to make integration proceed;
- tag/release/publish/deploy/install Bridge;
- run paid APIs;
- create new workflow/state/schema/ledger/controller/watcher.

## 8. Recovery

- dirty/staged canonical checkout or unfinished Git operation -> stop before integration and preserve user work unchanged;
- conflicting untracked path -> stop, do not clean/delete/overwrite;
- fast-forward precondition false -> stop;
- merge conflict/relevant drift -> abort from the verified clean baseline and stop;
- push rejection due remote advancement -> fetch, never force, and re-evaluate;
- partial cross-repo success -> keep successful integrations, report exact state, do not rewrite history.

## 9. End state

After all canonical integrations are verified:

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`

057 integration itself must not perform 056 changes.
