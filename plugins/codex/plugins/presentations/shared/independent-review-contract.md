# Independent Review Contract

Before applying this contract, read in order:

1. `presentation-end-to-end-pre-execution-runbook.md`
2. `pre-execution-cumulative-acceptance-contract.md`
3. `rendered-artifact-positive-ancestry-acceptance-contract.md`

This contract separates four review jobs that must not be conflated:

1. **prebuild specification Critic** — judges whether Planner authority is ready;
2. **fresh deterministic Auditor** — judges exact source/candidate conformance;
3. **fresh rendered-artifact Auditor** — judges every required page image and render-dependent guard;
4. **GPT Work final gate** — judges aesthetics, reader effort, pedagogy, and whole-deck communication.

A PASS from one layer cannot substitute for another.

---

## 1. Prebuild specification Critic

Required for failed-version recovery, major revision, and substantial high-risk new decks.

It reviews:

- exact source/history consumption;
- page count and sequence;
- every page job and required/forbidden object;
- content correctness and audience sufficiency;
- audience versus speaker/instructor boundary;
- visible-copy completeness;
- layout/archetype suitability;
- positive/negative visual ancestry completeness;
- historical-regression protection;
- the proposed autonomous Controller and review loop.

It returns:

- `PASS`;
- `REVISE` with bounded Planner amendments;
- or `BLOCKED_HISTORY_NOT_CONSUMED` / source-equivalent block.

A prebuild Critic PASS means only that the specification is coherent enough to produce. It never certifies the future render.

---

## 2. Executor trust separation

The agent/process that edits a candidate is the Producer/executor.

It may build, render, run smoke tests, and prepare evidence. It may not authoritatively accept its own candidate.

Its strongest state is:

```text
READY_FOR_INDEPENDENT_VALIDATION = YES
```

Do not report final PASS, release readiness, or human acceptance from Producer self-review.

---

## 3. Fresh deterministic Auditor

Run only after the Producer stops writing the exact candidate.

Preferred transport:

1. fresh CI/fresh process on a clean checkout;
2. fresh read-only subagent with isolated context;
3. same executor process only for debugging, never authoritative acceptance.

The Auditor must:

- bind to exact repository, source commit, artifact hashes, and authority hashes;
- use a pre-existing version-pinned validator runtime;
- treat Planner/user authority as read-only;
- have no permission to edit candidate, fixtures, gates, or thresholds;
- receive no executor scratchpad or self-acceptance narrative;
- verify exact copy, PageIDs, count/order, locks, allowlist, history coverage, required objects, positive visual object preservation, code execution, numerical results, figure labels, PDF/PPTX structure, and artifact identity;
- persist machine-readable evidence.

If a validator defect is found, repair/version the validator separately before rerunning the frozen candidate.

---

## 4. Fresh rendered-artifact Auditor

This is a distinct review stage. It cannot be replaced by source review, extracted text, or representative-page inspection.

The Auditor receives:

- exact PDF/PPTX hash;
- exact page PNG hashes;
- full contact sheet;
- PageIDs;
- frozen copy/layout/component/positive-ancestry authority;
- active historical guards;
- render-pending closure matrix template;
- relevant source anchors.

For major/full-deck work it must:

- inspect every page at whole-slide scale;
- inspect the full contact sheet;
- create one persisted row per page;
- create one persisted row per render-dependent historical item;
- verify primary-object scale, typography, whitespace, reading path, evidence proximity, Q/A geometry, component consistency, and whole-deck rhythm;
- verify protected diagrams/figures/tables/code-output relationships were not silently deleted;
- validate suspicious charts/traces/diagnostic plots against underlying quantities and nearby numerical summaries;
- bind findings to the exact candidate and page-image hashes.

A claimed full-deck PASS is invalid when:

- any page lacks a review row;
- any mandatory `RENDER_PENDING` item lacks an exact-render verdict;
- a protected visual object disappears without retirement authority;
- review evidence is bound to another candidate;
- P0/P1/P2 findings remain open.

---

## 5. Subagent independence

A subagent counts as independent only if:

- it starts with fresh context;
- its inputs are artifact/commit-bound;
- candidate and authority are read-only;
- it receives no expected human-rejection answer key;
- it cannot edit tests, detector code, gates, or thresholds;
- it has no access to Producer scratchpad/chain-of-thought;
- its output is persisted with exact artifact identity.

Otherwise its review is advisory only.

---

## 6. GPT Work final gate

GPT Work runs after deterministic and rendered review have closed routine defects.

### Major/new/recovery candidate

Review:

- every page;
- full contact sheet;
- high-risk pages at high resolution;
- cumulative visual/pedagogical guards;
- positive visual ancestry;
- whole-deck rhythm and density;
- audience reader effort;
- natural language;
- semantic proximity;
- whether pages feel complete rather than merely populated.

### Minor bounded revision

May review changed pages, affected consumers, minimum context, and full contact sheet only when page count, section order, shell, page jobs, and archetypes remain locked. Final release still requires a whole-deck regression.

GPT Work:

- does not implement fixes;
- does not change scientific/statistical meaning;
- does not override deterministic or numerical failures;
- returns PASS or REVISE with page/component-scoped findings;
- on REVISE, routes findings through a fresh Producer, fresh deterministic review, fresh rendered review, and then another GPT Work pass.

If GPT Work finds a defect that an earlier layer should have caught, the workflow must both repair the candidate and strengthen the upstream permanent guard.

---

## 7. Internal proof policy

For failed-version recovery and materially new visual systems:

- real-content component proof is mandatory;
- high-risk-page proof is mandatory;
- internal review/repair is mandatory before full-deck production.

The user may choose not to see the proof. That never authorizes skipping it.

---

## 8. Acceptance aggregation

Final acceptance is the conjunction of:

- required prebuild Critic PASS;
- Planner freezes intact;
- internal proofs PASS;
- deterministic Auditor PASS;
- rendered-artifact Auditor PASS;
- every mandatory render-dependent guard resolved on the exact candidate;
- positive visual ancestry preserved or explicitly retired;
- GPT Work PASS when required;
- required human decisions PASS;
- all previous locks preserved.

The aggregator cannot convert a failure to PASS.

---

## 9. Revision monotonicity

```text
open_feedback_next <= open_feedback_current
locked_pages_next >= locked_pages_current
locked_components_next >= locked_components_current
positive_visual_object_losses = 0
unrelated_changes = 0
```

Only explicitly authorized pages/components may change.

---

## 10. Repeated review/control failure

If a candidate with obvious full-deck defects reaches the user after claimed internal PASS:

1. mark the candidate human-rejected;
2. forbid minor page-local patching;
3. identify which gate failed to execute or lacked evidence;
4. add permanent cumulative guards;
5. replay the rejected candidate through the strengthened review path;
6. repair/version generic review infrastructure if the trust boundary failed.

A simple mechanical defect may receive a bounded correction. A new self-certification or missing-scope class triggers generic workflow repair.