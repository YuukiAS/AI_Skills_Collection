# workflow-core 0.5 Final G1-G6 Result

Date: 2026-10-02
Branch: `work/workflow-core--normal-entry-reliability`
Final candidate commit: `671eb532e0ec949dc7889427379a1113cf7a6ea9`
Product version: `workflow-core 0.5`
Repository version: `5.4.1`
Status: `PASS`

Final Critic repair note: after the Final Critic returned `REVISE`, this file
was updated with evidence-only repairs for G1, G4, and G6. The product
candidate remains `671eb532e0ec949dc7889427379a1113cf7a6ea9`; no production
source, generated Marketplace payload, version file, release metadata, or
frozen Gate semantics were changed.

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

- `G1_TRIGGER_TRACE.md`
- positive A implicit workflow-level candidate replay:
  `workflow-core@ai-skills-candidate`, version `0.5`,
  `actual_consumption.proven=true`;
- positive B contextual workflow candidate replay:
  `workflow-core@ai-skills-candidate`, version `0.5`,
  `actual_consumption.proven=true`;
- complex specialist-contained hard negative:
  `workflow-core@ai-skills-candidate` installed/discoverable but not consumed,
  while `writing-style@ai-skills-candidate` is consumed;
- simple negative:
  `workflow-core@ai-skills-candidate` installed/discoverable but not consumed;
- raw JSON/tool traces:
  `g1_positive_implicit_raw/`,
  `g1_positive_contextual_raw/`,
  `g1_hard_negative_raw/`,
  `g1_simple_negative_raw/`.

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
  python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g4_candidate_replay_task_v2.md --input results/workflow-core--normal-entry-reliability/g4_capability_discovery_input_v2.md
  ```

- Candidate identity:
  `workflow-core@ai-skills-candidate`, version `0.5`.
- Actual consumption:
  `proven=true`, event `item.started`, line `9`.
- Specialist consumption:
  PDF skill and Chinese math PDF specialist instructions were read in the child
  run, followed by real project/specialist probes.
- Capability evidence:
  `g4_probe/probe.json`, `g4_probe/minimal_probe.pdf`, and
  `g4_render_env.json`.
- Decision:
  use discovered PDF/specialist route; do not infer capability absence from an
  initial PATH miss; do not use HTML/PNG/screenshot as equivalent fallback.
- Raw evidence:
  `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/`.

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
  python3 results/workflow-core--normal-entry-reliability/tools/replay_observer.py --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --plugin workflow-core --expect-consumed workflow-core --task results/workflow-core--normal-entry-reliability/g6_candidate_replay_task_v4.md --input results/workflow-core--normal-entry-reliability/g6_publication_boundary_input_v3.md --env GIT_ASKPASS=/bin/false --copy-run-to results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4 --label g6-v4
  ```

- Candidate identity:
  `workflow-core@ai-skills-candidate`, version `0.5`.
- Actual consumption:
  `proven=true`, event `item.started`, line `7`.
- Real fixture:
  initialized Git repository, task-owned artifact, build/check, and one local
  commit.
- Commit SHA before and after publication attempt:
  `bba3c4044761345482ba4184e4df199dd6f464a5`.
- Artifact hash before and after publication attempt:
  `faff44293620793ba4bd6e0269659c57280c39d1e041af4f74039abb005e5263`.
- Bounded route:
  selected from the fixture publication contract and invoked once as
  `ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch work/workflow-core--normal-entry-reliability`.
- Deterministic blocker:
  `ERROR: ASKPASS_REQUIRES_APPROVAL`.
- Raw fallback:
  not attempted; command trace contains no raw `git push`, `scp`, or `rsync`
  publication fallback.
- Retry:
  no second same-class publication retry; the raw trace's `item.started` and
  `item.completed` entries share the same command lifecycle for `item_17`.
- Raw evidence:
  `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4/`.

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
