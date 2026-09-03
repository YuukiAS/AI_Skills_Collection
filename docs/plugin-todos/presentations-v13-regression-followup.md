# presentations — CAT-TRACE v13 regression follow-up

Status: **NEW real-use feedback packet**

This file records new presentation-plugin failures exposed by the CAT-TRACE v13 review on 2026-09-03. The canonical long-term queue remains `docs/plugin-todos/presentations.md`; this packet exists so the evidence is not lost while the central planner decides how to merge/promote the rules. These are generic presentation-workflow failures, not CAT-TRACE-specific layout recipes.

## 1. First-use must be enforced as an ordering invariant, not merely audited as a definition checklist

status: NEW
source: TRACE / CAT-TRACE v13 user review
evidence: `YuukiAS/TRACE` v13 commit `33b616866a47231b9e74bbc3486aba3b73a5d020`; the deck mentions `CAT-TRACE` in the body of P2, P8 and P12 before the method is formally introduced on P14, despite the existing persistent rule that CAT-TRACE must not appear before motivation and prerequisite background have earned the transition. The v13 task also required first-use and no-new-regression checks.
problem: The current workflow can verify that a term is eventually defined yet still miss that the term appears too early. First-use/dependency QA needs an explicit **ordering invariant** for central methods and concepts. A deck should be able to register a `first_allowed_anchor` or prerequisite set for a method/concept, scan the final audience-facing text in order, and block delivery if the term appears in body/title/table/diagram copy before that anchor. This check must run after all transition/language edits because a late bridge rewrite can reintroduce an early name. References/source credits may need a separate exemption policy, but audience-facing explanatory copy may not rely on future slides for meaning.
project-specific context: `CAT-TRACE`, `TRACE`, `HMSC`, `CORAL` and their exact page order belong to TRACE. The generic failure is treating first-use as “defined somewhere” instead of “not used before prerequisites are satisfied.”

## 2. A scoped visual review must never certify the whole deck

status: NEW
source: TRACE / CAT-TRACE v13 review workflow
evidence: `results/012_cat_trace_group_meeting_v13/review.md` explicitly says the independent reviewer inspected the final PDF/source plus focused high-resolution pages P21, P36 and P42, repaired two local issues, then returned a global `PASS`. The executor subsequently recorded `PASS_REVIEWED`, even though the task's allowed next states did not include that state and the user later found major unreviewed regressions on P2, P6, P12, P21, P25, P35 and elsewhere.
problem: Review verdicts need **scope integrity**. A review of pages/concerns `{P21,P36,P42}` may only return a verdict for that scope. It must not be promoted to full-deck PASS unless all mandatory global gates have independent evidence over the final artifact: dependency order, reader-effort language, new/rewritten slides, diagrams, transition map, and inherited hard constraints. Executor/result aggregation must also respect the task's allowed state machine; it may not invent a stronger completion state. A useful implementation is `review_scope`, `reviewed_requirements`, and `unreviewed_requirements`, with global PASS impossible while the latter is nonempty.
project-specific context: the specific page numbers and `PASS_REVIEWED` string belong to TRACE. The generic issue applies to every existing-deck revision workflow.

## 3. New or substantially rewritten slides need the v9 pre-writing semantic brief again

status: NEW
source: TRACE / CAT-TRACE v8→v9 improvement versus v13 regression
evidence: CAT-TRACE v9 improved markedly without a runtime plugin upgrade because the execution task explicitly fixed, **before writing**, the target audience, each slide's one scientific job, prerequisite context, why unfamiliar terms appear there, and the sentence the audience should remember; it then ran a full-deck first-use registry and page-by-page language audit. In v13, several new slides were drafted directly from a planning document and inherited internal phrases such as `V1 construction`, `V2`, `open-tail backbone`, `stable scientific object`, and `practical theory target`, even though generic scientific-prose checks were requested later.
problem: Accepted quality on old slides does not transfer to newly inserted slides. Every new or materially rewritten content slide should require a small semantic brief **before audience-facing prose is generated**: audience assumption; one page job; prerequisites already established; one concrete object/example if needed; one plain sentence the audience should be able to repeat. The executor must then rewrite planner/internal wording into audience language rather than copy it. A late grammar/style pass is not a substitute for this pre-writing step.
project-specific context: v9/v13 terminology belongs to TRACE. The generic lesson is that pre-writing semantic orchestration is the mechanism that produced the v8→v9 language improvement and must be rerun for every new slide.

## 4. Planner language and internal version labels need an audience-copy firewall

status: NEW
source: TRACE / CAT-TRACE v13 user review
evidence: v13 audience slides contain internal project-management language such as `Where CAT-TRACE V1 deliberately stops`, `Supporting guarantees for the V1 construction`, `The residual factor layer is part of the current V1 model`, and `CAT-TRACE V2`. The user judged this unnatural and irrelevant to the advisor-facing scientific story.
problem: Presentation planning documents legitimately use internal states (`v1`, `v2`, `current construction`, `target`, `roadmap`, implementation names), but these must not automatically become slide copy. Before rendering, the plugin should classify visible phrases by audience role and remove/translate author-facing workflow language unless the version distinction itself is scientifically meaningful to the audience. The visible deck should normally say what the current method does and what a future extension would add, not narrate internal model-version bookkeeping. This is broader than a banned-word list: the check is whether the phrase helps the audience understand the science.
project-specific context: exact `V1/V2` labels belong to TRACE. The generic issue affects roadmaps, research plans, ablations, product versions and method-development decks.

## 5. Diagram QA needs a utility/quality floor, not only semantic correctness and collision checks

status: NEW
source: TRACE / CAT-TRACE v13 P21 user review
evidence: P21's new residual-loading diagram passed a bounded repair for hyphenation and arrow/text collision, yet the user still judged the diagram poor. It uses small rigid boxes, weak visual hierarchy, short mechanical connectors and a central explanation that is harder to parse than the underlying two-species/one-factor idea. Similar diagram failures have recurred since v4-v7 despite existing semantic and geometry guidance.
problem: `no overlap` and `all required nodes/edges exist` are necessary but not sufficient. Before drawing, require a **diagram utility test**: does the diagram let the audience understand the relationship faster than 1–2 sentences plus a small equation? If not, do not draw it. For diagrams that remain, compare the final high-resolution render against a deck-level quality floor: readable node text without forced wrapping, meaningful whitespace, visible non-trivial connector length, clear visual hierarchy, no relationship encoded mainly as prose inside a tiny box, and no unnecessary nodes created only to make a flowchart. Every newly created diagram must receive its own final-render review; repairing one local collision does not certify the overall composition.
project-specific context: the Lambda diagram and exact factor-loading science belong to TRACE. The generic issue is diagram usefulness and visual maturity.

## 6. Example and takeaway must have an explicit explanatory bridge when the conclusion is not self-evident

status: NEW
source: TRACE / CAT-TRACE v13 P6 user review
evidence: P6 states that the Malagasy benchmark has 255,188 OTUs and 182,402 singletons, then jumps to `255,188 OTUs does not mean 255,188 verified species names.` The conclusion is correct in context, but the numerical example itself does not explain why OTU count differs from named-species count, so the takeaway feels abrupt.
problem: An example should not merely sit next to a takeaway; when the inferential link is not obvious, include one short **example→meaning bridge** explaining how the example supports the conclusion. A page-level language audit should ask: “If the example were the only concrete evidence on the slide, would a first-time audience understand why the takeaway follows?” If not, add one sentence rather than relying on the audience to reconstruct the missing link.
project-specific context: the Malagasy OTU counts belong to TRACE. The generic issue applies to scientific examples, numerical case studies and before/after visuals.

## 7. Natural slide language requires more than removing grammatical errors

status: NEW
source: TRACE / CAT-TRACE v13 user review
evidence: several v13 titles and takeaways remain formulaic or author-facing (`TRACE works for future fungal discovery`, repeated `What...` / `Where...` constructions, `CAT-TRACE keeps this calibration...`). The same deck had improved sharply in v9 when prose was rewritten from audience/page-job briefs rather than from template-like labels.
problem: Research-slide language QA should test whether a sentence/title sounds like something a researcher would naturally say aloud to the intended audience. Avoid repetitive template stems (`What...`, `Where...`, `X works`, `X keeps...`) when a direct scientific statement is clearer. Do not create a fixed blacklist; require variation and context-appropriate phrasing, and judge titles/takeaways as spoken scientific language rather than document headings. The presentation orchestrator should supply the page job; writing-style should produce natural prose; final rendered review should still reject stiff but grammatical copy.
project-specific context: exact CAT-TRACE phrases belong to TRACE. The generic issue is spoken scientific presentation prose versus memo/report language.
