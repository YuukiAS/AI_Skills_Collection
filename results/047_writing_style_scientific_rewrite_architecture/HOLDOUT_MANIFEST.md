# 047 Holdout Manifest

This manifest freezes evaluation identity before any 047 implementation work. It is an intake artifact for Planner; it does not include private plaintext.

## Base state

- task key: `047_writing_style_scientific_rewrite_architecture`
- branch: `reviewed/047_writing_style_scientific_rewrite_architecture`
- base branch: `main`
- base commit: `8909eb1389dcc419d3168c13e1cddbcf252134cf`
- base commit subject: `Add CAT-TRACE v8 audience and regression evidence`
- repository version: `5.0.3`
- writing-style version: `0.1`
- presentations version: `0.3`

## Freeze rules

- Holdout identity is frozen before implementation.
- Known regression material can prove regression closure, not unseen generalization.
- TRACE v8 -> v9 can motivate architecture, but cannot count as Chinese long-form holdout.
- Do not replace an item because the output is poor.
- Do not tune production code, prompts, example corpus, or deterministic checks on an unseen item and then reuse it as unseen.
- Do not commit private plaintext or private Text Review packets.

## 1. Known regression: 044 Deep Research report

- role: known regression only
- task: `044_writing_style_deep_research_chinese_replay`
- source identity: user-provided 2026-08-31 ChatGPT Deep Research PDF described in 044 `REQUEST.md`
- public evidence available in repo:
  - `automation/reviewed_handoff/tasks/044_writing_style_deep_research_chinese_replay/REQUEST.md`
  - `automation/reviewed_handoff/tasks/044_writing_style_deep_research_chinese_replay/PLAN.md`
  - `docs/plugin-todos/writing-style.md`
  - `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- private replay evidence referenced but not committed: production `writing-style` replay run `20260831T124239Z-b8734d927221`
- why included: 044 exposed the failure of instruction-only, phrase-scan, and protected-span accumulation for long Chinese scientific reports.
- why not unseen: it is already used as the known 044 stress/replay case.
- minimum gate if Planner uses it later: no critical semantic drift and no obvious residual English abstraction skeleton in reader-facing Chinese.

## 2. Positive architecture evidence: TRACE v8 -> v9

- role: positive architecture evidence only
- public evidence on current main: `8909eb1389dcc419d3168c13e1cddbcf252134cf` (`Add CAT-TRACE v8 audience and regression evidence`)
- why included: the useful pattern is audience -> page purpose -> meaning / role -> first-use context -> reader takeaway -> positive wording direction -> rewrite -> full-artifact language pass.
- why not a long-form holdout: it is slide/presentation evidence and belongs to TRACE, so it cannot prove Chinese scientific long-report maturity.

## 3. Unrelated should-not-fix controls

These controls should prevent a future scientific rewrite route from over-editing correct text.

### SNF-CN-TECH-001: Correct term-heavy Chinese technical prose

- source: `YuukiAS/AI_Research_Toolkit`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/AI_Research_Toolkit`
- commit: `b822dff09794766a1a013b100eb8f78a45514c7b`
- file: `R_RESEARCH_STACK.md`
- SHA256: `9aa06d5950715e3eb6b3d5d822b413b6f05620ddfddbf3bd8635d77c54c1a881`
- character count from checkout: `9738`
- reason: Chinese technical documentation with many formal R/Bioconductor/package terms, version constraints, analysis workflows, and reproducibility caveats.
- should-not-fix purpose: preserve correct formal terminology and caveats; do not translate package names, collapse version constraints, or over-naturalize a useful technical list.

### SNF-CN-SCI-002: Normal Chinese statistical product roadmap prose

- source: `YuukiAS/Asteria`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/Asteria`
- commit: `80ad881bc88ad1caf017959e320e539028eb5a25`
- file: `ROADMAP.md`
- SHA256: `01a6ebf49566fcec41739bc0469400d79654faceaf5b9c5912fa1468ca192535`
- character count from checkout: `19560`
- reason: Chinese long-form technical roadmap about statistical model notes, model lineage, evidence graphs, symbols, and view projections.
- should-not-fix purpose: avoid turning already readable scientific/product reasoning into casual prose; preserve technical relations such as entity/projection separation, semantic edge types, and model-variant distinctions.

## 4. Real unseen holdout candidates

The following are public, non-044, non-TRACE candidates. Planner may freeze these exact files or choose a bounded subset by line range before implementation, but must record the subset identity and hash before any rewrite run.

### HOLDOUT-UNSEEN-001: Asteria product roadmap

- source: `YuukiAS/Asteria`
- remote: `https://github.com/YuukiAS/Asteria.git`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/Asteria`
- commit: `80ad881bc88ad1caf017959e320e539028eb5a25`
- commit subject: `docs: add Asteria product roadmap`
- file: `ROADMAP.md`
- SHA256: `01a6ebf49566fcec41739bc0469400d79654faceaf5b9c5912fa1468ca192535`
- character count from checkout: `19560`
- relationship to 044/TRACE: unrelated public technical/statistical-product roadmap; not the Deep Research PDF and not TRACE slide material.
- suggested bounded unit for first experiment: one complete section, not an arbitrary token slice.
- evaluation role: real unseen Chinese technical/scientific long-form unit, plus should-not-overrewrite control.

### HOLDOUT-UNSEEN-002: AI Research Toolkit R research stack

- source: `YuukiAS/AI_Research_Toolkit`
- remote: `https://github.com/YuukiAS/AI_Research_Toolkit.git`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/AI_Research_Toolkit`
- commit: `b822dff09794766a1a013b100eb8f78a45514c7b`
- commit subject: `docs: add research software gap inventory`
- file: `R_RESEARCH_STACK.md`
- SHA256: `9aa06d5950715e3eb6b3d5d822b413b6f05620ddfddbf3bd8635d77c54c1a881`
- character count from checkout: `9738`
- relationship to 044/TRACE: unrelated public research-software technical documentation; not the Deep Research PDF and not TRACE slide material.
- suggested bounded unit for first experiment: a complete package/workflow section such as environment management, statistical modeling, or Bioconductor data structures.
- evaluation role: real unseen Chinese technical/scientific long-form unit, especially terminology-heavy should-not-fix behavior.

## 5. Candidate reviewed but not preferred as unseen

### CARE_Challenge

- source: `YuukiAS/CARE_Challenge`
- remote: `https://github.com/YuukiAS/CARE_Challenge.git`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/CARE_Challenge`
- commit: `75a40e454de43b64e59a0b0b438ff57ef2bb8345`
- commit subject: `plan: add CARE-ASE hierarchical pathology rescue blueprint`
- reason not preferred: public and rich in Chinese scientific material, but semantically close to the CARE/medical-segmentation context that appears in 044. It may be useful later as a domain stress case, but should not be the first non-044 unseen proof for 047.

## Version decision at intake

Repository bump decision: `NONE`

Reason: this intake commit creates reviewed-handoff planning artifacts and external-source evidence only. It does not change production behavior or create a release.

Affected plugins:

- `writing-style`: `NO_BUMP`
  - Reason: no implementation or production cutover has occurred.
- `presentations`: `NO_BUMP`
  - Reason: only used as TRACE evidence context; no presentations behavior is changed.
