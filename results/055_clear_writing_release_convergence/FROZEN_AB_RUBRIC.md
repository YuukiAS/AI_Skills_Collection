# 055 Clear Writing Frozen A/B/C Rubric

This rubric is frozen for the `055_clear_writing_release_convergence` candidate
closure. It summarizes the authoritative reviewer contract from
`docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.2 and does not
change the approved Goal, Plan, budget, transport, or recovery semantics.

## A — Source Fidelity

Hard blocker. The reviewer must inspect source and full candidate.

Check:

- claims, evidence, polarity, quantifiers, comparators, conditions, caveats,
  uncertainty, citations, attribution, and conclusion strength;
- formula, table, code, command, path, config, API, model, metric, dataset, and
  identifier preservation according to source role;
- Reader Plan disposition consistency: preserved, summarized, relocated, or
  omitted content must match the source obligation and reader-facing role.

Fail when the candidate omits source-required content, invents unsupported
claims, strengthens or weakens beyond source authority, changes attribution,
damages citations, or loses required structured technical content.

External-world truth is not a Clear Writing blocker by itself. It becomes an A
failure only when the candidate adds, strengthens, or wrongly attributes a fact
relative to the source.

## B — Reader-Facing Quality

Hard blocker. The reviewer reads the complete candidate and any required render.

Check:

- standalone reader-facing Chinese or Chinese-dominant prose;
- natural Chinese voice without English abstraction scaffolding;
- no internal workflow, audit, task, branch, CI, cache, candidate, or execution
  status leakage in ordinary reader-facing prose;
- source-author future work, limitations, proposals, and uncertainty preserve
  subject, completion state, temporal status, and epistemic status;
- legitimate code, path, config, API, citation, formula, table, and
  reproducibility details are placed where they help the reader instead of being
  blanket-deleted or allowed to dominate the main prose;
- long-document structure, section order, transitions, definitions, repeated
  concepts, and technical-detail placement read as a finished artifact.

Fail when the candidate reads like a project memo, execution plan, source
processing note, audit log, or local bundle stitching, even if local mechanical
receipts pass.

## C — External Factual Truth

Default non-blocking advisory for this task. The reviewer may record external
truth concerns, but `055` does not authorize automatic fact-checking or source
substitution.

Escalate C to A only when the candidate itself introduces, strengthens, or
misattributes the problem relative to the provided source.

## Finding Requirements

Every blocker must identify:

- `A`, `B`, or escalated `C`;
- the frozen gate or requirement violated;
- the candidate location;
- for A findings, the corresponding source location;
- the reason the finding violates the frozen rubric;
- initial attribution:
  `PLUGIN_DEFECT`, `SOURCE_DEFECT`, `REVIEWER_RUBRIC_DEFECT`,
  `ENVIRONMENT_DEFECT`, `WORKFLOW_DEFECT`, or `CONTRACT_AMBIGUITY`;
- the smallest condition required to close the finding.

Observations that cannot be tied to the frozen requirement are advisory.

## Sequence Guard

This rubric is part of candidate closure before pre-final Critic review. If
production source, generated payload, plugin/repository version identity, this
rubric, or the reviewed representative artifact changes after pre-final Critic
PASS, that PASS is invalidated and the task must return to candidate closure.
