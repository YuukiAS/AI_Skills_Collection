# presentations Changelog

## Unreleased

No pending released changes.

## 0.3 - 2026-09-01

- Tightened Beamer/PDF render routing so YuukiAS/TRACE handoffs preserve the
  current `/home/yuukias/render_resources/chinese_math_pdf` resource location and
  report missing local resources explicitly instead of substituting retired
  server-only paths.

## 0.2 - 2026-09-01

- Added the existing-deck revision production completion gate for targeted research-deck revisions, requiring reviewer-seen baseline evidence, accepted-element ledger checks, targeted feedback, rerender evidence, high-resolution problem pages, first-use dependency order checks, rendered scientific-object QA, English scientific-prose final pass after scientific freeze, and independent visual review before `PASS_REVIEWED`.
- Added public-safe known-failure replay and unrelated reviewed regression fixtures so the production gate blocks the real-use failure classes without packaging private CAT-TRACE rendered pages, TRACE absolute paths, project page numbers, or project-specific scientific content into the installed plugin payload.
- Removed the TRACE checkout-specific Times font path from the CUHK scientific layout renderer; Times font discovery now uses `AI_SKILLS_TIMES_FONT_DIR` or the shared render-resources default.

## 0.1 - 2026-08-30

- Generalized normal production validation so source/deck contract completeness is checked without Stage-4 fixture storyline assumptions.
- Hardened existing-deck revision routing so targeted PPT/deck refinement preserves reviewer-seen baselines, accepted elements, and page-scoped revision intent.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
