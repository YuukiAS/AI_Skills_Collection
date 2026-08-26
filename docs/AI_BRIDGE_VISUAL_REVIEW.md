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

`workflow_dispatch` remains the manual recovery/debug route and its explicit
`manifest` and `output` inputs take priority over automatic push resolution.

Use the repository secret name `OPENAI_VISUAL_REVIEW_API_KEY`. In the workflow, map it only inside the visual review job:

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_VISUAL_REVIEW_API_KEY }}
```

The production default Visual Review model is `gpt-5.6-terra`. Ordinary consumer repositories do not need to set a model variable. Set `OPENAI_VISUAL_REVIEW_MODEL` as a GitHub Actions variable or plain environment variable only when a project has an explicit quality, cost, permission, or model-freeze reason to override the shared default. An explicit CLI `--model` value takes priority over `OPENAI_VISUAL_REVIEW_MODEL`, which takes priority over the Bridge Kit shared default.

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
