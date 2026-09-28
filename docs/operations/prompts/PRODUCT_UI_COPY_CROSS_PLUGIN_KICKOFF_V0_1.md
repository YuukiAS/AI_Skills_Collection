# Product UI Copy Cross-Plugin — Kickoff Draft v0.1

**Do not use this Kickoff until the independent execution-ready Critic has returned PASS / READY_FOR_CODEX=YES for the exact v0.1 package and written the durable review artifact.**

Repository:

`YuukiAS/AI_Skills_Collection`

Approved architecture:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md`  
commit: `a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`

Architecture Critic PASS:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_2_2026-09-28.md`

Execution Plan:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_1_2026-09-28.md`

Canonical Goal:

`docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_1.md`

Expected execution-ready Critic review:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-28.md`

## 1. Exact task authorization

When the user sends this approved Kickoff, authorize exactly:

```text
task_key = product-ui-copy--cross-plugin-production-integration
branch = reviewed/product-ui-copy--cross-plugin-production-integration

canonical checkout expected on execution machine =
  /home/yuukias/AI_Skills_Collection

Bridge-derived sibling worktree =
  /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
```

No other task/branch/worktree is authorized.

If the canonical checkout is not exactly that path, or the repo identity is not `YuukiAS/AI_Skills_Collection`, stop before bootstrap and report the mismatch.

Do not substitute another path.

Do not use raw `git worktree add`.

Do not second-bootstrap an existing task.

## 2. Bootstrap only through current Bridge normal entry

From the exact canonical checkout:

1. read current repo `AGENTS.md`;
2. read current Bridge Reviewed Handoff normal-entry rules;
3. verify worktree clean enough for safe bootstrap;
4. run:
   `git fetch --all --prune`;
5. resolve the exact post-sync `origin/main` OID;
6. confirm the task branch does not already exist locally/remotely and the sibling worktree is not occupied;
7. run current Bridge first bootstrap:

```bash
ai-bridge reviewed-handoff task bootstrap   --task-key product-ui-copy--cross-plugin-production-integration   --expected-repo YuukiAS/AI_Skills_Collection   --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID>   --objective "Implement the approved Product UI Copy cross-plugin workflow from Proposal v0.2 and Execution Plan v0.1: Frontend content architecture -> protected Clear Writing Product UI Copy handoff -> locale-aware wording -> rendered Frontend acceptance. Do not redesign the approved architecture or modify consumer repositories."   --max-review-rounds 2   --ci-required
```

Do **not** add:

- `--visual-review-required`
- `--text-review-required`

This Kickoff does not authorize paid Text Review / Visual Review / Terra.

The first bootstrap must create the Bridge-derived sibling worktree above and initialize:

```text
PLAN_REQUESTED
RUN_GPT_PLANNER
```

That is expected. Do not start production implementation yet.

## 3. Planner-owned initial transaction

After bootstrap metadata is published/readable, stop Executor work.

GPT Planner must:

1. read `REQUEST.md` / `CURRENT.json`;
2. read the approved Proposal v0.2;
3. read Execution Plan v0.1 / Goal v0.1;
4. read the durable execution-ready Critic PASS;
5. write task-local `PLAN.md` using `AI_BRIDGE_REVIEWED_PLAN_V2`;
6. preserve all G1–G8 gates and H0→H4 chronology;
7. re-read current Bridge PLAN template and self-check required sections;
8. finally transition:
   `PLAN_REQUESTED -> PLAN_FROZEN`;
9. keep:
   `plan_revision = 0`;
10. set:
   `next_action = RUN_CODEX_EXECUTOR`.

Executor must not write/freeze its own Plan.

## 4. Production implementation

Only after legal `PLAN_FROZEN`, implement the frozen package.

Explicitly use:

```text
workflow-core
+ ai-skills-core
+ web-development
+ writing-style
```

Implement the approved bounded behavior:

### Clear Writing

- add `skills/writing/core/product-ui-copy/`;
- add direct/indirect/near-miss/negative activation evals;
- narrow `chinese-prose` **frontmatter description** so Product UI microcopy routes away;
- preserve long-form `chinese-prose` behavior;
- add the narrow Product UI Copy protected-meaning handoff to `writing-fidelity`;
- update Clear Writing plugin description/default prompt/package.

### Frontend Design

- preserve coordinator-first topology;
- update product-interface discovery for browser extension/web/desktop/mobile;
- add content-architecture → Product UI Copy handoff;
- add rendered-copy acceptance;
- keep backend/runtime/data/docs negatives out.

### Profiles / packaging

- review `profiles/codex-webdev.json`;
- review `profiles/frontend-research-product.json`;
- make only the minimum approved companion changes;
- use existing generator/package mechanisms.

### Candidate replay

Reuse `scripts/candidate_plugin_replay.py`.

If needed, minimally extend it so one isolated candidate run can install and prove actual consumption of both:

- `web-development@ai-skills-candidate`
- `writing-style@ai-skills-candidate`

from the same candidate commit.

Preserve single-plugin replay compatibility.

Do not build another replay framework.

## 5. H0 fresh-evidence preflight

Before implementation tuning, freeze only:

- task families;
- batch size;
- locale balance;
- coverage matrix;
- required KEEP/rewrite/escalation classes;
- rubric;
- reviewer criteria.

Do not create or expose exact final fresh-holdout prompts.

Use the bounded batch size frozen by the Plan.

## 6. Development evidence

Run cheap/focused checks before broad checks.

Use known development evidence:

- CUHK Date 150-line audit = known regression only;
- Lucerna = read-only known/compatibility;
- Mica = read-only browser-extension compatibility;
- SeminarArc = read-only mobile/Compose compatibility;
- Clear Writing unrelated regressions;
- Frontend Design 0.3 regressions.

Do not call any of these fresh.

## 7. Explicit authorization for read-only real-project replay

This approved Kickoff authorizes **only for this task's compatibility evaluation**:

- reading the minimum frozen source needed from:
  - `YuukiAS/Lucerna`
  - `YuukiAS/Mica-for-ChatGPT`
  - `YuukiAS/SeminarArc`;
- using those frozen source excerpts as read-only candidate-replay inputs through the current authorized Codex/OpenAI execution path;
- recording only the minimum provenance/source-consumption evidence needed for replay.

It does not authorize:

- any write to those repos;
- unrelated private project data;
- user secrets;
- broad repo export;
- publication or external redistribution.

If replay would require a broader external/private-data transmission than this bounded source set, stop and request new authorization.

## 8. SeminarArc mandatory paired replay

Positive prompt must be natural and must not mention Frontend Design.

It must prove:

```text
Compose/UI task
→ Frontend Design generic product-interface coordinator
→ android-lead / compose-expert remain Android/Compose implementation authority
```

Negative control must prove:

```text
Room / WorkManager / data-only task
→ Frontend Design does not activate
```

Do not modify SeminarArc.

Do not count this as maturity evidence.

## 9. Rendered acceptance

Build repo-safe representative Product UI fixtures/evidence only for this plugin evaluation.

Actually render them and save exact screenshots/evidence under:

`results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/`

Cover:

- wide/desktop;
- narrow/mobile;
- multi-block page rhythm;
- trust/help disclosure;
- KEEP control.

Do not claim these browser-rendered fixtures prove native desktop/mobile runtime behavior.

The independent Reviewer must actually inspect the images.

If the Reviewer surface cannot access them, report an evidence-access blocker. Do not use OCR/text summaries as a substitute.

## 10. Broad validation

At minimum:

```text
python scripts/skills.py registry --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py catalog --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest discover -s tests
```

Also run focused Product UI Copy / Frontend trigger / candidate replay / version-parity tests.

## 11. Version and H2 final candidate

Do not bump at task start.

After G1–G6 development evidence + rendered acceptance are stable, re-read current version source.

If the release baseline is still:

```text
repository = 5.3.1
web-development = 0.3
writing-style = 0.3
```

apply exactly once:

```text
repository = 5.4.0
web-development = 0.4
writing-style = 0.4
all other central plugins = NO_BUMP
maturity = unchanged / unclassified
```

If another formal release has advanced main, follow the approved version policy from then-current source while preserving the MINOR cross-plugin release decision unless a real source conflict requires Planner/Critic review.

Synchronize:

- both plugin changelogs;
- root CHANGELOG;
- README;
- VERSION;
- Marketplace/generated metadata;
- version/parity tests.

Then freeze H2:

- exact final candidate commit;
- final candidate identity;
- reviewer criteria.

No production tuning after H2 before H4.

## 12. Intentional H3 Planner revision

After H2, Executor must not create the exact fresh holdout.

Executor transitions to:

`NEEDS_GPT_PLANNER`

The external Planner owns H3.

Planner must:

- verify H2 candidate identity;
- verify H0 rubric;
- create exactly one repo-safe batch:
  `results/product-ui-copy--cross-plugin-production-integration/fresh_holdout/final_holdout_batch.json`;
- bind exact candidate/rubric;
- keep production source unchanged;
- update task-local Plan only to freeze the H3 locator/identity;
- transition:
  `NEEDS_GPT_PLANNER -> PLAN_FROZEN`;
- consume the single revision:
  `plan_revision = 1`.

No second automatic plan revision remains for fresh-batch chasing.

## 13. H4 one-shot

Executor runs the complete H3 batch once on the unchanged H2 candidate.

No:

- replacement prompts;
- cherry-picking;
- prompt substitution;
- adding easier cases;
- production repair before verdict.

If H4 PASS:

continue.

If H4 FAIL:

- preserve failure;
- do not create another fresh batch;
- do not call the task release-ready;
- if repaired, the failed batch is now known regression;
- return through the workflow/human decision boundary rather than chasing another hidden batch.

## 14. CI and independent Reviewer

After H4 PASS:

- write valid `RESULT.md`;
- set `implementation_commit` to the H2 final production candidate;
- enter:
  `WAITING_FOR_CI / ci_status=PENDING`;
- publish exact reviewed branch through the authorized current-branch publisher;
- wait for real GitHub CI.

CI PASS then goes to independent Scheduled GPT Reviewer.

Reviewer must inspect:

- Plan;
- real diff;
- G1–G8 evidence;
- actual two-plugin consumption;
- H4 complete batch/output;
- rendered screenshots;
- version/changelog/README/TODO closure;
- tracking status.

No paid review is authorized by this Kickoff.

If independent qualitative review cannot be performed from repository evidence, fail closed and request a separately authorized review route.

## 15. Maintenance tracking authorization

This Kickoff authorizes the bounded maintenance mutations required by this exact task, after applying the repository's Clear Writing requirement to reader-facing tracking copy:

- preserve Issue #17;
- keep Issue #13 dependency-only;
- create/bind one unique Frontend Product UI Copy tracking Issue replacing collided `#73`;
- create/bind one unique writing-style Product UI Copy naturalness tracking Issue replacing collided `#20`;
- update only those canonical `tracking: #N` lines;
- move relevant Project items to `DOING` when implementation begins;
- after central release, use `ADAPTING` if consumer hard bindings remain outstanding.

Do not close unrelated Issues.

If the current execution surface cannot modify GitHub Project, record exact pending mutation for the Project-capable AI Skills Maintainer. Do not ask the user to maintain the board manually.

## 16. Forbidden actions

Do not:

- modify Bridge Kit;
- modify Host Policy;
- modify any consumer repo;
- modify CUHK Date;
- create another task/branch/worktree;
- create successor;
- enable paid Text/Visual Review;
- broaden into writing-style #13;
- redesign Frontend 0.3;
- promote maturity;
- merge main;
- move release;
- delete branch/worktree;
- force/rewrite history;
- use destructive reset/clean/restore.

## 17. Stop / return to Planner

Stop if:

- canonical checkout/path mismatch;
- execution-ready Critic review missing/stale/REVISE;
- task branch already exists unexpectedly;
- first bootstrap cannot produce the exact sibling worktree;
- current source invalidates the approved architecture;
- implementation needs a new dependency manager/state machine;
- both candidate plugins cannot be proven consumed in one normal-entry runtime;
- H4 fails and a new fresh batch would be needed;
- paid review becomes necessary;
- consumer repo mutation becomes necessary;
- version policy source changed materially enough to invalidate the frozen release decision.

## 18. What this Kickoff does not authorize

This Kickoff does **not** authorize:

- main merge;
- release-ref movement;
- consumer project-local bindings;
- paid review;
- public deployment;
- maturity promotion.

After Reviewer PASS, stop at the human gate for final acceptance and later integration authorization.
