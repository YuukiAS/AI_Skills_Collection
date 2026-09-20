# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Implementation Critic Review R2

- Date: 2026-09-21
- Review role: independent Critic
- Review stage: INDEPENDENT_IMPLEMENTATION_REVIEW_R2
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- AI_Skills production candidate: `ce63f50238555849a48256068e6fa0d46e21a97b`
- AI_Skills pushed tip/evidence: `871489ee227dee773c8fff3c161bd5743da739c7`
- Bridge production candidate: `7f2707dd4020951650d561303c82a17e22b27317`
- Bridge pushed tip/evidence: `d09306f180634aa4d4ad4ec3ee46295a8b20945b`
- Prior implementation Critic review: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_CRITIC_REVIEW_R1_2026-09-20.md`
- Prior review commit: `232bb975c21bbc81422a00ca9b5969bc07d75e81`
- Decision: **PASS**
- Complexity: **APPROPRIATE**
- READY_FOR_INTEGRATION_PLANNING: **YES**
- Scope: exact implementation candidate tuple and repo-resident evidence only; no merge/release authorization

## 1. Closure

Both R1 implementation blockers are closed.

### C-WIGL-I1-STANDALONE-VALIDATOR-SHADOWING — CLOSED

Bridge production candidate `7f2707dd...` fixes the actual runtime defect:

- the imported `ai_bridge_kit.task_keys` module is no longer shadowed by a local set;
- the standalone script explicitly imports from the current checkout so direct execution tests the candidate source rather than an unrelated installed package;
- subprocess regression tests now execute the standalone validator normal entry;
- semantic + existing legacy validation passes;
- malformed semantic key fails cleanly without traceback;
- focused suite and full Bridge suite were rerun on the repaired candidate.

This is the minimum correct repair. It does not add another parser, registry, state or validation framework.

Python's documented execution model confirms the original failure mechanism: a binding in a function block makes that name local to the block. The repaired source removes that collision rather than masking it.

### C-WIGL-I2-REPLAY-CAPABILITY-EVIDENCE — CLOSED

The original candidate replay receipts are preserved as provenance and explicitly demoted from acceptance evidence.

The corrected replay scenarios now match the frozen Plan instead of restating the expected answer:

- **Verified Workflow** receives four classification cases: isolated local change, shared normal-entry change, unresolved multi-Gate evidence gap, and maturity promotion.
- **AI Skills Maintainer** receives five classification cases: single plugin, one-repo multi-plugin, AI_Skills + Bridge mutable with product repos read-only, existing-capability regression, and genuinely new capability.

For both scenarios the repository now preserves:

- frozen input/task hashes;
- exact candidate identity;
- candidate-consumption receipt;
- substantive model output;
- compact verdict.

The substantive outputs satisfy the frozen G3/G5/G6 expectations:

- isolated change can be narrow only when impact is explainably bounded;
- shared normal-entry/runtime changes require broad/full;
- unresolved Gate evidence cannot be stitched from old candidates;
- one successful replay is not enough for maturity promotion;
- scope precedence is correctly classified;
- existing capability regression stays in the existing Gate/regression bank;
- genuinely new capability is a Gate redesign consideration;
- domain plugins retain professional-quality ownership.

No third scenario, adaptive input replacement, Terra/OpenAI Responses paid review, or private-data replay was introduced.

Anthropic's current eval guidance reinforces the evidence standard used here: an eval includes task input, agent response/trace and grading logic, and transcript inspection is important for checking that the eval measures the intended behavior. The corrected repo-resident substantive outputs now provide the missing behavior surface rather than relying only on a loading receipt.

## 2. Final candidate tuple review

The implementation candidate tuple accepted by this review is:

```text
AI_SKILLS_PRODUCTION_CANDIDATE=ce63f50238555849a48256068e6fa0d46e21a97b
BRIDGE_PRODUCTION_CANDIDATE=7f2707dd4020951650d561303c82a17e22b27317
AI_SKILLS_EVIDENCE_BRANCH_TIP=871489ee227dee773c8fff3c161bd5743da739c7
BRIDGE_EVIDENCE_BRANCH_TIP=d09306f180634aa4d4ad4ec3ee46295a8b20945b
```

AI_Skills production source did not change during R1 repair; only evidence was corrected, so `ce63f502...` remains the AI production candidate.

Bridge production source changed for the validator fix, so `7f2707dd...` replaces `2a842371...` as the Bridge production candidate.

The evidence-only commits are correctly separate from production candidate identity.

## 3. Regression / scope check

No new implementation evidence reopens the approved architecture:

- semantic new task creation remains canonical;
- legacy numbered tasks remain validation-compatible;
- task identity propagation remains intact;
- stable Gate taxonomy + growing regression bank remains intact;
- same-final-candidate remains intact;
- `BROAD_FULL_FALLBACK` remains appropriate for this cross-cutting release;
- no display-name schema/title service was added;
- no controller/watcher/database/registry/ledger/state machine was added;
- domain plugin professional judgment was not absorbed by workflow-core or AI Skills Maintainer;
- no 001–057 migration occurred;
- no 056 source was modified.

The previously observed duplicate-approval incident is a separate workflow regression case, not a blocker for this candidate. It has been recorded in the existing `workflow-core` TODO under the current Human Gate / delivery-discipline candidate rather than creating a duplicate policy or a new Gate.

## 4. Main-drift / integration boundary

This PASS is **not** a merge/release PASS.

AI_Skills `main` has advanced since the task branch baseline through review/readme-planning/TODO documentation, including the newly recorded duplicate-approval regression. Bridge `main` remains at the pre-candidate baseline.

Before integration, Planner must therefore prepare a bounded integration/release package that:

1. re-reads current AI_Skills and Bridge main;
2. proves no relevant production/version slot has been consumed;
3. chooses the exact non-destructive integration method for both candidate branches without rewriting candidate history;
4. preserves the current main-only docs/TODO work;
5. verifies post-integration source/generated/version/changelog consistency;
6. defines the final install/release smoke required by the existing release contract;
7. obtains explicit user authorization for merge/release actions.

The historical 056 / **开发交付流程完善（原 056）** must not start before this integration/release closure. After these candidates are integrated, 056 must revalidate its source and version slots because workflow-core, ai-skills-core, AI_Skills repository and Bridge candidate versions will have moved.

## 5. Decision

```text
DECISION=PASS
COMPLEXITY=APPROPRIATE
C-WIGL-I1-STANDALONE-VALIDATOR-SHADOWING=CLOSED
C-WIGL-I2-REPLAY-CAPABILITY-EVIDENCE=CLOSED
AI_SKILLS_APPROVED_PRODUCTION_CANDIDATE=ce63f50238555849a48256068e6fa0d46e21a97b
AI_SKILLS_APPROVED_BRANCH_TIP=871489ee227dee773c8fff3c161bd5743da739c7
BRIDGE_APPROVED_PRODUCTION_CANDIDATE=7f2707dd4020951650d561303c82a17e22b27317
BRIDGE_APPROVED_BRANCH_TIP=d09306f180634aa4d4ad4ec3ee46295a8b20945b
READY_FOR_INTEGRATION_PLANNING=YES
READY_FOR_MAIN_MERGE=NO
READY_FOR_RELEASE=NO
START_056_NOW=NO
NEXT_HANDOFF=PLANNER
```

This PASS proves the reviewed implementation candidate and its required evidence are acceptable for integration planning. It does not authorize merge to main, tag/release/publish/deploy, real Host mutation, paid review, or execution of 056.
