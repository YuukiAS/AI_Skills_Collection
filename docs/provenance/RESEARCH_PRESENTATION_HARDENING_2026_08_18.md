# Research Presentation Hardening

Date: 2026-08-18

Baseline: `f88f3d9c5fec73b1a2ea0e15bb3e45c6a400b883`

Scope: post-4.4.0 hardening for editable `research-group-meeting` presentation support.

## Reviewed Handoff Phases

| Phase | Status | Evidence |
|---|---|---|
| `001_reference_library_expansion` | PASS | Added rebuildable metadata source manifest, search matrix, 72 page-level reference rows, and workflow documentation. Local `.cache` expanded but not committed. |
| `002_validator_and_evidence_integrity` | PASS | `validate_deck_plan.py` now supports `planning` and `final` phases, structured Evidence Board items, and `source_evidence_ids` referential integrity. |
| `003_real_pptx_regression_generation` | PARTIAL | Generator creates a real PPTX, synthetic scientific objects, evidence manifest, and render status. It no longer writes final QA/PASS. |
| `004_independent_scientific_visual_review` | BLOCKED_REAL_PPTX_RENDER in this environment | Independent reviewer exists and refuses to PASS without PNGs rendered from the PPTX by `soffice`, `libreoffice`, or an explicit renderer. No such renderer was found on this host. |
| `005_release_acceptance` | BLOCKED | Do not claim 4.4.1 release acceptance until a real PPTX renderer produces PNGs and the independent reviewer returns PASS. |

## Reference Library State

Local ignored cache path:

```text
.cache/research-presentation-reference-library/
```

Local cache status at implementation time:

- PDF/PPTX assets in `.cache/research-presentation-reference-library/sources/`: 39
- Local cache manifest: `.cache/research-presentation-reference-library/manifest.jsonl`
- Cache manifest rows: 47
- `git check-ignore -v` confirms `.cache/` ignores the cache manifest and downloaded PPTX/PDF assets.

Committed metadata:

- `skills/tools/documents-media/presentations/shared/references/build_reference_metadata.py`
- `skills/tools/documents-media/presentations/shared/references/reference_sources_manifest.json`
- `skills/tools/documents-media/presentations/shared/references/reference_source_search_matrix.csv`
- `skills/tools/documents-media/presentations/shared/references/research_slide_reference_index.csv`
- `docs/workflows/RESEARCH_PRESENTATION_REFERENCE_LIBRARY.md`

## Renderer Status

Renderer probes did not find:

- `soffice`
- `libreoffice`
- `unoconv`
- `chromium`
- `google-chrome`
- `docker`
- `podman`

The regression therefore records `BLOCKED_REAL_PPTX_RENDER` rather than producing a parallel PDF or marking visual QA as PASS.

## Release Rule

This hardening can be committed as architecture and test coverage. It must not be described as a completed 4.4.1 release until phase `004_independent_scientific_visual_review` passes on PNGs produced from the editable PPTX by a real presentation renderer.
