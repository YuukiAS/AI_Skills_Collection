# GPT Work Orchestrator — Presentations V19 Extraction to Plugin Promotion

## Mission

Continue autonomously from the frozen V19 extraction package and complete the Presentations infrastructure work through plugin promotion. The user should not have to relay ordinary Codex rounds.

Use GPT Work 5.6 with high/very-high reasoning as the default. Do not spend Ultra merely for implementation supervision. Escalate reasoning only if frozen authorities genuinely conflict or independent acceptance produces a non-local architectural contradiction.

## Repositories

### Infrastructure
`YuukiAS/AI_Skills_Collection`

Orchestration/integration branch:
`work/presentations-v19-core-validator-template-promotion-20261114`

### Real-use oracle
`YuukiAS/STAT5060-TA`

Branch:
`tutorial`

## First action

Remote-read the actual current HEAD of both branches. Do not assume the SHAs in this prompt remain current.

Then read in full, in this order:

1. `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_FROZEN_SPEC_2026-11-14.md`
2. `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_LAYOUT_CONTRACT_2026-11-14.yaml`
3. `docs/frozen/PRESENTATIONS_VALIDATOR_V2_FROZEN_SPEC_2026-11-14.md`
4. `docs/frozen/PRESENTATIONS_COURSE_STANDARD_CUHK_PARITY_V2_FROZEN_SPEC_2026-11-14.md`
5. `docs/goals/PRESENTATIONS_VALIDATOR_V2_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`
6. `docs/goals/PRESENTATIONS_SHARED_CORE_TEMPLATE_PARITY_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`
7. `docs/goals/PRESENTATIONS_V19_INTEGRATION_ACCEPTANCE_AND_PROMOTION_GOAL_2026-11-14.md`
8. old Validator V1 spec + all three Auditor finding packets
9. current Presentations plugin routing, visual QA, authoring workflow and CUHK template source.

From STAT5060 read:

`docs/frozen/2026-27/STAT5060_TUTORIAL_01_PRESENTATIONS_PLUGIN_EXTRACTION_AUTHORITY_V1.md`

and the exact V19 frozen files it names.

## Role split

### GPT Work owns

- Planner authority interpretation;
- held-out acceptance design and secrecy;
- exact branch/commit coordination;
- integration;
- independent acceptance;
- deciding whether a finding is implementation failure vs frozen-authority conflict;
- final plugin promotion;
- final write-back receipt to STAT5060.

### Longleaf Codex owns

- code implementation;
- refactors;
- tests;
- compiling/running fixtures;
- producing candidate reports;
- bounded repairs after Work findings.

Longleaf does not decide frozen rules and does not self-accept.

## Phase 0 — hidden acceptance before implementation

Before sending implementation prompts, construct the held-out benchmark classes required by the integration goal.

Keep exact hidden mutations/expected results private from Longleaf until candidates stop.

Do not weaken the benchmark because an implementation is difficult.

## Phase 1 — two Longleaf branches in parallel

Use these already-prepared child branches if present; otherwise create them from the orchestration branch HEAD:

- `implementation/presentations-validator-v2-v19-20261114`
- `implementation/presentations-shared-core-template-parity-20261114`

### Longleaf task A

Send the exact implementation task from:

`docs/goals/PRESENTATIONS_VALIDATOR_V2_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`

Require commit + push and exact candidate SHA.

### Longleaf task B

Send the exact implementation task from:

`docs/goals/PRESENTATIONS_SHARED_CORE_TEMPLATE_PARITY_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`

Require commit + push and exact candidate SHA.

Run these in parallel. Do not let them share an implementation branch.

Do not expose held-out acceptance payloads.

## Phase 2 — Work integration and independent acceptance

After both branches stop:

- remote-read exact candidate commits;
- inspect their reports and diffs;
- integrate onto the orchestration branch;
- run full public regression;
- run the held-out pack from a fresh read-only context.

Follow exactly:

`docs/goals/PRESENTATIONS_V19_INTEGRATION_ACCEPTANCE_AND_PROMOTION_GOAL_2026-11-14.md`

## Phase 3 — autonomous repair

For every acceptance failure:

1. write a short root-cause finding packet;
2. route it to the correct Longleaf branch;
3. start a fresh Codex implementation context;
4. do not reveal unrelated hidden cases;
5. obtain a new commit;
6. integrate;
7. rerun public tests;
8. rerun held-out acceptance fresh.

Do not ask the user to forward prompts or choose routine fixes.

Do not solve acceptance failures by editing frozen thresholds/specifications.

## Phase 4 — promotion

Only after independent acceptance:

- mark Validator V2 accepted;
- mark shared core accepted;
- mark course-standard/CUHK parity accepted;
- update canonical Presentations plugin files/routing/changelog;
- retain compatibility wrappers where required;
- run post-promotion full test suite;
- open PR to main and merge when repository policy/checks permit.

If an external branch-protection action is genuinely required, stop with the ready PR and the exact required action. Otherwise complete the merge yourself.

After merge, read back exact `AI_Skills_Collection/main` SHA.

## Phase 5 — STAT5060 write-back

Create on `YuukiAS/STAT5060-TA@tutorial`:

`docs/handoffs/2026-27/STAT5060_TUTORIAL_01_PRESENTATIONS_PLUGIN_PROMOTION_RECEIPT_V1.md`

with the exact accepted plugin main SHA, component paths/versions and acceptance evidence.

The receipt must end with:

`READY_FOR_TUTORIAL_CONTENT_FINALIZATION`

Do not modify Tutorial visible content.

## Stop condition

Stop only when either:

### Success

- plugin main contains accepted implementation;
- main SHA is verified;
- STAT5060 receipt is pushed and remote-read;
- status is `READY_FOR_TUTORIAL_CONTENT_FINALIZATION`.

### Genuine blocker

Only:
- frozen Planner authorities conflict materially;
- required protected/brand asset cannot be accessed;
- GitHub/Longleaf platform prevents implementation/promotion;
- a semantic product decision is truly missing.

Routine test failures, implementation bugs and review findings are not user blockers.

## Final user report

Use natural Chinese, concise:

- whether steps 1–4 are complete;
- accepted AI Skills main SHA;
- Validator V2 status;
- shared-core/template parity status;
- STAT5060 receipt path;
- whether Tutorial content finalization can now begin.

Do not dump internal logs or held-out mutation details.
