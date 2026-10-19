# Protected-cancel v3 execution evidence

Task: `hpc--slurm-cancel-production-closure`
Approved package: `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`
Current implementation candidate: `8f8d29f78dfc0f39c7043580e8ea06bcc7e436a4`

This file records process and runtime evidence only. It does not claim G4, independent Reviewer PASS, G5, release, or task completion.

## G1-G3 deterministic evidence

- Focused protected-cancel and existing Slurm regression: 38 tests passed on the final candidate.
- Full repository GitHub Actions run: `39272745060`, head SHA `8f8d29f78dfc0f39c7043580e8ea06bcc7e436a4`, all jobs passed.
- Local Skill validation passed for 155 active skills and 18 profiles.
- Local Codex Marketplace validation passed for 10 plugins and 29 active skills.
- `slurm_routing.py`, DII, and CARE were not changed.
- The installer test bank covers qualified Python 3.9+, sanitized runtime selection, staged qualification, atomic activation, recoverable backup, declaration-only config mutation, missing/127/nonzero/signalled/timed-out interpreter, corrupt identities, malformed Hook output, protected/unprotected targets, retain/confirm, replay, target drift, multi-target identity, unsupported command forms, subagent/headless rejection, and four unrelated working directories.

## Real Codex Hook normal-entry fault injection

- Runtime: Codex CLI `0.160.1`, model `gpt-5.6-sol`, ephemeral normal `codex exec` entry.
- Hook declaration and runtime were rendered from final candidate `8f8d29f78dfc0f39c7043580e8ea06bcc7e436a4` into a disposable `/tmp` runtime.
- The selected child interpreter wrapper qualified successfully and was then changed to exit `127` before the real Codex invocation.
- Codex selected `PreToolUse` and reported `Command blocked by PreToolUse hook: SLURM_CANCEL_DENIED reason=hook_runtime_failure`.
- Codex completed normally and did not report an ordinary raw Hook-process failure.
- The unique underlying Bash marker remained absent; observed Bash launch count was zero.
- No Slurm command or Job was used by this probe.

## Controlled Longleaf installation

- Live declaration source: `/users/a/e/aereinh/.codex/config.toml`.
- Task-owned runtime root: `/users/a/e/aereinh/.codex/slurm-protected-cancel/`.
- Selected production interpreter: `/usr/bin/python3.9` in the sanitized environment; no loader override was required.
- Bytes outside the protected-cancel declaration block remained identical before and after installation: SHA256 `29c85eaf8b89c9b092cf721c0b0436cd5d703c4c569c5e3fe86ac57ad93c4179`.
- A recoverable pre-v3 config/runtime backup exists inside the task-owned runtime backup directory.
- Installed identities:
  - supervisor SHA256: `4764d2d3a55328debce6c2037522d7a2332be6cc8efa01d19d8f91f406ae2117`
  - Hook SHA256: `74275496861a63d20beb8c55b17ec279217cdb3625d17321d24cc0a25b62ebe3`
  - runtime JSON SHA256: `684166063c419425019d2416bad64080d90aea0da75f96803337d2c02e1a9927`
  - policy JSON SHA256: `7afd293c43d5c186f051d52b5665793930a9909d562a634a919a0a86c1825735`
- Fresh official `hooks/list` sees the same enabled user-level `PreToolUse`, `PermissionRequest`, and `PostToolUse` declarations from the worktree, canonical repository, and `/tmp`, with the expected matchers and no load errors.

## Current human gate

The final declaration bytes differ from the previously trusted candidate, so fresh `hooks/list` currently reports all three declarations as `modified`. Existing trust state was preserved and was not rewritten or bypassed for production. The user must explicitly trust the final three declarations before the harmless production `scancel --help` probe.

Until that happens:

- `scancel --help` has not been run against the live final candidate;
- no Slurm test Job has been created;
- no Slurm Job has been mutated;
- G4, independent implementation review, G5, and release remain pending.
