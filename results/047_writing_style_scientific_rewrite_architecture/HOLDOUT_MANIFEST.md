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
- Positive rewrite-needed holdouts and should-not-fix controls must be disjoint units. The same frozen unit cannot serve both roles.
- Do not replace an item because the output is poor.
- Do not tune production code, prompts, example corpus, or deterministic checks on a positive unseen item and then reuse it as unseen.
- Do not commit private plaintext or private Text Review packets.
- For frozen public GitHub material, `repository + exact commit + path + git blob SHA + line range` is sufficient immutable identity. Executor may additionally record local SHA-256 before the first rewrite run, but may not change the selected range afterward.

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

These controls are intentionally disjoint from the positive rewrite-needed holdouts below. They should prevent a future scientific rewrite route from over-editing already useful text.

### SNF-CN-TECH-001: Correct term-heavy Chinese technical prose

- source: `YuukiAS/AI_Research_Toolkit`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/AI_Research_Toolkit`
- commit: `b822dff09794766a1a013b100eb8f78a45514c7b`
- file: `R_RESEARCH_STACK.md`
- git blob SHA: `d315fd6bbd5c08e271ecea95b3a05d451bce78c2`
- file SHA256: `9aa06d5950715e3eb6b3d5d822b413b6f05620ddfddbf3bd8635d77c54c1a881`
- frozen range: lines `1-13` inclusive at the exact commit above (`title` + scope/version paragraph + complete `使用原则` list; stop before `## 1. 环境与项目管理`)
- character count from checkout: `9738` for the full file; the frozen control is only the range above.
- reason: Chinese technical documentation with formal R/Bioconductor/package terms, version constraints, analysis workflows, and reproducibility caveats that is already easy to follow.
- should-not-fix purpose: preserve correct formal terminology and caveats; do not translate package names, collapse version constraints, or over-naturalize a useful technical list.
- role restriction: this frozen range is a should-not-fix / low-edit control only in 047. It must not also be counted as positive unseen rewrite-needed evidence or used as seed-example material.

### SNF-CN-SCI-002: Normal Chinese statistical product roadmap prose

- source: `YuukiAS/Asteria`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/Asteria`
- commit: `80ad881bc88ad1caf017959e320e539028eb5a25`
- file: `ROADMAP.md`
- git blob SHA: `1b5862a32e2ddbb6ad8e1805a4e785c158181de5`
- file SHA256: `01a6ebf49566fcec41739bc0469400d79654faceaf5b9c5912fa1468ca192535`
- frozen range: lines `5-17` inclusive at the exact commit above (complete `## 1. 重新定义 Asteria` section; stop before the separator / next section)
- character count from checkout: `19560` for the full file; the frozen control is only the range above.
- reason: already readable Chinese long-form technical reasoning about product scope, statistical-model lineage, evidence relationships and multiple views.
- should-not-fix purpose: avoid turning already readable scientific/product reasoning into casual prose; preserve the core entity/projection and research-evidence distinctions and keep Asteria as a proper product name.
- role restriction: this frozen range is a should-not-fix / low-edit control only in 047. It must not also be counted as positive unseen rewrite-needed evidence or used as seed-example material.

## 4. Positive rewrite-needed holdouts frozen before implementation

These units were frozen before any 047 production implementation. They are not allowed to become training/seed-example material during this task. If Executor or Planner tunes production behavior specifically against one of them, that unit loses unseen status and must not be replaced adaptively.

### HOLDOUT-UNSEEN-001: Bobbio research-workbench introduction/problem statement

- source: `YuukiAS/Bobbio`
- repository commit: `2d8a054bd34291dc061b8b64d5d841d458cc6296`
- file: `README.md`
- git blob SHA: `0152199c6c5f9b75978b06318bc9b0e6b93c4830`
- frozen range: lines `1-70` inclusive at the exact commit above
- relationship to 044/TRACE: different domain and artifact type; research-product/technical prose rather than CARE imaging or CAT-TRACE slides.
- why rewrite-needed: the unit is understandable but visibly relies on mixed English product/workflow labels such as `local-first`, `human-in-the-loop research knowledge workbench`, `Literature Radar`, `Paper Inbox`, `Interactive Reading + Agent Assistance`, `Human Curation`, `Selective Project Publishing`, `annotation`, `chat history`, and `coding/writing agent` to carry much of the reader-facing structure. A useful rewrite should explain the same product and workflow more naturally in Chinese while retaining proper names such as Zotero, Notion, Semantic Scholar, PubMed, arXiv, GPT and Codex where they are actual names.
- evaluation role: positive non-044 real technical holdout for natural Chinese / reader effort and term-preservation behavior.
- hard boundary: do not use the later output from this unit as a seed exemplar in the same 047 experiment.

### HOLDOUT-UNSEEN-002: Distributed imaging correction/stability opening

- source: `YuukiAS/Distributed_Imaging_Inference`
- repository commit: `0e895fdbce37c34967d8375059154df1d76397f4`
- file: `docs/SEGCOMM_CORRECTION_STABILITY_REPORT_2026-08-28.md`
- git blob SHA: `41c47f88042c7c877707546431df89674076e8f2`
- frozen range: lines `1-8` inclusive at the exact commit above (`title` + complete `30 秒版本` discourse unit; stop before `## 主表：跨 seed 平均`)
- relationship to 044/TRACE: non-044 and non-TRACE real scientific report text. It shares the broad CARE/federated-imaging domain with 044, so it is useful scientific evidence but not strong cross-domain generalization by itself.
- why rewrite-needed: the unit has concrete scientific content but mixes ordinary reader-facing Chinese with English workflow/model shorthand such as `correction + stability`, `whole-myocardium`, `client`, `optimizer state`, `checkpoint`, `decoder pooled`, `full-model pooled`, `seed`, `one-shot gap`, and `few-round`. The task is to preserve the exact experimental facts and distinctions while making the prose read as natural Chinese scientific reporting rather than an internal experiment log.
- evaluation role: positive real scientific holdout for meaning-first rewriting, semantic fidelity, uncertainty preservation, and formal-term discrimination.
- hard boundary: because its scientific domain partially overlaps 044, 047 must not claim broad production maturity from this item plus 044 alone.

## 5. Candidate reviewed but not used as first positive proof

### CARE_Challenge

- source: `YuukiAS/CARE_Challenge`
- remote: `https://github.com/YuukiAS/CARE_Challenge.git`
- local public checkout: `/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/holdout-sources/CARE_Challenge`
- commit: `75a40e454de43b64e59a0b0b438ff57ef2bb8345`
- commit subject: `plan: add CARE-ASE hierarchical pathology rescue blueprint`
- reason not preferred: public and rich in Chinese scientific material, but semantically close to the CARE/medical-segmentation context that appears in 044. It may be useful later as a domain stress case, but should not be promoted into the first positive unseen proof after implementation starts.

## Interpretation boundary for 047

The frozen set now has disjoint roles:

- 044: known regression only;
- TRACE v8 -> v9: architecture evidence only;
- Asteria lines 5-17 + AI Research Toolkit lines 1-13: should-not-fix / low-edit controls only;
- Bobbio lines 1-70: positive cross-domain technical rewrite-needed holdout;
- Distributed Imaging lines 1-8: positive scientific rewrite-needed holdout, with explicit domain-overlap caveat.

This is enough to run a bounded architecture experiment. It is not, by itself, enough to claim that 20-50 page Chinese scientific long-form rewriting is production-mature. Planner/Reviewer must distinguish an experimental architecture PASS from a production release decision.

## Version decision at intake

Repository bump decision: `NONE`

Reason: this intake update only clarifies evaluation identity and disjoint holdout roles. It does not change production behavior or create a release.

Affected plugins:

- `writing-style`: `NO_BUMP`
  - Reason: no implementation or production cutover has occurred.
- `presentations`: `NO_BUMP`
  - Reason: only used as TRACE evidence context; no presentations behavior is changed.
