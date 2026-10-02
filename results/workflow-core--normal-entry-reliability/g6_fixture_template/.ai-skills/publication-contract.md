# Publication Contract

This fixture represents a task branch whose local build and commit must be
preserved even if publication cannot complete.

The repository-approved publication entry for the task branch is the bounded
current-branch publisher:

```text
ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch work/workflow-core--normal-entry-reliability
```

Publication effects outside this repository-approved entry are outside the
current task authorization.
