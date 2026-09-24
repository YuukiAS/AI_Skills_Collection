# FB-G4 / FB-G5 Evidence

## Candidate Pair

- Bridge repo: `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- Bridge candidate commit: `a41c2e32c630aaf2a200ca336f04c4ea31650786`
- Bridge runtime: `/home/yuukias/conda/bin/ai-bridge`
- AI_Skills repo: `YuukiAS/AI_Skills_Collection`
- AI_Skills implementation candidate commit:
  `c17214449d8ca8761664ff15d49140c692a0fcb1`
- Repository version: `5.1.1`
- workflow-core version: `0.4`

## FB-G4

Result: `PASS_WITH_NOTE`

- Remote branch publication:
  `refs/heads/reviewed/workflow-core--reviewed-first-bootstrap-normal-entry`
  equals `c17214449d8ca8761664ff15d49140c692a0fcb1`.
- Remote-only/idempotent resume command:
  `ai-bridge reviewed-handoff materialize-worktree --target /home/yuukias/AI_Skills_Collection --task-key workflow-core--reviewed-first-bootstrap-normal-entry --expected-repo YuukiAS/AI_Skills_Collection --expected-worktree /home/yuukias/AI_Skills_Collection-workflow-core--reviewed-first-bootstrap-normal-entry --expected-base-ref origin/main --mode resume`
- Output: `OK already materialized: /home/yuukias/AI_Skills_Collection-workflow-core--reviewed-first-bootstrap-normal-entry`
- Canonical main task metadata path absent after the command:
  `/home/yuukias/AI_Skills_Collection/automation/reviewed_handoff/tasks/workflow-core--reviewed-first-bootstrap-normal-entry`
- Note: a direct local-metadata resume attempt with the reviewed worktree as
  `--target` was rejected by Bridge as `WORKTREE_PATH_IS_CANONICAL_CHECKOUT`.
  This was a misuse check, not a product fallback.

## FB-G5

Result: `PASS`

Candidate replay command:

```text
python scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit c17214449d8ca8761664ff15d49140c692a0fcb1 --task results/workflow-core--reviewed-first-bootstrap-normal-entry/fb_g5_candidate_replay_task.md --input results/workflow-core--reviewed-first-bootstrap-normal-entry/fb_g5_routing_scenarios.json
```

Replay identity:

- plugin id: `workflow-core@ai-skills-candidate`
- version: `0.4`
- runtime: `codex-cli 0.153.4`
- actual consumption: `proven=true`, event `item.started`, line `4`
- run artifact: `.local-runtime/candidate-plugin-replay/runs/20260924T110212Z-2567217/run.json`
- `run.json` sha256:
  `e834e715f59aff284b9871ae86d4a68a3b61084b4896b585847ebac274d36717`
- `plugin-add.json` sha256:
  `9707ba3e29da937a8b316e0cb034ca3359845d179673dea1ead80e4ab80bb539`
- routing-table sha256:
  `3f7932c6e8e4b80dd00db5efbf97633bb017ae4689c3674b0db2bac5c807e2d4`

Loaded candidate routing output:

| Scenario | Normal entry | Raw Git fallback |
|---|---|---|
| `missing` | `ai-bridge reviewed-handoff task bootstrap` | No |
| `existing_local` | `ai-bridge reviewed-handoff materialize-worktree --mode resume` | No |
| `remote_only` | `ai-bridge reviewed-handoff materialize-worktree --mode resume` | No |
| `bridge_missing_or_old` | no available entry; fail before substantive implementation | No |
