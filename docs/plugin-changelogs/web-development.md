# web-development Changelog

## Unreleased

No pending released changes.

## 0.3 - 2026-09-28

Before:

- Normal Frontend Design entry still generated a choose-one aggregate, so
  generic work could start from a peer specialist instead of one coordinator.
- Research-product frontend planning remained a separate generic active route,
  which could bypass product/design authority classification.
- Producer admission, browser/native evidence boundaries, handoff action
  reachability, and scale-down were not encoded in one production coordinator
  entry.

After:

- The production `frontend-visual-systems` aggregate is coordinator-first with
  coordinator artifact `system`.
- Product UX, visual direction, tokens, Figma handoff, motion,
  responsive/accessibility review, webapp testing, and research-product
  frontend are coordinator-selected delegates.
- The shared generator now has a minimal opt-in `coordinator-first` mode while
  non-opt-in aggregates retain choose-one behavior.
- Frontend source skills now preserve S1/S2/S3 scale, conditional Figma,
  no-Figma completion, browser/native evidence fidelity, interaction causality,
  P1/P2/P3 producer admission, handoff action reachability, and downstream
  builder boundaries.

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
