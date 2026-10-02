# G4 Normal Entry Trace

Final candidate commit: `671eb532e0ec949dc7889427379a1113cf7a6ea9`
Run id: `20261002T040924Z-756269`
Status: `PASS`

Command:

```text
python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g4_candidate_replay_task.md --input results/workflow-core--normal-entry-reliability/g4_capability_discovery_input.md
```

Replay identity:

- plugin id: `workflow-core@ai-skills-candidate`
- plugin version: `0.5`
- runtime: `codex-cli 0.153.4`
- actual consumption: `proven=true`, event `item.started`, line `6`

Tracked evidence:

| File | SHA256 |
|---|---|
| `g4_candidate_replay_task.md` | `9858804265b0c7ec9946e560189ebab6cad37ac5cbe31e6300d0adad7653f87e` |
| `g4_capability_discovery_input.md` | `db4745bf7c3286db46ae6a39be5d33aa7c2edf4fae09d6bc7d85a8208ccd259c` |
| `g4_candidate_replay_raw/run.json` | `d2d6323e419e8c6da25f70a7fac24a3c803dc623bc3ff02ba2ffb72457427b0f` |
| `g4_candidate_replay_raw/plugin-add.json` | `c61246482d14ff4186eb92f8747bf14af1c2a8e80ae2c37c044114c2a1e0d037` |
| `g4_candidate_replay_raw/child.stdout.jsonl` | `7efaff8c5e47274efbc16dfc6121f3ffb5ed5d049d16cfc2de4c047cb8e09440` |
| `g4_candidate_replay_raw/child.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `g4_candidate_replay_raw/g4_normal_entry_decision.md` | `b7d37f7c8811b0ae6ed4d715350bdc39609674b4e5a657d01e8227dd662a4d81` |

Decision summary:

- missing default renderer/probe is not capability absence;
- specialist normal entry must be checked before fallback;
- artifact identity changing fallback is not equivalent unless frozen scope
  explicitly authorizes it.
