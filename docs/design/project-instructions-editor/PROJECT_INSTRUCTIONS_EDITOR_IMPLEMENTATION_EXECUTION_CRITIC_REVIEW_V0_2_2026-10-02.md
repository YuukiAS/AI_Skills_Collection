# Project Instructions Editor — Implementation Execution Critic Review v0.2

Date: 2026-10-02  
Result: `PASS`  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch/ref: `main`  
Main observed before this review: `06d6bd79ddb32c32410b58a521829f74e155db14`  
Review stage: execution-ready implementation package v0.2 review  
Tracking: `#93`

Reviewed same-version package:

- Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`
- Goal: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md`
- Kickoff: `docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md`
- Package commit: `bc191c2875ced0a2a551258bddeeb2d819161f25`

Package blobs on current main remain identical to the reviewed package:

- Plan blob: `b77b1057e865e2a71966a315fc532b3214a01872`
- Goal blob: `2c1c9b9d7c09a6d3900b2a47c39c7369ae4b33cb`
- Kickoff blob: `f539dbe5c39585d423bb22f82b592790d411b4c2`

Prior execution review:

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-02.md`
- prior result: `REVISE`
- blockers: `E1`, `E2`

Approved product/design authority remains unchanged:

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md`
- design-freeze Critic PASS commit: `bf9add585924e93ab8844bb59a366f1cd4f837d6`

```text
CRITIC_RESULT=PASS
E1=CLOSED
E2=CLOSED
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

## 1. Conclusion

v0.2 closes both remaining execution-contract blockers without reopening or weakening the frozen product architecture.

The package is now execution-ready.

The implementation task is bounded to the exact standalone Skill source, tests, generated identity, release-candidate metadata, public-safe Gate evidence, task-local install/smoke, portable package, exact task branch/worktree, ordinary commits, and ordinary non-force push.

The Executor still does not own final product acceptance, main integration, or formal release.

## 2. E1 closure — G4 ownership and stop point

`E1=CLOSED`.

Plan, Goal, and Kickoff now agree on one owner model:

Executor owns:

- final candidate implementation;
- G1 PASS;
- G2 PASS;
- G3 PASS;
- complete representative G4 input/source/output packet from the exact final candidate;
- non-independent self-check only.

Executor maximum G4 claim is:

```text
G4_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor may then stop at:

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor is explicitly forbidden from claiming:

```text
G4=PASS
IMPLEMENTATION_OVERALL=PASS
```

The independent Reviewer owns:

- full final Skill source review;
- exact candidate/package identity review;
- G1–G3 evidence review;
- the full G4 representative packet and complete user artifact;
- candidate immutability proof;
- `G4=PASS|REVISE`;
- `IMPLEMENTATION_OVERALL=PASS|REVISE`.

The file split is also unambiguous:

- Executor: `G4_COMPLETE_TASK_PACKET.md`
- Reviewer: `G4_COMPLETE_TASK_REVIEW.md`

The four-Gate taxonomy remains unchanged; no G5 is introduced.

## 3. E2 closure — exact final candidate identity

`E2=CLOSED`.

v0.2 now freezes a non-circular sequence:

```text
finish candidate-owned content
-> deterministic preflight/tests
-> FINAL_CANDIDATE_COMMIT=C
-> install from C
-> G1 on C
-> G2 on C
-> G3 on C
-> G4 full packet from C
-> portable zip from C
-> evidence-only commit(s)
-> EVIDENCE_HEAD=E
-> prove C..E has no candidate-owned changes
-> independent Reviewer
```

Candidate-owned content is frozen before `C`, including:

- Skill runtime source/reference/evals/assets;
- focused test and standalone baseline declarations;
- generated registry/catalog/provenance/runtime identity;
- README/VERSION/CHANGELOG release-candidate metadata;
- current repository parity content.

After `C`, tracked mutation is restricted to:

`results/project-instructions-editor--standalone-skill-implementation/**`

for Gate evidence, result, manifest, handoff, and later Reviewer evidence/result.

The handoff must expose both:

```text
FINAL_CANDIDATE_COMMIT=C
EVIDENCE_HEAD=E
```

and retain a directly inspectable `git diff --name-status C..E` or equivalent proof.

Any candidate-owned mutation after `C` invalidates stale related Gate evidence, requires a new candidate commit, and requires blast-radius-matched rerun. Cross-candidate PASS stitching is explicitly forbidden.

The portable zip is also bound to exact `C` and must record candidate commit, SHA-256, archive file list, runtime-tree identity/hash, and generation method.

This is sufficient to prove that runtime, Gate evidence, package, and review all refer to the same candidate.

## 4. Regression check on previously accepted package decisions

No v0.2 regression was found in the parts already accepted by the v0.1 Critic.

Still valid:

- source path: `skills/core/codex-system/project-instructions-editor/`;
- standalone version: `0.1`;
- `requires_network=false`;
- `writes_files=false`;
- `executes_code=false`;
- `recommended_scope=global`;
- natural implicit normal entry;
- frozen near-miss owners;
- preservation-sensitive / greenfield / explicit reset;
- protected absence;
- bounded edit default;
- semantic ownership vs effective enforcement;
- locator lookup-before-action boundary;
- no-op;
- proportional user delivery;
- G1/G2/G3/G4 capability taxonomy;
- public-safe evidence policy;
- no Plugin wrapper;
- no paid API/model review;
- no private Project-data external transmission;
- no main merge/release/tag/publish during Executor stage.

## 5. Version decision

Current main still reports:

```text
VERSION=5.4.0
```

The previously accepted version decision remains valid:

```text
Repository bump decision: MINOR
candidate if origin/main remains 5.4.0: 5.5.0
project-instructions-editor standalone: 0.1
all central plugins: NO_BUMP
```

The current version policy permits a repository MINOR only for a genuinely new repository-level user capability. This new installable standalone Project-instruction editing capability satisfies that rule, consistent with the prior Project Thread Handoff standalone-Skill release precedent.

If kickoff-time `origin/main:VERSION` has drifted, the Executor must stop the version/release metadata portion with `VERSION_DRIFT` and return to Planner rather than invent a new target.

## 6. OpenAI Skills surface check

Targeted current official OpenAI documentation was independently rechecked.

Current official sources still support the package boundary:

- Skills are reusable instruction/resource directories centered on `SKILL.md`;
- skill discovery uses the skill name and description;
- ChatGPT Skills are available to eligible Business, Enterprise, Healthcare, and Edu users subject to workspace/product availability;
- Skills can also be supported in Codex and other OpenAI products, with installation/sync varying by product and surface.

Therefore the package remains correct to require v0.1 normal-entry production evidence through AI_Skills/Codex standalone install + fresh normal Codex session, while not claiming that the current Pro regular Chat can necessarily install/auto-use the standalone Skill.

No ChatGPT Plugin wrapper or live account mutation is required.

## 7. Authorization and stop boundary

The approved Kickoff is appropriately bounded.

Authorized only after the user actually sends the approved Kickoff:

- exact branch/worktree;
- frozen source/docs/tests/generated/release-candidate/results edits;
- deterministic tests;
- task-local standalone install/fresh Codex smoke;
- public-safe regression;
- portable zip;
- task-owned commits;
- ordinary non-force push exact branch.

Not authorized:

- main merge;
- release ref/tag/GitHub Release;
- paid API/model reviewer;
- private Project-data external transmission;
- live ChatGPT account mutation;
- central Plugin source changes;
- Bridge Kit changes;
- force push / remote remap / destructive Git;
- watcher/daemon/database/ledger/state machine.

The Executor can only claim:

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

after all candidate/evidence identity conditions are satisfied.

## 8. Maintenance state

Current tracking remains valid:

- Issue #93: open;
- labels: `maintenance-track`, `kind:new-capability`, `scope:standalone-skill`, `area:standalone-skill`;
- canonical source retains `tracking: #93`.

Current surface still has no verifiable Clear Writing invocation, so this review does not mutate the reader-facing Issue copy:

```text
CLEAR_WRITING_UNAVAILABLE
```

Current surface also has no GitHub Project field mutation surface.

Exact pending Project mutation remains:

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
```

Do not ask the user to maintain the Project card manually.

## 9. PASS boundary

This execution-ready PASS authorizes only the reviewed v0.2 implementation package after the user sends the exact approved Kickoff.

It does not authorize:

- a different branch/worktree;
- main merge;
- formal release or publication;
- paid review;
- private Project-data export;
- live ChatGPT account changes;
- central Plugin changes;
- Bridge Kit changes;
- scope expansion.

Implementation still requires independent review before any overall PASS or integration/release closure.

```text
CRITIC_RESULT=PASS
E1=CLOSED
E2=CLOSED
APPROVED_PLAN_PATH=docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
APPROVED_GOAL_PATH=docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md
APPROVED_PACKAGE_COMMIT=bc191c2875ced0a2a551258bddeeb2d819161f25
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```
