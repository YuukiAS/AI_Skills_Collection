# G4/G5 Fixture Evidence

Task key: `ai-skills-core--machine-update-orchestration`
Candidate commit: `12ca08dc127f8eee4c13a3a2c9cc598d00ce04ee`
Candidate/plugin/owner path consumed: `AI Skills Maintainer -> machine-update-orchestrator -> project-skill-installer; machine-update-orchestrator Route A failure recovery`
Fixture root: `/home/yuukias/AI_Skills_Collection-ai-skills-core-machine-update-orchestration/private/exports/ai-skills-core--machine-update-orchestration/fixtures`
Candidate output: `/home/yuukias/AI_Skills_Collection-ai-skills-core-machine-update-orchestration/.local-runtime/candidate-plugin-replay/runs/20260924T120413Z-2788805/workspace/outputs/g4_g5_candidate_result.json`

| Case | Status | Before hash | After hash | Failure injection | Diagnostics |
|---|---|---|---|---|---|
| `stale_managed_consumer` | `UPDATED_RELOAD_REQUIRED` | `f4eaa8d367e72c4d76fc9075bde06ca9f64479e48b151f732f3af9890c704bde` | `a8271e199733c180f109ea44c1cd0a908953b757a5be65cea39e5c624904dde1` | `` | Candidate project-skill-installer ownership applied as a bounded managed-block refresh; version 0.4 -> 0.5. No full profile install or current-session hot-reload claimed.<br>All non-target bytes and Git HEAD preserved; no Git ref commands executed. |
| `unaffected_repo` | `ALREADY_CURRENT` | `a937a64909c05c4612b5a706eb40d9956c1d139c60b027045cdc9383ab48e49f` | `a937a64909c05c4612b5a706eb40d9956c1d139c60b027045cdc9383ab48e49f` | `` | No managed consumer locator; no installation or mutation performed.<br>All non-target bytes and Git HEAD preserved; no Git ref commands executed. |
| `unmanaged_conflict` | `REPO_OWNED_CONFLICT` | `4205ddf977e33c7dfb732b99e114d57276402cd31fa6b3eaeb1cf8ed121a418e` | `4205ddf977e33c7dfb732b99e114d57276402cd31fa6b3eaeb1cf8ed121a418e` | `` | Unmanaged repository AI_Skills rule detected; preserved without attempting conflict resolution.<br>All non-target bytes and Git HEAD preserved; no Git ref commands executed. |
| `unrelated_dirty_non_overlap` | `UPDATED_RELOAD_REQUIRED` | `fe9aa5c2aae6594b6f521e7ff39229712bc519f83dfb762893e10bbe987def06` | `ef4ca373f0979bb5be2305e2658640b50c6e370872f425749bb961a7ba1563a1` | `` | Candidate project-skill-installer ownership applied as a bounded managed-block refresh; version 0.4 -> 0.5. No full profile install or current-session hot-reload claimed.<br>All non-target bytes and Git HEAD preserved; no Git ref commands executed. |
| `overlapping_dirty_human_gate` | `HUMAN_ONLY` | `02f9b5ac0f23c541eaac902bca4c9a685f21f6af19596bf8412f686fe195eedb` | `02f9b5ac0f23c541eaac902bca4c9a685f21f6af19596bf8412f686fe195eedb` | `` | Task-declared overlapping dirty target: stopped before mutation; one bounded gate recorded for replay, no live user approval requested.<br>All non-target bytes and Git HEAD preserved; no Git ref commands executed. |
| `failure_restoration_and_rerun` | `PARTIAL_UPDATE` | `cda584689289732d046182c0b7599d5a774941df1e53979d560d50106b8557b0` | `ceb16b3897456a37f82d590e5462f352434a07eb223e8138fbe5bfada4ecce50` | `after_safe_managed_update:marketplace_source_replacement_after_legacy_removal` | Candidate project-skill-installer ownership applied as a bounded managed-block refresh; version 0.4 -> 0.5. No full profile install or current-session hot-reload claimed.<br>Manifest supplies source fixture but no separate injection parameters; user-specified replacement failure simulated locally. No official Marketplace command or global state mutation executed.<br>All non-target bytes and Git HEAD preserved; no Git ref commands executed. |

All fixture repositories are task-owned local repositories under `private/exports/`.
The harness owns setup, failure injection fixtures, hashing, invariant assertions and evidence collation only.
Actual semantic statuses and mutations were produced by the committed candidate through candidate plugin replay.
