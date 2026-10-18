# Planner Handoff — PDF 5.4.5 Release Isolation R0

继续当前 AI Research Stack Planner 线程，只处理 standalone `render-chinese-math-pdf` 的 PDF-only 5.4.5 formal release isolation。

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone `render-chinese-math-pdf`
- design_topic_or_task_key: `documents-media--pdf-save-as-delivery`
- source / task branch: `reviewed/documents-media--pdf-save-as-delivery`
- task worktree: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery`
- review_stage: `FORMAL_RELEASE_ISOLATION_REVIEW_R0`
- reviewed package commit: `5b71d8ccec98fe29111d9e1c59170a5f5f459a74`
- Critic review:
  `results/documents-media--pdf-save-as-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_CRITIC_REVIEW_R0_2026-10-17.md`
- Critic review commit: `ddb977e4be7179ebcfc87d2915991a4aae8d5fec`
- verdict: `REVISE`
- stable blocker: `PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE`

## Critic disposition

Critic accepts the existing 5.4.5 isolation architecture:

- repository `5.4.4 -> 5.4.5` PATCH;
- `render-chinese-math-pdf 0.2 -> 0.3`;
- central plugins NO_BUMP;
- release candidate starts from exact formal `origin/release`, not current `main`;
- explicit allowlist;
- accepted PDF product bytes frozen by exact blob identity;
- isolated full green validation / GitHub CI / install+upgrade smoke;
- existing `ai-skills-repository-maintainer` fast-forward-only producer;
- after release, ordinary integration into then-latest main while preserving unrelated PIE / Research Authoring / Presentations work;
- Issue #101 / Project DONE only after release + main readback.

Do not redesign any of those parts.

## Required response to blocker

Respond to `PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE` with `ACCEPT`, `PARTIAL_ACCEPT`, or `REBUT`.

The minimum accepted change is one release-delivery smoke only. Do not reopen D1/D2/D3 and do not create REVIEW_3.

If ACCEPT, revise the Proposal/Plan + Goal + Kickoff as one complete new package version so that, after the exact 5.4.5 / PDF 0.3 candidate passes fresh-install/upgrade identity checks, the Executor must:

1. use the installed exact release candidate with a public-safe minimal bilingual/math input and the normal PDF production route;
2. render and QA one test PDF;
3. bind the test PDF identity by path/size/hash only as auxiliary evidence;
4. preserve that test PDF until the user-visible completion response;
5. require the release Goal's **first user-visible completion response** to lead with a real host file entry for that exact QA-passed PDF;
6. treat a server path, hash, receipt, preview, or prose saying where the file is as FAIL;
7. require no second user prompt such as “PDF 呢”;
8. use the already-confirmed host-local file-entry mechanism; do not require the user to click/confirm again;
9. block `release` advancement and #101 closure if this smoke has not passed;
10. if product blob identity remains unchanged, do not rerun D2/D3 or reopen product review; only if fixing the smoke would change PDF production bytes should execution return to Planner/Critic for a new product amendment.

The smoke must be explicitly included in the release gates / Positive Completion and reflected faithfully in the Kickoff authorization. It must not add Research Authoring, Presentations, PIE, Bridge Kit, paid calls, external upload, a new reviewer, or another workflow.

Keep the already approved exact branch/worktree and 5.4.5 release-isolation topology unless the new smoke requires a purely task-local artifact path.

After revising:

- commit/push the complete new Proposal/Plan + Goal + Kickoff on the same task branch;
- do not execute the release;
- preserve the prior R0 review;
- automatically output the next complete Critic prompt per Planner Role Contract, asking only whether `PDF-REL-B1` is closed and whether the smoke introduces any new release/scope risk.

Do not ask the user to decide technical details.
