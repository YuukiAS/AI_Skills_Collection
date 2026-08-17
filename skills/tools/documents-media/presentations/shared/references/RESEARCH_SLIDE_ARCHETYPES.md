# Research Slide Archetypes

Tables, cards, matrices, and timelines are implementation tools, not page archetypes. Choose the archetype from the scientific job of the page.

| Archetype | Page purpose | Required evidence | Scientific object | Visual priority | Text budget | Allowed fallback | Forbidden fallback | QA criteria |
|---|---|---|---|---|---|---|---|---|
| `RESULT_FIGURE` | Show whether a result supports a claim or question. | Quantitative plot, real table, or source-tracked result. | Data, metric, comparison, uncertainty. | Main evidence dominates the page; annotations stay near data. | Title plus bounded interpretation. | Mark preliminary or move to backup. | Decorative dashboard, claim title without data. | Result is readable in 5-10 seconds and interpretation does not exceed evidence. |
| `FAILURE_CASE` | Explain a concrete hard case or model failure. | Case image, log, metric, or reproduced failure trace. | Case, error type, condition, consequence. | Case/error visual large enough for discussion. | Labels and short diagnosis. | Use anonymized schematic only if privacy blocks image reuse. | Generic warning icon or vague "challenge" card. | Failure changes a research decision or next experiment. |
| `MEDICAL_IMAGE_COMPARISON` | Compare image, annotation, prediction, and error/uncertainty. | Original image plus GT/annotators/prediction/error metadata. | Anatomy/pathology, ROI, overlay, metric. | Aligned views with stable column semantics. | Case id, metric, caveat, source. | Deidentified crop or redraw if privacy requires. | Single mask labeled as unique GT when annotator variability exists. | Views are same case/crop/scale, labels are readable, privacy note is explicit. |
| `STATISTICAL_MODEL` | Explain an estimand, model, assumption, or inference path. | Equation, variable definitions, data-generating or estimation context. | Random variables, observed data, estimator, assumptions. | Formula plus semantic diagram or concrete example. | Minimal definitions and implication. | Move derivation to backup. | Formula as decoration with no inference target. | Audience can tell what is observed, estimated, and inferred. |
| `METHOD_DIAGRAM` | Show what object is transformed by a method. | Method source, architecture, algorithm, or workflow evidence. | Input, operation, output, innovation. | Redraw the mechanism that matters; omit standard parts. | One rationale sentence. | Reference the paper figure and redraw only the needed substructure. | Three generic arrows labeled input/AI/output. | Every node is a scientific object or operation. |
| `EXPERIMENT_DESIGN` | Make a planned or completed experiment critiqueable. | Protocol, sites, treatment/control, endpoints, comparators, success criteria. | Experimental units, assignments, shared information, endpoints. | Design graph or structured protocol. | Enough labels to expose decision points. | Mark as planned if not executed. | Roadmap with no experiment or metric. | Units, interventions, comparators, endpoint, and decision rule are explicit. |
| `NEGATIVE_RESULT` | Use failure to update the research path. | Failed run, non-significant result, loose bound, mismatch, or blocked assumption. | Attempt, observed failure, diagnosis, consequence. | Four-part failure logic. | Short diagnosis and decision consequence. | Treat as next experiment if diagnosis is unknown. | Hide failure behind success-only update. | The slide says what belief or plan changed. |
| `RESEARCH_UPDATE` | Summarize state change since last meeting. | Evidence board entries and source anchors. | Prior question, new evidence, belief update, current uncertainty. | State-change chain, not task list. | Concise and oral. | Use speaker notes for detailed backlog. | Internal planning terms pasted onto slide. | Page distinguishes evidence, interpretation, and uncertainty. |
| `NEXT_EXPERIMENT` | Define the highest-information next test. | Current uncertainty and candidate discriminating experiment. | Competing explanations, intervention/analysis, readout, decision rule. | Explanation fork or experiment spec. | Decision-ready. | Missing-evidence page. | Vague "try more models" next step. | The result of the experiment would choose, freeze, or stop something. |
| `SUPERVISOR_DECISION` | Ask for a concrete answer from advisor/committee. | Evidence summary, tradeoffs, consequences. | Decision options and consequences. | Decision table only if it has real axes. | One question plus choices. | Move unresolved context to notes. | "Questions?" or generic next steps. | A supervisor can answer in the meeting. |

## Object Topology

Use the relationship among scientific objects to select layout:

| Relationship | Composition |
|---|---|
| One main quantitative result | Single large plot. |
| Same case, GT, prediction, error | Aligned sequence. |
| Multiple cases by methods | Matrix with stable row/column semantics. |
| Multi-center or multi-protocol | Small multiples or stratified intervals. |
| Statistical model | Formula plus variable semantics and example. |
| Experimental treatment | Experimental-unit and assignment diagram. |
| New network mechanism | Redraw only the innovation substructure. |
| Ablation interventions | Intervention matrix plus result. |
| Field/season dependence | Scientific timeline tied to sampling units. |
| Supervisor decision | Evidence, choices, tradeoffs, consequence. |
