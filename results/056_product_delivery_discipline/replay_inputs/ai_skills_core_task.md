Use the installed AI Skills Maintainer candidate through its normal plugin
entry.

Read the input fixture and produce exactly one JSON file at
`outputs/ai_skills_core_gate_replay.json`.

The JSON must contain:

- `plugin`: `ai-skills-core`
- `normal_entry`: `AI Skills Maintainer candidate`
- one `G8` entry with `observed_behavior`, `pass`, and `reason`
- `classification`
- `consumer_path_checked`
- `adds_duplicate_policy`

The correct behavior is to diagnose the consumer path first and classify the
failure as stale install or the closest existing production-consumption class.
Do not add synonymous policy and do not claim source strings alone prove normal
production consumption.
