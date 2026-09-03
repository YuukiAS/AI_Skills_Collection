---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: infra_paid_review_safety_migration_20260903
decision: PLAN_FROZEN
---

# Paid external review safety migration

## Pass 1 — Product

### Final behavior

Normal AI_Skills generation and intermediate reasoning use the host model and local deterministic checks. Paid OpenAI review is an explicit final-QA capability, not a hidden production dependency.

Text Review and Visual Review remain available, but every paid call is bounded before it is sent.

### Failure even if tests pass

FAIL if any of the following remains true:

- ordinary push can launch Terra;
- text review silently falls back to the visual secret or vice versa;
- a paid review can run without a task/campaign budget context;
- retry/rerun can reset paid budget;
- a request can be sent before worst-case reservation is persisted;
- a billing/quota error enters a sleep/backoff loop;
- Visual Review can silently invoke image generation or another paid tool;
- Planner contracts still encourage per-stage external review for routine reasoning;
- Text Review or Visual Review is broken after migration;
- task 050 starts before this migration is integrated.

## Pass 2 — Reality

Executor must read the latest main of both repositories before implementation.

### AI_Skills_Collection verified starting points

Current main policy:

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

At Plan freeze, the generic text and visual workflows still contain paid `push` triggers. Text Review still permits `OPENAI_REVIEW_API_KEY || OPENAI_VISUAL_REVIEW_API_KEY`. These are migration targets, not acceptable final behavior.

### Bridge Kit

Read current `main`, AGENTS, Text Review / Visual Review implementation, Responses API request construction, retry behavior, and any usage/result schemas before editing. Bridge Kit owns generic transport/model-call mechanics; AI_Skills owns consumer policy and task planning.

## Pass 3 — Alternatives

### A. Rely only on OpenAI Project hard limit / RPM

Rejected. Platform limits are the final circuit breaker, not a per-task budget. Multiple concurrent tasks can still consume the project budget.

### B. Query organization Costs API before each call

Rejected as runtime gating. It is asynchronous/aggregated and would require stronger organization credentials than review workflows should possess.

### C. Persistent per-task worst-case reservation + platform limits

Selected.

Each paid request is preflighted using the exact request input token count and bounded maximum output. Worst-case cost is reserved persistently before sending. Reservations are never automatically refunded. Platform Terra-only allowlist, 10 RPM / 100k TPM, and USD 10 monthly hard limit remain external safety layers.

## Pass 4 — Red team

Actively test:

- two concurrent/restarted workflows targeting the same campaign;
- a workflow rerun after a failed request;
- transient 429 versus `credit_balance_exhausted` / spend-limit errors;
- malformed/missing pricing config;
- model ID mismatch from the Terra-only contract;
- text and image-input token preflight;
- paid call count exhausted with money remaining;
- budget exhausted with call slots remaining;
- evidence writeback triggering another paid run;
- missing secret on explicit manual review;
- Visual Review trying to use any generation/tool capability;
- old specialized presentation workflows bypassing the central budget guard.

## Pass 5 — Execution contract

### 1. Planner / GPT contract

Update the Reviewed Handoff Planner contract so any Plan containing paid external review must explicitly freeze:

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

The Planner must reject routine per-stage paid review when host-model reasoning + deterministic checks suffice.

Do not create a new workflow state merely for cost control.

### 2. Executor contract

Update Executor guidance to refuse any paid invocation that lacks the frozen budget context or violates `docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md`.

### 3. Shared Bridge Kit budget guard

Prefer one generic implementation used by both Text Review and Visual Review rather than separate ad-hoc consumer calculators.

The generic guard must support at least:

```text
task_key / campaign_id
model_id
campaign_budget_usd = 0.50 default
max_paid_calls = 2 default
per_call_worst_case_usd = 0.25 default
max_output_tokens
pricing identity / verified price table
persistent reservation ledger
```

Before sending a paid Responses request:

1. build the exact request;
2. count exact input tokens using the provider-supported Responses input-token count path, including image inputs when present;
3. calculate worst-case cost using uncached input plus bounded max output;
4. validate model/pricing identity;
5. atomically/serially reserve the worst-case amount and one call slot in the task campaign;
6. only then send the request.

Reservation is not automatically refunded on failure, shorter output, retry, rerun or restart.

Use a per-campaign concurrency/locking mechanism appropriate to the actual GitHub/Bridge Kit execution path so two concurrent runs cannot both spend the same remaining budget.

Do not use Organization Admin API credentials.

### 4. Current Terra price/config boundary

Current reviewed baseline is:

```text
model: gpt-5.6-terra
input: USD 2 / 1M tokens
cached input: USD 0.20 / 1M tokens
output: USD 12 / 1M tokens
```

Source must be recorded as official OpenAI model documentation with a reviewed date. Runtime preflight uses uncached input. Unknown/stale/mismatched model pricing must fail closed rather than guess.

Do not silently switch to Luna/Sol/another model to make a request fit the budget.

### 5. Retry classification

Default automatic paid retry count is zero.

Billing/quota errors including at least:

```text
credit_balance_exhausted
project_spend_limit_exceeded
organization_spend_limit_exceeded
organization_usage_limit_exceeded
```

must fail immediately.

If a future bounded transient retry is implemented, it consumes the same campaign call slot/reservation and cannot reset budget.

### 6. Workflow triggers

Generic Text Review and Visual Review paid jobs must be `workflow_dispatch` / equivalent explicit bounded invocation only.

Remove paid `push` triggers. Ordinary CI may validate manifests/budgets without calling Terra.

Specialized presentation visual-review workflows are already manual at Plan freeze, but must still be audited so they cannot bypass the same budget guard.

### 7. Secret migration

Keep separate repository secret names:

```text
OPENAI_REVIEW_API_KEY
OPENAI_VISUAL_REVIEW_API_KEY
```

They may point to the same new `AI_Research_Review` project-scoped API key.

Remove cross-secret fallback. Missing secret during an explicit paid review must fail closed with a clear non-secret message; it must not silently PASS/SKIP as if review occurred.

Never print secret values.

The Executor may verify only `PRESENT/MISSING`. If the new project-scoped key is not yet configured, stop at one explicit credential handoff and give the user the exact GitHub secret names to update; do not request the value in chat and do not use an old archived-project key as fallback.

### 8. Model variables

Audit `OPENAI_TEXT_REVIEW_MODEL` and `OPENAI_VISUAL_REVIEW_MODEL`. Final production review must resolve to `gpt-5.6-terra` under the new project allowlist. Do not leave a stale model variable that makes the new key fail unexpectedly.

### 9. Visual boundary

Visual Review uses Terra image input only. No image generation, web search, file search, computer use or other paid tool is part of review.

`images/min` platform capacity is not the repository budget. Image inputs must be included in the exact request token preflight.

### 10. Tests before live spend

Before any live OpenAI call, pass deterministic tests proving at minimum:

- paid push triggers are absent;
- text/visual secret fallback is absent;
- Planner and Executor policy references are active;
- max calls / per-call / campaign budget validation;
- persistent reservation survives rerun/restart;
- concurrent same-campaign reservation cannot double-spend;
- request is blocked before send when next worst-case cost exceeds remaining budget;
- quota/billing error has zero automatic retry;
- model mismatch / unknown pricing fail closed;
- Text Review request path still constructs successfully;
- Visual Review image-input path still constructs successfully and has no image-generation/tool capability.

### 11. Live migration smoke

Only after deterministic tests pass and the user has configured the new project-scoped GitHub review secret(s), run a tiny public-safe live smoke for:

1. Text Review;
2. Visual Review with one small public-safe image.

Use one migration campaign with the same canonical max 2 calls / USD 0.50 reserved budget. Each request must remain under USD 0.25 worst-case.

Do not use private 050 artifacts for infrastructure smoke.

### 12. Integration / 050 gate

After Bridge Kit companion and AI_Skills consumer migration both pass, pin the exact Bridge Kit commit in AI_Skills, run CI, then integrate the migration to `main`.

Only after that integration may task `050_writing_style_host_codex_runtime` advance from `PLAN_FROZEN` into execution. Rebase/merge current main policy and migration changes into the 050 branch before executing it.

## Release decision

Repository bump decision: `NONE` during migration implementation.

This is infrastructure safety/compatibility work. Re-evaluate release/version only if existing public install/runtime behavior requires a formal release under the repository's canonical version policy.
