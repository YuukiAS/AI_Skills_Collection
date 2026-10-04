# Project Instructions Editor — Final Delivery Closure Plan v0.2

Date: 2026-10-04
Status: DRAFT_FOR_CRITIC_REVIEW
Repository: YuukiAS/AI_Skills_Collection
Task key: project-instructions-editor--standalone-skill-implementation
Tracking: #93
Supersedes: PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md
Critic finding disposition: FD1=ACCEPT

Approved implementation identities:

FINAL_CANDIDATE_COMMIT = 266334ca807640b08605faddbdded7d5a6591aa1
EVIDENCE_HEAD = 34428d3db409ffc97aea36cc3776c14f33b94289
G4 review PASS = 254e9ea5ca1739dee0689afa13f7a1d34ac4469d
Implementation review PASS = ad217bd9d131456ba646fe70367a1b77a7fc912f

Implementation state:

IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS
READY_FOR_INTEGRATION=YES
READY_FOR_RELEASE=NO

This plan does not reopen the product architecture or the four Capability Gates. It freezes the remaining delivery path: private ChatGPT distribution wrapper, one real Server+VPS acceptance, then main/release closure without changing the accepted C4 Skill tree.

## 1. Current formal release baseline and FD1

Planner re-read the current formal release contract and directly compared the live refs.

Observed at this planning round:

origin/release = 03b0281b1f7fbd29621faa6298cd1db2578a0ffc
origin/main = 2dd26aa17aa695a80d6eacc39afe4de4857f147a
release VERSION = 5.4.3
main VERSION = 5.4.3
workflow-core on main = 0.5
presentations on main = 0.3

The residual origin/release..origin/main diff is non-empty and currently includes unrelated Presentations production/generated source:

- plugins/codex/plugins/presentations/shared/font-policy.md
- plugins/codex/plugins/presentations/shared/template-routing.md
- skills/tools/documents-media/presentations/shared/font-policy.md
- skills/tools/documents-media/presentations/shared/template-routing.md
- tests/test_codex_marketplace.py
- tests/test_standalone_skill_baselines.py

Root CHANGELOG still says Unreleased: No unreleased changes. Therefore the current observed main is not a release-clean baseline for PIE final publication even though VERSION remains 5.4.3.

FD1 is accepted. The v0.1 rule “any non-overlapping 5.4.x main drift is harmless” was too broad.

The stable authority is now:

- origin/release is the formal release baseline;
- VERSION alone does not prove release cleanliness;
- main may contain parallel development that is not yet part of a formal release;
- only formal release closure may advance release.

Repository release decision for PIE remains MINOR because Project Instructions Editor is a new standalone repository-level user capability.

If the final formal baseline remains a compatible 5.4.x release and PIE is not already integrated, target remains:

repository = 5.5.0
project-instructions-editor = standalone 0.1
central plugins = NO_BUMP

Parallel development is expected and does not invalidate this Plan. Exact main/release SHAs above are observations, not frozen execution prerequisites.

The only new requirement is a repeatable FORMAL_RELEASE_CLEANLINESS_PREFLIGHT immediately before final integration/release mutation.

## 2. Final delivery sequence

The remaining sequence is:

1. Critic approves this final-delivery closure package.
2. Create one PRIVATE / USER-scope / skills-only ChatGPT personal Plugin wrapper from exact C4.
3. Use that wrapper once in the real Server+VPS Project to edit or no-op the live Project instructions.
4. Apply the accepted Project-setting result if needed.
5. In a fresh Server+VPS Project thread, run one natural acceptance question without style coaching.
6. If the first response passes, record USER_ACCEPTANCE=PASS.
7. Run FORMAL_RELEASE_CLEANLINESS_PREFLIGHT against the then-current origin/release and origin/main.
8. If the residual drift is only formal-baseline history or docs/TODO/evidence-only non-production drift, continue the already-reviewed final integration/release Kickoff.
9. If unrelated unreleased production/generated/plugin/profile/routing/runtime drift exists, stop only the integration/release mutation with READY_FOR_RELEASE=NO and WAITING_FOR_FORMAL_RELEASE_BASELINE=YES. Wrapper creation and Server+VPS acceptance remain valid.
10. When the unrelated work completes its own formal release and origin/release advances, rerun the same cleanliness preflight. A new Planner/Critic round is not required merely because the formal 5.4.x baseline advanced compatibly.
11. Integration must prove the accepted C4 Skill tree is byte-identical after reconciliation.
12. Merge/integrate to main and advance the formal release only under the reviewed release contract.
13. Close Issue #93 only after release closure and required Project lifecycle evidence are truthful.

The user is not a regression suite. No multi-device, multi-prompt, repeated acceptance loop is allowed.

This sequence is deliberately tolerant of parallel development: unrelated development may continue on main, but PIE must not publish it accidentally.

## 3. ChatGPT personal Plugin wrapper

Current Plugin Creator inventory shows one owned personal wrapper for Project Thread Handoff and no existing Project Instructions Editor wrapper.

Therefore Project Instructions Editor needs one initial wrapper creation, not an update.

### 3.1 Canonical source

The wrapper must bundle exact C4 source:

skills/core/codex-system/project-instructions-editor/

Required C4 runtime files:

- SKILL.md
- agents/openai.yaml
- assets/app-facing.svg
- evals/trigger_queries.json
- references/editor-contract.md

The canonical source remains the standalone Skill. The personal Plugin is only a distribution wrapper.

### 3.2 Wrapper identity

Initial wrapper:

name = project-instructions-editor
version = 0.1.0
scope = USER
discoverability = PRIVATE
skills-only = YES
MCP = NO

Do not create a central Marketplace Plugin.

### 3.3 Icon

Do not search for, redraw, redesign, or ask the user to locate an icon.

Canonical icon:

skills/core/codex-system/project-instructions-editor/assets/app-facing.svg
@ C4

The wrapper must contain:

assets/app-facing.svg
skills/project-instructions-editor/assets/app-facing.svg

Both copies must be byte-equivalent to the C4 canonical SVG.

Both plugin manifests must point:

composerIcon = ./assets/app-facing.svg
logo = ./assets/app-facing.svg

SVG is already supported by the current Project Thread Handoff personal wrapper precedent. Deterministic conversion is allowed only if Plugin Creator explicitly rejects SVG; redesign is never allowed.

### 3.4 Wrapper manifests

Follow the verified Project Thread Handoff wrapper shape:

plugin.json
.codex-plugin/plugin.json
assets/app-facing.svg
skills/project-instructions-editor/**

No MCP, connector, Developer Mode dependency, external API, database, app state, watcher, or new control plane.

### 3.5 Future updates

The user must not be required to copy Plugin IDs, find icons, rebuild archives, or manually maintain the wrapper.

Future update flow:

1. use Plugin Creator inventory to find the unique owned personal Plugin named project-instructions-editor;
2. read current release ID and existing files;
3. compare against the exact canonical Skill commit;
4. build an overlay archive using the canonical Skill and canonical icon;
5. update with expected_release_id optimistic concurrency;
6. preserve the same Plugin identity;
7. report only the result.

If zero wrappers exist after initial creation, create only with explicit authorized bootstrap.
If multiple same-name wrappers exist, ask one minimal clarification.
If a future source update requires file deletion/rename that overlay semantics cannot safely remove, stop rather than leave stale files.

Private Plugin ID / URL must not be committed to the public repository.

## 4. Server+VPS final user acceptance

The final real consumption surface is the user's actual Server+VPS ChatGPT Project.

The full live Project instructions and private infrastructure context are not committed to AI_Skills_Collection.

### 4.1 Editor use

In the Server+VPS Project, explicitly invoke the private Project Instructions Editor wrapper for this one acceptance preparation step.

Ask it to inspect the current live Project instructions against the real bad-answer failure:

- audit/report structure appeared before the actual conclusion;
- unnecessary English and internal process language leaked into explanatory prose;
- closed checks were over-explained;
- the actual remaining blocker appeared too late;
- “do I need to act?” was not stated early enough;
- next action was not concentrated;
- the same conclusion was repeated through PASS/FAIL/status language;
- the response did not distinguish “Project setting missing a rule” from “existing Project rule was simply not followed”.

The editor must choose among:

- bounded edit;
- bounded consolidation/reordering;
- no-op + execution-noncompliance diagnosis.

It must not assume that adding more rules is correct.

If the ChatGPT surface does not expose the exact live Project-setting text to the Skill, the Skill may ask once for the current baseline. That is expected safe degradation, not failure.

### 4.2 Reading-layer acceptance

A good Server+VPS answer must prioritize:

1. what actually remains wrong or whether it is solved;
2. whether the user needs to do anything now;
3. the single next action;
4. only then the minimum technical reason/evidence.

Unnecessary English is itself part of this acceptance.

Ordinary explanatory concepts should be natural Chinese. English should remain only when the exact product/project identity, path, command, field, state value, process name, file name, version, or other machine string is needed for execution or unambiguous reference.

A response should not lead with:

- PASS/FAIL/UNKNOWN matrices;
- implementation-verdict labels;
- SHA/PID/job/status dumps;
- internal reviewer/workflow labels;
- long lists of already-closed checks;
- repeated versions of the same conclusion.

This readability requirement must not weaken ownership, authorization, fail-closed behavior, privacy, secrets, evidence strength, or exact technical identifiers.

### 4.3 Frozen natural acceptance question

After applying the accepted setting edit, or after a justified no-op, open a fresh thread in the real Server+VPS Project and ask once:

“按最新实现审一下 Workstation 自动恢复，现在到底能不能放心不管了？还有什么会卡住？”

Do not restate style rules in this prompt.

If the real Workstation issue has materially changed, preserve the same natural task shape but use the current remote-recovery state rather than forcing stale technical facts.

### 4.4 PASS criteria

The first response must:

- lead with the actual current conclusion;
- immediately state whether user action is needed;
- state the next action before deep evidence;
- avoid unnecessary English in explanatory prose;
- avoid audit/status machinery as the opening narrative;
- avoid re-listing closed items unless needed;
- avoid repeated conclusions;
- preserve correct Clash_Profile / Remote_Compute_Infrastructure / MACHINE_LOCAL_INFRA ownership;
- preserve user-controlled live network state;
- preserve USER_ACTION_REQUIRED semantics;
- not ask the user to become the regression suite;
- not turn source-only evidence into live/global verification;
- keep unresolved facts unresolved.

If it fails, record USER_ACCEPTANCE=FAIL and preserve the first output. Do not repair the answer and call the same attempt PASS.

## 5. Plugin Creator and user burden

After Critic PASS, the assistant—not the user—owns:

- wrapper archive construction;
- canonical icon selection;
- manifest construction;
- initial Plugin Creator creation;
- future Plugin Creator updates.

The user owns only the unavoidable live ChatGPT Project actions:

- invoke the private wrapper in Server+VPS;
- apply the resulting Project-setting edit if any;
- open a fresh thread;
- send the one frozen natural acceptance question;
- return the first response.

No manual icon search, Plugin ID copying, archive building, README editing, or multi-prompt regression session is requested from the user.

## 6. README local-state rule

Do not use the current remote README as the integration source of truth for the Project Instructions Editor reader-facing section.

The user explicitly states that the exact integration worktree may already contain newer local README edits that are not pushed.

Therefore the final integration Executor must, before fetch/merge or README mutation:

1. inspect the exact local worktree;
2. run git status --short;
3. inspect git diff -- README.md and staged README diff if present;
4. treat task-owned local Project Instructions Editor README wording as an input that must be preserved/reconciled, not overwritten by remote text;
5. never reset, restore, stash, or discard it silently.

If local README changes touch only the Project Instructions Editor card / ChatGPT-use / release wording and are consistent with the accepted capability, they may be incorporated into the integration candidate.

If local README changes are unrelated or ownership is ambiguous, stop with one precise blocker rather than overwriting them.

Any final README modification must also satisfy the current AGENTS rule requiring an actual Clear Writing invocation over the affected reader-facing region before commit.

## 7. Release metadata cleanup

Implementation review already identified two non-product release cleanups:

1. CHANGELOG stale wording that implies a current/empty/reset baseline is required for discovery.
2. README still showing Project Instructions Editor as “开发中”.

These can be fixed during final integration without re-running G1–G4 if and only if the accepted C4 Skill tree remains byte-identical.

Correct release semantics:

- an explicit Project-instruction editing request may route to PIE even when the live baseline is missing;
- missing baseline causes safe degradation/request for the baseline, not owner loss.

If the private ChatGPT wrapper and Server+VPS acceptance both pass, README may state in one short user-facing sentence that Project Instructions Editor can also be used through a private skills-only ChatGPT personal Plugin wrapper, with no MCP. Do not expose private Plugin ID/URL.

## 8. Formal release cleanliness and final integration/release boundary

Final integration still occurs only after:

IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS
SERVER_VPS_USER_ACCEPTANCE=PASS

Before any final integration/release mutation, run:

FORMAL_RELEASE_CLEANLINESS_PREFLIGHT

### 8.1 Resolve authoritative refs

Fetch and resolve both:

- origin/release;
- origin/main.

Read the VERSION, root CHANGELOG, plugin/standalone versions, and current release producer contract from the resolved refs.

The formal baseline is origin/release, not the numeric VERSION on main.

### 8.2 Compare release..main

Compute the exact origin/release..origin/main diff.

Classify the state into:

A. FORMAL_RELEASE_BASELINE

Changes already reachable from the current origin/release are formal history and are the baseline. If another task advances origin/release during parallel work, rerun this preflight and use the new formal baseline.

B. NON_PRODUCTION_DRIFT

Residual main-only changes that are strictly docs / TODO / review / evidence / planning material and do not alter production source, generated runtime identity, plugin/profile exposure, routing, runtime behavior, release payload, or user-visible installed behavior.

B is harmless for PIE release scope.

C. UNRELEASED_PRODUCTION_DRIFT

Residual main-only changes that alter any production or generated plugin/Skill/profile/routing/runtime behavior, install/distribution payload, shared production tests that encode behavior, or other user-visible release content that is not present in origin/release.

C is not harmless merely because:
- VERSION still starts with 5.4;
- the changes do not overlap the PIE Skill tree;
- the changes are from another task;
- the changes are already on main.

### 8.3 Decision

If residual drift is only B, PIE may continue.

If another task has already formally closed its work and advanced origin/release, that work becomes part of A after the preflight is rerun; PIE may continue from that newer compatible formal baseline.

If any C exists:

READY_FOR_RELEASE=NO
WAITING_FOR_FORMAL_RELEASE_BASELINE=YES

Do not:
- revert the unrelated task;
- reset/restore/stash away its work;
- ad-hoc cherry-pick a private release composition;
- silently absorb the behavior into PIE 5.5.0;
- force/rebase refs;
- bypass the formal release producer.

Default recovery is simple: wait for the unrelated production work to complete its own formal release closure, then rerun this same preflight.

This waiting condition does not invalidate C4, the private wrapper, Server+VPS acceptance, or this approved closure package. It does not require a new Planner round as long as the new formal baseline remains a compatible 5.4.x line, PIE is not already integrated, and no direct PIE source/distribution conflict appears.

A separately reviewed isolated-integration strategy is allowed in principle, but this Plan does not design or authorize one.

### 8.4 Integration after cleanliness PASS

Once FORMAL_RELEASE_CLEANLINESS_PREFLIGHT=PASS:

- sync the release-clean latest main into the exact task branch without rewriting history;
- preserve all formal 5.4.x release history and current plugin/standalone versions;
- reconcile release metadata to 5.5.0;
- preserve C4 Skill tree byte-for-byte;
- regenerate derived registry/catalog/provenance with current generators;
- run current deterministic/full repository tests and release checks;
- run the required Clear Writing README check;
- prove no accepted Skill runtime change occurred.

Immediately before main/release movement, rerun the cleanliness preflight because parallel work may have landed since the first check.

If C appears at that second check, stop publication and wait; do not rebuild scope around it.

If C4 Skill tree changes, stop and return to implementation review; do not call it a metadata-only integration.

After integration validation and a final cleanliness PASS, main and formal release movement must use the repository's current bounded, non-force producer path.

## 9. Issue #93 closure

Issue #93 stays DOING through wrapper creation and user acceptance.

Only after successful main/release closure may it move to DONE.

If Project-field mutation is available, set Resolution commit and complete the Project lifecycle according to AI_SKILLS_MAINTENANCE_BOARD.md.

If Project-field mutation is unavailable, do not ask the user to maintain the board manually. Record the exact pending mutation and do not claim DONE until the lifecycle is truthfully complete.

Reader-facing Issue updates require actual Clear Writing invocation.

## 10. Stop conditions

Before Server+VPS user acceptance:

READY_FOR_RELEASE=NO

If user acceptance fails:

READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

If FORMAL_RELEASE_CLEANLINESS_PREFLIGHT finds unrelated unreleased production drift:

WAITING_FOR_FORMAL_RELEASE_BASELINE=YES
READY_FOR_RELEASE=NO

This is a release-channel wait, not a PIE product failure and not a reason to undo other parallel development. After the unrelated work advances the formal release baseline, rerun the same preflight.

If user acceptance passes but C4 Skill tree changes during integration:

READY_FOR_RELEASE=NO
RETURN_TO_IMPLEMENTATION_REVIEW=YES

Only after successful integration/release closure:

FORMAL_RELEASE_CLEANLINESS_PREFLIGHT=PASS
READY_FOR_RELEASE=YES
FINAL_SERVER_VPS_USER_ACCEPTANCE=PASS

