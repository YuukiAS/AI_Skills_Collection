# Clear Writing W2 matched-environment preflight v0.3

Date: 2026-10-18  
Status: FROZEN_READ_ONLY_PREFLIGHT  
Task: `clear-writing--every-response-invocation-policy`

This preflight runs **before any live ChatGPT candidate creation, Project
creation/modification, Project-instruction write or model prompt**.

Its only outcomes are:

- `W2_MATCHED_ENVIRONMENT_PREFLIGHT=PASS`
- `W2=INCONCLUSIVE`

No partial/pass-with-caveat state exists.

## 1. Preconditions

At preflight start:

- task `CURRENT.state` must still be non-executor-owned
  `NEEDS_GPT_PLANNER`;
- execution-ready Critic PASS for package v0.3 must exist;
- the user must have sent the exact approved v0.3 Kickoff;
- the source/evidence branch must still be
  `reviewed/clear-writing--scientific-explanation-readability-repair`;
- no live Project/plugin mutation from this task may already have occurred.

If any item is false, stop.

## 2. Watcher fail-closed check

This Web Gate does **not** use Reviewed Handoff watcher/Codex as its execution
transport.

Before any ChatGPT live mutation, resolve the actual authorized local checkout
for the exact source/evidence branch and run Bridge Kit watcher lifecycle
inspection for that exact target + branch:

```text
ai-bridge reviewed-handoff watcher status --target <resolved-target> --branch reviewed/clear-writing--scientific-explanation-readability-repair
```

If a watcher is active for that exact target + branch:

1. stop it with the existing Bridge lifecycle command;
2. run `watcher status` again;
3. require the second status to prove no active watcher and no active Executor
   event.

If status cannot be obtained, the watcher cannot be proven inactive, or a
currently active Executor event cannot be safely stopped, stop before live
mutation.

Do not rely on `next_action`, task naming, branch age or an assumption that
an old watcher is gone.

After this preflight passes, no watcher may be started/restarted on that exact
target + branch until this Web Gate leaves its manual execution phase.

## 3. Account/workspace boundary — read-only

Record the current ChatGPT account/workspace boundary without changing it.

Both W2 arms must remain inside that same boundary.

The preflight must prove that W2 can be constructed without:

- account switching;
- subscription/plan switching;
- workspace switching;
- role/permission mutation;
- plugin-permission mutation;
- repeated global install/uninstall.

If not, `W2=INCONCLUSIVE`.

## 4. Candidate availability isolation — read-only capability check

Before creating the Clear Writing test candidate, determine whether the current
ChatGPT surface exposes a legal, testable mechanism that can make the candidate
available/consumable in Treatment while unavailable/non-consumable in Control,
with all other frozen W2 conditions unchanged.

Acceptable mechanism must be scoped tightly enough that:

- it does not require global plugin uninstall/reinstall between arms;
- it does not require separate accounts/workspaces;
- Control cannot auto-consume the candidate;
- Treatment can consume the exact frozen candidate;
- the mechanism itself does not change Project-setting bytes, model, effort,
  permissions, task set, rubric or conversation history.

A Project-scoped plugin availability/attachment control is an example if the
current product actually exposes it and its semantics can be verified. Do not
assume such a control exists from documentation or memory.

If no current surface mechanism can prove this isolation before candidate
creation:

`W2=INCONCLUSIVE`

and stop **all live Web Gates**. Do not create the candidate, create Projects,
run W0/W1, or run W3.

## 5. Project memory isolation — read-only capability check

"Same memory mode" is insufficient.

W2 requires an isolation mode that actually prevents one arm from seeing the
other arm's chat/Project history.

PASS requires either:

- explicit project-only memory / project-scoped history isolation exposed by
  the current product; or
- another current product mechanism whose documented/observable semantics
  equivalently prevent cross-arm history.

Default memory that may reference other Projects or chats is not acceptable.

If the required isolation cannot be established before Project creation:

`W2=INCONCLUSIVE`

and stop all live Web Gates.

## 6. Same surface/model/effort feasibility

Before mutation, record and verify that both arms can use the same:

- ChatGPT surface;
- model;
- visible reasoning/effort mode;
- task bank;
- task-order policy;
- attempt budget;
- rubric/evaluation path.

If an arm would require a different model/surface/effort because of candidate
availability, W2 is not matched.

Result:

`W2=INCONCLUSIVE`

and stop all live Web Gates.

## 7. Preflight evidence

Write only read-only-preflight evidence under:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.3/preflight/`

Required:

- `W2_MATCHED_ENVIRONMENT_PREFLIGHT.md`
- sanitized watcher-status evidence;
- sanitized account/workspace-boundary description;
- candidate-availability isolation mechanism evidence;
- Project-memory isolation evidence;
- surface/model/effort feasibility record.

Do not store account IDs, private URLs, credentials or unrelated Project data.

## 8. PASS postcondition

Only a full PASS permits the later sequence:

1. deterministic candidate archive materialization;
2. at most one private test candidate creation;
3. post-create release parity verification;
4. disposable test Project creation;
5. W0 -> W1 -> W2 -> W3.

A preflight PASS does not itself mutate anything and does not prove any Web Gate
behavior.

## 9. INCONCLUSIVE postcondition

If any required matched condition cannot be proven:

`W2=INCONCLUSIVE`

The release-critical batch stops before all candidate/Project/model mutations.

**W3 is not run after preflight INCONCLUSIVE.**

This is the single frozen answer for the preflight-INCONCLUSIVE case. W3 cannot
rescue W2.
