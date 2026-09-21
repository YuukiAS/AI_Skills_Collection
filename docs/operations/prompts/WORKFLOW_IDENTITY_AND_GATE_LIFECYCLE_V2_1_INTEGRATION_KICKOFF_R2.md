# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Integration Kickoff Draft R2

- Kickoff version: `integration-r2`
- Status: `DRAFT_NOT_AUTHORIZED`
- Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_PLAN_R2_2026-09-21.md`
- Goal: `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_GOAL_R2.md`
- This draft becomes execution authorization only if independent Critic passes this exact integration package and the user sends the approved Kickoff.

## Kickoff Draft

继续执行 **工作流命名与插件回归机制完善（AI_Skills + Bridge）** 的 integration/release execution package。

先读取：

- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_PLAN_R2_2026-09-21.md`
- `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_GOAL_R2.md`
- implementation Critic PASS R2
- integration Critic PASS R2
- 两个 repo 的最新 `AGENTS.md`

不要重新设计 v2.1。不要修改 approved production candidates。不要启动 056。

## Current Approved Tuple

```text
AI_SKILLS_MAIN_FOR_PRODUCTION_DRIFT=0a38519ed051cf01503ba3ed02b5a33b787b9c99
AI_SKILLS_APPROVED_PRODUCTION_CANDIDATE=ce63f50238555849a48256068e6fa0d46e21a97b
AI_SKILLS_APPROVED_EVIDENCE_TIP=871489ee227dee773c8fff3c161bd5743da739c7
BRIDGE_MAIN=afb2414b6fbe4b2b03292d3b1437d4dd22277fd0
BRIDGE_APPROVED_PRODUCTION_CANDIDATE=7f2707dd4020951650d561303c82a17e22b27317
BRIDGE_APPROVED_EVIDENCE_TIP=d09306f180634aa4d4ad4ec3ee46295a8b20945b
```

## Authorization Envelope

If I send this Kickoff after Critic PASS, I authorize only the following bounded phases.

### Phase 1: Clean Temporary Integration Rehearsal

Authorized:

- create clean temporary integration worktrees based on exact latest main for AI_Skills and Bridge;
- merge approved candidate history without rebase, squash or rewrite;
- resolve only integration overlaps required by the approved Plan;
- run local source/generated/version/changelog parity, focused tests and full tests;
- write integration rehearsal evidence into repo-owned task evidence paths;
- freeze exact integrated commit/tree for Critic/user review.

Not authorized in Phase 1:

- push main;
- tag/release/publish/deploy;
- paid API;
- live global plugin cache mutation;
- private artifact upload;
- 056 execution.

### Phase 2: Main Push

Not authorized by default.

After Phase 1 passes, ask me for explicit authorization naming:

- repository;
- current remote main;
- exact integrated commit/tree;
- fast-forward or merge-commit method;
- expected remote main after push;
- confirmation that tag/release/publish/deploy is excluded.

Only after I approve may you ordinary push the exact integrated commit to `main`. No force push, reset, rebase, branch deletion or remote mutation.

### Phase 3: Post-Push Production-Identity Smoke

Not authorized by default.

After main push, ask me for explicit authorization to run production-identity smoke. The request must repeat the target, identity, install path, expected versions, side effects and cleanup boundary below.

#### AI_Skills Smoke

Target:

- Git marketplace source: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- Ref: `main`
- Sparse paths: `.agents/plugins`, `plugins/codex/plugins`

Codex identity:

- current Codex identity;
- use task-local isolated/shadow `CODEX_HOME` or equivalent task-local plugin cache by default.

Install/upgrade path:

- fresh install from `main`;
- upgrade from a task-local prior install if practical;
- verify normal plugin availability in a fresh runtime.

Expected versions:

```text
Repository / CLI: 5.0.6
workflow-core: 0.2
ai-skills-core: 0.3
```

Side effects:

- may create task-local temporary Codex home/cache and test directories;
- may fetch public GitHub data;
- may use current Codex identity for normal plugin/runtime loading if separately approved for this smoke.

Restoration boundary:

- clean up task-local temporary state after evidence is saved;
- do not mutate live global plugin install/cache unless separately approved after isolated route fails with evidence.

Network/API:

- GitHub fetch/install and fresh runtime loading may require network/API and current Codex identity.
- Terra/OpenAI Responses paid review, private review, new provider/account/credential and private artifact upload are not authorized.

#### Bridge Smoke

Target:

- repository: `https://github.com/YuukiAS/GPT_Codex_AI_Bridge_Kit.git`
- ref: `main`

Codex/runtime identity:

- task-local Python environment;
- no live server/tunnel mutation.

Install/upgrade path:

- isolated venv or equivalent local environment;
- install Bridge from integrated `main`;
- verify CLI import/version;
- run `ai-bridge init`;
- run `ai-bridge validate`;
- run `reviewed-handoff task init --task-key repo--example`;
- validate existing legacy task compatibility and malformed semantic rejection.

Expected version:

```text
Bridge: 0.8.4
```

Side effects:

- may create task-local venv and temporary fixture repositories;
- may fetch public GitHub data.

Restoration boundary:

- delete or leave clearly identified task-local temporary evidence only;
- do not mutate production tunnels, live services, global auth, or unrelated repos.

Network/API:

- public GitHub fetch/install may require network.
- paid API, private external upload and new provider/account/credential are not authorized.

### Phase 4: Release/Publish

Not authorized.

Only after production-identity smoke passes may a separate release request be made for any of:

- Git tag;
- GitHub Release;
- package publish;
- marketplace publication;
- deployment.

## Required AI_Skills Overlap Resolution

Resolve all four known overlap files from the real merge base:

- `README.md`: keep current main human-facing gallery/concise structure; apply `Repository 5.0.6`, `workflow-core 0.2`, `ai-skills-core 0.3`.
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`: keep current main self-contained handoff prompt rules and candidate v1.4 semantic task-key / Gate lifecycle rules.
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`: keep current main self-contained next-role prompt rules and candidate v1.4 semantic task-key / Gate lifecycle rules.
- `tests/test_codex_marketplace.py`: keep current main human-facing plugin-gallery regression, apply candidate version expectations, and retain candidate workflow-identity/Gate-lifecycle regression.

Do not only resolve README.

## Required Verification Before Main Push

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

Bridge:

```bash
python -m unittest tests.test_reviewed_handoff tests.test_reviewed_runner tests.test_repo_cli_compat tests.test_upfront_authorization_persistent_authoring
python -m unittest discover -s tests
```

If pre-push rehearsal fails, do not push main. Preserve evidence and either make a bounded integration-resolution commit or return to Planner/Critic.

If post-push production smoke fails:

- no tag/release/publish/deploy;
- preserve evidence;
- use bounded corrective/revert commit or return to Planner/Critic;
- no reset, force push or history rewrite.

## Final State

```text
READY_FOR_MAIN_MERGE=NO_UNTIL_PHASE_1_GREEN_AND_USER_APPROVES
READY_FOR_RELEASE=NO_UNTIL_POST_PUSH_SMOKE_PASS_AND_USER_APPROVES_RELEASE
START_056_NOW=NO
```
