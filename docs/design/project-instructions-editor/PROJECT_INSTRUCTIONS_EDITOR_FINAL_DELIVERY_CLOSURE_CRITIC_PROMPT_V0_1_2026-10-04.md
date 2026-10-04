# Critic Prompt — Project Instructions Editor Final Delivery Closure v0.1

You are reviewing the final-delivery closure package for the accepted standalone Skill project-instructions-editor.

This is not a product redesign. Do not reopen the already-PASS product architecture, implementation package v0.2, or G1–G4 unless this closure package itself introduces a direct contradiction.

## Active Review Context

target_repo:
YuukiAS/AI_Skills_Collection

target_plugin_or_domain:
standalone Skill / project-instructions-editor

design_topic_or_task_key:
project-instructions-editor--standalone-skill-implementation

source_branch_or_ref:
main

execution branch:
work/project-instructions-editor--standalone-skill-implementation

execution worktree:
../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

review_stage:
final ChatGPT distribution + Server+VPS user acceptance + integration/release closure

accepted implementation identities:

FINAL_CANDIDATE_COMMIT=
266334ca807640b08605faddbdded7d5a6591aa1

EVIDENCE_HEAD=
34428d3db409ffc97aea36cc3776c14f33b94289

G4 review PASS =
254e9ea5ca1739dee0689afa13f7a1d34ac4469d

Implementation review PASS =
ad217bd9d131456ba646fe70367a1b77a7fc912f

reviewed final-delivery Plan:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md

reviewed final-delivery Goal:
docs/goals/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_1.md

reviewed future integration/release Kickoff:
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md

same-version package commit:
7bbe8d5982b9cd6abdca503ca6b12094976b92c6

tracking:
Issue #93

At Planner packaging time:
IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS
READY_FOR_INTEGRATION=YES
READY_FOR_RELEASE=NO

The user explicitly selected the real Server+VPS ChatGPT Project as the final real-world acceptance surface.

If main has advanced after the package commit, use latest main. Docs/tracking-only drift does not invalidate the package mechanically.

## 1. Must read

Read latest main:

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- docs/skill-todos/project-instructions-editor.md

Read the exact task branch:

- results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_REVIEW.md
- results/project-instructions-editor--standalone-skill-implementation/IMPLEMENTATION_REVIEW.md
- results/project-instructions-editor--standalone-skill-implementation/MANIFEST.md
- results/project-instructions-editor--standalone-skill-implementation/CANDIDATE_IMMUTABILITY_PROOF.md
- accepted C4 Skill source

Read Project Thread Handoff as the existing ChatGPT personal Plugin wrapper precedent:

- docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md
- results/science-communication--project-thread-handoff/result.md
- current Project Thread Handoff personal-wrapper shape if the Plugin Creator inspection surface is available.

Main review objects:

- final-delivery Plan v0.1
- final-delivery Goal v0.1
- final integration/release Kickoff v0.1

## 2. Do not move the product finish line

Implementation is already independently accepted.

Do not re-review:

- three edit modes;
- protected absence;
- bounded edit default;
- ownership/effective enforcement;
- no-op;
- G1/G2/G3/G4 taxonomy;
- C4 runtime behavior;
- standalone version 0.1;
- repository MINOR decision;
- central plugins NO_BUMP;

unless the final-delivery package contradicts them.

The purpose of this review is distribution, real-user acceptance, and integration/release safety.

## 3. ChatGPT personal Plugin wrapper

Planner proposes one initial private wrapper because the current account has no Project Instructions Editor wrapper.

Review the proposed identity:

name = project-instructions-editor
version = 0.1.0
scope = USER
discoverability = PRIVATE
skills-only = YES
MCP = NO

The wrapper must package exact C4 source only and remain a distribution wrapper, not a second canonical implementation.

Check whether this is the minimal current ChatGPT regular-Chat route, consistent with the verified Project Thread Handoff precedent.

Reject any need for:

- central Marketplace Plugin;
- MCP;
- connector;
- external API;
- database;
- app state;
- watcher/control plane;

unless there is direct current product evidence requiring one.

## 4. Icon / user burden

The user explicitly does not want to find or maintain an icon manually.

Canonical icon:

skills/core/codex-system/project-instructions-editor/assets/app-facing.svg
@ C4

The plan requires:

- wrapper root assets/app-facing.svg = byte-equivalent C4 icon;
- bundled Skill icon = byte-equivalent C4 icon;
- composerIcon/logo -> ./assets/app-facing.svg;
- no icon search/redesign;
- deterministic conversion only if Plugin Creator explicitly rejects SVG.

Project Thread Handoff already uses SVG directly in a personal wrapper.

Check that this fully removes unnecessary user burden without adding a new visual-source owner.

## 5. Future Plugin updates

The user should not need to copy a Plugin ID, find an icon, or rebuild an archive on future PIE updates.

Planner proposes:

- discover the unique owned personal plugin by exact name project-instructions-editor;
- read current release ID;
- build/update from exact canonical source;
- use expected_release_id concurrency guard;
- preserve identity;
- stop only on duplicate ambiguity or structural deletion/rename that overlay semantics cannot safely remove.

Check whether this is safe and matches current Plugin Creator behavior.

Do not require the user to maintain a private ID in README/repo.

## 6. Server+VPS final acceptance

The real final acceptance surface is the user's live Server+VPS ChatGPT Project.

The wrapper is used to edit/no-op the actual live Project setting. Then a fresh thread asks once:

“按最新实现审一下 Workstation 自动恢复，现在到底能不能放心不管了？还有什么会卡住？”

No style coaching is repeated in the acceptance prompt.

Review whether this is a legitimate real consumption test rather than a synthetic benchmark.

The acceptance specifically checks the real failure the user reported:

- conclusion/action/next step came too late;
- audit/status machinery led the answer;
- unnecessary English leaked into explanatory prose;
- closed checks were over-explained;
- next action was diluted;
- conclusions were repeated;
- the system did not distinguish “Project setting lacks a rule” from “existing rule was not followed”.

The editor is allowed bounded edit, bounded consolidation, or no-op.

Check that this does not hardcode a single answer or force the Skill to add rules.

## 7. Unnecessary-English requirement

This is an explicit user-facing acceptance requirement.

Ordinary explanatory terms should be natural Chinese.
English remains only for exact product/project identity, path, command, field/state value, process/file name, version, or other machine string needed for execution or unambiguous reference.

Check that this is derived from the live Server+VPS Project contract and does not weaken technical precision.

## 8. Privacy

The full Server+VPS Project setting, private Project history, private infrastructure transcript, and private Plugin ID/URL are not committed.

The repo retains only the acceptance contract, candidate identity, and redacted outcome/failure category if needed.

Check this against the existing no-private-Project-data-external-transmission boundary.

## 9. Local README rule

The user explicitly says the exact local integration worktree may contain newer README edits that are not pushed.

The final integration Kickoff therefore requires:

- inspect local git status;
- inspect unstaged/staged README diff before fetch/merge or rewrite;
- preserve task-owned local PIE README wording;
- no reset/restore/stash/discard;
- stop only on unrelated or genuinely ambiguous local ownership.

Remote README is not allowed to silently overwrite local accepted wording.

Check whether this is the correct minimum behavior.

Also check latest AGENTS: any final README mutation requires a real Clear Writing invocation. The Kickoff correctly treats missing callable Clear Writing as a blocker rather than asking the user to rewrite README manually.

## 10. Version/release drift

Planner observed main 5.4.3 at packaging time.

The accepted release type is still MINOR -> 5.5.0.

The plan generalizes patch drift:

if integration-time main remains 5.4.x and PIE is not already integrated:
target remains 5.5.0

Stop only if:

- main is already 5.5.0+;
- PIE was integrated elsewhere;
- version policy changed;
- current main directly overlaps accepted PIE source/distribution semantics.

Check whether tolerating non-overlapping 5.4.x patch drift avoids pointless Planner loops while preserving release truth.

## 11. Metadata-only integration boundary

Implementation review already identified two non-product cleanups:

- stale CHANGELOG discovery wording;
- README “开发中” marker.

These may change without rerunning G1–G4 only if C4 Skill tree stays byte-identical.

Accepted runtime tree hash:

c504970421c4d14ce9ac5cc1140c014cc5c7fff4ec826b5ab8c66adbe6db42c3

Check whether the Kickoff correctly stops and returns to implementation review if any accepted Skill file changes.

## 12. Integration/release authorization

The future Kickoff is sent only after SERVER_VPS_USER_ACCEPTANCE=PASS.

It authorizes:

- exact existing task branch/worktree;
- current-main synchronization;
- bounded conflict resolution;
- local README preservation/reconciliation;
- release metadata cleanup;
- generated parity;
- full tests/release validation;
- main integration through current bounded non-force path;
- formal release ref movement through current bounded release path;
- Issue #93 closure only when board policy is satisfied.

It forbids:

- force push/rebase;
- raw broader fallback publication;
- remote remap;
- unrelated source changes;
- C4 Skill change;
- central Plugin behavior changes;
- Bridge Kit changes;
- private Project export;
- live network mutation;
- GitHub Release object unless current repo policy requires it.

Check whether this authority is sufficiently narrow and complete.

## 13. Issue #93 lifecycle

Issue #93 remains DOING through wrapper creation and user acceptance.

Only after formal main/release closure may it become DONE.

If Project-field mutation is unavailable, the task must leave an exact pending mutation and not ask the user to maintain the board manually.

Check this against current board policy.

## 14. PASS / REVISE

If this package is sufficient and does not reopen implementation:

CRITIC_RESULT=PASS
FINAL_DELIVERY_PLAN=PASS
CHATGPT_WRAPPER_PLAN=PASS
SERVER_VPS_ACCEPTANCE_PLAN=PASS
LOCAL_README_PRESERVATION=PASS
INTEGRATION_RELEASE_CONTRACT=PASS
GATE_TAXONOMY_CHANGED=NO
C4_RUNTIME_CHANGE_AUTHORIZED=NO

APPROVED_PLAN_PATH=
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md

APPROVED_GOAL_PATH=
docs/goals/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_1.md

APPROVED_KICKOFF_PATH=
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md

APPROVED_PACKAGE_COMMIT=
7bbe8d5982b9cd6abdca503ca6b12094976b92c6

NEXT_HANDOFF=
CHATGPT_WRAPPER_CREATION_AND_SERVER_VPS_ACCEPTANCE

Do not say READY_FOR_RELEASE=YES yet.

At PASS, state clearly:

1. the assistant may create the private personal wrapper from exact C4;
2. the user then performs one Server+VPS acceptance session;
3. only if USER_ACCEPTANCE=PASS may the already-reviewed integration/release Kickoff be sent to Codex.

If REVISE:

CRITIC_RESULT=REVISE
NEXT_HANDOFF=PLANNER

Every blocker must have a stable ID, direct evidence, causal risk, and minimum closure.

Do not block because the plan could be more verbose.
