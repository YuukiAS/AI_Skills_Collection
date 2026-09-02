# 047 Isolated Production-Like Replay Evidence

Recorded at: `2026-09-01T20:49:41-04:00`

Implementation commit: `ade5a1f653f88df07eb0c70edfd016c744b1611a`

Policy clarification commit: `a05e4a67`

## Isolation Boundary

No current live global Codex Marketplace installation, plugin cache, or
session-consumed plugin state was modified.

The replay used a task-local Codex environment:

- `CODEX_HOME`:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/codex-home`
- `HOME`:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/home`
- `XDG_CACHE_HOME`:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/cache`
- `XDG_CONFIG_HOME`:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/config`

The local `/overflow/htzhu/mingcheng_new/bin/codex` wrapper was not used for
this isolated verification because it unsets `CODEX_HOME`-related variables.
The underlying Codex JS entrypoint was used directly:

`/overflow/htzhu/mingcheng_new/conda/lib/node_modules/@openai/codex/bin/codex.js`

## Installation Mechanism

The isolated environment used the normal Marketplace/plugin commands:

- `plugin marketplace add /tmp/AI_Skills_Collection_047 --json`
- `plugin add writing-style@yuukias-ai-skills --json`
- `plugin list --json`

Observed installed plugin:

- plugin id: `writing-style@yuukias-ai-skills`
- installed version: `0.1`
- enabled: `true`
- source: `/tmp/AI_Skills_Collection_047/plugins/codex/plugins/writing-style`
- installed cache:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/codex-home/plugins/cache/yuukias-ai-skills/writing-style/0.1`

The installed cache contains the generated `scientific-rewrite` payload under:

`.../skills/scientific-rewrite/SKILL.md`

## Payload Identity

The canonical generated payload and the isolated installed cache copy matched:

```text
d6a5821c7f635a459a40d99c8e5ec0b87f459f52871056a65fc8c2b597b844b2  /tmp/AI_Skills_Collection_047/plugins/codex/plugins/writing-style/skills/scientific-rewrite/SKILL.md
d6a5821c7f635a459a40d99c8e5ec0b87f459f52871056a65fc8c2b597b844b2  /overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/codex-home/plugins/cache/yuukias-ai-skills/writing-style/0.1/skills/scientific-rewrite/SKILL.md
```

## Normal Invocation Probe

The routing probe used an ordinary user prompt, without a skill path, hidden
artifact id, internal router name, benchmark helper, or test keyword:

```text
把这份中文科研报告说人话一些，但不要改变事实、数字、公式、引用、专业术语和结论强度。
```

`codex debug prompt-input` for that fresh isolated session showed:

- `writing-style:scientific-rewrite` present
- `writing-style:chinese-prose` present
- `writing-style:writing-fidelity` present
- `scientific-rewrite` path present from the isolated plugin cache:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/codex-home/plugins/cache/yuukias-ai-skills/writing-style/0.1/skills/scientific-rewrite/SKILL.md`

This proves the ordinary production-style entrypoint exposes the installed
`scientific-rewrite` route through `writing-style` in a fresh isolated session.
It is routing evidence, not a model-produced rewritten artifact.

## Model Invocation Status

The isolated fresh session was probed with `codex exec --ephemeral` and a
minimal ordinary prompt. The first attempt inherited proxy variables and failed
with connection refused. Retrying with `http_proxy`, `https_proxy`, and
`all_proxy` variants unset reached the OpenAI endpoint but failed with:

```text
401 Unauthorized: Missing bearer or basic authentication in header
```

No model-produced artifact was generated. The isolated `CODEX_HOME` had no
model credentials, and local environment checks found:

```text
OPENAI_API_KEY=ABSENT
OPENAI_REVIEW_API_KEY=ABSENT
OPENAI_VISUAL_REVIEW_API_KEY=ABSENT
```

No live auth token or secret was copied from the real Codex home. This leaves
the model-produced production replay artifact pending, while preserving the
user's live-global non-mutation boundary.

## Planner Revision 1 Auth Replay Attempt

Recorded at: `2026-09-01T22:20:05-04:00`

After Planner revision 1, Executor performed only non-secret auth checks:

- `codex login status` reported an existing ChatGPT login.
- the active session `CODEX_HOME` was
  `/overflow/htzhu/mingcheng_new/.codex-homes/Longleaf_Connection_Bridge`;
- an `auth.json` file was present there, but its contents were not read or
  printed.

Executor copied that file once into the task-local isolated Codex home with
file mode `0600`, as authorized by Planner revision 1. The subsequent fresh
isolated `codex exec --ephemeral` replay request was rejected by the execution
approval layer before running, because it would use the copied Codex login to
send the private 044 report to the external OpenAI endpoint.

Executor did not retry through another path, did not invoke a source-tree skill
as a substitute production replay, did not modify live global plugin state, and
did not send the private 044 artifact to the model endpoint through this
attempt. The task-local `auth.json` copy was then removed; a post-removal check
reported `auth_copy_removed`.

No 044 candidate rewrite artifact was produced by this attempt. Therefore the
required encrypted Text Review payload and manifest remain pending.

## User Authorization Receipt and Final Replay Boundary

Recorded at: `2026-09-01T22:20:05-04:00`

The user then explicitly authorized one-time replay within this exact scope:

- artifact scope: 044 known-regression report;
- provider: OpenAI/Codex;
- purpose: 047 isolated production-entrypoint regression replay and required
  review preparation;
- credential mode: task-local temporary `auth.json` copy;
- prohibited: live global plugin cache mutation, committing/pushing auth,
  tokens, or private 044 plaintext, and printing secrets.

Executor re-created the task-local `auth.json` copy with file mode `0600` and
retried the same fresh isolated `codex exec --ephemeral` production-entrypoint
command. The execution approval layer rejected the command again before it ran,
stating that sending the private 044 report to the external OpenAI endpoint is
disallowed by tenant policy even with the user's explicit authorization.

Executor did not attempt a workaround or indirect execution. The task-local
auth copy was removed again; a post-removal check reported
`auth_copy_removed`.

Final status for this path:

- isolated Marketplace install: verified;
- generated payload identity: verified;
- ordinary prompt routing evidence: verified;
- fresh model-produced 044 artifact: not produced;
- private 044 sent by this final attempt: false;
- live global plugin/cache mutation: false.

## Terminalization Check

Recorded at: `2026-09-01T22:45:59-04:00`

After the final replay boundary was recorded and pushed, Executor checked the
Reviewed Handoff state transition path:

- `transition plan` returned `next_action=HUMAN_PLAN_DECISION` and
  `next_state=AWAIT_HUMAN_DECISION`;
- `transition apply` refused that terminal state because
  `results/047_writing_style_scientific_rewrite_architecture/text_review/text_inputs.json`
  is missing.

Executor did not create a placeholder manifest or payload because the frozen
Plan requires the manifest to bind a real model-produced 044 candidate artifact,
and that artifact does not exist under the current execution policy.
