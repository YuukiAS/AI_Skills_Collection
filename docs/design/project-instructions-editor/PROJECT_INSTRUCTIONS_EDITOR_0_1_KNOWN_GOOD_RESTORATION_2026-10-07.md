# Project Instructions Editor 0.1 — Known-Good Restoration

Date: 2026-10-07

Status: bounded restoration; no new Critic round

Branch:

```text
work/project-instructions-editor--0.1-closure
```

## Decision

Stop inventing new prompt architecture.

A real earlier Server+VPS replacement was already judged materially better by
the user. Restore that behavior as the positive baseline, then selectively port
only later fixes that protect semantics without changing the successful editing
style.

This is a restoration task, not another design round.

## Positive behavior baseline

The user-confirmed good Server+VPS version organized the durable setting around
these user-meaningful families:

1. 权威归属
2. 面向用户的回答
3. 代理客户端与交付
4. 客户端实时网络状态与用户操作
5. 自动验证优先
6. 权威来源与生产修改
7. 保守判定与冗余
8. 完整性与敏感信息
9. 生产任务结束时

These names are a regression reference for the real Server+VPS case, not a
generic production template.

The important behavior was:

- ordinary response rules were consolidated instead of split across multiple
  audit-style sections;
- proxy delivery integrity and server-first behavior lived together;
- live client-network mutation and user-action requirements lived together;
- canonical source plus production mutation rules lived together;
- fail-closed and redundancy were expressed once;
- completeness and secrets were expressed once;
- production closure remained a distinct trigger;
- ordinary Chinese was natural and source labels were digested;
- volatile client/device inventory was not treated as durable Project truth;
- the result read like Project instructions, not an internal audit contract.

Historical C6 commit `6ddab9029bbd96a21d7e5bf0317f7674c66cd909`
is additional implementation evidence for this behavior: compact output,
volatile inventory -> source bridge, broad current authorization/privacy/evidence
preserved, false no-op avoided. C6 itself is not restored wholesale.

## What to restore

Restore the simpler candidate-construction behavior:

```text
live setting + current request + necessary current source facts
-> identify durable user-facing rule groups
-> consolidate duplicates
-> move volatile detail behind stable source bridge
-> preserve current semantic force
-> emit clean replacement
```

Do not require internal semantic tables, K1-K7 labels, a closed-world table, or
a multi-stage pseudo-pipeline in the production Skill.

The production Skill should prefer a small number of strong editor principles
over a long algorithmic runtime protocol.

## What later fixes must remain

Selectively retain only proven non-regressing fixes:

- live setting is the preservation baseline;
- protected absence: old/deleted/rejected historical-only rules do not return;
- no-op cannot hide a material safely repairable in-scope defect;
- volatile source-owned inventory becomes a short current-source bridge;
- exact machine/formal identifiers remain exact;
- authorization, privacy, safety, evidence strength, uncertainty, completion
  claims and mandatory/optional force are preserved;
- ordinary user output does not print internal mode labels;
- missing baseline/source/authority degrades honestly;
- C11 advanced/cross-turn reader-layer guarantee remains unsupported;
- ordinary Chinese in the current edited setting is desirable, but no token
  scan/blacklist/ratio/finalizer is used.

## What to remove

Remove the recent prompt machinery that did not improve the real Web result and
made the Skill harder to follow:

- K1-K7 runtime-kernel framing;
- Allowed Durable Meaning Set as an explicit production algorithm;
- bidirectional provenance machinery as an explicit runtime protocol;
- semantic mutation radius / surface reconstruction radius terminology;
- pseudo-formal normalization field lists;
- other duplicated wording introduced only to force the two failed recent
  attempts.

Keep the underlying useful semantics in plain editor rules where needed.

Do not restore C7-C11 token-oriented language machinery.

## Restoration rule for the real Server+VPS regression

For the real Server+VPS acceptance, use the earlier user-confirmed good version
as a positive fixture.

A new candidate should be considered structurally regressed if it:

- splits “面向用户的回答” back into multiple overlapping normal-response sections;
- separates proxy production-integrity and server-first behavior without a real
  trigger distinction;
- keeps current device/platform member lists when the canonical repository owns
  the current supported set;
- duplicates canonical-source lookup rules across several sections;
- repeats ordinary closure-report behavior in normal-response sections;
- introduces new durable security/2FA/best-practice examples that were not in the
  live setting/current request/current required source sync;
- returns to 12/13 source-shaped sections merely because the live setting has
  them.

For this specific regression, the earlier nine-family shape is an allowed
positive reference. Do not turn “nine sections” into a generic rule for other
Projects.

## Implementation strategy

Use Git history, not another additive patch.

Executor should compare:

- C6 source and C6 Server+VPS artifact;
- current production source;
- later protected-absence/no-op/output-label fixes;
- the latest two real Web failures.

Then construct a smaller production Skill by starting from the last simpler
editor core that produced compact output and selectively porting the later
non-regressing fixes.

Do not start from current `8eebd7fb...` and append another rule set.

The expected result is a materially smaller and simpler production runtime than
the current kernel version.

## Tests

Keep generic contract tests for:

- live baseline;
- protected absence;
- no-op eligibility;
- locator/source bridge;
- exact identifiers;
- authorization/privacy/evidence preservation;
- missing-input degradation.

Add one real-regression positive fixture for Server+VPS that captures the
earlier good nine-family organization as qualitative reference.

The fixture may be domain-specific because it is a real regression fixture.
Production logic must remain generic.

Do not test exact wording, English counts, or fixed nine-section output for
generic projects.

## Wrapper

Standalone Skill stays `0.1`.

Current live wrapper is `0.2.5`.

After restoration, build `0.2.6` candidate. Do not update live wrapper until
repository validation passes.

## Acceptance

After repository-side restoration and wrapper update, run one fresh Server+VPS
normal-entry acceptance.

Compare directly against:

1. the earlier user-confirmed good version;
2. the two recent failed source-shaped versions.

PASS requires the result to be at least as compact/coherent as the good version
while preserving the later semantic safety fixes.

This restoration supersedes the prior “stop and scope-down” conclusion.
