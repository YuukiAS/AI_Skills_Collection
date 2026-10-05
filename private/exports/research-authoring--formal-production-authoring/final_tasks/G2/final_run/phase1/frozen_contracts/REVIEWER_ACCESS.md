# G2 Reviewer Access Contract

## Source access

Reviewer must have direct read access to:

- repository: `YuukiAS/Distributed_Imaging_Inference`
- exact ref: `c6ed0fb40c702936ec1f41454390ef188a5b4d97`
- exact Phase 1 paths/hashes in `PHASE1_INPUT_MANIFEST.md`
- exact Phase 2 paths/hashes in `PHASE2_DELTA.md`

The linked GitHub connector is the primary source path. If that surface cannot expose a required file during final review, Executor must materialize the exact blob into the AI_Skills task private export before the Gate starts and bind it by hash. Do not substitute a summary.

## Runtime isolation

Phase 1 generation receives a task-local snapshot containing only Phase 1 manifest files. Phase 2 delta is stored separately and withheld until `PHASE1=PASS`.

## Output access

Full Phase 1/Phase 2 Markdown, route receipts, source manifests and diffs must be stored under:

`private/exports/research-authoring--formal-production-authoring/final_tasks/G2/final_run/`

Tracked review packets under `results/research-authoring--formal-production-authoring/` may point to those files by hash/path but may not replace full-document review.

## Reviewer requirement

The independent Reviewer must read:
- all frozen raw inputs needed to verify claims;
- the full Phase 1 document;
- Phase 2 delta;
- frozen Phase 1 baseline;
- full Phase 2 document;
- baseline-to-Phase2 diff.

Summary-only or excerpt-only review cannot PASS G2.
