# 057 Repo AGENTS Hygiene — Integration Plan

- Task key: `057_repo_agents_hygiene`
- Integration package version: `v0.1`
- Stage: `AWAITING_INTEGRATION_CRITIC_REVIEW`
- Reviewed evidence commit: `E3 = 745281b70322b8508e43e59a5bdef70529749ea5`
- Reviewed manifest commit: `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`
- Design / implementation authority remains the approved 057 v2 Plan/Goal and H1–H9. This plan only integrates the already-reviewed tuple.

This plan does not authorize merge, release, tag, deployment, branch deletion, paid API, or Task 056 execution. Integration may begin only after independent Critic reviews this exact Plan + Goal + Kickoff and returns `READY_FOR_INTEGRATION_CODEX=YES`, and the user then sends the approved Kickoff.

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

## 3. Current canonical-branch reality at planning time

Planner rechecked current canonical branches on 2026-09-17.

| Repo | Canonical head | Relation to reviewed candidate | Current integration form |
| --- | --- | --- | --- |
| AI_Skills_Collection | `c82f9a3c064d216b46738b4079347f3dde180f69` | diverged from M3; merge base `e8ba7515...`; current-main changes are outside `results/057_repo_agents_hygiene/` | clean history merge expected |
| GPT_Codex_AI_Bridge_Kit | `cb77b1cc5a1fce097a38066d2db452291e359852` | candidate ahead by 2, behind by 0 | `--ff-only` |
| Bobbio `develop` | `0811116ac7197590f0af773f3c6296d4ca41db80` | candidate ahead by 2, behind by 0 | `--ff-only` |
| Lucerna | `852a4a8c8c67ba68ddd533b682eeb1460464140e` | diverged; merge base `760931ae...`; reviewed side changes only `AGENTS.md`, current-main post-base changes do not touch `AGENTS.md` | clean history merge expected |
| Mica-for-ChatGPT | `aa4ce52581fff2e207d1f93600becbb3018b0efc` | candidate ahead by 2, behind by 0 | `--ff-only` |
| Asteria | `166791c27752c70255043f026dcbda4deb693c04` | candidate ahead by 2, behind by 0 | `--ff-only` |
| SeminarArc | `71c59d39f4d7e9cd3a3d813ad55d5cf6a38a4b11` | candidate ahead by 2, behind by 0 | `--ff-only` |

Thus current evidence supports a pure integration. AI_Skills and Lucerna require merge commits only because canonical history advanced independently; no manual content reconciliation is currently justified.

Execution must re-fetch immediately before integration. These heads are evidence locators, not permission to ignore later drift.

## 4. Integration strategy

### 4.1 Preflight all repositories before the first canonical push

For every mutable repo:

1. use existing canonical local checkout/worktree; do not create new task branches/worktrees;
2. `git fetch origin` for canonical and `reviewed/057_repo_agents_hygiene` refs;
3. verify `origin/reviewed/057_repo_agents_hygiene` resolves to the exact reviewed candidate SHA for that repo; AI_Skills reviewed branch must resolve to M3;
4. verify canonical remote head and inspect any advancement since this package;
5. compare merge base and changed paths.

If canonical advancement touches a reviewed candidate file, changes relevant instruction/version/release authority, produces an actual merge conflict, or otherwise makes the reviewed semantics uncertain: stop before merging that repo and return to Planner/Critic. Do not edit the candidate, cherry-pick an improvised fix, force merge, or create another integration branch.

Unrelated, clearly disjoint canonical advancement may proceed under this already-reviewed integration contract after the Executor records the new head and confirms no candidate-path/authority overlap.

### 4.2 Fast-forward integrations

When current canonical is an ancestor of the exact reviewed candidate, integrate by fast-forward only:

`git merge --ff-only <EXACT_REVIEWED_SHA>`

Expected planning-time repos:

- Bridge `main`
- Bobbio `develop`
- Mica `main`
- Asteria `main`
- SeminarArc `main`

No squash/rebase/cherry-pick is allowed because those would create rewritten candidate identities. Fast-forward keeps the exact reviewed commits as canonical history.

### 4.3 Diverged but non-overlapping integrations

For AI_Skills and Lucerna, current planning-time history has advanced independently. Preserve both histories with a merge commit that has the exact reviewed candidate as a parent.

Before committing:

- use a merge-base/path-overlap check;
- perform `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`;
- if any conflict or unexpected semantic/content change appears, `git merge --abort` and stop;
- inspect staged merge result and run `git diff --cached --check`;
- verify reviewed candidate-owned files are semantically identical to the reviewed candidate and no manual edits were introduced;
- then commit the mechanical merge and push canonical branch.

No manual conflict resolution is authorized by this package.

### 4.4 Push order and partial-integration safety

Complete all read-only/pre-commit preflight checks before the first push.

Recommended push order:

1. Bobbio / Mica / Asteria / SeminarArc fast-forwards;
2. Lucerna clean merge;
3. Bridge fast-forward;
4. AI_Skills merge last, so canonical evidence history closes the cross-repo integration after other repo pushes succeed.

If a remote branch advances after local preflight and a push is rejected, fetch and stop that repo. Do not force push. Already-successful canonical integrations remain truthful partial integration; report exact heads and return to Planner/Critic rather than rewriting published history.

## 5. Bridge 0.8.3 boundary

Integrating Bridge candidate `e1d6b781...` into `main` makes the reviewed `0.8.3` source/version metadata canonical.

This integration package does **not** authorize:

- Git tag creation;
- GitHub Release creation;
- package publication;
- deployment;
- Host Policy installation/update;
- deletion of the reviewed task branch.

No `0.8.4` bump is allowed. Task 056 will later revalidate then-current Bridge main and choose its next valid version slot.

## 6. Validation after integration

Because final implementation candidates and H1–H9 already received independent review, integration must not rerun product development or broad test suites merely for ceremony.

For each repo:

- verify canonical remote head after push;
- verify the exact reviewed candidate is reachable from canonical history;
- for fast-forward repos, canonical head must equal the exact reviewed candidate;
- for merge repos, merge commit must have the exact reviewed candidate in ancestry and no manual content changes beyond the mechanical combination;
- run `git diff --check` on the integration delta / staged merge where applicable;
- verify no unreviewed target files were introduced.

For Bridge, additionally verify canonical source version surfaces still read `0.8.3`; do not publish/reinstall.

No paid API, Terra, GPT Work, product smoke, 363-test rerun, or H1–H9 rerun is required unless the canonical branch changed in a way that invalidates the reviewed candidate—such a case is a stop condition, not an excuse to silently expand integration.

## 7. Should-not-change

Integration must not:

- modify candidate content;
- alter CUHK Date;
- edit 056 artifacts or execute 056;
- add H10/new state/schema/ledger/controller/watcher;
- delete task branches;
- create PRs;
- rebase/squash/cherry-pick reviewed commits;
- force push or rewrite history;
- create releases/tags/deployments;
- change application/runtime code beyond what is already contained in the exact reviewed commits (057 reviewed commits themselves are instruction/docs/Bridge scaffold changes).

## 8. Recovery

- Fast-forward precondition false -> stop and re-evaluate; do not switch to cherry-pick.
- Diverged merge conflict or relevant semantic drift -> `git merge --abort`, preserve canonical branch, return to Planner/Critic.
- Push rejected because remote advanced -> fetch, do not force; return to Planner/Critic if the new state is relevant or overlapping.
- Partial cross-repo integration -> do not roll back successful published merges by rewriting history; report exact integrated/not-integrated repos and obtain a bounded follow-up decision.

## 9. External reality check

Planner rechecked current official Git documentation. `git merge --ff-only` refuses non-fast-forward integration, while a true merge commit preserves both parent histories; `--no-commit` permits inspection before creating a non-fast-forward merge commit. This supports the chosen split: fast-forward exact candidates when possible, and use a no-manual-edit merge only for already-diverged but non-overlapping canonical history.

## 10. Completion and next handoff

Integration execution is complete only when all mutable canonical branches contain the exact reviewed candidate histories and remote heads are verified, with CUHK Date unchanged and Bridge unreleased beyond source integration.

After separately approved integration completes:

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`

Do not execute 056 inside this integration task.
