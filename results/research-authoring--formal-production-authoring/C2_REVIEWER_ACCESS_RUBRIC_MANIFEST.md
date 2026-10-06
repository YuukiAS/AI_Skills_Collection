# C2 Reviewer Access / Rubric Manifest

Task: `research-authoring--formal-production-authoring`  
Candidate: `ac501d988f00cb6672fec105ae5fd51a0679cae0`

## G1

- Case bank:
  `private/exports/research-authoring--formal-production-authoring/c2_pre_final/G1/G1_CASE_BANK.md`
- Rubric:
  `private/exports/research-authoring--formal-production-authoring/c2_pre_final/G1/G1_RUBRIC.md`
- Reviewer needs final normal-runtime route evidence bound to C2, not static trigger metadata alone.

## G2

- Phase 1 scope:
  `.../c2_pre_final/G2/PHASE1_RAW_SCOPE.md`
- Phase 1 manifest:
  `.../c2_pre_final/G2/PHASE1_INPUT_MANIFEST.md`
- Phase 2 delta:
  `.../c2_pre_final/G2/PHASE2_DELTA.md`
- Rubric:
  `.../c2_pre_final/G2/G2_RUBRIC.md`
- Access:
  `.../c2_pre_final/G2/REVIEWER_ACCESS.md`

External source access:

```text
YuukiAS/Reliable_Imaging_Inference
Phase1 ref = dc0b2ea471e79c29963d2ed92575a77540d23425
Phase2 ref = 0c1fa13f6a4149b012f13191afed164a648478ec
```

Reviewer must directly read complete frozen inputs, Phase 1 output, Phase 2 delta, baseline, updated output and diff.

## G3

- Task:
  `.../c2_pre_final/G3/TASK_IDENTITY.md`
- Source manifest:
  `.../c2_pre_final/G3/SOURCE_MANIFEST.md`
- Project authority:
  `.../c2_pre_final/G3/PROJECT_AUTHORITY.md`
- Package subset:
  `.../c2_pre_final/G3/PACKAGE_SUBSET.md`
- Rubric:
  `.../c2_pre_final/G3/G3_RUBRIC.md`
- Access:
  `.../c2_pre_final/G3/REVIEWER_ACCESS.md`

External source access:

`YuukiAS/CARE_Challenge@75a40e454de43b64e59a0b0b438ff57ef2bb8345`

Reviewer must directly inspect complete manuscript source/PDF and primary source evidence.

## G4

- C2 task reuse:
  `.../c2_pre_final/G4/REUSED_TASK_DECISION.md`
- Offline wrapper composition:
  `.../c2_pre_final/G4/OFFLINE_WRAPPER_COMPOSITION.md`
- Wrapper manifest:
  `.../c2_pre_final/G4/WRAPPER_MANIFEST.md`
- Existing frozen rubric, unchanged:
  `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/CHAT_CODEX_HANDOFF_RUBRIC.md`
  blob `a7bf0b765bd9bf6d5b5a6acdf31c3a5b6bf6c5ad`

G4 Reviewer eventually needs:

- new C2 G2 PASS semantic baseline;
- complete fresh ChatGPT-stage package;
- wrapper exact-C2 identity;
- independent Chat-stage review;
- Codex handoff;
- exact C2 `research-main` production evidence;
- final PDF/render QA;
- post-render Research Authoring scientific QA.

The first historical G4 FAIL package remains visible only as regression evidence.

## Access failure

If any required source/artifact is unavailable in the review surface, final Gate cannot PASS from summaries. Materialize the exact source/artifact under the AI_Skills private export with hashes before review.
