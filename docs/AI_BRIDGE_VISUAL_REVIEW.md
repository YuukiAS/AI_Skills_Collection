# AI Bridge Visual Review

Visual Review is a shared optional evidence producer for Reviewed Handoff and Agent-Flow. It is not a new GPT role and it does not give Planner, Critic, Controller, Verifier, Executor, Scheduled GPT, local Codex, or local watchers access to an OpenAI API key.

Default live execution belongs in GitHub Actions:

```text
trusted branch push / workflow_dispatch
→ render or collect public-safe visual inputs
→ ai-bridge visual-review run
→ results/<task_key>/visual_review/VISUAL_REVIEW.json
→ existing Reviewer / Planner / Final Critic reads tracked evidence
```

The installed workflow installs the canonical Bridge Kit Git source pinned to
the ref rendered at install time. It does not vendor-copy `ai_bridge_kit/` into
the consumer repository and does not run `pip install -e .` against the
consumer project.

Use the repository secret name `OPENAI_VISUAL_REVIEW_API_KEY`. In the workflow, map it only inside the visual review job:

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_VISUAL_REVIEW_API_KEY }}
```

The model name is not secret. Set `OPENAI_VISUAL_REVIEW_MODEL` as a GitHub Actions variable or plain environment variable when the default model should be changed.

Recommended OpenAI setup:

```text
OpenAI Project: AI Bridge Visual Review
one restricted project-scoped key per repository
```

Default privacy policy is `PUBLIC_SAFE_ONLY`. Do not upload patient images, private clinical data, unpublished research images, credentials, private screenshots, or proprietary assets unless the project profile or task manifest contains explicit external upload authorization.

Preflight:

```bash
ai-bridge visual-review preflight --target <repo>
```

This checks whether visual review is configured, whether a GitHub workflow references the standard secret name, and, when `gh` is available and logged in, whether `gh secret list` shows `OPENAI_VISUAL_REVIEW_API_KEY`. It never reads the secret value.

Generated evidence must stay under the repository-relative path
`results/<task_key>/visual_review/**`. The workflow ignores
`results/**/visual_review/**` push changes so an evidence-only commit does not
retrigger the visual review job.
