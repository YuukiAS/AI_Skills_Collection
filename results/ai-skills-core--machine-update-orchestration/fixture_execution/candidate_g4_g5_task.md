# Candidate Replay Task: G4/G5 Machine Update Fixture Execution

Use AI Skills Maintainer.

This is release-critical candidate-direct evidence for task `ai-skills-core--machine-update-orchestration`. Read
the attached manifest and operate only on the task-owned fixture repositories
listed there. Do not use unrelated real projects.

For every case, select the production owner path from the candidate plugin
itself. The fixture harness owns setup and invariant checks only; the semantic
action and returned state must come from this candidate run.

Required output: write JSON to `outputs/g4_g5_candidate_result.json` with:

```json
{
  "candidate_commit": "12ca08dc127f8eee4c13a3a2c9cc598d00ce04ee",
  "candidate_plugin": "ai-skills-core@ai-skills-candidate",
  "owner_path_consumed": "...",
  "cases": [
    {
      "case": "stale_managed_consumer",
      "status": "UPDATED_RELOAD_REQUIRED",
      "failure_injection_point": null,
      "diagnostics": ["..."],
      "human_gate_count": 0
    }
  ]
}
```

Case requirements:

- `stale_managed_consumer`: update only the AI_Skills managed block from
  `ai-skills-core: 0.4` to the current candidate `0.5`; preserve project-owned
  text and return `UPDATED_RELOAD_REQUIRED`.
- `unaffected_repo`: no managed locator exists; leave bytes unchanged and return
  `ALREADY_CURRENT`.
- `unmanaged_conflict`: repo-owned `AGENTS.md` mentions AI_Skills without
  managed markers; leave bytes unchanged and return `REPO_OWNED_CONFLICT`.
- `unrelated_dirty_non_overlap`: preserve dirty `notes.txt`, update the managed
  block and return `UPDATED_RELOAD_REQUIRED`.
- `overlapping_dirty_human_gate`: `AGENTS.md` has overlapping user dirty work;
  leave it unchanged and return `HUMAN_ONLY` with exactly one bounded Human
  Gate.
- `failure_restoration_and_rerun`: perform the safe managed update, then apply
  the manifest's marketplace replacement failure injection after that safe step;
  restore the exact legacy `marketplace-source.json`, return `PARTIAL_UPDATE`,
  rerun fresh discovery once, and report convergence without a second mutation.

Do not call paid APIs, do not mutate Marketplace/Host/global Codex state, and
do not change Git refs. The fixture repos themselves are writable for this
candidate replay.
