# Authorized replacement G4 acceptance — 2026-10-21

Frozen runtime candidate: `3e81802ab0251d3bf31ec2d808d4e3273505b2f6`.
Control head before this checkpoint: `d9b52d944623252ddfa8c79cb695b059c457bdce`.

## Current-user authorization and preserved boundary

On 2026-10-21 the user explicitly authorized exactly one replacement held/future test Job to complete live retain then confirm acceptance. This supersedes the previous no-second-Job restriction only for this one replacement. No third Job is authorized. Job 5693449 remains historical successful confirmation evidence and must not be mutated again.

The original submission evidence was read from `AMENDED_G4_EVIDENCE.md`; its approved resource contract was read directly from `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_G4_RESOURCE_AMENDMENT_V3_1_2026-10-20.md` at `8e1f982885b84d6149109503bf2441467b2d97a0`. Current read-only inspection again confirmed partition/account eligibility, the allowed `gpu_access` QoS, and `MinTRES=gres/gpu=1`. `htzhulab` is hidden; its partition readback required `scontrol show partition htzhulab -a`.

All seven installed manifest files and all four frozen source/rule files were checked unchanged. The three task-owned handlers remain enabled and natively trusted with no load errors. No source, Hook, policy, SDK, trust or reload change was made. The existing 54/69/401-test and successful candidate-CI evidence remains same-runtime evidence; it was not rerun before this live acceptance.

## Exactly one replacement submission

A durable task-local one-shot submission intent was created with exclusive creation and fsync before the direct submission. This is evidence of the bounded submission attempt, not a new cancellation authorization path or wrapper.

Exactly one direct command returned Job **6028303**:

```sh
sbatch --parsable --partition=htzhulab --account=rc_htzhu_pi --qos=gpu_access --gres=gpu:1 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=1M --time=00:01:00 --hold --begin=now+25hours --job-name=hpc-pcancel-3e81802a-g4replacement-20261021T090547Z --output=/dev/null --error=/dev/null --wrap='sleep 30'
```

Immediate direct read-only `scontrol show job -o 6028303` proved:

```text
JobId=6028303
UserId=aereinh(397557)
Partition=htzhulab
Account=rc_htzhu_pi QOS=gpu_access
JobState=PENDING Reason=JobHeldUser Priority=0
RunTime=00:00:00 TimeLimit=00:01:00
SubmitTime=2026-10-21T05:06:33
EligibleTime=2026-10-22T06:06:33
NodeList= AllocTRES=(null)
ReqTRES=cpu=1,mem=1M,node=1,billing=1,gres/gpu=1
```

The scheduler timestamps are site-local. BeginTime is 25 hours after submission. The Job has not been released or allocated. The product audit contains the original Job's sole historical invocation and zero replacement cancellation invocations. No other Job was mutated by this task.

Durable private intent: canonical-checkout `private/exports/hpc--slurm-cancel-production-closure/replacement-g4-submission-intent.json`. It records the returned JobId and submission count one. Never submit another Job when resuming this checkpoint.

Initial pre-request checkpoint (superseded by the actual response below):

```text
ORIGINAL_CONFIRM_JOB_ID=5693449
ORIGINAL_CONFIRM_PATH=PASS
G4_REPLACEMENT_JOB_ID=6028303
REPLACEMENT_SUBMISSION_COUNT=1
REPLACEMENT_JOB_REMAINS_HELD=YES
NODE_ALLOCATED=NO
REPLACEMENT_EXACT_CANCEL_COUNT=0
KEEP_TEST=NOT_RUN
REPLACEMENT_CONFIRM_TEST=NOT_RUN
OTHER_JOB_MUTATION=NO
G4=INCOMPLETE
COMPLETE=NO
```

## Actual first native response and terminal verification

The user sent the exact cancellation request for 6028303. The ordinary tool attempt remained blocked; the trusted MCP handler issued the same required two-option form. Its actual wire response was:

```json
{"action":"accept","content":{"decision":"confirm"}}
```

No `retain` response was received. The executor cannot independently observe the physical client click and does not infer it from the user's earlier stated intent. The expected retain assertion failed against the actual response and consumed pending state; it is not a successful keep test.

Audit identity: `b0432e985742d5653897c17a320954a1792256aa15a7a48e65b76818151e2e1f`.
Root session/metadata thread: `01a1572b-d446-7fa3-94cf-95f978b0efde`.
Turn: `01a15db8-b5c3-7c32-af1d-2580f77b455c`.
Tool use: `exec-c68d38e7-c52d-425e-b311-6154dc239215`.

The real confirm response consumed the exact pending identity and created one durable reservation. Exact final re-resolution, one frozen invocation, return code 0 and reconciliation were recorded. Direct read-only `scontrol` and independent `sacct` both verified Job 6028303 terminally CANCELLED, with elapsed/runtime zero, AllocNodes=0 and no assigned node. No second cancellation attempt was made.

The complete private audit/pending/reservation snapshot and hashes are durable in canonical-checkout `private/exports/hpc--slurm-cancel-production-closure/replacement-g4-confirm-20261021/`. The submission intent was atomically updated to terminal cancellation, retaining submission count one and forbidding further Jobs.

Current truthful status:

```text
ORIGINAL_CONFIRM_JOB_ID=5693449
ORIGINAL_CONFIRM_PATH=PASS
G4_REPLACEMENT_JOB_ID=6028303
REPLACEMENT_SUBMISSION_COUNT=1
KEEP_TEST=NOT_RUN
REPLACEMENT_CONFIRM_TEST=PASS
REPLACEMENT_EXACT_CANCEL_COUNT=1
REPLACEMENT_JOB_TERMINALLY_CANCELLED=YES
NODE_ALLOCATED=NO
OTHER_JOB_MUTATION=NO
G4=INCOMPLETE_KEEP_NOT_RUN
COMPLETE=NO
```

The product audit contains exactly one invocation for each of the two authorized JobIds and no other target. Neither Job may be mutated again. A third Job is explicitly forbidden. Do not request another cancellation, simulate retain, substitute deterministic tests for the missing live acceptance, change frozen product code, or silently waive the release gate. Independent final acceptance, main integration, version closure and formal release remain gated by the missing live retain evidence.
