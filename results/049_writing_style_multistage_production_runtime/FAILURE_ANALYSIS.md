# 049 Failure Analysis — why 048 passed automation but failed the user

## Status

This document records the production failure that motivates task `049_writing_style_multistage_production_runtime`.

It is intentionally not a phrase blacklist and does not contain the private report plaintext.

## Verified facts from 048

- 048 implementation identity: `928de2325d781ca630883d03e0f381092675b269`.
- The internal `scientific-rewrite` skill documented a meaning-first workflow: document map -> argument units -> Meaning Card / Fidelity Ledger -> selected positive transformations -> rewrite -> exact check -> semantic audit -> Chinese language review -> whole-document coherence review.
- The private transform actually used Bridge Kit `text-transform` as one whole-document Responses API call. The transform manifest bound the complete source together with the complete scientific-rewrite / fidelity / Chinese-prose instruction bundle.
- Bridge Kit `text-transform` therefore executed a single transform call; it did not mechanically enforce the documented per-unit multistage orchestration.
- 048 Text Review returned PASS for fidelity/readability/completeness/coherence, and Reviewed Handoff Review 2 also returned PASS.
- The user rejected the delivered artifact immediately on real reading. The first page still foregrounded internal/abstract English research-process vocabulary and retained the source's audit/log-like conceptual skeleton. The user explicitly reported that seeing `provenance` on first read was enough to lose interest.

The user rejection is the decisive product evidence. Automated PASS does not override it.

## Root causes

### 1. Documented architecture != production behavior

The skill file described Architecture C, but the production transform behaved much closer to:

```text
full source
+ full rule bundle
+ full seed library
-> one model call
-> full rewritten document
```

That leaves the model strongly anchored to the source's existing headings, rhetorical skeleton and meta-language. The task proved that writing a multistage method in `SKILL.md` is not equivalent to executing it.

### 2. Literal-fidelity pressure was allowed to dominate reader-facing structure

048 required every citation/path/formal identifier to survive somewhere in the returned document. That is appropriate for fidelity, but the implementation did not distinguish:

- information that must remain inline because it carries the scientific argument; and
- exact trace material that may be relocated to a technical appendix without losing information.

As a result, evidence/provenance/implementation detail remained too prominent in the main reading path.

### 3. Seed transformations were available but not truly retrieved per unit

The seed library existed, but the whole library was included in the one-shot transform bundle. The production path did not prove that 2–4 relevant transformations were selected for each argument unit based on the unit's actual rewrite problem.

### 4. The final language gate was too source-aware and too tolerant

The source-aware Text Review was valuable for fidelity, but it also judged readability while seeing the source and candidate together. That makes it easy to reward completeness/fidelity while being too forgiving of reader effort.

The user demonstrated a false positive: automated readability PASS, human first-page REJECT.

### 5. No human style smoke existed before the expensive full-document run

The full private report was generated and reviewed before the user saw a representative style sample. A wrong prose regime therefore consumed the whole-document transform/review cycle before the actual reader could veto it.

## What 049 must change

049 is not another rule-tuning task. It must turn the already-researched meaning-first architecture into real production behavior.

Required changes:

1. Real multistage runtime, with model calls separated by responsibility.
2. Argument-unit rewrite, not one-shot full-document rewriting.
3. Per-unit Meaning Card / Fidelity Ledger that are generated and checked before prose generation.
4. Actual per-unit selection of a small number of positive transformations.
5. Literal fidelity split into `inline-critical` vs `relocatable-trace`, so technical trace can move to a reader-appropriate appendix.
6. Separate source-aware fidelity review from candidate-only reader review.
7. Mandatory three-segment human style smoke before full private report generation.
8. No target-document phrase blacklist, no AI-detector metric, no English-ratio KPI.
9. 048's secure private transport remains valuable and should be reused rather than rebuilt.

## Product success criterion

The task is not complete because CI or Terra says PASS.

Product success requires both:

- normal installed `writing-style` actually executes the multistage scientific-rewrite runtime; and
- the user reads the resulting Deep Research report and says it is genuinely useful for upcoming research/experiment work.
