# Presentations V19 Extraction — Orchestration Current State

Date: 2026-11-14
Status: **READY_FOR_GPT_WORK_AUTONOMOUS_EXECUTION**

## Parent orchestration branch

`work/presentations-v19-core-validator-template-promotion-20261114`

## Prepared implementation branches

1. `implementation/presentations-validator-v2-v19-20261114`
2. `implementation/presentations-shared-core-template-parity-20261114`

Both were created from the orchestration branch after all frozen specs and implementation goals were present.

## Frozen Planner authorities

- `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_FROZEN_SPEC_2026-11-14.md`
- `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_LAYOUT_CONTRACT_2026-11-14.yaml`
- `docs/frozen/PRESENTATIONS_VALIDATOR_V2_FROZEN_SPEC_2026-11-14.md`
- `docs/frozen/PRESENTATIONS_COURSE_STANDARD_CUHK_PARITY_V2_FROZEN_SPEC_2026-11-14.md`

## Longleaf implementation tasks

Validator:
`docs/goals/PRESENTATIONS_VALIDATOR_V2_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`

Shared core / templates:
`docs/goals/PRESENTATIONS_SHARED_CORE_TEMPLATE_PARITY_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`

## GPT Work integration/promotion task

`docs/goals/PRESENTATIONS_V19_INTEGRATION_ACCEPTANCE_AND_PROMOTION_GOAL_2026-11-14.md`

Master orchestrator:

`docs/operations/prompts/PRESENTATIONS_V19_GPT_WORK_ORCHESTRATOR_2026-11-14.md`

## External oracle

`YuukiAS/STAT5060-TA@tutorial`

`docs/frozen/2026-27/STAT5060_TUTORIAL_01_PRESENTATIONS_PLUGIN_EXTRACTION_AUTHORITY_V1.md`

## Required completion

The Work run is not complete until:

- Validator V2 independently accepted;
- shared Beamer core independently accepted;
- canonical course-standard template accepted;
- CUHK migrated to shared core and parity accepted;
- accepted implementation promoted to `AI_Skills_Collection/main`;
- exact main SHA read back;
- STAT5060 promotion receipt pushed;
- receipt states `READY_FOR_TUTORIAL_CONTENT_FINALIZATION`.

Do not modify Tutorial visible content before that receipt.
