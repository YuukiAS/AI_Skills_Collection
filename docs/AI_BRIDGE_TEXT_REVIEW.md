# AI Bridge Text Review

Text Review is a shared optional evidence producer for Reviewed Handoff. It is
not a new GPT role. It lets a private UTF-8 Markdown/plain-text artifact be
reviewed by OpenAI through GitHub Actions without committing plaintext.

The production path is:

```text
private local text
-> age public-key encryption
-> encrypted payload + manifest committed to the reviewed task branch
-> GitHub Actions decrypts in a temporary runner directory
-> OpenAI Responses API with store=false reads the complete plaintext
-> results/<task_key>/text_review/TEXT_REVIEW.json
```

Tracked files may include the public age recipient, encrypted payload, manifest
and `TEXT_REVIEW.json`. Tracked files must never include the age private
identity, plaintext artifact or OpenAI API key.

Install:

```bash
ai-bridge text-review install --target /path/to/project
```

Configure transport:

```bash
ai-bridge text-review configure --target /path/to/project --repo owner/name
```

This generates an age keypair, writes the private identity to the GitHub Secret
`AI_BRIDGE_PRIVATE_REVIEW_AGE_KEY` through `gh secret set`, writes the public
recipient to `automation/reviewed_handoff/private_text_review.age.pub`, and
does not print the secret value.

If `gh` permissions are unavailable, configure exactly this GitHub Secret
manually. Do not paste the secret into chat or commit it to the repository.

OpenAI key contract in AI_Skills CI is:

```text
OPENAI_REVIEW_API_KEY
```

Text Review must not fall back to `OPENAI_VISUAL_REVIEW_API_KEY`. The production
model is `gpt-5.6-terra`; AI_Skills workflows pin this explicitly so a stale
repository variable cannot redirect paid review to another model.

Live Text Review is manual-only. It may be run only through an explicit
`workflow_dispatch` target with a task-local campaign budget. Ordinary push,
manifest commits and evidence commits must not call OpenAI.

Encrypt a private artifact from the user machine:

```bash
ai-bridge text-review encrypt \
  --target /path/to/project \
  --task-key 044_example \
  --input /private/path/final.md \
  --output results/044_example/text_review/payload.age \
  --manifest results/044_example/text_review/text_inputs.json \
  --implementation-commit <commit> \
  --rubric "Read the complete artifact and decide whether it satisfies the frozen user-facing prose requirements." \
  --external-upload-authorization "User authorized private text review through OpenAI Responses API with store=false for this task."
```

The `TEXT_REVIEW.json` evidence contains SHA-256 bindings and structured
findings, not the private plaintext. The adjacent
`results/<task_key>/paid_review_budget.json` records the persistent worst-case
reservation receipt: max 2 paid calls, USD 0.50 campaign ceiling, USD 0.25
per-request ceiling, and zero automatic paid retry.

For a task whose frozen Plan authorizes a stricter initial campaign, the
manifest may add `paid_review_initial_contract` with only these fields:

```json
{
  "max_paid_calls": 1,
  "campaign_reserved_cost_hard_ceiling_usd": "0.25",
  "per_call_worst_case_ceiling_usd": "0.25",
  "automatic_paid_retries": 0
}
```

The values may only equal or narrow the default. Model, pricing, service tier,
reasoning, tools, cache policy and request safety remain Bridge Kit defaults.
Before a paid dispatch, run the zero-paid capability check:

```bash
ai-bridge text-review contract-preflight \
  --target . \
  --manifest results/<task_key>/text_review/text_inputs.json
```

The preflight sends no OpenAI request and creates no
`paid_review_budget.json` reservation.
