# Reviewed Handoff Request — 047_writing_style_scientific_rewrite_architecture

## Objective

Start a bounded `writing-style` architecture experiment for fidelity-constrained document-level scientific rewriting.

The final user-facing product remains the existing `writing-style` plugin. This task must not create a new top-level plugin and must not continue the instruction-only repair path from 044. The intended direction is a document-level scientific rewrite route that can take a Chinese scientific or technical long report and rewrite it into natural, direct, reader-friendly Chinese while preserving meaning, facts, equations, citations, terminology, uncertainty, attribution, and conclusion strength.

The current candidate architecture is:

```text
source
-> document understanding
-> loss-aware claim / terminology map
-> task and discourse classification
-> retrieve relevant positive transformations
-> meaning-first local rewrite
-> exact deterministic verification
-> independent semantic fidelity verification
-> targeted repair
-> Chinese prose review
-> whole-document coherence review
```

Planner owns the frozen scope, implementation target, holdout rules, release/version decision, and final review contract. Executor must not write `PLAN.md`, must not expand this into a generic humanizer, and must not declare Program PASS without current CI and Reviewer evidence.

## User-provided inputs

- Task key: `047_writing_style_scientific_rewrite_architecture`
- Target branch: `reviewed/047_writing_style_scientific_rewrite_architecture`
- Repository: `YuukiAS/AI_Skills_Collection`
- Base requirement: start from latest `main`, not from 044.
- Current refreshed base: `origin/main` at `8909eb1389dcc419d3168c13e1cddbcf252134cf` (`Add CAT-TRACE v8 audience and regression evidence`, commit time `2026-09-01T16:04:39+08:00`).
- Repository version at intake: `5.0.3`.
- Marketplace plugin versions at intake:
  - `writing-style`: `0.1`
  - `presentations`: `0.3`
  - `ai-skills-core`: `0.2`

### External repositories inspected for architecture intake

The external sources were downloaded into machine-local cache only:

```text
/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/
```

They must not be vendored wholesale into this repository.

- `MrGeDiao/shuorenhua`
  - Remote: `https://github.com/MrGeDiao/shuorenhua.git`
  - Inspected commit: `6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`
  - License: MIT
  - License SHA256: `d26eebf6104e9770ca097771022767da18fc07ca73a542469d2748b2e3186878`
  - Intake expectation after inspection: `SELECTIVELY_PORTED`
- `whh110112/human-writing-skills`
  - Remote: `https://github.com/whh110112/human-writing-skills.git`
  - Inspected commit: `2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`
  - License: MIT
  - License SHA256: `4683c8e7b19375dad28c8589e7b31bb67eadcc6799ce14ab9feb64f1d21e3c1a`
  - Intake expectation after inspection: `SELECTIVELY_PORTED`

Detailed adoption notes are in `results/047_writing_style_scientific_rewrite_architecture/SOURCE_ADOPTION.md`.

### Existing evidence that must shape the Plan

#### A. 044 negative evidence

Task 044 is now read-only regression evidence. It must not be modified, merged, deleted, or used as the source branch for 047.

The relevant finding is not that one or two words were missed. The failure mode is that an instruction-only architecture, protected-span accumulation, phrase scanning, and whole-text reviewer reading did not reliably produce natural Chinese scientific rewriting. 044 showed that even after production `writing-style` replay, the final private `rewritten_report.md` still let ordinary English abstractions such as `provenance`, `estimand`, `scientific gap`, `residual gap`, `state of the art`, `resource contract`, `testbed`, `baseline`, `shared initialization`, `local drift`, and `pooled gap` carry Chinese sentence structure. That is a known regression, not an unseen holdout.

No 047 implementation should solve this by adding another banned phrase list, project-specific English blacklist, or regex completion gate.

#### B. TRACE v8 -> v9 positive evidence

TRACE v8 -> v9 is positive production evidence for a meaning-first writing pattern, but it is presentation/slide evidence, not proof that Chinese long-form scientific rewriting is solved.

The useful pattern is:

```text
audience
-> page purpose
-> meaning / role
-> first-use context
-> reader takeaway
-> positive wording direction
-> rewrite
-> full-artifact language pass
```

Planner should treat this as evidence that positive direction and audience/meaning decomposition are worth testing, not as a ready-made long-report holdout.

#### C. Deep Research architecture decision

The Deep Research decision boundary is to move from "more rules plus English scan" to an explicit document-level architecture:

- document map before local rewriting;
- argument/discourse units instead of full-document one-shot rewriting or sentence-by-sentence rewriting;
- meaning cards with source coverage audit;
- fidelity ledger that separates literal preservation from semantic preservation;
- deterministic exact checks for numbers, dates, units, citations, formulas, identifiers, and formal names;
- independent semantic checks for omitted, reversed, broadened/narrowed, invented, reattributed, uncertainty, caveat, and conclusion-strength changes;
- positive transformation examples that teach rewrite operations without leaking facts.

## User constraints

- `writing-style` remains the only top-level product entry. Do not create another top-level plugin.
- 047 must not continue modifying 044. Keep `reviewed/044_writing_style_deep_research_chinese_replay` as read-only regression evidence until Planner/user decides final disposition.
- Do not merge 044, do not consume stale 044 review artifacts, and do not bring 044 implementation diff into main as the basis for 047.
- Do not write `PLAN.md` in this intake commit. Initial legal state is `PLAN_REQUESTED`; the dedicated Scheduled GPT Planner named "Scientific Rewrite Handoff" owns `PLAN_FROZEN`.
- Do not use the generic watcher; it is not task-key bound.
- Do not vendor external repositories into `AI_Skills_Collection`.
- Do not turn external sources into runtime dependencies unless Planner explicitly freezes that choice.
- Do not copy full phrase lists or fiction/webnovel architecture into `writing-style`.
- Do not use FAISS, Chroma, BGE, `sentence-transformers`, or embedding API dependencies in the P0 experiment unless metadata retrieval is first proven to be the blocker.
- Do not commit private 044 plaintext or private Text Review material.
- Do not declare architecture maturity from clone completion, synthetic benchmark success, 044-only PASS, or tests alone.
- If the real unseen holdout evidence remains insufficient, the Plan must classify this as `EXPERIMENTAL ARCHITECTURE PROTOTYPE`, with `NO_BUMP` and `NO_PRODUCTION_CUTOVER` unless later Reviewer evidence justifies release.
