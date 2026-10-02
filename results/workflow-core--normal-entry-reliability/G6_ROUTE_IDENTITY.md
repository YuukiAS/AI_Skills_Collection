# G6 Route Identity

Status: `PASS`

Execution-time bounded route:

```text
ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch work/workflow-core--normal-entry-reliability
```

Executable identity:

- executable wrapper: `/users/a/e/aereinh/bin/ai-bridge`
- tool-reported version: `0.9.3`
- resolved implementation package:
  `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit/ai_bridge_kit/host.py`
- relevant implementation function:
  `_assert_publisher_preconditions(...)`

Current real task branch identity before G6 evidence commit:

```text
branch = work/workflow-core--normal-entry-reliability
upstream = origin/work/workflow-core--normal-entry-reliability
local HEAD = 671eb532e0ec949dc7889427379a1113cf7a6ea9
upstream HEAD = 671eb532e0ec949dc7889427379a1113cf7a6ea9
```

Chosen deterministic blocker:

```text
GIT_ASKPASS=/bin/false
```

Observed bounded route result:

```text
exit_code = 1
stderr = ERROR: ASKPASS_REQUIRES_APPROVAL
```

Why this is the correct G6 blocker:

- Bridge 0.9.3 rejects inherited process transport helpers before Git
  repository or remote operations.
- The helper is still invoked with the exact expected repository and branch.
- The blocker is deterministic, local, and pre-network.
- The failure belongs only to the publication effect; it does not invalidate
  local workspace-write evidence or final-candidate source/generated parity.
- No raw `git push`, alternative remote, alternate branch, force push, or
  wider privilege route was attempted.
