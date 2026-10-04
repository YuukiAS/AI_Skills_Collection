# Project Instructions Editor — Final Integration / Release Kickoff v0.1

Status: DRAFT_FOR_CRITIC_REVIEW

Use this Kickoff only after:

- implementation overall PASS;
- G1/G2/G3/G4 PASS;
- private ChatGPT wrapper created from exact C4;
- real Server+VPS user acceptance PASS.

The user sending this approved Kickoff is the authorization for the final integration/release stage.

## Kickoff text

Continue the existing Project Instructions Editor task through final integration and formal repository release closure.

Repository:
YuukiAS/AI_Skills_Collection

Task key:
project-instructions-editor--standalone-skill-implementation

Exact task branch:
work/project-instructions-editor--standalone-skill-implementation

Exact task worktree:
../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

Accepted Skill identity:

FINAL_CANDIDATE_COMMIT=
266334ca807640b08605faddbdded7d5a6591aa1

EVIDENCE_HEAD=
34428d3db409ffc97aea36cc3776c14f33b94289

Accepted Skill-tree hash:
c504970421c4d14ce9ac5cc1140c014cc5c7fff4ec826b5ab8c66adbe6db42c3

Read and obey:

docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md

docs/goals/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_1.md

docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md

results/project-instructions-editor--standalone-skill-implementation/IMPLEMENTATION_REVIEW.md

Do not reopen product design or rerun product G1–G4 solely for metadata integration.

### 1. Confirm final acceptance precondition

Before any integration mutation, require durable evidence that:

SERVER_VPS_USER_ACCEPTANCE=PASS

If the acceptance is missing or failed, stop.

Do not release around a failed/missing user acceptance.

### 2. Protect local README before remote synchronization

The user explicitly warned that the exact local worktree may contain newer README edits that are not yet pushed.

Before fetch/merge or any README rewrite:

- verify exact repo / branch / worktree identity;
- run git status --short;
- inspect git diff -- README.md;
- inspect git diff --cached -- README.md.

Do not assume remote README is the latest reader-facing wording.

If local README changes are task-owned and limited to Project Instructions Editor card / ChatGPT-use / release wording, preserve and reconcile them.

Do not reset, restore, stash, discard, or overwrite local README changes.

If README changes are unrelated or ownership is genuinely ambiguous, stop with one precise blocker.

### 3. Fetch latest main and resolve release baseline

Fetch latest origin/main.

Read:

- VERSION;
- CHANGELOG.md;
- README.md;
- scripts/codex_marketplace_config.json;
- standalone skill/version baselines;
- relevant generated registry/catalog/provenance sources.

If latest main remains on the 5.4.x formal release line and Project Instructions Editor is not already integrated:

Repository bump decision = MINOR
target VERSION = 5.5.0
project-instructions-editor = standalone 0.1
central plugins = NO_BUMP

Preserve every current-main 5.4.x release entry and every unrelated current plugin/standalone version.

Patch drift inside 5.4.x is expected and does not require Planner re-entry unless it directly overlaps PIE source/distribution semantics.

Stop if:

- main is already 5.5.0 or later;
- PIE is already integrated;
- version policy changed;
- main contains direct overlapping PIE source/distribution changes.

### 4. Synchronize latest main into exact task branch

Use the existing exact task branch/worktree.

No successor branch.
No new clone.
No rebase.
No force push.
No remote remap.

Require clean task-owned state after preserving/committing any authorized local README edit.

Merge latest origin/main into the exact task branch through an ordinary history-preserving merge.

Conflict resolution must preserve:

current main:
- all 5.4.x release history;
- workflow-core 0.5 and other current central plugin versions;
- current Project Thread Handoff / Slurm Workflows versions;
- unrelated shared tests and source;

Project Instructions Editor:
- accepted C4 Skill tree;
- focused tests / standalone baseline;
- standalone card/icon;
- generated identity;
- 5.5.0 release addition;
- task evidence history.

Generated files are regenerated source-first after conflicts; do not pick stale generated sides manually.

### 5. C4 Skill tree is immutable

After synchronization/reconciliation, compute the Project Instructions Editor runtime Skill-tree identity.

It must be byte-equivalent to C4 and match:

c504970421c4d14ce9ac5cc1140c014cc5c7fff4ec826b5ab8c66adbe6db42c3

If any file under:

skills/core/codex-system/project-instructions-editor/**

changes from accepted C4:

stop;
READY_FOR_RELEASE=NO;
return to implementation review.

Do not silently “small-fix” the accepted Skill during integration.

### 6. Release metadata cleanup

Fix only the already accepted integration metadata issues.

CHANGELOG:

Remove the stale implication that natural PIE discovery requires a current/empty/reset baseline.

Correct meaning:

an explicit long-lived ChatGPT Project-instruction editing request may enter PIE even when the live baseline is missing; missing baseline causes safe degradation/request for the baseline rather than owner loss.

README:

- preserve the exact local task-owned wording found in step 2;
- remove “开发中” only when this formal release is actually being closed;
- describe the capability in natural Chinese;
- avoid unnecessary English in reader-facing explanation;
- if ChatGPT wrapper creation + Server+VPS acceptance passed, include at most one short truthful sentence saying PIE can also be used through a private skills-only ChatGPT personal Plugin wrapper with no MCP;
- never include private Plugin ID/URL.

Do not rewrite unrelated README sections.

### 7. Mandatory Clear Writing README check

Current AGENTS requires a real Clear Writing invocation for every README mutation.

Actually invoke the current installed Clear Writing / writing-style capability on the affected README reader-facing region.

This is a language-quality check only. It must not alter version, paths, product identity, technical meaning, or release truth.

If no real callable Clear Writing invocation is available, stop before committing the final README mutation and report:

CLEAR_WRITING_UNAVAILABLE

Do not ask the user to rewrite README manually.

### 8. Regenerate and validate

Regenerate current derived outputs from source using current repository generators.

Run the current required mechanical/full validation, including at least the implementation Plan equivalents:

python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests

Run current icon/version/generated parity checks required by latest main.

Do not interpret test count as product acceptance; product acceptance is already independently established.

### 9. Integration candidate proof

Before main movement, record a final integration proof under:

results/project-instructions-editor--standalone-skill-implementation/

It must include:

- accepted C4 commit and Skill-tree hash;
- final integration candidate commit;
- latest main baseline integrated;
- VERSION target;
- README/CHANGELOG cleanup summary;
- generated parity result;
- full-test result;
- proof that C4 Skill tree is unchanged;
- Server+VPS acceptance PASS locator;
- private wrapper existence verified without committing private ID/URL.

### 10. Main and formal release closure

Only if all checks pass:

- integrate the validated task branch to main using the repository's current bounded, non-force integration path;
- require current main to be an ancestor of the exact validated integration candidate before fast-forward/integration;
- publish main through the current bounded publisher;
- advance the formal release ref to the same validated release commit only through the current approved bounded release path;
- verify origin/main and origin/release resolve to the intended release commit.

Do not use force push, force-with-lease, rebase, raw fallback publication, remote remap, or destructive Git.

Do not create a GitHub Release object unless current repository release policy explicitly requires one.

If the current bounded publisher cannot perform the required main/release movement, stop and report the exact bounded-route blocker; do not fall back to broader raw Git.

### 11. Issue #93 closure

After formal release closure succeeds:

- update durable closure evidence;
- update Issue #93 reader-facing copy only after real Clear Writing invocation;
- set Resolution commit / DONE through the available Project lifecycle surface if accessible;
- truthfully close Issue #93 only when board policy requirements are satisfied.

If Project field mutation is unavailable:

- do not ask the user to drag cards or fill fields;
- record the exact pending Project mutation;
- do not falsely claim Project DONE.

### 12. Final claim

Only report READY_FOR_RELEASE=YES if all of these are true:

IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS
SERVER_VPS_USER_ACCEPTANCE=PASS
C4_SKILL_TREE_UNCHANGED=YES
INTEGRATION_VALIDATION=PASS
MAIN_INTEGRATION=PASS
FORMAL_RELEASE_ADVANCED=PASS

Report the final main/release commit and any remaining board-only pending mutation separately.

Do not alter private ChatGPT Project data, private Plugin identity, live network state, Bridge Kit, central Plugin behavior, or unrelated repository functionality in this integration stage.
