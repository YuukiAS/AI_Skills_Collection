# Session Hook snapshot A/B evidence

Task: `hpc--slurm-cancel-production-closure`
Approved package: `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`
Original candidate: `8f8d29f78dfc0f39c7043580e8ea06bcc7e436a4`
Final source candidate: `a8765b97b69c319304cb51dbd271d57ed8492c34`

## Runtime and source

- Actual existing Desktop backend PID: `1618201`; code-mode-host PID: `1644298`, parent `1618201`.
- Backend binary: `/users/a/e/aereinh/.codex-cli-candidates/0.160.1/20261015T064058Z/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex`.
- Host binary: the same directory's `codex-code-mode-host`.
- Codex: `0.160.1`; current Desktop client: `26.908.40834`.
- A and B both use `gpt-6.1-sol`, `code_mode_only`, `unified_exec`, and `/users/a/e/aereinh/.codex`. The historical G4 model remains `gpt-5.6-sol`.
- A task-local diagnostic WebSocket client connected to the existing backend socket `/users/a/e/aereinh/.codex-run/as/b7587b26bdc509ee.sock`. No second app-server was started. It attached to A through loaded-thread resume, created B through that same backend, and captured live native notifications plus raw response items.
- `hooks/list` was used only to check the installed declaration's trust, never as proof of session consumption.

Exact inspected source is clean `rust-v0.160.1@d27764b82f7118f674371e6d6e76271d9d606edb`, locally at `/tmp/codex-rust-v0.160.1-source`:

1. `codex-rs/core/src/session/session.rs:1578`: build Hook config and `Hooks::new`; `:1689`: store the session-owned `ArcSwap` Hook object.
2. `codex-rs/core/src/session/mod.rs:2115`: explicit runtime refresh calls `refresh_hooks`; `:2118`: rebuild and replace the session Hook object. Editing disk bytes alone is not that operation.
3. `codex-rs/app-server/src/request_processors/config_processor.rs:172`: config batch-write reload is conditional on `reload_user_config`; `:356`: explicit reload refreshes loaded threads. Trust persistence alone is not proof that this refresh ran.
4. `codex-rs/app-server/src/request_processors/thread_processor.rs:1341`: new-thread task loads config before creating a new session.
5. `codex-rs/app-server/src/request_processors/thread_processor.rs:4269`: resume of an already loaded thread reuses that thread/session; `:3955` and `:3974`: cold resume loads config and constructs a resumed session instead.
6. `codex-rs/app-server/src/request_processors/catalog_processor.rs:614`: `hooks/list` loads configuration for cwd; it does not inspect the target thread's Hook object.

## Exact reinstall and trust

- Reinstalled with the original candidate's existing atomic installer; installation completed at epoch nanoseconds `1792424596842623359`.
- Recoverable backup: `/users/a/e/aereinh/.codex/slurm-protected-cancel/backups/pre-v3-20261019T154316Z`.
- Bytes outside the protected-cancel declaration remained SHA256 `29c85eaf8b89c9b092cf721c0b0436cd5d703c4c569c5e3fe86ac57ad93c4179`.
- The user completed normal trust; the existing backend reported all three final declarations trusted before A/B commands.
- Enforcement hashes were asserted before reinstall and again after the source-only boundary clarification:
  - supervisor: `4764d2d3a55328debce6c2037522d7a2332be6cc8efa01d19d8f91f406ae2117`
  - Hook: `74275496861a63d20beb8c55b17ec279217cdb3625d17321d24cc0a25b62ebe3`
  - runtime: `684166063c419425019d2416bad64080d90aea0da75f96803337d2c02e1a9927`
  - policy: `7afd293c43d5c186f051d52b5665793930a9909d562a634a919a0a86c1825735`
- Final PreToolUse declaration identity: `sha256:6ccd79ff1004c8ce1bd184903881a155dc1c3f7a24cd7520b556fb9e931ae228`.

## A: original, already loaded Desktop thread

- Thread: `01a15211-6a48-7262-adcd-f9d5ee5d485e`, created at epoch seconds `1792378235`, before reinstall.
- Turn: `01a154d7-c58d-7c60-ad0c-154911812e78`.
- Exact command: `printf '__HOOK_SESSION_PROBE_A__\n'`.
- Nested command ID: `exec-808c7283-d23f-46dd-a42a-a7fe4a78270e`.
- Native `hook/started` and `hook/completed` both occurred for `pre-tool-use:0:/users/a/e/aereinh/.codex/config.toml:exec-808c7283-d23f-46dd-a42a-a7fe4a78270e`.
- Completion was `failed`, `hook exited with code 1`; command then printed its A marker and exited zero.
- This was not the final fail-closed declaration, which emits valid JSON and exits zero even on runtime failure. The same session's pre-reinstall commands had native Hook failures with exit `127`; it retained the old declaration after its external target was replaced.
- Selected source is directly recorded as `user`, `/users/a/e/aereinh/.codex/config.toml`, display order `0`. The old declaration hash is `sha256:c262ae3e7433d97b164cc8f4d8c72ad3f4d5b54c8bcd3d2fee689dea614cddc9`; native run notifications themselves do not serialize the declaration hash.

## B: new thread after final install and normal trust

- Thread: `01a154d8-0e36-7f60-8a34-d09690340bca`, created at epoch seconds `1792424808`, after install/trust.
- Turn: `01a154d8-4227-7e93-8fac-b19440e1308c`.
- Exact command: `printf '__HOOK_SESSION_PROBE_B__\n'`.
- Outer exec call: `call_16af95f6a61f4d00a2b5f3ac08e09e60`.
- Nested command ID: `exec-8bfe15b6-0c59-4776-8d6f-f456216ffe6f`.
- The matching native Hook run started and completed normally, followed by commandExecution printing the B marker and exiting zero.
- In the same thread, harmless `scancel --help` then produced a native `blocked` completion with `SLURM_CANCEL_DENIED reason=unsupported_scancel_target_or_option`; no commandExecution started for it.
- Help-probe outer call: `call_0a69675024224427baf96f3a4b657711`; nested ID: `exec-83261b98-c1e5-47f3-bcdd-fe2f68ed2268`.

## Minimal authorized source clarification and final-candidate probe

The original Skill/installer did not expressly require the necessary fresh-session boundary. Candidate `a8765b97b69c319304cb51dbd271d57ed8492c34` adds installer manifest `fresh_session_required=true`, an explicit next action, a Skill paragraph, and one CLI regression proving unchanged rendered enforcement identities. No Hook, supervisor, routing, DII, CARE, permission, or trust logic was changed. All 39 focused/existing Slurm tests passed.

The user-authorized repeated fresh-thread probe for that new source candidate used:

- Thread: `01a154da-7f35-7f52-9bc5-84e4623772b0`.
- Turn: `01a154da-bd8b-7631-80de-ff90bc4fa290`.
- Outer call: `call_573143869f3241bab8621bba398871b5`.
- Nested ID: `exec-5debf6b7-9af8-4702-9b83-757ca1cf720c`.
- Exact ordinary command: `scancel --help`.
- Native Hook source: user config; event started, completed as `blocked`, feedback `SLURM_CANCEL_DENIED reason=unsupported_scancel_target_or_option`.
- No matching commandExecution start occurred; the dispatcher returned `Command blocked by PreToolUse hook` to the model. The real scancel launch count was zero.
- This is G4 harmless-probe PASS, not full G4 or release PASS.

## Frozen resource-contract stop

Only after that PASS, the final fresh thread attempted one submission, requesting `--partition=htzhulab --account=rc_htzhu_pi --qos=gpu_access --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=32M --time=00:01:00 --gres=none --begin=now+5hours`, harmless `/usr/bin/true`, unique name `hpc-pcancel-a8765b97-20261019T1553`.

- Turn: `01a154db-fcee-7242-9230-a005fcee3165`.
- Outer call: `call_f7c124e855214760b5c113d4cf36fd24`.
- Nested ID: `exec-768ceebb-edc4-43e4-acc1-ca01e4cb9fc8`.
- PreToolUse and PermissionRequest completed normally. The single sbatch process exited `1`: `QOSMinGRES`, `Batch job submission failed: Job violates accounting/QOS policy`.
- No JobId was returned; exact-name partition query returned no rows. No second submission was attempted.
- Read-only `scontrol show partition htzhulab -a` showed `Hidden=YES`, `State=UP`, `AllowQos=gpu_access,gpu_access_patron`.
- Read-only `sacctmgr show qos where name=gpu_access,gpu_access_patron format=Name,MinTRES -n -P` returned:

```text
gpu_access|gres/gpu=1
gpu_access_patron|gres/gpu=1
```

Both permitted QoS values require at least one GPU. The approved CPU-only/no-GPU contract therefore cannot be met under current site policy. No Job was created or mutated; retain/confirm and independent review/release were not run. No GPU or alternate partition was substituted. The verified installed Hook remains active and trusted; it was not rolled back after harmless-probe PASS.

## Durable raw evidence

Machine-local, non-public raw notifications, probe scripts and reinstall receipt are preserved at:

`/overflow/htzhu/mingcheng_new/AI_Skills_Collection/private/exports/hpc--slurm-cancel-production-closure/session-hooks-ab-20261019T154316Z/`

Closed observer `backend-events.jsonl` SHA256: `3e933af4641214630d48adb047045cd2ef495fa241ccd88c06a4bc8627fb57bb`.

## Outcome

`ROOT_CAUSE=STALE_SESSION_HOOK_SNAPSHOT`

The first divergence was the old session-owned Hook object, not the nested tool's supported lifecycle. A new session consumed the final declaration and blocked before shell launch. This validates the Hook boundary in a fresh Desktop session, but does not establish full protected-cancel acceptance.

`NEXT_ACTION=RETURN_TO_PLANNER` solely for the exact scheduler/resource-contract conflict. No successor or architecture change was created.
