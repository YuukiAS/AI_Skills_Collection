---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 031_research_presentation_one_call_production_entry
---

# Final Report

## What this task solved

031 established the first real one-call production entry for `research-presentations`. A normal file/path-oriented invocation can now take a supplied research bundle through source ingestion, source-fidelity mapping, storyline/page-job construction, normal Stage 2 gold retrieval, Stage 3 executable layouts, canonical exact-CUHK Beamer generation, real LaTeX compile/render, mechanical QA and task-local visual-review handoff.

The task also closed its first-round rendered-quality blockers: canonical CUHK identity is now visible in the actual content-page pixels, and the same-case medical comparison now exposes GT / Prediction / Error semantics with directly inspectable TP/FP/FN overlays and ROI zooms.

031 does not PASS because the second-round fresh render exposed one remaining production-storyline defect: the normal orchestration places an otherwise valid medical-imaging workstream between clustered-coverage failure analysis and its next experiment, so the deck reads as two workstreams spliced together without an explicit boundary.

## What changed

The production path now has a real shared orchestration surface rather than a benchmark-only entry. It reads user-supplied input from a stable path, creates the normal deck-plan/evidence representations, calls compatibility-driven gold selection and shared Stage 3 layouts, copies the canonical CUHK Beamer source, compiles `.tex` to PDF, renders pages and writes traceable build/visual artifacts.

The first-round repair also changed shared presentation infrastructure rather than patching one output page: the canonical CUHK headline now visibly carries the existing crest in rendered pages, and the shared medical comparison path derives semantic display overlays and matching ROI crops from the same case/error coordinate space. Source/plugin mirrors and regression tests were kept synchronized.

## New capabilities / behavior

The repository can now demonstrate a genuine one-call production chain from supplied research material to source-editable exact-CUHK `.tex`, compiled PDF and rendered content pages while preserving source anchors and runtime gold/layout provenance internally.

The generated content pages can use distinct mature Stage 3 scientific layouts in the same production deck, including native mathematical layout, quantitative plots, typed experiment relations, negative evidence, same-case medical ROI comparison and next-experiment reasoning. Current rendered pages also show canonical CUHK visual identity and medically interpretable GT/prediction/error overlays rather than relying only on source-side claims.

The remaining missing behavior is source-derived multi-workstream storyline grouping. The current runner can construct page jobs, but it does not yet reliably separate independent workstreams into a coherent deck-level sequence with explicit transition cues.

## Deliberately not adopted / unchanged

031 did not use either final Stage 5 holdout paper, did not turn the 027/030 engineering benchmark generator into the product entrypoint, did not force gold IDs or override compatibility scoring, did not expand the gold corpus, and did not introduce a separate visual-review state machine.

The repair did not fabricate a new CUHK identity or replace the medical source case. It reused the canonical CUHK asset and the same-case GT/prediction/error evidence. It also did not implement the full Stage 4 deck-rhythm / bounded automatic repair loop; that remains a separate later Stage 4 concern.

Because the second independent review still found a frozen-Plan blocker, 031 retains its two-round `REVISE` history and must not receive a fabricated third review or be relabeled PASS.

## Example usage

A normal user-facing research route can accept a path to a research bundle and produce an exact-CUHK source-editable deck with compiled PDF and rendered pages, while internally preserving which source evidence supported each scientific page and which compatible gold composition/layout was consumed.

For a mathematical methods update, the same route can create a native equation page and presentation-scale result figure without switching to benchmark-specific orchestration. For a medical comparison page, it can render same-case Input / GT / Prediction / Error panels with matching ROI zoom and interpretable TP/FP/FN semantics.

For an input containing two independent research workstreams, the current limitation is visible: the runner may still place the workstreams in a locally valid but globally incoherent order. The next bounded recovery will add source-derived workstream grouping and explicit transition behavior without changing the accepted page layouts.

## Regression and remaining limitations

Real GitHub CI passed for the repair handoff, and fresh task-local visual evidence is bound to implementation `11509b5e2bf7959433f1616c1d4ad77f77f4000e` and the current six rendered content pages. Five pages received item-level PASS; the medical page also passed its internal image-semantic checks but received `REVISE` for deck coherence.

The accepted one-call integration, source-fidelity map, compatibility-driven gold selection, Stage 3 layout consumption, exact-CUHK compile/render, visible CUHK identity, medical overlay semantics and anti-meta leakage must be preserved by follow-up work.

The remaining blocker is specifically deck-level storyline coherence for multiple independent workstreams. Full Stage 4 is still incomplete because deck-rhythm review and the bounded quality-repair loop have not yet been established through the normal production route. Stage 5 real-paper holdouts have not begun.

## Technical appendix

- task: `031_research_presentation_one_call_production_entry`
- initial implementation reviewed in round 1: `93c99427012d771098f4116b81cb7e86e406fbbc`
- repair implementation: `11509b5e2bf7959433f1616c1d4ad77f77f4000e`
- repair CI handoff: `47c8330a0893dcb4b4886a0ee227ab57ebf646ca`
- real `Codex Marketplace` run: `33124952035`, conclusion `success`
- fresh visual evidence: `results/031_research_presentation_one_call_production_entry/visual_review/VISUAL_REVIEW.json`
- visual evidence id: `visual-review-031_research_presentation_one_call_production_entry-bc543a99163b`
- visual identity / manifest SHA: `bc543a99163bebb8ffd274f0dc7834edb531f6fecd5d21ed2600ac5ef6c24ed2`
- generated build manifest: `results/031_research_presentation_one_call_production_entry/generated/BUILD_MANIFEST.json`
- source-fidelity map: `results/031_research_presentation_one_call_production_entry/generated/source_fidelity_map.json`
- runtime trace: `results/031_research_presentation_one_call_production_entry/generated/runtime_trace.json`
- generated exact-CUHK source/PDF: `results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/main.tex` and `main.pdf`
- review rounds used: 2 / 2
- final 031 decision: `REVISE` at review limit; quality-preserving recovery required
