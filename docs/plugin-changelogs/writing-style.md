# writing-style Changelog

## Unreleased

No pending released changes.

## 0.2 - 2026-09-10

Reader-facing scientific/technical rewrites now avoid source-process framing in standalone prose. The scientific-rewrite route rejects output that says things like "原文指出", "根据给定材料", or "源文说明" when the user asked for a normal reader-facing rewrite, while still preserving legitimate author or literature attribution.

Reviewed Handoff Text Review packet construction now keeps workflow identities, gate labels, run ids, commits, hashes, and review-wrapper labels out of the prose body sent for external text review. Multi-document review packets use natural document titles instead.

Regression evidence for this release covers the Bloom known regression, unrelated light Chinese polish, fidelity-only and English scientific-prose compatibility replays, two frozen public-safe fresh holdouts, one final Terra Text Review, and the full Codex Marketplace release workflow.

## 0.1 - 2026-08-30

Initial independent plugin baseline in AI_Skills_Collection repository `5.0.0`.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
