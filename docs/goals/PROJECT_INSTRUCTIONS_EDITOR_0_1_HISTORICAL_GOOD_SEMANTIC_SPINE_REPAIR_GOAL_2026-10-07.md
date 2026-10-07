# Project Instructions Editor 0.1 — Historical-Good Semantic Spine Repair Goal

Work only on:

```text
YuukiAS/AI_Skills_Collection
branch: work/project-instructions-editor--0.1-closure
```

This is a bounded pre-release repair. The user explicitly does not want another
Critic round. Do not create C12.

## Required read order

First read latest branch/repo rules needed for this bounded task, then:

```text
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_1_HISTORICAL_GOOD_SEMANTIC_SPINE_REPAIR_V0_1_2026-10-07.md

current source:
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
tests/test_project_instructions_editor_contract.py
docs/skill-todos/project-instructions-editor.md
```

Then inspect the historical C6 implementation directly with Git, not summaries:

```text
git show 6ddab9029bbd96a21d7e5bf0317f7674c66cd909:skills/core/codex-system/project-instructions-editor/SKILL.md
git show 6ddab9029bbd96a21d7e5bf0317f7674c66cd909:skills/core/codex-system/project-instructions-editor/references/editor-contract.md
git show 6ddab9029bbd96a21d7e5bf0317f7674c66cd909:results/project-instructions-editor--standalone-skill-implementation/SERVER_VPS_R6_UNCOACHED_REGRESSION.md
git show 6ddab9029bbd96a21d7e5bf0317f7674c66cd909:results/project-instructions-editor--standalone-skill-implementation/C6_IMPLEMENTATION_CRITIC_REVIEW.md
```

Also read the preserved C7/C9/C10/C11 failure summaries already present in the
closure branch, only to ensure this repair does not reintroduce their failed
mechanism.

## Root cause to fix

Do not treat the latest failure as another English-token problem.

Current `9cdbe8ed712caf3a3a90592cd09c61ac146d9b02` added a useful durable semantic
map, but it is one level too flat. It classifies clauses without first clustering
them into a smaller semantic spine.

The latest real Server+VPS output therefore still:

- follows too much source/live-setting section structure;
- keeps a mutable platform enumeration in Project instructions;
- drops the broad current-task production-mutation authorization boundary while
  retaining a narrower client-network rule;
- splits overlapping normal user-delivery rules across sections;
- systematically echoes ordinary source vocabulary.

## Implement exactly this repair class

### 1. Two-level semantic spine

Keep atomic meanings, but cluster them into semantic families before drafting.

Family key should reason over:

```text
governed actor/surface
+ trigger/phase
+ intended behavior/prohibition
+ owner/authority
+ failure consequence
```

Draft from families, not source headings.

### 2. Structure is not protected

Make explicit that heading names/count/order, duplicated rationale, source
labels, and source grouping are not semantic invariants by default.

A preservation-sensitive cleanup may merge/reorder/rename them without changing
the protected rules.

### 3. Scope dominance

Add a generic semantic-subsumption check.

A broad authorization/safety/privacy/evidence/fail-closed rule cannot be removed
merely because a narrower special-case rule overlaps it.

Broad production mutation authorization must remain broad when it governs more
objects/actions than a client-network-specific rule.

Do not encode Server+VPS names into the mechanism.

### 4. Dynamic-set abstraction

If a client/platform/device/route/inventory set is mutable and canonically owned
elsewhere, preserve:

```text
all currently supported items defined by the canonical source
```

plus the required lookup bridge, not the current member list.

Concrete lists remain only when the member set itself is a durable user
constraint or a formal finite machine/protocol/state set.

### 5. Merge by trigger + user consequence

Overlapping normal user-delivery rules should have one primary home.

Do not merge a formal production-closure report into normal response behavior
when the trigger genuinely differs.

### 6. Pre-draft target-language terminology

For Chinese-facing Project instructions, choose natural Chinese names for
ordinary concepts at semantic-family construction time.

Source English is evidence, not vocabulary.

Do not add:
- Latin-token scanning;
- blacklist;
- translation table;
- English ratio;
- “reason for every token” logic.

A few isolated English words alone are not the final PIE blocker. Systematic
source-label organization is.

### 7. Final semantic-spine reconciliation

Before delivery, verify the actual candidate against the semantic spine:

- complete protected semantic coverage;
- no broader boundary narrowed by consolidation;
- dynamic sets abstracted;
- no duplicated meaning across families without a real trigger/consequence
  distinction;
- no source-heading inertia;
- no unsupported durable rules;
- protected absence intact;
- exact identities intact;
- candidate growth justified.

Do not expose this internal review to normal users.

## Historical behavior to preserve, not source to restore

C6 `6ddab902...` is development evidence, not a source rollback target.

Its useful behavior:

- removed copied volatile client list;
- kept source-owner bridge;
- kept broad production authorization;
- kept privacy/evidence/fail-closed semantics;
- produced a compact durable setting.

Its known defects must stay fixed:

- no internal `preservation-sensitive` label in ordinary output;
- do not restore its token-oriented R7 mechanism;
- do not restore `Project setting` / `secret value` leakage as acceptable.

Do not cherry-pick C6 wholesale.

## Tests and development replays

Update contract tests for the new structural semantics.

Add a generic public-safe structural fixture containing:

- broad + narrow authorization rules;
- mutable source-owned set;
- duplicated normal user-delivery sections;
- distinct closure trigger;
- protected deletion history;
- privacy/evidence/fail-closed semantics;
- ordinary English source labels;
- exact identities.

Tests must not assert:
- exact section count;
- exact final wording;
- banned English terms;
- English percentage.

Run at least:

```text
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python scripts/skills.py validate
python scripts/skills.py audit --all
git diff --check
```

If the existing local Codex/runtime replay harness can execute without new
infrastructure, run two **development-only** qualitative replays:

A. historical C6 public-safe Server+VPS case from immutable commit;
B. the new generic complex structural fixture.

Save complete outputs and qualitative review. Do not call either fresh final
evidence.

If the replay harness is unavailable, say so plainly; do not replace it with a
mechanical fixture PASS claim.

## Wrapper

The currently live personal wrapper is:

```text
version=0.2.3
Skill version=0.1
```

If PIE source changes, build a new exact-source wrapper candidate:

```text
wrapper version=0.2.4
Skill version=0.1
```

Do not mutate the live wrapper unless the current execution environment has the
authorized Plugin Creator path and the task's existing wrapper update contract
permits it. Otherwise produce the exact archive/handoff.

## Stop point

Stop after:

- source repair;
- focused validation;
- development replay if available;
- wrapper 0.2.4 candidate/handoff.

Do not integrate to main/release yet.

The next and only final user test remains one real Server+VPS ChatGPT Web fresh
thread. That real output decides release.

## Forbidden shortcuts

Stop if the implementation turns into:

- C12;
- Server+VPS-specific branch;
- fixed nine-section template;
- hard-coded Android/Windows/macOS/iPadOS handling;
- fixed Chinese terminology dictionary;
- English token scan;
- sibling `chinese-prose` chain;
- external finalizer/API/MCP;
- wholesale restoration of C6.

## Final report

Keep it short:

```text
FINAL_SOURCE_COMMIT=
PIE_SKILL_VERSION=0.1
SEMANTIC_SPINE_REPAIR=
SCOPE_DOMINANCE=
DYNAMIC_SET_ABSTRACTION=
STRUCTURAL_TESTS=
DEVELOPMENT_REPLAY=
WRAPPER_CANDIDATE=
SERVER_VPS_ACCEPTANCE_READY=
C11_READER_LAYER_FAILURE_PRESERVED=YES
```
