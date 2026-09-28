# Candidate Plugin Replay Status

Status: `RUNTIME_READY_COMMIT_REQUIRED`

Prepared replay route:

- Marketplace name: `ai-skills-candidate`
- Plugin selector: `web-development@ai-skills-candidate`
- Plugin version: `0.3`
- Runtime: `.local-runtime/codex/0.153.4/bin/codex`
- Runtime version: `codex-cli 0.153.4`
- Runtime binary SHA256: `56ef98ab4032d317ab26e9b5e5a175650717351edb16ed9cde0cb6d1734d62da`

Rejected live/global command, retained as negative evidence:

```bash
codex plugin marketplace add /tmp/ai-skills-candidate-marketplace-CNFQXV --json
```

Result: auto-review rejected the command because it mutates current live/global Codex marketplace configuration.

Safer route found:

```bash
python scripts/candidate_plugin_replay.py replay \
  --plugin web-development \
  --candidate-commit <implementation-commit> \
  --task results/web-development--frontend-design-production-consolidation/replay/frontend_candidate_replay_task.md \
  --input results/web-development--frontend-design-production-consolidation/candidate_visible_regressions/scenarios.json
```

This helper uses the pinned repo-local runtime and temporary `@ai-skills-candidate` identity process-locally, then cleans up the candidate. It does not modify the live/global Codex plugin configuration.
