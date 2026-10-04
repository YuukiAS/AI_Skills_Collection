# Project Instructions Editor — Final Delivery Closure Goal v0.1

Status: DRAFT_FOR_CRITIC_REVIEW
Task key: project-instructions-editor--standalone-skill-implementation
Plan: docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md

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
8. After user acceptance PASS, integrate latest main and the accepted C4 capability without changing the C4 Skill tree.
9. Reconcile README/CHANGELOG/repository version/generated parity to formal 5.5.0 release semantics.
10. Preserve all latest current-main 5.4.x release history and all unrelated current plugin/standalone versions.
11. Use actual Clear Writing for final README reader-facing edits.
12. Complete the formal main/release closure only after mechanical validation succeeds.
13. Keep Issue #93 open/DOING until formal release closure is truthful.

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

Planner observed main VERSION=5.4.3.

If integration-time main is still any 5.4.x formal release and Project Instructions Editor is not already integrated:

Repository bump decision: MINOR
target repository version: 5.5.0
project-instructions-editor: standalone 0.1
central plugins: NO_BUMP

Patch drift within 5.4.x is allowed if it does not overlap the accepted PIE Skill/distribution contract.

Stop if main is already 5.5.0+, PIE is already integrated, or current source creates direct semantic overlap.

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
INTEGRATION_VALIDATION=PASS
FORMAL_RELEASE_CLOSURE=PASS

may the task claim:

READY_FOR_RELEASE=YES

No release closure is authorized merely by this draft. The user must first send the Critic-approved integration/release Kickoff after Server+VPS acceptance PASS.
