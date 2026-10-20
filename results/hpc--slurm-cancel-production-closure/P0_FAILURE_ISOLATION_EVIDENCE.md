# P0: isolate unrelated Bash from Slurm runtime failure

Frozen implementation candidate: `3e81802ab0251d3bf31ec2d808d4e3273505b2f6`. Subsequent control/evidence checkpoints must not change its runtime source bytes. Resume from this task's CURRENT, normal reload and the required native trust gate; never create another Job.

This continues the existing task and preserves root/pending implementation `10f10017129bd59f2611885ecb24a080e80b3272`. No Slurm routing, confirmation protocol/UI, Codex, Bridge Kit, DII, CARE, or unrelated Hook is changed.

## Repair and deterministic evidence

The declaration now classifies the original event before mutable supervisor/hash/runtime/policy checks. Non-Bash events and definitely unrelated Bash return `{}`. Raw and shell-decoded scancel tokens and paths, unsupported compounds, and the protected sentinel enter the strict protected path. The inline parser uses a qualified system interpreter independently of the private guard interpreter and loader environment. Parser failure, timeout or missing output produces a valid deny for uncertain scope. The parallel MCP entry also classifies unrelated events before pinned runtime loading.

`python -m unittest discover -s tests -p 'test_slurm_protected_cancel*.py'`: **54 tests PASS**, 23.185 seconds.

Actual captured declarations were executed in subprocesses after their supervisor, guard, runtime, or policy bytes changed. For both PreToolUse and PermissionRequest, `git status --short`, `ls`, `python --version` and `printf harmless` returned `{}`. Exact/absolute/escaped/quoted scancel, help, compounds and the harmless sentinel remained denied; the fake scancel invocation count stayed zero. Separate tests cover broken private guard Python, missing scope-parser Python, and non-Bash events. Existing root/pending/MCP, retain, exact one-shot, drift and unprotected tests remain passing.

The previous outer-declaration infrastructure-failure test used unrelated `printf harmless` as its protected target. It now uses `scancel 12345`; strict cancellation protection remains required while unrelated Bash passthrough is verified separately.

`STALE_SESSION_ISOLATION=PASS` for the deterministic stale-declaration regression above. Production active-Hook verification is still required after installation, native trust, and normal reload.

## Current runtime checkpoint

Ordinary `git status --short` executed successfully from the canonical checkout before installation. The emergency-recovered live configuration currently has no protected-cancel declaration or server block, so this success is not misreported as active Slurm protection. The bounded installer must restore only this task's blocks, preserve all existing trust values and unrelated configuration, atomically install the frozen candidate, and perform the normal empty-edit config reload with `reloadUserConfig=true`.

After native trust of the three changed task-owned handlers, reload again and verify unrelated Bash, blocked scancel help, and the harmless Hook-to-MCP card before touching the single existing Job. No Job lookup, allocation, cancellation, or cancellation reservation occurred during this P0 repair. G4/G5, final CI/review/release and formal installation closure are not yet claimed. README unchanged; no version bump at this checkpoint.
