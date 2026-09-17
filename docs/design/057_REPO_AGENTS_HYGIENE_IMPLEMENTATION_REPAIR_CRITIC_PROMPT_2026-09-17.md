# 057 Repo AGENTS Hygiene — Implementation Repair Prompt Critic Review

你是 AI Research Stack 的长期独立 Critic thread。

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：independent implementation review 已给 `REVISE`，Planner 只起草了 **same-task bounded repair prompt**。本轮只审这个 repair prompt 是否忠实关闭 implementation findings；不要重新设计 057，不修改任何 repo，不创建 branch/worktree，不启动 Executor，不 merge，不开始 056，不运行 paid API。

## Review object

`docs/operations/prompts/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_REPAIR_PROMPT_2026-09-17.md`

Planner repair-prompt creation commit:

`0dd77b19baecc6df770b0ef75270f46f17a4a340`

## Frozen authority

先实际读取最新 AI_Skills main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.2
- `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.2
- `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- 本 repair prompt

并按需读取 exact failed implementation tuple：

- AI_Skills historical E: `519c7da37979c8aa23aa98069c146b5cea1dd81c`
- AI_Skills historical M: `0a7198277dd9575010904f05b642deefffd00009`
- Bridge: `a5c4fe61dc9ab0e228822e854ace5c7e50a4d967`
- Bobbio: `dd977705a2cdfecaa2d4e09127ab4464ae898b32`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `7afb2277cd1001204e77e4987d9fcaa447e7c675`
- Asteria: `b34f6c5d27dd9ac7b1193826ac878fca4a953fb5`
- SeminarArc: `c3fc5a64a3abaec7860808fbcb4082b95d2a0302`
- CUHK Date inspected ref: `711fab75f044b7ad31e5ff8610c076f902ccc949`

Do not reopen already frozen design: v0.2 architecture, repo dispositions, H1–H9, exact task-branch isolation, Bridge scaffold direction, `0.8.3` unreleased candidate direction, or `057 -> implementation review -> integration -> bounded 056 source-drift revalidation`.

## Stable implementation findings to verify

Check that the repair prompt closes exactly these findings without adding unrelated scope:

### C057-I1-BRIDGE-H8-BYTE-PRESERVATION

Must require exact project-owned content preservation outside managed marker span for existing roots under normal / `--force` / repeated init. `rstrip()` / `lstrip()` normalization must be removed from that semantic boundary. Real CLI behavior and irregular-whitespace fixtures are required.

### C057-I2-BRIDGE-VERSION-CLOSURE

Must keep repair in unreleased `0.8.3`, synchronize README/package/changelog identity, and add the two missing Lite boundaries:

- docs/TODO/test-only non-user-consumable changes normally do not bump;
- intermediate implementation commits may remain unreleased until the next actual candidate/release.

Must retain repo-local-policy precedence, prerelease opt-in, no formal-version reuse across different user-consumable candidates, and no root-template duplication. H7 must prove generated Lite consumes the complete fallback, not just a keyword.

### C057-I3-MICA-CONSOLIDATION-NOT-DONE

Must actually remove overlap among development budget / tiers / focused-before-full-E2E sections and produce one testing ladder while preserving all Mica-specific diagnostics/account/hot-path/manual-real-site safety boundaries. No runtime/version change.

### C057-I4-ASTERIA-MAP-CONVERSION-PARTIAL

Must move remaining root Dev Server mechanics to the existing single runtime owner, shrink Browser root section to locator + inline-contract hard requirement where applicable + `可以自动操作页面；不能绕过页面`, preserve GPT Work-before-human and visual/scientific locators, and leave `prompts/AGENT_RULES.md` untouched.

### C057-I5-SEMINARARC-MAP-CONVERSION-NOT-DONE

Must move detailed environment/inventory/mixed-device/command/incident/harness mechanics into existing `docs/DEVICE_TESTING.md`, while root retains the six explicit high-risk safety summary items plus project skills/product/dogfood/Compose invariants. No third manual.

### Bobbio approved consolidation

Must preserve the already-correct three-way visual authority closure while finally consolidating duplicated general GUI/human/pre-user/anti-blocking mechanics, using existing deeper owners where appropriate. No product/Figma/runtime/schema/version change.

### Lucerna / CUHK Date

Must not expand scope: Lucerna remains light; CUHK Date remains inspect-only.

## Final-candidate closure

Verify the prompt requires:

- old E/M and old repo candidates remain immutable failed history;
- repair uses existing `reviewed/057_repo_agents_hygiene` branches/worktrees only;
- new semantic candidate commits are produced on those branches;
- `git diff --check` on all final candidates;
- affected H1–H9 rerun with H5 qualitative and H7/H8 real normal-entry behavior;
- stable Bridge full regression once;
- new evidence commit `E2`;
- new manifest-only closure commit `M2` binding exact final tuple;
- no self-reference in `M2`;
- stop at independent implementation-review handoff, no integration/release/056.

## Complexity check

Actively reject if the repair prompt introduces any of:

- successor/new task branch names;
- H10/new gate;
- ledger/schema/state/controller/watcher;
- migration engine;
- paid API;
- product/runtime work;
- 056 work;
- main/develop merge or formal Bridge release.

Also reject if the prompt is too weak and permits heading-only cleanup, grep-only H7/H8, line-count-only H5, or mutation of old E/M.

## Output

If the repair prompt is not execution-safe:

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_REPAIR_PROMPT_2026-09-17.md
REPAIR_PROMPT = REVISE
READY_FOR_CODEX_REPAIR = NO
NEXT_HANDOFF = PLANNER
```

Give stable blocker IDs and, per Critic contract, a complete Planner revision prompt.

If it is ready:

First explain in normal Chinese why this is an implementation repair rather than an architecture redesign, and how the prompt closes I1–I5 plus Bobbio consolidation without expanding scope.

Then give:

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_REPAIR_PROMPT_2026-09-17.md
REPAIR_PROMPT = PASS
READY_FOR_CODEX_REPAIR = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_REPAIR_PROMPT
```

Finally return the exact reviewed repair prompt verbatim:

```text
=== APPROVED 057 REPAIR PROMPT BEGIN ===
<verbatim file content>
=== APPROVED 057 REPAIR PROMPT END ===
```

Do not write a newer "improved" prompt after PASS.
