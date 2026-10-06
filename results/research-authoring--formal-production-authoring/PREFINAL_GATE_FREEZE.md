# Research Authoring C2 Pre-Final Gate Freeze

Task: `research-authoring--formal-production-authoring`  
Branch: `work/research-authoring--formal-production-authoring`  
Date: 2026-10-06

## Candidate identity

```text
C2_CANDIDATE_READY=YES
C2_FINAL_CANDIDATE_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT=
eafb5e11ec65e54259b99fea44fe169096b9dcb9

DEVELOPMENT_EVIDENCE_PACKET_HEAD=
7d780ca50b67785877a87af0ada967f8389254c2

FINAL_GATES_NOT_STARTED=YES
```

Promotion authority:

`docs/design/059_RESEARCH_AUTHORING_C2_PROMOTION_ADMISSION_CRITIC_REVIEW_V0_1_2026-10-06.md`
@ `a0bf3b3e6ccdc827a39923920c13baa452d4bd26`

Promotion record:

`results/research-authoring--formal-production-authoring/C2_PROMOTION_FREEZE.md`

Shared replay infrastructure is validation infrastructure only and is not part of the Research Authoring product candidate.

## Historical final evidence disposition

- predecessor G1: regression only;
- DII G2: regression only;
- MoSAIC G3: regression / should-not-change only;
- first historical G4 ChatGPT package: immutable FAIL regression only.

No predecessor final PASS can be combined with C2.

## G1 — C2-bound / frozen / not started

Case bank:

`private/exports/research-authoring--formal-production-authoring/c2_pre_final/G1/G1_CASE_BANK.md`

Rubric:

`private/exports/research-authoring--formal-production-authoring/c2_pre_final/G1/G1_RUBRIC.md`

C2 final G1 must directly replay natural entry and owner boundary, including the standalone formal-PDF report path repaired in C2.

```text
G1_C2_BOUND=YES
G1_FINAL_EXECUTION_STARTED=NO
```

## G2 — new fresh two-phase task / frozen / not started

Project:

`YuukiAS/Reliable_Imaging_Inference`

Phase 1 ref:

`dc0b2ea471e79c29963d2ed92575a77540d23425`

Phase 2 delta ref:

`0c1fa13f6a4149b012f13191afed164a648478ec`

Frozen packet:

- `c2_pre_final/G2/PHASE1_RAW_SCOPE.md`
- `c2_pre_final/G2/PHASE1_INPUT_MANIFEST.md`
- `c2_pre_final/G2/PHASE2_DELTA.md`
- `c2_pre_final/G2/G2_RUBRIC.md`
- `c2_pre_final/G2/REVIEWER_ACCESS.md`

Phase 1 must not see Phase 2 files before independent `PHASE1=PASS`.

```text
G2_FRESH_TASK_FROZEN=YES
G2_PHASE1_RAW_SCOPE_FROZEN=YES
G2_PHASE2_DELTA_FROZEN=YES
G2_FINAL_EXECUTION_STARTED=NO
```

## G3 — new fresh manuscript task / frozen / not started

Project:

`YuukiAS/CARE_Challenge`

Ref:

`75a40e454de43b64e59a0b0b438ff57ef2bb8345`

Task:

create a manuscript-ready technical paper package from the CARE failure-forensics evidence plus later verified CARE-ASE negative result, without upgrading the deferred rescue blueprint into a completed method.

Frozen packet:

- `c2_pre_final/G3/TASK_IDENTITY.md`
- `c2_pre_final/G3/SOURCE_MANIFEST.md`
- `c2_pre_final/G3/PROJECT_AUTHORITY.md`
- `c2_pre_final/G3/PACKAGE_SUBSET.md`
- `c2_pre_final/G3/G3_RUBRIC.md`
- `c2_pre_final/G3/REVIEWER_ACCESS.md`

```text
G3_FRESH_MANUSCRIPT_TASK_FROZEN=YES
G3_FINAL_EXECUTION_STARTED=NO
```

## G4 — C2 offline wrapper / G2 reuse / not started

G4 continues to reuse the C2 G2 scientific baseline after full G2 PASS.

The ordinary natural request and existing frozen rubric are unchanged.

C2 packet:

- `c2_pre_final/G4/REUSED_TASK_DECISION.md`
- `c2_pre_final/G4/OFFLINE_WRAPPER_COMPOSITION.md`
- `c2_pre_final/G4/WRAPPER_MANIFEST.md`

Unchanged frozen rubric:

`private/exports/research-authoring--formal-production-authoring/final_tasks/G4/CHAT_CODEX_HANDOFF_RUBRIC.md`

No evaluation-only command blacklist is allowed.

```text
G4_REUSED_TASK=G2
G4_OFFLINE_C2_BINDING_FROZEN=YES
G4_LIVE_PLUGIN_MUTATION_AUTHORIZED=NO
G4_FINAL_EXECUTION_STARTED=NO
```

## Pre-final admission state

```text
C2_CANDIDATE_READY=YES
PREFINAL_PACKET_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```

Only independent pre-final Critic PASS may admit G1-G4 final execution. Live Plugin update remains separately user-authorized even after pre-final PASS.
