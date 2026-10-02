# workflow-core 0.5 Final Critic Handoff

Status: `READY_FOR_FINAL_CRITIC`

Task: `workflow-core--normal-entry-reliability`

Repository: `YuukiAS/AI_Skills_Collection`

Branch: `work/workflow-core--normal-entry-reliability`

Final production candidate commit:
`671eb532e0ec949dc7889427379a1113cf7a6ea9`

Current evidence HEAD:
verify with `git rev-parse HEAD` on the task branch.

Final Critic repair status:
the prior Final Critic returned `REVISE` for evidence quality only. The current
handoff keeps final production candidate
`671eb532e0ec949dc7889427379a1113cf7a6ea9`, `workflow-core 0.5`, and
repository `5.4.1`; it repairs only tracked Gate evidence and handoff records.

Second-round closure status:
the second Final Critic returned `REVISE` only for WC05-FC2 and WC05-FC4.
This closure keeps the same production candidate and versions. WC05-FC2 is
closed by a new true capability-absent contrast under
`g4_absent_contrast_raw/`. WC05-FC4 is closed by normalizing the canonical TODO
status in `docs/plugin-todos/workflow-core.md` from
`PROMOTED / RELEASED_IN_5.4.1` to `PROMOTED`; release evidence remains in the
TODO release-evidence field and changelog/version metadata.

## Scope

This is the single independent final-candidate Critic checkpoint required by:

`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md`

There was no mid implementation pre-final Critic. Critic PASS is required
before main integration, formal repository release closure, release ref closure,
or production identity/install-update smoke.

## Required Inputs

Read:

- `AGENTS.md`
- `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md`
- `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md`
- `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_4_2026-10-01.md`
- `results/workflow-core--normal-entry-reliability/FINAL_CANDIDATE_IDENTITY.md`
- `results/workflow-core--normal-entry-reliability/GATE_CASES.json`
- `results/workflow-core--normal-entry-reliability/QUALIFICATION_RESULT.md`
- `results/workflow-core--normal-entry-reliability/G1_G6_RESULT.md`
- `results/workflow-core--normal-entry-reliability/G1_TRIGGER_TRACE.md`
- `results/workflow-core--normal-entry-reliability/G4_NORMAL_ENTRY_TRACE.md`
- `results/workflow-core--normal-entry-reliability/G6_NORMAL_ENTRY_TRACE.md`
- `results/workflow-core--normal-entry-reliability/G6_ROUTE_IDENTITY.md`
- `results/workflow-core--normal-entry-reliability/BROAD_CI.md`

Raw candidate replay evidence:

- `results/workflow-core--normal-entry-reliability/qualification_candidate_replay_raw/`
- `results/workflow-core--normal-entry-reliability/g1_positive_implicit_raw/`
- `results/workflow-core--normal-entry-reliability/g1_positive_contextual_raw/`
- `results/workflow-core--normal-entry-reliability/g1_hard_negative_raw/`
- `results/workflow-core--normal-entry-reliability/g1_simple_negative_raw/`
- `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/`
- `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/`
- `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4/`

## Review Questions

Decide `PASS` or `REVISE`.

Check at least:

1. The implementation actually satisfies Proposal V0.5 and Plan V0.4 without
   scope expansion.
2. Qualification used canonical task-local candidate replay and did not rely on
   global `workflow-core@yuukias-ai-skills` installation.
3. G1-G6 evidence is direct enough and all gates bind back to the same final
   production candidate commit.
4. G1 trigger evidence includes production-compatible positive and negative
   replay traces, including non-consumption proof for specialist-contained and
   simple-negative cases.
5. G4 and G6 prove actual `workflow-core@ai-skills-candidate` consumption from
   the candidate plugin replay route.
6. G4 proves actual targeted capability discovery/probe output before route
   choice and does not substitute a non-equivalent artifact fallback.
7. G4 also includes a true capability-absent contrast where canonical task,
   matched specialist, and project-declared runtime routes are all unavailable
   in a controlled fixture, and the candidate fails closed without unrelated
   host scanning, invented stack, product downgrade, false completion, or
   Human Gate.
8. G6 validates a real fixture Git repository, build/check, local commit,
   bounded publisher route boundary, no raw fallback, no second same-class
   retry, and local evidence preservation.
9. Version/changelog/README/generated parity and release metadata match the
   approved exactly-once version policy.
10. `docs/plugin-todos/workflow-core.md` uses canonical status vocabulary for
    the promoted workflow-core 0.5 item (`status: PROMOTED`) while preserving
    release evidence separately.
11. Broad local checks and required remote CI are PASS.
12. Evidence-only/metadata correction commits after the final candidate do not modify production
   source, generated payload, version metadata, release metadata, or frozen
   gate semantics.
13. No paid API, live-global candidate install, production Marketplace mutation,
   Bridge/Host Policy mutation, force/destructive Git, branch deletion, or
   unauthorized branch/ref publication occurred.

## Explicit Non-Blocker

`codex plugin list --json` not listing
`workflow-core@yuukias-ai-skills` only proves the current Codex identity lacks
that global Marketplace plugin installation. It is not evidence that the
canonical task-local candidate replay route is unavailable.

Candidate replay availability and consumption must be judged from:

- `scripts/candidate_plugin_replay.py`;
- its tests;
- historical replay precedent;
- the tracked `run.json`, `plugin-add.json`, `child.stdout.jsonl`, and response
  artifacts in this task.

## Output Contract

If PASS, state that the exact final production candidate
`671eb532e0ec949dc7889427379a1113cf7a6ea9` may proceed to the Plan V0.4
canonical integration / release closure envelope, subject to current main drift
preflight.

If REVISE, list concrete blockers and whether repair belongs to Executor within
Plan V0.4, Planner/Critic, or an out-of-scope authority owner.
