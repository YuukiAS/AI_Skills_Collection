# Final Terra Review Blocker for C6

Task: `055_clear_writing_release_convergence`

Date: `2026-09-16`

Status: `NEEDS_GPT_PLANNER`

Failure attribution: `WORKFLOW_DEFECT`

## Candidate And Gate State

```text
FINAL_CANDIDATE_COMMIT = 79d620a0c60cdd086dd5828c8686bac843291cda
pre_final_critic = PASS
G7 fresh = 3/3 PASS
Terra final review = NOT_RUN
```

The blocker was found after G7 passed and before any final Terra request was
sent. No OpenAI paid review call was dispatched for this final C6 gate.

## Frozen 055 Paid Envelope

The frozen Goal / Plan authorize exactly one final Terra Text Review with:

```text
model = gpt-5.6-terra
max paid calls = 1
automatic paid retries = 0
per-call worst-case ceiling <= USD 0.25
campaign ceiling <= USD 0.25
credential = existing GitHub Actions OPENAI_REVIEW_API_KEY only
transport = POST /v1/responses/input_tokens, then POST /v1/responses
store = false
tools = none
```

Allowed Terra-visible content is final Deep Research candidate text,
public-safe fresh candidate text, and frozen rubric. Private source,
intermediates, repo logs, credentials, Meaning Map, and Reader Plan remain
forbidden.

## Observed Consumer Contract

The repository's current Text Review consumer is:

```text
.github/workflows/ai-bridge-text-review.yml
```

That workflow uses the installed Bridge Kit command:

```text
ai-bridge text-review run
```

Read-only inspection of the installed local Bridge Kit implementation showed:

```text
file = /overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit/ai_bridge_kit/paid_review.py
DEFAULT_MAX_PAID_CALLS = 2
DEFAULT_CAMPAIGN_RESERVED_COST_HARD_CEILING_USD = Decimal("0.50")
DEFAULT_PER_CALL_WORST_CASE_CEILING_USD = Decimal("0.25")
DEFAULT_AUTOMATIC_PAID_RETRIES = 0
DEFAULT_MAX_OUTPUT_TOKENS = 4096
```

The same implementation requires an existing budget state contract to equal
`default_contract()` when it loads the ledger, and `reserve_paid_review_call()`
checks reservation count and cumulative campaign ceiling against the same
default constants. The `ai-bridge text-review encrypt --help` and
`ai-bridge text-review run --help` interfaces expose no argument for overriding
`max_paid_calls` or `campaign_reserved_cost_hard_ceiling_usd`.

Therefore the current canonical Text Review path can enforce the per-call
`USD 0.25` ceiling, but its durable receipt/ledger contract remains the generic
AI Bridge default of `2 calls / USD 0.50 campaign`, not the frozen 055
`1 call / USD 0.25 campaign`.

## Why This Stops Certification

Running Terra through the current consumer would create a paid-review campaign
whose recorded contract is broader than the 055 frozen authorization. Even if
only one call were actually dispatched, the campaign receipt would still not
bind the task to the required max call count and campaign ceiling.

Narrowing that behavior would require a consumer/workflow repair to the paid
review budget contract handling. The current 055 authorization explicitly
forbids modifying Bridge Kit and does not authorize creating a new paid-review
state/schema/ledger or alternate provider/credential path.

## Recovery Boundary

Do not run Terra until Planner/Critic/user authorize a safe recovery. Valid
recovery likely needs one of the following:

- an approved Bridge Kit / Text Review consumer capability to honor a stricter
  task-local paid campaign contract, or
- an explicit Planner/user decision that the generic `2 calls / USD 0.50`
  campaign contract is acceptable for this final 055 review.

The second option changes the frozen paid envelope and therefore cannot be
assumed by Executor.

## Preserved Evidence

G7 public evidence is already committed and pushed:

```text
results/055_clear_writing_release_convergence/G7_FRESH_EXECUTION_C6.md
```

Final Terra was not run, no paid reservation was intentionally created for 055,
and no final `TEXT_REVIEW.json` exists for this task at this point.
