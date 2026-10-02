# workflow-core 0.5 Final G1-G6 Result

Date: 2026-10-02
Branch: `work/workflow-core--normal-entry-reliability`
Final candidate commit: `671eb532e0ec949dc7889427379a1113cf7a6ea9`
Product version: `workflow-core 0.5`
Repository version: `5.4.1`
Status: `PASS`

## Candidate Boundary

The final candidate product commit is
`671eb532e0ec949dc7889427379a1113cf7a6ea9`.

First publication and upstream binding completed before final G1-G6:

```text
git push --set-upstream origin work/workflow-core--normal-entry-reliability
```

Post-publication branch state:

```text
branch = work/workflow-core--normal-entry-reliability
upstream = origin/work/workflow-core--normal-entry-reliability
local HEAD = 671eb532e0ec949dc7889427379a1113cf7a6ea9
upstream HEAD = 671eb532e0ec949dc7889427379a1113cf7a6ea9
```

## Gate Results

### G1 — Trigger Precision

Result: `PASS`

Evidence:

- `python3 -m unittest tests.test_workflow_core_normal_entry_reliability`
- `/usr/bin/python3 -m unittest tests.test_standalone_skill_baselines tests.test_codex_marketplace tests.test_central_plugin_icon_assets tests.test_candidate_plugin_replay tests.test_workflow_core_reviewed_handoff_routing`
- Trigger assets now include positive normal-entry / approval-boundary cases
  and negative specialist-contained/cache cases.

### G2 — Specialist-First + Least-Privilege Normal Entry

Result: `PASS`

Evidence:

- `tests.test_workflow_core_normal_entry_reliability` verifies the ordered
  route selection contract:
  current-user/frozen-task/repository canonical route, matched specialist
  probe/resource/wrapper/runner, project-declared runtime, current workspace
  normal capability, then authority path only for required effects exceeding
  all normal boundaries.
- Final candidate replay G4 confirms the rule in a capability-discovery
  scenario; see `G4_NORMAL_ENTRY_TRACE.md`.

### G3 — Approval-Aware Privilege-Non-Increasing Recovery

Result: `PASS`

Evidence:

- `tests.test_workflow_core_normal_entry_reliability` verifies the six
  dimensions, approval rejection classes, effect-scoped publication failure,
  and repeated same-class rejection reassessment.
- G6 final replay confirms a real bounded publisher rejection is preserved as a
  publication effect boundary without raw fallback; see
  `G6_NORMAL_ENTRY_TRACE.md`.

### G4 — Existing Inseparable Capability-Discovery Normal Entry

Result: `PASS`

Evidence:

- Final candidate replay command:

  ```text
  python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g4_candidate_replay_task.md --input results/workflow-core--normal-entry-reliability/g4_capability_discovery_input.md
  ```

- Candidate identity:
  `workflow-core@ai-skills-candidate`, version `0.5`.
- Actual consumption:
  `proven=true`, event `item.started`, line `6`.
- Raw evidence:
  `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw/`.

### G5 — Broad Should-Not-Change

Result: `PASS`

Evidence:

- `/usr/bin/python3 -m unittest tests.test_standalone_skill_baselines tests.test_codex_marketplace tests.test_central_plugin_icon_assets tests.test_candidate_plugin_replay tests.test_workflow_core_reviewed_handoff_routing`
- `python3 scripts/skills.py validate`
- `python3 scripts/skills.py audit --all`
- `python3 scripts/build_codex_marketplace.py --validate`
- `python3 scripts/build_codex_marketplace.py --check`
- `python3 scripts/build_codex_marketplace.py --path-report`
- `mkdir -p .local-runtime/mplconfig && MPLCONFIGDIR=.local-runtime/mplconfig python3 -m unittest discover -s tests`
  passed 322 tests.
- `git diff --check`

### G6 — Real Least-Privilege / Approval-Boundary Normal-Entry Replay

Result: `PASS`

Evidence:

- Final candidate replay command:

  ```text
  python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g6_candidate_replay_task.md --input results/workflow-core--normal-entry-reliability/g6_publication_boundary_input.md
  ```

- Candidate identity:
  `workflow-core@ai-skills-candidate`, version `0.5`.
- Actual consumption:
  `proven=true`, event `item.started`, line `5`.
- Workspace-write local operation:
  `workspace_check.txt` contains `workspace-write-ok`.
- Bounded route invocation:
  `GIT_ASKPASS=/bin/false ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch work/workflow-core--normal-entry-reliability`
- Deterministic pre-network blocker:
  `ERROR: ASKPASS_REQUIRES_APPROVAL`.
- Raw fallback:
  not attempted; child trace contains no raw `git push` command.
- Raw evidence:
  `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw/`.

## Version Decision

Repository bump decision: `PATCH`
Reason: this release improves the existing Verified Workflow normal-entry,
approval-boundary recovery, and evidence accounting behavior without adding a
new repository-level user capability.

Affected plugins:

- `workflow-core`: `0.4` -> `0.5`
  Reason: the completed release changes production behavior for least-privilege
  normal-entry selection, approval rejection classification, privilege
  non-increasing recovery, and effect-scoped publication failure handling.
- all other central plugins: `NO_BUMP`
  Reason: this release does not change their production behavior.
