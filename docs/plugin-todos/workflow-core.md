# workflow-core — Long-Term TODO

Canonical maintenance inbox for the `workflow-core` plugin.

## Open candidates

### Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs
status: PROMOTE_NOW
source: 042/043 Reviewed Handoff pause
evidence: AI_Skills validation currently reports a stale-review/implementation binding blocker for 042; the generic runtime source of truth is `YuukiAS/GPT_Codex_AI_Bridge_Kit`
target layer: external-runtime
problem: project workflows can be tempted to patch local history or duplicate generic Reviewed Handoff runtime code when the defect actually belongs to Bridge Kit.
candidate action: record the external-runtime ownership clearly; fix generic validator semantics in Bridge Kit when resumed, never by rewriting 042 review history or vendoring runtime into AI_Skills.
promotion gate: Bridge Kit regression proving legal `PLANNER_DECISION` terminalization and preserving strict binding for Reviewer-owned states.

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
