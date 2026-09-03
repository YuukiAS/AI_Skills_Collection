# AI Bridge Visual Review

Visual Review is a shared optional evidence producer for Reviewed Handoff and Agent-Flow. It is not a new GPT role and it does not give Planner, Critic, Controller, Verifier, Executor, Scheduled GPT, local Codex, or local watchers access to an OpenAI API key.

Default live execution belongs in an explicit GitHub Actions dispatch:

```text
workflow_dispatch with a task-local manifest
→ render or collect public-safe visual inputs
→ ai-bridge visual-review run
→ results/<task_key>/visual_review/VISUAL_REVIEW.json
→ existing Reviewer / Planner / Final Critic reads tracked evidence
```

The installed workflow installs the canonical Bridge Kit Git source pinned to
the ref rendered at install time. It does not vendor-copy `ai_bridge_kit/` into
the consumer repository and does not run `pip install -e .` against the
consumer project.

For Reviewed Handoff push events, the workflow resolves task-local visual
review targets from tracked task state instead of repository-level fixed
manifest variables. A task is eligible only when its
`automation/reviewed_handoff/tasks/<task_key>/CURRENT.json` declares
`visual_review_required=true`, is in `READY_FOR_GPT_REVIEW`, has
repository-relative `visual_review_manifest_path` and
`visual_review_evidence_path`, and the manifest binds
`workflow_type=reviewed_handoff`, the same `task_key`, and the same
`identity_bindings.implementation_commit`. Zero eligible tasks are a normal
no-op. Exactly one eligible task runs live review. Multiple eligible tasks or
manifest identity conflicts fail closed.

`workflow_dispatch` is the only live paid Visual Review route in AI_Skills.
Ordinary push may publish manifests, renders or evidence, but must not call
OpenAI.

Use the repository secret name `OPENAI_VISUAL_REVIEW_API_KEY`. In the workflow, map it only inside the visual review job:

```yaml
env:
  OPENAI_VISUAL_REVIEW_API_KEY: ${{ secrets.OPENAI_VISUAL_REVIEW_API_KEY }}
```

The production Visual Review model is `gpt-5.6-terra`. AI_Skills workflows pin
this explicitly; unknown pricing or model mismatch must fail closed.

Recommended OpenAI setup:

```text
OpenAI Project: AI_Research_Review
one restricted project-scoped key per repository
```

Default privacy policy is `PUBLIC_SAFE_ONLY`. Do not upload patient images, private clinical data, unpublished research images, credentials, private screenshots, or proprietary assets unless the project profile or task manifest contains explicit external upload authorization.

Preflight:

```bash
ai-bridge visual-review preflight --target <repo>
```

This checks whether visual review is configured, whether a GitHub workflow references the standard secret name, and, when `gh` is available and logged in, whether `gh secret list` shows `OPENAI_VISUAL_REVIEW_API_KEY`. It never reads the secret value.

Generated evidence must stay under the repository-relative path
`results/<task_key>/visual_review/**`. The adjacent
`results/<task_key>/paid_review_budget.json` records the persistent worst-case
reservation receipt: max 2 paid calls, USD 0.50 campaign ceiling, USD 0.25
per-request ceiling, and zero automatic paid retry. Visual Review sends image
inputs for review evidence only; it must not enable image generation, web
search, file search, computer use or other paid tools.
