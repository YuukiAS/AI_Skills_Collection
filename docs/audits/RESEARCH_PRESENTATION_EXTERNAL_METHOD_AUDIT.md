# Research Presentation External Method Audit

Audit date: 2026-08-23

Reviewed Handoff task: `018_presentation_external_method_audit`

## Executive Conclusion

当前最大的架构缺口不是“缺少更多审美规则”，而是缺少一个可执行的 reference-calibrated composition layer。

本仓库已经有比较强的研究汇报规则：page archetype、evidence boundary、anti-card/dashboard、真实 PPTX render、Terra visual review、reference page lessons、016/017 的 regression benchmark。但当前链路仍然容易退化为：

```text
inspected reference page -> prose lesson -> generator凭经验重画
```

外部项目反复出现的有效机制是把“好 slide 的视觉组织”先变成更硬的中间对象，再让生成器在受约束的候选空间里选择和实现：

```text
source facts / paper evidence
-> slide job and headline
-> composition candidate(s)
-> locked visual system / geometry / layout family
-> rendered pixels
-> visual review
```

因此，019 的首要方向应是 **exemplar composition representation**，而不是先做完整 multi-candidate generator、不是继续扩 reference corpus，也不是继续写抽象 QA 文案。没有 composition representation，multi-candidate search 很容易只是换皮肤；有了 representation，后续的 candidate search、comparative Terra review、deck rhythm check 和 PPTX/Beamer 分路才有稳定输入。

上一轮 10 页 `RESEARCH_PRESENTATION_CURRENT_CYCLE_REVIEW_PACK` 应保留为 engineering / correctness / medium-quality baseline。它不能作为 gold visual exemplar：016/017 确实证明了可编辑 PPTX、真实 render、机械 QA、Terra 与 Planner handoff 能跑通，也关闭了 ASCII math、internal leakage、image/object-too-small 等低级问题；但它们仍是 synthetic benchmark，且用户已经明确否定其整体 Presentation 质量可作为成熟科研组会金标准。

## Current Repository Baseline

已存在能力：

- `research-presentations/SKILL.md` 明确要求 research-group-meeting 先建立 Research State / Evidence Board，再用 page archetype 选择页面，而不是从通用模板开始。
- `RESEARCH_SLIDE_ARCHETYPES.md` 已把 `RESULT_FIGURE`、`STATISTICAL_MODEL`、`MEDICAL_IMAGE_COMPARISON`、`NEGATIVE_RESULT` 等页面定义为 scientific job，不把 cards/tables/timelines 当 archetype。
- `visual-qa.md` 已要求真实 render、scientific object、5-10 秒理解、formula/label/readability、evidence boundary、anti-card/dashboard 和 independent visual reviewer。
- 016/017 增加了 reference_design_audit、audience-facing internal leak gate、math-source leak gate、medical image / overlay / endpoint QA、Terra maturity rubric。

缺口：

- Reference page lessons 当前主要是 prose metadata，不是可执行 composition object。
- 当前没有对 matched reference 和 generated candidate 做 side-by-side comparative selection。
- 当前没有内部生成 2-4 个真实内容 composition candidates 并用同一 evidence set 比较。
- 当前没有 deck-level composition rhythm representation，只能靠 contact sheet / reviewer 判断。
- PPTX 与 Beamer 的共享层仍偏 narrative/evidence/rule，缺少能分路投射到 native PPTX object 或 TeX/TikZ composition 的中间表示。

## Source Audits

### 1. zarazhangrui/frontend-slides

Source: https://github.com/zarazhangrui/frontend-slides

Inspected commit: `9906a34d640d2111f724544cbc50f7f130569ae1`

License: MIT.

Files inspected: `LICENSE`, `SKILL.md`, `plugins/frontend-slides/skills/frontend-slides/SKILL.md`, `html-template.md`, selected `bold-template-pack/templates/*/design.md`.

Actual mechanism:

- Uses a mandatory visual style discovery phase: generate three real single-slide previews before the full deck.
- Mixes safe preset, bold template and wildcard so choices differ in composition/visual thesis, not only color.
- Treats selected preview or selected `design.md` as a design recipe and locks typography, palette, spacing rhythm and component grammar for the full deck.
- Uses fixed 1920 x 1080 stage and screenshot checks for overflow/overlap.
- Explicitly bans visible workflow metadata in previews.

Research relevance:

- The strongest transferable mechanism is not its web aesthetic; it is `show, don't tell` plus design-system lock.
- For scientific decks, the preview packet must use real scientific content, not decorative hero slides.
- Its HTML-first route has higher design ceiling but is not enough for editable PPTX unless followed by a native translation path.

Gap versus current repo:

- Current repo has page-level reference lessons but no real candidate preview gate.
- It lacks a first-class object saying “this reference lesson becomes this layout grammar for this deck.”

Disposition: `candidate_for_future_adoption` for preview/candidate workflow concepts; do not copy template styling into research slides.

### 2. andyqiu847-ai/high-quality-slides

Source: https://github.com/andyqiu847-ai/high-quality-slides

Inspected commit: `30a90be3561e61580cd52800a43f867513a8b144`

License: MIT.

Files inspected: `LICENSE`, `README.md`, `plugin/skills/high-quality-slides/SKILL.md`, `plugin/skills/high-quality-slides/layouts.md`, `plugin/skills/high-quality-slides/html-template.md`.

Actual mechanism:

- Defines quality as research x narrative x visual system x per-slide layout decisions.
- Enforces a gated five-phase workflow: audience strategy, evidence, narrative outline, design system, build.
- Requires every slide outline item to contain headline assertion, one supporting fact and intended visual.
- Uses deck-wide design tokens and a layout-pattern vocabulary.
- Runs a self-check for source trace, overflow, color discipline, repeated layouts and chart junk.

Research relevance:

- The useful part is the productized slide-art-director framing: evidence and narrative are inputs to layout decisions.
- Its generic business/pitch presets are not directly suitable as academic quality standards.
- Its `chart-focus` rule is directly relevant: the chart fills most of the slide and the headline states the result.

Gap versus current repo:

- Current repo has scientific archetypes but not a candidate construction protocol that forces each page to name `headline + evidence + intended visual + layout`.
- Current repo has rules but not a preview/sample-slide approval gate.

Disposition: `concept_only` for phased workflow and layout vocabulary; avoid adopting its broad business preset taxonomy as-is.

### 3. brycewang-stanford/many-ppt-skills

Source: https://github.com/brycewang-stanford/many-ppt-skills

Inspected commit: `76bfca23f908b299d9e4737717b88b31a67cbcb2`

License: MIT for repository, plus `LICENSE-CODE` present.

Files inspected: `LICENSE`, `LICENSE-CODE`, `SKILL.md`, `skills/many-ppt-skills/SKILL.md`, `data/skills.json`, `principles/README.md`, all eight original principle files (`principles/01-show-dont-tell.md` through `principles/08-distill-dont-design.md`), and `scripts/render.py`.

Actual mechanism:

- It is a registry and comparison method, not a deck generator.
- It separates route choice by real constraints such as editable PowerPoint versus HTML-native, speaker notes, template mandate, offline, PDF.
- It records capability claims as documentation-backed verdicts, not tested truth.
- Its eight principles add a compact evidence-backed method layer:
  - `01-show-dont-tell`: use real-content visual options; do not ask users to specify taste abstractly.
  - `02-anti-ai-slop`: concrete banned lists work better than aspirational "make it beautiful" language.
  - `03-fixed-stage`: slides are fixed presentation compositions, not responsive web pages.
  - `04-constraint-beats-freedom`: lock palette/type/layout inventory where consistency matters.
  - `05-progressive-disclosure`: keep always-loaded skill files as workflow maps, loading detail only when needed.
  - `06-single-file`: for HTML artifacts, portability argues for self-contained output when the deck is an artifact.
  - `07-render-and-look`: rendered visual QA and contact sheets catch the defects source inspection misses.
  - `08-distill-dont-design`: durable rules should be distilled from repeated successful runs and failures, not imagined up front.

Research relevance:

- The route-question discipline is valuable: editable PPTX and HTML/Beamer have different design ceilings and should not be collapsed.
- `show-don't-tell`, `constraint beats freedom`, and `render-and-look` together support same-content candidate comparison plus design-system lock.
- `progressive disclosure` supports a future architecture where composition catalogs are indexed compactly and only selected records are expanded.
- `distill, don't design` is a warning that synthetic 5-page fixtures cannot alone define mature research quality.

Gap versus current repo:

- Current repo has a fixed route policy, but not a comparative registry of candidate composition mechanisms.
- Current rule set is partly distilled from failures, but the next stage needs positive exemplar-derived composition records.

Disposition: `concept_only`.

Repair note after `REVIEW_1`: all eight principle files were read and checked against the current recommendation. The conclusion remains unchanged: the transferable value for this repository is not to copy another registry, but to add a compact, reference-derived composition representation that can later drive candidate generation, design-system constraints and comparative rendered review.

### 4. RFYoung/slideweaver

Source: https://github.com/RFYoung/slideweaver

Inspected commit: `8735c40d5c7bfe647f35f293a902fc02cc81c9a4`

License: MIT.

Files inspected: `LICENSE`, `README.md`, `SKILL.md`, `assets/smart_layout.py`, `assets/deck_profile.py`, `assets/render_qa.py`, `assets/shape_cookbook.py`.

Actual mechanism:

- Builds academic PPTX with native editable objects via `python-pptx`, layout solver, deck profile and shape cookbook.
- Treats `python-pptx` as writer, not layout system; complex pages must be planned and solved before drawing.
- `smart_layout.py` validates bounds, overlaps, text capacity and connector clearance before PPT shape creation.
- `deck_profile.py` locks fonts/colors/safe frame from an existing deck or profile.
- `render_qa.py` scores PNG previews heuristically for focus, balance, density, whitespace and contrast.
- Explicitly requires render PDF/PNG and page comparison after each modification.

Research relevance:

- This is the strongest native editable PPTX mechanism among inspected sources.
- Its solver/cookbook pattern directly addresses our repeated failure modes: random arrows, overlapping boxes, tiny type and card overuse.
- It is Chinese academic-PPT oriented and includes practical Office corruption/chart checks.

Gap versus current repo:

- Current repo can generate/edit PPTX fixtures, but does not expose a reusable composition/geometry solver layer for research page functions.
- Current QA checks pixels and semantics, but not enough pre-render geometry constraints.

Disposition: `candidate_for_future_adoption` for layout-solver concepts and native object discipline; any code reuse requires separate intake and compatibility review.

### 5. wmyung/manuscript-to-editable-slides

Source: https://github.com/wmyung/manuscript-to-editable-slides

Inspected commit: `2b7c9b5b234384d69ee0c153aa98107fc3f037bc`

License: MIT.

Files inspected: `LICENSE`, `README.md`, `SKILL.md`, `references/layout_families.md`, `references/layout_rhythm.md`, `references/acceptance_tests.md`, `references/render_repair_loop.md`, `scripts/render_pptx.js`, `scripts/render_slide_previews.py`.

Actual mechanism:

- Converts scientific manuscripts into editable PPTX while preserving source order, numbered figures/tables and paragraph coverage.
- Uses a normalized paper bundle, source coverage map, visible/internal boundary, slide candidates and speaker-note metadata.
- Has layout families tied to scientific function: visual row, split, editorial, full visual, zoom detail, matrix, flow.
- Enforces deck rhythm: avoid repeated major layout, repeated card grid, and ensure visual-dominant results when source has figures.
- Has hard gates for completeness, typography, visual integrity, canvas hygiene, layout quality and editability.
- Uses render-slide previews and montage plus repair loop.

Research relevance:

- Strongest mechanism for source fidelity and coverage.
- Particularly relevant for future real holdout benchmarks from papers, because it treats figures/tables and source paragraphs as traceable units.
- Its default “preserve one complete source sentence per paragraph” may be too dense for short oral talks, but useful for journal-club / manuscript-order decks.

Gap versus current repo:

- Current repo has evidence status and source ids, but no complete source-to-slide coverage map for full papers.
- Current deck rhythm check is mostly reviewer-level, not a structured pre-generation object.

Disposition: `candidate_for_future_adoption` for source coverage, layout rhythm and hard gates; adapt density policy to seminar/oral use.

### 6. sunzhejian/academic-paper-image-ppt

Source: https://github.com/sunzhejian/academic-paper-image-ppt

Inspected commit: `85cb24e365d1f81d7ad320836b105a156b3a4b16`

License: MIT.

Files inspected: `LICENSE`, `README.en.md`, `skill/SKILL.md`, `skill/references/evidence-contract.md`, `skill/references/run-contract.md`, `skill/scripts/validate_run.mjs`, `skill/scripts/assemble_editable_deck.mjs`, `tests/validate_run.test.mjs`, `tests/assemble_editable_deck.test.mjs`.

Actual mechanism:

- Generates exactly four slide-browser preview images from a common six-slide audition packet, then stops for explicit style selection.
- Uses image generation only for style audition; final slides must be native editable PowerPoint objects.
- Strict paper figures remain independent PNG assets, byte-identical to authorized sources; no crop, relabel, recolor or redraw.
- Uses a phase state machine and run-root-relative path validation.
- Tests reject URI/absolute path leaks, full-slide image substitution, out-of-bounds objects, missing hashes and strict figure SHA changes.

Research relevance:

- Very strong distinction between visual-direction preview and final editable scientific artifact.
- The common audition packet solves a core one-shot problem: compare visual systems on the same scientific story.
- Its mandatory human style gate is useful for product UX, but the long-term user requirement here prefers automated comparative review unless ambiguity is real.

Gap versus current repo:

- Current repo has reference_design_audit but no preview/audition packet.
- Current repo can render, but does not enforce strict source figure byte identity for paper-derived figures.

Disposition: `candidate_for_future_adoption` for audition packet and strict native-editable assembly contract; do not adopt imagegen dependency as mandatory for all research decks.

### 7. hugohe3/ppt-master

Source: https://github.com/hugohe3/ppt-master

Inspected commit: `65bb2eca59a36270819caba377097910c4466c6e`

License: MIT.

Files inspected: `LICENSE`, `README.md`, `skills/ppt-master/SKILL.md`, `workflows/generate-pptx.md`, `workflows/stages/visual-review.md`, `workflows/stages/live-preview.md`, `references/image-layout-spec.md`, `references/image-layout-patterns.md`, `templates/layouts/layouts_index.json`, `workflows/create-template/create-layout.md`.

Actual mechanism:

- Routes presentation work into distinct authorities: generate PPTX, image-to-PPTX, beautify, create template, fill native PPTX, enhance native PPTX.
- Uses a project workspace, imported sources, candidate template boundary, strategist stage, live preview, quality checks and export.
- Treats SVG page design as a page-design source and converts to PPTX/native objects under explicit structure contracts.
- Provides a detailed image-layout specification: contain/fill math, weighted tracks, free composition coordinates, checks for focal-safe crop, peer scale and geometry drift.
- Provides an image-layout pattern catalog: primary structures, native overlays, multi-visual structures, crop/reveal/registration treatments and cross-page continuity.
- Optional visual-review stage reads SVG plus rendered PNG and applies atomic fixes without changing brand/layout structure.
- Create Layout workflow separates reusable structure from brand identity.

Research relevance:

- Strongest inspected source for composition vocabulary and native/structured export boundary.
- Its image-layout pattern catalog maps well to scientific image/figure slides, especially medical imaging and annotated evidence pages.
- It is broad and complex; adopting it wholesale would exceed this task and could overfit to a separate presentation ecosystem.

Gap versus current repo:

- Current repo lacks a comparable composition grammar for figures/images/formulas/annotations.
- Current repo should not merge ppt-master wholesale; it should first create a small research-specific composition representation aligned to existing archetypes.

Disposition: `candidate_for_future_adoption` for composition grammar and image-layout math, reference-only for broad workflow/runtime.

## Public Scientific Guidance

### 8. Assertion-Evidence Approach

Source: https://www.assertion-evidence.org/

License / reuse boundary: public educational site; concepts and high-level method can be referenced. Do not copy templates, model talk assets, or long text without explicit license verification.

Primary lesson:

- Technical slides should be built on succinct assertion messages rather than phrase topics.
- Each assertion should be supported by visual evidence rather than bulleted lists.
- The approach also provides model talks/templates, but this task uses it as presentation design guidance only.

Current repo implication:

- Existing claim-title and scientific-object rules are aligned.
- The missing part is automatic enforcement that the visual object really supports the assertion and is compositionally central.

Disposition: `reference_only`.

### 9. MIT Communication Lab

Sources:

- MIT EECS Communication Lab, Slide Presentation: https://mitcommlab.mit.edu/eecs/commkit/slideshow/
- MIT AeroAstro Communication Lab, Slide Design: https://mitcommlab.mit.edu/aeroastro/commkit/slide-design/

License / reuse boundary: MIT CommKit content is CC BY-NC 4.0 unless otherwise noted. Use as guidance/reference; do not copy images/templates into active skill artifacts.

Primary lessons:

- Criteria include larger motivation, concrete connection to research, each slide telling a message, and no more information than needed.
- Data should be introduced before the audience must interpret it.
- Slide title should be the takeaway; visuals should dominate over text.
- Figures for talks should be simplified from paper figures and annotated to support the message.
- Visual hierarchy, proximity/similarity/enclosure/continuity/connection and figure-ground relationships can guide audience attention, but can also mislead if used carelessly.
- Back-of-room readability matters; font size and figures should be large enough.

Current repo implication:

- 016/017 rules align with these principles.
- Current gap is not recognizing the principles; it is operationalizing them as page-composition candidates and reference comparisons.

Disposition: `reference_only`.

### 10. PLOS Computational Biology — Ten simple rules for effective presentation slides

Source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009554

Version: published 2021-12-02.

License / reuse boundary: PLOS article is CC BY. Cite and paraphrase; do not import figures as templates unless attribution and task scope require it.

Primary lessons:

- Each slide should carry one idea; complex information should be progressively built up.
- If one slide takes more than about a minute to explain, split or reduce it.
- Headings should state the message, not the topic.
- Non-essential details on the slide consume attention and should be removed.
- Avoid pointless animation and salience that distracts from important content.

Current repo implication:

- Supports a hard “one intellectual job per slide” and progressive build policy.
- For one-shot quality, the generator needs to know when to split rather than shrink or card-pack.

Disposition: `reference_only`.

## Capability Gap Matrix Summary

| Mechanism | Current repo | External evidence | Gap |
|---|---|---|---|
| Evidence-first research content | Strong for 016/017; page archetypes exist | high-quality-slides, manuscript-to-editable-slides, academic-paper-image-ppt | Need normalized source-to-slide coverage for real papers |
| Reference transfer | Page lessons exist in CSV/manifest and audits | ppt-master composition catalog, frontend preview recipes | Need executable composition representation, not prose-only lessons |
| Multi-candidate visual search | Not present | frontend-slides, academic-paper-image-ppt | Need same-content candidate packet; do not start with style-only variants |
| Design-system lock | Partial; skill guidance and generated fixtures | frontend-slides, high-quality-slides, slideweaver deck_profile | Need a locked, auditable design system object per deck |
| Native PPTX editability | Present in fixtures but not as broad solver | slideweaver, ppt-master, academic-paper-image-ppt | Need native object geometry constraints and source-figure identity checks |
| Render-and-look QA | Strong after 016/017 | many-ppt-skills, slideweaver, ppt-master, manuscript-to-editable-slides | Need comparative reference-aware review, not only absolute PASS |
| Deck rhythm | Some contact sheet / reviewer checks | manuscript-to-editable-slides, many-ppt-skills | Need structured rhythm map and repeated-layout detection |
| Anti-AI-slop / internal leakage | Stronger after 016 | frontend-slides, high-quality-slides, manuscript-to-editable-slides | Already rule-covered; failures indicate execution gap |

## Adoption Recommendation

Necessary next mechanism:

1. **Exemplar composition representation.**
   - For each inspected reference page and each generated candidate, record page function, main scientific object, object roles, approximate area ratios, hierarchy, annotation/caption strategy, whitespace role, layout family, figure/formula/image treatment, and deck-rhythm role.
   - The representation must be compact enough for retrieval and comparison, but concrete enough to generate a layout candidate.

Worth trying after that:

- Internal multi-candidate design search using the same scientific content across candidates.
- Comparative Terra review that sees generated candidate(s) alongside matched reference composition records and rendered exemplars.
- Native PPTX geometry helper inspired by `slideweaver` / `ppt-master`, scoped to research page archetypes.
- Source-to-slide coverage map for real manuscript holdout decks.

Not recommended now:

- Wholesale vendoring `ppt-master`, `slideweaver`, or any external skill.
- Expanding reference corpus before the current reference lessons can drive composition decisions.
- Making imagegen previews mandatory for all research decks.
- Treating HTML preview aesthetics as final PPTX quality.

## Recommended 019 Bounded Task

Recommended task: **Research Presentation Exemplar Composition Representation**.

Minimal scope:

- Add an internal JSON schema / data shape for `composition_lesson` records derived from existing inspected reference pages and from 016/017 generated pages.
- Populate a small seed set from already-inspected references only; do not expand corpus.
- Add a deterministic validator that checks required fields, source linkage, page function, main scientific object, area/hierarchy approximations, annotation/caption strategy, and reuse boundary.
- Produce a report showing how each seed record would constrain a future generated page.
- Do not modify generator, Terra, active skill text, PPTX renderer, or reference corpus in this task.

Why this first:

- Multi-candidate search without composition representation degenerates into style variants.
- Comparative review without reference-composition records cannot judge whether lessons were actually adopted.
- Native PPTX/Beamer implementation needs a representation to target before renderer-specific code can be meaningfully improved.

## Evidence Boundary

This audit inspected public source repositories and public guidance pages as of 2026-08-23. It records mechanisms, reuse boundaries and future recommendations only. It does not adopt, vendor, merge, partially merge, install, expose, or route any external skill or plugin.
