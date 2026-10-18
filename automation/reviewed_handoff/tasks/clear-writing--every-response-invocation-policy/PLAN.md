---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: clear-writing--every-response-invocation-policy
decision: PLAN_FROZEN
---

# Clear Writing Web Gate execution Plan v0.2

Date: 2026-10-18
Status: FROZEN_FOR_EXECUTION_READY_CRITIC_REVIEW

Authority:
- proposal: `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- proposal Critic PASS: `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md@50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- frozen production candidate: `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- prior repo/Codex product PASS terminal: `fd0ad0603309fae52b3af0f9f7cdd7f31adea4b4`
- tracking: Issue #13
- maintenance companion: `ai-skills-core`
- domain owner: `writing-style`
- execution protocol owner: `workflow-core`

## Objective and value

Validate the approved invocation policy on real ChatGPT Web without modifying the already-PASS production candidate.

The product claim under test is intentionally narrow:

- natural-language and mixed final responses in a participating Project follow the Project-level Clear Writing policy;
- pure exact-only machine/verbatim requests are activation exemptions;
- W1 proves Project-policy behavior reliability, not plugin causality;
- W2 is the only release-critical matched gate for plugin incremental value unless the surface itself exposes stronger direct load evidence;
- W3 is diagnostic only.

A Project instruction, a model self-report or an attractive answer cannot substitute for the frozen Web evidence.

## Frozen decisions

### Production and architecture

The six-skill Clear Writing architecture and candidate `fd7a1578...` are frozen. This task cannot edit any production skill, routing, Marketplace/profile payload, Research Authoring, Presentations, PIE or Mica.

If W0 reveals a real product defect, stop and return to Planner/Critic. Do not repair production inside this Web Gate.

### Project bridge exact bytes

All Project-policy test conditions must use exactly these UTF-8 bytes:

```text
对每条面向用户的自然语言最终回答，以及自然语言与机器内容混合的最终回答，如果当前 Clear Writing 可用，则使用其最合适的现有写作能力；纯 JSON、YAML、代码、命令、原始日志、逐字引用或其他要求精确机器输出的请求不为此强制调用 Clear Writing，直接保持精确原样。不要模拟、重建或复制 Clear Writing 内部规则。
```

Before live testing, record this text and its SHA-256 in the freeze manifest. W2 Treatment and Control must use identical bytes.

### W0 — invocation-policy safety

W0-A tests natural-language and mixed responses. PASS requires appropriate existing sibling behavior, exact preservation of embedded machine payloads, no mechanical shortening of necessary long answers, and preservation of complete executable prompts/contracts and genuinely branched procedures.

W0-B tests pure exact-only output after explicit Clear Writing plugin-level selection when the surface permits it. Without concrete Skill-load evidence the maximum claim is:

`PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`

For exact-only tasks the assistant message content must equal the frozen target payload exactly, with no preface, Markdown fence, explanation or reformatting unless the target itself contains it.

Any release-critical W0 failure stops W1/W2.

### W1 — Project-policy behavior reliability

W1 starts only after W0 PASS and uses disposable test Project context. The user must not manually invoke Clear Writing on each turn.

The only formal W1 claim is:

`PROJECT_POLICY_BEHAVIOR_RELIABILITY`

W1 must test ordinary -> exact exemption -> ordinary recovery, Chinese -> one-turn English -> Chinese recovery, short -> necessary long answer, explanation -> complete executable prompt/contract -> ordinary response, sibling route -> unrelated ordinary response, and mixed -> exact-only -> ordinary response.

Record invocation/load evidence if the surface actually exposes it. In its absence, model self-report and output style cannot prove plugin loading.

W1 PASS does not prove plugin causality.

### W2 — strict matched plugin increment

W2 starts only after W0 and W1 PASS.

Before the first W2 prompt, freeze:

- Treatment and Control Project-setting exact bytes;
- ChatGPT surface;
- model identity and any exposed effort mode;
- actual Web Clear Writing candidate identity;
- Project memory mode;
- conversation-isolation structure;
- task set and task-order policy;
- pair-order policy;
- attempt budget;
- rubric and evaluation procedure;
- Reviewer input;
- stop condition.

Treatment and Control must use identical Project-setting bytes, the same surface/model, the same pre-frozen tasks/order/budget/rubric/evaluation, fresh isolated conversation contexts, and no cross-arm access to outputs or Project history.

If Projects are used, both must use the same frozen memory mode and a structure that prevents cross-arm contamination.

The only material difference may be:

`Clear Writing candidate availability / consumption`

Control must not copy Clear Writing Skill prose, imitate Treatment after seeing it, or receive rules derived from Treatment.

If the product surface cannot legally establish that matched condition:

`W2=INCONCLUSIVE`

and release stops. Any known-confounded alternative is `DIAGNOSTIC_ONLY`.

No broad account change may be silently used to manufacture a matched condition. If the required availability difference cannot be achieved inside the reviewed test envelope, stop rather than weakening W2.

### W2 frozen scoring rule

Use the pre-frozen paired task bank with one output per task/arm.

Hard failures include semantic/factual drift, changed exact machine payload, violated language override, incomplete executable prompt/contract, or materially wrong sibling ownership.

For the seven reader-facing paired tasks:

- Treatment must be independently preferred for contract-relevant reasons on at least 4 of 7;
- Control may be preferred on at most 1 of 7;
- remaining tasks may tie;
- Treatment must have zero hard failures;
- exact/mixed protection controls must not regress.

Initial scoring uses arm-neutral labels A/B. Reveal arm identity only after judgments are frozen.

Failure to meet this rule means plugin incremental value is not proven. The rubric cannot change after outputs are seen.

### W3 — no-bridge diagnostic

W3 runs only after W2 concludes. It measures discoverability/fallback behavior and is non-release-critical. It cannot rescue W2.

### Fresh G7 reservation

G7 is not executable under this package.

Only after W0/W1/W2 satisfy the release-critical conditions may Planner freeze a separate G7 batch. That later freeze must bind production candidate, actual Web candidate identity, Project bridge bytes, surface/model, Project memory mode, isolation policy, attempt budget, fresh task set, task order, W0/W1/W2 rubric, Reviewer input and stop condition.

KR-WEB-01..09, old controls, every W0/W1/W2 task and every debug/diagnostic sample seen during this work are permanently excluded from G7 fresh evidence.

## Positive completion

This task has a successful path only when:

1. W0 PASS;
2. W1 `PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS`;
3. W2 strict matched comparison PASS and plugin incremental value is proven;
4. W3 diagnostic result is recorded honestly;
5. all identities, inputs, outputs, attempts and evidence are preserved;
6. an independent Reviewer reads the actual Web outputs and evidence.

A successful result only permits Planner to prepare a separate fresh-G7 freeze. It does not authorize release or rollout to the real Project setting.

## Non-substitutable semantics

- Pure exact-only output is an activation exemption, not proof of a global Clear Writing bypass coordinator.
- W1 reliability is not plugin causality.
- W2 must be truly matched or be `INCONCLUSIVE`.
- Model self-report never proves Skill/plugin consumption.
- Clear Writing selection does not justify changing protected machine payloads.
- Existing sibling ownership remains unchanged.
- A poor model answer is evidence and cannot be retried until it wins.
- No development sample can later be relabeled G7 fresh.
- No gate claim may exceed its actual evidence.

## Implementation / execution scope

Repository writes are limited to task control/evidence under:

- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/`;
- `docs/goals/`;
- `docs/operations/prompts/`;
- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_2_2026-10-18.md`;
- `results/clear-writing--every-response-invocation-policy/`;
- Issue #13 tracking text.

No production source edits are allowed.

## Account / Project / plugin authorization boundary

This planning turn authorizes no live ChatGPT mutation.

Only after an independent Critic gives execution-ready PASS to this exact Plan/Goal/Kickoff package and the user explicitly sends the approved kickoff may the execution thread perform or request the reviewed test-only setup.

The reviewed setup may create disposable empty test Projects/chats, place the exact frozen bridge text in those disposable Projects, freeze the same Project memory mode where the product exposes such a control, and inspect the actual Clear Writing candidate identity/availability.

Any platform confirmation needed to make the exact reviewed **test candidate** available remains a user-visible action at execution time. The package does not authorize changes to the user's real AI Research Stack Project, global custom instructions, plugin permissions, unrelated chats/files, subscription/account identity, public release state or any broader plugin set.

The package also does not authorize repeated candidate availability toggling merely to force W2 to become matched. If strict W2 cannot be established without operations outside this envelope, record `W2=INCONCLUSIVE` and stop.

## Evidence preservation

Frozen public-safe inputs live in:

`docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_2_2026-10-18.md`

Execution evidence must be written under:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.2/`

Required artifacts:

- `FREEZE_MANIFEST.json`
- `PROJECT_BRIDGE.txt`
- W0 full inputs/raw outputs/run manifest/verdicts
- W1 full turn-by-turn sequences/run manifest/verdicts
- W2 arm-separated raw outputs, frozen pair manifest, blinded review, reveal map and causal verdict
- W3 diagnostic inputs/outputs/verdict
- `FINAL_REVIEW_INPUT_MANIFEST.md`
- `RESULT.md`

Each run records at minimum gate/task/turn id, timestamp, surface/model label, Project memory mode, bridge SHA, frozen production commit, actual Web candidate identity or `UNOBSERVABLE`, opaque isolation id, attempt number, prompt SHA-256, response SHA-256, direct invocation/load evidence when available, and exact-output comparison when applicable.

Do not store account IDs, credentials, private chat URLs or unrelated Project content. Public-safe full outputs may be committed. UI screenshots containing private account information belong only in `private/exports/`; repository evidence records a sanitized description/hash when needed.

## Attempt / retry policy

Default: exactly one model answer per frozen task/turn/arm.

One technical retry is allowed only when the original attempt produced no usable model answer because of an infrastructure failure. Preserve the failed-attempt record.

A low-quality or failing answer is not an infrastructure failure and cannot be retried.

## Stop / recovery

Stop and return to Planner if:

- W0 release-critical safety fails;
- W1 behavior reliability fails;
- frozen identity cannot be established;
- memory/isolation cannot prevent cross-arm contamination;
- W2 strict matched availability cannot be established;
- requested setup exceeds the reviewed account/project/plugin envelope;
- surface/model/candidate identity changes mid-batch;
- evaluation rules would need to change after outputs are seen.

Do not create a successor automatically.

After infrastructure-only interruption, resume from the first unanswered frozen task only if every frozen identity remains unchanged. Otherwise invalidate the partial batch and return to Planner before restarting.

## Acceptance and regression gates

| Gate | Required result | Release effect |
|---|---|---|
| W0 | natural/mixed safety + explicit-selection exact stress PASS | blocker |
| W1 | `PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS` | blocker |
| W2 | strict matched plugin increment PASS | blocker; INCONCLUSIVE stops |
| W3 | diagnostic result recorded | non-blocking |
| G7 | separate later frozen fresh batch | not executable here |

Existing KR-WEB-01..09 and four prior should-not-change controls remain historical known evidence and do not substitute for current Web behavior.

## Final independent review input

The Reviewer must receive:

1. this Plan, the matching Goal and approved Kickoff;
2. proposal v0.2 and its Critic PASS;
3. `FREEZE_MANIFEST.json`;
4. exact bridge bytes/hash;
5. actual Web candidate identity evidence;
6. every W0 raw output and exact comparison;
7. every W1 turn-by-turn output and behavior verdict;
8. both W2 arms with arm identity hidden for first-pass scoring;
9. frozen W2 rubric, blinded judgments, reveal map and causal verdict;
10. W3 diagnostic evidence;
11. attempt/retry log;
12. executor `RESULT.md`.

The Reviewer separately decides PROCESS / IDENTITY, W0 PRODUCT SAFETY, W1 PROJECT_POLICY_BEHAVIOR_RELIABILITY, W2 PLUGIN_INCREMENT and W3 diagnostic finding. The Reviewer cannot convert W1 into plugin causality, rescue a confounded W2 or authorize G7 unless W0/W1/W2 meet the frozen criteria.

## Natural-language usage / routing expectations

If the gates later succeed, the intended normal experience is:

- ordinary and mixed reader-facing answers in a participating Project follow the Project-level Clear Writing policy;
- pure exact-only machine requests remain untouched without forcing a writing Skill;
- the user does not manually invoke Clear Writing on every normal turn;
- sibling writing responsibilities remain task-appropriate.

This Plan does not claim those behaviors are already verified.

## Out of scope

Production edits, real Project rollout, broad account/plugin mutation, paid external review, G7 execution, user acceptance, release/version bump, PIE, Mica, Research Authoring, Presentations, and any new skill/router/state machine/finalizer are out of scope.
