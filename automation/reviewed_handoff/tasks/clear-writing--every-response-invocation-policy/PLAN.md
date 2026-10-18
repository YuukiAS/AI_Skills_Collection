---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: clear-writing--every-response-invocation-policy
decision: PLAN_FROZEN
---

# Clear Writing Web Gate execution Plan v0.3

Date: 2026-10-18  
Status: FROZEN_FOR_EXECUTION_READY_REREVIEW

- Repository: `YuukiAS/AI_Skills_Collection`
- Source/evidence branch:
  `reviewed/clear-writing--scientific-explanation-readability-repair`
- Task: `clear-writing--every-response-invocation-policy`
- Approved invocation-policy proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- Proposal Critic PASS:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md@50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- Prior execution package: `35c28d5ee695d20bcfcc37ee919d60545cae34bb`
- Frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- Prior repo/Codex product PASS terminal:
  `fd0ad0603309fae52b3af0f9f7cdd7f31adea4b4`
- Tracking: Issue #13
- Maintenance companion: `ai-skills-core`
- Domain owner: `writing-style`
- Execution protocol owner: `workflow-core`
- Plan revision: `1 / 1`
- CI: `NOT_REQUIRED` for this evidence-only Web Gate task.

## Objective and value

Validate the already-approved invocation-policy v0.2 on real ChatGPT Web
without modifying the already-PASS Clear Writing production candidate.

This v0.3 package closes only five execution-readiness defects:

1. fail closed against Reviewed Handoff watcher/Codex execution before
   execution-ready PASS + user Kickoff;
2. freeze exact test-only Web candidate materialization and post-create parity;
3. prove W2 matched-environment feasibility before any candidate/Project
   mutation or model request;
4. make every frozen execution contract read-only after execution-ready PASS;
5. freeze W2 opaque arm labels and a genuinely blind first-pass review packet.

The invocation-policy itself is unchanged.

## Frozen decisions

### A. Production and architecture remain immutable

The six-skill architecture and production candidate `fd7a1578...` remain
frozen. This task cannot modify any production Skill, routing, Marketplace
payload, profile, Research Authoring, Presentations, PIE or Mica.

If W0 exposes a real production defect, stop and return to Planner -> Critic.
Do not repair it inside the Web Gate.

### B. Project bridge exact bytes

Every Project-policy condition must use exactly these UTF-8 bytes:

```text
对每条面向用户的自然语言最终回答，以及自然语言与机器内容混合的最终回答，如果当前 Clear Writing 可用，则使用其最合适的现有写作能力；纯 JSON、YAML、代码、命令、原始日志、逐字引用或其他要求精确机器输出的请求不为此强制调用 Clear Writing，直接保持精确原样。不要模拟、重建或复制 Clear Writing 内部规则。
```

Record these exact bytes and SHA-256 before live testing. W2 Treatment and
Control must use byte-identical text.

### C. Pre-kickoff watcher fail-closed latch

This task does **not** use Reviewed Handoff watcher/Codex as its Web Gate
execution transport.

The task-local Plan is frozen, but `CURRENT.state` intentionally remains a
non-watcher state, `NEEDS_GPT_PLANNER`, while waiting for execution-ready
Critic re-review and the user's later approved Kickoff.

This uses the existing Bridge state machine; no new state/schema is added.

The task must not return to `PLAN_FROZEN` until all of the following are true:

1. execution-ready Critic PASS exists for this exact v0.3 package;
2. the user sends the exact approved Kickoff;
3. the exact target + branch watcher lifecycle has been inspected;
4. no active watcher/Executor event remains for that exact target + branch;
5. `W2_MATCHED_ENVIRONMENT_PREFLIGHT=PASS`.

Watcher lifecycle inspection/stop follows the current Bridge Kit contract in
`CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_3_2026-10-18.md`.

After those conditions pass, the manual Web execution transport may use the
existing legal Reviewed Handoff transitions
`NEEDS_GPT_PLANNER -> PLAN_FROZEN -> EXECUTING` while the exact branch watcher
is confirmed stopped. No watcher may be started/restarted for that target +
branch during manual Web execution.

If watcher inactivity cannot be proven, no live ChatGPT mutation is allowed.

### D. W2 matched-environment preflight is gate zero

Before:

- Web candidate creation/installation;
- test Project creation/modification;
- Project instruction writes;
- the first model prompt;

run the read-only contract:

`docs/design/clear-writing/CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_3_2026-10-18.md`

It must prove, in the current real ChatGPT surface and authorization envelope:

- same account/workspace boundary;
- same surface/model/visible effort mode;
- byte-identical Project bridge;
- candidate availability/consumption can be the only material arm difference;
- no account/subscription/workspace/role/permission mutation;
- no repeated global plugin install/uninstall;
- no cross-arm history access;
- Project memory is project-only or an explicitly equivalent isolation
  mechanism.

"Same memory mode" is not enough if that mode may expose cross-Project history.

If any required matched condition cannot be proven:

`W2=INCONCLUSIVE`

and the **entire live batch stops before candidate creation, Project creation,
W0, W1, W2 and W3**.

This is the single frozen answer for preflight INCONCLUSIVE. W3 never rescues
it.

### E. Exact Web test candidate materialization

The only candidate setup contract is:

`docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`

Source authority is only:

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

The archive must be deterministically built from the exact six Clear Writing
source Skills and required support files, with source/generated parity,
per-file SHA-256 and archive SHA-256 recorded before Plugin Creator mutation.

Only after preflight PASS may the executor create **at most one PRIVATE**
Clear Writing test candidate.

After creation, record the returned:

- `plugin_id`;
- `release_id`;
- `current_release_id`;
- `latest_release_id` when exposed;
- version;
- scope;
- discoverability.

Before W0, re-read the actual Web release using Plugin Creator metadata, file
listing/read and complete archive retrieval, and prove byte/source parity with
the frozen package.

If parity or identity cannot be proven, stop before W0. Do not test an
approximate candidate.

Do not update/delete/replace Research Authoring, Project Instructions Editor,
Project Thread Handoff or any other plugin.

If W0/W1/W2 FAIL or W2 becomes INCONCLUSIVE after candidate creation, retain the
single test candidate **unchanged and PRIVATE**. This package does not authorize
uninstall, deletion, update, publication, permission changes or replacement.
Later cleanup requires separate explicit user authorization.

### F. W0 — invocation-policy safety

W0 begins only after preflight and candidate parity PASS.

W0-A tests natural-language/mixed safety across ordinary explanation, complex
scientific explanation, multi-index objects, necessary long answers,
one-turn English override, complete executable prompt/contract, genuine
branching, mixed exact payload and exact identities.

W0-B explicitly selects Clear Writing at plugin level for pure exact-only
stress. Without concrete Skill-load evidence the maximum claim remains:

`PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`

Exact assistant output must equal the frozen target payload exactly.

Any release-critical W0 failure stops W1/W2. The private candidate is retained
unchanged.

### G. W1 — Project-policy behavior reliability

W1 runs only after W0 PASS.

Its only formal claim is:

`PROJECT_POLICY_BEHAVIOR_RELIABILITY`

W1 uses the frozen bridge without manual per-turn `@Clear Writing` and tests
multi-turn exact exemption/recovery, language override/recovery, short/long
behavior, complete executable prompt preservation and sibling route switching.

Invocation/load evidence is recorded only when the surface exposes it. Model
self-report or output style cannot prove loading.

W1 PASS does not prove plugin causality. W1 FAIL stops W2.

### H. W2 — strict matched plugin increment

W2 runs only after W0 and W1 PASS and only under the environment already proven
eligible by gate-zero preflight.

Treatment and Control must remain strictly matched on:

- Project-setting exact bytes;
- account/workspace boundary;
- surface/model/effort;
- Project memory/isolation;
- pre-frozen tasks;
- task-order policy;
- pair-order policy;
- attempt budget;
- rubric/evaluation;
- fresh isolated conversation contexts.

No arm may read the other arm's Project/chat/output history.

The only material difference may be:

`Clear Writing candidate availability / consumption`

Control cannot copy Skill prose, imitate Treatment or receive Treatment-derived
rules.

If strict matching ceases to hold at any point:

`W2=INCONCLUSIVE`

and release stops. W3 is **not run** after W2 INCONCLUSIVE.

A known-confounded fallback is `DIAGNOSTIC_ONLY` and cannot replace W2.

### I. W2 frozen scoring rule

The previously accepted rule is unchanged:

- P01-P07 are reader-facing preference pairs;
- P08 is a multi-turn hard control and is not counted in the preference
  threshold;
- Treatment preferred for contract-relevant reasons on at least 4/7;
- Control preferred on at most 1/7;
- other tasks may tie;
- Treatment has zero hard failures;
- exact/mixed protection does not regress.

Hard failures include factual/semantic drift, changed exact payload, language
override violation, incomplete executable prompt/contract and materially wrong
sibling ownership.

One valid output per task/arm. No quality retry.

### J. W2 genuinely blind first-pass packet

Opaque arm labels and Treatment/Control mapping were frozen before any Web
output in:

`docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`

The Task Bank exposes only the opaque labels, not their arm mapping.

The initial preference Reviewer must be a **fresh independent thread that has
not read the reveal map**. Therefore the execution-ready Critic that reviews
this package/reveal map is ineligible to serve later as the W2 blind preference
Reviewer.

The initial blind packet may contain only:

- exact task id;
- exact prompt;
- opaque output label 1 + raw output;
- opaque output label 2 + raw output;
- frozen preference/hard-failure rubric.

It must omit:

- execution order;
- timestamps;
- Treatment/Control Project names;
- plugin/candidate identity;
- invocation/load evidence;
- account/workspace locator;
- any metadata that permits inference from pair order.

Per-task verdict and reason must be fully frozen before the Reviewer is allowed
to read the reveal map or process/identity metadata.

Only after reveal may the causal summary be formed.

### K. W3 — diagnostic only

W3 uses no Project bridge and no manual Clear Writing invocation.

Frozen reachability:

- W2 PASS -> W3 may run;
- W2 FAIL -> W3 may run for diagnostic value;
- W2 INCONCLUSIVE -> W3 is not run.

W3 is non-release-critical and can never rescue W2.

### L. Fresh G7 reservation only

G7 is not executable under this package.

Only after W0/W1/W2 release-critical PASS may Planner create a separate frozen
G7 package. That future package must bind production candidate, actual Web
candidate/release identity, Project bridge bytes, surface/model, Project memory,
conversation isolation, attempt budget, fresh task set, task order,
W0/W1/W2 rubric, Reviewer input and stop condition.

KR-WEB-01..09, prior controls, W0/W1/W2/W3, preflight diagnostics and every
debug/recovery sample seen before G7 freeze are permanently excluded.

## Positive completion

A successful Web Gate path requires:

1. watcher fail-closed preconditions PASS;
2. `W2_MATCHED_ENVIRONMENT_PREFLIGHT=PASS`;
3. exact PRIVATE candidate materialization + post-create parity PASS;
4. W0 PASS;
5. W1 `PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS`;
6. W2 strict matched plugin increment PASS;
7. W3 diagnostic recorded;
8. complete raw evidence and attempt records;
9. independent final review of actual Web evidence.

Success only permits Planner to prepare a later G7 freeze. It does not authorize
real Project rollout, release or production changes.

An INCONCLUSIVE path is also a truthful terminal product-evaluation outcome for
this batch; it does not become PASS.

## Non-substitutable semantics

- Pure exact-only output is an activation exemption.
- W1 reliability is not plugin causality.
- W2 must be strictly matched or INCONCLUSIVE.
- Default/cross-Project memory is not acceptable isolation.
- Model self-report never proves plugin/Skill consumption.
- The Web candidate must be byte/source-bound to `fd7a1578...`.
- No second/replacement candidate may be created under this package.
- Failure does not authorize candidate cleanup/mutation.
- The W2 first-pass Reviewer must remain blind to arm identity and order metadata.
- Poor model output is evidence and cannot be rerun to win.
- Frozen contracts cannot be edited during execution.
- No Gate claim may exceed actual evidence.

## Implementation / execution scope

After execution-ready PASS, the following are **read-only** for the entire
execution:

- approved proposal v0.2 and its Critic review;
- `REQUEST.md`;
- this `PLAN.md`;
- Canonical Goal v0.3;
- Kickoff v0.3;
- Project bridge bytes;
- Task Bank v0.3;
- W2 matched-environment preflight contract;
- Web test candidate materialization contract;
- W2 reveal map;
- pair/task order;
- attempt budget;
- rubric;
- scoring thresholds;
- stop/recovery conditions.

Execution may write only:

- `results/clear-writing--every-response-invocation-policy/**`;
- existing Reviewed Handoff executor-owned `CURRENT` fields through legal
  transitions;
- necessary Issue #13 tracking copy.

No execution write is allowed under `docs/goals/`,
`docs/operations/prompts/`, `docs/design/clear-writing/`, `skills/`,
`plugins/`, profiles, Marketplace source or other production areas.

If a frozen contract needs to change:

**stop -> Planner -> independent Critic**.

Do not edit in place and continue.

## Account / Project / plugin authorization boundary

This planning/revision turn authorizes **zero live ChatGPT mutation**.

Only after execution-ready Critic PASS and the user sends the exact approved
Kickoff may the manual Web execution thread begin the read-only watcher/W2
preflight.

After preflight PASS, the reviewed live envelope allows only:

- creation of at most one PRIVATE Clear Writing test candidate from the frozen
  deterministic archive;
- read-back verification of that candidate's exact release;
- disposable empty test Projects/chats;
- frozen bridge bytes in those disposable Projects;
- the matched Project-only/equivalent memory isolation proven at preflight;
- the per-gate model requests in the frozen Task Bank;
- public-safe evidence preservation.

Not authorized:

- real AI Research Stack Project setting edits;
- global custom-instruction edits;
- other plugin create/update/delete/uninstall;
- Clear Writing replacement candidate;
- Clear Writing permission changes;
- repeated global plugin install/uninstall;
- account/workspace/subscription/role/permission changes;
- deleting/overwriting user chats/files;
- public/unlisted release;
- G7;
- PIE/Mica/Research Authoring/Presentations.

Any operation outside this envelope requires stop and new explicit review/user
authorization.

## Evidence preservation

Frozen public-safe inputs:

`docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_3_2026-10-18.md`

Execution evidence root:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.3/`

Required evidence:

- `preflight/W2_MATCHED_ENVIRONMENT_PREFLIGHT.md`
- `FREEZE_MANIFEST.json`
- `PROJECT_BRIDGE.txt`
- candidate archive/file manifest + post-create release parity record
- W0 full prompts/raw outputs/run manifests/verdicts
- W1 full turn-by-turn outputs/run manifest/verdicts
- W2 arm-separated raw execution evidence
- W2 sanitized blind packet
- W2 blind Reviewer verdict/reasons
- reveal record + causal summary
- W3 evidence when reachable
- attempt/retry log
- `FINAL_REVIEW_INPUT_MANIFEST.md`
- `RESULT.md`

Each model run records gate/task/turn, timestamp, surface/model, Project memory
mode, bridge hash, production candidate, actual Web plugin/release identity,
opaque conversation isolation id, attempt number, prompt SHA, response SHA,
load evidence when exposed and exact comparison when applicable.

The **blind packet** deliberately strips timing/order/identity metadata before
being given to the W2 preference Reviewer.

Do not store account IDs, credentials, private chat URLs or unrelated Project
content. Account/private UI screenshots go only to
`private/exports/clear-writing--every-response-invocation-policy/`; public
evidence contains sanitized description/hash only.

## Attempt / retry policy

Default: exactly one valid model answer per frozen task/turn/arm.

One infrastructure-only retry is permitted only when the original attempt
produced no usable model answer due to transport/service interruption. Preserve
the failed attempt and reason.

A bad, ugly, wrong, incomplete or plugin-failing answer is a real result and
cannot be retried.

## Stop / recovery

Stop immediately and return to Planner when:

- watcher inactivity cannot be proven;
- W2 preflight is INCONCLUSIVE;
- exact candidate package/release parity fails;
- unexpected plugin scope/discoverability/identity appears;
- W0 release-critical safety fails;
- W1 behavior reliability fails;
- W2 strict matching ceases to hold;
- cross-arm memory contamination is possible;
- a requested operation exceeds the account/Project/plugin envelope;
- surface/model/candidate identity changes mid-batch;
- frozen rubric/contract would need modification after outputs are seen.

No successor is created automatically.

If a failure occurs after the private test candidate exists, retain it unchanged
and private.

After infrastructure-only interruption, resume from the first unanswered frozen
task only when every frozen identity and matched condition remains unchanged.
Otherwise invalidate the partial batch and return to Planner.

## Acceptance and regression gates

| Gate | Required result | Effect |
|---|---|---|
| Preflight | strict matched environment PASS | blocker before all live mutation |
| Candidate | deterministic source/archive/Web-release parity PASS | blocker before W0 |
| W0 | natural/mixed safety + explicit-selection exact stress PASS | blocker |
| W1 | `PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS` | blocker |
| W2 | strict matched plugin increment PASS | blocker; INCONCLUSIVE stops |
| W3 | diagnostic only after W2 PASS/FAIL | non-blocking |
| G7 | separate later frozen batch | forbidden here |

Existing KR-WEB-01..09 and historical controls remain known evidence only.

## Final independent review input

The final product Reviewer receives:

1. this frozen Plan, Goal and approved Kickoff;
2. approved proposal v0.2 and proposal Critic PASS;
3. preflight evidence;
4. candidate source/archive/Web-release parity evidence;
5. freeze manifest and bridge bytes/hash;
6. W0 full raw outputs/exact comparisons;
7. W1 full multi-turn outputs;
8. W2 raw arm evidence;
9. the **already-frozen blind Reviewer judgments**;
10. reveal map/reveal record and causal summary;
11. W3 diagnostic evidence when reachable;
12. attempts/retries;
13. executor `RESULT.md`.

The W2 initial preference review must be performed earlier by a fresh blind
Reviewer that has not read the reveal map. The execution-ready Critic that
reviews this package cannot serve as that blind Reviewer.

The final causal Reviewer separately judges:

- PROCESS / IDENTITY;
- candidate parity;
- W0 PRODUCT SAFETY;
- W1 PROJECT_POLICY_BEHAVIOR_RELIABILITY;
- W2 PLUGIN_INCREMENT PASS / FAIL / INCONCLUSIVE;
- W3 diagnostic, if reachable.

No Reviewer may convert W1 into plugin causality, rescue confounded W2 or
authorize G7 unless W0/W1/W2 meet the frozen release-critical criteria.

## Natural-language usage / routing expectations

If later Gates succeed, normal Project behavior is intended to be:

- ordinary and mixed reader-facing responses use the Project-level Clear
  Writing policy;
- pure exact-only requests remain activation exemptions;
- the user does not manually invoke Clear Writing every normal turn;
- sibling writing responsibilities remain appropriate.

This Plan does not claim those behaviors are already verified.

## Out of scope

Production edits, real Project rollout, global account/plugin mutation, candidate
cleanup, paid external model review, G7 execution, user acceptance,
release/version bump, PIE, Mica, Research Authoring, Presentations and any new
skill/router/state machine/finalizer remain out of scope.
