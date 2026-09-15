---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: 055_clear_writing_release_convergence
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Implement the approved Clear Writing release convergence package so the formal
`writing-style` plugin can produce source-faithful, reader-facing Chinese or
Chinese-dominant scientific/technical rewrites from the normal plugin entry.

This control Plan is only a locator and execution summary. The authoritative
product contract is `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md`
v0.2 and `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.2,
approved by
`docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW_R2.md`.

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style` / Clear Writing

## Frozen decisions

Use the approved `PARTIAL_REDESIGN` only:

- keep `Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly ->
  fidelity/audit`;
- make Reader Plan the reader-disposition contract;
- preserve completion status, subject, tense, and epistemic state in
  `REALIZE_MEANING`;
- make assembly own whole-document finish;
- keep writing-fidelity as verifier, not prose generator;
- use mechanical helpers only for validation and receipts.

Do not reopen architecture, G1-G8, A/B/C reviewer taxonomy, paid review budget,
private handoff route, or recovery semantics.

## Positive completion

Overall task completion requires every condition in the canonical Goal:
G1-G6 on one exact final candidate, pre-final Critic review of the private
source/candidate/render, G7 fresh `3/3 PASS`, one final Terra or legal
adjudication, release CI, bounded production smoke with restore, final GPT
Reviewer PASS, user `ACCEPT`, and non-force integration to latest `main` with
the certified payload unchanged.

Partial local tests, generated parity, CI, a Critic PASS, or branch push alone
do not complete the task.

## Non-substitutable semantics

- Final release evidence must bind to the same `FINAL_CANDIDATE_COMMIT` and
  generated plugin payload hash.
- Fresh samples must be frozen only after pre-final Critic PASS and cannot be
  replaced or supplemented after product failure.
- Private source/candidate/render for pre-final Critic are user-upload only;
  Executor must not actively transmit private plaintext.
- Terra sees only the final allowed review packet, not private source,
  intermediates, logs, credentials, Meaning Map, or Reader Plan.

## Implementation scope

Expected source/generated areas:

- `skills/writing/core/scientific-rewrite/`
- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `scripts/codex_marketplace_config.json`
- `docs/plugin-changelogs/writing-style.md`
- root release metadata/changelog/README only when Phase 3 version closure is
  reached
- generated `plugins/codex/plugins/writing-style/**`
- focused tests and public evidence under `results/055_clear_writing_release_convergence/`

## Acceptance and regression gates

Follow the canonical phase order:

1. known implementation and known regression;
2. latest-main reconcile, version/changelog/generated payload/rubric closure,
   and candidate commit `C_n`;
3. G1-G6 representative replay from exact `C_n`;
4. public evidence plus repo-local private Critic bundle, then stop for user
   upload;
5. only after Critic PASS, designate `FINAL_CANDIDATE_COMMIT`;
6. freeze exactly 3 fresh public-safe sources;
7. run all three fresh items from the final candidate normal entry and require
   `3/3 PASS`;
8. final Terra, release CI, bounded production smoke/restore, final GPT
   Reviewer, user acceptance, and integration.

## Natural-language usage / routing expectations

Representative ordinary request:

```text
把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢。
```

The result should read as a standalone reader-facing scientific/technical
document, not as a source-processing note, workflow status, task plan, or audit
log.

## Out of scope

- Bridge Kit, Host Policy, execpolicy, new provider/account/credential path.
- New top-level plugin, runtime, daemon, queue, state machine, schema, or ledger.
- Research Authoring redesign or default fact-checking.
- Whole-branch 054 merge, sample-specific patching, adaptive fresh replacement,
  second Terra call, automatic successor, or destructive Git.
