# 054 Clear Writing — Failure Attribution Critic Contract

Status: AUDIT_ONLY

This contract exists because 054 reached a final Terra `REVISE`, but the four findings may mix true Clear Writing defects, source-quality issues, reviewer overreach, contract ambiguity, and gaps in pre-Terra qualitative QA. Do not create 055, modify production code, mutate the 054 Goal/Plan/CURRENT, or spend another paid review before this attribution is resolved.

## 1. Source of truth

Read, in order:

1. `AGENTS.md`
2. `docs/goals/054_CLEAR_WRITING_RELEASE_CLOSURE_GOAL.md`
3. `automation/reviewed_handoff/tasks/054_clear_writing_release_closure/PLAN.md`
4. `automation/reviewed_handoff/tasks/054_clear_writing_release_closure/CURRENT.json`
5. `docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md`
6. `results/054_clear_writing_release_closure/FINAL_REPORT.md`
7. `results/054_clear_writing_release_closure/text_review/TEXT_REVIEW.json`
8. 054 Deep Research source/task/intermediate/final artifacts under repo-local `private/exports/054_clear_writing_release_closure/`
9. 054 H1/H2/H3 frozen TASK/source/intermediate/final artifacts
10. current Clear Writing source (`scientific-rewrite`, `chinese-prose`, `writing-fidelity`) only to understand the frozen contract; do not edit it.

The critic must distinguish three different truth questions:

- **rewrite fidelity:** did the candidate preserve or distort what the provided source says?
- **reader-facing quality:** did it turn source material into an appropriate finished document for the frozen user task?
- **external factual truth:** is the source itself historically/scientifically correct according to outside knowledge?

Clear Writing is source-faithful rewriting by default. External fact-checking is not silently part of the contract unless the frozen task/Goal explicitly asks for it.

## 2. First legality check — can 054 itself still reach release PASS?

Before discussing a repair, answer from the frozen 054 Goal/Plan and `PAID_EXTERNAL_REVIEW_POLICY.md`:

- 054 froze exactly one final Terra call and it has been consumed with `REVISE`.
- the 054 fresh batch was already evaluated.
- an existing paid-review campaign cannot be enlarged in place after reservation merely to add another final call.
- a Plan revision cannot weaken or replace the canonical Goal.

Determine whether any repository-supported legal path still allows 054 itself to become release PASS **without rewriting historical review evidence or mutating the frozen paid/fresh contract**.

If not, state clearly:

`054_RELEASE_PASS_STILL_LEGAL = NO`

This does **not** prove a product redesign is needed. It only means any later release-validation campaign must use a successor contract after the attribution audit establishes what, if anything, needs product repair.

Do not recommend a successor scope until Sections 3–6 are complete.

## 3. Terra F1–F4 provenance tracing

For each finding, trace:

`raw source -> frozen TASK/user intent -> Meaning Map / Reader Plan / semantic audit -> final candidate -> Terra rubric/finding`

For each F1/F2/F3/F4 answer all of:

1. What exact frozen Goal/Plan/TASK requirement governs this case?
2. Is the challenged content already present in the source?
3. Was it preserved, introduced, strengthened, reattributed, or merely reformatted by the candidate?
4. Is it genuinely useful reader-facing scientific/technical content, reproducibility detail, source packaging, project-internal execution detail, or future-work/research-plan content?
5. Why did pre-Terra local/semantic QA pass it?
6. Did Terra apply a requirement actually present in the frozen rubric/contract, or invent a broader requirement?
7. Does fixing it require changing Clear Writing production behavior?

Use one or more of these classifications only:

- `TRUE_CLEAR_WRITING_PRODUCT_DEFECT`
- `REVIEW_RUBRIC_OVERREACH`
- `SOURCE_QUALITY_ISSUE_OUTSIDE_DEFAULT_REWRITE_SCOPE`
- `CONTRACT_AMBIGUITY`
- `PRE_TERRA_QUALITATIVE_QA_FALSE_PASS`
- `MIXED`

### F3 — H1 Python code blocks

Do not assume code fences are invalid merely because Terra called them “raw source code”. Compare the actual H1 TASK, 054 Goal/Plan, source, candidate and Terra rubric.

The critic must explicitly answer:

- Were code examples necessary/helpful to explain `FeatureHasher` input/use?
- Did the frozen task prohibit them?
- Did the final Terra rubric prohibit legitimate reader-facing code examples, or only raw source/platform markup and formula-like fences?
- Would blanket removal of code conflict with the Goal's requirement to retain reader-useful code/path/config/command when needed for understanding/reproducibility?

### F4 — H3 2015 deep-learning attribution

Start from the tracked H3 source. The source itself states that LeCun, Bengio and Hinton “在2015年正式提出深度学习的概念”. Determine whether the candidate materially changed that claim or faithfully preserved it.

If Terra rejected the claim using external historical knowledge while the frozen task asked source-faithful rewriting rather than fact-checking, classify that explicitly. Do not silently turn Clear Writing into Research Authoring/citation verification.

If the candidate strengthened the source beyond its wording, identify the exact strengthening.

### F1/F2 — private Deep Research

These are the most important unknowns and require direct inspection of the private source/task/intermediate/final artifacts.

Trace Terra examples such as:

- “下一轮最小实验”
- “本项目未验证”
- `Dataset501_CAREMyoPS/.../fold_0/checkpoint_best.pth`
- `mms_data_contract.md`

For each class determine whether it is:

- necessary scientific conclusion/limitation,
- legitimate future-work section,
- necessary reproducibility detail,
- project-internal execution plan/status,
- source/repository metadata that should have been filtered,
- or something introduced/strengthened by the rewrite.

Do not use keyword presence alone. Judge the surrounding paragraph and the frozen reader task.

## 4. Audit the pre-Terra QA design

Explain how 054 could record known/stress + Deep Research + fresh batch as PASS and still receive a four-finding Terra `REVISE`.

Specifically assess:

- whether semantic audit mainly checks consistency with the Meaning Map rather than whether the Meaning Map itself selected the right reader-facing content;
- whether current local QA is overly mechanical (tokens/markup/formulas/tables/keyword scans) and weak on whole-document finished-reader judgment;
- whether the host model is effectively self-certifying qualitative quality;
- whether the final Terra rubric exceeded the frozen product contract in F3/F4;
- whether the single independent qualitative review occurs too late in the campaign;
- whether the campaign needs a **zero-paid, independent whole-artifact critic/reviewer before fresh freeze / final paid Terra**, or another simpler control.

Do not propose “add more tests” unless each proposed test prevents a concrete observed failure.

## 5. Architecture decision

Decide whether the 051–054 heavy architecture itself is wrong.

Choose exactly one:

- `ARCHITECTURE_KEEP_AND_HARDEN`
- `ARCHITECTURE_PARTIAL_REDESIGN`
- `ARCHITECTURE_REPLACE`

`ARCHITECTURE_PARTIAL_REDESIGN` or `REPLACE` requires evidence that Meaning Map / Reader Plan / REALIZE_MEANING / fidelity ownership is itself causing failures, not merely that QA/rubric missed them.

## 6. What a successor would actually need — only after attribution

Because 054's frozen final Terra has already been consumed, if future release validation is still desired the critic may conclude a successor contract is necessary. But it must distinguish:

- `SUCCESSOR_EVALUATION_ONLY`: no production change justified; only corrected review contract + new fresh evidence + new authorized final review are needed.
- `SUCCESSOR_PRODUCT_REPAIR`: one or more true generic Clear Writing product defects require bounded repair before new fresh evidence.
- `SUCCESSOR_ARCHITECTURE_REDESIGN`: only if Section 5 proves the current architecture is wrong.

Do not draft the successor Goal. Do not pick new holdouts. Do not authorize a new paid campaign. This audit is only to decide what the next contract should contain.

## 7. Critic recommendation for future workflow

Assess whether AI_Skills central-plugin refinement should add a repo-local **pre-execution / pre-release critic checkpoint** before launching a new successor Goal or before spending final fresh/paid evidence.

This is AI_Skills repo-specific workflow unless the evidence proves a truly cross-repository general capability; do not modify Bridge Kit here.

If recommending a critic checkpoint, specify the minimum job it must do, such as:

- detect Goal/Reviewer rubric contradictions;
- verify paid/fresh budgets leave a legal recovery path;
- verify reviewer is not adding requirements outside the product contract;
- verify qualitative whole-artifact QA happens before irreversible fresh/paid gates;
- reject a new successor Goal that merely fragments the same unresolved root cause.

Do not design a new state machine/schema/ledger merely to add a critic.

## 8. Output

Write only:

`results/054_clear_writing_release_closure/FAILURE_ATTRIBUTION_AUDIT.md`

Commit and non-force push only that audit file. Do not modify production source, Goal, Plan, CURRENT, historical evidence, paid ledger, or Bridge Kit.

The report must begin with a concise Chinese executive conclusion and end with exactly these fields:

```text
054_RELEASE_PASS_STILL_LEGAL=YES/NO
F1_CLASSIFICATION=...
F2_CLASSIFICATION=...
F3_CLASSIFICATION=...
F4_CLASSIFICATION=...
PRODUCT_REPAIR_NEEDED=YES/NO/PARTIAL
EVALUATION_CONTRACT_DEFECT=YES/NO
PRE_TERRA_QUALITATIVE_QA_GAP=YES/NO
ARCHITECTURE_DECISION=ARCHITECTURE_KEEP_AND_HARDEN|ARCHITECTURE_PARTIAL_REDESIGN|ARCHITECTURE_REPLACE
SUCCESSOR_TYPE=NONE|SUCCESSOR_EVALUATION_ONLY|SUCCESSOR_PRODUCT_REPAIR|SUCCESSOR_ARCHITECTURE_REDESIGN
RECOMMEND_REPO_LOCAL_CRITIC_CHECKPOINT=YES/NO
NEED_BRIDGE_KIT_CHANGE=YES/NO
AUDIT_COMMIT=<sha>
```

`NEED_BRIDGE_KIT_CHANGE` should be `YES` only if the observed defect is genuinely general across repositories rather than AI_Skills-specific review/refinement behavior.