# G4 ChatGPT-stage independent review

Date: 2026-10-06  
Task: `research-authoring--formal-production-authoring`  
Reviewed live handoff package: `advisor_update_codex_handoff.zip`  
Uploaded package SHA-256: `afc2efd74b80c7e4675dc7133b4c4b5627f92360d92741354efdfe10d6516879`

## Result

```text
G4_CHATGPT_STAGE=FAIL
G4_PASS=NO
NEXT_HANDOFF=PLANNER
```

This is the first substantive G4 ChatGPT-stage result. Do not send the package onward as a passing G4 handoff and do not repair/retry it while still calling the same final evidence PASS.

## What passed

The package is otherwise strong and internally consistent:

- `PACKAGE_SHA256SUMS.txt` verifies every listed package file.
- `G4_CHATGPT_INPUT_BASELINE.md` matches the frozen G4 input byte-for-byte.
- `advisor_update.md` is byte-for-byte the frozen scientific body.
- `python3 verify_fidelity.py` passes.
- Protected claim-strength phrases, numerical tokens, and evidence-anchor expressions are present in `advisor_update.tex`.
- An independent local build of the supplied `advisor_update.tex` succeeds under XeLaTeX and produces a 4-page A4 PDF.
- Independent render inspection found no clipping, table overflow, broken glyphs, heading collision, or obvious readability defect.
- The handoff preserves advisor-facing document identity, final artifact identity, semantic authority, content-preserving edit scope, citation/evidence-anchor boundary, formal LaTeX route, and final scientific QA requirements.
- It does not reroute to Presentations.

## Blocking finding G4-C1

### Requirement

The frozen G4 rubric explicitly requires the ChatGPT side to:

> not claim to have rendered the PDF itself

The frozen G4 task also separates responsibilities:

```text
ChatGPT: semantic authoring + stable Markdown/LaTeX + complete production handoff
Codex: formal PDF production + renderer QA + final Research Authoring QA
```

### Direct evidence

`CHATGPT_AUTHORING_QA.md` states:

- “A local XeLaTeX QA compile of `advisor_update.tex` completed successfully as a four-page A4 document.”
- “Every page was rendered to images and visually inspected.”
- “Text was extracted from the QA PDF…”

The package also includes `build_pdf.sh` and describes the ChatGPT stage as having already compiled and rendered a QA PDF.

### Causal risk

This crosses the exact owner boundary G4 is intended to test. Even though the package correctly says the *final* advisor PDF must still be produced by Codex, the frozen rubric does not permit the ChatGPT stage to claim PDF rendering. Allowing this package to PASS would weaken the already-frozen acceptance criterion after seeing the output.

It also makes the cross-surface test less diagnostic: Codex would receive a source that ChatGPT had already compiled and visually validated, rather than proving the intended handoff from semantic authoring to production/rendering.

### Minimum closure

Do not patch this package and continue the same G4 evidence as PASS.

Planner must attribute the failure using the live wrapper/source and exact G4 prompt:

1. determine whether the live Research Authoring wrapper or its bundled skill instructions encouraged/allowed ChatGPT to perform renderer work despite the frozen handoff boundary;
2. distinguish product-routing failure from a test/runtime behavior outside the plugin;
3. if product behavior must change, create a new candidate and invalidate affected final evidence according to the Capability Gate contract;
4. if direct evidence proves the product correctly forbids rendering and this was exclusively a test/runtime harness violation, propose the smallest evidence-valid recovery without weakening the frozen rubric.

The blocker closes only when a fresh valid G4 ChatGPT-stage artifact demonstrates semantic authoring/handoff without ChatGPT claiming PDF rendering.

## Scope

This FAIL does **not** reopen G1-G3 automatically and does not show scientific-content corruption. It is a G4 cross-surface responsibility-boundary failure.

No main merge, release, paid API use, or additional Plugin Creator mutation is authorized by this review.
