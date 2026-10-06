# C2 G2 Phase 1 Input Manifest

Repository:

`YuukiAS/Reliable_Imaging_Inference`

Ref:

`dc0b2ea471e79c29963d2ed92575a77540d23425`

| Path | Git blob SHA | Role |
|---|---|---|
| `docs/RESEARCH_DIRECTION.md` | `6a681141c6e1229c008ed69063f80b9e3b46d768` | provisional scientific direction and evidence boundary |
| `docs/DATA_AND_ANNOTATION_NEEDS.md` | `89d0c0f66e9126dcab78198d9f5ab8f3345df685` | available data, missing evidence, annotation/resource boundary |
| `sources/SEMINAR_CARDIOVASCULAR_PHENOTYPE_2026-08.md` | `8b7bcf4a3d10d202dad1e5ef8cb8e670747da2be` | phenotype/cohort seminar evidence index |
| `sources/SEMINAR_CLINICAL_AI_AND_HEART_BRAIN_2026-08.md` | `5e4a7500ab8898b2a43ba18f4d7296b2b6a94382` | clinical-AI and heart-brain evidence/source boundary |
| `docs/notes/SEMINAR_ROADMAP_REFINEMENTS_2026-08-22.md` | `f1d9508a08617865ff7b7488e1763754a9f7ad0c` | incremental roadmap implications without later literature audit |

No other Reliable_Imaging_Inference file belongs to final Phase 1 input.

## Materialization

After pre-final Critic PASS, materialize only these exact blobs into a task-local read-only C2 G2 Phase 1 input directory. Phase 1 must not run from the full repository checkout.

The Phase 2 delta must not be materialized or exposed to the Phase 1 authoring context before independent `PHASE1=PASS`.
