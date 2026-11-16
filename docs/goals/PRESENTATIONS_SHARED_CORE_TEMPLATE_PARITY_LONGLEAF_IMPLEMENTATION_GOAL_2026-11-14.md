# Presentations Shared Beamer Core + Course-standard / CUHK — Longleaf Codex Implementation Goal

Repository: `YuukiAS/AI_Skills_Collection`
Parent branch: `work/presentations-v19-core-validator-template-promotion-20261114`
Recommended child branch: `implementation/presentations-shared-core-template-parity-20261114`

## Objective

Implement the V19-derived shared Beamer core, canonical course-standard template, and CUHK migration so both skins consume the same core and differ only by approved brand skin fields.

Read first:

1. `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_FROZEN_SPEC_2026-11-14.md`
2. `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_LAYOUT_CONTRACT_2026-11-14.yaml`
3. `docs/frozen/PRESENTATIONS_COURSE_STANDARD_CUHK_PARITY_V2_FROZEN_SPEC_2026-11-14.md`
4. current `plugins/codex/plugins/presentations/shared/font-policy.md`
5. current CUHK template source/assets
6. current routing docs
7. current research presentation fixtures

Implementation only. Do not alter frozen Planner specs.

## Shared core

Create canonical shared core under:

`plugins/codex/plugins/presentations/shared/templates/_shared/beamer-core-v1/`

At minimum:

- core import;
- typography tokens;
- geometry/body rail;
- semantic spacing/list grammar;
- Question/Answer;
- caption/table-note;
- header/section navigation;
- footer;
- table/code roles;
- column presets;
- diagram/node/arrow styles;
- closing component;
- machine-readable layout contract;
- README.

The machine-readable contract must be generated from or byte-consistent with the frozen Planner contract. Do not hand-maintain a second set of numbers that can drift.

## Course-standard

Add canonical route:

`plugins/codex/plugins/presentations/shared/templates/course-standard/`

It must:

- consume shared core;
- provide only course-standard palette/identity skin;
- include minimal buildable example;
- include source-editable Beamer template;
- include usage docs;
- include rendered reference deck.

Do not copy STAT5060 text or PageIDs.

## CUHK migration

Keep approved CUHK brand assets.

Refactor the canonical CUHK Beamer route so:

- generic typography/layout/component code comes from shared core;
- CUHK skin owns palette, logos/backgrounds and identity text only;
- compatibility import paths remain usable where practical;
- no duplicate generic token owner remains in legacy style files.

Do not remove brand assets.

## Exact parity fixture

Build one shared synthetic semantic deck that exercises:

- title;
- ordinary bullets;
- Question→table→Answer;
- figure + multiline caption + interpretation;
- equal columns;
- evidence/explanation columns;
- wrap-sensitive table;
- code;
- process diagram;
- section label near budget;
- substantive closing.

Render exact same semantic content through course-standard and CUHK.

## Parity comparator

Implement a reusable parity checker that compares, outside explicit brand masks:

- strings;
- line breaks;
- font identity/size/weight;
- text/object bounding boxes;
- body rail;
- spacing;
- columns;
- caption/Q&A/table/code geometry;
- header/footer anchors;
- closing geometry.

Default geometry tolerance <=2 px at 1920×1080; font tolerance <=0.1 PDF pt.

Brand masks must be explicit and may cover only logo/background/decorative brand regions.

## Existing CUHK regression

Run at least one current real CUHK research fixture after migration.

Verify:

- brand assets still present;
- generated text uses shared font contract;
- research deck remains usable;
- no brand mask hides generated text drift.

## STAT5060 style replay

Materialize a de-course-specific style fixture from the exact V19 geometry and confirm course-standard shared core reproduces the frozen token/geometry contract.

Do not import course source at runtime.

## Routing

Update template routing so:

- explicit/repo-selected course-standard Beamer/teaching LaTeX uses canonical course-standard route;
- CUHK research/group-meeting uses CUHK route;
- explicit user template still wins;
- editable PPTX/Slides behavior remains unchanged.

## Tests

Add tests for:

- shared-core single ownership;
- skin cannot redefine frozen typography/spacing/body rail;
- parity fixture;
- brand masks;
- course-standard build;
- CUHK build/regression;
- routing.

## Completion

Produce:

- implementation report;
- parity report;
- CUHK regression report;
- course-standard reference render;
- changed-file manifest;
- candidate commit.

Allowed final state:

```text
SHARED_CORE_CANDIDATE_READY = YES
COURSE_STANDARD_CANDIDATE_READY = YES
CUHK_MIGRATION_CANDIDATE_READY = YES
READY_FOR_INTEGRATION_ACCEPTANCE = YES
CANDIDATE_COMMIT = <sha>
```

Do not claim final parity acceptance or plugin promotion.
