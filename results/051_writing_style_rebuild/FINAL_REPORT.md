# Final Report

## What this task solved

Task 051 has produced a real successor candidate for the existing `writing-style` plugin's heavy Chinese scientific/technical rewrite path and has already proved that an ordinary installed-plugin request can route into the new heavy path without forcing the user to name internal implementation stages. The task also established repo-local candidate replay, known-regression replay, complete-report replay, frozen fresh-holdout evaluation, and independent Text Review evidence.

The task is not eligible for final PASS or integration. After the second Text Review failed on an incomplete frozen Kalman holdout, the user explicitly authorized exactly one final bounded recovery: use one semantically complete fresh holdout, do no holdout-specific production tuning, and allow one final candidate-only Text Review with worst-case reservation at most USD 0.25 and no paid retry. That final holdout replay was prepared successfully, but the Text Review workflow stopped in pre-request accounting validation with `ERROR: paid review budget contract mismatch`. No paid model request was proven sent and no new Text Review evidence was written.

The user then authorized accounting-only recovery for the exact same candidate, Bloom holdout, encrypted packet, provider, privacy boundary, one unsent model call, USD 0.25 worst-case reservation, and no automatic retry. The current installed/canonical Text Review accounting runtime has no supported way to express that recovery without mutating or bypassing prior ledger history. 051 therefore stops as `051_STOP_ACCOUNTING_INFRA`, not as a writing-style production failure and not as final PASS.

## What changed

The current production/recovery implementation candidate remains frozen at `2690de2cbc3d4ffb0741ecb80297a569647051f2`. No production implementation is changed by this Planner transaction.

The final bounded recovery completed the requested governance hardening, froze a semantically complete Bloom-filter holdout before generation, and replayed it through the existing candidate. The replay proved ordinary `scientific-rewrite` routing, heavy-route receipt V2, no paid generation, and passing mechanical reader-facing leakage/fidelity/semantic checks. The resulting private candidate packet was encrypted and staged for the final independent Text Review.

The repository paid-review ledger records the two completed earlier reviews and the user's authorization for a third and final paid call. However, the Bridge Kit workflow rejected the current campaign contract before sending a model request. The failed workflow is GitHub Actions run `34379122780`; its `Run text review` step failed with `paid review budget contract mismatch`, and the evidence-commit step was skipped.

Required final CI, release/version closure, install/upgrade smoke, GPT Reviewer PASS, and integration remain intentionally unstarted.

## New capabilities / behavior

The candidate continues to demonstrate the intended heavy Chinese rewrite behavior: ordinary long Chinese source-faithful rewrite requests route to `scientific-rewrite`; short/local Chinese polish, fidelity-only work, and English `scientific-prose` remain separate; host Codex remains the generation owner; formal realization is meaning-driven rather than raw-source paragraph paraphrase; structured semantic audit/repair remains separated from drafting; and normal production generation does not use paid external generation calls.

The final recovery additionally demonstrates a fresh-holdout completeness preflight before freeze. The Bloom-filter source range ends on a complete semantic boundary rather than mid-equation, mid-list, or before a promised mathematical definition, addressing the defect that invalidated the preceding Kalman holdout.

## Deliberately not adopted / unchanged

051 still does not rename the `writing-style` plugin, introduce a second generation runtime, restore per-stage paid generation, use fixed-size heavy chunking as the semantic planner, treat arbitrary Latin spans as exact identities, or turn candidate replay into another workflow/runtime manager.

The failed Kalman holdout is not being repaired or relabeled as a valid unseen PASS. The final Bloom-filter holdout is not being replaced or tuned against. No additional provider, endpoint, private-data scope, or production behavior has been introduced. No paid Text Review request was sent by the failed final workflow, and no automatic rerun is being performed.

## Example usage

A normal user-facing request the candidate is intended to support is:

> 把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢；不要逐句翻译，也不要总结掉内容。

Another valid request is:

> 内容都对，但现在像项目备忘录。按原意重新讲清楚，让第一次看的研究者能顺着读下去，正式算法名和数据集名保留。

Short local polishing, fidelity-only checking, and English scientific prose remain on their existing routes.

## Regression and remaining limitations

The first independent Text Review returned `REVISE` for Gate 3 A/B and the first Gate 5 holdout. The bounded recovery then regenerated A/B from complete context and applied a generic reader-facing internal-workflow leakage guard. The second independent Text Review passed recovered Gate 3 A/B, unchanged Gate 3 C, and Gate 4, but returned `REVISE` for the new Kalman holdout because its frozen source itself ended before the promised equation and produced an incomplete-feeling reader artifact.

The user then authorized one final bounded recovery. That recovery froze a semantically complete Bloom-filter source and produced a final candidate packet, but the independent review itself has not occurred: workflow run `34379122780` failed during pre-request accounting validation. Logs show the payload decrypted successfully, then `ai-bridge text-review run` stopped with `ERROR: paid review budget contract mismatch`. The workflow wrote no new `TEXT_REVIEW.json`, and repository control state records that no paid model request was proven sent.

This failure remains recoverable only after Bridge/Text Review accounting grows a supported authorized unsent-call recovery path. Such a path must preserve the immutable prior two-call ledger and task-wide cumulative cost record while enforcing the separately authorized final one-call cap. The current 051 branch does not hack the ledger, delete history, fake a reservation, or create an unsupported campaign identity to bypass that missing contract.

Required final CI remains pending by design and was not started. Because safe accounting still cannot be established, 051 stops without final PASS, final CI, version/changelog/release closure, production install smoke, GPT Reviewer PASS, or integration.

## Generic governance result

The repository now contains a generic governance commit that is useful beyond
051 and is safe to integrate independently if 051 itself remains stopped:

```text
generic_governance_commit=431cf8113b7fd269c1a8cb05982e8cffad33b849
generic_governance_safe_to_integrate_independently=YES
candidate_replay_canonicalized=YES
state_refresh_rule_added=YES
authorization_dedup_rule_added=YES
holdout_preflight_rule_added=YES
paid_campaign_freeze_rule_added=YES
pre_request_unsent_recovery_rule_added=YES
```

That commit records the reusable 052/053 rules for resume-time state refresh,
canonical central-plugin candidate replay, authorization deduplication,
holdout semantic-completeness preflight, immutable paid campaign contracts, and
pre-request unsent-call recovery semantics.

## Technical appendix

- Task branch: `reviewed/051_writing_style_rebuild`
- Current implementation candidate: `2690de2cbc3d4ffb0741ecb80297a569647051f2`
- Final outcome: `051_STOP_ACCOUNTING_INFRA`
- Frozen Plan revision: `1` of maximum `1`
- Current CI status: `PENDING`; final release/integration CI has not started
- Latest completed Text Review evidence: `results/051_writing_style_rebuild/text_review/TEXT_REVIEW.json`
- Latest completed Text Review decision: `REVISE`
- Latest completed paid review call number: `2`
- Final recovery Text Review manifest: `results/051_writing_style_rebuild/text_review/text_inputs.json`
- Final recovery encrypted payload SHA256: `a3e078b4f809ed9932e3caa35a1c7f6d874a0c6cb0fcf0b69824abe8a212def0`
- Final recovery plaintext packet SHA256: `07b985887d6e35c24835fe156b631469498ee34cee84f8b13f2b6cf6b91e9dc1`
- Final recovery holdout manifest: `results/051_writing_style_rebuild/recovery/final_holdout_manifest.json`
- Failed final Text Review workflow: `34379122780`
- Workflow conclusion: `failure`
- Failed step: `Run text review`
- Observed error: `ERROR: paid review budget contract mismatch`
- Paid model request proven sent: `false`
- New Text Review evidence written: `false`
- Accounting-only recovery authorized: `true`
- Accounting-only recovery completed: `false`
- Accounting infrastructure missing capability: supported one-call authorized
  unsent-call recovery that preserves immutable prior ledger history
- Existing implementation-commit combined status checks: none reported; final required CI remains not started
- No production implementation file is modified by this Planner transaction.
