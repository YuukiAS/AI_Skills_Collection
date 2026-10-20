# Root and pending identity binding repair

Continuation of `hpc--slurm-cancel-production-closure` on its existing task branch and worktree. Current-user authority explicitly permits repairing the existing command guard and MCP input, atomically installing the candidate, and native re-trust of only the task-owned PreToolUse command, PreToolUse MCP, and PermissionRequest command. No other Hook, Codex, Bridge Kit, DII, CARE, Slurm routing, confirmation protocol, or card UI changes are authorized by this repair.

The actual prior normal-entry failure was `hook input placeholder ${agent_id} was not found`. The installed direct MCP form path already returned a real user selection through standard `elicitation/create`; that is capability evidence, not G4 acceptance for this new candidate.

## Source repair

- The template references only guaranteed root Hook fields. Neither optional agent field is required for expansion.
- The complete raw command event remains the pending producer. It always blocks original protected scancel, resolves and checks the current owner's exact cancellable targets, rejects explicit agent fields, and publishes a private random-nonce pending record without overwriting an earlier event identity.
- Pending records bind session, turn, tool use, normalized target set, partition/state, validated owner, operation, cwd and a 900-second lifetime. They are preserved across atomic installation together with existing audit and one-shot state.
- The MCP server requires the host-injected concrete `metadata.threadId` to equal the root `session_id` before pending access or elicitation. It waits at most two seconds for the matching command-produced pending; it cannot create that authorization.
- Retain and unconfirmed/failed elicitation close pending without creating a cancellation reservation. Confirmation revalidates the pending and nonce, then preserves exact re-resolution, durable one-shot reservation, final re-resolution and one absolute scancel invocation, with read-only reconciliation and durable result audit. A consumed identity cannot be replayed.
- The harmless sentinel uses the same guard-to-pending-to-MCP path with operation `ui_probe` and no scheduler lookup, cancellation reservation or shell execution.

## Focused verification

`python -m unittest discover -s tests -p 'test_slurm_protected_cancel*.py'`

49 tests passed. Coverage includes absent optional root fields, required-field template expansion, actual supervisor pending production, root/concrete-thread matching, explicit subagent rejection, missing/incorrect/expired/consumed pending, malformed and wrong call identities, bounded early-MCP race, unavailable/closed/malformed elicitation, retain without reservation, one-shot exact invocation, post-reservation drift, independent fail-closed guard, unprotected passthrough and unsupported selectors.

One existing cross-cwd fixture reused the same tool-use identity for four distinct invocations. It now assigns one tool-use identity per invocation; production duplicate-event rejection remains intact.

## Runtime checkpoint

Frozen implementation: `10f10017129bd59f2611885ecb24a080e80b3272`. This subsequent control checkpoint changes no implementation bytes. Installation must compare each installed runtime source against this Git object and preserve every existing native trust value. After the authorized atomic installation, the next dependent action is native re-trust of exactly the three task-owned handlers, followed by a refreshed normal root session and the harmless sentinel; do not request real cancellation first.

No real Job was read or mutated during this repair. No cancellation reservation for Job 5693449 was created. Native trust, the new candidate's harmless normal-entry card, retain/confirm on the single existing Job, G4, full regression/CI, independent final review, G5, version/release and formal installation remain subsequent gates. No completion or release PASS is claimed here.

README: no change required. No version or changelog bump is made at this pre-G4 checkpoint.
