# Presentations Shared Beamer Core V1 — Frozen Specification

Date: 2026-11-14
Status: **FROZEN PLANNER AUTHORITY**
Implementation repository: `YuukiAS/AI_Skills_Collection`
Source oracle: `YuukiAS/STAT5060-TA` Tutorial V19

## 1. Purpose

Extract the human-accepted STAT5060 V19 presentation style into one generic Beamer shared core consumed by both:

- `course-standard`
- `cuhk`

This specification governs generated slide geometry and component behavior. Skins may brand the core; they may not independently redefine typography, spacing, body geometry, semantic components, or validator semantics.

Exact source authority:

- STAT5060 V19 production commit: `62678cd22409906797474752ae4f304f867d96cc`
- STAT5060 style-freeze commit: `d019fd53513682004c154d6d0e6ea76b2099296b`
- V19 PDF SHA-256: `88eae6b2073715729abd9c2b004d1d0f31541c4314c2b64cd49194346b35d6e1`
- extraction authority: `docs/frozen/2026-27/STAT5060_TUTORIAL_01_PRESENTATIONS_PLUGIN_EXTRACTION_AUTHORITY_V1.md` in `YuukiAS/STAT5060-TA@tutorial`

Older STAT5060 parity/reviewer documents are evidence only. They do not override V19.

## 2. Architecture

Canonical target:

```text
plugins/codex/plugins/presentations/shared/
  templates/
    _shared/
      beamer-core-v1/
        core.tex
        typography.tex
        geometry.tex
        semantic-components.tex
        navigation.tex
        layout-contract.yaml
        README.md
    course-standard/
      beamer/
        source/
          main.tex
          skin.tex
    cuhk/
      beamer/
        source/
          main.tex
          skin.tex
          assets/...
```

Compatibility wrappers may preserve existing public paths, but production typography/layout code must have one owner under the shared core.

## 3. Skin boundary

### Shared core owns

- aspect-ratio geometry;
- generated-text font identities;
- role font sizes, weights and leading;
- body rail;
- frametitle rhythm;
- list grammar;
- semantic spacing grammar;
- column presets;
- table/code/caption rules;
- Question/Answer;
- section navigation geometry and label budget;
- footer geometry and native navigation group;
- density/compression rules;
- diagram/node/arrow grammar;
- closing-page geometry;
- validator-facing semantic role names.

### Skin may own only

- palette;
- logo and approved brand assets;
- title-page brand background;
- default brand/identity text;
- brand-specific source/credit text;
- approved decorative brand regions that do not move shared text geometry.

A skin must not change body rail, font size, line height, caption alignment, semantic spacing, section-label budget, Q/A geometry, footer height, or closing geometry.

## 4. Typography

Design values are fixed. Measurement tolerance is not authoring freedom.

| Role | Canonical TeX size/leading | Expected PDF size |
|---|---:|---:|
| frame title | 13 / 15.5 pt | ~12.951 pt |
| body | 11 / 13.5 pt | ~10.959 pt |
| semantic subhead | body token | ~10.959 pt |
| table | 10 / 12.2 pt | ~9.963 pt |
| code | 8 / 9.6 pt | ~7.970 pt |
| caption/table note | 8 / 9.6 pt | ~7.970 pt |
| footer/source | 8 / 9.6 pt | ~7.970 pt |
| section navigation | 6.8 / 7.4 pt bold | ~6.775 pt |
| closing Questions | 16 / 19.2 pt | ~16 pt |

Production fallback by shrinking fonts is forbidden.

## 5. Font identities

Use the existing Presentations fixed font policy:

- Latin generated text: TeX Gyre Termes
- Math: TeX Gyre Termes Math
- cal/bfcal: New Computer Modern Math
- CJK: Noto Serif SC / Noto Sans SC
- Code: Latin Modern Mono

No host-font guessing or runtime fallback.

## 6. Geometry

Canonical extracted mode is 16:9.

- ordinary body rail: 8 mm left/right;
- ordinary content uses `\textwidth`, not paper-width overlays;
- shared title/footer/header geometry is token-owned;
- 4:3 support, if retained elsewhere, must be a separately validated geometry adapter and may not mutate the 16:9 core tokens.

## 7. Semantic spacing

Measure rendered visible-object bounds.

| Relation | Target PDF pt | FAIL below |
|---|---:|---:|
| list item → next list item | 3–7 | 2 |
| paragraph → list | 5–12 | 3 |
| paragraph → table | 7–14 | 4 |
| paragraph → figure | 7–14 | 4 |
| paragraph → display math | 5–12 | 3 |
| display math → table | 7–14 | 4 |
| display math → body | 5–12 | 3 |
| table → interpretation | 7–17 | 5 |
| caption → body | 6–12 | 4 |
| Question → next object | 8–15 | 6 |
| within group | 5–15 | 4 |
| between groups | 9–22 | 7 |

Teaching-list defaults:

- body leading remains 13.5 pt;
- item separation 4 pt;
- token-authorized range 3–6 pt;
- `itemsep=0`, reduced local baselineskip and raw negative spacing are forbidden.

Values outside target but above hard failure become REVIEW unless a stronger semantic rule applies.

## 8. Columns

Default presets:

- equal peers: 0.48 / 0.48
- evidence-left: 0.57 / 0.39
- evidence-right: 0.39 / 0.57

Sequential arguments are vertical. Columns require true peers or a stable evidence/explanation pair. Custom ratios are REVIEW unless an archetype explicitly owns them.

Same-role peers must share declared optical anchors within 2 px at 1920×1080.

## 9. Captions and table notes

- below the owned object;
- left-aligned to that object within 2 px;
- multiline remains ragged-right;
- caption explains identity/reading, not the main scientific conclusion;
- no “short caption centered” exception exists in the final core.

## 10. Question / Answer

Question:
- accent rule;
- bold accent label;
- italic question copy.

Answer:
- bold accent label outside/above the rule;
- one continuous accent rule begins at answer-body optical top and ends at final answer-body optical bottom;
- endpoint tolerance ~2 px;
- answer body remains upright.

## 11. Footer

Shared structure:

```text
[credit/source] ... [native slide nav][native section nav] [x/N]
```

- theme-colour divider;
- same shared band height and insets;
- left source/identity is optically vertically centred;
- native right-side navigation remains clickable;
- skin changes colour/identity, not geometry.

## 12. Section navigation

- fixed 6.8 pt bold label;
- single line;
- no shrink/wrap fallback;
- adjacent visible gap >=12 px at 1920×1080;
- width cap based on section frame count:

[
W_{cap}(n_s)=34+38rac{n_s}{n_{max}} 	ext{PDF pt}.
]

- >100% = FAIL;
- 90–100% = REVIEW;
- over-budget wording must be shortened.

## 13. Tables

- booktabs-style generated tables;
- semantic atoms must not wrap accidentally;
- fix width/layout before type;
- dense tables may not drop below the frozen table token;
- table-to-interpretation spacing uses the shared role.

## 14. Density and whitespace

Automatic validation must never equate “nonblank” or “acceptable total occupancy” with good composition.

Hard failures include:

- overflow/collision;
- font/leading compression to fit;
- spacing below hard relation limits;
- unauthorized deletion;
- required-object clipping;
- objectively invalid table/arrow/component geometry.

Whitespace/density detectors are triage:

- large lower/internal void + objectively undersized/crowded primary region => FAIL when both parts are measurable;
- large void without an objective contradiction => REVIEW;
- high semantic-block density without a hard violation => REVIEW;
- no whitespace trigger firing never grants aesthetic PASS.

Whole-slide rendered review remains mandatory for visual balance.

## 15. Diagram / arrow

- shared node/edge styles;
- connectors bind node boundaries;
- no text/node collision or crossings unless semantically intentional and separately reviewed;
- no arbitrary shorten hacks;
- ordered-process shaft:
  - <6 mm FAIL
  - 6–8 mm REVIEW
  - >=8 mm eligible for PASS after endpoint/collision/peer checks
  - 8–10 mm preferred.

## 16. Closing

Default substantive closing archetype:

- normal body rail;
- upper/lower functional split ~68/32;
- upper region holds headline/takeaways;
- lower region centres fixed 16 pt Questions cue;
- Questions centre approximately 78% of body height ±4%;
- skin may add approved brand background without moving the shared content rail.

A different closing archetype requires explicit planner authority; a skin may not silently invent one.

## 17. Shared-core parity invariant

Given identical visible content and the same 16:9 archetype, `course-standard` and `cuhk` must produce the same:

- text strings and line breaks;
- font identities/sizes/leading;
- text/object bounding boxes within tolerance;
- body margins;
- semantic spacing;
- columns;
- captions;
- Q/A;
- tables/code geometry;
- header/footer placement;
- page number;
- closing geometry.

Allowed skin differences:

- colour values;
- logo/background/decorative brand pixels;
- default brand identity/source text.

Brand masks must be explicit in parity tests; they may not hide generated text geometry.

## 18. Compatibility and migration

The current CUHK `beamerthemesintef.sty` is legacy implementation. It may remain as a compatibility wrapper, but duplicated layout logic must be removed or delegated to the shared core.

The new canonical course-standard Beamer route must consume the same shared core.

Existing exact-CUHK assets remain authoritative brand assets.

## 19. Acceptance

This shared core is not promoted merely because it compiles.

Promotion requires:

- exact STAT5060 V19 replay;
- historical negative replay;
- unrelated teaching and research fixtures;
- course-standard/CUHK parity fixtures;
- independent validator acceptance;
- no production imports from STAT5060;
- no duplicated layout token ownership between skins.
