# 057 Repo AGENTS Hygiene — Integration Plan

- Task key: `057_repo_agents_hygiene`
- Integration package version: `v0.2`
- Stage: `AWAITING_INTEGRATION_CRITIC_R2`
- Reviewed evidence commit: `E3 = 745281b70322b8508e43e59a5bdef70529749ea5`
- Reviewed manifest commit: `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`
- Prior integration package: `v0.1` at `0d84bf541800c1b0bc39d8f15c0a17f72905b1fd`, Critic `REVISE`
- Stable integration blocker addressed here: `C057-G1-CLEAN-CANONICAL-WORKTREE-GATE`
- Design / implementation authority remains the approved 057 v2 Plan/Goal and H1–H9. This plan only integrates the already-reviewed tuple.

This plan does not authorize merge, release, tag, deployment, branch deletion, paid API, or Task 056 execution. Integration may begin only after independent Critic reviews this exact v0.2 Plan + Goal + Kickoff and returns `READY_FOR_INTEGRATION_CODEX=YES`, and the user then sends the approved Kickoff.

## 0. Critic blocker disposition

### C057-G1-CLEAN-CANONICAL-WORKTREE-GATE — ACCEPT

The v0.1 merge strategy was directionally correct but did not make a clean canonical checkout/index an explicit precondition. v0.2 adds that gate without changing the integration architecture.

Before any integration merge is attempted, every canonical checkout selected for integration must prove:

- current branch/HEAD is the intended canonical branch;
- no merge, rebase, cherry-pick, revert, bisect, or equivalent incomplete Git operation is active;
- index has no pre-existing staged changes;
- tracked working tree has no pre-existing unstaged changes;
- untracked files do not collide with candidate paths, merge outputs, or checkout/merge targets.

Use `git status --porcelain` or an equivalent observable status check and preserve the exact evidence in the Executor handoff.

If unrelated dirty/staged user work is present, do not stash, reset, clean, commit, move, overwrite, or absorb it into the merge. Stop that repo and report the exact dirty state to Planner/Critic. This rule applies to both fast-forward and non-fast-forward integration cases and must be checked for all mutable repos before the first canonical push.

For AI_Skills and Lucerna specifically, `git merge --no-ff --no-commit` is allowed only after this clean worktree/index gate passes. That gives `git merge --abort` a credible clean recovery base and prevents pre-existing staged changes from entering the mechanical merge commit.

No new integration strategy, branch, state, gate number, or recovery subsystem is introduced.

## 1. Positive target

Integrate only the exact independently reviewed 057 commits into each repository's canonical branch, without modifying reviewed candidate content or reopening 057 design.

After integration:

- Bobbio `develop` contains reviewed candidate `ab5dccb6b8b87c49671aa097233ce1bcc38be004`;
- Bridge, Lucerna, Mica, Asteria and SeminarArc canonical `main` histories contain their exact reviewed candidate commits;
- AI_Skills `main` contains reviewed `E3 -> M3` evidence history;
- CUHK Date remains unchanged;
- no task branch is deleted;
- no Bridge tag/GitHub release/package publication/Host install is performed;
- Task 056 remains untouched and moves next only to bounded source-drift revalidation.

## 2. Exact reviewed tuple

- AI_Skills E3: `745281b70322b8508e43e59a5bdef70529749ea5`
- AI_Skills M3: `24051588d13f07e7f71e0edf5a723aca36754ed5`
- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date inspected only: `711fab75f044b7ad31e5ff8610c076f902ccc949`

Historical E/M and previously revised tuples remain immutable history.

## 3. Current canonical-branch reality frozen for this package

Independent review of v0.1 already accepted the following facts; v0.2 does not reopen them:

| Repo | Canonical state at integration review | Integration form |
| --- | --- | --- |
| AI_Skills_Collection | canonical `main` has independent later history; M3 remains mechanically mergeable | `CLEAN_MERGE` |
| GPT_Codex_AI_Bridge_Kit | exact reviewed candidate remains fast-forwardable | `FF_ONLY` |
| Bobbio `develop` | exact reviewed candidate remains fast-forwardable | `FF_ONLY` |
| Lucerna | canonical `main = 852a4a8c8c67ba68ddd533b682eeb1460464140e`; post-base changes do not modify candidate `AGENTS.md` | `CLEAN_MERGE` |
| Mica-for-ChatGPT | exact reviewed candidate remains fast-forwardable | `FF_ONLY` |
| Asteria | exact reviewed candidate remains fast-forwardable | `FF_ONLY` |
| SeminarArc | exact reviewed candidate remains fast-forwardable | `FF_ONLY` |

All `reviewed/057_repo_agents_hygiene` branch heads were also independently confirmed to equal the frozen exact candidate SHAs. Execution must nevertheless fetch and re-check immediately before integration.

## 4. Unified preflight before the first canonical push

Every mutable repo must pass the entire preflight before **any** canonical push occurs.

### 4.1 Source and reviewed identity

For each repo:

1. use the existing canonical local checkout/worktree; do not create new task branches/worktrees;
2. fetch canonical and `reviewed/057_repo_agents_hygiene` refs;
3. verify `origin/reviewed/057_repo_agents_hygiene` resolves to the exact reviewed candidate SHA; AI_Skills reviewed branch must resolve to M3;
4. verify current canonical remote head, merge base, and changed paths;
5. confirm execution-time relation is still the approved `FF_ONLY` or `CLEAN_MERGE` case.

Relevant canonical advancement that touches candidate files, changes instruction/version/release authority, creates semantic uncertainty, or creates a merge conflict is a stop condition. Do not edit the candidate, cherry-pick a repair, force merge, or create another integration branch.

### 4.2 Clean canonical checkout/index gate

For the exact canonical checkout that would perform the integration, record observable Git status evidence and verify:

- checked-out branch and HEAD are the intended canonical branch/head;
- no unfinished merge/rebase/cherry-pick/revert/bisect or equivalent operation exists;
- no pre-existing staged changes exist in the index;
- no pre-existing unstaged tracked changes exist in the working tree;
- untracked paths do not collide with candidate paths, merge outputs, or files that checkout/merge would need to create/update.

`git status --porcelain` plus the relevant branch/operation-state inspection is an acceptable evidence surface; equivalent direct Git evidence is allowed.

If unrelated dirty/staged user work exists:

- do not `git stash`;
- do not `git reset`;
- do not `git clean`;
- do not commit it;
- do not move/overwrite it to make the merge proceed;
- do not include it in the integration commit;
- stop that repo and report the exact state to Planner/Critic.

Untracked files may remain only when they are proven non-conflicting with the integration. Any ambiguity is a stop condition; do not delete or overwrite them.

This clean-state gate applies equally to fast-forward repos. If the canonical checkout is unsafe, stop the repo rather than switching merge strategy.

## 5. Integration strategy

### 5.1 Fast-forward integrations

When current canonical is still an ancestor of the exact reviewed candidate and the clean-state gate passes, integrate only by:

`git merge --ff-only <EXACT_REVIEWED_SHA>`

Frozen cases:

- Bridge `main`
- Bobbio `develop`
- Mica `main`
- Asteria `main`
- SeminarArc `main`

No squash/rebase/cherry-pick is allowed. If fast-forward is no longer possible, stop and return to Planner/Critic rather than selecting a different strategy.

### 5.2 Diverged but non-overlapping integrations

AI_Skills and Lucerna may use a merge commit only if the unified preflight still confirms the already-reviewed non-overlapping state **and** the canonical checkout/index is clean.

Then:

1. run `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`;
2. if any conflict or unexpected semantic/content change appears, run `git merge --abort` and stop;
3. inspect the staged merge result and run `git diff --cached --check`;
4. verify candidate-owned files remain semantically identical to the reviewed candidate and no unrelated/pre-existing content entered the index;
5. commit only the mechanical merge and push the canonical branch.

No manual conflict resolution is authorized. Because integration starts from a verified clean checkout/index, `merge --abort` has a defined recovery baseline rather than being used on top of unknown local modifications.

### 5.3 Push order and partial-integration safety

Complete **all** source/identity/drift/clean-worktree preflight checks for **all** mutable repos before the first canonical push.

Keep the already-reviewed push order:

1. Bobbio
2. Mica
3. Asteria
4. SeminarArc
5. Lucerna
6. Bridge
7. AI_Skills

If a remote branch advances after preflight and a push is rejected, fetch and stop that repo. Do not force push. Already-successful integrations remain truthful partial integration; report exact integrated/not-integrated state and return to Planner/Critic rather than rewriting published history.

## 6. Bridge 0.8.3 boundary

Integrating Bridge candidate `e1d6b781ad7e56d567bed419001069baf439d0a5` into `main` makes the reviewed `0.8.3` source/version metadata canonical.

This package does **not** authorize:

- Git tag creation;
- GitHub Release creation;
- package publication;
- deployment;
- Host Policy installation/update;
- deletion of the reviewed task branch;
- `0.8.4` bump.

Task 056 later revalidates then-current Bridge main and selects its own next valid version slot.

## 7. Validation after integration

Implementation candidates and H1–H9 already passed independent implementation review. Integration therefore does not rerun product development, Bridge 363 tests, H1–H9, GPT Work, or paid/Terra checks merely for ceremony.

For each repo verify:

- canonical remote head after push;
- exact reviewed candidate reachability;
- for `FF_ONLY`, canonical head equals exact reviewed candidate;
- for `CLEAN_MERGE`, merge commit preserves exact reviewed candidate in ancestry and contains no manual/unrelated content;
- integration delta/staged merge passes `git diff --check` as applicable;
- no unreviewed target files are introduced.

For Bridge also verify canonical source/version surfaces still read `0.8.3`; do not publish/reinstall.

If execution-time drift invalidates reviewed evidence, stop instead of restarting development inside integration.

## 8. Should-not-change

Integration must not:

- modify candidate content;
- alter CUHK Date;
- edit or execute 056;
- add H10/new state/schema/ledger/controller/watcher;
- delete task branches;
- create PRs;
- create new branch/worktree names;
- rebase/squash/cherry-pick reviewed commits;
- force push or rewrite history;
- stash/reset/clean/commit unrelated local work to make integration proceed;
- create releases/tags/deployments;
- change application/runtime code beyond what is already contained in exact reviewed commits.

## 9. Recovery

- Dirty/staged canonical checkout or unfinished Git operation -> stop that repo before integration; preserve user work untouched and report exact status.
- Conflicting untracked path -> stop; do not delete, clean, overwrite, or relocate it automatically.
- Fast-forward precondition false -> stop; do not switch to another merge strategy.
- Diverged merge conflict or relevant semantic drift -> `git merge --abort` from the verified clean baseline and stop.
- Push rejected because remote advanced -> fetch, do not force; re-evaluate and return to Planner/Critic when state is no longer exactly approved.
- Partial cross-repo integration -> do not roll back successful published merges by rewriting history; report exact integrated/not-integrated repos and obtain a bounded follow-up decision.

## 10. Completion and next handoff

Integration is complete only when all mutable canonical branches contain the exact reviewed candidate histories, remote heads are verified, CUHK Date remains unchanged, and Bridge has not been released beyond source integration.

After separately approved integration completes:

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`

Do not execute 056 inside this integration task.
