# Presentations V19 Extraction — Integration, Independent Acceptance and Plugin Promotion Goal

Repository: `YuukiAS/AI_Skills_Collection`
Integration branch: `work/presentations-v19-core-validator-template-promotion-20261114`

Owner: GPT Work, not Longleaf Codex.

## Objective

Integrate the two independent implementation candidates, run Planner-held acceptance that the implementers did not see, repair only demonstrated failures through fresh Longleaf Codex tasks, and promote the accepted shared core / validator / templates into the Presentations plugin.

Completion means the plugin main branch contains the accepted implementation and STAT5060 receives an exact promotion receipt declaring:

`READY_FOR_TUTORIAL_CONTENT_FINALIZATION`

## Inputs

Frozen specs:

- `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_FROZEN_SPEC_2026-11-14.md`
- `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_LAYOUT_CONTRACT_2026-11-14.yaml`
- `docs/frozen/PRESENTATIONS_VALIDATOR_V2_FROZEN_SPEC_2026-11-14.md`
- `docs/frozen/PRESENTATIONS_COURSE_STANDARD_CUHK_PARITY_V2_FROZEN_SPEC_2026-11-14.md`

Implementation goals:

- `docs/goals/PRESENTATIONS_VALIDATOR_V2_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`
- `docs/goals/PRESENTATIONS_SHARED_CORE_TEMPLATE_PARITY_LONGLEAF_IMPLEMENTATION_GOAL_2026-11-14.md`

External oracle:

- `YuukiAS/STAT5060-TA@tutorial`
- `docs/frozen/2026-27/STAT5060_TUTORIAL_01_PRESENTATIONS_PLUGIN_EXTRACTION_AUTHORITY_V1.md`

## Phase A — before dispatching implementers

GPT Work must construct a held-out acceptance plan before Longleaf implementation begins.

Do NOT send the exact hidden mutations/expected rows to Longleaf.

Held-out classes must cover:

### Authority/integrity

- duplicate JSON keys;
- source path substitution;
- source blob omission;
- source commit mismatch;
- fake relocation authority;
- derivative feedback field drift;
- component field drift;
- artifact ID/hash namespace confusion;
- partial reviewed pages with global PASS;
- missing lock evidence;
- missing baseline/candidate/tree;
- exact historical evidence locator missing;
- coordinated multi-field attacks.

### Layout/render

- font one step below token;
- local font shrink/scale;
- body rail drift;
- item gap below hard line / inside target / review region;
- paragraph→table crowding;
- caption centered;
- caption above object;
- Answer rule starting at label;
- footer source shifted;
- section label over dynamic budget;
- accidental table semantic-atom wrap;
- connector <6 mm;
- connector 6–8 mm;
- connector >=8 mm with collision;
- closing full-bleed body rail regression;
- large whitespace + tiny/crowded content;
- large intentional whitespace without objective contradiction.

### Parity

- font size drift in one skin;
- changed body margin in one skin;
- caption alignment drift;
- Q/A geometry drift;
- hidden text drift under an overbroad brand mask;
- CUHK brand-only differences that should pass.

Store the held-out pack in GPT Work private working state until implementation candidates stop. Do not commit exact hidden payloads to branches visible to Longleaf before acceptance.

## Phase B — integrate candidate branches

Receive exact candidate commits from:

1. Validator V2 implementation branch.
2. Shared-core/template parity implementation branch.

Verify each claims only its allowed completion state.

Integrate onto the integration branch using explicit commits. Resolve only genuine overlap at the shared layout-contract interface. Do not relax frozen specs to make integration easy.

## Phase C — public/full regression

Run all repository tests relevant to Presentations plus both candidate public suites.

Require:

- no existing Presentations regressions;
- both course-standard and CUHK compile;
- synthetic parity fixture runs;
- Validator V2 CLI runs;
- no import from STAT5060 production code;
- exact plugin routing remains valid.

## Phase D — held-out acceptance

Run the private held-out pack from a fresh read-only context.

Acceptance rules:

### Validator

- zero false PASS on explicit human-rejected / hidden negative cases;
- exact V19 oracle has zero deterministic FAIL;
- REVIEW remains REVIEW when intended;
- all historical V1 Auditor root classes are caught;
- no fixture/mutation-name branching.

### Templates

- shared core has one token owner;
- course-standard and CUHK parity passes outside explicit brand masks;
- existing CUHK research fixture remains usable;
- course-standard reproduces V19-derived core behavior;
- brand masks do not cover generated text geometry.

### Pipeline

- deterministic PASS never substitutes for rendered semantic review;
- plugin docs/routing describe the new boundary truthfully.

## Phase E — bounded repair loop

If acceptance fails:

1. GPT Work writes a compact finding packet with root mechanism, counterexample and required behavior.
2. Dispatch a fresh Longleaf Codex task on the relevant implementation branch.
3. Longleaf may change implementation/tests only; frozen specs and held-out expected answers remain hidden.
4. Re-integrate exact repair commit.
5. Re-run public regression.
6. Re-run held-out acceptance from fresh state.

Do not ask the user to relay ordinary repair cycles.

Stop for user only if:
- frozen Planner authorities materially conflict;
- required brand/source asset is inaccessible;
- GitHub/Longleaf runtime prevents implementation;
- a semantic product decision genuinely has no frozen answer.

## Phase F — independent acceptance report

After all gates pass, write:

- Validator V2 acceptance report;
- shared-core acceptance report;
- course-standard/CUHK parity report;
- held-out mutation summary by class, without exposing reusable exploit payloads;
- final changed-file manifest;
- exact integrated candidate commit.

States may then be:

```text
VALIDATOR_V2_ACCEPTED = YES
SHARED_CORE_ACCEPTED = YES
COURSE_STANDARD_TEMPLATE_ACCEPTED = YES
CUHK_SHARED_CORE_MIGRATION_ACCEPTED = YES
TEMPLATE_PARITY_ACCEPTED = YES
```

## Phase G — plugin promotion

Promote the accepted implementation to the Presentations plugin.

Required work:

- update canonical plugin files;
- update template routing;
- update Presentations changelog/TODO states;
- document Validator V2 as the production validator;
- retain V1 history without routing new production through it;
- make canonical course-standard available;
- make canonical CUHK consume shared core;
- preserve existing supported public paths through compatibility wrappers where needed.

Run the complete post-promotion test suite on the exact promotion candidate.

Open a PR to `main` with evidence. If repository policy and checks allow automated merge, merge it. If branch protections require an external human action, leave the PR fully ready and report the exact blocker; do not claim promotion complete until main contains the code.

After main contains the accepted implementation, read back the exact main SHA.

## Phase H — write back to STAT5060

On `YuukiAS/STAT5060-TA@tutorial`, create:

`docs/handoffs/2026-27/STAT5060_TUTORIAL_01_PRESENTATIONS_PLUGIN_PROMOTION_RECEIPT_V1.md`

It must include:

- AI Skills accepted main commit;
- Validator V2 version/path;
- shared-core version/path;
- course-standard template path/version;
- CUHK template path/version;
- acceptance report paths;
- parity result;
- V19 replay result;
- statement that V19 style remains the Tutorial style oracle;
- statement:

`READY_FOR_TUTORIAL_CONTENT_FINALIZATION`

Do not modify Tutorial visible content in this task.

## Final completion

This orchestration is complete only when:

1. AI Skills main contains the accepted implementation;
2. exact main SHA is recorded;
3. STAT5060 promotion receipt exists on remote `tutorial`;
4. both remotes are read back;
5. no ordinary implementation blocker remains.

Then stop. The next task is Tutorial content finalization under frozen style and promoted validator/template.
