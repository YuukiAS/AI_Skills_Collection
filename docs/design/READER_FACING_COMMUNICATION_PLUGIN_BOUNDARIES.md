# Reader-facing communication boundaries: language layer, research-writing, presentations

Status: PROPOSAL / source-of-truth design note for future promotion. This file does not change active production behavior by itself.

## Decision summary

The system should keep three different owners instead of growing one oversized writing plugin:

1. a **generic reader-facing language layer** (currently `writing-style`);
2. `research-writing` for research-document authoring and scholarly evidence structure;
3. `presentations` for slide/deck information architecture, visual sequence, and rendered communication.

The generic language layer is intended to become a reusable companion for many other domain plugins, including `statistical-modeling`, `scientific-visualization`, `medical-imaging`, `bioinformatics`, research reports, and presentations. It owns how already-decided content is expressed; it does not take over domain judgment.

The current `writing-style` slug is also too easy to confuse with `research-writing`. After task 050 closes and its production identity is no longer needed for replay, the preferred rename candidate is:

- current slug: `writing-style`
- proposed slug: `clear-language`
- proposed display name: `Clear Language`
- product meaning: **say it plainly, keep the content faithful**

Do not rename the active plugin during 050. The repository currently has no established plugin-slug alias contract, and 050 production evidence explicitly uses `writing-style@yuukias-ai-skills`; a mid-task slug migration would invalidate the production identity being tested. Any rename must therefore be a separate bounded migration after 050 acceptance, with marketplace/profile/generated-path/reference updates and real installed-plugin replay.

`research-writing` should keep its current name. It is a domain plugin for research authoring, not merely a report formatter: repo-grounded reports, manuscripts, paper workflows, literature/citation work, review/rebuttal/supplement coordination, and claim-evidence organization all belong naturally under Research Writing.

## Why the separation matters

Recent real-use failures occur at different levels:

- the 050 scientific rewrite can preserve facts but still read like a bilingual research memo when ordinary English abstractions carry the sentence skeleton;
- a Distributed Imaging advisor report can contain the right experiments yet fail because it narrates execution order and internal labels instead of rebuilding the document around the scientific decision;
- a CAT-TRACE deck can have individually acceptable sentences and pages yet fail because first-use context, page jobs, adjacent-slide transitions, or whole-deck rhythm are weak.

All three artifacts need “说人话”, but the defect owner is different. A language-layer repair cannot fix a wrong report plan or a wrong slide sequence, and a presentation plugin should not fork a second Chinese-writing rule set.

## Shared reader-facing contract

All reader-facing domain plugins may rely on these common principles:

1. **Audience-facing language over internal workflow language.** Run names, audit labels, lifecycle states, project nicknames, benchmark tokens, and implementation bookkeeping are not automatically reader-facing concepts.
2. **Exact identity vs ordinary reasoning.** Preserve exact algorithm/dataset/metric/package/API/command/path/citation identities when identity matters. Ordinary organization, inference, comparison, qualification, and transition language should be natural Chinese in Chinese artifacts unless English materially improves technical recognition.
3. **Evidence boundaries remain visible.** Facts, literature claims, interpretation, hypotheses/candidate methods, uncertainty, limitations, and future plans must not collapse into one authority level.
4. **Reader effort is not compression.** A shorter artifact is not better if it removes the bridge that explains why two facts are related. Local expansion, a list, a table, a diagram, or a better heading is valid when it lowers cognitive burden.
5. **Meaning fidelity is not source-order fidelity.** When a task authorizes structural rewriting, reader-facing grouping/order may change while the evidence graph, formulas, numbers, citations, conditions, caveats, attribution, and conclusion strength remain stable.
6. **No proxy PASS.** Schema validity, render success, token checks, page-level readiness, or executor self-review cannot override a poor final artifact.
7. **Domain semantics stay with the domain owner.** The language layer may clarify what a model/result/caption says, but it may not invent a new statistical conclusion, change a visual encoding, choose a new experiment, strengthen a medical claim, or rewrite scientific scope merely to sound smoother.

These are shared principles. Artifact-specific information architecture remains with the owning domain plugin.

## 1. Generic language layer (currently `writing-style`, future candidate `clear-language`)

### Product job

This is the reusable **content-preserving reader-facing language layer**.

A useful one-sentence contract is:

> Make the wording, local explanation, and reader-facing organization easier to understand without changing what the source/domain owner has actually established.

It can be the primary plugin when the user already has text and asks for rewriting/polishing/say-it-plain behavior. It can also be a companion layer inside other domain workflows after the domain plugin has fixed the scientific/content semantics.

### It owns

- Chinese-first reader-facing wording and de-translation;
- exact-name vs ordinary-reasoning English decisions;
- sentence and paragraph connective logic;
- first-use explanation of unfamiliar terms;
- local explanation around formulas, methods, captions, conclusions, limitations, and comparisons;
- wording inside existing tables, captions, legends, annotations, callouts, and slide copy;
- source-faithful heavy rewriting of an existing text when the user explicitly requests structural rewriting;
- semantic/literal fidelity while rewriting;
- candidate-only readability/language review;
- local repair that preserves claims and evidence authority.

### It does not own

- deciding which experiments belong in a newly authored report;
- deciding the scientific comparison axis of a new table;
- selecting a statistical model, inferential target, or conclusion;
- deciding what a figure should encode or which plot answers the scientific question;
- choosing slide count, slide order, slide archetype, visual object, or deck rhythm;
- deciding manuscript contribution scope, venue strategy, literature search scope, or research novelty;
- silently deleting source propositions because a newly authored artifact could be shorter.

### Modes of use

The same canonical language source should support several sizes of task without forcing every consumer through the heavy long-document runtime:

- **microcopy / caption / label / conclusion:** local wording + fidelity pass;
- **paragraph / subsection:** local semantic rewrite + fidelity;
- **long existing document:** heavy source-faithful structural rewrite with document/reader plan;
- **slide copy:** wording from a presentation-owned semantic/page brief;
- **domain-generated result explanation:** wording from a domain-owned claim/evidence/uncertainty brief.

Do not create separate “caption humanizer”, “statistics humanizer”, or “slide humanizer” skills when the only missing capability is reader-facing wording.

## 2. `research-writing` owns research-document authoring

`research-writing` is not merely a report plugin. It owns research-document and scholarly-authoring workflows across reports, papers, literature/citations, review, rebuttal, supplement, and related claim-evidence organization.

### It owns

- audience and document purpose;
- scientific/research question framing within the authorized project scope;
- claim-evidence map;
- reader-facing document plan;
- selecting decisive evidence for the main narrative;
- separating main text, methods detail, appendices, reproducibility metadata, and author-internal notes;
- manuscript/report section logic and document-level coherence;
- literature/citation authority and bibliography hygiene;
- deciding whether information belongs in prose, a table, a figure, or an appendix;
- **table semantics and table style at document level:** comparison rows/columns, units, metric direction, precision/rounding consistency, missing-data notation, condition comparability, captions/notes, and avoiding prose repetition of every cell;
- advisor-facing vocabulary for scientific objects and replacement of private project nicknames when the audience should not be expected to know them;
- next-decision logic for advisor/group-meeting reports;
- manuscript-specific workflows such as claim support, reviewer-style critique, rebuttal/supplement/venue coordination through its own research-writing skills.

### It should delegate to the language layer

Once the scientific/document plan is stable, hand off reader-facing wording rather than duplicating Chinese/English style rules.

Logical handoff (not a new repository schema):

`audience + document purpose + section job + claim/evidence boundary + table/figure role + allowed structural freedom -> language layer -> document-level QA`

The Distributed Imaging report v2 is positive evidence for this boundary: the successful revision rebuilt the document around scientific questions and decisions, kept only decision-changing results in the main body, translated internal labels into scientific objects, and moved detailed experiment contracts to tables/appendices. That is primarily a `research-writing` information-architecture success, with the generic language layer responsible for the final reader-facing wording.

## 3. `presentations` owns deck-level scientific communication

A slide deck is not a compressed report. `presentations` owns communication under spatial, temporal, visual, and audience-attention constraints.

### It owns

- audience assumptions and deck purpose;
- deck storyline / belief-update sequence;
- one scientific job per slide;
- slide/page archetype selection;
- first-use registry for concepts, symbols, methods, figure labels, and prerequisites;
- the visible scientific object: result figure, equation, image, diagram, table, experiment design, negative result, or decision question;
- slide density and information morphology;
- transition map: why slide `k+1` follows slide `k`;
- within-slide explanation order where spatial placement matters;
- visible slide content vs speaker notes;
- visual hierarchy, layout, diagram utility, citation placement, rendering, accessibility, and whole-deck rhythm;
- advisor-question decision value and preparedness;
- final rendered reader-effort review.

### It should delegate wording

Before visible prose is written, `presentations` should provide a compact semantic/page brief to the language layer:

`audience assumption + page job + prerequisite/context + exact terms that must remain + intended takeaway + evidence boundary + visible-space constraint`

After wording is returned, `presentations` still owns the rendered result. Text that is good in a report may be too dense for a slide, and a good single slide may still fail to transition naturally from the previous slide.

## 4. Other domain consumers

The generic language layer should be reusable outside the two writing-heavy plugins.

### `statistical-modeling`

Domain owner decides:

- model, assumptions, inferential target, estimand/parameter semantics, diagnostics, uncertainty, comparison, and statistical conclusion.

Language layer may handle:

- result interpretation wording;
- explanation of assumptions/diagnostics to the intended reader;
- table/figure caption text after the statistical comparison is fixed;
- bounded conclusion/limitation prose;
- translating ordinary English scaffolding into natural Chinese without changing statistical meaning.

The language layer may never “simplify” a statistical result by changing the estimand, uncertainty, conditioning set, comparator, or conclusion strength.

### `scientific-visualization`

Domain owner decides:

- visual encoding, axes, scales, panels, statistical annotations, uncertainty display, figure hierarchy, and whether a plot/schematic is scientifically appropriate.

Language layer may handle:

- figure title/caption;
- axis/legend/annotation wording where semantics are already fixed;
- concise takeaway text;
- terminology consistency and reader-facing explanation.

The language layer must not change the figure’s scientific comparison or visual encoding merely to make a caption easier to write.

### `medical-imaging` / `bioinformatics` and other domain plugins

The domain plugin owns task semantics, database/model/metric meaning, clinical or biological interpretation, and workflow correctness. The language layer can be the final wording/caption/conclusion pass once those semantics are frozen.

## Coherence ownership by scale

All three core communication plugins care about coherence, but at different scales:

- generic language layer: sentence -> paragraph -> local section / local explanation coherence;
- `research-writing`: claim -> section -> whole-document decision-story coherence;
- `presentations`: sentence/object -> slide -> adjacent slides -> whole-deck sequence coherence.

A presentation transition failure is not primarily a language-layer failure when each sentence is already natural. A report that preserves experiment chronology is not primarily a language-layer failure when the document plan itself is wrong.

## Table ownership

Tables appear in several domains, but ownership differs:

- generic language layer: cell/heading/caption wording and fidelity in an existing table;
- `research-writing`: whether the document should use a table, scientific comparison logic, rows/columns, units, precision, missing-data notation, captions/notes, appendix vs main-text placement, and prose/table division of labor;
- `presentations`: whether the table should appear on a slide at all, legibility, row/column density, whether a plot/diagram better serves the slide job, and how the table participates in deck rhythm;
- statistical/visual domain plugins: the actual statistical quantities or visual encoding represented by the table/figure remain domain-owned.

## Runtime/source ownership: reuse without rule forks

The canonical wording/fidelity rules should live under the generic language layer's source skills. Other plugins should not maintain their own copies of generic “说人话” rules.

Until there is a demonstrated need for a formal cross-plugin dependency mechanism, use the smallest production-compatible route available:

- install/enable the generic language plugin as a companion in workflows that need it; or
- package the same canonical `skills/writing/core/...` sources into a domain/profile when the current runtime requires co-packaging.

The important invariant is **one canonical source of generic language behavior**, not a particular packaging trick. Do not introduce a new dependency schema solely for this design note.

## Final routing rule

- Existing text + “rewrite / polish / say it plainly without changing meaning” -> generic language layer is primary.
- New research report / advisor update / manuscript / literature-citation workflow -> `research-writing` is primary; use the generic language layer for final reader-facing wording where appropriate.
- New/revised scientific deck -> `presentations` is primary; use the generic language layer after page jobs/evidence/sequence are fixed, then return to `presentations` for rendered QA.
- Statistical/visual/medical/bioinformatics workflow -> domain plugin is primary; invoke the generic language layer only for reader-facing wording after domain semantics are stable.

Do not create a fourth generic humanizer plugin.

## Naming migration decision

Recommended direction after 050 closes:

`writing-style` -> `clear-language`

Why rename this plugin rather than `research-writing`:

- `research-writing` already names a real domain: scholarly/research authoring across reports, papers, citations, and review workflows;
- `writing-style` sounds like optional cosmetic styling even though the intended capability is a reusable content-preserving language layer;
- `clear-language` is distinct from research authoring and naturally covers captions, conclusions, table text, annotations, slide copy, reports, and technical explanations;
- the product description can state the fidelity constraint explicitly, avoiding the implication that “clear” means simplifying away technical content.

Migration preconditions:

1. 050 reaches human STYLE_ACCEPT and its current `writing-style@yuukias-ai-skills` evidence is closed;
2. audit every active plugin/profile/marketplace/test/reference that uses the slug;
3. decide the compatibility mechanism supported by the actual marketplace/runtime (do not invent an alias feature if it does not exist);
4. update source config first, regenerate plugin payloads, then profiles/docs/tests;
5. perform real installed-plugin replay under the new identity;
6. only then retire the old slug.

## Promotion checks

Before promoting these boundaries into active runtime behavior, verify on real tasks:

- one long source-faithful scientific rewrite;
- one advisor-facing research report with substantial tables;
- one research deck requiring both slide-level wording and adjacent-slide coherence;
- one statistical result/caption or conclusion handoff;
- one scientific-visualization caption/annotation handoff.

Success means each domain plugin changes the artifact at its own level, generic language rules come from one canonical source, and no plugin silently assumes another plugin's scientific responsibilities.
