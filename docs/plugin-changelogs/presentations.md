# presentations Changelog

## Unreleased

No pending released changes.

## 0.5 - 2026-11-27

- Made the blue `course-standard` Beamer source the default built-in Beamer
  route for research and teaching presentations; CUHK is now selected only
  when the user or repository explicitly requests it.
- Froze `course-standard` and CUHK as one shared body-page system. They now use
  identical fonts, role sizes, leading, title bar, 8 mm margins, captions,
  lists, formulas, tables, footer and navigation; CUHK school identity is
  confined to approved title-page artwork.
- Aligned the shared list spacing and automatic one-line/multi-line caption
  behavior with the accepted standard Beamer reference, and added a versioned
  template-family freeze plus same-content parity regression.

## 0.4 - 2026-10-15

- Bound the canonical CUHK Beamer route to the packaged TeX Gyre Termes text
  and math font files discovered through `render-chinese-math-pdf`, and added
  post-render font inspection so a normal presentation run fails clearly when
  the expected fonts cannot be used.
- Strengthened existing-deck acceptance so it verifies the exact candidate,
  source and rendered artifact identities, page-by-page evidence, contact-sheet
  review, and an independently produced review trace instead of trusting a
  self-declared status or missing artifact paths.

## 0.3 - 2026-09-01

- Tightened Beamer/PDF render routing so <private repository> handoffs preserve the
  current `/home/yuukias/render_resources/chinese_math_pdf` resource location and
  report missing local resources explicitly instead of substituting retired
  server-only paths.

## 0.2 - 2026-09-01

- Added the existing-deck revision production completion gate for targeted research-deck revisions, requiring reviewer-seen baseline evidence, accepted-element ledger checks, targeted feedback, rerender evidence, high-resolution problem pages, first-use dependency order checks, rendered scientific-object QA, English scientific-prose final pass after scientific freeze, and independent visual review before `PASS_REVIEWED`.
- Added public-safe known-failure replay and unrelated reviewed regression fixtures so the production gate blocks the real-use failure classes without packaging private a private research project rendered pages, TRACE absolute paths, project page numbers, or project-specific scientific content into the installed plugin payload.
- Removed the TRACE checkout-specific Times font path from the CUHK scientific layout renderer; Times font discovery now uses `AI_SKILLS_TIMES_FONT_DIR` or the shared render-resources default.

## 0.1 - 2026-08-30

- Generalized normal production validation so source/deck contract completeness is checked without Stage-4 fixture storyline assumptions.
- Hardened existing-deck revision routing so targeted PPT/deck refinement preserves reviewer-seen baselines, accepted elements, and page-scoped revision intent.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
