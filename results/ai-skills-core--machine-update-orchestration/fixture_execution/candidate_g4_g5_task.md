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
  "candidate_commit": "4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00",
  "candidate_plugin": "ai-skills-core@ai-skills-candidate",
  "owner_path_consumed": "...",
  "marketplace_commands": [
    {
      "argv": ["...", "plugin", "marketplace", "list", "--json"],
      "codex_home": "...",
      "returncode": 0
    }
  ],
  "cases": [
    {
      "case": "stale_managed_consumer",
      "status": "...",
      "failure_injection_point": null,
      "diagnostics": ["..."],
      "human_gate_count": 0
    }
  ]
}
```

Case requirements:

- For managed consumer fixtures, use the AI_Skills managed markers/manifest to
  decide whether a candidate-owned update is allowed. Preserve project-owned
  text and unrelated dirty files.
- For repo-owned apparent conflicts without managed ownership, preserve bytes
  and classify using the Maintainer conflict contract.
- For overlapping user-owned dirty work, emit exactly one bounded Human Gate
  and leave the overlapping user file unchanged.
- For the failure/restoration case, perform one safe managed consumer step
  first. Then use the manifest's isolated temporary `CODEX_HOME`, pinned
  `codex_cli`, and official `codex plugin marketplace` commands to exercise
  the legacy-source replacement path. Inject the bounded failure by attempting
  to add the provided missing replacement source after removing the legacy
  source. Restore the exact legacy source through the same official command
  family, run fresh discovery once, and report whether it converged without a
  second mutation.
- Select each case's returned status from the manifest vocabulary based on the
  actual candidate/owner behavior. Do not treat this task prompt as an answer
  key for the case outcomes.

Do not call paid APIs, do not mutate Marketplace/Host/global Codex state, and
do not change Git refs. The fixture repos themselves are writable for this
candidate replay.
