# G2 Final Reviewer Rubric

Candidate before pre-final promotion: C0 `1c37c0715aca0096606f24e56192b7857e72bbd6`.

The same final candidate and this same rubric must govern both phases.

## Phase 1 — greenfield authoring

PASS requires all of the following:

1. **Greenfield provenance**: the document is built from the frozen raw manifest, not an existing reader-facing report.
2. **Reader-first structure**: the scientific question and decision logic organize the document; execution chronology does not.
3. **Orientation**: a technically competent advisor who has not followed the run history can understand the data roles, comparison, and why the clean/robustness evidence was needed.
4. **Claim/evidence discipline**: every strong claim is supported by the frozen raw evidence; CARE primary evidence and M&Ms supporting evidence are not collapsed.
5. **Uncertainty**: uncertainty and limitations are represented at the strength supported by source.
6. **Internal-detail filtering**: job IDs, runtime chronology, audit tokens, internal paths and implementation bookkeeping are absent from the reader-facing main narrative unless scientifically necessary.
7. **Table/figure/formula role**: any table, figure or formula has a genuine scientific job. Decorative/redundant objects are a failure. Omission is acceptable when no object improves the scientific argument.
8. **References/provenance boundary**: reader-facing scientific evidence is distinguishable from author-only repository provenance.
9. **Clear Writing handoff**: wording may improve, but scientific meaning, numeric values, evidence authority and limitations remain unchanged after the language pass.
10. **No Phase 2 leakage**: the document does not state or imply personalized-partial-pooling results.

Any material failure above => `PHASE1=FAIL`. Phase 2 must not start.

## Phase 2 — incremental authoring

PASS requires:

1. frozen Phase 1 PASS document is the baseline;
2. only the pre-frozen Phase 2 delta is newly introduced;
3. changed sections correspond to the minimal dependency closure of the delta;
4. unaffected accepted text remains materially unchanged;
5. notation, claim strength, citation keys, equation/theorem labels, figure/table identity and cross references remain stable unless the delta directly requires a change;
6. prior uncertainty/limitations are not rewritten to make the new result look inevitable;
7. the new result changes the scientific decision only to the degree supported by the delta;
8. baseline -> candidate diff contains no unexplained broad rewrite.

Any material failure => `G2=FAIL`.

## Freshness / anti-adaptation

Before Phase 1 begins, freeze:
- final candidate C;
- this rubric;
- Phase 1 manifest;
- Phase 2 delta identity.

After seeing Phase 1 or Phase 2 output, any product/rubric/task/delta change terminates the final attempt. Subsequent use of the same materials is development regression only.

Reviewer records:
- `PHASE1=PASS|FAIL`;
- after Phase 2, `G2=PASS|FAIL`;
- concise evidence with exact source/candidate identities.
