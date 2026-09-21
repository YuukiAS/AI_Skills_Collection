# Workflow Identity & Capability Gate Lifecycle — Critic Review v2.1

- Date: 2026-09-20
- Review role: independent Critic
- Review stage: DESIGN_PROPOSAL_R3
- Reviewed proposal: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md`
- Reviewed proposal version: `v2.1`
- Reviewed proposal commit: `ba2fc85f9c58b9b332eb07f821d1756b417fe1d1`
- Proposal blob SHA at reviewed commit/current main: `36f58a1c5f21dd4f430310701b456741c8bd9e7a`
- AI_Skills current main checked: `554073f5c2560948ddd7bb7e1232bdda04d3550b`
- Bridge Kit current main checked: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **PASS**
- Complexity verdict: **APPROPRIATE**
- Scope: design review only; no implementation / production / paid / branch authorization

## 1. Closure

The v2.1 clarification closes `C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL` without reopening the three already-closed technical blockers.

The design now separates two layers cleanly:

1. **technical task_key** — stable machine locator for Reviewed Handoff task/result directories, task branch, CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT locators, and text/visual review identity;
2. **human-readable short label** — ordinary wording used in Planner/Critic/Codex headings, Goal titles, review/report headings, handoffs and normal discussion.

The short label is a writing convention, not a second identity system. The proposal explicitly rejects a `display_name` schema field, title registry/service, database/ledger, or Bridge human-label parser.

For a frozen single-plugin release, the human label can simply be `Clear Writing 0.4` or `Presentations 0.3`. Before the version is frozen, the label stays outcome-oriented, for example `Clear Writing 发布收口` or `Presentations 视觉质量完善`.

For current 056-like broad work, the technical identity can be `cross-repo--product-delivery-discipline`, while normal user-facing language uses `开发交付流程完善（AI_Skills + Bridge）`. Historical 056 is not renamed; `开发交付流程完善（原 056）` is only a transition locator.

The proposal also correctly limits the naming convention to workflow-controlled text. It does not claim control over ChatGPT/Codex client-generated sidebar/conversation titles.

## 2. C-WIGL-04 review

### C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL — CLOSED

The minimum closure requirements are all present in §5.8:

- technical task_key is explicitly a machine locator, not the ordinary user-facing work name;
- human-readable short labels are the default for controlled prompts/Goals/reviews/reports/chat handoffs;
- no new display-name field/schema/registry/title service/mapping system is introduced;
- single-plugin frozen releases can use display name + version;
- unfrozen work uses a short outcome phrase instead of prematurely freezing a candidate version;
- broad/cross-repo work uses a short outcome label with an optional compact scope hint;
- historical 001–057 are not renamed or migrated;
- version remains optional in technical task identity and is only allowed as semantic disambiguation when the release target is already frozen;
- collisions still fail closed and do not gain UUID/date/sequence suffixes;
- repair/review/integration reuse the same task key;
- platform-generated UI titles are explicitly outside this repo/workflow contract.

No new production hole is introduced by this clarification.

## 3. Small regression check

The v2.1 change does not reopen or weaken the accepted architecture:

- `C-WIGL-01-SCOPE-PRECEDENCE` remains CLOSED;
- `C-WIGL-02-IMPACT-FALLBACK-BOUNDARY` remains CLOSED;
- `C-WIGL-03-IDENTITY-CUTOVER-COVERAGE` remains CLOSED;
- G1–G7 remain unchanged in function;
- 001–057 remain no-migration;
- same-final-candidate remains mandatory;
- stable Gate taxonomy + growing regression bank remains intact;
- Bridge remains lexical/compatibility/propagation owner only;
- AI Skills Maintainer, workflow-core and domain-plugin responsibilities remain separated;
- docs directory reorganization remains deferred;
- no controller/watcher/database/registry/ledger/state machine is added.

Targeted re-read of current 056 still confirms two mutable canonical repos (AI_Skills + Bridge), so its hypothetical new technical class remains `cross-repo`. Current Bridge source still enforces the old numeric grammar in the known validator surfaces and binds text/visual evidence through task-key paths/equality; v2.1 naming clarification does not change any of those already-reviewed implementation requirements.

## 4. Complexity

**APPROPRIATE**

The human-readable naming rule is deliberately kept as prose convention. Turning it into a machine field or second identity model would be unnecessary complexity; omitting it would recreate user-facing cognitive burden. The current separation is the minimum sufficient design.

## 5. Decision

```text
REVIEWED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
REVIEWED_PROPOSAL_VERSION=v2.1
REVIEWED_PROPOSAL_COMMIT=ba2fc85f9c58b9b332eb07f821d1756b417fe1d1
DECISION=PASS
COMPLEXITY=APPROPRIATE
C-WIGL-01=CLOSED
C-WIGL-02=CLOSED
C-WIGL-03=CLOSED
C-WIGL-04=CLOSED
BLOCKERS=NONE
NON_BLOCKING=NONE
READY_FOR_EXECUTION_PLAN=YES
NEXT_HANDOFF=PLANNER
```

## 6. What this PASS does and does not approve

This PASS approves the **v2.1 design** as a basis for Planner execution-package planning.

It does not approve or authorize:

- Codex execution;
- production source changes;
- Bridge release;
- task branch/worktree creation;
- paid API;
- merge/release/deployment;
- historical task renaming;
- client UI title control.

The next step is for Planner to prepare the execution package under the approved design and send that exact package back for execution-ready Critic review.
