# Presentations — Severe Render Regression Postmortem and Workflow Hardening

Date: 2026-10-07  
Status: **P0 ARCHITECTURE EVIDENCE / INCORPORATED INTO CANONICAL RUNTIME**

## 1. Incident summary

A real 38-page teaching deck reached the user after substantial source/history governance and Planner review. Its semantic structure and much of its copy were materially improved, but the rendered artifact remained unacceptable.

The repository itself labelled the artifact only as a **candidate ready for GPT Work final review**, not as a final accepted deck. It was nevertheless surfaced to the user before the required GPT Work gate completed. This was a direct process violation.

Observed classes included:

- widespread tiny objects combined with large unused body regions;
- dense multi-role pages compressed into unreadable text;
- pages that looked like document excerpts rather than slides;
- previously useful diagrams removed and replaced by prose;
- prior visual improvements not preserved;
- render-dependent historical feedback left visibly violated;
- a suspicious trace/plot whose scale appeared inconsistent with nearby numerical summaries;
- title/closing technically containing shell elements but still poorly composed;
- a deterministic Auditor returning PASS without page-level evidence strong enough to justify the visible result;
- a pre-GPT candidate being shown to the user;
- the user becoming the first effective whole-deck visual reviewer.

The candidate should never have reached user review.

## 2. Root causes

### 2.1 Specification correctness was mistaken for artifact quality

The prebuild Critic correctly reviewed page jobs, copy, source fidelity and layout intent. That review was later treated as if it guaranteed the quality of the future render.

It did not.

A prebuild Critic can certify only that a specification is coherent enough to produce.

### 2.2 Historical feedback was stored but not closed against the exact render

The workflow retained the raw feedback ledger, but the final review did not prove one row per render-dependent historical item against the exact candidate image.

“Guard exists” was confused with “guard passes on this artifact.”

### 2.3 Positive visual ancestry was not protected

The workflow tracked semantic ancestry but not enough positive visual ancestry. A Producer could preserve the page topic while discarding a useful diagram or composition.

### 2.4 Internal proof was skipped or treated as optional

The user did not want to review intermediate proofs. This was incorrectly translated into skipping or weakening internal component/high-risk-page proof.

The correct interpretation is: proofs remain mandatory but internal.

### 2.5 Render review lacked exact scope/evidence binding

A valid full-deck render review needs one row per page, per-page image identity, contact-sheet review, closure of all render-pending items, and exact candidate hashes.

The V13 page matrix recorded PASS flags and hashes, but did not persist the substantive whole-slide observations needed to justify PASS. A row containing only `PASS`, `P0=0`, `P1=0`, and `P2=0` is not a visual review.

### 2.6 Numerical visual plausibility was not a hard gate

Figures were treated mainly as rendered assets rather than numerical claims. A chart whose scale conflicts with nearby summaries must trigger source-variable validation.

### 2.7 Release-state routing failed

The artifact state was `CANDIDATE_READY_FOR_GPT_WORK_FINAL_REVIEW`. That state must never be presented as ready for user review.

Only an exact-candidate GPT Work PASS followed by acceptance aggregation may set `READY_FOR_USER_REVIEW = YES`.

## 3. Hardening applied

The canonical runtime now adds:

1. **positive visual ancestry freeze** for every non-trivial page/component;
2. **no deletion-as-repair** without explicit Planner retirement authority;
3. **mandatory internal component and high-risk-page proofs** for failed-version recovery;
4. **exact-candidate render closure matrix** for every render-dependent historical item;
5. **one substantive rendered-review row per page** for major/full-deck work;
6. **whole-slide + contact-sheet dual review**;
7. **typography floors and whitespace/scale review triggers**;
8. **numerical visual validation** for charts, traces and diagnostics;
9. **fresh rendered-artifact Auditor** distinct from prebuild Critic and deterministic Auditor;
10. **GPT Work binding to the exact final candidate**;
11. **release-state gate** forbidding user exposure of pre-GPT candidates;
12. **severe workflow failure rule** that forbids minor patching after widespread visual regression;
13. **upstream strengthening rule** whenever GPT Work or the user finds a defect that earlier gates should have caught.

## 4. Runtime files changed

- `plugins/codex/plugins/presentations/shared/presentation-end-to-end-pre-execution-runbook.md`
- `plugins/codex/plugins/presentations/shared/pre-execution-cumulative-acceptance-contract.md`
- `plugins/codex/plugins/presentations/shared/rendered-artifact-positive-ancestry-acceptance-contract.md`
- `plugins/codex/plugins/presentations/shared/independent-review-contract.md`

## 5. Promotion consequence

The presentations workflow is not considered mature until at least one substantial real deck demonstrates:

- complete history-to-authority mapping;
- positive visual ancestry preservation;
- mandatory internal proof without user involvement;
- all-page exact-render review with substantive observations;
- closure of every render-dependent historical item;
- numerical figure validation;
- GPT Work PASS on the exact final artifact;
- no candidate surfaced before the GPT Work gate;
- two-to-four-round monotone user convergence;
- zero recurrence of prior guarded failures.

A build, source audit, representative-page PASS, or pre-GPT candidate state is not sufficient.