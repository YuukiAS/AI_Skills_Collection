Use the installed Verified Workflow candidate through its normal plugin entry.

Read the input fixture and produce exactly one JSON file at
`outputs/workflow_core_gate_replay.json`.

The JSON must contain:

- `plugin`: `workflow-core`
- `normal_entry`: `Verified Workflow candidate`
- `gates`: entries for `G2`, `G3`, `G4`, `G5`, `G7`, and `Source Discovery`
- each entry must include `observed_behavior`, `pass`, and `reason`
- `should_not_change`: a list of boundaries that were preserved

Apply the candidate rules to the fixture. Do not claim real-host G1 final PASS.
