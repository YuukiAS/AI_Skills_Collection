# G2 Phase 1 Input Manifest

Repository: `YuukiAS/Distributed_Imaging_Inference`
Commit: `c6ed0fb40c702936ec1f41454390ef188a5b4d97`

Git blob SHAs bind the exact raw inputs.

| Path | Git blob SHA | Role |
|---|---|---|
| `results/care_clean_subject_disjoint_2026-09-04/experiment_contract.json` | `bb39b2b5c697dece8a592d4163d59c477e0c3184` | clean CARE experiment definition |
| `results/care_clean_subject_disjoint_2026-09-04/clean_replication_pattern_decision.json` | `fc8f2635ae0e698cdf626a52421aef806f2bf35c` | clean replication decision |
| `results/care_pattern_h_robustness_2026-09-04/pattern_h_robustness_decision.json` | `74ff50a4bf7bf68beb47f451d16ddf021290d47e` | H-ROBUST decision |
| `results/care_pattern_h_robustness_2026-09-04/paired_bootstrap_ci.csv` | `3d5eff2fd1d3b3e99c391cdf5e474de89fdffe44` | uncertainty/effect evidence |
| `results/mms_replication_2026-09-04/mms_experiment_contract.json` | `190b97e77e30ec85ae5873759d9fd58ae510a98f` | supporting M&Ms experiment definition |
| `results/mms_replication_2026-09-04/mms_replication_decision.json` | `c41cb36586708a4361b94f43c95e794c87f48eb0` | supporting replication decision |

No other DII file is part of the Phase 1 final input.

## Materialization

After pre-final Critic PASS, copy these exact blobs to:

`private/exports/research-authoring--formal-production-authoring/final_tasks/G2/runtime_input/phase1/`

Preserve path names or provide a manifest mapping. Record content hashes after materialization.

Do not expose the full DII checkout to the Phase 1 generation runtime.

## Explicit exclusions

The following are not Phase 1 inputs even though they exist at the same repository commit:

- `deliverables/group_meeting_2026-09-05/**`
- `deliverables/group_meeting_2026-10-03/**`
- existing DII advisor reports
- all `results/care_personalized_partial_pooling_2026-09-04/**`
- all Phase 2 files named in `PHASE2_DELTA.md`

Phase 1 must not use those files for structure, wording, interpretation, or result knowledge.
