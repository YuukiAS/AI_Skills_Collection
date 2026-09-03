---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: infra_paid_review_safety_migration_20260903
---

# Paid external review safety migration

## User request

Before executing task 050, harden the repository-wide paid external review path so future GPT Planner / Codex / GitHub Actions cannot silently turn routine intermediate work into repeated paid API review calls.

The user has created a new OpenAI API project for independent review with the intended platform controls:

```text
project: AI_Research_Review
allowed model: gpt-5.6-terra only
project rate override: 10 RPM
project rate override: 100,000 TPM
monthly project spend: USD 10 hard limit
```

Repository policy is already frozen in:

```text
docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md
AGENTS.md §8.3.1
```

## Required outcome

1. GPT Planner cannot freeze a Plan that casually uses paid external model calls for ordinary generation/intermediate reasoning/self-review.
2. Codex / workflow runtime cannot accidentally generate unbounded paid review calls.
3. Text Review and Visual Review both remain usable as explicit independent final QA.
4. Ordinary push / ordinary CI never triggers a paid model call.
5. Text and visual review secrets do not silently fall back into one another.
6. A task-local persistent worst-case reservation budget enforces the canonical defaults: max 2 paid calls, USD 0.50 campaign reserved-cost ceiling, USD 0.25 worst-case per call, automatic paid retry 0.
7. Billing/quota failures fail immediately with no backoff loop.
8. The migration preserves private artifact safety and does not print or commit secret values.
9. Task 050 remains frozen and must not execute until this migration is integrated and the new project-scoped review secret(s) are configured.

## Explicit scope

Audit both owners of the current path:

- `YuukiAS/GPT_Codex_AI_Bridge_Kit` for generic Text Review / Visual Review runtime and budget enforcement;
- `YuukiAS/AI_Skills_Collection` for Planner/Executor contracts, workflows, manifests, tests, and consumer wiring.

Do not start 050 writing-style implementation in this task.
