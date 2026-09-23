# web-development Changelog

## Unreleased

No pending released changes.

## 0.2 - 2026-09-22

Before:

- Frontend Design exposed visual-system and research-product frontend guidance,
  but its production aggregate did not include the existing Figma handoff or
  motion-interaction skills.
- Canonical design artifacts, state coverage, localization tokens, motion and
  actual-surface convergence were not grouped into one production readiness gate.

After:

- Added F-A/F-B/F-C production gates for design authority/state coverage,
  design-system coherence, and actual-surface convergence.
- The `web-development` Marketplace payload now routes the visual aggregate
  through existing `figma-design-to-code` and `motion-interaction` skills in
  addition to visual systems, direction and tokens.
- Frontend Design now distinguishes canonical-design tasks from docs-only,
  backend/server-only and tiny nonvisual tasks so Figma/locale/provider/full E2E
  checks are not over-applied.

## 0.1 - 2026-08-30

Initial independent plugin baseline in AI_Skills_Collection repository `5.0.0`.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
