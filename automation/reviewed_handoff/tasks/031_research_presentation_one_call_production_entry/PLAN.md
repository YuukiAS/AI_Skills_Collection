---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 031_research_presentation_one_call_production_entry
decision: PLAN_FROZEN
---

# 031 Research Presentation One-Call Production Entry — Plan

## Frozen decisions

031 is the first bounded task of Stage 4. It must prove that the normal `research-presentations` production route actually orchestrates the Stage 1–3 capabilities in one invocation. It must not turn a benchmark generator into the product entrypoint, must not use Stage 5 holdout papers, and must not claim full Stage 4 PASS merely because a single engineering regression succeeds.

Stage 1–3 accepted capabilities are frozen assets: exact CUHK Beamer identity, normal Stage 2 gold selection/recipe consumption, Stage 3 executable scientific layout families, source-derived geometry, capacity failure through `SPLIT_REQUIRED`, native mathematical layout, presentation-native result figures, typed experiment relations, medical ROI comparison, next-experiment reasoning, real compile/render and task-local Visual Review.

## Implementation scope

### 1. Resolve the real production entry surface

Executor must first inspect the current `research-presentations` skill, shared presentation routing, existing scripts and plugin mirrors to determine the real normal production entry surface.

If an existing shared production runner/orchestrator already exists, adapt it. If no executable orchestration surface exists, add one minimal shared production runner and wire the normal skill/routing documentation and tests to it. Do not create a second product route that is only reachable from tests.

The production surface must accept user-supplied source input through a stable file/path-oriented interface rather than embedding task-specific content in code.

### 2. Source ingestion and source-fidelity map

For one repository-owned, public-safe engineering regression bundle, the normal production invocation must:

- read the supplied research text/evidence assets;
- construct or validate the normal research deck plan representation;
- preserve source anchors for claims, equations, figures, tables or quantitative evidence;
- expose an internal source-fidelity/evidence map that lets Reviewer trace the generated page content back to supplied material;
- keep internal planning labels out of audience-facing slides.

The engineering bundle is only an integration fixture. It must be explicitly marked in trace/README/tests as ineligible for Stage 5 holdout use.

### 3. Storyline and page-job routing

The one-call path must derive a coherent research storyline and explicit page jobs rather than directly invoking fixed slide IDs. At minimum, the regression should exercise several distinct scientific jobs and include both a mathematical/method object and a quantitative evidence page; if the supplied bundle legitimately supports negative/failure or next-experiment content, route those through the same normal page-job mechanism.

Page jobs must remain the bridge between source evidence and Stage 2/3 runtime selection. Do not hardcode `GSC-*` IDs in the production path.

### 4. Normal gold retrieval and executable Stage 3 consumption

For every generated scientific content page that uses a gold-backed Stage 3 family, save a runtime trace showing:

- page job and scientific object query;
- normal compatible gold candidates/selection;
- selected source composition identity;
- source-derived composition fields actually consumed;
- resolved Stage 3 layout family / geometry;
- any capacity decision, including `SPLIT_REQUIRED` when applicable.

The production entry must call shared selector/recipe/layout components, not benchmark-only helper functions. A deterministic test must fail if the normal production path bypasses selector compatibility or calls a task-specific Stage 3 regression generator as its orchestration surface.

### 5. Exact CUHK generation and real render

The normal invocation must copy/use the canonical exact CUHK Beamer source and produce:

- generated source-editable `.tex`;
- compiled PDF through the actual LaTeX capability/dependency contract;
- rendered PNGs for content pages;
- mechanical/source-fidelity QA;
- production trace linking input -> plan -> gold -> layout -> output.

Exact CUHK title/navigation/frame/footline identity must come from the canonical template source, not a derived PPTX or reconstructed scaffold.

### 6. Bounded quality handoff, not full repair loop yet

031 must create task-local visual-review inputs for its produced engineering deck, using:

`results/031_research_presentation_one_call_production_entry/visual_review/visual_inputs.json`

and evidence path:

`results/031_research_presentation_one_call_production_entry/visual_review/VISUAL_REVIEW.json`

The manifest must include the current implementation identity and the principal generated content pages. The rubric must check:

- source-specific content rather than generic placeholders;
- exact CUHK identity;
- scientific-object prominence and projection readability;
- math/plot/image semantic correctness where applicable;
- internal meta-language leakage;
- repeated-template / generic-card smell;
- whether the generated deck looks like a coherent research update rather than disconnected benchmark pages.

031 does not need to implement the final bounded automatic repair loop. It must, however, expose a machine-readable quality-loop handoff state that can carry page-level blocking findings into the next bounded Stage 4 task without inventing a new Reviewed Handoff state machine.

### 7. Deterministic regression and mirrors

Add tests that prove at least:

- normal user-facing research route reaches the production orchestration surface;
- engineering input is passed as input rather than embedded in production code;
- source-fidelity map contains real anchors consumed by generated pages;
- normal gold selector/recipe/layout path is used;
- exact CUHK source is used;
- audience-facing output contains no internal RRL/gold/QA/provenance labels;
- benchmark/task-specific generators are not the normal production entry;
- plugin/source mirrors remain synchronized where repository architecture requires it;
- Stage 1–3 regression tests continue to pass.

## Acceptance and regression gates

Planner may PASS 031 only if all of the following hold:

1. A normal `research-presentations` invocation can be demonstrated from one supplied engineering research input to final `.tex + PDF + rendered pages` without directly invoking a benchmark helper as the product entry.
2. Input claims/equations/figures used in output have an inspectable source-fidelity/evidence map.
3. Storyline/page jobs are generated through the production path rather than fixed to the 030 slide sequence.
4. Gold selection is normal and compatibility-driven; no force-id, score override or holdout-specific hardcode exists.
5. Stage 3 shared executable layouts are actually consumed by the production path and runtime trace proves it.
6. Exact CUHK canonical source is actually used and real compile/render succeeds.
7. Current task-local visual manifest/evidence binds the produced deck and principal content pages; item/page-level evidence is read independently by Planner.
8. Deterministic tests, full tests, skills/marketplace validation, Reviewed Handoff validation and real GitHub CI pass.
9. Stage 1–3 accepted behavior does not regress.
10. The engineering regression is explicitly excluded from Stage 5 holdouts and production code contains no fixture-specific layout/content constants.
11. 031 does not claim full Stage 4 PASS; remaining bounded quality-loop/deck-rhythm work is documented for the next Stage 4 task unless evidence shows it already exists through the same production path.

## Stop condition

Stop when the ordinary production route demonstrably connects user-supplied engineering research material to source-faithful deck planning, normal gold retrieval, Stage 3 exact-CUHK generation, real render and task-local visual-review handoff, with all required regression/CI evidence.

If the existing architecture lacks a stable production orchestration surface and closing that gap would require multiple materially different product architectures, route to Planner rather than choosing a large redesign autonomously. If there is one obvious minimal shared integration path, implement it within this task.

## Out of scope

031 must not:

- use either final Stage 5 holdout paper;
- perform final statistics/biostatistics or medical-imaging one-shot acceptance;
- expand or re-admit the Stage 2 gold corpus;
- redesign canonical CUHK identity;
- rewrite 027–030 history;
- introduce an independent visual-review state machine;
- implement an unbounded autonomous repair loop;
- claim Stage 4 PASS, `PROGRAM_MATURE`, `ONE_SHOT_QUALITY_PASS`, or final human acceptance.
