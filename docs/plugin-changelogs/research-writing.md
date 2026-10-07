# research-writing Changelog

## Unreleased

No pending released changes.

## 0.3 - 2026-10-05 (candidate)

Before: `report`, `paper`, and `litcite` could each handle local research-writing work, but document-producing requests could still reach lower-level skills without one shared document-level Research Authoring contract.

After: Research Authoring has a canonical `research-authoring-core` that freezes audience, document purpose, source authority, claim-evidence spine, section jobs, table/figure/formula roles, citation authority, incremental-edit scope, downstream route, and final document-level QA before delegating to report, paper, literature, citation, or artifact skills.

C3 candidate update: the normal-entry owner boundary now distinguishes renderer discovery from renderer admission. Standalone Research Authoring report/manuscript requests that eventually want formal PDF stop at stable source/package plus downstream handoff; `research-main` is the integrated route that admits rendering after handoff and returns to Research Authoring scientific QA; render-only finalized sources bypass Research Authoring planning.

This is a branch-local final-candidate entry. It does not by itself publish a formal repository release, merge to `main`, or change repository `VERSION`.

## 0.2 - 2026-09-23

Research Authoring now has a bounded formal-PDF handoff: research-reporting keeps claim/evidence organization and document semantics, then delegates explicitly requested formal PDF mechanics to the standalone `render-chinese-math-pdf` companion when installed through `research-main`.

Before: standalone report authoring could leave users to discover renderer/math/profile issues after the prose was already written.

After: Markdown-only report requests stay Markdown-only, `research-main` installs the renderer companion for complete PDF workflows, and standalone Marketplace Research Authoring fails closed for formal PDF requests when the companion is missing.

## 0.1 - 2026-08-30

Initial independent plugin baseline in AI_Skills_Collection repository `5.0.0`.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
