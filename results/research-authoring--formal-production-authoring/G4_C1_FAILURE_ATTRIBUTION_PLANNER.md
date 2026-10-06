# 059 Research Authoring — G4-C1 Failure Attribution (Planner)

Date: 2026-10-06  
Task: `research-authoring--formal-production-authoring`  
Branch: `work/research-authoring--formal-production-authoring`  
Final candidate: `1c37c0715aca0096606f24e56192b7857e72bbd6`  
Failed G4 review: `results/research-authoring--formal-production-authoring/G4_CHATGPT_STAGE_REVIEW.md`  
Review commit: `424a39b1fba33d310a8a966cc8747ce38eb13d7b`

## Decision

```text
G4-C1 = ACCEPT_AS_REAL_FAILURE
PRIMARY_ATTRIBUTION = CHATGPT_RUNTIME/HARNESS_BYPASS_OF_ACTIVE_PRODUCT_BOUNDARY
RESEARCH_AUTHORING_PRODUCT_CHANGE_REQUIRED = NO_ON_CURRENT_EVIDENCE
FINAL_CANDIDATE_CHANGE = NO
G1_G3_REOPEN = NO
G4_FIRST_ATTEMPT = FAIL_AND_IMMUTABLE
```

This attribution does **not** reinterpret the local XeLaTeX compile, page rendering, or PDF text extraction as “not rendering”. Those operations crossed the frozen ChatGPT/Codex owner boundary and the first G4 ChatGPT-stage attempt is a real FAIL.

The narrower question is why that violation occurred.

## 1. Direct product evidence

The live PRIVATE USER-scope plugin is:

```text
name = research-authoring
version = 0.3.0
plugin_id = plugins_6ac4471b735881918c17cd310f262429
release_id = pluginrel_6ac4471c7b90819189bc23af890135f3
```

Direct Plugin Creator readback shows that the live files are byte-for-byte equal to the Research Authoring candidate copies for the report aggregate, canonical core, and report delegate.

The live wrapper does not bundle a renderer runtime, MCP, connector, database, watcher, or state machine.

### Canonical core already owns the boundary

`skills/report/_src/core/source.md` states that Research Authoring is:

> not a renderer

and routes:

> `render-chinese-math-pdf`, LaTeX, DOCX, Quarto, or PDF skills only for artifact mechanics after the document semantics are stable.

It also states that Research Authoring does not own:

> fonts, pagination, Pandoc/XeLaTeX, PDF QA, Office packing, or renderer implementation.

### Report delegate already owns the handoff boundary

`skills/report/_src/report/source.md` states:

- do not implement low-level PDF/DOCX/PPTX/LaTeX mechanics here;
- when a final formal PDF is requested, stabilize the research semantics first and hand artifact mechanics to `render-chinese-math-pdf`;
- standalone Research Authoring without the renderer companion must fail closed rather than invent a private XeLaTeX route.

Therefore the current candidate does not lack the renderer-owner rule.

## 2. Frozen G4 prompt and rubric

The frozen natural request says:

> 把这份已经通过科学审核的研究更新整理成给导师的正式 PDF。先在 ChatGPT 侧保持科学内容不变，生成稳定的 Markdown/LaTeX source 和完整的 Codex production handoff；再由 Codex 用正式科研文档生产路线生成最终 PDF。不要把它改写成 PPT，也不要改变结论强度。

The frozen G4 rubric independently requires the ChatGPT side to:

> not claim to have rendered the PDF itself

and assigns final PDF production, renderer QA, and post-render Research Authoring QA to Codex.

The natural prompt assigns the production sequence correctly, but unlike the rubric it does not spell out a command-level prohibition such as “do not run XeLaTeX/latexmk/pdftotext/pdfinfo or render pages even for QA”.

That omission is a **G4 execution-harness weakness**, not evidence that the Research Authoring product source grants renderer ownership.

## 3. Failed artifact evidence

The uploaded package `advisor_update_codex_handoff.zip` contains:

- `CHATGPT_AUTHORING_QA.md`
- `CODEX_PRODUCTION_HANDOFF.md`
- `CODEX_GOAL_PROMPT.txt`
- source/fidelity artifacts.

`CHATGPT_AUTHORING_QA.md` explicitly claims:

- a local XeLaTeX QA compile;
- a four-page A4 PDF;
- page-by-page raster rendering and visual inspection;
- PDF text extraction.

This is the violation.

At the same time, `CODEX_PRODUCTION_HANDOFF.md` correctly treats Codex as the production owner and contains the formal compile/render/text-extraction QA contract for the next stage.

The failed ChatGPT stage therefore created a correct downstream production contract **and then prematurely executed part of that contract itself**.

Because the live plugin has no renderer payload, the compile/render execution necessarily came from the general ChatGPT runtime/tool environment rather than the plugin's packaged renderer capability.

## 4. Failure attribution

The failure chain is:

```text
active product source says Research Authoring is not renderer
+ frozen G4 architecture assigns formal render/QA to Codex
+ live wrapper contains no renderer runtime
+ G4 natural prompt asks Chat to produce source + Codex handoff
but
G4 Chat execution harness does not surface the frozen no-render rule as an explicit command-level stop
+ Chat runtime has generic file/compute capabilities
-> model treats “QA compile” as extra source validation
-> model runs XeLaTeX/render/text extraction anyway
-> G4-C1
```

This is classified as:

```text
TEST_RUNTIME_HARNESS_BOUNDARY_BYPASS
```

not:

```text
MISSING_RESEARCH_AUTHORING_RENDER_OWNER_RULE
```

The distinction matters because repository policy says that when an active rule already exists but real use still fails, first repair the caller/prompt/entry/consumer path rather than duplicating the same rule into production source.

## 5. Minimal recovery — no frozen-rubric weakening

Do not patch the failed package and call it PASS.

Do not change the Research Authoring candidate or live wrapper source on current evidence.

Run one bounded fresh G4 ChatGPT-stage recovery after Critic approval with:

- same final candidate;
- same live plugin release;
- same frozen G2 semantic baseline;
- same G4 task;
- same frozen G4 rubric.

The only changed object is the **G4 Chat-stage execution harness**, which must operationalize the existing rubric verbatim.

The recovery harness must state before the baseline:

```text
CHATGPT_STAGE_RENDER_BOUNDARY

This stage ends at stable scientific source + Codex production handoff.

Do not run or claim:
- XeLaTeX, latexmk, Pandoc PDF, or another PDF compiler;
- build_pdf.sh or an equivalent build command;
- PDF creation, opening, rendering, rasterization, screenshot/page inspection;
- pdftotext, pdfinfo, pdffonts, or PDF-derived text/font/page QA;
- any “QA PDF”, “preview PDF”, “test PDF”, or render validation.

A QA/preview compile is still rendering and is forbidden in this ChatGPT stage.

Allowed:
- preserve/check Markdown/LaTeX source semantically;
- run source-only fidelity checks that do not create/read a PDF;
- prepare the complete Codex production/render/QA instructions.

If layout correctness cannot be established without compiling, record it as PENDING_CODEX_RENDER_QA. Do not resolve it here.
```

The fresh Chat package must have a Chat-stage QA receipt that truthfully records:

```text
CHATGPT_RENDER_ATTEMPTED=NO
PDF_CREATED_OR_OPENED=NO
PDF_RENDER_QA=NOT_RUN_BY_CHATGPT
PDF_TEXT_EXTRACTION=NOT_RUN_BY_CHATGPT
NEXT_OWNER=CODEX
```

It may provide a build command or build script **for Codex to execute later**, but ChatGPT must not execute it.

The independent Chat-stage Reviewer must check the complete fresh package, not reuse passed subfindings from the failed package.

Only after fresh Chat-stage PASS may Codex begin the PDF-production half of G4.

## 6. Evidence validity

Because no candidate-owned file changes are proposed:

- `FINAL_CANDIDATE_COMMIT` remains `1c37c0715aca0096606f24e56192b7857e72bbd6`;
- G1, G2, G3 remain closed and are not rerun;
- live Plugin Creator creation/readback remains valid;
- the first G4 ChatGPT-stage package remains immutable FAIL evidence;
- **all first-attempt G4 ChatGPT-stage output/evidence is invalid for a later G4 PASS and cannot be stitched into the recovery PASS**;
- Codex PDF production did not start, so there is no Codex-stage G4 evidence to invalidate.

The recovery must produce a complete new Chat-stage package and a new independent Chat-stage review.

## 7. Escalation condition

If the corrected harness still causes the same live wrapper to compile/render/inspect a PDF, then the “harness-only” hypothesis is falsified.

At that point return to Planner and treat the consumer/product contract as insufficient. A canonical Research Authoring source change would create a new candidate `C2`.

If `C2` changes `research-authoring-core` or report routing, same-final-candidate release evidence on C becomes stale. Under the existing Plan, G1–G4 must be re-established on C2 with risk-matched replay; prior G2/G3 materials become development/regression evidence rather than PASS evidence. Do not avoid that cost by calling the source change “documentation only”.

## 8. Planner status

```text
G4_C1_ATTRIBUTION_READY_FOR_CRITIC=YES
PRODUCTION_CANDIDATE_MODIFIED=NO
FROZEN_G4_RUBRIC_MODIFIED=NO
G1_G3_REVIEWED_AGAIN=NO
FINAL_G4_RECOVERY_STARTED=NO
NEXT_HANDOFF=CRITIC
```
