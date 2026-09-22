# research-writing Changelog

## Unreleased

No pending released changes.

## 0.2 - 2026-09-22

Research Authoring now has a bounded formal-PDF handoff: research-reporting keeps claim/evidence organization and document semantics, then delegates explicitly requested formal PDF mechanics to the standalone `render-chinese-math-pdf` companion when installed through `research-main`.

Before: standalone report authoring could leave users to discover renderer/math/profile issues after the prose was already written.

After: Markdown-only report requests stay Markdown-only, `research-main` installs the renderer companion for complete PDF workflows, and standalone Marketplace Research Authoring fails closed for formal PDF requests when the companion is missing.

## 0.1 - 2026-08-30

Initial independent plugin baseline in AI_Skills_Collection repository `5.0.0`.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
