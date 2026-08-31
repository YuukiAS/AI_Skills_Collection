# workflow-core — Long-Term TODO

Canonical maintenance inbox for the `workflow-core` plugin.

## Open candidates

### Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs
status: PROMOTE_NOW
source: 042/043 Reviewed Handoff pause; 044 writing-style production replay
evidence: AI_Skills validation previously exposed a stale-review/implementation binding blocker for 042; task 044 then exposed a second generic runtime problem when an otherwise authorized plugin replay had to launch a fresh `codex exec` on a private local artifact and the Host Policy approval reviewer stopped it before the plugin could be tested. The generic runtime source of truth is `YuukiAS/GPT_Codex_AI_Bridge_Kit`; the bounded Host Policy design is now recorded there in `docs/design/host_policy_plugin_replay_authorization.md`.
target layer: external-runtime
problem: project workflows can be tempted to patch local history, add project-specific approval exceptions, or duplicate generic Reviewed Handoff / Host Policy runtime code when the defect actually belongs to Bridge Kit. Plugin-repair tasks also need a stable production-replay path; raw nested `codex exec` should not become an ad hoc per-task approval negotiation.
candidate action: keep generic validator and Host Policy fixes in Bridge Kit. For plugin production replay, use the Bridge-owned bounded replay path once implemented, rather than broad raw `codex exec` allow rules or AI_Skills-local Host Policy copies. After the Bridge Kit behavior is stable, make the AI_Skills Executor guidance prefer that path for plugin-repair replay without changing Planner/Reviewer authority.
promotion gate: Bridge Kit regression proving legal `PLANNER_DECISION` terminalization where relevant, plus a generic plugin-replay smoke showing an explicitly selected private local input can be processed by a fresh production Codex/plugin runtime and written to a local private replay directory without repeated approval, while dangerous Git/branch/remote actions remain protected.

### Real-task-driven Reviewed Handoff batches
status: PROMOTE_NOW
source: user decision after presentation Stage-5 loop
evidence: `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
target layer: routing/qa
problem: an automation can become an endless synthetic recovery chain even after the product has reached a useful baseline.
candidate action: require explicit real blocker / plugin TODO source for long-running refinement batches and stop the watcher when the batch is closed or user redirects to real workflow refinement.
promotion gate: apply to the next AI_Skills maintenance batch without creating a second state machine.

## Do not do

- Do not duplicate Bridge Kit core Reviewed Handoff implementation in this repo.
- Do not use workflow-core to make domain judgments for writing, Presentation, statistics or imaging.
