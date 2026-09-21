# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Integration / Release Plan R2

- Plan version: `integration-r2`
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Status: `READY_FOR_INTEGRATION_RELEASE_CRITIC_REVIEW_R2`
- Prior implementation Critic PASS: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_CRITIC_REVIEW_R2_2026-09-21.md`
- Integration Critic R1: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_CRITIC_REVIEW_R1_2026-09-21.md`
- Integration Critic R1 commit: `a30eec22b0337008ebde6075bf4d558e989e9cd4`
- Revision scope: close only `C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE` and `C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY`
- This plan does not authorize merge to `main`, tag, release, publish, deploy, paid API, 056 execution, production candidate changes, or v2.1 redesign.

## 1. Current Source Facts

### AI_Skills

- Production-source main for drift audit: `0a38519ed051cf01503ba3ed02b5a33b787b9c99`
- Latest `origin/main` also contains the integration Critic R1 review commit: `a30eec22b0337008ebde6075bf4d558e989e9cd4`
- Approved production candidate: `ce63f50238555849a48256068e6fa0d46e21a97b`
- Approved evidence branch tip: `871489ee227dee773c8fff3c161bd5743da739c7`
- Merge base between approved branch and current main: `2b6a5b50d75488298fb2206a6eebe92b3748ede2`
- Current main release slots remain unconsumed:
  - Repository: `5.0.5`
  - `workflow-core`: `0.1`
  - `ai-skills-core`: `0.2`
- Candidate release slots:
  - Repository: `5.0.6`
  - `workflow-core`: `0.2`
  - `ai-skills-core`: `0.3`

Main-only commits after the candidate baseline include R1/R2 implementation reviews, integration Critic R1, README refactor planning/render evidence, merged human-facing README structure, and the duplicate-approval TODO commit `9d145db9d04ea366f2cd5c8ded8681a4251a4c31`. All must be preserved.

### Bridge

- Main: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Approved production candidate: `7f2707dd4020951650d561303c82a17e22b27317`
- Approved evidence branch tip: `d09306f180634aa4d4ad4ec3ee46295a8b20945b`
- Merge base: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Current main version: `0.8.3`
- Candidate version: `0.8.4`
- No main-side production drift was observed.

## 2. Non-Goals

- Do not reopen v2.1 architecture.
- Do not modify approved production candidates.
- Do not create a successor task, branch, or worktree during planning.
- Do not merge either repository to `main` during planning.
- Do not tag, release, publish, deploy, run paid API, or start 056.
- Do not add another duplicate-approval rule, Gate, or same-meaning TODO. The incident is already recorded in `docs/plugin-todos/workflow-core.md` by commit `9d145db9d04ea366f2cd5c8ded8681a4251a4c31`.

## 3. C-WIGL-INT1 Closure: AI_Skills Main-Drift Overlap Audit

Integration must be rehearsed from the real merge base:

```text
BASE=2b6a5b50d75488298fb2206a6eebe92b3748ede2
MAIN=0a38519ed051cf01503ba3ed02b5a33b787b9c99
CANDIDATE=871489ee227dee773c8fff3c161bd5743da739c7
```

The four known overlapping files must be resolved explicitly.

### 3.1 `README.md`

Main-side contribution:

- new concise human-facing gallery structure;
- first-screen Codex App / CLI marketplace instructions;
- plugin cards that use `displayName`, plugin slug and version from source config;
- reduced internal maintenance prose and render evidence from the README refactor.

Candidate-side contribution:

- repository release value `5.0.6`;
- `workflow-core` version `0.2`;
- `ai-skills-core` version `0.3`;
- explanation that `AI Skills Maintainer` is the display name while `ai-skills-core` remains the slug;
- release dashboard/changelog links consistent with the candidate version closure.

Resolution rule:

- Keep the current main human-facing README structure and gallery.
- Apply candidate release values exactly:
  - `Repository / CLI release: 5.0.6`
  - `workflow-core` v`0.2`
  - `ai-skills-core` v`0.3`
- Keep main-only README refactor wording unless it directly contradicts the candidate release values.
- Do not restore the old long README layout from the candidate branch.
- Do not drop README render evidence or README gallery regression expectations from main.

Post-resolution checks:

- README first screen still uses the human-facing gallery shape.
- README release string matches `VERSION`.
- README plugin versions match `scripts/codex_marketplace_config.json`.
- README still names `AI Skills Maintainer` as the display label and keeps `ai-skills-core` as the slug.

### 3.2 `docs/workflows/PLANNER_ROLE_CONTRACT.md`

Main-side contribution:

- Planner handoff prompts must be self-contained;
- Planner cannot tell the user to assemble the next prompt from README/GitHub manually;
- Planner must fill real paths, package versions and review locators.

Candidate-side contribution:

- role contract advances to v1.4;
- task key is a machine locator, not a UI title;
- new Bridge / Reviewed Handoff task keys use semantic `<scope-token>--<goal-token>`;
- historical numbered keys are compatibility-only;
- Capability Gate Matrix must cover regression-bank and release-selection semantics;
- broad/full fallback, same-final-candidate and Gate lifecycle rules are explicit.

Resolution rule:

- Preserve main self-contained handoff prompt requirements.
- Preserve candidate v1.4 semantic task-key and Gate lifecycle additions.
- If both edits touch the same paragraph, the final wording must contain both ideas: self-contained prompt assembly and semantic task-key/Gate lifecycle enforcement.
- Do not downgrade v1.4 back to v1.3.

Post-resolution checks:

- File still requires Planner to generate complete Critic prompts with real locators.
- File still states semantic task keys are technical locators and not display titles.
- File still requires Capability Gate Matrix release-selection semantics.

### 3.3 `docs/workflows/CRITIC_ROLE_CONTRACT.md`

Main-side contribution:

- Critic-generated next-role prompts must be self-contained;
- Critic cannot leave placeholders or require the user to inspect GitHub manually;
- closure explanation must precede machine fields / approved Kickoff when applicable.

Candidate-side contribution:

- role contract advances to v1.4;
- task key is a technical locator, not a human title;
- Critic must review semantic task-key owner/scope binding;
- Critic must review Gate lifecycle: existing regression mapping, split/new Gate justification, retirement/merge obligations, release gate depth, same-final-candidate.

Resolution rule:

- Preserve main self-contained prompt and closure-explanation requirements.
- Preserve candidate v1.4 semantic task-key and Gate lifecycle review requirements.
- Do not reduce Critic duties to a generic PASS/REVISE checklist.
- Do not downgrade v1.4 back to v1.3.

Post-resolution checks:

- File still requires next-role prompt self-containment.
- File still requires semantic task-key and scope review.
- File still requires Gate lifecycle and final-candidate review.

### 3.4 `tests/test_codex_marketplace.py`

Main-side contribution:

- `test_readme_human_facing_plugin_gallery_matches_sources` checks the new gallery README contract:
  - `Repository / CLI release` from `VERSION`;
  - each central plugin card contains icon, display name, slug and `v<plugin version>`;
  - gallery entries use the generated marketplace/source metadata.

Candidate-side contribution:

- expected plugin versions:
  - `workflow-core = 0.2`
  - `ai-skills-core = 0.3`
- AI Skills Maintainer source/payload expectations for `0.3`;
- `test_workflow_identity_and_gate_lifecycle_contracts_are_source_authoritative`;
- regression checks for semantic task-key / human label separation, Gate lifecycle, broad/full fallback, same-final-candidate and no governance bloat.

Resolution rule:

- Preserve the main human-facing plugin-gallery regression test.
- Apply candidate version expectations exactly.
- Preserve candidate workflow-identity/Gate-lifecycle regression coverage.
- If old candidate README-table regex no longer matches the main README gallery, replace it with the main gallery assertion style rather than restoring the old README table.
- Do not drop tests merely to pass the merge.

Post-resolution focused test:

```bash
python -m unittest tests.test_codex_marketplace
```

The full AI_Skills suite must also run after generator/parity steps.

## 4. C-WIGL-INT2 Closure: Main-As-Production Integration and Recovery

Because normal Marketplace consumers use `Ref: main`, pushing an integration commit to main changes the user-consumed source before tag/release/publish. The integration sequence therefore has two separate proof stages: pre-push rehearsal and post-push production-identity smoke.

### Stage 0: Approval boundary

This plan does not authorize execution. The next Executor/Kickoff must obtain separate user authorization for:

1. creating clean temporary integration worktrees;
2. performing the pre-push integration rehearsal;
3. pushing the exact reviewed integration commit to `main`;
4. running production-identity install/upgrade smoke after push;
5. any later tag, GitHub Release, package publish or deployment.

### Stage 1: Clean temporary integration worktree

For each repository, create a clean temporary integration worktree based on the exact latest main approved for that stage.

AI_Skills expected base:

```text
0a38519ed051cf01503ba3ed02b5a33b787b9c99
```

Bridge expected base:

```text
afb2414b6fbe4b2b03292d3b1437d4dd22277fd0
```

If latest main differs at execution time, re-run drift audit before mutating. If the difference touches production/version/source/release surfaces, return to Planner/Critic.

### Stage 2: Merge approved candidate history

AI_Skills:

- merge approved evidence tip `871489ee227dee773c8fff3c161bd5743da739c7` into the clean integration worktree;
- use a real merge commit if histories are divergent;
- do not rebase, squash, cherry-pick production changes, or rewrite candidate history;
- resolve all three-way overlaps listed in Section 3.

Bridge:

- since main is the candidate base, integrate approved evidence tip `d09306f180634aa4d4ad4ec3ee46295a8b20945b` by fast-forward if policy allows, or by explicit `--no-ff` merge commit if the release owner wants a visible integration commit;
- do not rebase, squash, or rewrite candidate history;
- if main has drifted at execution time, stop and perform the same main-drift audit before continuing.

### Stage 3: Pre-push verification

Run all verification before pushing main.

AI_Skills:

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python scripts/skills.py validate
python scripts/skills.py audit --all
python -m unittest tests.test_codex_marketplace
python -m unittest discover -s tests
```

Required AI_Skills parity checks:

- `VERSION`, setup package version, registry top-level version and README release all equal `5.0.6`;
- `scripts/codex_marketplace_config.json` contains `workflow-core 0.2` and `ai-skills-core 0.3`;
- generated plugin manifests for `workflow-core` and `ai-skills-core` match source config;
- `docs/plugin-changelogs/workflow-core.md` latest release is `0.2`;
- `docs/plugin-changelogs/ai-skills-core.md` latest release is `0.3`;
- README human-facing gallery still matches marketplace config and capability status;
- no generated payload contains maintenance-only TODO/changelog/provenance files unless intentionally promoted.

Bridge:

```bash
python -m unittest tests.test_reviewed_handoff tests.test_reviewed_runner tests.test_repo_cli_compat tests.test_upfront_authorization_persistent_authoring
python -m unittest discover -s tests
```

Required Bridge parity checks:

- `pyproject.toml` version is `0.8.4`;
- `CHANGELOG.md` contains `0.8.4`;
- README / QUICKSTART do not leave release-facing `0.8.3 candidate` wording for the integrated `0.8.4` release;
- standalone validator smoke covers semantic PASS, existing legacy PASS and malformed semantic FAIL.

If any pre-push check fails:

- do not push main;
- preserve failure evidence in repo-local task evidence;
- either make a bounded integration-resolution commit in the temporary integration worktree or return to Planner/Critic;
- do not reset/force/rewrite history to hide the failed rehearsal.

### Stage 4: Freeze exact integrated tree

After pre-push verification passes, record:

```text
AI_SKILLS_INTEGRATED_COMMIT=<sha>
AI_SKILLS_INTEGRATED_TREE=<sha>
BRIDGE_INTEGRATED_COMMIT=<sha>
BRIDGE_INTEGRATED_TREE=<sha>
```

Also record:

- exact merge commands used;
- overlap files resolved;
- parity/test commands and exit status;
- whether any additional integration-only commits were needed.

No release/tag/publish decision is made at this point.

### Stage 5: User authorization for merge/push main

Only after Stage 4 is green, ask the user for explicit authorization to push the exact integrated commit(s) to `main`.

The request must name:

- repository;
- current remote main before push;
- exact integrated commit/tree to push;
- whether push is fast-forward or merge commit;
- expected remote main after push;
- confirmation that no tag/release/publish/deploy is included.

### Stage 6: Post-push production-identity install/upgrade smoke

After main push, immediately run separately authorized production-identity smoke.

AI_Skills smoke target:

- Git marketplace source: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- Ref: `main`
- Sparse paths: `.agents/plugins`, `plugins/codex/plugins`
- Expected repository release: `5.0.6`
- Expected plugin versions:
  - `workflow-core 0.2`
  - `ai-skills-core 0.3`

AI_Skills Codex identity:

- default: current Codex identity in a task-local isolated/shadow `CODEX_HOME` or equivalent task-local plugin cache;
- do not mutate the user's live global plugin cache unless separately authorized after an isolated route is proven insufficient.

AI_Skills install/upgrade path:

- fresh add/install from `main` and, if possible, upgrade from a task-local prior install;
- verify manifests and normal plugin availability in a fresh runtime;
- optionally use existing `candidate_plugin_replay.py` or a production-entrypoint equivalent only if the user authorizes the runtime/network/API side effects for this smoke.

AI_Skills side effects and restoration boundary:

- may create task-local temporary Codex home/cache and test directories;
- may read public GitHub repository data;
- must not send private artifact data;
- must not call Terra/OpenAI Responses paid review;
- must not write live global plugin state unless separately authorized;
- cleanup task-local temporary state after evidence is saved.

Bridge smoke target:

- repository: `https://github.com/YuukiAS/GPT_Codex_AI_Bridge_Kit.git`
- ref: `main`
- expected version: `0.8.4`

Bridge install/upgrade path:

- task-local isolated venv or equivalent isolated Python environment;
- install from integrated `main`;
- verify CLI import/version;
- run `ai-bridge init`, `ai-bridge validate`, `reviewed-handoff task init --task-key repo--example`;
- validate legacy existing task compatibility and malformed semantic rejection.

Bridge side effects and restoration boundary:

- may create task-local temporary venv and fixture repositories;
- may read public GitHub repository data;
- no private artifact upload;
- no paid API;
- no live production server/tunnel mutation;
- cleanup task-local temporary state after evidence is saved.

Network/API boundary:

- GitHub fetch/install and normal plugin/runtime loading may require network and current Codex identity and therefore require explicit user authorization at smoke time.
- Paid review, Terra, OpenAI Responses private review, new provider/account/credential and live-global mutation are not included.

If post-push smoke fails:

- no tag;
- no GitHub Release;
- no package publish;
- no deployment;
- preserve failure evidence;
- choose one of:
  - bounded corrective commit on `main` if the fix is narrow and within the already-approved integration/release scope;
  - bounded revert commit on `main` if production source must be restored;
  - return to Planner/Critic if the fix changes architecture, release semantics, authorization, provider, credential, cost, or recovery policy.
- never use reset, force push, history rewrite, or remote deletion to recover.

### Stage 7: Release/publish only after smoke PASS

Only after post-push production-identity smoke passes may a separate release phase be proposed. That phase needs its own user authorization for any of:

- Git tag;
- GitHub Release;
- package publish;
- marketplace publication;
- deployment.

## 5. Bridge Integration Method

Bridge has no current-main drift at the inspected source. The execution package must still bind the exact method:

```text
BASE=afb2414b6fbe4b2b03292d3b1437d4dd22277fd0
MAIN=afb2414b6fbe4b2b03292d3b1437d4dd22277fd0
CANDIDATE_TIP=d09306f180634aa4d4ad4ec3ee46295a8b20945b
PRODUCTION_CANDIDATE=7f2707dd4020951650d561303c82a17e22b27317
```

Preferred integration:

- use fast-forward from `afb2414...` to `d09306f...` if the release owner accepts evidence commits on main;
- otherwise use a non-rewriting merge commit that preserves all approved commits and makes the integration point explicit.

Either method must preserve the production candidate commit `7f2707dd...` and evidence commit `d09306f...`.

## 6. Next Handoff

```text
DECISION_REQUESTED=PASS_OR_REVISE
READY_FOR_INTEGRATION_EXECUTION_PACKAGE=YES_IF_CRITIC_PASS
READY_FOR_MAIN_MERGE=NO
READY_FOR_RELEASE=NO
START_056_NOW=NO
NEXT_HANDOFF=INTEGRATION_RELEASE_CRITIC_REVIEW_R2
```
