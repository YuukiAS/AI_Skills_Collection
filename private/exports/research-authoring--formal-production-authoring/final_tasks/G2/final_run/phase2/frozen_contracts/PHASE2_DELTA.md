# G2 Phase 2 Frozen Evidence/Decision Delta

Gate: G2  
Frozen before Phase 1 starts: YES  
Visible to Phase 1: NO

Repository: `YuukiAS/Distributed_Imaging_Inference`  
Commit: `c6ed0fb40c702936ec1f41454390ef188a5b4d97`

## Exact delta

| Path | Git blob SHA | Delta role |
|---|---|---|
| `results/care_personalized_partial_pooling_2026-09-04/experiment_contract.json` | `4d7661f340f8e893eaffaf991b7045760042bbf6` | follow-up personalization/partial-pooling experiment contract |
| `results/care_personalized_partial_pooling_2026-09-04/personalization_gate_decision.json` | `8e063c0af3cc4f097b59a998f06c6fef95043576` | final decision labels/interpretation |
| `results/care_personalized_partial_pooling_2026-09-04/gap_closure_summary.csv` | `97bc144aa3399e3dde75c62411656575e4f59636` | quantitative gap-closure evidence |
| `results/care_personalized_partial_pooling_2026-09-04/paired_bootstrap_ci.csv` | `5764bf36da252ab63ac5cc269ca26a5f80856ca5` | uncertainty/effect evidence |

These four files are the complete Phase 2 final delta. Additional personalized-partial-pooling narrative reports are not allowed to steer the update.

## Required Phase 2 action

After independent Reviewer marks Phase 1 `PHASE1=PASS`:

1. freeze the exact Phase 1 document as baseline;
2. materialize only the four delta blobs above into:
   `private/exports/research-authoring--formal-production-authoring/final_tasks/G2/runtime_input/phase2_delta/`;
3. update the same document using the approved minimal dependency closure contract;
4. do not rebuild the document from scratch unless the delta demonstrably invalidates the document spine;
5. produce baseline, delta manifest, candidate and diff for Reviewer.

The candidate must derive the actual scientific interpretation from the frozen delta. This freeze does not prescribe a positive result.

## Anti-leakage rule

Phase 1 runtime must not see this file's scientific contents or the four delta blobs. The Executor may know the frozen identity for orchestration, but the Phase 1 generation context may contain only the Phase 1 manifest.

Changing any delta path/blob after Phase 1 output is seen terminates this final G2 attempt.
