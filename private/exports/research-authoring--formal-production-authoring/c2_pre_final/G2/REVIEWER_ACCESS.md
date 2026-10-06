# C2 G2 Reviewer Access

Reviewer must have direct access to:

## Phase 1 source

`YuukiAS/Reliable_Imaging_Inference@dc0b2ea471e79c29963d2ed92575a77540d23425`

and every exact path/blob in `PHASE1_INPUT_MANIFEST.md`.

## Phase 2 delta

`YuukiAS/Reliable_Imaging_Inference@0c1fa13f6a4149b012f13191afed164a648478ec`

and every exact path/blob in `PHASE2_DELTA.md`.

## Final artifacts

After final execution, full artifacts must be under the C2 task private export and directly available to Reviewer:

- complete Phase 1 source/document;
- Phase 1 claim/evidence or route receipt;
- independent Phase 1 review;
- frozen Phase 1 baseline;
- exact Phase 2 delta materialization manifest;
- complete Phase 2 document;
- baseline-to-Phase2 diff;
- full route/runtime evidence.

GitHub connector direct read is the primary source path. If any source/artifact cannot be read directly, materialize the exact file into the AI_Skills private export and bind it by hash before review.

Summary-only review cannot PASS G2.
