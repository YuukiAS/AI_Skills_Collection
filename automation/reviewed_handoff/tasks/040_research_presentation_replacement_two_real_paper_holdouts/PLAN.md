---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 040_research_presentation_replacement_two_real_paper_holdouts
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Perform the replacement Stage 5 two-paper unseen acceptance test after 038's genuine unseen failure and 039's generic non-holdout recovery. The purpose is to test the **already frozen** normal `research-presentations` production route on two new real papers, not to improve the system on these papers.

The holdouts are frozen as:

1. **Statistics / methodology** — Kasper Kristensen, Anders Nielsen, Casper W. Berg, Hans Skaug, Bradley M. Bell (2016), *TMB: Automatic Differentiation and Laplace Approximation*, Journal of Statistical Software 70(5), DOI `10.18637/jss.v070.i05`.
2. **Medical imaging** — Danielle L. Ferreira, Connor Lau, Zaynaf Salaymang, Rima Arnaout et al. (2025), *Self-supervised learning for label-free segmentation in cardiac ultrasound*, Nature Communications 16:4070, DOI `10.1038/s41467-025-59451-5`.

Planner exact-title/DOI searches against tracked repository content returned no hit before freezing. The JSS paper is publicly available under the journal's Creative Commons Attribution article policy; the Nature Communications paper is open access under CC BY 4.0 and explicitly includes article images/third-party material in that license unless a figure-specific credit states otherwise. Executor must verify and record the exact version, license text and any figure-level exceptions before use.

## Frozen decisions

- 038 remains a real failed holdout. Bürkner/brms and MedSAM are permanently disqualified as unseen papers and must not appear in 040 inputs, fixtures, rule changes or visual tuning.
- 039 PASS proves only the generic quality-loop execution mechanism. Its stress bundle is not a Stage 5 pass and must not be substituted for either real paper.
- 040 is **evaluation-only**. Do not change the normal production generator, gold library, scientific-layout emitters, selector/scoring rules, storyline/grouping rules, validators, render-identity contract, Visual Review protocol, quality-loop normalization/mapping, shared skill source, plugin behavior or CI behavior to make these papers pass.
- The two holdout identities above are fixed. If pre-render audit shows either paper was actually used for exemplar extraction, rule distillation, gold construction, tuning or an earlier holdout, stop before first render and return `NEEDS_GPT_PLANNER`; do not select a replacement inside this task.
- Full source preparation occurs **before first render**. Read the complete main article and all supplementary/source-data material needed to understand methods, figures, tables, limitations and image semantics. Build the normal file/path-oriented source bundle and then freeze it with SHA256 plus source/figure inventory before invoking production.
- After the first production render of a paper, its source bundle is immutable for the unseen claim. Seeing generated slides, local QA or Terra may not trigger source-bundle rewriting, re-curation of claims, figure swapping, or selective omission.
- Each paper must be generated independently through `generate_research_presentation_production_entry.py --input-bundle ... --out-dir ...` or the current documented normal production entrypoint if that exact wrapper has been renamed without semantic change. Do not use task fixtures, benchmark helpers or task-local generators.
- The already shipped bounded quality loop may run at most once per deck. Only structured visual findings supported by the generic 039 mechanism may trigger it. Unknown/ambiguous findings, unsafe source changes, exhausted budget or paper-specific intervention fail closed.
- No manual `.tex`/PNG/PDF patch, no second repair, no paper-specific production branch, no forced gold ID, no score override, no post-hoc source claim rewrite, and no new rule/gold/test learned from either holdout.
- Each deck must be a complete paper-talk/journal-club presentation whose length follows source coverage rather than a fixed page count. Audience must be able to understand motivation/problem, core method/mechanism, important evidence/results, failure/limitation boundary and final interpretation.
- Exact CUHK Beamer source identity remains mandatory. Internal repository/workflow/provenance/QA language must not be visible to the audience.
- Task-local Visual Review evidence is mandatory from the beginning. Missing fresh evidence is a wait state and must not consume a review round.

## Holdout-specific scientific requirements

### A. TMB statistics/methodology deck

The deck must be recognizably about TMB rather than a generic random-effects or Stage-4 calibration talk. The paper's own objects should drive the presentation, including as source-appropriate:

- the joint likelihood / random-effects formulation and Laplace approximation used to marginalize latent random effects;
- automatic differentiation and the derivative/sparsity computational mechanism;
- the R/C++ template workflow and relationship between user model specification and TMB's optimization/inference machinery;
- benchmark/scaling evidence comparing TMB with ADMB across examples, including the paper's large-random-effect motivation;
- the paper's stated accuracy/validation evidence, computational limitations and interpretation.

Use real equations, diagrams, tables/plots or replicated source objects only when anchored to the paper. Do not import brms/Stan holdout copy merely because both are statistical software papers; do not import the Stage-4 clustered-calibration fixture.

### B. Cardiac-ultrasound medical-imaging deck

The deck must be recognizably about self-supervised, manual-label-free cardiac ultrasound segmentation and preserve the clinical/image semantics of the paper. It should cover as source-appropriate:

- the motivation: annotation burden/variability in echocardiographic chamber segmentation and measurement;
- the actual weak-label/self-supervised pipeline for A2C, A4C and SAX views, including the role of computer vision, clinical shape knowledge, early/self-learning and successive refinement;
- real article qualitative echocardiography segmentation evidence. At least one substantive page must directly use article figures/images covered by the license and preserve view/chamber/pathology/annotation/prediction semantics;
- the main quantitative validation against clinical echocardiographic measurements, external data and the CMR subset, including the paper's real reported measures/plots as appropriate;
- meaningful failure cases/limitations and the clinical interpretation rather than only a model architecture summary.

Do not synthesize replacement ultrasound pixels, masks, pathologies or human annotations. Cropping/reframing for presentation is allowed only if it preserves source pixels and semantics and respects figure licensing/credit lines. The 039 medical legend/callout repair may change layout around source imagery but may not generate or alter medical pixels.

## Implementation scope

1. **Eligibility and contamination audit before acquisition/render**
   - Search reference-source manifests/indexes, gold metadata/lessons, corpus manifests, task history/results, tuning metadata and tracked presentation assets for exact title, DOI, author+distinctive identifiers, and paper-specific artifact names.
   - Record scopes and results in `results/040_research_presentation_replacement_two_real_paper_holdouts/holdout_eligibility.json`.
   - Explicitly record that 038 brms/MedSAM are excluded from 040 source/gold/rule preparation.
   - If either new paper has real prior tuning use, stop it before first render and route to Planner.

2. **Source acquisition, full reading and freeze-before-render**
   - Acquire the version of record / publisher PDF or HTML plus required supplementary/source-data materials.
   - Record bibliographic metadata, DOI, license, source URL/version/acquisition date, source SHA256, page/section inventory, figure/table inventory and figure-level credit/license notes.
   - Build `statistics/source_bundle.json` and `medical/source_bundle.json` with source anchors for substantive claims, equations, tables, figures/images, results and limitations.
   - Write corresponding bundle hashes and inventories **before** any production render. Add a mechanical guard proving the bundle hash is unchanged after first render and after any permitted quality-loop repair.

3. **Two independent normal production invocations**
   - statistics output root: `results/040_research_presentation_replacement_two_real_paper_holdouts/statistics/`;
   - medical output root: `results/040_research_presentation_replacement_two_real_paper_holdouts/medical/`;
   - invoke the normal production entrypoint once per frozen bundle and record exact invocation/exit status;
   - preserve each deck's source-fidelity map, deck plan, selected/consumed gold evidence, canonical CUHK `.tex`, PDF, rendered pages, contact sheet, render-input identity, rendered-pixel identity, sequence summary and quality-loop state.

4. **One generic bounded repair maximum per deck**
   - If initial rendered pixels receive blocking structured visual findings that map safely through the shipped 039 quality-loop execution path, allow exactly one automatic source-faithful repair for that deck.
   - Prove any repair changes the relevant render-input/pixels and leaves source-bundle SHA, CUHK identity and protected medical source pixel hashes unchanged.
   - If the existing consumer cannot safely repair a blocker, stop with no winner. Do not implement a new fix in 040.

5. **Fresh combined task-local visual evidence**
   - Once each deck's final candidate is fixed (initial render if no repair, otherwise its single repaired render), create `results/040_research_presentation_replacement_two_real_paper_holdouts/visual_review/visual_inputs.json` containing every substantive page and a contact sheet for each deck.
   - Bind evidence to each source-bundle SHA, implementation/base identity, render-input identity, rendered-pixel identity, page/PDF/contact-sheet SHA and source-fidelity map.
   - Terra rubric must separately judge each page and each whole deck for source specificity, exact-CUHK identity, scientific-object prominence, formula/table/plot/image semantic fidelity, projection readability, no internal meta language, narrative completeness and mature doctoral-group-meeting / strong paper-talk quality.
   - For cardiac ultrasound, item reviews must explicitly inspect whether real source images, chamber/view labels, human-vs-prediction meaning, failure examples and legends/callouts remain semantically correct and unobstructed.

6. **Result handoff**
   - `RESULT.md` reports the two papers separately: contamination audit, source/license evidence, frozen source-bundle hashes, normal invocation, whether a repair was used, final render identities, source fidelity, actual page/contact-sheet paths, CI and all unresolved failures.
   - Do not summarize top-level Terra PASS as visual-quality PASS; Executor must expose item-level evidence for Planner review.

## Acceptance gates

040 can be Planner PASS only if **all** conditions hold:

- both papers pass the pre-render unseen/tuning exclusion audit;
- complete article and necessary supplements/source data were actually read, with source/version/license and figure-credit evidence recorded;
- each source bundle was frozen and hashed before first render and remained byte-identical afterward;
- both decks were independently produced from the normal production entrypoint without benchmark/task-specific bypass or post-output source editing;
- no production/gold/layout/rule/validator/quality-loop implementation change was made in response to either holdout;
- any automatic repair used the already-shipped generic quality loop and occurred at most once per deck;
- TMB deck is source-specific, mathematically/computationally correct, uses paper-specific method and evidence, and contains no brms/Stan-holdout or Stage-4 fixture leakage;
- cardiac-ultrasound deck uses real licensed article medical images where scientifically needed, preserves their clinical/segmentation semantics and source pixels, and contains no fabricated medical evidence;
- both decks are complete source-driven paper talks, not a small set of benchmark archetype slides;
- exact CUHK source identity, source-fidelity maps, selected→consumed gold evidence, render-input identities, rendered-pixel identities, PDFs/pages/contact sheets and quality-loop traces are complete;
- real GitHub CI passes for the published 040 handoff;
- fresh final 040 task-local Visual Review is identity-bound and every substantive page has item-level evidence with no blocking finding;
- each deck's contact sheet is independently item-level `PASS` and explicitly judged mature doctoral group meeting / strong paper talk;
- Planner independently checks source/bundle/trace/render/evidence and agrees that both satisfy Program Goal Final Quality Gates.

## Failure and stop conditions

If either paper fails after its initial render plus, at most, the one existing automatic repair:

- preserve that first unseen failure as terminal evidence;
- that paper permanently loses unseen-holdout eligibility;
- do not tune production on it inside 040;
- 040 cannot be passed by keeping only the successful paper or swapping a new paper mid-task;
- Planner may later create a new bounded generic recovery only if a unique, quality-preserving blocker mechanism exists, then choose a genuinely new paper in a later task.

If both papers pass Terra and Planner:

- 040 task may PASS;
- Stage 5 / Program must immediately route to the **final user acceptance gate** with both real rendered decks exposed for inspection;
- do not declare `ONE_SHOT_QUALITY_PASS`, `PROGRAM_MATURE=true`, disable the Planner automation, or otherwise close the Program until the user explicitly accepts both decks.

## Out of scope

- Reusing or repairing the 038 brms/MedSAM decks.
- Expanding reference/gold corpus from either 040 paper.
- Editing production code, quality-loop mappings or layout emitters based on 040 output.
- Choosing easier replacement papers after first render.
- Manual slide beautification or a second repair cycle.
- Treating CI/compile/top-level package assessability as final visual/scientific quality.
- Final user acceptance; that remains a separate human decision after both real decks pass.