# Project Instructions Editor C9 final Gate Critic review

Date: 2026-10-06
Result: `REVISE`

## Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=standalone Skill / project-instructions-editor
design_topic_or_task_key=project-instructions-editor--standalone-skill-implementation
source_branch_or_ref=work/project-instructions-editor--standalone-skill-implementation
review_stage=C9 final-candidate campaign failure adjudication
FINAL_CANDIDATE_COMMIT=C9=648bca42759210b63f4bb394c265c508ebfe038f
FRESH_G4_FREEZE_COMMIT=F9=fbd68ed2d87f73babedf5c5687f704cb1d4c3e3a
FAILURE_EVIDENCE_HEAD=6a2950d119360912838ce29ccc7ad3025cd8c82b
```

Reviewed directly:

- latest main Planner/Critic contracts, Capability Gate policy, maintenance-board policy and AGENTS;
- exact C9 `SKILL.md` and `references/editor-contract.md`;
- exact C9 final failure evidence and F9 fresh-case freeze packet;
- C9 -> failure-head Git diff;
- frozen design/implementation documents governing adjacent writing helpers;
- current `chinese-prose` and `writing-fidelity` source;
- current official OpenAI Projects/Skills documentation relevant to Project instructions and multi-Skill use.

## Adjudication

The Executor stopped correctly.

C9 is a failed final candidate. It must not be modified and continue under the same candidate identity.

The first required qualitative failure is the known Server+VPS R7 structural replay. The durable replacement contains ordinary non-exact English:

- `生产 tunnel`;
- `网络/tunnel`;
- `tunnel 生命周期`.

The same output then claims ordinary descriptive English has been naturalized. The failure therefore reproduces the already-defined R7 artifact/self-check mismatch exactly.

The failure is not explained by an OpenAI product constraint. Project instructions remain Project-specific instructions, and current Skills behavior allows reusable skills to be used when helpful. No platform requirement makes the generic word `tunnel` an exact identifier in these sentences.

## What C9 did prove

The C9 package and execution discipline worked as intended:

- exact C9 was frozen;
- F9 froze the final fresh case/rubric before first fresh output;
- C9 -> F9/failure-head mutations are results-only;
- candidate-owned content was not changed after final campaign start;
- no substitute fresh case was selected;
- E9/S9 were not fabricated after the Gate failed.

Therefore the failure is product/runtime evidence, not a Gate-process defect.

The final fresh case was also subsequently observed by the runner. Because C9 must now change, that exact F9 case is no longer fresh for any successor candidate. It may be retained only as development/regression evidence.

## Stable blocker

```text
C9-B2=PROMPT_ONLY_R7_ENFORCEMENT_NOT_RELIABLE
```

Status: `BLOCKING`

### Requirement

The existing project rules require repeated failure of an already-written rule to be repaired at the actual consumer/execution mechanism rather than by adding synonymous instructions.

The frozen PIE design also explicitly allows:

- PIE to remain the semantic-placement owner;
- `chinese-prose` to act after semantic/placement freeze as the Chinese realization/final-readability helper;
- `writing-fidelity` to act as a preservation guardrail.

The implementation plan additionally says that if the frozen capability cannot be satisfied by the assumed instruction/reference-only implementation, the task must return to Planner/Critic rather than silently adding an unreviewed runtime mechanism.

### Direct evidence

R7 has now survived multiple increasingly explicit prompt-layer repairs:

- C7: ordinary English could be preserved under vague “product/context value” reasoning;
- C8: `Project setting` leaked through a different complete-replacement path;
- C9: after introducing one mandatory final replacement pass over every complete-replacement path, `tunnel` still leaked while the self-check claimed naturalization succeeded.

C9 therefore falsifies the working assumption that another stronger wording of the same PIE self-check is sufficient.

Current main already has a specialized mature helper whose explicit responsibility is Chinese final readability and removal of unnecessary English: `chinese-prose`. The frozen PIE architecture explicitly permits using it after PIE semantic/placement decisions are fixed.

### Causal risk

Continuing with another prompt-only reinforcement creates a predictable loop:

```text
add stronger self-check wording
-> one regression passes
-> another ordinary technical English token leaks under output variance
-> self-check still reports success
-> new candidate / new final campaign
```

That is exactly the repeated real failure sequence C7 -> C8 -> C9.

More examples, synonym rules, token lists, or stronger “inspect every token” wording would not constitute a new mechanism and would risk converging toward a disguised blacklist.

### Minimum closure

Return to Planner for a bounded implementation-mechanism recovery, not a product redesign.

Planner must compare at least:

1. **Reuse the existing writing stack**: PIE remains semantic/placement owner; after the complete replacement's semantic decisions and exact identities are fixed, invoke `chinese-prose` as the Chinese realization/final-readability helper; then re-check PIE semantic invariants. Use `writing-fidelity` as needed to protect exact identities, permissions, evidence strength, privacy, deletion history and other non-negotiable semantics.
2. **Continue PIE-only prompt enforcement**: explain what genuinely new mechanism would make it different from C7/C8/C9. Merely adding stronger wording/examples is not sufficient.
3. Any other mature existing implementation that directly addresses the same final-realization failure without introducing a blacklist, translation dictionary, English-ratio scorer, database, watcher, or new control plane.

The Planner must determine the smallest normal-entry consumption path and how it is proven at runtime. If `chinese-prose` is selected, the Gate must prove actual helper consumption in the mixed Project-edit + Chinese-finalization route rather than merely showing the helper is installed.

The repair must preserve:

- PIE as semantic owner;
- R5 protected absence;
- R6 no-op eligibility;
- exact/formal identities;
- authorization/privacy/evidence/fail-closed semantics;
- non-Chinese Projects not being forced into Chinese;
- four-Gate taxonomy.

Do not create a fifth Gate.

A successor candidate must be new (C10 or equivalent). C9 known failures and the observed F9 case become development regressions. The successor needs one newly frozen final fresh case after the successor candidate and qualitative rubric are frozen.

## Gate / identity judgment

```text
R5=CLOSED
R6=CLOSED
R7=OPEN

C9_G1=DIAGNOSTIC_ONLY
C9_G2=DIAGNOSTIC_ONLY
C9_G3=DIAGNOSTIC_ONLY
C9_G4=FAIL

C9_FINAL_FRESH_CASE_FUTURE_STATUS=DEVELOPMENT_REGRESSION_ONLY

E9=NOT_FORMED
S9=NOT_FORMED

IMPLEMENTATION_OVERALL=REVISE
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
```

## Maintenance state

Issue #93 remains `DOING`.

This review does not authorize README/VERSION/CHANGELOG changes, main integration, Plugin Creator mutation, Bridge Kit/Host Policy changes, paid review, live ChatGPT mutation, or release.

## Final decision

```text
CRITIC_RESULT=REVISE

BLOCKERS=C9-B2
C9-B2=PROMPT_ONLY_R7_ENFORCEMENT_NOT_RELIABLE

R5=CLOSED
R6=CLOSED
R7=OPEN

FINAL_CANDIDATE_COMMIT=648bca42759210b63f4bb394c265c508ebfe038f
FRESH_G4_FREEZE_COMMIT=fbd68ed2d87f73babedf5c5687f704cb1d4c3e3a
FAILURE_EVIDENCE_HEAD=6a2950d119360912838ce29ccc7ad3025cd8c82b

READY_FOR_CODEX=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

NEXT_HANDOFF=PLANNER
```

This review does not reopen PIE's frozen product responsibilities, edit modes, routing boundaries, wrapper architecture, Gate taxonomy, Bridge Kit, Host Policy, final-delivery design, or FD1. It reopens only the implementation mechanism used to realize the already-frozen R7 Chinese readability requirement.
