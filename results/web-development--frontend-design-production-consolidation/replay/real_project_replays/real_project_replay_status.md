# Real-Project Replay Status

Status: `AWAITING_USER_AUTHORIZATION_FOR_PROVIDER_TRANSMISSION`

Task key: `web-development--frontend-design-production-consolidation`

Candidate plugin commit: `fbf70ed65e6d5ff1be69135443522c4c4d7e58a8`

## What Is Frozen

The G6 replay set is frozen to:

- Bobbio at `445d31e5d5408b2a39948ad1d98613f6eb31e742`
- Lucerna at `origin/main` / `b626c2ce998882941dba0f30a00ecf627cc740b5`
- Asteria at `f2fbbc3cd2edb3f005ae939f8d30637966256098`

Frozen replay files:

```text
3aee0029cabbea387a39e9b146a7230d2dc08b91096b745fe7d726c639a056ce  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_task.md
41c11b19c34f1f61ed9a632f650972f26e7af705f0bdace173151bb3ae910e1f  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_rubric.md
4903e20d19941eb5c64f6b9da56aadfb6971a3d7492766c67363ea27cb457457  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_freeze_manifest.json
```

The freeze manifest records locators and hashes only. It does not copy Bobbio,
Lucerna, or Asteria source text into this repository.

## Lucerna Source Resolution

Earlier preflight found the v0.3 Lucerna files missing at the stale local worktree
HEAD. A read-only `git fetch origin main` updated `origin/main` to
`b626c2ce998882941dba0f30a00ecf627cc740b5`, where the exact v0.3 files exist:

- `AGENTS.md`
- `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`
- `docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`
- `docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`

The Lucerna worktree remains dirty/behind and was not pulled, cleaned, reset, or
checked out.

## Why Replay Has Not Run

Running the G6 candidate replay would require the child Codex runtime to read
Bobbio/Lucerna/Asteria project documents and send relevant content to the model
provider for analysis. Auto-review rejected this operation because the current
user-visible authorization does not explicitly approve transmitting those
specific project documents to the provider.

No workaround was used. The next required action is an explicit user decision on
whether this bounded provider transmission is authorized.

If authorized, resume with this exact command from the reviewed worktree:

```bash
python scripts/candidate_plugin_replay.py replay \
  --plugin web-development \
  --candidate-commit 2bd1a3fbba5254a4fe6dbfce752287dd8380e403 \
  --task results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_task.md \
  --input results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_freeze_manifest.json \
  --input results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_rubric.md
```

After replay, copy only repo-safe summaries from the runtime output directory to
`results/web-development--frontend-design-production-consolidation/replay/real_project_replays/`.
Do not copy raw project source text into AI_Skills evidence.

## Requested Authorization Envelope

Authorize only the following, if approved:

- Data scope: the frozen files listed in `real_project_replay_freeze_manifest.json`
  from Bobbio, Lucerna, and Asteria.
- Provider path: the repo-local `scripts/candidate_plugin_replay.py` child Codex
  runtime using the current Codex model/provider.
- Purpose: G6 Frontend Design candidate replay and attribution only.
- Output scope: route/source-consumption summaries, attribution fields, hashes,
  and evidence limits under `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/`.
- No target project mutation, no checkout/pull/reset/clean in target projects,
  no full source-text copying into AI_Skills evidence, no fourth project, no paid
  reviewer/API beyond the normal Codex replay path.
