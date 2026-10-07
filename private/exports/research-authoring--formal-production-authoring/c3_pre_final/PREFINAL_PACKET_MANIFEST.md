# C3 pre-final packet manifest

Task: `research-authoring--formal-production-authoring`

```text
C3_FINAL_CANDIDATE_COMMIT=9e88d7eda1749c09bac0ed97562909a90810ccdb
FINAL_GATES_NOT_STARTED=YES
LIVE_PLUGIN_MUTATION=NO
PAID_API=NO
MAIN_MERGE_RELEASE=NO
READY_FOR_CHATGPT_FINAL_REVIEW=YES
```

## Scope-corrected authority

- Critic PASS: `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_CRITIC_REVIEW_V0_1_2026-10-07.md`
- Gate matrix: `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_CAPABILITY_GATE_MATRIX_V0_1_2026-10-07.md`

## G1

- `G1/G1_CASE_BANK.md`
- `G1/G1_RUBRIC.md`

## G2

Copied unchanged from the approved G2 final-task packet:

- `G2/PHASE1_RAW_SCOPE.md`
- `G2/PHASE1_INPUT_MANIFEST.md`
- `G2/PHASE2_DELTA.md`
- `G2/G2_RUBRIC.md`
- `G2/REVIEWER_ACCESS.md`

## G3

Copied unchanged from the approved G3 final-task packet:

- `G3/TASK_IDENTITY.md`
- `G3/VENUE_PROJECT_AUTHORITY.md`
- `G3/PACKAGE_SUBSET.md`
- `G3/G3_RUBRIC.md`
- `G3/REVIEWER_ACCESS.md`

## G4

- `G4/REUSED_TASK_DECISION.md`
- `G4/CHAT_CODEX_HANDOFF_RUBRIC.md`
- `G4/WRAPPER_COMPOSITION.md`
- `G4/WRAPPER_MANIFEST.json`
- `G4/research-authoring-wrapper-0.3.1-c3-9e88d7ed.tar.gz`

## Should-not-change

- `SHOULD_NOT_CHANGE_BANK.md`

## Live wrapper authorization timing

Before any ChatGPT wrapper final evidence is collected, obtain one fresh bounded user authorization for the exact hash-bound C3 wrapper:

```text
archive=G4/research-authoring-wrapper-0.3.1-c3-9e88d7ed.tar.gz
archive_sha256=4783abc0b95c1a0775b9d801825d822819fa5426a8a38a418ad16759a028b388
scope=USER
discoverability=PRIVATE
skills_only=YES
```

If wrapper identity, scope, discoverability, and archive hash remain unchanged, that same authorization covers both G1 and G4. This pre-final packet does not authorize live Plugin mutation.

## Packet status

```text
PREFINAL_PACKET_READY=YES
FINAL_GATES_STARTED=NO
READY_FOR_CHATGPT_FINAL_REVIEW=YES
```
