# Curriculum-Driven Domain Plugin Refinement

Status: **design proposal; pilot required before this becomes a routine maintenance path.**

This document records a user-approved direction for strengthening broad domain plugins by letting AI study bounded, authoritative course/reference material and converting that study into tested production behavior. It does **not** authorize bulk textbook ingestion, mass skill creation, automatic plugin rewrites, or a new workflow state machine.

The first goal is to prove one small pilot. If the pilot does not produce a measurable production improvement, stop and revise the approach rather than scaling it.

## 1. Product goal

The target is not to make the repository contain more notes or more textbook summaries. The target is:

> after studying authoritative material, the installed domain plugin makes better decisions on real user tasks than it did before.

A source only counts as integrated when it changes a real decision, workflow, diagnostic, validation gate, or output and that change survives review and regression. Reading, downloading, summarizing, indexing, or citing a source is not sufficient.

The practical analogy is a professional course:

- authoritative sources are the course material;
- Codex is the student and implementation executor;
- GPT/Planner defines the competency and decides what is worth promoting;
- Reviewer acts as an examiner;
- synthetic cases are exercises;
- real research tasks are the final practical test.

## 2. Different plugins need different curricula

Do not force one source strategy across all domains.

| Plugin | Primary learning sources | Main review mode | Main risk |
|---|---|---|---|
| `statistical-modeling` | textbooks, classic/modern methodological papers, official statistical software documentation | text/reasoning review plus case-based assessment | memorizing software recipes without learning statistical judgment |
| `scientific-visualization` | visualization textbooks, graphical-perception literature, journal/venue guidance, strong real figure examples | text review **and visual review of rendered artifacts** | mechanically satisfying rules while producing a poor figure |
| `medical-imaging` | standards, consensus/guideline documents, official tool documentation, mature implementations, landmark papers, selected textbooks | text/domain review plus real image/data/artifact validation | outdated or incorrect modality, geometry, label, metric, or clinical semantics |
| `bioinformatics` | official workflow documentation, mature repositories, benchmark/best-practice papers, reference-database guidance, selected textbooks | workflow review plus real data-format/pipeline validation | collecting many tools without a coherent, reproducible workflow |

Public posts, newsletters, WeChat articles, Xiaohongshu posts, blog posts, and similar material may be useful for **discovery**. They are not integration truth. Before adoption, trace the useful idea to an authoritative paper, official documentation, standard, mature repository, or other defensible source.

## 3. The unit of work is a competency, not a book

Do not create tasks such as:

> Read *Doing Bayesian Data Analysis* and improve `statistical-modeling`.

That scope is too broad and makes it easy to turn the plugin into a summary dump.

Planner should freeze a bounded **competency module**, for example:

- prior specification and regularization;
- prior predictive checking;
- partial pooling and hierarchical-model choice;
- posterior predictive diagnosis;
- interaction and nonlinear effect reasoning;
- uncertainty visualization;
- multi-panel scientific figure hierarchy;
- DICOM/NIfTI geometry and resampling semantics;
- single-cell QC and batch-correction decision boundaries.

A module may use several sources at once. This is preferred when multiple authoritative sources provide complementary views.

Before execution, the frozen module should state, in ordinary Markdown rather than a new schema:

- the competency to be learned;
- source bundle and exact source locators/chapters/sections when available;
- the relevant current plugin/skill baseline;
- natural `should-trigger` cases;
- adjacent `should-not-trigger` cases;
- at least one ambiguous/grey case where the correct behavior may be to request more information;
- expected assessment mode;
- source-access and rights constraints.

## 4. Two-phase contract

### Phase A — study and extraction

The study phase does **not** modify active production skills.

1. **Planner freezes one bounded competency module.** It first checks the current `main`, active domain skill, neighboring skills, and existing references so the course does not relearn an already implemented rule.
2. **Codex reads only the required source bundle.** It produces a candidate lesson rather than editing the plugin.
3. The candidate lesson must explain:
   - what practical problem the competency solves;
   - the decision logic, not merely the definition;
   - assumptions and preconditions;
   - counterexamples and non-applicable cases;
   - common AI failure modes or over-generalizations;
   - source locators for each important claim;
   - the smallest plausible change in AI behavior.
4. **Reviewer checks source fidelity.** The review looks specifically for omitted conditions, recommendation-to-rule inflation, false consensus between sources, and unjustified generalization.
5. **Planner compares the reviewed lesson with the current plugin.** The result may be no change, reference-only retention, strengthening an existing rule, or a bounded production improvement.

Codex does not own the final decision to promote study material into an active skill.

### Phase B — production promotion

Only a reviewed, bounded improvement enters the existing maintenance system:

```text
reviewed candidate lesson
-> Planner freezes bounded production change
-> Codex implementation
-> replay of the target cases
-> unrelated regression
-> independent review
-> version/changelog closure when required
```

Reuse the existing Reviewed Handoff, AI Skills Maintainer rules, plugin versioning, and real-world refinement workflow. Do not create a parallel role system, promotion taxonomy, ledger, or state machine for curricula.

## 5. Assessment must test decisions, not definitions

A model already knows many textbook definitions. A curriculum is useful only if it changes behavior on difficult cases.

### Statistical modeling

Use case-based reasoning exams, not questions such as “What is partial pooling?” A module should include:

- cases where the new competency should clearly change the analysis;
- near-miss cases where the plugin should **not** apply the new rule;
- grey cases where the right response is conditional or requires more information;
- code/model checks only when implementation behavior is part of the competency.

A correct answer must expose the relevant assumptions and uncertainty rather than simply name a model or package.

### Scientific visualization

Text review is necessary but insufficient. The acceptance artifact should include a real rendered figure or equivalent visual object. Reviewer must inspect the render for hierarchy, perceptual clarity, uncertainty encoding, density, labeling, comparison structure, and whether the scientific conclusion is easier to recover.

Mechanical QA such as DPI, font size, contrast, colorblind checks, or file format cannot by itself establish visual quality.

### Medical imaging

Assessment should use real or realistic domain artifacts and preserve physical-space geometry, modality/task semantics, label meaning, patient/case structure, metric semantics, and reproducibility. A toy tensor or import test cannot establish readiness for a medical-imaging competency.

### Bioinformatics

Assessment should use real data formats and a real workflow boundary where practical. Check reference/database provenance, software/tool version assumptions, sample structure, reproducibility, and whether the selected workflow is still appropriate. Synthetic fixtures remain useful for regression but cannot substitute for real pipeline validation.

## 6. Reviewer mode

Choose review mode from the artifact that determines success:

- reasoning, statistical guidance, workflow text, or extracted lesson -> **Text Review**;
- scientific figure, schematic, poster, or other visual artifact -> **Visual Review** in addition to any text review;
- mixed tasks -> both, with each reviewer responsible for the artifact it can actually inspect.

A reviewer must not PASS a study module merely because the Executor produced a well-structured summary. If the decisive source or artifact is unavailable to the reviewer, the result remains waiting for evidence rather than a semantic PASS.

## 7. Source and copyright boundary

Do not search for or download unauthorized textbook copies. Use user-provided files, institutionally/lawfully accessible copies, official open material, papers, documentation, and other permitted sources.

The repository should normally retain derived decision guidance, bibliographic/source locators, provenance, tests, and evaluation cases—not copied textbook chapters. Quotation should be minimal and only when necessary.

## 8. Compute and API policy

The pilot should **not require the OpenAI API**. Prefer the existing ChatGPT + Codex + Reviewed Handoff path so source interpretation, Planner judgment, and review stay visible and controllable.

API use is an optional later scaling layer only after the small workflow is proven. Plausible future uses include large batches of independent extraction jobs, large case-generation/evaluation sets, or repeatable scoring passes. Do not pay API cost merely to reproduce work that a small number of ChatGPT/Codex runs can already perform.

Scheduled or unattended automation should also wait until the curriculum, role boundaries, source access, and acceptance criteria are stable. Automation is useful for a mature repeated process; it should not make an uncertain curriculum run faster in the wrong direction.

## 9. First pilot

Start with `statistical-modeling`, because textbook-driven improvement is most directly aligned with that plugin's current gap.

Proposed first competency:

> **Prior specification + prior predictive checking**

Candidate source bundle, subject to lawful access and Planner confirmation:

- John K. Kruschke, *Doing Bayesian Data Analysis*;
- Gelman et al., *Bayesian Data Analysis*;
- Richard McElreath, *Statistical Rethinking*;
- relevant official PyMC / Stan guidance.

The pilot should demonstrate all of the following before this design is generalized:

1. Codex can extract a compact decision lesson without copying or summarizing the whole book.
2. Reviewer can identify and reject over-generalized rules.
3. Planner can map the lesson onto the existing `statistical-modeling` plugin without unnecessary new skills.
4. Case-based assessment shows a behavior improvement on `should-trigger`, `should-not-trigger`, and grey cases.
5. The production plugin survives replay and unrelated regression.
6. A later real modeling task shows that the change is useful outside the curriculum exercise itself.

Until this pilot succeeds, do not bulk-assign textbooks to all four plugins and do not build a separate curriculum registry or automation system.
