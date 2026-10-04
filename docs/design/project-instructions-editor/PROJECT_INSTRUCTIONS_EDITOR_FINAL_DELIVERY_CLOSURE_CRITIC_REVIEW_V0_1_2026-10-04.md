# Project Instructions Editor — Final Delivery Closure Critic Review v0.1

Date: 2026-10-04  
Result: `REVISE`  
Repository: `YuukiAS/AI_Skills_Collection`  
Review stage: final ChatGPT distribution + Server+VPS real user acceptance + integration/release closure  
Tracking: `#93`

Reviewed package:

- Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md`
- Goal: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_1.md`
- Kickoff: `docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md`
- Package commit: `7bbe8d5982b9cd6abdca503ca6b12094976b92c6`

Accepted implementation identity remains:

```text
FINAL_CANDIDATE_COMMIT=C4=266334ca807640b08605faddbdded7d5a6591aa1
EVIDENCE_HEAD=E4=34428d3db409ffc97aea36cc3776c14f33b94289
IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS
```

The Plan/Goal/Kickoff blobs on current main remain byte-identical to the reviewed package commit. The product architecture and G1–G4 are not reopened.

## 1. ChatGPT wrapper plan — PASS

The current Plugin Creator surface was checked directly.

Current personal inventory contains one owned private USER-scope wrapper named `project-thread-handoff` and no `project-instructions-editor` wrapper. Therefore PIE requires an initial creation rather than an update.

The existing Project Thread Handoff wrapper confirms the proposed distribution shape is real rather than hypothetical:

- scope = USER;
- discoverability = PRIVATE;
- skills-only package;
- root `assets/app-facing.svg`;
- bundled Skill `assets/app-facing.svg`;
- both `plugin.json` and `.codex-plugin/plugin.json` point `composerIcon` and `logo` to `./assets/app-facing.svg`;
- SVG is accepted directly;
- no MCP is present.

Current Plugin Creator semantics also match the future-update contract:

- personal creation is PRIVATE and USER-scope in the current personal-account surface;
- `update_plugin` requires the current `expected_release_id`;
- update is overlay semantics;
- omitted files remain, and the tool cannot delete files.

Therefore the Plan correctly stops on ambiguous duplicate identity or structural delete/rename instead of pretending overlay update can remove stale files.

The wrapper remains a distribution shell around exact C4. No central Marketplace Plugin, MCP, connector, external API, database, app state, watcher, or control plane is justified.

```text
CHATGPT_WRAPPER_PLAN=PASS
```

## 2. Icon plan — PASS

The user does not need to locate or redesign an icon.

The accepted C4 canonical icon remains:

`skills/core/codex-system/project-instructions-editor/assets/app-facing.svg`

The wrapper contract requires both the root and bundled icon copies to be byte-equivalent to that source and forbids redesign. The existing Project Thread Handoff wrapper independently demonstrates that the current personal Plugin surface accepts the same SVG pattern.

```text
ICON_DELIVERY_PLAN=PASS
```

## 3. Server+VPS acceptance plan — PASS

The chosen real acceptance surface is the user's actual Server+VPS ChatGPT Project.

The frozen acceptance order matches the current Project contract:

1. actual conclusion first;
2. immediately say whether the user must act;
3. give the next action before deep evidence;
4. use natural Chinese for ordinary explanation;
5. preserve exact machine identifiers where required;
6. keep repository ownership, machine-local ownership, authorization, evidence strength, fail-closed behavior, and live network-state boundaries intact.

The acceptance also correctly distinguishes:

- a missing Project-setting rule; from
- an existing rule that the current response failed to follow.

That distinction prevents the editor from responding to every poor answer by adding more long-lived rules.

The exact live Server+VPS Project setting is not directly exposed to this Critic surface. That does not block the plan because the live acceptance step itself must inspect the real setting, and the contract allows at most one baseline request if the product surface cannot expose it.

The single fresh-thread prompt is appropriate. It is a real consumption check after G1–G4, not a new G5, and the first failed answer remains FAIL rather than being repaired into PASS.

```text
SERVER_VPS_ACCEPTANCE_PLAN=PASS
GATE_TAXONOMY_CHANGED=NO
```

## 4. User burden — PASS

The plan correctly keeps wrapper archive construction, manifest/icon handling, Plugin Creator creation, and future wrapper updates away from the user.

The user only needs to perform the unavoidable real-Project actions:

- invoke the private PIE wrapper in Server+VPS;
- provide the live setting once only if the runtime cannot access it;
- apply the bounded edit if the result is not a no-op;
- open one fresh Server+VPS thread;
- ask the frozen natural question once;
- return the first answer.

No manual Plugin ID lookup, icon search, ZIP construction, README edit, multi-device matrix, or repeated prompt loop is required.

```text
USER_BURDEN_PLAN=PASS
```

## 5. Local README preservation — PASS

The final Kickoff correctly protects the exact local integration worktree before fetch/merge or README rewriting:

- inspect `git status --short`;
- inspect unstaged and staged README diffs;
- preserve task-owned local PIE wording;
- no reset/restore/stash/discard.

Current main `AGENTS.md` also does require a real installed Clear Writing invocation before any root README mutation. The Kickoff correctly treats Clear Writing as a language-quality check that cannot change version, paths, identity, technical meaning, or release truth.

```text
LOCAL_README_PRESERVATION=PASS
```

## 6. C4 immutability — PASS

The integration boundary is correct:

- release metadata/generated parity/integration evidence may change;
- the accepted C4 Skill tree may not.

Accepted runtime tree identity:

`c504970421c4d14ce9ac5cc1140c014cc5c7fff4ec826b5ab8c66adbe6db42c3`

If any file under `skills/core/codex-system/project-instructions-editor/**` changes, the package correctly returns to implementation review rather than reusing stale G1–G4 evidence.

```text
C4_RUNTIME_CHANGE_AUTHORIZED=NO
C4_IMMUTABILITY_CONTRACT=PASS
```

## 7. FD1 — final release preflight does not distinguish formal patch drift from unrelated unreleased production drift

Status: blocking.

### Requirement

The AI_Skills formal release producer contract says only an exact formally closed release commit may advance `release`.

Ordinary newer `main` commits do not become formal releases merely because they are ancestors of a later task branch. A final release must not silently publish unrelated in-progress production behavior under another task's version/closure.

The final-delivery Plan correctly allows non-overlapping **formal 5.4.x patch drift**, but its stop conditions only check:

- main >= 5.5.0;
- PIE already integrated;
- version policy changed;
- direct overlap with PIE source/distribution.

That is not sufficient when `main` is ahead of the formal `release` ref with unrelated production changes that have not themselves been formally closed.

### Direct evidence

At final Critic review time:

```text
origin/release = 03b0281b1f7fbd29621faa6298cd1db2578a0ffc
origin/main    = c885460d53a2df353e10b7d653711afa4a107b25
main VERSION   = 5.4.3
release..main  = 17 commits ahead
```

The formal `release` ref still points to the 5.4.3 Project Thread Handoff closure.

But `release..main` already contains unrelated Presentations production/generated changes:

```text
plugins/codex/plugins/presentations/shared/font-policy.md
plugins/codex/plugins/presentations/shared/template-routing.md
skills/tools/documents-media/presentations/shared/font-policy.md
skills/tools/documents-media/presentations/shared/template-routing.md
tests/test_codex_marketplace.py
tests/test_standalone_skill_baselines.py
```

Meanwhile:

- root `CHANGELOG.md` still says `Unreleased: No unreleased changes`;
- `presentations` remains version `0.3`;
- the formal release ref has not advanced to these commits.

This is not ordinary already-released 5.4.x patch drift. It is current-main production drift beyond the formal release channel.

### Causal risk

If the current Kickoff simply merges latest `origin/main` into the PIE task branch and then advances formal `release` to that combined commit, the PIE 5.5.0 release can silently ship unrelated Presentations production changes that have not been closed/versioned as part of this task.

That would violate:

- AI_Skills release-channel producer semantics;
- isolated-release scope;
- per-plugin version/changelog discipline;
- the package's own prohibition on changing unrelated central Plugin behavior.

The fact that the unrelated changes do not overlap the PIE Skill tree does not make them safe to publish.

### Minimum closure

Planner only needs a narrow v0.2 amendment to the final-delivery Plan/Goal/Kickoff. Do not reopen PIE implementation or Server+VPS acceptance.

Before any final integration/release mutation, require an explicit **formal release cleanliness preflight**:

1. fetch and resolve both `origin/release` and `origin/main`;
2. compare `origin/release..origin/main`;
3. distinguish:
   - already formally closed release history / docs-only evidence drift; from
   - unrelated unreleased production/generated/plugin/profile behavior;
4. if unrelated unreleased production behavior exists, do **not** let the PIE release sweep it into `release`;
5. final integration may proceed only after that unrelated production drift is itself formally closed/released, or after a separately reviewed integration strategy proves an isolated release candidate without broadening PIE scope;
6. do not solve this by reverting/discarding another task's work, cherry-picking ad hoc, force-moving refs, or silently absorbing the other work into PIE 5.5.0.

The existing rule for harmless 5.4.x patch drift may remain, but it must be explicitly limited to **formal or docs/evidence-only non-production drift**.

Owner: Planner.

## 8. Version target

The approved repository release classification remains MINOR.

If the formal integration baseline is still a clean 5.4.x release line after FD1 is satisfied:

```text
target repository version = 5.5.0
project-instructions-editor = standalone 0.1
central plugins = NO_BUMP for this task
```

No version redesign is required.

## 9. Maintenance state

Issue #93 correctly remains open / DOING through wrapper creation, real Server+VPS acceptance, and integration preparation.

No DONE/release claim is permitted yet.

This Critic surface has no GitHub Project-field mutation tool, so Project-field synchronization is not claimed and the user is not asked to drag the board manually.

## 10. Decision

```text
CRITIC_RESULT=REVISE

FINAL_DELIVERY_PLAN=REVISE
CHATGPT_WRAPPER_PLAN=PASS
ICON_DELIVERY_PLAN=PASS
SERVER_VPS_ACCEPTANCE_PLAN=PASS
USER_BURDEN_PLAN=PASS
LOCAL_README_PRESERVATION=PASS
C4_IMMUTABILITY_CONTRACT=PASS
INTEGRATION_RELEASE_CONTRACT=REVISE

GATE_TAXONOMY_CHANGED=NO
C4_RUNTIME_CHANGE_AUTHORIZED=NO

BLOCKER=FD1
READY_FOR_RELEASE=NO
NEXT_HANDOFF=PLANNER
```

This review does not reopen C4, G1–G4, the private-wrapper architecture, or the Server+VPS acceptance design. Only the formal-release cleanliness preflight must be amended.
