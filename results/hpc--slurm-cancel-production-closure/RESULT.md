# hpc--slurm-cancel-production-closure

RESULT = PASS

## Product candidates

- AI Skills product commit: `4453808e02388725f47d3c0a278e5494fdd55478`
- DII consumer commit: `1a9d4b88c5b7a619e9510fc48db7b5d259338663`
- CARE consumer commit: `98a01cc2626de94c3087360524f909f15413f729`
- Branch in all three repositories: `work/hpc--slurm-protected-partition-chat-confirmation-v2-1`
- Publication: ordinary non-force bounded publisher PASS for all three branches.

## Installed global identity

- `CODEX_HOME`: `/users/a/e/aereinh/.codex`
- Hook source: user config only, `/users/a/e/aereinh/.codex/config.toml`
- Hook implementation:
  `/users/a/e/aereinh/.codex/slurm-protected-cancel/hooks/slurm-protected-cancel-1b4223d6013fb5b5083e526aa62394728c3e85849a753e835fa3c429a041f7fd.py`
- Hook content SHA-256: `1b4223d6013fb5b5083e526aa62394728c3e85849a753e835fa3c429a041f7fd`
- Private policy: `protected_cancel_partitions = ["htzhulab"]`
- `PreToolUse` key: `/users/a/e/aereinh/.codex/config.toml:pre_tool_use:0:0`
- `PreToolUse` current hash: `sha256:64e0bcdfc70491251df7e144af4cf940ad6236f8e9a8c7a012cc89300d041820`
- `PermissionRequest` key: `/users/a/e/aereinh/.codex/config.toml:permission_request:0:0`
- `PermissionRequest` current hash: `sha256:786a893875ea7a8fd98c4a1d2ce7573937c40b3b62c142c0471bc7e978397293`
- `PostToolUse` key: `/users/a/e/aereinh/.codex/config.toml:post_tool_use:0:0`
- `PostToolUse` current hash: `sha256:a37ea99a9dc4ca25797f86873179f926afd7b506061a3e83326208209a417419`
- All three statuses: `Trusted`.

Official `hooks/list` readback from AI Skills, DII, CARE and `/tmp` returned the
same three keys and hashes, `source=user`, `trustStatus=trusted`, and no warnings
or errors. No project-local Slurm Hook declaration remains in any of the three
canonical repositories.

## Removed surfaces

- `slurm-chat-guard` named permission profile: absent.
- `slurm-protected-cancel-global` named permission profile: absent.
- Slurm-specific `default_permissions`: absent.
- Project-local protected-cancel Hooks and private runtimes: absent.
- `automation-bin/scancel`, wrapper, shim and PATH interception: absent.
- Persisted confirmation token and next-shell consume flow: absent.
- User-visible Slurm permission mode added by this task: none.

## Behavior

- Non-protected exact cancellation receives no extra protected-cancel prompt and
  keeps Codex's ordinary permission and command behavior.
- A protected exact cancellation is denied by both `PreToolUse` and
  `PermissionRequest` with zero mutation and a deterministic native
  `request_user_input` contract.
- Only the dedicated `确认取消` response in a root interactive event can reach
  `PostToolUse`; it re-resolves the exact target, reserves a one-time identity,
  and invokes the frozen absolute cancellation executable once.
- Retain, empty, timeout, Other, free text, wrong target/partition, subagent,
  duplicate and replay cases produce zero mutation.
- Headless protected cancellation fails closed.
- DII and CARE consumers only propagate an exact cancellation intent; they do
  not start a cancellation subprocess or copy protected-partition authority.
- This is Codex normal-entry plus adapted-consumer enforcement. It does not claim
  same-UID operating-system hard isolation and does not alter an ordinary SSH
  terminal used directly by the user.

## Validation

- `python -m unittest tests.test_slurm_protected_cancel`: 12 PASS.
- `python -m unittest tests.test_slurm_protected_cancel_normal_entry`: 3 PASS.
- `python -m unittest tests.ops.test_slurm_cancel_chat_blocker`: 11 PASS.
- `python -m unittest discover -s tests`: 356 PASS.
- `python scripts/skills.py validate`: PASS, 155 active skills.
- `python scripts/skills.py audit --all`: PASS.
- Marketplace write/validate/check/path-report: PASS.
- Canonical AI Skills, DII and CARE task-owned production files were compared
  with their published candidates after installation.
- All cancellation behavior tests used fake executables and deterministic fake
  scheduler state.

## Scheduler truth

- `REAL_SLURM_COMMAND_THIS_RECOVERY = NO`
- `REAL_SLURM_MUTATION_THIS_RECOVERY = NO`
- Historical incident retained without reinterpretation:
  `ACCIDENTAL_REAL_SLURM_COMMAND = scancel 9101`
- `HISTORICAL_REAL_SLURM_MUTATION = UNKNOWN`
- No scheduler command was run to investigate Job 9101.

## Trust persistence

The Hook identity is tied to one user-level `CODEX_HOME` and immutable Hook
bytes, not to a repository, branch, worktree or task. New repositories, threads,
restarts and worktrees reuse the same trusted hashes. A future trust action is
needed only when the global Hook implementation or declaration actually changes.
