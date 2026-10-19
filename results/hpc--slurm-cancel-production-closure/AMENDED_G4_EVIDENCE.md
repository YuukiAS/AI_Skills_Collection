# Amended G4 execution evidence

Task: `hpc--slurm-cancel-production-closure`
Implementation candidate: `a8765b97b69c319304cb51dbd271d57ed8492c34` (unchanged)
Plan revision: `1`; PLAN commit `c11dc034001512dc8660648f9709ad9948103273`; CURRENT commit `00bead37571634e6af5ad5eba85a261cece60a3c`.
Resource authority: `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_G4_RESOURCE_AMENDMENT_V3_1_2026-10-20.md` at `8e1f982885b84d6149109503bf2441467b2d97a0`, read directly from that Git object.

## Read-only resource qualification

- Partition `htzhulab`: UP, allows account `rc_htzhu_pi`, QoS `gpu_access,gpu_access_patron`.
- Current association: `longleaf|aereinh|rc_htzhu_pi||gpu_access,gpu_access_patron,normal|normal`.
- Selected QoS `gpu_access`: `MinTRES=gres/gpu=1`, maximum `cpu=16,mem=128G`; no memory minimum or maximum walltime specified in QoS.
- `scontrol show node g180702 -a` reports A100 GRES and `CfgTRES` with generic `gres/gpu=8`; no typed/H100 request is necessary.
- Installed Slurm 25.11.6 documentation supports untyped `--gres=gpu:1`, memory units in MB, and one-minute walltime resolution. Zero memory/time have special unlimited semantics and were not selected.
- Because the server enables `JobSubmitPlugins=lua` and its policy source is not readable locally, one official **read-only** `sbatch --test-only` validated the exact resource request, hold and future BeginTime before submission. The local official manpage explicitly says no job is actually submitted. This succeeded with `gpu:1`, CPU 1, memory `1M`, time `00:01:00`, hold and `now+25hours`. Its estimated number `5693345` had no Job record (`Invalid job id specified`). No failed submission/parameter adjustment was used to discover legal parameters.

## Exactly one Job

Same existing backend: PID `1618201`, Codex `0.160.1`, `CODEX_HOME=/users/a/e/aereinh/.codex`. The already verified fresh root Desktop thread `01a154da-7f35-7f52-9bc5-84e4623772b0` was resumed, not the old stale-snapshot thread. No new backend was started and no Hook/trust/config was changed.

Submission turn: `01a1550f-b9a8-7a93-b95c-384cb5451fb1`.
Nested command ID: `exec-5f4ed924-3e11-479e-9d0b-f902902708d4`.
One actual `sbatch` command completed successfully and returned **5693449**:

```sh
sbatch --parsable --partition=htzhulab --account=rc_htzhu_pi --qos=gpu_access --gres=gpu:1 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=1M --time=00:01:00 --hold --begin=now+25hours --job-name=hpc-pcancel-a8765b97-g4r1-20261019T164716Z --output=/dev/null --error=/dev/null --wrap='sleep 30'
```

Immediate native read-only command `exec-6f6267db-c7fe-4797-9022-cf731f6d1093`, and independent root read-only checks before and after the cancellation attempt, agreed:

```text
JobId=5693449
UserId=aereinh(397557)
Partition=htzhulab
Account=rc_htzhu_pi QOS=gpu_access
JobState=PENDING Reason=JobHeldUser Priority=0
SubmitTime=2026-10-19T12:47:42
EligibleTime=2026-10-20T13:47:42
StartTime=2026-10-20T13:47:42
RunTime=00:00:00 TimeLimit=00:01:00
NodeList= AllocTRES=(null)
ReqTRES=cpu=1,mem=1M,node=1,billing=1,gres/gpu=1
```

The Job was never released; no node/GPU was allocated. No replacement Job was created.

## First protected cancellation and precise stop

Cancellation turn: `01a15510-42a9-7d63-b907-85417d860d6d`.
Exact normal nested command: `scancel 5693449`.
Nested command ID: `exec-e4cc6da5-8fd1-44e8-9287-d9574eddc86d`.

The live native stream records `hook/started` and `hook/completed` for this exact call, source `user`, `/users/a/e/aereinh/.codex/config.toml`. Completion status is **blocked**, with `NEEDS_INTERACTIVE_CHAT_CONFIRMATION`, `mutation_count=0`, and the exact Job/partition. No matching commandExecution start occurred. Thus the original scancel did not launch.

The denial asks for a native question with keys `id`, `header`, `question`, `options`, `isOther=false`, `isSecret=false`, and choices `确认取消` / `保留 Job`. The execution thread stopped before calling request_user_input because the exposed native schema does not permit the last two keys. There was **no native question call or user answer**, and no PostToolUse cancellation. This is not a completed retain interaction.

Targeted source corroboration (not a reopened Hook-lifecycle investigation):

- Current exposed `request_user_input` schema lists only `id/header/question/options` for questions.
- Exact upstream `rust-v0.160.1@d27764b82f7118f674371e6d6e76271d9d606edb`, `codex-rs/core/src/tools/handlers/request_user_input_spec.rs:39-70`, constructs those four keys and disallows additional properties; lines 116-118 force `question.is_other=true` during normalization.
- Candidate `skills/tools/hpc/slurm-workflows/scripts/slurm_cancel_hook.py:196-210` generates six keys with `isOther=false`; lines 213-235 require that exact six-key object, and lines 385-388 reject a mismatch in PostToolUse.

The supported native question contract and the candidate's exact required question object are incompatible. No unsupported invocation, field deletion, manual answer relay, terminal prompt, raw cancellation or configuration workaround was attempted. The stream does **not** prove a server-side request rejection or a PostToolUse result, since neither was invoked. The observed product failure is inability to present the prescribed native question under the advertised schema.

The bounded run stops under the user's substantial-product-change stop condition. No candidate repair is implemented, no additional plan revision is created, and no review/G5/release PASS is claimed. The single exact Job remains held and future-dated pending further explicit recovery direction; it is not automatically cancelled as cleanup.

## Durable raw evidence and result

Durable machine-local directory:
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection/private/exports/hpc--slurm-cancel-production-closure/amended-g4-20261019T164716Z/`

- `backend-events.jsonl`: closed raw observer log, including earlier historical events and this bounded continuation; SHA256 `2c7ece0e07daf7f801e74aa8d1f81488fb7b5554ef93750b6e3b1aba7589be7d` verified after copying.
- `request_user_input_spec.rs`: exact inspected upstream source snapshot.

```text
TEST_JOB_ID=5693449
G4_HARMLESS_PROBE=PASS
G4=FAIL
KEEP_TEST=FAIL
CONFIRM_CANCEL_TEST=NOT_RUN
EXACT_CANCEL_COUNT=0
OTHER_JOB_MUTATION=NO
IMPLEMENTATION_CANDIDATE=a8765b97b69c319304cb51dbd271d57ed8492c34
INDEPENDENT_REVIEW=NOT_RUN
G5=NOT_RUN
PUBLISHED=NO
FORMAL_INSTALL_VERIFIED=NO
GLOBAL_HOOK_MUTATED=NO
PRODUCT_SOURCE_MUTATED=NO
NEXT_ACTION=RETURN_TO_PLANNER
```
