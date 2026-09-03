# presentations — CAT-TRACE v14 content/language second-gate feedback

Status: **NEW real-use feedback packet**

Source: TRACE / CAT-TRACE v14 human review on 2026-09-03.

This packet records failures that remained **after** the major v13 narrative/diagram repair. The important lesson is that a first structural/style pass can make a deck look substantially better while still leaving content-language problems that make the talk tiring or unnatural. These are generic presentation-workflow issues, not CAT-TRACE-specific wording recipes.

## 1. A final content-language gate is distinct from grammar/style cleanup

status: NEW

evidence: CAT-TRACE v14 is visually cleaner and removes several v13 regressions, yet the human review still found many technically correct sentences that sound like memo/report prose rather than something a researcher would naturally say aloud: `A regional catalogue is not automatically a site-specific dark-diversity set`, `specification-sensitive discovery prediction`, `The fitted model should report...`, `This remains future model design...`, and multiple narrator-style labels.

problem: A presentation can pass first-use, grammar, collision, and ordinary scientific-prose checks while still being cognitively stiff. Research-deck production needs a **second content-language gate after the first repair pass**. This gate should reread the final slide as spoken explanation and ask: (1) would the presenter actually say this sentence aloud; (2) does every sentence explain the science rather than the document/workflow; (3) did simplification remove context the audience still needs; and (4) can a first-time audience infer why the next statement follows without reconstructing missing logic.

project-specific context: the quoted CAT-TRACE sentences are evidence only. The generic requirement is a second reader-effort/content-language pass after structural repair.

## 2. Declarative scientific titles should be the default; pseudo-question titles are a recurrent AI pattern

status: NEW

evidence: v14 still contains explanatory titles such as `What does an external catalogue mean in practice?`, `What can be known before discovery?`, and `How to read the residual loading Lambda`. These slides do not genuinely ask the audience to solve a question; they explain a scientific relationship. The same deck has repeatedly accumulated `What...`, `Where...`, and `How...` template titles across revisions.

problem: Do not turn an explanatory page into a question merely to make the title sound engaging. Use a question title only when the page genuinely poses a scientific/design question whose answer is developed on that page. Otherwise prefer a declarative title that states the relationship the audience should learn, e.g. `A regional catalogue can contain species we have not seen locally`, `Identity determines how much we can borrow`, or `Residual loadings describe shared unexplained gradients`. This should be checked as part of spoken-language QA, not implemented as a blind ban on the words `what/how/where`.

project-specific context: exact titles belong to TRACE. The generic failure is pseudo-question titling.

## 3. Narrator/meta table headers such as `What it says` should not survive into audience-facing slides

status: NEW

evidence: v14 residual-diagnostic P13 uses the table header `What it says`. Similar narrator labels (`What it measures`, `What this means`, `How matching works`) have appeared repeatedly in earlier deck versions.

problem: Table/list headers should name the scientific role of the column, not narrate the fact that the slide is explaining something. Prefer concrete labels such as `Interpretation`, `Purpose`, `Matching rule`, `Result`, `Evidence`, or eliminate the table when two short statements are clearer. `What it says`, `What this means`, `How it works`, and similar meta-microcopy should trigger a rewrite unless they are genuinely the clearest audience wording.

project-specific context: v14 P13/P16 are current examples. The generic issue is narrator/meta microcopy.

## 4. Simplifying a slide must not delete the narrative that explains why the object is in the talk

status: NEW

evidence: v14 dataset pages became visually cleaner but were over-compressed. Finland, Malagasy arthropods, and Victoria plants now read mainly as figures + data tables + a Question block. Earlier versions contained enough prose to explain why each dataset occupies a distinct role: continuity with TRACE; extreme rare/open-tail stress test; identity-rich catalogue borrowing case.

problem: Language/layout cleanup can create a **semantic deletion regression**. For a real-data slide, preserving the numbers and question is not enough. The page should normally answer in 2–3 natural sentences: what was sampled; what makes this dataset statistically distinctive; and why it appears at this point in the paper/talk. Keep a deliberate gap between this narrative and the data table so the table supports rather than replaces the explanation. After any compression pass, recheck that every major scientific object still has an audience-facing reason to exist.

project-specific context: exact dataset roles belong to TRACE. The generic issue applies to datasets, experiments, case studies, and benchmark pages.

## 5. First-use/context QA must include figure legends, axis labels, table cells, and baseline display names

status: NEW

evidence: v14 P12's plot exposes `bigMVP`, `bigMVP-h`, `TRACE-h`, and `TRACE no covariates` directly in the figure even though the audience is not told what the package-style `big` prefix or `-h` suffix means. The prose first-use audit can therefore pass while the rendered figure introduces unexplained shorthand.

problem: First-use scanning must include **all visible text layers**, not only LaTeX body prose: plot legends, tick labels, panel titles, table cells, diagram nodes, annotations, and captions. When implementation/package names add no scientific value, replace them with audience names (`MVP`, `Hierarchical MVP`, `Hierarchical TRACE`) and keep implementation provenance in the source/footer/notes. Presentation-specific figure regeneration is preferred when the original analysis labels are too code-like or too small for projection.

project-specific context: `bigMVP` is a TRACE evidence example. The generic requirement is visible-figure first-use and audience relabeling.

## 6. A result figure should be redrawn around the claim the audience needs to see

status: NEW

evidence: v14 P12 retains analysis-style log-MSE boxplots. They are valid, but the important scientific statement is that vanilla TRACE tends to overpredict in the project reruns and that model specification matters. A package-labeled MSE figure makes the audience decode methods and a transformed loss before seeing that point.

problem: For research presentations, do not inherit a report figure merely because it exists. Identify the single result claim first, then choose a display that exposes that claim directly. If raw split-level evidence supports it, a signed prediction-error plot (`predicted - observed`, zero is ideal) may communicate over/underprediction more directly than log-MSE. If the original metric is retained, relabel methods and axes in scientific language and make the comparison direction explicit. Figure redesign must remain faithful to the underlying data; never choose a transform only because it flatters the focal method.

project-specific context: the Finland rerun is the current example. The generic issue is claim-first presentation figure design.

## 7. Diagram geometry rules are cumulative and must be inherited by every newly drawn diagram

status: NEW

evidence: the rejected v13 Lambda diagram was not merely aesthetically weak: it also reintroduced cramped nodes and short/mechanical connectors despite repeated CAT-TRACE rules on node spacing, minimum visible shaft, natural boundary clipping, peer-edge consistency, and avoiding content compressed around arrows. The v14 repair correctly removed the diagram, but the next theory timeline or any future diagram could regress in the same way if drawn ad hoc.

problem: A new diagram must inherit the **full union** of previously accepted geometry rules; satisfying a new semantic/utility rule does not replace old arrow invariants. Before implementation, record which existing diagram tokens/primitives are being reused. In the final render check: connectors meet node boundaries; visible shafts are long enough to read as relationships rather than tiny ticks; peer edges have consistent treatment; nodes are not squeezed together while unused space exists elsewhere; labels do not sit on shafts; and a repair never trades one old geometry constraint for a new one. If a simple timeline or equation is clearer, use it instead of a box-and-arrow diagram.

project-specific context: the Lambda diagram is the repeated evidence. The generic issue is cumulative diagram-rule inheritance.

## 8. Theory-page status should be conveyed through the scientific narrative, not inconsistent administrative labels

status: NEW

evidence: v14 uses `Theory result 1` followed by two `Theory target` slides. The distinction is scientifically important, but the labels make the section read like an internal project tracker. Adding `Work in progress` to every later title would add more workflow language rather than make the science clearer.

problem: In an advisor-facing theory section, titles should state the mathematical/scientific object. Convey status naturally in the explanation: `We can already show...`; `The next result we need is...`; `Once that limit is established...`. Do not number a single established result as `result 1` when there is no parallel established result, and do not require `work in progress` badges when ordinary prose can make the boundary unambiguous. At the same time, never phrase an unproved target as if established.

project-specific context: exact CAT-TRACE theorem/targets belong to TRACE. The generic issue is audience-facing theory progression versus project-management status labels.

## 9. Mathematical symbols used on the next page must be explicitly defined before reuse

status: NEW

evidence: v14 P20 uses `D_W` in the correlation normalization without defining it, and P26 uses `lambda_{g,m|n}` although P25 has not explicitly introduced the asymptotic limit that this symbol represents. The latter also risks mixing a conditional theoretical limit with a posterior-predictive quantity.

problem: First-use rules apply to mathematical symbols and inferential levels as well as words. Before a symbol is reused across slides, the first page must state what it is and at what conditioning level it lives. In theory/prediction sections, explicitly distinguish fixed-parameter limits from posterior-integrated predictions; do not combine them in one decomposition merely because the notation looks compatible. A final symbol registry should include important cross-page symbols, not only acronyms.

project-specific context: `D_W` and `lambda_{g,m|n}` belong to TRACE. The generic issue is cross-slide mathematical first-use and conditioning-level consistency.

## 10. Oracle/generative checks and fitted simulations need visibly different jobs

status: NEW

evidence: CAT-TRACE Simulation 1A is an oracle-level generative check of the grouped richness theorem; it draws directly from the DGP and does **not** fit CAT-TRACE. The project documentation explicitly describes it as `an oracle calibration check rather than an inference experiment`. Simulation 1B is intended to fit the model and test recovery of the catalogue/open-tail discovery split.

problem: Simulation numbering alone does not communicate scientific role. A presentation should make the contrast explicit: an **oracle/theorem check** asks whether the finite-truncation DGP behaves as the theory predicts; a **fitted recovery simulation** asks whether inference can recover the target from data. Never imply that a DGP-only Monte Carlo check demonstrates estimator quality. Titles/question blocks should expose the job, e.g. `Simulation 1A: Oracle check of grouped richness calibration` versus `Simulation 1B: Fitted recovery of the discovery split`, with a short `no model fitting` clarification on the oracle page when needed.

project-specific context: the exact 1A/1B simulations belong to TRACE. The generic distinction applies to theorem checks, prior-predictive checks, oracle studies, and fitted method comparisons.

## 11. Second-gate acceptance should compare the final deck against the best prior language baseline, not only the immediate predecessor

status: NEW

evidence: the user repeatedly identifies v9 as the point where CAT-TRACE became comfortable to read. v14 improves substantially over v13, but several natural-language and context choices are still weaker than v9 because the immediate comparison is dominated by v13 regressions.

problem: Existing-deck QA should allow a **quality-reference baseline** distinct from the immediate scientific predecessor. For content-language review, compare new/rewritten pages against the best accepted readability standard from the same deck (or an established unrelated example), not merely ask whether they improved relative to the most recent bad version. This prevents a sequence of local repairs from ratcheting quality downward.

project-specific context: CAT-TRACE v9 is the current readability reference; v12 remains a later accepted visual/style reference. The generic issue is maintaining a quality floor across long revision chains.
