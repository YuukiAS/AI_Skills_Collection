# Presentations Stage 1 — F03 Bridge Dependency

**Status:** CLOSED_BY_BRIDGE_0_9_3  
**Date:** 2026-09-29  
**Presentations task:** \`presentations--stage1-front-door-two-template-foundation\`

## Closure

Historical blocker:

\`PRES-S1-ER-F03\`

is closed.

Bridge Kit formal release:

\`\`\`text
BRIDGE_KIT_VERSION = 0.9.3
FORMAL_RELEASE_TARGET =
9dad0ba4bfa54e251f345091c5151ae991251ec9
FORMAL_DISTRIBUTION_COMPLETE = YES
\`\`\`

Current production normal entry:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key <task_key> \
  --expected-repo <owner/repo>
\`\`\`

The command now provides the bounded same-name first remote publication required after \`task bootstrap\` and the exact first REQUEST/CURRENT commit.

Direct closure evidence:
- Bridge \`pyproject.toml\` and runtime version = 0.9.3;
- formal \`release\` ref points to the repaired candidate above;
- Machine Policy includes bounded \`reviewed-handoff task publish-first\`;
- fresh AI_Skills real-consumer FP-G6 passed;
- Presentations narrow F03 Critic review recorded:
  \`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V3_F03.md\`.

## Superseded historical behavior

Do not repeat the historical workaround/blocker language:

- \`UPSTREAM_REMOTE_MISMATCH\` from generic existing-branch publisher;
- manual/raw \`git push -u\`;
- second ordinary first-publication approval;
- consumer-local first-push wrapper.

Those describe pre-0.9.3 capability state and are superseded for a machine running compatible Bridge 0.9.3+.

## Current execution-machine condition

Formal distribution does not prove every machine is updated.

At execution preflight:
- confirm compatible Bridge 0.9.3+ runtime;
- confirm \`ai-bridge reviewed-handoff task publish-first --help\` is available;
- confirm current Host/Reviewed Handoff validation passes.

If the execution machine is stale, use:

\`BLOCKED_BRIDGE_RUNTIME_STALE\`

This is a machine/runtime prerequisite, not reopening \`PRES-S1-ER-F03\`.

## Current Presentations amendment

The prior Stage 1 v1.1 package was execution-ready after F03 closure.

A new v1.2 package is now being reviewed for a **different reason**: real teaching-deck evidence promotes TODO #49 into the course-standard adapter foundation.

Bridge 0.9.3 changes only the execution-control chronology; it does not change Presentations product semantics.

## Maintenance truth

Presentations lifecycle remains \`DOING\`.
Source maturity is changed only where the new Planner amendment explicitly promotes #49.
No issue is DONE/closed by this dependency closure.
