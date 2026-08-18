# Research Presentation Hardening

Date: 2026-08-18

Baseline: `f88f3d9c5fec73b1a2ea0e15bb3e45c6a400b883`

Scope: post-4.4.0 hardening for editable `research-group-meeting` presentation support.

## Reviewed Handoff Phases

| Phase | Status | Evidence |
|---|---|---|
| `001_reference_library_expansion` | PASS | Added rebuildable metadata source manifest, search matrix, 72 page-level reference rows, and workflow documentation. Local `.cache` expanded but not committed. |
| `002_validator_and_evidence_integrity` | PASS | `validate_deck_plan.py` now supports `planning` and `final` phases, structured Evidence Board items, and `source_evidence_ids` referential integrity. |
| `003_real_pptx_regression_generation` | PASS | Generator creates a real PPTX, synthetic scientific objects, evidence manifest, and render status. It no longer writes final QA/PASS. |
| `004_independent_scientific_visual_review` | PASS | A user-space LibreOffice AppImage was downloaded to ignored `.cache/tools/`, extracted without FUSE, and used as the explicit renderer. The reviewer saw 4 PNGs rendered from the PPTX and returned PASS. |
| `005_release_acceptance` | PASS | Release acceptance for `v4.4.1` is based on real PPTX rendering plus independent reviewer PASS. |

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

System renderer probes did not find `soffice`, `libreoffice`, `unoconv`, `chromium`, `google-chrome`, `docker`, or `podman`.

User-space renderer used for acceptance:

```text
.cache/tools/LibreOffice-still.basic-x86_64.AppImage
.cache/tools/squashfs-root/opt/libreoffice25.8/program/soffice
```

AppImage details:

```text
size_bytes=291239104
sha256=e9c7d9a2c2f9cc1123452c13ebf5d0e09cd399789e2447d5e0a04bb69c6c2b2d
```

The AppImage could not mount through FUSE, so it was extracted in `.cache/tools/`. The generator now passes a cache-local `-env:UserInstallation=file://.../lo-profile` to LibreOffice so headless profile initialization succeeds.

Regression acceptance artifact:

```text
.cache/research-group-meeting-regression-lo2/RENDER_STATUS.json
.cache/research-group-meeting-regression-lo2/SCIENTIFIC_VISUAL_REVIEW.json
```

Result: `render_status.status=ok`, `png_count=4`, `review.status=PASS`.

## Release Rule

This hardening is accepted as `v4.4.1` because phase `004_independent_scientific_visual_review` passed on PNGs produced from the editable PPTX by a real presentation renderer.
