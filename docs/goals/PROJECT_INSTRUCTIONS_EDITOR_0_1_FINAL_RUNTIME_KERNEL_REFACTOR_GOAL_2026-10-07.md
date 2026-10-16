# PIE 0.1 Final Runtime Kernel Refactor Goal

Repository:

```text
YuukiAS/AI_Skills_Collection
```

Branch:

```text
work/project-instructions-editor--0.1-closure
```

The user explicitly declined another Critic round. This is the final bounded
simple-core repair before one more real Server+VPS acceptance.

Read first:

```text
AGENTS.md
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_1_FINAL_RUNTIME_KERNEL_REFACTOR_V0_1_2026-10-07.md
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
tests/test_project_instructions_editor_contract.py
docs/skill-todos/project-instructions-editor.md
```

Use C6 only as the historical structural reference named in the design. Do not
restore it wholesale and do not reopen C7-C11 language-finalizer work.

## Task

Refactor PIE 0.1 candidate construction rather than adding more checks.

Implement the design's short K1-K7 runtime kernel:

```text
K1 freeze Allowed Durable Meaning Set
K2 normalize meanings
K3 form semantic families
K4 apply global transforms
K5 render fresh complete candidate
K6 bidirectional reconciliation
K7 concise user delivery
```

The critical product changes are:

1. separate **semantic mutation radius** from **surface reconstruction radius**;
   bounded semantics must not force paragraph-by-paragraph patching of the live
   setting;
2. preservation-sensitive complete replacements must be freshly rendered from
   normalized families when structure itself is defective;
3. use a closed-world durable meaning set so history, memory, old candidates,
   model best practice, and incidental source examples cannot independently add
   new durable rules or example lists;
4. examples count as semantic content and need authority;
5. dynamic-set abstraction applies globally across the candidate;
6. scope dominance applies only among currently allowed meanings and must not
   resurrect historical-only broad rules;
7. final reconciliation is bidirectional: coverage of allowed meanings +
   provenance for every candidate rule/detail.

## Refactor, do not append

The current production Skill has accumulated too many repair-era instructions.

Reorganize it so K1-K7 is the dominant normal-entry path near the top. Remove or
merge duplicated runtime prose. Move detailed rationale/edge cases to
`references/editor-contract.md`.

Do not weaken:

- live-setting precedence;
- edit modes;
- no-op eligibility;
- protected absence;
- ownership vs effective enforcement;
- locator safety;
- authorization / privacy / safety / evidence / uncertainty / completion;
- exact identities;
- honest degradation;
- current-artifact target-language responsibility;
- C11 unsupported reader-layer boundary.

Do not add:

- token scanning;
- English ratios;
- blacklists;
- translation dictionaries;
- fixed section counts;
- fixed platform/device terms;
- Server+VPS branch;
- sibling `chinese-prose` chain;
- MCP/API/external finalizer;
- C12.

## Regression tests

Add generic structural coverage for:

- bounded semantic change + global surface reconstruction;
- closed-world behavior preventing opportunistic historical/best-practice
  additions;
- the same mutable source-owned set appearing in multiple sections;
- live broad + live narrow scope dominance;
- historical-only broad + live narrow protected absence.

Do not assert exact final wording or exact section count.

Run the focused PIE tests and normal repository validation required by current
AGENTS.

If no already-authorized standalone runtime replay harness exists, record
`DEVELOPMENT_REPLAY=NOT_RUN`; do not improvise a new control plane.

## Wrapper

If source changes, build exact-source personal wrapper candidate:

```text
wrapper version = 0.2.5
Skill version = 0.1
```

Do not mutate the live wrapper unless the existing authorized wrapper-update
path is available after repository validation. Otherwise stop with the exact
candidate/handoff.

## Stop

Stop before main/release integration.

After this repair there is exactly one more fresh Server+VPS Web acceptance.

If that acceptance repeats scaffold copying, global dynamic-set leakage, current
scope narrowing, unsupported durable additions, or bidirectional traceability
failure, do not design another prompt repair. Record simple-core full-setting
restructure as unsupported/release-scope-limited and return to Planner for
scope closure.

Final report only:

```text
FINAL_SOURCE_COMMIT=
PIE_SKILL_VERSION=0.1
RUNTIME_KERNEL_REFACTOR=
SEMANTIC_VS_SURFACE_RADIUS=
CLOSED_WORLD_MEANING_SET=
BIDIRECTIONAL_RECONCILIATION=
GLOBAL_DYNAMIC_SET_ABSTRACTION=
SCOPE_DOMINANCE_WITH_PROTECTED_ABSENCE=
FOCUSED_TESTS=
DEVELOPMENT_REPLAY=
WRAPPER_CANDIDATE=
SERVER_VPS_ACCEPTANCE_READY=
ONE_MORE_ATTEMPT_STOP_RULE=YES
C11_READER_LAYER_FAILURE_PRESERVED=YES
```
