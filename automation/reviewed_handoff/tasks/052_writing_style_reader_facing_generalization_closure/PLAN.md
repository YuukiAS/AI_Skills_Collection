---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: 052_writing_style_reader_facing_generalization_closure
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Close the two residual 051 reader-facing failures for `writing-style` without
rewriting 051 history or broadening the infrastructure: source-process framing
inside standalone candidate prose, and workflow-wrapper leakage in Text Review
packets.

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

## Frozen decisions

Use `origin/main` as the baseline and selectively port only the still-valid
production `writing-style` heavy rewrite payload from
`2690de2cbc3d4ffb0741ecb80297a569647051f2`.

051 remains historical evidence only:

```text
STOPPED / NOT_RELEASED / FINAL_TEXT_REVIEW_REVISE
```

Do not copy 051 task state, result files, private artifacts, paid-review
ledgers, or final-report status. Do not restart or consume 051 review/holdout
budget.

Do not build new replay/runtime/Bridge/Host Policy mechanisms. Existing main
governance and Bridge Kit 0.7.4 consumer pin remain authoritative.

## Positive completion

052 is complete only when the real `writing-style` production candidate:

- rejects or repairs source-process framing in standalone scientific/technical
  rewrite candidates while preserving legitimate author/literature attribution;
- keeps Text Review plaintext candidate-only, with workflow identities in
  manifest/metadata only;
- passes Bloom as `KNOWN_REGRESSION`, two frozen fresh public-safe holdouts,
  unrelated regressions, exactly one Terra Text Review, full/release CI, real
  production identity install/upgrade smoke, GPT Reviewer, final user ACCEPT,
  and integration back to latest `main`.

Maximum claim scope: success proves this bounded reader-facing closure for the
current heavy Chinese rewrite route; it does not prove universal writing
quality, a plugin rename, or cross-plugin consumer integration.

## Non-substitutable semantics

- `SOURCE_PROCESS_FRAME` is semantic framing, not a simple phrase blacklist.
  Standalone candidates should state technical content directly. Legitimate
  attribution such as "Smith et al. [12] reported ..." remains allowed.
- `REVIEW_PACKET_CONSTRUCTION` is transport hygiene. If a reviewer finding only
  hits wrapper labels absent from candidate bytes, the defect is packet
  construction, not writing-style product quality.
- Fresh holdouts must be frozen as an exact 2-item complete batch before
  generation. One failure fails the whole batch; no third replacement is
  allowed.
- Paid review is exactly one final candidate-only Text Review after local and
  holdout gates pass.

## Implementation scope

- `skills/writing/core/scientific-rewrite/`
- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `scripts/codex_marketplace_config.json`
- generated `plugins/codex/plugins/writing-style/**`
- focused tests for scientific rewrite and Reviewed Handoff Text Review packet
  construction
- minimal `AGENTS.md` bootstrap ergonomics note requested by the user

## Acceptance and regression gates

Run in order:

1. focused tests;
2. Bloom known regression;
3. unrelated light Chinese polish;
4. fidelity-only regression;
5. English scientific-prose regression;
6. frozen fresh holdout 1;
7. frozen fresh holdout 2;
8. one final Terra Text Review on Bloom + holdout 1 + holdout 2 candidate text
   with natural document titles and no wrapper labels;
9. full/release CI;
10. production install/upgrade smoke;
11. GPT Reviewer;
12. final user ACCEPT;
13. integration to latest `main`.

## Natural-language usage / routing expectations

A normal user can ask:

```text
把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢。
```

The final candidate should discuss the scientific or technical content itself,
not say that "原文指出" or "根据给定材料" unless the user requested comparison or
review commentary.

## Out of scope

- Renaming `writing-style`.
- New replay/runtime/Bridge/Host Policy mechanisms.
- Extra paid-review calls or automatic paid retry.
- Reopening 051 or changing 051 final state.
- Adaptive holdout replacement.
- Creating a phrase blacklist as the primary product fix.
