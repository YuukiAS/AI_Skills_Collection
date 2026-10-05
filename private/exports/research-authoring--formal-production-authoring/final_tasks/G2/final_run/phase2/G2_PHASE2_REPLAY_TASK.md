# G2 Phase 2 Final Candidate Task

Use the installed `research-writing` candidate through its normal incremental document-producing entry.

This is Phase 2 of the frozen G2 task. Phase 1 has received an independent `PHASE1=PASS`. Treat `G2_PHASE1_PASS_BASELINE.md` as the frozen accepted baseline.

Read the provided files:

- `PHASE2_DELTA.md`;
- `G2_RUBRIC.md`;
- `MATERIALIZED_PHASE2_DELTA.json`;
- `G2_PHASE1_PASS_BASELINE.md`;
- the four materialized Phase 2 delta evidence blobs.

Write all outputs under `outputs/`:

1. `G2_PHASE2_ADVISOR_UPDATE.md`  
   The complete updated advisor-facing research update. Apply RA2 minimal dependency closure: update only the claims, table entries, interpretation, uncertainty, and next-question language that are actually affected by the personalized partial-pooling delta. Preserve unrelated accepted Phase 1 structure and wording as much as possible.

2. `G2_PHASE2_CLAIM_EVIDENCE.md`  
   A claim-evidence map that includes the Phase 1 baseline anchors and new Phase 2 delta anchors, with clear labels for what changed.

3. `G2_PHASE2_ROUTE_EVIDENCE.md`  
   A route/evidence packet proving this was handled as Research Authoring incremental authoring, that the frozen Phase 1 baseline was used, that only the four Phase 2 delta blobs were newly introduced, and that no broad rewrite or task/rubric change occurred.

4. `G2_PHASE2_BASELINE_TO_UPDATED.diff`  
   A unified diff from `G2_PHASE1_PASS_BASELINE.md` to `G2_PHASE2_ADVISOR_UPDATE.md`.

Do not change the product task, rubric, delta, or source identity. Do not make the Phase 1 report look prescient. If the delta changes the scientific conclusion, state the change only to the degree supported by the four new files.
