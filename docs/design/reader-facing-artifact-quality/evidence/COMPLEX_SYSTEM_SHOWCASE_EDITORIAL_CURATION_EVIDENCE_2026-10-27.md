# Complex-system showcase editorial / curation evidence

Date: 2026-10-27

Status: research evidence; not a production Skill contract
Source task: two independent R2 Delivery Assurance showcase sites in `AI_Research_Toolkit`

## Why this file exists

This evidence extends the existing reader-facing artifact-quality design and the already tracked Product UI Copy / Frontend Design items (#90 and #89). It does **not** define a second synonymous rule system, change a production Skill, or claim that Artifact Curation is implemented.

The two sites were rendered and reviewed as products before their author reports were read. The audit covered desktop, different component and edge selections, success/failure/regression paths, disclosures and 390px mobile layouts. The final ledger contains 720 current visible-content entries plus 26 cross-site replay cases.

## Observed cross-model failure

The visual architectures differed, but both sites independently converged on the same content behavior:

1. every component had to fill five or six parallel explanatory fields;
2. graph relationships were repeated in inspectors and later prose;
3. the same implementation state appeared in the header, hero, badges, details, evidence and footer;
4. research alternatives, historical estimates and process notes occupied the primary product path;
5. individually acceptable sentences accumulated into a report-like whole page;
6. mobile either inherited the desktop information structure or required a separate path-first correction.

This is stronger evidence than a single awkward sentence. The repeated failure occurred across two independent model outputs that had already performed their own sentence-level copy audits.

## Ownership result

| Decision | Owner | Evidence from this audit |
| --- | --- | --- |
| Whether a text block, field, card or disclosure should exist | Frontend Design / future Artifact Curation | Removing or merging fixed fields produced the largest quality gain. |
| Where the retained fact belongs and how prominent it should be | Frontend Design / future Artifact Curation | Route comparisons and old estimates became useful only after relocation. |
| How retained copy should read | Clear Writing / Product UI Copy | Task-led titles and shorter dynamic steps improved naturalness without changing meaning. |
| Which facts must survive | Writing Fidelity / domain authority | Version identity, evidence invalidation, failure destination and legacy behavior remained protected. |

## Artifact Curation candidate contract

The evidence supports a small, explicit disposition vocabulary:

- `KEEP`: the element has direct reader or user value in its current layer;
- `DELETE`: it adds no information or exists only because a template has a slot;
- `MERGE`: its meaning is useful but duplicates neighboring content;
- `RELOCATE`: it is useful evidence or detail at the wrong reading level;
- `REWRITE`: the element should remain, but its realization is not acceptable.

Candidate rules supported by both sites:

1. No default `KEEP`. Every meaningful rendered block must receive a disposition.
2. Template completeness is not reader completeness. Components may have one summary and zero additional fields.
3. `why / input / output / recipient / removal consequence / status` is not a universal component schema.
4. A graph's direction, grouping and order should not be restated line by line unless the text adds an accessibility or risk boundary.
5. One fact should have one primary location. Repetition elsewhere must add a new consequence or action.
6. Research history, rejected alternatives, cost estimates and source-method notes default to a lower layer.
7. Responsive curation changes priority, not merely scale. Mobile acceptance should start from the reader's primary task.
8. Intentional whitespace and an empty optional slot are valid outputs.

These are review rules, not automatic deletion rules. A core component may still need a status or existence rationale when it changes a decision.

## Clear Writing evidence

Once disposition and placement were frozen, current writing capabilities handled the retained copy well:

- `交付验收怎样工作` → `交付前，谁检查什么`
- `一次交付怎样完成验收、返修和复验` → `失败怎样回到原任务`
- long multi-actor failure steps → one current action plus its evidence change
- internal process labels such as `下一位接收者` → task language such as `去向`
- repeated caveats → one primary boundary plus only new local detail

Required negative test: Clear Writing must not recreate deleted fields or polish an upstream content-architecture defect as if it were only a wording problem.

Required fidelity test: de-templating must preserve candidate/version identity, actual vs expected result, known unknowns, failure return, permission boundary and legacy-function protection.

## Rendered outcome

Default visible text fell from 1,258 to 894 non-whitespace characters for the GPT‑6 candidate and from 1,807 to 940 for the GPT‑5.6 candidate. Default inspector terms fell from 5 and 9 to 3 and 3. These reductions are not the acceptance target by themselves. Acceptance came from retaining all architecture nodes/edges and all three delivery paths while making the product easier to read.

One site's 1,710px mobile relationship graph was replaced by a five-step path and component entry points. The other site's existing path-first mobile structure was retained and edited. This is a useful near-miss pair: the same disposition should not mechanically force the same component implementation.

## Replay assets

- [Regression cases](COMPLEX_SYSTEM_SHOWCASE_REGRESSION_CASES_2026-10-27.tsv)
- Toolkit source branch: `research/complex-system-showcase-20261027-work-editorial-audit`
- Toolkit audit: `docs/research/complex-system-showcase-20261026/r2/editorial-audit/EDITORIAL_AND_CURATION_AUDIT.md`
- Toolkit full ledger: `docs/research/complex-system-showcase-20261026/r2/editorial-audit/VISIBLE_CONTENT_AUDIT.tsv`

## Research conclusions versus future production work

Supported research conclusions:

- whole-page AI-like quality is not reducible to sentence naturalness;
- existence decisions must precede writing polish;
- fixed-field saturation, semantic repetition and mobile priority are high-value review signals;
- one shared replay set can evaluate both writing and curation while keeping ownership separate.

Future implementation candidates, not completed here:

- a rendered-state visible-content extractor;
- a disposition ledger in the Frontend Design workflow;
- page-level repeated-state, template-coverage and graph/text redundancy probes;
- a replay harness that routes retained wording to Product UI Copy and existence defects to Artifact Curation;
- formal Artifact Curation Skill design, implementation and promotion gates.

No production Skill, plugin manifest, generated payload, version or release artifact is changed by this evidence branch.
