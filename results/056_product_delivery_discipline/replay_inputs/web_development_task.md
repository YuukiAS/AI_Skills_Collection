Use the installed Frontend Design candidate through its normal plugin entry.

Read the input fixture and produce exactly one JSON file at
`outputs/web_development_gate_replay.json`.

The JSON must contain:

- `plugin`: `web-development`
- `normal_entry`: `Frontend Design candidate`
- one `G6` entry with `observed_behavior`, `pass`, and `reason`
- evidence that the candidate treats the canonical design source as authority
- evidence that Figma handoff and motion production wiring are consumed
- evidence that missing material states are returned to design-source closure
  rather than silently invented in code

Do not modify any product repository and do not claim real-host G1 final PASS.
