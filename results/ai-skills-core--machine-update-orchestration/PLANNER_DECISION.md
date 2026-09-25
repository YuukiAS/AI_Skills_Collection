# Planner Decision — AI Skills Maintainer Machine Update Orchestration

Task key: `ai-skills-core--machine-update-orchestration`  
Date: 2026-09-24  
Status: `APPROVED_TO_CONTINUE_PRE_RELEASE_VALIDATION`

This decision resolves D1-D3 in `PLANNER_DECISION_REQUEST.md` without changing the frozen V2.1 architecture, scope, Gate Matrix, authorization boundary, version semantics, or recovery semantics.

## D1 — Fresh normal-entry evidence

Decision: **use the existing canonical candidate replay path. No paid API authorization is required.**

The task's `No paid API` boundary means no paid OpenAI Responses/Terra/API call. It does **not** prohibit the already-existing repo-local candidate replay that:

- uses the pinned local Codex runtime;
- reuses the existing Codex account identity;
- launches a fresh ephemeral `codex exec --ignore-user-config` child;
- stages the exact committed candidate under the temporary `@ai-skills-candidate` namespace;
- cleans up the candidate identity afterwards;
- leaves the installed production plugin identity unchanged.

Canonical source: `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`.

Previous repository execution review also explicitly records that this replay requires no Terra/OpenAI Responses call.

Therefore the earlier host-safety interpretation that “fresh Codex child == paid API” is incorrect for this task.

Authorized next action:

- run the existing `scripts/candidate_plugin_replay.py replay` path against the exact committed final candidate;
- use public-safe task inputs;
- exercise the required short normal-entry routing evidence for G1/G3;
- do not call Terra, `/v1/responses`, or any paid API;
- do not copy credentials or create another replay framework.

If Host/Auto-review still blocks the canonical replay command, record the exact denial as an **environment/control-plane blocker**. Do not reclassify it as a paid-API authorization blocker and do not weaken G1/G3.

## D2 — Capability-bearing formal `release` for G2

Decision: **choose D2 option 1. Do not advance `release` or migrate the real Marketplace yet.**

The current AI_Skills `release` correctly points to the already formal 5.1.0 release, which still contains `ai-skills-core 0.4`. The task candidate is the next capability-bearing release candidate (`5.2.0`, `ai-skills-core 0.5`) after main drift.

Correct sequence:

1. finish pre-release candidate evidence that does not require the formal release identity:
   - G1/G3 candidate normal-entry replay;
   - G4/G5 task-owned fixture execution;
   - deterministic regressions already required by the frozen package;
2. hand the exact final candidate to the independent implementation Reviewer;
3. only after Reviewer PASS, integrate/promote the exact final candidate through the approved release path;
4. advance AI_Skills `release` to that exact formally closed commit under the frozen fast-forward-only producer contract;
5. then run the **real** G2 legacy Marketplace `main -> release` migration, reinstall `ai-skills-core 0.5`, require reload, and prove the fresh released production identity.

Do not move `release` to the task branch before review merely to unblock G2. G2 waiting for the capability-bearing formal release is a sequencing boundary, not a reason to stop the current pre-release validation work.

## D3 — Real G4/G5 fixture execution

Decision: **choose D3 option 2: task-owned local fixture repositories are authorized.**

Create only task-owned fixtures under the current task repository boundary, preferably:

`private/exports/ai-skills-core--machine-update-orchestration/fixtures/`

The fixture repositories may model only the frozen G4/G5 cases:

- stale AI_Skills managed consumer that should update;
- unaffected repo that must remain byte-for-byte unchanged;
- unmanaged apparently-conflicting AGENTS/project rule that must remain unchanged and produce the correct diagnostic;
- unrelated dirty canonical checkout that can safely proceed;
- overlapping user-owned dirty path that must produce exactly one bounded Human Gate;
- bounded failure after an earlier safe step;
- exact Marketplace/source restoration behavior required by G5;
- rerun/convergence and should-not-change evidence.

Constraints:

- do not use unrelated real user projects as fixtures;
- do not mutate real unowned AGENTS/project rules;
- do not use `/tmp` as the only durable evidence location;
- fixture repositories themselves may remain ignored/private, but commit a concise evidence report with paths/hashes/results under the task's tracked `results/` directory;
- no paid API, Host mutation, Bridge runtime source change, or new framework/state machine.

## Task state after this decision

The task is **not blocked on Planner**.

Executor should resume bounded pre-release validation in this order:

1. D1 canonical no-paid candidate replay for G1/G3;
2. D3 task-owned G4/G5 fixture execution;
3. refresh completion/evidence audit and push;
4. hand exact candidate to independent Reviewer;
5. after Reviewer PASS/integration, perform D2 formal release advancement and real G2 production Marketplace migration/fresh-session smoke.

Do not claim full G1-G5 PASS until the corresponding evidence exists.

No architecture/Critic revision is required by this decision.
