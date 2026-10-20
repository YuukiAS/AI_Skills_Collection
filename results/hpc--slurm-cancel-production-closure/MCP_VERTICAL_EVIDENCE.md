# Current-chat MCP vertical verification — STOP

Source candidate: `ac6a380c00b416ef7a5c4c46591fd0cfe9b6770a`.
Existing task/branch/worktree unchanged. No new conversation or backend was created. No pending hidden request was replayed or answered.

## Installation and native trust

The atomic installation qualified the real official MCP SDK 1.30.0 and the staged server. Its durable receipt is `private/exports/hpc--slurm-cancel-production-closure/mcp-install-receipt.json` in the canonical checkout. Command guard/supervisor/runtime/policy bytes and existing trust hashes were unchanged; only the task-owned MCP route was added and its old PostToolUse binder retired. Independent source review of this exact candidate passed after two concrete implementation findings were repaired; this is not a runtime PASS.

Installed MCP source SHA256: `78d78a7f2972b93364f069bec8e1dbfd0425b2101b0d7cd8927de9b88d85e726`.

The user completed native trust while this run remained active. At `2026-10-20 02:29:44 UTC`, the same existing backend's official hooks/list reported:

- key: `/users/a/e/aereinh/.codex/config.toml:pre_tool_use:0:1`
- handler: `mcpTool`, `slurm-protected-cancel/slurm_protected_cancel`
- enabled: true
- currentHash: `sha256:14b601c685e149b2e6947f7dfbea7460c431e4acfc8abeb832eef19cdc766c78`
- trustStatus: `trusted`

An independent read of the exact config entry verified trusted_hash equals that exact currentHash. Executor never wrote trusted_hash, bypassed trust or trusted unrelated handlers.

## Supported normal load and actual current-chat probe

No external client started an assistant turn or generated the question.

1. Existing backend RPC 1100: official `config/batchWrite` with `edits=[]`, `reloadUserConfig=true` returned `status=ok`; no configuration value edit was requested.
2. RPC 1101: official `mcpServerStatus/list` scoped to the current root chat `01a15211-6a48-7262-adcd-f9d5ee5d485e`, server `slurm-protected-cancel`, returned `runtimeStatus=connected`, SDK version 1.30.0, the correct `slurm_protected_cancel` tool and no toolsError. This establishes connection/catalog state, not execution-session Hook proof.
3. This current visible chat's ordinary nested `tools.exec_command` invoked exactly:

   `printf '__SLURM_PROTECTED_CANCEL_CARD_PROBE__\n'`

   Tool result chunk `2ab9fa`: exit_code=0, output `__SLURM_PROTECTED_CANCEL_CARD_PROBE__` followed by newline, wall time about 0.049 seconds. Thus the harmless Bash command actually launched and returned; it did not wait for a native form or return the MCP probe's blocking result.
4. Read-only inspection immediately afterward found no files in the installed task-owned `audit/` or `consumed/` directories. In the frozen source, `handle()` identifies this exact sentinel (line 231) and must create `elicitation_requested` before requesting the form (line 246); every completed diagnostic response blocks the original Bash command. The observed execution did not reach that audited elicitation point.

The actual card did not occur. `MCP_ELICITATION_VERTICAL_PROBE=FAIL`. An SDK fake-client form smoke, a trusted catalog entry and a connected server are not relabeled as a Desktop card PASS. These observations do not uniquely distinguish handler selection from pre-dispatch failure; no unobserved Hook notification or unsupported-UI root cause is invented.

Per the user's explicit failure condition, no second probe, alternate architecture, hidden conversation, runtime patch or Slurm cancellation was attempted after this failure. The installed, now-trusted candidate is retained; it was not rolled back.

## Read-only Job reconciliation

At `2026-10-20 02:32:39 UTC`, exact Job 5693449 still reported current owner, partition htzhulab, PENDING/JobHeldUser, Priority 0, RunTime zero, NodeList empty and AllocTRES null. No release occurred. No cancellation reservation exists. No second Job was created; no other Job mutation occurred.

`HOOK_TRUST=PASS`
`MCP_ELICITATION_VERTICAL_PROBE=FAIL`
`KEEP_TEST=NOT_RUN`
`CONFIRM_CANCEL_TEST=NOT_RUN`
`EXACT_CANCEL_COUNT=0`
`OTHER_JOB_MUTATION=NO`
`COMPLETE=NO`

Final-candidate CI, full candidate regression replay, G4, final review closure, G5 and formal release/install closure were not completed and are not claimed. No version was bumped. README checked: no update required.
