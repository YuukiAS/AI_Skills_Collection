# PDF 首次交付 — CI 基线恢复独立 Critic 提示词 v0.1

你是 AI Research Stack 的独立 Critic。本轮不是重新审查 PDF 产品方向，而是审查实施后暴露出的一个**CI 基线恢复**问题。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone `render-chinese-math-pdf`
- design_topic_or_task_key: `documents-media--pdf-save-as-delivery`
- review_stage: `RECOVERY_ACCEPTANCE_REVIEW`
- task_branch: `reviewed/documents-media--pdf-save-as-delivery`
- task_worktree: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery`
- original execution-ready package: `da6063bedb8db4779347fc08f9ae1875da2dd115`
- task-local frozen Plan: `automation/reviewed_handoff/tasks/documents-media--pdf-save-as-delivery/PLAN.md`
- implementation commit: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- current branch product/evidence tip before recovery routing: `eb1c788e5cce9ef3e42c7710bd61a399a789913f`
- REVIEW_1: `results/documents-media--pdf-save-as-delivery/REVIEW_1.md`
- recovery proposal: `results/documents-media--pdf-save-as-delivery/PLANNER_CI_BASELINE_RECOVERY_PROPOSAL_V0_1.md`
- recovery package commit: `1480b6c8da3aff96707a7f898f19981ce0b2f304`
- current main at Planner diagnosis: `362a8cab6991120a79600352d070926e2602dcbd`
- failed GitHub Actions run: `38706208966`
- tracking issue: `#101`

## First read

Read latest `main` versions of:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

Then read from the exact task branch:

- REQUEST / PLAN / CURRENT
- RESULT
- REVIEW_1
- D1 delivery event
- Planner CI baseline recovery proposal

Independently inspect GitHub Actions run `38706208966` and the current `main` baseline. In particular verify the Planner claim that the four failing full-suite tests are pre-existing repository-wide drift outside the PDF task, and that current main still has no integrated legal repair.

Do not rely only on Planner wording. The repository currently contains:
`results/project-instructions-editor--standalone-skill-implementation/SURFACE_CONSOLIDATION_REPAIR_RESULT.md`,
which historically records the same four failures; independently determine whether that evidence still applies to current main.

## What is already closed

Do not reopen D1–D3 unless the new recovery would weaken them.

The later branch event at `eb1c788e...` records the actual first-completion PDF delivery that REVIEW_1 originally said was missing. Verify it, but the recovery question is now CI semantics.

Do not ask this task to repair unrelated Presentation / Research Authoring / publication-layer debt merely to obtain a green repository if that would violate frozen scope.

## Recovery question

The current frozen Plan requires all-green required GitHub CI. That is impossible to satisfy inside the frozen scope while current main itself carries the same unrelated failures.

Planner proposes one bounded revision:

- after Critic PASS only, consume the task's sole `plan_revision: 0 -> 1`;
- set Reviewed Handoff routing to `ci_required=false`, `ci_status=NOT_REQUIRED`;
- replace the impossible all-green gate with a **broad differential regression gate** comparing the exact final candidate against then-current main under the same full-suite/publication checks;
- candidate may proceed only if target tests pass and it introduces no new full-suite failures or generated/publication differences relative to main;
- preserve run `38706208966` as truthful failed-CI evidence, not as PASS;
- require a durable `CI_BASELINE_DIFFERENTIAL.md`;
- send the same final candidate to REVIEW_2;
- do not create a successor, repair unrelated owners, add a third review, alter PDF D1–D3, or change privacy/version/product scope.

## Critic questions

1. Is the current all-green gate a real product/release safety requirement that must remain blocking even when current main is already red, or is it an over-broad gate that makes a bounded task responsible for unrelated repository debt?
2. Does the proposed main-vs-candidate differential still provide broad enough regression evidence, especially because this task touched version/README/registry/catalog release surfaces?
3. Can the differential be gamed by merely matching a broken baseline? If so, specify the smallest extra evidence needed without forcing unrelated repair.
4. Is changing `ci_required=true -> false` semantically correct for Reviewed Handoff when full-suite differential evidence remains a frozen product gate rather than workflow-controlled CI?
5. Should integration/release remain separately gated if current main is still red? If yes, state the exact boundary: product/reviewer PASS vs merge/release closure, without reopening PDF implementation.
6. Confirm review-budget handling: REVIEW_1 remains history; no REVIEW_2 is consumed until recovery is approved and executed; no third review.

## Required verdict

Return exactly one:

`CRITIC_VERDICT=PASS`

or

`CRITIC_VERDICT=REVISE`

If REVISE, each blocker must contain:
- frozen requirement;
- direct evidence;
- causal risk;
- minimum closure condition.

Do not add unrelated architecture improvements.

If PASS, clearly state what the single Planner revision may change, what must remain unchanged, and whether Codex may then execute only the differential evidence/review closure without further product changes.

Because this is a recovery review after an earlier REVISE, explain in user-readable Chinese how the old CI blocker is resolved or preserved before machine-style fields. Then provide the next-role Planner prompt required by the Critic contract.
