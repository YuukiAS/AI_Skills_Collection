---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: infra_paid_review_safety_migration_20260903
decision: PLAN_FROZEN
---

# Paid external review safety migration

## Objective and value

Make paid Text Review and Visual Review explicit, bounded infrastructure gates rather than hidden automatic production dependencies. The migration must also reduce GitHub Actions noise by turning heavyweight full CI into a lifecycle gate instead of a per-commit ritual.

## Frozen decisions

The migration is bounded by the pass-by-pass contract below. It must preserve separate `OPENAI_REVIEW_API_KEY` and `OPENAI_VISUAL_REVIEW_API_KEY` names, remove cross-secret fallback, pin paid review to `gpt-5.6-terra`, use the exact Bridge Kit paid-review safety implementation, and keep 050 blocked until this repo-wide migration is integrated.

Paid-review accounting and parallelism are now also frozen:

- every successful paid call must record both worst-case reservation and actual model cost derived from Responses usage;
- reviewer requests use deterministic pricing semantics: Terra, `service_tier=default`, low reasoning, no tools, bounded output, and explicit prompt-cache mode with no implicit cache breakpoint;
- plugin development may remain parallel, but AI_Skills paid Terra review uses one repo-wide execution slot;
- GitHub Actions concurrency is only the final race mutex, not a FIFO queue;
- do not add a database, worker, daemon, queue service, or new Reviewed Handoff state for this.

## Implementation scope

Scope is limited to AI_Skills paid-review workflow consumers, paid-review documentation, Reviewed Handoff Planner/Executor policy, CI lifecycle policy, deterministic regression tests, Bridge Kit pinning, and canonical Presentation TODO consolidation required to restore the full Marketplace gate.

## Acceptance and regression gates

The acceptance gates are the failure list, red-team checks, deterministic tests, live-smoke conditions, CI lifecycle requirements, and integration/050 gate specified below. Ordinary push must make zero paid OpenAI calls, full Marketplace CI must be explicit PR/manual gate, and CI must not write repository commits.

## Natural-language usage / routing expectations

An Executor may use local deterministic tests during development. A paid external review is only requested when a frozen Plan includes a bounded campaign budget and an explicit manual review invocation. Full GitHub Marketplace CI is dispatched after an implementation candidate is frozen, not after every ordinary commit.

If another AI_Skills paid Text/Visual review is already queued/running, a task does not dispatch another paid workflow and does not reserve budget; it waits for the repo-wide paid-review slot and continues on the next normal Executor/scheduler check.

## Out of scope

Do not execute 050 writing rewrite, do not run private 050 smoke, do not bring back 049 Terra-per-stage behavior, do not use old archived-project API keys, do not add a new Reviewed Handoff state machine, do not build a FIFO queue service, and do not version bump unless canonical version policy and Planner require it.

## Pass 1 — Product

### Final behavior

Normal AI_Skills generation and intermediate reasoning use the host model and local deterministic checks. Paid OpenAI review is an explicit final-QA capability, not a hidden production dependency.

Text Review and Visual Review remain available, but every paid call is bounded before it is sent and leaves a task-local accounting receipt afterward.

### Failure even if tests pass

FAIL if any of the following remains true:

- ordinary push can launch Terra;
- text review silently falls back to the visual secret or vice versa;
- a paid review can run without a task/campaign budget context;
- retry/rerun can reset paid budget;
- a request can be sent before worst-case reservation is persisted;
- successful review usage is not attributable back to the task as actual model cost;
- a billing/quota error enters a sleep/backoff loop;
- Visual Review can silently invoke image generation or another paid tool;
- Planner contracts still encourage per-stage external review for routine reasoning;
- multiple plugin paid reviews are allowed to race against the shared 100k TPM without a repo-wide slot/mutex contract;
- GitHub concurrency pending behavior is treated as a reliable FIFO queue;
- Text Review or Visual Review is broken after migration;
- task 050 starts before this migration is integrated.

## Pass 2 — Reality

Executor must read the latest main of both repositories before implementation.

### AI_Skills_Collection verified starting points

Current policy:

```text
AGENTS.md §8.3.1
docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md
```

Known active risk paths to inspect at minimum:

```text
.github/workflows/ai-bridge-text-review.yml
.github/workflows/ai-bridge-visual-review.yml
.github/workflows/research-presentation-comparative-visual-review.yml
.github/workflows/research-presentation-candidate-visual-finish-review.yml
automation/reviewed_handoff/prompts/PLANNER.md
automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md
docs/AI_BRIDGE_TEXT_REVIEW.md
docs/AI_BRIDGE_VISUAL_REVIEW.md
relevant tests
```

At initial Plan freeze, the generic text and visual workflows still contained paid `push` triggers and Text Review permitted `OPENAI_REVIEW_API_KEY || OPENAI_VISUAL_REVIEW_API_KEY`. Migration implementation has already begun to remove those paths; Executor must re-read current branch, not assume initial state.

### Bridge Kit

Read current migration branch/main, AGENTS, paid-review guard, Text Review / Visual Review implementation, Responses request construction, retry behavior, usage/result schemas and tests. Bridge Kit owns generic transport/model-call/accounting mechanics; AI_Skills owns consumer policy and dispatch lifecycle.

## Pass 3 — Alternatives

### A. Rely only on OpenAI Project hard limit / RPM

Rejected. Platform limits are final circuit breakers, not per-task accounting or scheduling.

### B. Query organization Costs API before each call

Rejected. It is asynchronous/aggregated and requires stronger credentials than review workflows should possess.

### C. Build a dedicated FIFO review service

Rejected. Current paid review frequency is too low to justify a queue database, worker, lease/heartbeat system or daemon. It adds more failure modes than user value.

### D. Persistent per-task reservation + actual-cost receipt + repo-wide execution slot

Selected.

Each request is preflighted from the exact request, worst-case cost is reserved persistently before send, successful usage is converted into task-local actual model cost, and multiple plugin tasks keep independent ledgers. AI_Skills serializes only the paid Terra execution slot; normal Codex/plugin development stays parallel. Platform Terra-only allowlist, 10 RPM / 100k TPM and USD 10 monthly hard limit remain external safety layers.

## Pass 4 — Red team

Actively test:

- two concurrent/restarted workflows targeting the same campaign;
- two different plugin campaigns with independent budgets;
- two different plugin tasks trying to enter paid review simultaneously;
- workflow rerun after a failed request;
- transient 429 versus billing/spend-limit errors;
- malformed/missing pricing config;
- model/service-tier/reasoning/tool mismatch;
- unexpected cache-write accounting;
- text and image-input token preflight;
- paid call count exhausted with money remaining;
- budget exhausted with call slots remaining;
- evidence writeback triggering another paid run;
- missing secret on explicit manual review;
- Visual Review trying to use any generation/tool capability;
- old specialized presentation workflows bypassing the central guard;
- GitHub concurrency pending cancellation/replacement being misread as FIFO delivery.

## Pass 5 — Execution contract

### 1. Planner / GPT contract

Update the Reviewed Handoff Planner contract so any Plan containing paid external review explicitly freezes:

```text
necessity of independent external review
model
max paid calls
per-call worst-case ceiling
campaign hard budget
manual trigger
retry policy
candidate/source boundary
```

Planner must reject routine per-stage paid review when host-model reasoning + deterministic checks suffice. Planner must also distinguish parallel development from serialized paid final QA and must not invent a queue service merely to coordinate a few final reviews.

### 2. Executor contract

Update Executor guidance to refuse any paid invocation that lacks the frozen budget context or violates `docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md`.

Before dispatching a paid Text/Visual workflow, Executor must inspect current AI_Skills paid review runs. If another paid review is queued/in-progress, it must not dispatch and must not reserve budget. Keep the current task state legal and report `waiting_paid_review_slot` operationally; do not create a new workflow state solely for this.

### 3. Shared Bridge Kit budget/accounting guard

Use one generic implementation for Text Review and Visual Review.

The guard must support at least:

```text
task_key / campaign_id
model_id
campaign_budget_usd = 0.50 default
max_paid_calls = 2 default
per_call_worst_case_usd = 0.25 default
max_output_tokens = 4096 default
pricing identity / reviewed price table
persistent reservation ledger
actual response usage
actual per-call/campaign model cost
```

Before sending `/v1/responses`:

1. build the exact request;
2. count exact input tokens via `/v1/responses/input_tokens`, including image input;
3. validate request pricing semantics;
4. calculate worst-case cost;
5. atomically reserve cost + call slot in the task campaign;
6. persist reservation before send;
7. only then send the paid request.

Reservation is never automatically refunded.

After success, record response id, input/cached/cache-write/output/reasoning usage, actual model cost and cumulative actual model cost. `output_tokens` already includes reasoning tokens; do not double-count reasoning.

### 4. Deterministic Terra request / pricing boundary

Current reviewed model price baseline (official OpenAI docs, reviewed 2026-09-03):

```text
model: gpt-5.6-terra
input: USD 2 / 1M tokens
cached input: USD 0.20 / 1M tokens
output: USD 12 / 1M tokens
cache write: 1.25x uncached input price
```

The paid review request must explicitly use:

```text
model = gpt-5.6-terra
service_tier = default
reasoning.effort = low
tools = []
max_output_tokens = bounded
prompt_cache_options.mode = explicit
no explicit cache breakpoint
```

This intentionally disables implicit cache-write behavior for low-frequency review calls and makes preflight/accounting deterministic. If successful response still reports nonzero cache-write usage or another unrecognized pricing mode, mark accounting unverified and block subsequent paid calls in that campaign.

Any request entering a different/unknown model price tier must fail closed. Do not silently switch to Luna/Sol.

### 5. Retry classification

Default automatic paid retry count is zero.

Billing/quota errors including at least:

```text
credit_balance_exhausted
project_spend_limit_exceeded
organization_spend_limit_exceeded
organization_usage_limit_exceeded
```

must fail immediately. A future transient retry still consumes the same campaign budget/call slot.

### 6. Workflow triggers and repo-wide paid-review slot

Generic Text Review and Visual Review paid jobs are `workflow_dispatch` / equivalent explicit bounded invocation only. Remove paid `push` triggers.

All AI_Skills paid Text/Visual workflows share one repository-wide concurrency group:

```text
ai-bridge-paid-review-${{ github.repository }}
```

with `cancel-in-progress: false`.

This concurrency group is only a final race mutex. It is not the queue. Executors must avoid dispatching while another paid run is active, so the repository should not accumulate multiple pending paid workflows. Do not claim FIFO ordering from GitHub concurrency.

Different task campaigns retain independent `results/<task_key>/paid_review_budget.json` ledgers. Waiting for the repo-wide slot consumes no reservation and no paid-call count.

### 7. Secret migration

Keep separate repository secret names:

```text
OPENAI_REVIEW_API_KEY
OPENAI_VISUAL_REVIEW_API_KEY
```

Both belong to the new `AI_Research_Review` project; they may be distinct keys with the same minimal `Responses=Write` scope. Remove cross-secret fallback. Missing secret during explicit review fails closed. Never print secret values.

### 8. Model variables

Audit `OPENAI_TEXT_REVIEW_MODEL` and `OPENAI_VISUAL_REVIEW_MODEL`. Production review resolves exactly to `gpt-5.6-terra`; stale variables must not override it.

### 9. Visual boundary

Visual Review uses Terra image input only. No image generation, web search, file search, computer use or other paid tool. Image inputs must be included in the exact request preflight.

### 10. Tests before live spend

Before any live OpenAI call, deterministic tests must prove at minimum:

- paid push triggers absent;
- text/visual secret fallback absent;
- Planner/Executor policy references active;
- max calls / per-call / campaign budget validation;
- reservation survives rerun/restart;
- same-campaign concurrency cannot double-spend;
- different campaigns keep independent budgets;
- actual cost from usage is correct and reasoning tokens are not double-counted;
- request forces default service tier / low reasoning / no tools / explicit no-breakpoint cache mode;
- unexpected cache-write/pricing mode blocks subsequent paid call;
- quota/billing errors have zero automatic retry;
- model/pricing mismatch fail closed;
- Text Review request constructs correctly;
- Visual Review image-input request constructs correctly;
- repo-wide concurrency is shared across Text/Visual workflows;
- policy/dispatcher does not treat GitHub pending runs as FIFO queue.

### 11. Live migration smoke

Only after deterministic tests pass and both new project-scoped GitHub secrets are PRESENT, run a tiny public-safe live smoke for:

1. Text Review;
2. Visual Review with one small public-safe image.

Use one migration campaign with max 2 calls / USD 0.50 reserved budget; each request <= USD 0.25 worst-case. Record actual model cost for each call and campaign total.

Do not use private 050 artifacts.

### 12. CI lifecycle migration

Codex Marketplace full matrix / release/integration CI is explicit PR/manual gate, not every push. CI must be read-only and must not generate/push its own marketplace commit. Ordinary push may only run cheap, path-scoped, zero-paid, read-only checks.

### 13. Integration / 050 gate

After Bridge Kit companion and AI_Skills consumer migration pass, pin the exact Bridge Kit commit, run explicit full CI, then integrate the migration to main.

Only after that may `reviewed/050_writing_style_host_codex_runtime` advance from `PLAN_FROZEN`. Reconcile the latest main migration changes into 050 first.

## Release decision

Repository bump decision: `NONE` during migration implementation.

This is infrastructure safety/compatibility work. Re-evaluate release/version only if canonical version policy requires it.
