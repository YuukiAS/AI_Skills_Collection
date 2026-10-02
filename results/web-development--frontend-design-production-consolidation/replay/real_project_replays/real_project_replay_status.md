# Real-Project Replay Status

Status: `PASS_COMPATIBILITY_ONLY`

Task key: `web-development--frontend-design-production-consolidation`

Candidate plugin replay commit: `df01fac271e030f9259a1510034380e2ec422f76`

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

## Replay Authorization And Run

The user explicitly authorized this bounded provider transmission for the frozen
Bobbio/Lucerna/Asteria files listed in the manifest. The replay was run with:

```bash
python scripts/candidate_plugin_replay.py replay \
  --plugin web-development \
  --candidate-commit 2bd1a3fbba5254a4fe6dbfce752287dd8380e403 \
  --task results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_task.md \
  --input results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_freeze_manifest.json \
  --input results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_rubric.md
```

Run result:

- Run id: `20260928T032921Z-2135985`
- Actual plugin consumption: `proven=true`, event `item.started`, line index `8`
- Candidate selector: `web-development@ai-skills-candidate`
- Runtime version: `codex-cli 0.153.4`
- Child stderr: empty

Repo-safe outputs:

```text
3a58facb4f957c3e7efd79878ab27c7beb7a56a642c1aac14de8eb0aad0123e7  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.md
37ea0eb88308c6726ffde400aaf4b15c9a8b803ea5a666786665b02f85381a13  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.json
dbfff9c3b25176c907327fdc1d6ca8ab38ba23574409f827a0bfb5d4015cb47a  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_source_consumption.json
2936acecf0ad2ed6d7c8c3b25cf0afa2fed5b44b7f295ee6bc9198cd2e7667c8  results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_run.json
```

The freeze manifest was created before the final resume-command evidence commit
and declares candidate commit `fbf70ed65e6d5ff1be69135443522c4c4d7e58a8`.
The actual replay installed candidate commit
`df01fac271e030f9259a1510034380e2ec422f76`. The intervening commits changed only
task evidence/status files, not the generated `web-development` payload.

## Attribution Result

- Bobbio: `COUNTS_AS_COMPATIBILITY=true`, `COUNTS_AS_PLUGIN_CAPABILITY=false`
- Lucerna: `COUNTS_AS_COMPATIBILITY=true`, `COUNTS_AS_PLUGIN_CAPABILITY=false`
- Asteria: `COUNTS_AS_COMPATIBILITY=true`, `COUNTS_AS_PLUGIN_CAPABILITY=false`

All three prove compatibility/regression only. No project supplies plugin
capability evidence beyond its repo-local rules and historical evidence.
`web-development` maturity remains `unclassified`.

## Requested Authorization Envelope

The replay used only the authorized envelope:

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
