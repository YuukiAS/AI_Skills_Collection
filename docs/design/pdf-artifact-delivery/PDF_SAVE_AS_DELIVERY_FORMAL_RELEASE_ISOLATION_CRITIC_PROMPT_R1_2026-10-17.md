# PDF Save-as Delivery — Formal Release Isolation Critic Prompt R1

你是 AI Research Stack 的独立 Critic。本轮只复核上一轮唯一 blocker：

`PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE`

不要重新审查已经在 R0 明确通过的 5.4.5 release-isolation 架构、版本选择、release-line ancestry、allowlist、accepted PDF byte identity、全绿 isolated release validation、fast-forward-only producer、main reintegration、maintenance closure 或 PDF 产品方向。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone `render-chinese-math-pdf`
- task_key: `documents-media--pdf-save-as-delivery`
- review_stage: `FORMAL_RELEASE_ISOLATION_REVIEW_R1`
- task_branch: `reviewed/documents-media--pdf-save-as-delivery`
- accepted PDF implementation: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- implementation review: `REVIEW_2 = PASS`
- prior execution package commit: `5b71d8ccec98fe29111d9e1c59170a5f5f459a74`
- prior Critic review:
  `results/documents-media--pdf-save-as-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_CRITIC_REVIEW_R0_2026-10-17.md`
- prior Critic review commit: `ddb977e4be7179ebcfc87d2915991a4aae8d5fec`
- prior verdict: `REVISE`
- sole blocker: `PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE`
- revised execution package commit: `75804e2eda36870b079e43f8ccd6271e205bf631`

Branch history between the old and new package also contains the R0 Critic prompt/review/handoff and a control `CURRENT.next_action` update. Those are review/control artifacts, not execution-package semantic changes. The execution-package semantic revision is limited to the three files below.

## Revised review object

Read the complete revised files at exact commit `75804e2e...`:

1. Proposal / Plan  
   `docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_PROPOSAL_PLAN_V0_1_2026-10-17.md`

2. Canonical Goal  
   `docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_GOAL_V0_1.md`

3. Kickoff Draft  
   `docs/operations/prompts/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_KICKOFF_V0_1.md`

Also read the full R0 Critic review at commit `ddb977e4...`.

Compare each of these three package files against the old package at `5b71d8c...` and confirm that the only substantive change is the release-delivery smoke needed to close `PDF-REL-B1`.

Do not require a new versioned Proposal/Goal/Kickoff file merely because this is R1; the user explicitly requested the same package version with one minimal blocker-closing revision, uniquely bound by the new package commit.

## What R0 already PASSed and must remain closed

Unless the new smoke text directly regresses one of these boundaries, do not reopen:

- repository release `5.4.4 -> 5.4.5` = PATCH;
- `render-chinese-math-pdf 0.2 -> 0.3`;
- central plugins = NO_BUMP;
- release candidate starts from exact formal `origin/release`, not current main;
- no PIE / Research Authoring / Presentations production bytes enter 5.4.5;
- accepted PDF production blob identities remain frozen;
- product bytes unchanged => no D1/D2/D3 rerun;
- isolated candidate must pass full deterministic release validation + exact-SHA GitHub CI;
- fresh install + 5.4.4 -> 5.4.5 upgrade identity smoke;
- fast-forward-only / non-force formal producer;
- formal 5.4.5 then integrates back into latest main without losing unrelated work;
- Issue #101 remains open until truthful release/main closure;
- no REVIEW_3, successor PDF task, paid call, external upload, Bridge modification, or unrelated product review.

## Only blocker to re-evaluate

### PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE

Determine whether the revised package now freezes all of the following:

1. **Exact installed identity first**
   - smoke runs only after the exact 5.4.5 / PDF 0.3 release candidate has completed fresh-install / upgrade identity verification.

2. **Normal production route**
   - one public-safe minimal mixed Chinese/English + math input;
   - invoke the installed candidate's normal PDF production route;
   - a helper-only/script-only bypass cannot PASS.

3. **Real renderer + QA**
   - renderer and existing PDF QA must PASS;
   - no lower-quality substitute or alternate renderer.

4. **Artifact identity vs delivery evidence**
   - smoke PDF is persisted in a task-owned local/private export location and is not committed/publicly uploaded;
   - path / byte size / SHA-256 bind identity only;
   - path/hash/receipt/preview/queued/prose location statement cannot count as user delivery.

5. **First completion reply**
   - the installed-candidate smoke's first completion response begins with the real host file entry for that exact QA-passed PDF;
   - no second user “PDF 呢” request is needed;
   - file entry resolves to the same PDF identity.

6. **Pre-release gate**
   - `release` cannot move and Issue #101 cannot close before this smoke PASS.

7. **Overall Goal final reply**
   - the same smoke PDF is preserved through release/main closure;
   - the overall Goal's final first user-visible completion response also begins with the real host file entry for that same PDF, before the release summary.

8. **Failure routing**
   - if frozen PDF product blobs still match REVIEW_2, a smoke failure is first treated as release/install/load/normal-entry/delivery wiring failure and only this smoke is rerun;
   - no D2/D3 rerun and no REVIEW_3;
   - if fixing the smoke requires changing accepted PDF production bytes, execution stops and returns to Planner/Critic before release.

9. **No scope expansion**
   - no Research Authoring / Presentations / PIE / Bridge change;
   - no new upload service, reviewer, workflow, paid model/API, or private transfer.

## Anti-proxy check

Reject if the revised package could still PASS using any of these weaker substitutes:

- “installed SKILL.md hash matches” without a normal-entry completion;
- generated PDF exists on disk;
- server path shown in prose;
- receipt/hash/preview;
- file entry appears only after a second user request;
- file entry points to a different PDF from the QA-passed smoke artifact;
- a direct renderer/helper test bypasses the installed candidate's normal route;
- release moves before the smoke is actually observed.

## Required verdict

Return exactly one:

`CRITIC_VERDICT=PASS`

or

`CRITIC_VERDICT=REVISE`

If REVISE, only keep/add a blocker if the revised text still fails the original `PDF-REL-B1` requirement or if the smoke amendment itself introduces a direct new release-safety regression. Do not reopen unrelated R0 PASS findings.

For any REVISE blocker, include:

- requirement;
- direct evidence;
- causal risk;
- minimum closure condition.

If PASS, explicitly state:

```text
PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE=CLOSED
PRODUCT_REVIEW_REOPENED=NO
D1_D2_D3_RERUN_REQUIRED=NO
REVIEW_3_REQUIRED=NO
RELEASE_ISOLATION_ARCHITECTURE_CHANGED=NO
READY_FOR_CODEX=YES
```

Then provide:

```text
APPROVED_PROPOSAL_PATH=docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_PROPOSAL_PLAN_V0_1_2026-10-17.md
APPROVED_GOAL_PATH=docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_GOAL_V0_1.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_KICKOFF_V0_1.md
APPROVED_COMMIT=75804e2eda36870b079e43f8ccd6271e205bf631
```

Because this is execution-ready review, reproduce the **revised Kickoff body verbatim** from the approved file as required by the Critic contract. Do not write a newly improvised Codex prompt.

No additional Planner/Critic round is needed after PASS unless actual execution would change accepted PDF product bytes, release-isolation semantics, version intent, privacy/authorization, or formal producer behavior.
