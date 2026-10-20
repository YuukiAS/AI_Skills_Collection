# Live normal-entry confirmation — 2026-10-20

Implementation candidate: `3e81802ab0251d3bf31ec2d808d4e3273505b2f6`.
Control head before this evidence update: `0ab483a4328fafd6de21725abedd6c28c80e4125`.

## Actual execution

- The three task-owned handlers were enabled, natively trusted, and free of load errors. Current hashes equalled native trusted hashes. No trust state was synthesized or edited by the executor.
- Normal `config/batchWrite` with `edits=[]` and `reloadUserConfig=true` completed for loaded tasks.
- Actual canonical-checkout `git status --short` exited 0 with empty output; it was not denied by Slurm protection.
- Actual `scancel --help` was blocked by PreToolUse with `unsupported_scancel_target_or_option`; the real command process did not start.
- Before the real request, exact Job readback proved current owner, `htzhulab`, `PENDING / JobHeldUser`, `RunTime=00:00:00`, empty NodeList, and null allocated TRES. Pending and consumed directories had no JSON records. A read-only `sq` inventory included the held test Job.
- The user later sent the exact cancellation request in this same root chat. The ordinary `scancel 5693449` tool attempt was denied; it was not retried. The parallel trusted MCP handler handled confirmation and the protected mutation.

## Exact current-chat audit

Audit identity: `e240714f23c60a8649e88f7c785f41f10b7a63cde17008fa549fdf057476b987`.
Root session and MCP metadata thread: `01a1572b-d446-7fa3-94cf-95f978b0efde`.
Hook turn: `01a1598b-3e30-7881-a0a1-555f3c80e357`.
Tool use: `exec-3a6c2e53-47b5-486c-ae11-00f124ab5822`.

The immutable request audit records the actual required single-select schema with only `确认取消` / `保留 Job`. The answer audit records `action=accept`, `content.decision=confirm`. This is actual Hook-to-MCP evidence; it is not the earlier harmless direct probe, a reconstructed question, or a request-user-input call.

The command guard created the exact pending identity with its private nonce. The MCP handler consumed that identity, wrote a durable one-shot reservation, performed final exact scheduler re-resolution, recorded one invocation intent for `/usr/bin/scancel` with the sole target `5693449`, and recorded return code 0. The completed reservation and reconciliation remain durable. The original Bash invocation stayed blocked.

Read-only `scontrol show job -o 5693449` reported `JobState=CANCELLED`, current owner, the same partition, zero runtime and no allocated node. Independent accounting returned:

```text
5693449 | aereinh | htzhulab | CANCELLED by 397557 | 00:00:00 | AllocNodes=0 | None assigned | 0:0
```

The product audit has exactly one invocation intent and only Job 5693449 as its target. No other Job was mutated by this task. The subsequent read-only inventory contained the other jobs and no active test Job. Natural elapsed-time or scheduler-reason changes in other jobs are not represented as task mutations.

The full private audit/pending/reservation snapshot, SHA256 manifest and terminal-state receipt are durable in the canonical checkout at:

`private/exports/hpc--slurm-cancel-production-closure/post-confirm-20261020/`

No nonce or private scheduler inventory is included in this tracked evidence.

## Acceptance boundary

```text
HOOK_TRUST=PASS
UNRELATED_BASH_PASSTHROUGH=PASS
SLURM_HOOK_INTERFERENCE=NO
SCANCEL_HELP_BLOCKED_BEFORE_PROCESS=PASS
HOOK_TO_MCP_ELICITATION=PASS
ROOT_IDENTITY_BINDING=PASS
PENDING_IDENTITY_BINDING=PASS
CONFIRM_CANCEL_TEST=PASS
EXACT_CANCEL_COUNT=1
JOB_5693449_TERMINALLY_CANCELLED=YES
OTHER_JOB_MUTATION=NO
KEEP_TEST=NOT_RUN
G4=INCOMPLETE
G5=NOT_RUN
COMPLETE=NO
```

The first real form was confirmed. No live retain/held-Job acceptance occurred on this candidate. Deterministic retain coverage is supporting source evidence, not a substitute for the frozen real-Job gate. A second Job, another cancellation attempt, a fictitious retain result or an unapproved release waiver is prohibited. Release/version/main integration remains gated; this document does not claim final acceptance or formal release.

## Same-candidate regression

- Focused protected-cancel suite: 54 PASS, 22.104 seconds.
- Full Slurm suite: 69 PASS, 29.828 seconds.
- Skill validation and audit: exit 0.
- Marketplace validation, freshness and path report: exit 0.
- Registry generation compared with committed registry after excluding the generation timestamp: identical, 155 skills.
- All seven installed manifest files and all four frozen source/rule files checked byte-identical after cancellation.
- Initial full repository run: 401 tests, two read-only fixture-write failures. The authorized writable rerun passed all 401 tests in 125.821 seconds without product changes. The failed sandbox run and successful writable run are retained separately.

Logs are retained under the same canonical private task directory with `post-confirm-` names. No product runtime, policy, Hook declaration, README, version, or unrelated skill/plugin was changed during this acceptance attempt.
