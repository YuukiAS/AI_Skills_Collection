---
name: research-reporting
description: Report-family Research Authoring route for advisor reports, group-meeting written reports, milestones, research updates, methods notes, experiment retrospectives, and evidence-backed technical notes; enter the document-level core first, then delegate report semantics to research-reporting.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/writing/research/research-authoring-core
  - skills/writing/research/research-reporting
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
routing_mode: "coordinator-first"
coordinator_artifact_id: "core"
default_prompt:
---

# research-reporting

## Trigger Boundary

Report-family Research Authoring route for advisor reports, group-meeting written reports, milestones, research updates, methods notes, experiment retrospectives, and evidence-backed technical notes; enter the document-level core first, then delegate report semantics to research-reporting.

Use this aggregate Codex App skill by entering the coordinator source first.

## Source Workflows

- `research-authoring-core` (coordinator): Canonical document-level coordinator for Research Authoring. Use before producing or substantially revising reports, manuscripts, related work, research updates, responses, or supplements, including formal-PDF intent. Stabilize source/handoff before admitted rendering; route render-only and support-only work to owners. Reference: `_src/core/source.md`
- `research-reporting` (delegate): Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, advisor/group-meeting reports, and result retrospectives from project evidence. Use for report semantics even when the final deliverable is a formal PDF; stabilize source and handoff before an explicitly admitted renderer owns mechanics. Reference: `_src/report/source.md`

## Plugin Workflow Notes

- For document-producing report-family requests, read `_src/core/source.md` first to freeze audience, purpose, source authority, claim-evidence spine, section jobs, table/figure/formula roles, citation authority, incremental-edit scope, downstream route, and final document-level QA.
- For explicit formal PDF delivery, keep report semantics in Research Authoring and delegate only rendering mechanics to `render-chinese-math-pdf` after a canonical handoff and only when the active profile/surface admits that renderer route.
- A globally installed or discoverable renderer is not admission for a standalone Research Authoring task; the current surface must explicitly authorize the Research Authoring -> renderer sequence.
- On standalone or skills-only surfaces where the approved renderer companion is absent, stop after stable Markdown/LaTeX scientific source plus a complete downstream production handoff; do not create, open, render, compile, preview, or QA a PDF.
- Renderer mechanics include local/preview/QA compile, XeLaTeX, `latexmk`, Pandoc-to-PDF or equivalent PDF compilation, PDF creation/open/render, page rasterization, page visual inspection, and PDF-derived text/font/page QA such as `pdftotext`, `pdfinfo`, or `pdffonts`.
- Generic runtime, file, or compute capability is not a substitute for `render-chinese-math-pdf`; Markdown/LaTeX source authoring, source-only semantic/fidelity QA, and full Codex/downstream renderer handoff remain allowed.
- Any layout correctness that requires compile/render stays pending for the downstream renderer and must not be closed by standalone Research Authoring.

## Workflow

1. Read the coordinator source `_src/core/source.md` first.
2. Let the coordinator classify the task, authority, surface, risk, and required delegates.
3. Load delegate sources only after the coordinator selects them.
4. Return delegate findings to the coordinator for convergence, admission, and final handoff.
5. Follow stricter current-project instructions when they apply.
