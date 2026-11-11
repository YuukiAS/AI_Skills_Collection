# artifact-content-design — Long-Term TODO

> **USER_DECISION_2026-11-12 — 产品形态已确认。**
>
> Artifact Content Design 固定为 **共享 standalone Skill**，不做独立 Plugin。它由适用的产物型插件/能力消费，至少覆盖制作前的可见内容准入与层级判断，以及**真实渲染后的整件作品复审**。后文仍保留的 “standalone skill / shared contract / Artifact Director / 分散到各 owner” 等比较属于历史研究问题，不再表示产品形态仍待用户裁决。
>
> Canonical product-shape decision: `docs/design/SHARED_CAPABILITY_PRODUCT_SHAPE_DECISIONS_2026-11-12.md`.


Future standalone capability for deciding what a reader-facing artifact should visibly contain before or alongside rendering.

## Open candidates

### Cross-artifact content restraint and whitespace
status: NEW
source: repeated user feedback across DII Notion, generated images and product/UI artifacts; CAT-TRACE Numerical Atlas full-copy audit and user acceptance, 2026-10-27
evidence: `YuukiAS/AI_Research_Toolkit` branch `research/complex-system-showcase-20261026-r2-comparison`, `docs/history/notion/distributed-imaging-inference-version-history-2026-10-24-to-2026-10-27.md`; `YuukiAS/CAT-TRACE` branch `feat/numerical-atlas-20261023`, commits `f9ff1b8c530ad8dd749bb0b1396cdd41c0303108` and `cb5d1907fc24b1923c8f6a9e6dcbae5a92b40ed1`, `apps/numerical-atlas/docs/copy-audit/COPY_AUDIT_20261027.md`
problem: Different artifact types repeatedly become over-authored even when the underlying content is correct. The model adds explanatory text, labels, guidance, metadata, sections or decorative structure after the user already has enough information to understand or act. The missing capability is not ordinary prose polishing or low-level rendering; it is deciding what should be visible at all, at what granularity, and when the artifact should stop explaining and leave space.
scope examples: Notion/project pages, UI, generated visual artifacts, documents and presentations where content selection and visual restraint matter before final rendering.
boundary: Clear Writing owns prose quality; product-ui-copy owns interface wording; research-writing owns research-document semantics; presentations and visualization own their domain composition; renderers own faithful layout. This future capability should not silently absorb those responsibilities.
project-specific context: DII page history and current Notion cleanup are evidence only. CAT-TRACE method identities, formulas, accepted-versus-candidate method boundaries and unpublished-data boundary are also project-specific. Do not encode either project's sections, terminology or research workflow as generic behavior.
next research step: audit overlap with existing authoring, UI, presentation, visualization and rendering skills; determine whether this becomes one standalone skill, a shared pre-render contract, or a small capability consumed by artifact-producing skills. Do not implement production behavior until that ownership study is complete.

#### Accepted real-use evidence: CAT-TRACE Numerical Atlas

A rendered-state inventory covered 11 routes plus desktop, mobile, filtering, selection, expansion and primary interaction states. It found 420 unique baseline copy units. The final checklist contained 423 disposition rows: 360 `KEEP`, 52 `REVISE` and 11 `DELETE`; the accepted render contained 403 unique visible copy units.

The useful evidence was not a universal word-count target. The repair removed repeated process guidance, duplicated status, rigid field headings, unsupported interaction claims and reader-facing internal framing while retaining formulas, method identity, failure conditions, privacy boundaries and the distinction between adopted and candidate research methods. User review was performed against both the live website and the complete sentence-level disposition table rather than an implementation summary alone.

The final user correction also exposed a boundary between content admission and wording. The literal translation `primitive` -> `原语` had entered the Chinese UI even though the concrete objects were `log1p` and `expm1`. The accepted wording used `稳定计算` for the control and `数值稳定函数` for the explanation. This terminology repair belongs to product copy and domain naming; artifact-level judgment should decide whether the text deserves space, then hand surviving wording to the appropriate owner instead of preserving a poor sentence merely because its underlying fact is relevant.




### Accepted real-use evidence: Project Atlas — content admission must finish before first delivery
complete itemized evidence: `docs/design/product-ui-copy/evidence/PROJECT_ATLAS_COPY_REVIEW_HISTORY_2026-11-03.md` — preserves every Atlas A/B first-round REVISE/REJECT row, every second-round changed row, and every third-round independent finding with exact before/after text.


status: NEW
source: Project Atlas A/B user-visible content review, 2026-11-03
evidence: `YuukiAS/Project_Atlas` branches `prototype/atlas-a` and `prototype/atlas-b`; first complete reviews at commits `086801e26543f2932233657b5682a460d4aec9eb` and `52d07fbea43addf5292d6fba6cc111d6cdadb88a`; independent follow-up revisions at `a9d4fd4e5e5f1db9a49fee187b9b04e14cb5fe7b` and `2b534c63c648e71f1bf3bd1160804c61b13437e1`.
problem: Two visually mature Project Atlas candidates reached review with large amounts of content that should have been decided before delivery. The first full inventory classified A as 2174 ACCEPT / 472 REVISE / 36 REJECT and B as 203 ACCEPT / 139 REVISE / 39 REJECT. An independent follow-up still found 72 additional A revisions and 25 B revisions. The user therefore had to act as the first effective whole-product editor even though content admission and wording should have been completed before the candidates were presented.

The strongest evidence was not wording-only:
- B listed future DII, Mica and Lucerna decisions under “需要我” before those actions were ready. The correct artifact decision was REMOVE, not better phrasing.
- A/B exposed maintenance/source-process concepts such as source freshness, candidate identity and internal validation language that did not deserve primary user attention.
- Removing rejected “需要我” rows left a large empty region in B until the follow-up review also repaired the composition. Content deletion therefore changes layout and must feed back into the artifact producer.
- Repeated rendered occurrences inflated the review count. A future capability should distinguish **unique semantic content identities** from repeated DOM/theme/view occurrences: editorial judgment happens on the semantic unit, while rendering verification proves every occurrence uses the approved unit.

General lesson:
- Content admission is a **pre-delivery gate**. A reader-facing artifact should not be declared ready and then rely on the user to discover dozens of blocks that should be removed, demoted or rewritten.
- Artifact Content Design should complete KEEP/COMPRESS/DEMOTE/REMOVE decisions before final wording and rendering. Surviving UI text then goes to Product UI Copy; the artifact producer consumes the returned wording and re-renders the whole surface.
- The final artifact review remains necessary, but its normal job is to catch integration/layout leakage, not to perform another large editorial rewrite. If it finds a substantial batch of content-admission defects, the upstream pass failed.
- User acceptance should evaluate the finished artifact’s usefulness, taste and direction. Requiring the user to repeatedly identify internal process language or unnecessary blocks is evidence that the artifact was delivered too early.

Candidate acceptance question to add:

> Before this artifact is shown as ready, has every visible semantic unit already earned its place, received its final reader-facing wording, and been re-checked in the actual rendered composition?

If no, the artifact is still in production, not ready for user acceptance.



### Accepted real-use evidence: expert scientific figures should remove redundant defensive disclaimers

status: NEW
source: CAT-TRACE advisor-facing group-meeting figures, 2026-10-28
evidence: `YuukiAS/CAT-TRACE` results under `results/group-meeting-core-progress-20261028/`; user review of the final predictive-calibration and zero-slot numerical figures
problem: A scientifically correct figure can still be weakened by adding defensive caveats that merely repeat information already encoded in the title, subtitle, axes, or surrounding oral narrative. In expert-facing research communication, these lines can make the artifact look as though it is written for an inexperienced reader or for a hostile reviewer rather than for a knowledgeable advisor. The defect is not wording quality and not plotting accuracy; it is incorrect visible-content admission.

Concrete CAT-TRACE case:

- Figure 1 already stated `360 synthetic columns; 64 supplied parameter draws; 20,000 future replicates per column`. The footer `Validation conditional on supplied parameter draws; not fitted-model recovery.` was factually correct but redundant for the intended advisor audience and should be removed from the figure.
- Figure 2 already stated `Deterministic scan with p_g = m_g = 1000 and q = 0`. The footer `Fixed-parameter numerical diagnostic; not fitted ecological data.` was likewise factually correct but redundant and should be removed.
- By contrast, the in-figure note `Production integrator not yet selected` should remain. It communicates a live research-state boundary that materially changes interpretation of the result: the failure of ordinary local Laplace has been demonstrated, but the replacement method has not yet been chosen.

General lesson to research:

- Do not treat every epistemic caveat as automatically deserving visible space.
- If the artifact already makes the evidence type obvious through title/subtitle/axes, and the audience is expert, repeating `not fitted data`, `not recovery`, `not real-world evidence`, or similar defensive language may be artifact clutter.
- Preserve a limitation when removing it would cause a reasonable expert to misunderstand the scientific state, scope, or decision boundary.
- Remove or demote a limitation when it only restates what the artifact already visibly establishes and adds no new interpretive constraint.
- The decision belongs to artifact-level editorial judgment before rendering; Clear Writing may improve surviving wording, but it should not be asked to polish text that should not be visible.
- Final review must inspect the actual rendered figure and ask whether each caveat earns its visual cost at the intended audience level.

Candidate preflight question:

> If this caveat disappears, would a competent member of the intended audience make a materially different scientific inference from the artifact?

If no, default to REMOVE or move the boundary to oral narration/caption/notes rather than keeping it permanently inside the figure.

This case should be used in future Artifact Director / artifact-content-design evaluation because it distinguishes **necessary research-state boundaries** from **defensive disclaimer debris** without weakening scientific honesty.


### External candidate techniques: UI clutter restraint prompts

status: NEW
source: V2EX thread `GPT 的设计品味令人遗憾。` (2026-11-06), https://www.v2ex.com/t/1254844; user-supplied screenshot, 2026-11-07
evidence: the thread records two lightweight methods proposed for reducing GPT-generated interface clutter; the user is collecting additional examples and does not yet want these promoted into production rules.
problem: GPT-generated interfaces often add secondary labels, explanatory microcopy, warnings, floating guidance, repeated descriptions or decorative text after the layout already communicates enough. This is directly relevant to Artifact Content Design because the failure is deciding what deserves visible space, not merely rewriting the prose.

Candidate methods to retain for later comparison:

1. **Layout-first subtraction prompt.** Exact prompt from the thread: `Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining.` The useful hypothesis is that the model should first use grouping, position, alignment and visual hierarchy to express relationships instead of adding another explanatory label.
2. **Necessary-copy gate.** Keep UI copy only when it helps the user understand, judge or complete an action; remove repeated explanation and decorative text. The expanded version shown in the supplied screenshot adds an important safety boundary: simplification must not remove necessary field labels, business meaning, quantities/units, action conditions, status/error feedback, irreversible-consequence warnings or accessibility names, and should normally stay within the UI being changed rather than trigger an unrelated whole-product rewrite.

Current disposition: **evidence intake only**. Do not treat either phrasing as a validated universal rule yet. Future examples should test when the short layout-first prompt is sufficient, when the explicit necessary-copy gate is more reliable, what each one wrongly removes, and whether either duplicates an existing Artifact Content Design principle rather than adding a new one.

## Preliminary concept sketch — Artifact Director / artifact-level editorial judgment

**Status of this section: PRELIMINARY ONLY.** This is an early working hypothesis captured before formal architecture research. It is deliberately non-binding: future Planner/Critic work may revise individual parts, choose a different ownership model, rename the capability, split it across existing domains, or reject and replace this concept entirely. Nothing below authorizes production implementation.

### Working problem statement

The recurring failure is broader than bad prose or bad rendering. A generated artifact may be factually correct and locally well written, yet still be a poor finished work because it contains too much: unnecessary explanation, labels, process narration, metadata, decorative structure, internal terminology, redundant guidance, or information that is true but irrelevant to the audience's immediate task.

The working hypothesis is that artifact production needs an editorial judgment layer whose first question is not "how should this be phrased?" but **"should this be visible at all?"**

A useful default principle to investigate is:

> Absence does not need justification; added visible content does.

Whitespace and silence are therefore valid design resources rather than empty regions that a model should automatically fill.

### Tentative boundary with Clear Writing

This concept is intended to complement, not compete with, Clear Writing.

A provisional distinction is:

- domain capabilities decide whether the underlying scientific, product, statistical, visual or interaction semantics are correct;
- this artifact-level layer decides what deserves visible space in the final artifact, how much emphasis it deserves, and whether it should instead be compressed, moved, visualized or omitted;
- Clear Writing decides how approved reader-facing language should be expressed clearly and naturally without changing established meaning;
- the artifact-specific producer still owns medium-specific realization, such as interaction design, slide composition, document structure, visualization encoding or image composition.

Under this model, a sentence can be factually correct and well written but still be removed because the audience does not need it. Clear Writing should not be expected to solve that problem by polishing the sentence.

### Tentative editorial actions

A minimal artifact-content decision vocabulary worth researching is:

- **KEEP** — visible content is necessary at its current level;
- **COMPRESS** — the idea matters, but the current granularity is excessive;
- **VISUALIZE** — the information matters, but prose is the wrong carrier;
- **DEMOTE** — useful supporting material belongs in a secondary location, appendix, detail view, note or lower visual hierarchy;
- **REMOVE** — the artifact is stronger without it.

Deletion should be a first-class outcome, not only a correction for factual error.

### Tentative pre-production questions

Before a reader-facing artifact is realized, the layer may need to answer a very small set of questions rather than create a large control schema:

1. Who is the artifact for?
2. What is the reader/viewer trying to understand, decide or do?
3. If only one to three things are remembered, what should they be?
4. Which candidate elements directly support that purpose?
5. Which elements are merely available in the source material but do not earn visible space?
6. What deserves primary, secondary or background attention?
7. Is any prose better represented as a visual object, control, table, figure or progressive disclosure?
8. Has the artifact reached the point where adding more would reduce clarity or restraint?

The desired behavior is the opposite of "the model knows this, therefore it should display this."

### Tentative cross-artifact role

The capability should be generic only where the judgment is genuinely generic. It should not become a universal artifact generator.

A provisional architecture to research is:

```text
user goal / domain truth
        |
        v
artifact-level editorial judgment
(audience, visible-content admission, restraint,
priority, density, medium choice)
        |
        +-----------------------+
        |                       |
        v                       v
artifact/domain producer    Clear Writing
(UI, presentations,         approved visible
documents, images,          wording and fidelity
visualization, Notion)
        |                       |
        +-----------+-----------+
                    |
                    v
             rendered artifact
                    |
                    v
artifact-level final review
(whole-work judgment on the real consumption object)
```

The artifact-specific producer keeps medium expertise. Examples:

- UI/product design owns navigation, components, interaction states and responsive behavior;
- presentations owns deck story, page jobs, slide archetypes, spatial hierarchy and rhythm;
- research-writing owns research-document argument/evidence structure;
- visualization owns encoding and graphical semantics;
- image generation owns image composition and rendering mechanics;
- Notion/project systems own database/view/workspace mechanics.

The shared layer should ask whether a visible element has earned its place, not reimplement those domains.

### Tentative post-render responsibility

A pre-render plan is insufficient. Many failures appear only after individually defensible elements are combined.

The final review should inspect the actual consumption object — rendered UI, slide deck, image, PDF, Notion page, chart, README or other finished artifact — and judge the work as a whole.

Questions worth testing include:

- Is the focal point obvious?
- Is there visible content whose removal would improve the artifact without harming the reader's task?
- Is internal process language leaking into the audience-facing work?
- Does the artifact explain beyond the point of usefulness?
- Is hierarchy being replaced by accumulation?
- Is empty space being respected?
- Would a mature human editor/designer regard any element as unnecessary, defensive, decorative or self-explanatory clutter?

This should be works-level judgment, not merely token scanning, schema validation or render-success checking.

### Tentative integration model

If this idea survives research, it should probably be consumed implicitly by artifact-producing capabilities rather than exposed as another step the user must remember to invoke manually.

Possible consumers include UI/product design, presentations, research authoring, visualization, image generation, documents, Notion/project-page generation and other reader-facing delivery paths.

The important unresolved question is whether the best implementation is:

1. one standalone shared skill;
2. a shared artifact-content contract invoked by several existing plugins;
3. a lightweight common decision kernel plus domain-specific adapters;
4. or no new top-level capability at all, with the useful principles distributed into existing artifact owners.

Formal architecture research should decide this rather than treating the present sketch as the answer.

### Open research questions

Before promotion, investigate at least:

- exact ownership boundaries versus `writing-style`, `research-writing`, `presentations`, product/UI, visualization, documents and image-generation paths;
- whether a shared content-admission decision can remain lightweight instead of becoming another workflow/state/schema layer;
- how to make restraint and deletion reliable without causing silent loss of required information;
- how to represent audience purpose and visible-content priority with minimal overhead;
- whether "whitespace is a valid output" can be operationalized without crude density thresholds;
- how final whole-artifact review should differ across UI, slides, documents, images, charts and workspace pages;
- how to ensure the capability is exercised in normal production paths rather than existing only as a written guideline;
- which mature editorial/design systems or existing repositories provide reusable concepts instead of rebuilding a lower-quality framework from scratch.

Again, this section is only a starting hypothesis. It may be substantially revised or fully replaced after overlap analysis and formal architecture review.

## Additional research note — human-operational information is valid artifact content

**Status of this section: PRELIMINARY ONLY.** This extends the concept above with a concrete lesson from the DII Notion history study. Notion is only one evidence case; the principle should be researched across project workbenches, documents, dashboards, UI, presentations, READMEs and other reader-facing artifacts.

### Do not confuse workflow content with machine-only content

A previous overcorrection treated AI workflow information as something that should automatically disappear from a human-facing workspace. That boundary is wrong.

Workflow information may be exactly what the user needs to understand or operate a long-lived project. If the user may return months later and needs to know which actor does the next step, which prompt or tool to open, what prior results are inputs, what condition advances the work, or when to stop iterating and start validation, that information has earned visible space.

The useful distinction to research is therefore not:

```text
human content vs AI workflow content
```

but closer to:

```text
human-operational semantics vs machine execution mechanics
```

Examples of human-operational semantics that may deserve direct visibility:

- current direction, current stage and next meaningful action;
- which person, model, tool or task should receive the next step;
- which prompt, document, view or control the user should open;
- which prior results are needed before continuing;
- the minimum sequence of stages needed to resume a workflow correctly;
- transition conditions such as "move to validation once the proposal is concrete enough";
- stop conditions such as "continue review only after new evidence or a substantive mechanism change";
- current candidates, key decisions and the few historical judgments that still change present choices.

Examples of machine execution mechanics that usually should not consume visible space unless the human explicitly needs them:

- run IDs, task IDs and internal identity strings;
- branches, commit SHAs and pinning mechanics;
- WRITE_CHECK / HANDOFF / receipt plumbing;
- exact revision-storage conventions;
- internal provenance or recovery metadata;
- implementation details whose only purpose is to keep agents synchronized.

The general design question is: **what is the minimum visible information that lets the intended human understand, decide or continue correctly?**

### Four visibility outcomes before wording or rendering

The earlier KEEP / COMPRESS / DEMOTE / REMOVE vocabulary should be tested with a more explicit information-sufficiency lens:

1. **DIRECT** — show the information where the user is already looking because it changes immediate understanding, choice or action.
2. **COMPRESS** — the information matters, but only the operational or decision-relevant core should remain visible.
3. **LINK / DEMOTE** — the detail is legitimate and may need inspection, but the artifact only needs a short result or link to the full source.
4. **REMOVE** — deleting it causes no meaningful loss of understanding, judgment or operation.

This is not a rigid schema proposal; it is a useful decision test to study. The important behavior is that "important" does not imply "show in full."

### Information sufficiency and the stop-explaining rule

A recurring failure is that a model continues explaining after the artifact already contains enough information.

For each visible block, ask:

1. If this sentence or element is removed, does the user lose understanding, judgment or operating ability?
2. What is the minimum granularity needed to preserve that ability?
3. Has the point already been made by the heading, previous sentence, diagram, table or control?
4. Does the next sentence add a genuinely new fact, decision or action?
5. If not, stop.

The desired artifact may therefore contain deliberate whitespace after a complete instruction or conclusion. A mature artifact should not add "this means...", "this helps avoid...", defensive disclaimers, repeated summaries or examples merely because more explanation is possible.

### Current state should replace stale control information

For long-lived project artifacts, visible control information should usually behave like a maintained workbench rather than an append-only log.

When the active stage changes:

- replace the old "what to do now" with the new one;
- keep an old workflow visible only if the user is likely to return to it as a meaningful historical object;
- otherwise retain the detailed history in the durable source and expose a link only when useful.

The same principle applies beyond Notion: dashboards, project READMEs, status pages and product workspaces should privilege current operational truth over accumulated historical narration.

### Subpages and secondary surfaces should earn their existence

Create a subpage, appendix, details panel or secondary view only when the content forms a coherent object that the user is likely to revisit on its own.

Do not create hierarchy merely because:

- the content is long;
- a workflow has many stages;
- history exists;
- every artifact type "should" have the same sections;
- a model wants somewhere to put information it does not know how to delete.

The alternative may simply be to compress the content, link the canonical source, or omit it.

### Research implication for the future capability

Artifact content design should therefore treat **operability for the human reader** as a first-class admission criterion alongside comprehension and decision support.

A future implementation should be tested on whether it can:

- preserve concise but essential operational instructions;
- remove machine-only execution mechanics from the visible layer;
- compress long workflow contracts into the few steps the human actually needs;
- stop explaining after information sufficiency is reached;
- distinguish current state from historical detail;
- prefer a canonical-source link over duplicated detail when the user does not need the full text in place;
- avoid both failure modes: over-authored artifacts and over-minimal artifacts that leave the user unable to resume work.

The DII Notion case is evidence for this distinction, not a Notion-specific specification. Formal architecture research should test the same judgment across other artifact classes before deciding ownership or implementation.

### CAT-TRACE explainer admitted accurate but reader-irrelevant project metadata into the main artifact
status: NEW
source: CAT-TRACE framework explainer user rejection, 2026-11-11
evidence: exact rejected Markdown preserved at \`docs/provenance/CAT_TRACE_FRAMEWORK_EXPLAINED_ZH_REJECTED_2026-11-11.md\`; source artifact was \`YuukiAS/CAT-TRACE@docs/cat-trace-explainer-20261110\` \`docs/explainer/CAT_TRACE_FRAMEWORK_EXPLAINED_ZH.md\`.
problem: The first page admitted visible content such as the document's internal purpose statement, authoritative commit, implementation-source branches and a disclaimer that no statistical programs had been rerun. These statements were accurate and useful to the authoring process, but the user had asked for an independently readable technical guide and had not asked to see repository provenance in the reader path. The same over-admission continued later through a large current-function/file table, internal C-stage identifiers and branch-specific failure narratives.
problem: The artifact also underused higher-value visible structures. The reader needed an immediate complete formulation, a notation table, a prior table and direct comparisons between parallel model components; instead, those facts were dispersed through prose while lower-value traceability metadata consumed prominent space. This is a content-admission failure before it is a wording or rendering failure.
artifact-content lesson to retain as evidence: Truthful information does not automatically earn main-text space. For a reader-facing technical guide, provenance, file/function locators, branch status and implementation incidents should usually be DEMOTE/LINK/REMOVE unless the reader needs them to understand or act. Conversely, a notation table, prior table, side-by-side component comparison or semantic diagram may deserve VISUALIZE/KEEP because it materially reduces reconstruction effort. The artifact-level pass should decide these visibility outcomes before prose polishing and rendering.
project-specific context: The CAT-TRACE commit/branch names, C-stage labels and exact model components are local evidence. Artifact Content Design is still a future standalone capability under study, not a released plugin; this entry records real-use evidence in its canonical skill TODO and does not authorize a production implementation.

