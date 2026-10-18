# Goal — Clear Writing Web invocation policy v0.4

Repository: `YuukiAS/AI_Skills_Collection`  
Task: `clear-writing--every-response-invocation-policy`  
Source/evidence branch: `reviewed/clear-writing--scientific-explanation-readability-repair`

This package keeps invocation-policy proposal v0.2 unchanged and revises only
the Web execution transport/blind-review isolation needed to close
`CW-WEB-ER-01` and `CW-WEB-ER-05`.

## Product goal

Evaluate the already-PASS Clear Writing production candidate on real ChatGPT Web
without changing production.

The live evidence path is:

0. execution-ready Critic PASS + user sends approved v0.4 Kickoff;
1. exact-branch watcher status/stop proof;
2. read-only W2 matched-environment preflight v0.4;
3. exact private candidate materialization/parity;
4. W0;
5. W1;
6. W2 strict matched execution;
7. W2 initial preference review inside the isolated blind-review context v0.4;
8. reveal + causal W2 summary;
9. W3 diagnostic only after determinate W2 PASS/FAIL;
10. independent final Web Gate review;
11. stop before G7.

## Frozen production identity

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

Six-skill architecture remains unchanged.

## Manual Web transport is decoupled from exhausted Reviewed Handoff state

The Reviewed Handoff task exhausted its one allowed Plan revision. It has now
been closed through the existing legal Planner-decision terminal route:

```text
CURRENT.state=AWAIT_HUMAN_DECISION
human_gate_reason=PLANNER_DECISION
plan_revision=1
max_plan_revisions=1
```

The required task-local `FINAL_REPORT.md` records that this terminal state
closes only the machine transport, not Issue #13 or the Web evaluation.

Therefore:

- `CURRENT.json` is not the execution transport for the Web experiment;
- no raw CURRENT edit/reset/budget increase is permitted;
- no re-arm to `PLAN_FROZEN` is attempted;
- no new state/schema is added;
- Bridge Kit is not modified;
- watcher/Codex Executor is not used for Web execution;
- live Web execution is a user-authorized manual test run governed by this
  frozen package;
- final review is handed manually to an independent Critic using the frozen
  final-review prompt and evidence manifest, not through a Reviewed Handoff
  state transition.

This is deliberate decoupling through the Bridge Kit's existing legal terminal
path, not a bypass of its state graph.

## Canonical v0.4 read-only execution contract

After execution-ready PASS, the following are immutable:

- approved invocation-policy proposal v0.2 + Critic PASS;
- task REQUEST and PLAN;
- this Goal;
- Task Bank v0.4;
- W2 matched-environment preflight v0.4;
- Web test candidate materialization v0.3;
- W2 reveal map v0.3;
- W2 blind-review context v0.4;
- W2 blind-review prompt v0.4;
- Web Gate Kickoff v0.4;
- bridge bytes;
- pair/task order;
- attempt budget;
- rubric;
- scoring thresholds;
- stop/recovery rules.

Any required change stops the batch and returns to Planner -> Critic.

## W2 preflight requirement

Preflight must run before all candidate/Project mutation and before the first
model request.

It must prove:

- strict Treatment/Control candidate-availability isolation;
- same account/workspace/surface/model/effort;
- exact same bridge bytes;
- project-only or explicitly equivalent cross-arm memory isolation;
- no repeated global install/uninstall;
- no account/workspace/role/permission mutation;
- feasibility of the separate blind-review isolation context.

If any required matched/isolation mechanism cannot be proven:

`W2=INCONCLUSIVE`

and the entire live batch stops before candidate creation, Project creation, W0,
W1, W2 and W3.

## Candidate setup

Candidate materialization remains exactly the already-closed v0.3 contract:

`docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`

At most one PRIVATE test candidate is created from the exact frozen source after
preflight PASS, then re-read and parity checked before W0.

Failure after creation leaves it unchanged + PRIVATE. No cleanup/update/delete/
replacement is authorized here.

## W0 / W1 / W2 / W3

The accepted gate semantics remain unchanged:

- W0: natural/mixed safety + explicit-selection exact-only non-contamination;
- W1: only `PROJECT_POLICY_BEHAVIOR_RELIABILITY`;
- W2: strict matched plugin increment;
- W3: non-release-critical diagnostic only.

W2 `INCONCLUSIVE` => W3 not run.
W2 determinate PASS/FAIL => W3 may run diagnostically.

The frozen 4/7 rule is unchanged.

## Blind-review isolation

The W2 initial preference Reviewer must follow:

`docs/design/clear-writing/CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`

and the frozen blind prompt:

`docs/operations/prompts/CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`

Preferred transport is a new empty review Project:

`CW-W2-BLIND-v04`

with project-only memory, no prior task chats, no files/knowledge/repo source, and
no tool/connector/source access.

A fresh thread inside the current AI Research Stack Project is not blind enough.

Before the first blind-review response, record the context identity/isolation
manifest. The Reviewer sees only the sanitized blind packet. Verdicts/reasons
for P01-P08 must be saved and hashed before reveal.

If this isolation cannot be proven, W2 cannot receive PASS.

## Evidence and final review

All live evidence goes only under:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/`

The terminalized `CURRENT.json` remains unchanged throughout manual Web
execution.

At the end, the execution operator creates the frozen evidence manifest and
uses the pre-frozen final-review prompt to hand the result to an independent
Critic manually.

No `REVIEW_1.md`/Reviewed-Handoff transition is invented for this decoupled
manual Web transport.

## Completion

Successful v0.4 Web Gate completion requires:

- preflight PASS;
- candidate parity PASS;
- W0 PASS;
- W1 behavior reliability PASS;
- W2 strict matched increment PASS;
- valid isolated blind review;
- W3 diagnostic recorded;
- independent final Web Gate review.

Success only makes the project eligible for a later G7 freeze.

G7, real Project rollout, production changes, release/version bump, PIE, Mica,
Research Authoring and Presentations remain out of scope.
