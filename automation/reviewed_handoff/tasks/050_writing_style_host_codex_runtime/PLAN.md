---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 050_writing_style_host_codex_runtime
decision: PLAN_FROZEN
---

# 050 Writing Style — host-Codex production runtime

## Pass 1 — Product

### Final user experience

The user asks the installed `writing-style` plugin to rewrite an existing Chinese scientific/technical document in natural Chinese while preserving facts, numbers, formulas, citations, comparison logic, caveats, uncertainty and conclusion strength.

The current host Codex model performs the actual rewrite. The user does not need an API key and normal plugin use does not generate a separate OpenAI API bill.

### Product success

050 succeeds only if:

1. normal installed `writing-style` routes heavy Chinese scientific rewrite to `scientific-rewrite`;
2. host Codex actually follows the meaning-first workflow rather than source-order paraphrase;
3. local deterministic checks protect exact literals without fabricating semantic understanding;
4. the fixed A/B/C private style smokes are visibly better than the rejected 049 outputs and are accepted by the user;
5. after style acceptance, the complete private report is produced through the same host-Codex route and accepted by the user;
6. optional Terra is independent final reader QA only, never a generation dependency.

### Product failure even if tests pass

FAIL if any of the following occurs:

- any normal rewrite stage requires `OPENAI_API_KEY` or calls OpenAI/Terra directly;
- intermediate Terra/OpenAI calls remain in the production generation path;
- a helper fills missing semantic content by copying source prose and calls that a Meaning Card;
- deterministic checks are treated as semantic understanding;
- a benchmark/helper path works but the ordinary installed plugin does not;
- A/B/C are hand-edited or generated through a different architecture than normal use;
- Terra/CI says PASS but the user rejects the artifact;
- a paid workflow is triggered by ordinary push;
- external paid QA exceeds the frozen budget.

## Pass 2 — Reality

### Source of truth

Executor must read before changing code:

- branch-local `AGENTS.md`;
- 050 `REQUEST.md`, `PLAN.md`, `CURRENT.json`;
- 049 `REQUEST.md`, `PLAN.md`, `CURRENT.json` and failure/smoke evidence as historical input;
- current 050 inherited implementation from 049 tip `19d7ba6f1a2a8752adfa4e7c11d3ebe9ed318070`;
- latest `main` before integration;
- current `scientific-rewrite`, `chinese-prose`, `writing-fidelity`, routing and marketplace generator;
- `ai-bridge plugin-replay` / current Host Policy behavior;
- current paid text-review / text-transform workflows only to remove accidental production coupling and preserve secure optional QA.

### Verified 049 lessons inherited

- one-shot source-following rewrite failed;
- fake multistage model calls whose outputs are unused failed;
- candidate-only reader review must actually see candidate prose;
- source-copy semantic fallback is not acceptable;
- private transport and plugin-entrypoint validation are separate concerns;
- repeated paid stage calls caused unacceptable API spend and must not recur.

## Pass 3 — Alternatives

### A. Continue Terra-per-stage orchestration

Rejected. It duplicates the host model, creates avoidable cost, makes normal plugin use depend on an external paid service, and already produced a large cost regression.

### B. Replace Terra with a cheaper external model for intermediate stages

Rejected as the default architecture. This reduces unit price but keeps the wrong product dependency and encourages silent quality degradation.

### C. Host Codex owns generation; local code verifies; Terra optionally reviews the final candidate

Selected. This matches how a Codex skill/plugin should work: the installed skill guides the current model, deterministic code enforces exact constraints, and an external model is used only where genuine reviewer independence adds value.

## Pass 4 — Red team

Reviewer must actively look for these fake-PASS paths:

- `scientific-rewrite` still imports/calls `api.openai.com` during normal generation;
- host Codex is nominal owner but a helper still performs the semantic rewrite itself;
- semantic-stage files are templated/source-copied instead of being produced by the host model;
- stage receipts prove files exist but not that the host model used the intended workflow;
- plugin replay prompt is task-specific and succeeds only for CARE/Deep Research wording;
- normal live plugin behavior differs from the replay harness;
- Terra receives source/intermediate material instead of only final candidate + audience/questions;
- Terra REVISE causes an automatic paid review loop;
- workflow reruns reset cost counters;
- ordinary push launches paid QA;
- API failure silently falls back to template/deterministic generation;
- exact-fidelity logic forces repo/checkpoint traces back into Reader Core;
- user rejection is overridden by automated PASS.

Any one is a blocker.

## Pass 5 — Execution contract

### 1. Retire 049 as active architecture

049 remains historical evidence. Do not continue 049 implementation or generate new 049 outputs. Do not merge 049 as Product PASS.

050 inherits useful code from 049 but owns all new results/evidence.

### 2. Production generation owner = host Codex

The `scientific-rewrite` skill must express and enforce, through instructions and bounded local tooling, this workflow:

```text
source
-> document understanding / map
-> argument units
-> Meaning Card + Fidelity Ledger per unit
-> source-to-card coverage check
-> selected positive transformations
-> unit rewrite from meaning + original
-> local exact verification
-> host-Codex semantic self-audit
-> targeted repair if needed
-> assembly / coherence self-check
-> final candidate
```

These semantic/writing steps are performed by the current Codex model in the same plugin task/session. They are not separate paid API calls.

### 3. Local helper boundary

Local deterministic helpers may:

- assign stable source-span ids;
- extract exact literal inventories;
- classify literal location roles where mechanically safe;
- verify numbers/formulas/citations/paths/formal identifiers;
- check that required stage artifacts/ids are present;
- check source/generated parity and privacy boundaries;
- produce non-sensitive receipts/hashes.

They must not:

- generate reader-facing prose;
- fabricate Meaning Cards from source excerpts after semantic failure;
- auto-complete missing claims/caveats by copying source text and call that semantic PASS;
- replace host-model semantic judgment with keyword overlap.

If semantic artifacts are malformed or incomplete during replay, fail/repair through the host Codex workflow; do not silently synthesize a fallback.

### 4. Production evidence without external generation calls

For bounded replay/evidence, host Codex may write task-local private intermediate artifacts such as:

```text
document_map.json
argument_units.json
meaning_cards/<unit>.json
self_audit.json
candidate_units/
final_candidate.md
stage_receipt.json
```

Private plaintext/intermediates remain machine-local and are never committed. Public evidence contains hashes/counts/ids only.

The receipt proves execution/dataflow; it is not itself a quality PASS.

### 5. Private generation route

Use `ai-bridge plugin-replay` or the current equivalent bounded isolated installed-plugin route with the current Codex identity.

The user has directed that host Codex perform the private report's intermediate reasoning and rewrite for this 050 continuation. Do not request the same authorization again. Do not copy `auth.json` or private credentials into a new environment unless separately authorized.

Private source/output stay in approved machine-local replay locations. No private plaintext in Git.

### 6. Terra ownership

Terra is optional independent candidate-only reader QA, not a normal plugin dependency.

For style-smoke QA, one Terra request may contain the final A/B/C candidates plus audience and the frozen reader questions. It must not contain original source, Document Map, Meaning Cards, intermediate drafts or internal self-audit.

After user `STYLE_ACCEPT`, at most one additional Terra request may review the complete final candidate in the same candidate-only manner.

Terra REVISE routes findings back to host Codex and then to the human gate. Do not automatically call Terra again.

Released normal plugin use keeps Terra OFF by default.

### 7. Cost safety contract

For all paid QA in 050:

- campaign call limit: 2 total Terra calls;
- campaign hard cost ceiling: USD 0.50;
- per-call worst-case preflight ceiling: USD 0.30;
- every call must use a bounded output-token limit and low/no unnecessary reasoning;
- campaign budget persists across reruns/processes;
- a retry counts as another paid call and against the same campaign cost;
- default automatic paid retry count: 0;
- `credit_balance_exhausted`, `insufficient_quota`, project/org spend-limit errors: immediate zero-retry failure;
- if the next call's conservative worst-case cost would exceed the remaining budget, do not send it;
- unknown model pricing or missing usage accounting = do not send paid QA.

Do not lower model quality silently to fit the budget.

### 8. Paid workflow trigger policy

Ordinary `push`/CI must never call a paid model.

Paid Terra QA must require explicit manual/bounded invocation after local candidate generation and cost preflight. CI may validate manifests, hashes, schemas and budget configuration without making a paid request.

### 9. Fixed regression gates

Reuse the exact 049 frozen SMOKE-A/B/C source identities/ranges as known regression inputs. They are not unseen holdout.

Generate A, B and C through the actual isolated installed host-Codex route. Do not hand edit candidates.

Before Terra:

- local exact checks PASS;
- no private plaintext committed;
- production receipt shows host-Codex workflow artifacts;
- no OpenAI API was used for generation/intermediate stages.

Then optionally perform one combined Terra candidate-only reader QA within budget.

Stop at human gate:

`STYLE_ACCEPT` or `STYLE_REJECT`.

### 10. Full run gate

Only after `STYLE_ACCEPT`:

- generate the full private report with the same installed host-Codex route;
- local exact/fidelity checks PASS;
- host Codex semantic self-audit has no unresolved critical finding;
- optional one final candidate-only Terra QA stays within the remaining 050 campaign budget;
- user reads the artifact and gives final `ACCEPT` / `REJECT`.

### 11. Tests

At minimum add/adjust tests proving:

- normal heavy generation path does not require/call OpenAI API;
- light/fidelity-only routing remains correct;
- long unheaded text is handled as bounded argument units in the skill/replay contract;
- deterministic helper cannot source-copy its way around semantic-stage failure;
- reader-core vs relocatable-trace exact verification remains valid;
- private replay leaves no plaintext in Git;
- paid QA workflow is manual-only;
- candidate-only Terra packet excludes source/intermediates;
- hard call/cost budget survives reruns;
- quota/billing failures have zero paid retry;
- public source/generated parity and normal isolated install pass.

### 12. Release

At Plan freeze:

Repository bump decision: `NONE`.

Affected plugin:

- `writing-style`: `NO_BUMP` until final user `ACCEPT`.

Do not merge 050 or bump version at style smoke.

## Stop conditions

If the host-Codex architecture cannot produce materially better A/B/C without task-specific wording hacks, do not reactivate Terra-per-stage generation and do not add a phrase blacklist. Stop, preserve evidence and return to Planner for an alternative architecture decision.
