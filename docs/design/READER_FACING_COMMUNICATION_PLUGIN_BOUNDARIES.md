# Reader-facing communication boundaries: writing-style, research-writing, presentations

Status: PROPOSAL / source-of-truth design note for future promotion. This file does not change active production behavior by itself.

## Why this note exists

Recent real-use failures in three workflows show the same generic problem at different artifact levels:

- `writing-style`: a source-faithful scientific rewrite can remain technically correct but read like a bilingual research memo when ordinary English abstractions, source-order structure, or compressed technical labels still carry the reader-facing argument.
- `research-writing`: an advisor-facing report can be scientifically complete but still fail when experiment chronology, internal run labels, audit tokens, and exhaustive details are promoted into the main narrative.
- `presentations`: a deck can have individually correct slides and sentences but still fail when page jobs, first-use context, slide-to-slide transitions, visual hierarchy, or whole-deck narrative continuity are weak.

The common objective is lower reader inference burden without changing scientific meaning or evidence authority. The plugins should share that objective without collapsing into one oversized communication plugin.

## Shared contract

All three plugins should preserve these generic rules:

1. **Audience-facing language over internal workflow language.** Internal run names, audit labels, project nicknames, lifecycle states, and implementation bookkeeping are not automatically reader-facing concepts.
2. **Exact identity vs ordinary reasoning.** Preserve exact method/dataset/package/API/metric names when identity matters. Ordinary organizational, inferential, comparative, and qualifying language should be natural Chinese in Chinese artifacts unless English materially improves technical recognition.
3. **Evidence boundary.** Facts, literature claims, interpretation, hypotheses/candidate methods, uncertainty, and future plans must remain distinguishable.
4. **Reader effort is not compression.** A shorter artifact is not better if it removes the bridge that explains why two facts are related. Lists, tables, headings, diagrams, or local expansion are valid when they reduce cognitive burden.
5. **Meaning fidelity is not source-order fidelity.** When the task authorizes structural rewriting, reader-facing grouping/order may change while the evidence graph, formulas, numbers, citations, conditions, caveats, attribution, and conclusion strength remain stable.
6. **No proxy PASS.** Schema validity, render success, exact-token checks, page-level readiness, or executor self-review cannot override a poor final artifact.

These are shared principles. Ownership of information architecture remains artifact-specific below.

## 1. writing-style owns linguistic realization and rewrite fidelity

`writing-style` is a cross-cutting expression layer. It should be callable by other domain plugins after those plugins have decided what the artifact is trying to communicate.

It owns:

- Chinese-first reader-facing wording and de-translation;
- exact-name vs ordinary-reasoning English decisions;
- sentence/paragraph connective logic;
- local explanation of technical concepts and formulas;
- heavy source-faithful structural rewriting when explicitly requested;
- semantic/literal fidelity during rewriting;
- candidate-only language/readability review;
- final prose repair that does not change scientific claims.

It does **not** own:

- deciding which experiments are scientifically decisive in a newly authored report;
- deciding what the advisor needs in the main body versus appendix when creating a new report from repo evidence;
- choosing a research narrative that changes project scientific scope;
- deciding slide count, slide sequence, page archetype, visual object, or deck rhythm.

For heavy rewrite of an existing source document, `writing-style` may reorganize existing material by reader question, but it may not silently discard source propositions merely because a new report would be shorter.

## 2. research-writing owns document-level scientific information architecture

`research-writing` / `research-reporting` owns creation of a report from research evidence.

It owns:

- audience and document purpose;
- claim-evidence map;
- reader-facing document plan;
- selecting the decisive evidence for the main narrative;
- moving secondary experiments, detailed splits, run history, reproducibility details, and implementation evidence to appendices;
- deciding when tables/figures carry exact values and prose should only interpret the decision-changing comparisons;
- table semantics: comparison columns, units, metric direction, precision/rounding consistency, missing-data notation, condition comparability, captions, and avoiding prose repetition of every cell;
- advisor-facing vocabulary and replacement of private project nicknames with scientific objects the audience recognizes;
- report-level section coherence and next-decision logic;
- citation/evidence authority appropriate to the report.

It should invoke `writing-style` after the document plan and scientific content are stable, rather than duplicating Chinese phrasing rules.

A useful handoff is:

`audience + document purpose + claim/evidence map + section jobs + table/figure roles + evidence boundaries -> writing-style final prose`

The Distributed Imaging report revision is positive evidence for this boundary: the successful revision stopped narrating experiments in execution order, kept only decision-changing results in the main body, translated internal labels into scientific objects, and moved detailed experiment contracts to tables/appendix.

## 3. presentations owns deck-level scientific information architecture and visual sequence

`presentations` owns communication under slide constraints. A slide deck is not a compressed report.

It owns:

- audience assumptions and deck purpose;
- deck storyline and belief/update sequence;
- one scientific job per slide;
- slide/page archetype selection;
- first-use registry for concepts, symbols, methods, and figure labels;
- what scientific object should be visible: result figure, equation, image, diagram, table, experiment design, negative result, decision question;
- slide-level density and information morphology;
- transition map: why slide `k+1` follows slide `k`;
- within-slide explanation order where spatial arrangement matters;
- speaker-note material versus visible slide content;
- visual hierarchy, layout, diagram utility, citation placement, render QA, and whole-deck rhythm;
- advisor-question decision value and preparedness;
- final rendered-reader-effort review.

It should not duplicate general Chinese/English prose rules. Instead it should provide `writing-style` with a compact semantic brief for each slide:

`audience assumption + page job + prerequisite/context + term role + intended takeaway + visible-space constraint`

After wording is returned, `presentations` must still re-check the rendered deck because language that is fine in a document can be too dense, too long, or poorly sequenced on a slide.

## Different coherence responsibilities

The three plugins all care about coherence, but at different scales:

- `writing-style`: sentence -> paragraph -> local section coherence in an existing text.
- `research-writing`: claim -> section -> document decision-story coherence.
- `presentations`: sentence/object -> slide -> adjacent-slide -> whole-deck sequence coherence.

A presentation-specific transition failure is not primarily a writing-style failure when each sentence is individually natural. A report whose main body preserves experiment chronology is not primarily a writing-style failure when the document plan itself is wrong.

## Table ownership

Tables appear in all three domains, but ownership differs:

- `writing-style`: wording inside an existing table, heading clarity, Chinese/English language, and semantic fidelity; do not redesign scientific comparison logic by default.
- `research-writing`: whether information should be a table, what rows/columns answer the report question, exact-value presentation, units/precision, comparability, captions, and relationship between table and prose.
- `presentations`: whether the table belongs on a slide at all, how many rows/columns remain legible, whether the claim is better served by a plot/diagram, and whether the table supports the slide's one job.

## Final routing rule

When a user asks for an artifact:

- Existing text + "rewrite/polish/say it plainly without changing meaning" -> `writing-style` is primary.
- New research report / advisor update / experiment retrospective from repo evidence -> `research-writing` is primary, then hand off final wording to `writing-style`.
- New/revised scientific deck -> `presentations` is primary, with `writing-style` as the wording layer after page jobs and evidence structure are fixed.

Do not create a fourth generic "humanizer" plugin. The reusable reader-facing language contract belongs in `writing-style`; document and deck information architecture remain with their domain owners.

## Promotion checks

Before converting this design note into active runtime rules, verify on real tasks:

- one long source-faithful scientific rewrite;
- one advisor-facing research report with substantial tables;
- one research deck requiring both slide-level wording and adjacent-slide coherence.

Success means each domain plugin changes the artifact at its own level while the final language remains consistent and no plugin silently assumes another plugin's responsibilities.
