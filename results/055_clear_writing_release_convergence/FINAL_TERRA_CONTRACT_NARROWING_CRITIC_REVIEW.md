# 055 Clear Writing — Final Terra Contract Narrowing Recovery Critic Review

- Review stage: `RECOVERY_AMENDMENT`
- Decision: `PASS`
- Date: `2026-09-17`
- Target repo: `YuukiAS/AI_Skills_Collection`
- Task: `055_clear_writing_release_convergence`
- Reviewed task commit: `789e6dc28b8fec96ab82bb8ba6ea0dae96f99c5e`
- Final candidate: `C6 = 79d620a0c60cdd086dd5828c8686bac843291cda`
- Pre-final Critic: `PASS`
- G7 fresh: `3/3 PASS`
- Terra: `NOT_RUN`
- Paid call consumed: `0`
- Reservation created: `0`
- Blocker evidence: `results/055_clear_writing_release_convergence/FINAL_TERRA_REVIEW_BLOCKER_C6.md`

## 1. Scope and decision

PASS the Planner's minimal recovery amendment. The observed failure is a `WORKFLOW_DEFECT / CONSUMER_CAPABILITY_GAP`, not a Clear Writing product defect. The frozen 055 contract requires the initial paid campaign itself to be bounded to exactly one call and USD 0.25, while the current canonical Text Review consumer persists the generic initial contract of two calls / USD 0.50.

This review does not reopen C6, the Clear Writing architecture, G1–G8, A/B/C, the fresh batch, or the paid envelope. It approves only a generic Bridge Kit capability for monotone **initial campaign narrowing**, plus Text Review plumbing, focused tests, and a zero-paid contract-capability preflight.

## 2. Evidence reviewed

Latest AI_Skills main at review start: `7dbd0a5ce87f2a30ff9e8e7d2f8866365eaf40eb`.

Read current `AGENTS.md`, Planner/Critic contracts, `PLUGIN_CAPABILITY_GATE_POLICY.md`, `PAID_EXTERNAL_REVIEW_POLICY.md`, `.github/workflows/ai-bridge-text-review.yml`, `docs/AI_BRIDGE_TEXT_REVIEW.md`, frozen 055 Goal/Plan, G7 evidence, Terra blocker, and CURRENT.

Read current Bridge Kit paid-review/Text Review implementation and tests. AI_Skills currently pins Bridge Kit `5c894d98d3053c39cbda79cdbd0b8dfb4fbec4c0`; Bridge Kit current main is `cc7a6a3ea7a95d15d253821c50f2beda9bf221f9`. The intervening five commits do not modify the existing paid-review/Text Review implementation surface.

## 3. No mature existing no-fix path

No existing canonical path safely enforces the frozen 055 initial `1 call / USD 0.25` campaign:

- normal `ai-bridge text-review run` resolves the hard-coded default initial contract `2 / 0.50`;
- the current Text Review manifest/CLI exposes no initial max-call/campaign-ceiling override;
- pre-creating a narrower ledger is rejected by the existing exact-contract mismatch guard;
- the existing one-call `paid_review_extension` is a different recovery mechanism for a previously existing parent campaign and is not a valid substitute for a narrower initial campaign with zero prior reservation/call;
- dispatching the workflow only once does not make the persisted campaign contract one-call-safe against rerun/restart;
- implementing a direct OpenAI path in AI_Skills would duplicate the shared accounting/safety owner and is rejected;
- project/monthly spend controls are outer account/project limits, not a task-local max-call/campaign authorization contract.

Therefore a consumer capability repair is justified.

## 4. Correct owner and minimum mechanism

The budget-contract resolver/enforcer belongs in shared Bridge Kit `paid_review`, because Text and Visual Review already share the campaign ledger, pricing, reservation and accounting safety logic. However this recovery should wire the new optional narrowing contract into **Text Review only**. Do not expand Visual Review product behavior merely because the primitive is shared.

Minimal mechanism:

1. Add one reusable paid-review resolver for an optional initial task-local budget override. It may narrow only:
   - `max_paid_calls`;
   - `campaign_reserved_cost_hard_ceiling_usd`;
   - `per_call_worst_case_ceiling_usd`;
   - `automatic_paid_retries`.
2. Missing override resolves byte/semantically to the existing default contract.
3. Reject unknown override fields and every broader-than-default value. Model, pricing, service tier, reasoning, tools, cache and request safety remain fixed by the existing reviewed defaults.
4. The resolved full contract is the exact contract written to / compared against the existing `paid_review_budget.json`; no second ledger or schema is introduced.
5. Reservation limits, post-response actual-usage accounting, zero-billing handling and receipt generation must all preserve/use the same resolved initial contract. It is insufficient to narrow only the first reservation path and then reload the ledger as the generic default.
6. Existing-ledger contract mismatch remains fail-closed.
7. Text Review manifest/CLI may carry an optional backwards-compatible budget-contract field; no override remains fully backward compatible.
8. Add a zero-paid, zero-reservation contract-capability preflight that resolves and validates the intended contract and checks any existing ledger for compatibility without `/v1/responses`, without reservation, and preferably without requiring the final Terra artifact to exist. This is the early gate future tasks can run before fresh/final-paid evaluation.

No new AGENTS/policy rule is required. Bridge Kit's current paid-review policy already says the defaults apply unless a consumer Plan freezes a stricter user-approved override; the defect is that the runtime does not yet implement that stated capability. Update user-facing Text Review docs/changelog only as needed to document the supported interface.

## 5. Required regression boundary

Focused tests must prove at least:

- no override -> unchanged `2 calls / USD 0.50 / USD 0.25 per call / 0 retries`;
- 055-like initial override -> resolved and persisted ledger contract exactly `1 / 0.25 / 0.25 / 0`;
- max calls, campaign ceiling, per-call ceiling, retry count, unknown fields, model/pricing/request-safety expansion attempts -> fail closed;
- existing ledger with a different contract -> fail closed;
- post-response actual accounting and receipt continue successfully under a valid narrowed initial contract and retain that exact contract;
- zero-billing/error accounting does not silently reload the generic default;
- zero-paid contract preflight creates no reservation and sends no paid request;
- existing authorized one-call extension behavior remains unchanged;
- Text Review default behavior remains backward compatible.

## 6. AI_Skills consumer closure

After Bridge Kit implementation/tests PASS, AI_Skills may update only the exact Bridge Kit pin required by `.github/workflows/ai-bridge-text-review.yml` and directly related consumer docs/tests/evidence. Before pinning, compare the current `5c894d98...` pin to the new Bridge Kit commit and record that the pre-existing main delta did not change the paid-review/Text Review surface except for the approved narrowing repair; run the relevant AI_Skills Text Review/paid-review workflow regressions.

Then run a **zero-paid** 055-like contract-capability preflight proving the consumer resolves exactly `max_paid_calls=1`, `campaign ceiling=USD 0.25`, `per-call ceiling=USD 0.25`, `automatic retries=0`, with reservation count still zero. Do not run Terra in the implementation recovery step.

## 7. Preservation of C6 and G7

C6 and G7 `3/3 PASS` remain valid. The defect is downstream paid-review accounting/consumer infrastructure; no Terra request or reservation was made, and the repair must not alter C6, its payload, rubric, G7 inputs, outputs or evaluation decisions. Re-running fresh would add no legitimate evidence and would instead risk contaminating the frozen holdout history.

After the zero-paid consumer capability is proven, return to the 055 Planner to resume the already-approved Goal and decide the normal final-Terra dispatch. This PASS does not itself send or consume the paid call.

## 8. Independent external check

Current OpenAI model documentation still lists GPT-5.6 Terra at USD 2/M input, USD 0.20/M cached input and USD 12/M output, with the >272K long-context boundary. GitHub Actions documentation confirms manually dispatched workflows can accept typed inputs, so no daemon/service is needed to transport bounded task-local controls. OpenAI project limits remain outer project-level controls and do not substitute for a per-task persistent max-call/campaign contract.

## 9. PASS boundary

```text
RECOVERY_AMENDMENT_DECISION=PASS
FAILURE_ATTRIBUTION=WORKFLOW_DEFECT / CONSUMER_CAPABILITY_GAP
CLEAR_WRITING_PRODUCT_CHANGE=NO
C6_CHANGE=NO
G7_RERUN=NO
055_PAID_ENVELOPE_CHANGE=NO
BRIDGE_KIT_SCOPE=INITIAL_CAMPAIGN_NARROWING_ONLY
NEW_LEDGER_SCHEMA_STATE=NO
PAID_CALLS_AUTHORIZED_BY_IMPLEMENTATION_STEP=0
NEXT_AFTER_IMPLEMENTATION=055_PLANNER
```
