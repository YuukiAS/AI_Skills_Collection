---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 050_writing_style_host_codex_runtime
---

# 050 Writing Style — host-Codex runtime and bounded external QA

## User decision

Task 049 is superseded and must not continue as the active refinement task. Its useful implementation work is inherited only as engineering evidence/substrate; its paid Terra-per-stage architecture and its failed style outputs are not accepted product behavior.

Start 050 from 049 tip `19d7ba6f1a2a8752adfa4e7c11d3ebe9ed318070`. The latest observed `main` at task creation is `00b6b83b8bdf9d21f4c10908931ed1b5ffc5f473`; 050 must re-read current `main` before integration and must not overwrite unrelated later work.

## Product objective

A normal user should invoke the installed `writing-style` plugin and have the current host Codex model itself perform the meaning-first scientific rewrite. The plugin must not create a hidden paid-model pipeline for Document Map, segmentation, Meaning Cards, writing, semantic audit, repair, or assembly.

The desired ownership is:

```text
host Codex + installed writing-style
  -> document understanding
  -> argument units
  -> Meaning Cards / fidelity reasoning
  -> unit rewrite
  -> semantic self-audit / targeted repair
  -> assembly
local deterministic helpers
  -> literal / citation / formula / path / coverage checks
optional independent Terra QA
  -> final candidate-only reader review only
human
  -> style and final artifact acceptance
```

Normal production use of `writing-style` must require no OpenAI API key and incur no additional API charge beyond the user's existing Codex/ChatGPT product access.

## 049 inheritance

Preserve and selectively reuse useful 049 work where it remains valid, including:

- argument-unit and source-span concepts;
- Meaning Card / Fidelity Ledger semantics;
- `inline-critical` vs `relocatable-trace` fidelity roles;
- Reader Core / Technical Trace separation;
- deterministic literal verification;
- isolated/shadow installed-entrypoint replay rules;
- private-artifact authorization boundaries;
- style-smoke A/B/C identities and source ranges;
- evidence that fake multistage stages, source-copy fallback, and automated readability PASS are insufficient.

Do not preserve as production architecture:

- OpenAI/Terra calls for intermediate rewrite stages;
- GitHub push-triggered paid transforms;
- model-call-count as proof of multistage quality;
- source-copy completion of missing semantic meaning;
- automatic paid review/repair loops.

## Cost boundary

External paid model use is QA only, not generation.

For task 050:

- at most one combined Terra reader review for the three fixed style smokes;
- after user `STYLE_ACCEPT`, at most one Terra reader review for the complete final candidate;
- maximum two Terra API calls for the entire 050 campaign;
- hard cumulative Terra cost ceiling: USD 0.50;
- hard worst-case preflight ceiling per Terra call: USD 0.30;
- retries/reruns/new processes do not reset the campaign budget;
- ordinary Git pushes must never trigger paid model work;
- billing/quota errors are zero-retry failures;
- no weaker-model fallback is allowed merely to stay within budget.

If a paid review cannot fit the hard budget, do not call the API. Return to Planner/user with a cost preflight instead.

## Human gates

Use the same fixed SMOKE-A/B/C regression content inherited from 049. Generate them with the actual installed host-Codex route, not by hand editing and not through Terra generation.

After local checks and at most one combined candidate-only Terra QA, stop for user `STYLE_ACCEPT` / `STYLE_REJECT`.

Do not generate the complete private report before `STYLE_ACCEPT`.
