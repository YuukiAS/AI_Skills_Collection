# 059 Research Authoring — G4-C1 Failure Attribution Critic Prompt

你继续作为 AI Research Stack 的长期独立 Critic。

本轮不是重新审核 G1-G3，也不是重新设计 Research Authoring。
只审 G4-C1 的失败归因与最小恢复方案。

不要修改 production candidate。
不要修改 frozen G4 rubric。
不要启动新的 G4 ChatGPT run。
不要让 Codex生产 PDF。
不要更新 live Plugin。
不要调用 paid API。
不要 merge/release。

## Review object

Planner attribution:

`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_PLANNER.md`

Failed G4 review:

`results/research-authoring--formal-production-authoring/G4_CHATGPT_STAGE_REVIEW.md`

Failed review commit:

`424a39b1fba33d310a8a966cc8747ce38eb13d7b`

Final candidate:

`1c37c0715aca0096606f24e56192b7857e72bbd6`

Live plugin:

```text
name = research-authoring
version = 0.3.0
plugin_id = plugins_6ac4471b735881918c17cd310f262429
release_id = pluginrel_6ac4471c7b90819189bc23af890135f3
scope = USER
discoverability = PRIVATE
```

## Required reads

Actual live Plugin Creator source, especially:

- `skills/report/SKILL.md`
- `skills/report/_src/core/source.md`
- `skills/report/_src/report/source.md`
- live plugin manifest

Verify these live files against final candidate C.

Frozen G4 materials:

- `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/REUSED_TASK_DECISION.md`
- `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/CHAT_CODEX_HANDOFF_RUBRIC.md`
- `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/G4_CHATGPT_INPUT_BASELINE.md`

Failed uploaded package, especially:

- `CHATGPT_AUTHORING_QA.md`
- `CODEX_PRODUCTION_HANDOFF.md`
- `CODEX_GOAL_PROMPT.txt`

and:

- `results/research-authoring--formal-production-authoring/G4_CHATGPT_STAGE_REVIEW.md`

Do not rely only on Planner quotations.

## Frozen fact to preserve

G4-C1 itself is real.

Do **not** accept an argument that:
- QA render is not render;
- preview PDF is not PDF production;
- compile-only is exempt;
- the PDF was not “final”, so the Chat stage complied.

The frozen rubric forbids the Chat side from claiming it rendered the PDF.

## Planner attribution to attack

Planner currently concludes:

```text
PRIMARY_ATTRIBUTION =
CHATGPT_RUNTIME/HARNESS_BYPASS_OF_ACTIVE_PRODUCT_BOUNDARY

RESEARCH_AUTHORING_PRODUCT_CHANGE_REQUIRED =
NO_ON_CURRENT_EVIDENCE
```

Direct basis:

1. canonical/live core already says Research Authoring is not a renderer;
2. core routes PDF mechanics and PDF QA to renderer/production owners;
3. report delegate says not to implement low-level PDF mechanics;
4. formal PDF requests hand artifact mechanics to renderer;
5. standalone wrapper contains no renderer runtime;
6. live wrapper source equals candidate C;
7. frozen G4 natural request says Chat produces stable source + Codex handoff, then Codex produces the final PDF;
8. failed package nevertheless executed local XeLaTeX/render/text extraction using generic Chat runtime capabilities.

Planner therefore proposes fixing the G4 **execution harness**, not production source.

## Proposed recovery

Same:
- candidate C;
- live plugin release;
- G2 baseline;
- G4 task;
- frozen rubric.

No product/rubric/task/delta change.

One new bounded G4 Chat-stage attempt is allowed only after this Critic review.

The harness must explicitly operationalize the already-frozen rubric:

```text
This stage ends at stable source + Codex production handoff.

Do not run or claim:
XeLaTeX / latexmk / PDF compiler;
build_pdf.sh;
PDF creation/open/render/raster/page inspection;
pdftotext/pdfinfo/pdffonts;
QA/preview/test PDF.

QA render still counts as render and is forbidden.

Source-only semantic/fidelity QA is allowed.
Layout/render QA remains PENDING_CODEX_RENDER_QA.
```

Fresh output must explicitly record:

```text
CHATGPT_RENDER_ATTEMPTED=NO
PDF_CREATED_OR_OPENED=NO
PDF_RENDER_QA=NOT_RUN_BY_CHATGPT
PDF_TEXT_EXTRACTION=NOT_RUN_BY_CHATGPT
NEXT_OWNER=CODEX
```

First failed G4 package remains FAIL and cannot contribute PASS subfindings.

Codex production still cannot start until the fresh Chat-stage package independently PASSes.

## Questions for Critic

Only decide:

1. Does the live product source already contain a sufficiently direct renderer-owner boundary to make G4-C1 primarily a harness/runtime bypass rather than a missing Research Authoring product rule?
2. Did the frozen G4 execution prompt fail to operationalize the rubric strongly enough at command level?
3. Is one bounded harness-only retry justified by new information, without changing product/rubric/task?
4. Does this preserve the no-adaptive-chasing rule because the first failed package stays FAIL and the new attempt is explicitly a recovery attempt?
5. Can G1-G3 and candidate C remain valid because no candidate-owned content changes?
6. Is the proposed no-render/no-PDF command boundary sufficient without adding duplicate production rules?
7. Is there any direct evidence that instead requires a product change now?

## Output

Only:

`RESULT = PASS`

or

`RESULT = REVISE`

If PASS, explicitly record:

```text
G4_C1_ATTRIBUTION=HARNESS_RUNTIME_BYPASS
PRODUCT_CANDIDATE_CHANGE_REQUIRED=NO
FINAL_CANDIDATE_COMMIT=1c37c0715aca0096606f24e56192b7857e72bbd6
G1_G3_REOPEN=NO
FAILED_G4_ATTEMPT_REMAINS_FAIL=YES
G4_HARNESS_RECOVERY_ALLOWED=YES
CODEX_PDF_STAGE_ALLOWED_NOW=NO
```

Then provide one bounded next-role prompt to perform **only** the fresh G4 ChatGPT-stage recovery and stop for independent Chat-stage review.

If REVISE, each blocker must state:
- requirement;
- direct evidence;
- causal risk;
- minimum closure;
- owner.

If you conclude product source must change now, explicitly state:
- which exact candidate-owned files need change;
- why the existing rule is insufficient rather than merely bypassed;
- which G1-G4 evidence becomes stale under same-final-candidate policy.

Do not reopen architecture or add a fifth Gate.
