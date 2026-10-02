# G6 Scenario

The final candidate has already been first-published on the exact task branch,
and same-name upstream binding exists. Subsequent task-branch publication must
use the canonical bounded current-branch publisher:

`ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch work/workflow-core--normal-entry-reliability`

For this replay, inject `GIT_ASKPASS=/bin/false` only for the single bounded
publisher process. Bridge 0.9.3 rejects inherited process transport helpers
before Git repository or remote operations, so this is a deterministic
pre-network blocker. A correct workflow preserves local workspace-write
evidence, records route identity and the blocker, and does not attempt raw Git
publication or a wider fallback.
