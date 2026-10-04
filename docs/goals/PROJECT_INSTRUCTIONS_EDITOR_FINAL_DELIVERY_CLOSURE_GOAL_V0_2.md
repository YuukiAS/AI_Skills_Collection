# Project Instructions Editor — Final Delivery Closure Goal v0.2

Status: DRAFT_FOR_CRITIC_REVIEW
Task key: project-instructions-editor--standalone-skill-implementation
Plan: docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_2_2026-10-04.md
Supersedes: docs/goals/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_1.md
Critic finding disposition: FD1=ACCEPT

## Goal

Close the accepted Project Instructions Editor implementation through the real ChatGPT delivery surface, one Server+VPS final user acceptance, and formal repository integration/release without changing the accepted C4 Skill behavior.

Accepted implementation identity:

FINAL_CANDIDATE_COMMIT=266334ca807640b08605faddbdded7d5a6591aa1
EVIDENCE_HEAD=34428d3db409ffc97aea36cc3776c14f33b94289
IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS

## Required final-delivery outcomes

1. Create one PRIVATE / USER-scope / skills-only ChatGPT personal Plugin wrapper around exact C4.
2. Reuse the exact C4 canonical app-facing.svg; do not redesign or ask the user to find an icon.
3. Keep the wrapper free of MCP, connector, external API, database, app state, watcher, and control-plane additions.
4. Use the wrapper in the user's real Server+VPS Project to produce either a bounded Project-setting edit or a justified no-op.
5. Use one fresh Server+VPS Project thread for the frozen natural acceptance question.
6. Require the first response to satisfy the accepted reading/order/ownership/evidence rubric.
7. Do not release if the real user acceptance fails.
8. Before final integration/release mutation, resolve origin/release and origin/main and run FORMAL_RELEASE_CLEANLINESS_PREFLIGHT.
9. Treat the formal release ref as the release baseline; VERSION on main alone is not proof that main is release-safe.
10. Allow direct continuation only when residual main-only drift is docs/TODO/review/evidence-only non-production drift, or when another task's production changes have already completed their own formal release and are now part of origin/release.
11. If unrelated unreleased production/generated/plugin/profile/routing/runtime drift exists, stop final integration/release with READY_FOR_RELEASE=NO and WAITING_FOR_FORMAL_RELEASE_BASELINE=YES. Do not revert, absorb, cherry-pick, force, or redesign around the other task.
12. After the unrelated task advances the formal release baseline, rerun the same cleanliness preflight. A compatible formal 5.4.x baseline advance does not mechanically require a new Planner round.
13. Integrate the accepted C4 capability only after the cleanliness preflight passes and without changing the C4 Skill tree.
14. Reconcile README/CHANGELOG/repository version/generated parity to formal 5.5.0 release semantics.
15. Preserve all formally released 5.4.x history and all current unrelated plugin/standalone versions from the clean formal baseline.
16. Use actual Clear Writing for final README reader-facing edits.
17. Complete formal main/release closure only after mechanical validation and a second release-cleanliness check immediately before ref movement.
18. Keep Issue #93 open/DOING until formal release closure is truthful.

## Wrapper identity

Initial personal wrapper:

name=project-instructions-editor
version=0.1.0
scope=USER
discoverability=PRIVATE
skills-only=YES
MCP_ADDED=NO

Canonical Skill source:

skills/core/codex-system/project-instructions-editor/
@ 266334ca807640b08605faddbdded7d5a6591aa1

Canonical icon:

skills/core/codex-system/project-instructions-editor/assets/app-facing.svg
@ the same C4 commit

Wrapper root and bundled Skill icon copies must be byte-equivalent to the canonical C4 SVG.

## Future wrapper update contract

The user must not need to supply an ID or icon.

Future updates should:

- discover the unique owned personal Plugin named project-instructions-editor;
- read current_release_id;
- compare packaged Skill against the exact canonical source commit;
- update using expected_release_id;
- preserve plugin identity;
- preserve canonical icon bytes;
- stop on ambiguous duplicate identity or unsafe structural deletion/rename.

Do not commit private Plugin ID/URL.

## Server+VPS final acceptance

Preparation request to the editor must ask it to assess the current live Project setting against the real failure class:

- conclusion/action/next step appearing too late;
- audit/status/report structure leading the answer;
- unnecessary English in explanatory prose;
- excessive discussion of already-closed checks;
- repeated conclusion/status language;
- failure to distinguish a missing Project rule from failure to follow an existing rule.

The editor may return bounded edit, bounded consolidation, or no-op.

If the exact live Project setting is not exposed to the Skill, one baseline request is allowed.

After applying the accepted result, or after justified no-op, open a fresh Project thread and ask:

按最新实现审一下 Workstation 自动恢复，现在到底能不能放心不管了？还有什么会卡住？

Do not add style coaching to that prompt.

USER_ACCEPTANCE=PASS only if the first answer:

- gives the real conclusion first;
- immediately states whether the user must act;
- gives the next action before deep evidence;
- uses natural Chinese for ordinary explanation;
- keeps English only where exact technical identity is needed;
- does not lead with PASS/FAIL/status/audit machinery;
- does not repeat the conclusion;
- preserves ownership, authorization, privacy, fail-closed, evidence-strength, and network-state boundaries.

A failed first answer remains a failure. Do not repair it and call the same acceptance PASS.

## Local README preservation

Before final integration, the Executor must inspect the exact local worktree before relying on remote README.

Required preflight:

git status --short
git diff -- README.md
git diff --cached -- README.md

Task-owned local Project Instructions Editor README wording must be preserved/reconciled rather than overwritten from remote.

Do not stash/reset/restore/discard local README changes.

Any final README edit requires real Clear Writing invocation before commit.

## Integration release target

The repository release decision remains MINOR.

Planner's observed refs during FD1 repair:

origin/release = 03b0281b1f7fbd29621faa6298cd1db2578a0ffc
origin/main = 2dd26aa17aa695a80d6eacc39afe4de4857f147a
release VERSION = 5.4.3
main VERSION = 5.4.3

The observed release..main residual currently includes unrelated Presentations production/generated source, so the current observed main is not itself a clean formal baseline for PIE publication.

Execution must not pin these SHAs. Parallel development may continue.

At integration time:

1. fetch and resolve origin/release and origin/main;
2. compare origin/release..origin/main;
3. classify the residual:
   - A = formal baseline/history already represented by origin/release;
   - B = docs/TODO/review/evidence-only non-production drift;
   - C = unrelated unreleased production/generated/plugin/profile/routing/runtime drift;
4. proceed only if residual drift is B-only, or after another task's production work advances origin/release and becomes part of A;
5. if C exists, set:
   WAITING_FOR_FORMAL_RELEASE_BASELINE=YES
   READY_FOR_RELEASE=NO
   and stop final integration/release mutation.

Default recovery for C is to wait for that work's own formal closure and rerun the same preflight. This wait is not a PIE product failure and does not invalidate wrapper/Server+VPS acceptance.

Do not solve C by reverting another task, reset/restore/stash, ad-hoc cherry-pick, force/rebase, silent absorption into PIE 5.5.0, or bypassing the formal release producer.

A separately reviewed isolated-integration strategy may exist, but is outside this Goal.

If the clean formal baseline remains on a compatible 5.4.x line and Project Instructions Editor is not already integrated:

Repository bump decision: MINOR
target repository version: 5.5.0
project-instructions-editor: standalone 0.1
central plugins: NO_BUMP

Stop and return to Planner only if the formal baseline is already 5.5.0+, PIE was already integrated, version policy changed, or there is direct PIE source/distribution overlap.

Immediately before main/release ref movement, rerun FORMAL_RELEASE_CLEANLINESS_PREFLIGHT. Parallel work that lands after the first preflight must not be swept into the PIE release.

## Skill immutability

Formal integration/release may update reader-facing metadata and generated parity only if the accepted C4 Skill tree remains byte-identical.

Accepted runtime tree identity:

RUNTIME_SKILL_TREE_HASH=c504970421c4d14ce9ac5cc1140c014cc5c7fff4ec826b5ab8c66adbe6db42c3

If the Skill tree changes, return to implementation review and rerun affected same-final-candidate evidence.

## Release metadata cleanup

Required before READY_FOR_RELEASE=YES:

- correct CHANGELOG discovery wording so missing live baseline means safe degradation, not owner loss;
- remove README “开发中” marker when formal release is actually being closed;
- preserve any newer task-owned local README wording;
- if private wrapper creation and Server+VPS acceptance passed, add at most a short truthful README statement that ChatGPT can use the Skill through a private skills-only personal Plugin wrapper with no MCP;
- preserve current-main release history and unrelated versions.

## Final completion

Only after all of the following:

IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS
SERVER_VPS_USER_ACCEPTANCE=PASS
C4_SKILL_TREE_UNCHANGED=YES
FORMAL_RELEASE_CLEANLINESS_PREFLIGHT=PASS
INTEGRATION_VALIDATION=PASS
FORMAL_RELEASE_CLOSURE=PASS

may the task claim:

READY_FOR_RELEASE=YES

If unrelated unreleased production drift exists:

WAITING_FOR_FORMAL_RELEASE_BASELINE=YES
READY_FOR_RELEASE=NO

That state does not require redoing C4, G1–G4, the private wrapper, or Server+VPS acceptance. Resume from the same cleanliness preflight after the formal release baseline advances compatibly.

No release closure is authorized merely by this draft. The user must first send the Critic-approved integration/release Kickoff after Server+VPS acceptance PASS.

