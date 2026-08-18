# Review 000 Short Task

audited_status: NEEDS_EVIDENCE
promotion_decision: BLOCKED

Allowed `audited_status` values:

- `AUDITED_GO`
- `NEEDS_EVIDENCE`
- `NEEDS_REVISION`
- `NEEDS_HUMAN_APPROVAL`
- `NEEDS_GPT_PLANNER`
- `STOP`

Allowed `promotion_decision` values:

- `PROMOTE`
- `BLOCKED`
- `HUMAN_APPROVAL_REQUIRED`
- `RETURN_TO_EXECUTOR`
- `RETURN_TO_GPT_PLANNER`
- `STOP`

## Task Goal

Restate the task goal and promotion gate from the task file.

## Claimed Completion

Summarize the executor's self-assessed status and claims without accepting them
yet.

## Audited Status

State the controlled decision enum. Do not write vague decisions such as
`looks good`, `probably done`, or `mostly fine`.

## Claim Ledger

| Claim | Auditor judgment | Evidence | Notes |
| --- | --- | --- | --- |
| `claim.example` | `SUPPORTED` | `path:line` or command exit status | concise note |

Allowed claim judgments:

- `SUPPORTED`
- `PARTIAL`
- `UNSUPPORTED`
- `CONTRADICTED`

## Supported Claims

- claim:
- evidence:

## Partial Claims

- claim:
- missing evidence:

## Unsupported Claims

- claim:
- reason:

## Contradicted Claims

- claim:
- contradiction:

## Missing Evidence

- evidence needed:
- why it matters:

## Permission Boundary Check

- allowed actions respected:
- forbidden actions touched:
- network/upload/delete/high-risk actions:
- human approval required:

The auditor must remain read-only. Do not fix code, generate missing artifacts,
or continue execution unless a new execution task explicitly authorizes it.

## Promotion Decision

- promotion_decision:
- blocked_promotion_reason:
- next_allowed_action:

For medium/high risk tasks, no promotion, release, deployment, commit, push, or
high-cost expansion should happen without supported claims and a passing audit,
unless the task explicitly waives review.

## Next Allowed Action

Choose exactly one:

- `STOP`
- `REQUEST_EVIDENCE`
- `REQUEST_REVISION`
- `REQUEST_HUMAN_APPROVAL`
- `PROMOTE_AND_SYNC_REMOTE`
- `RETURN_TO_GPT_PLANNER`
