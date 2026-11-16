# Presentations Course-standard / CUHK Template Parity V2 — Frozen Specification

Date: 2026-11-14
Status: **FROZEN PLANNER AUTHORITY**

## 1. Goal

Make `course-standard` and `cuhk` two skins over one shared Beamer core.

Except for explicit brand differences, the same content must render with the same:

- fonts;
- font sizes;
- line heights;
- body margins;
- title/body/footer/header geometry;
- list spacing;
- semantic spacing;
- Question/Answer;
- captions/table notes;
- tables/code;
- column presets;
- diagrams/arrows;
- closing layout;
- section-navigation behavior.

This parity is executable and tested, not a prose aspiration.

## 2. Canonical core

Both skins consume:

`docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_FROZEN_SPEC_2026-11-14.md`

Production layout tokens must have one owner in shared core.

## 3. Allowed skin differences

### course-standard

- course-standard palette;
- no CUHK research logo/background;
- default course identity/source text;
- title brand slot may be empty or course identity.

### CUHK

- CUHK palette;
- approved CUHK logo;
- approved CUHK title/background assets;
- CUHK research brand identity/source text.

### Explicitly NOT skin-owned

- generated-text font identity;
- any role font size;
- body rail;
- frametitle vertical rhythm;
- semantic spacing;
- caption alignment;
- Question/Answer geometry;
- footer height/insets/navigation group;
- section-label font/budget;
- table/list/code geometry;
- diagram/arrow geometry;
- closing content rail.

## 4. Title-page parity

Brand assets may differ, but generated title/subtitle/author/institute/date boxes share:

- the same role typography;
- the same relative text anchors;
- the same maximum widths;
- the same line-break behavior for identical strings.

A CUHK background/logo may occupy explicit brand regions. It may not push generated title copy into a different geometry.

## 5. Footer parity

The footer has the same:

- divider position/weight;
- band height;
- left/right insets;
- source/identity region;
- native navigation group;
- page-number region;
- optical vertical-centering contract.

Only colour and identity text differ.

## 6. Header parity

Same:

- 6.8 pt bold section-label token;
- single-line rule;
- frame-count width budget;
- miniframe ownership;
- active/inactive state geometry;
- adjacent label gap;
- clickable section/miniframe destinations.

Colours may differ.

## 7. Semantic component parity

The two skins must render the same visible copy with identical semantic component geometry for:

- TeachingQuestion;
- TeachingAnswer;
- Term/Takeaway/Note/Conclusion roles;
- caption/table note;
- generated table;
- code/listing;
- equal/evidence columns;
- process diagram;
- closing.

## 8. Synthetic parity deck

Create one shared content fixture that exercises:

1. title page;
2. ordinary body + bullets;
3. Question → table → Answer;
4. figure + multiline caption + interpretation;
5. equal columns;
6. evidence/explanation columns;
7. table with wrap-sensitive semantic atom;
8. code block;
9. process diagram with arrows;
10. section with long but legal label;
11. substantive closing.

The exact same semantic source/manifest is rendered through both skins.

## 9. Parity comparison

### 9.1 Text-level exactness

For generated text:

- identical strings;
- identical line breaks;
- identical page assignment;
- identical text role mapping.

### 9.2 Font-level exactness

- same font identity;
- same size within 0.1 PDF pt;
- same weight/italic role;
- same baseline/leading contract.

### 9.3 Geometry

For generated objects outside explicit brand masks:

- x/y/width/height tolerance <=2 px at 1920×1080;
- same body rail;
- same semantic gaps within each token tolerance;
- same table/column geometry;
- same Q/A rule endpoints;
- same footer/header anchors.

### 9.4 Brand masks

Allowed masks are explicit rectangles/polygons corresponding only to:

- logo;
- brand background;
- approved decorative brand marks.

A mask may not cover generated text, tables, figures, Q/A, navigation, or body layout merely to hide parity drift.

## 10. CUHK legacy migration

Current canonical CUHK source under:

`plugins/codex/plugins/presentations/shared/templates/cuhk/beamer/source/`

contains legacy layout ownership.

Migration requirements:

- preserve approved brand assets;
- move generic typography/layout/component logic to shared core;
- keep compatibility path/imports where needed;
- make CUHK `skin.tex` or equivalent own only brand differences;
- do not retain duplicate token values that can drift from shared core.

## 11. Course-standard canonical template

Add:

`plugins/codex/plugins/presentations/shared/templates/course-standard/`

It must be a first-class canonical route, not a copy of STAT5060 source.

It consumes shared core and provides:

- course-standard skin;
- minimal source example;
- usage documentation;
- exact rendered reference deck;
- parity fixture integration.

## 12. Routing

Update template routing so:

- explicit CUHK research/group-meeting route => CUHK skin;
- explicit or repository-selected course-standard Beamer / teaching LaTeX route => course-standard skin;
- an explicit user template still overrides both;
- editable PPTX routes remain unchanged.

Do not force all teaching requests into Beamer when an editable PPTX/Slides format is explicitly requested.

## 13. Acceptance

Parity is accepted only if:

- both skins compile from the same shared core;
- synthetic parity deck passes text/font/geometry comparison;
- existing CUHK brand assets remain present;
- STAT5060 V19 style replay through course-standard matches the frozen shared-core contract;
- an unrelated CUHK research fixture still renders correctly;
- no duplicate generic layout-token owner remains in skin code.

## 14. Completion signal

```text
COURSE_STANDARD_TEMPLATE_ACCEPTED = YES
CUHK_SHARED_CORE_MIGRATION_ACCEPTED = YES
TEMPLATE_PARITY_ACCEPTED = YES
```

Only an independent integration/acceptance run may set these states.
