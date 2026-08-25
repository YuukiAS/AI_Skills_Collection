# Research Presentation Iteration Notes — CAT-TRACE review, 2026-08-25

This note records reusable presentation-design failures exposed while reviewing a statistics group-meeting deck. It is intentionally project-agnostic: the examples came from CAT-TRACE, but the TODOs below should be considered for later consolidation into `research-presentations/TODO.md`, active guidance, or rendered-slide QA.

## Status

All items below are `KEEP_BACKLOG` candidates until the normal presentation-skill consolidation / reviewed-handoff process decides whether they should be promoted, merged with an existing rule, or covered by a regression check.

## Audience-first terminology gate

- [KEEP_BACKLOG] A slide can satisfy an acronym-expansion rule and still fail audience grounding. Rendered QA should also flag domain-specific shorthand whose meaning is not obvious to the actual audience, even when it is not formally an acronym. Examples include OTU, GBIF-based taxonomy, COI barcode, singleton/doubleton, soft matching, and domain-specific catalogue terminology.
- [KEEP_BACKLOG] At first use, a domain term should answer in plain language: what physical or biological object it refers to, how it is obtained, and whether it is identical to the everyday word used nearby. Example pattern: “OTU: a sequence-defined analysis unit; it may approximate a species but is not necessarily a verified named species.”
- [KEEP_BACKLOG] Assume expertise only in the audience’s home discipline. A statistics audience may know Bayesian hierarchical models and asymptotics but not ecological databases, sequencing pipelines, taxonomic infrastructure, or field-sampling terminology.

## Internal-planning language leakage

- [KEEP_BACKLOG] Phrases useful during analysis planning can sound synthetic or evasive on a scientific slide. Terms such as “anchor”, “schema calibration”, “main stress factor”, “continuity regime”, “benchmark role”, and similar workflow labels should be translated into the scientific claim actually being tested, unless the term is standard in the field.
- [KEEP_BACKLOG] A dataset slide should say what organism/system was sampled, how the response was measured, what the main rare/common structure looks like, and what scientific/statistical question the dataset answers. It should not rely on internal project-role labels as the explanation.

## Comparator / prior-work explanation

- [KEEP_BACKLOG] For a comparator unfamiliar to the audience, one formula plus a label is insufficient. Explain the mechanism as a short causal sequence: what data are fitted first, what information is learned, what gets transferred/conditioned on, and which target remains outside the method’s scope.
- [KEEP_BACKLOG] When the distinction from the proposed method depends on “observed response columns” versus “future unseen columns”, make that boundary visually explicit rather than requiring the audience to infer it from prose.

## Mathematical model and theorem pages

- [KEEP_BACKLOG] A model section should contain at least one page where the complete generative structure is visible in one place. Splitting components across many pages without a closed model equation/diagram leaves the audience unable to reconstruct what was actually proposed.
- [KEEP_BACKLOG] A theorem page must state not only the mathematical result but also: what failure it prevents, why that property is needed for the proposed model, and which limitation of the closest existing method it addresses. For extensions of an existing theorem, explicitly state what is genuinely new and what reduces to the baseline result.
- [KEEP_BACKLOG] When a key prior/scaling argument is central to the parent method, preserve the mathematics even if it requires an extra slide; do not compress away the derivation merely to keep page count fixed.

## Simulation slides

- [KEEP_BACKLOG] Distinguish an oracle/theorem check from an inference experiment. An oracle Monte Carlo check should not be presented as if a model were fitted to `n` training samples.
- [KEEP_BACKLOG] A simulation slide should show explicit sample-size and dimension choices (`n`, future horizon `m`, response dimension/truncation `p`, group count/rank when relevant), not just the symbolic DGP. This lets a statistical audience judge whether the regime is too small, adequate, or computationally unrealistic.
- [KEEP_BACKLOG] Every simulation needs a discriminating comparator/ablation tied to the paper claim. “Measure recovery error” alone does not establish that the proposed component is necessary.

## Real-data slides

- [KEEP_BACKLOG] Restore compact prevalence/rarity visuals when singleton/doubleton structure is part of the motivation. A good dataset page combines one real-world/context image with one quantitative rarity panel rather than replacing the distribution with counts embedded in prose.
- [KEEP_BACKLOG] When showing rarity categories across datasets, use the same category definition and axis scale where possible, e.g. singleton / doubleton / prevalence ≥ 3, and label bars as `count (percentage)`.
- [KEEP_BACKLOG] Biological context must be understandable without specialist taxonomy knowledge. When using group names such as Diptera, Hymenoptera, or Lepidoptera, add familiar examples (flies/mosquitoes; ants/bees/wasps; butterflies/moths) when that materially reduces audience effort.

## Visual hierarchy and parallel blocks

- [KEEP_BACKLOG] Parallel semantic components shown as peer cards/blocks should have equal visual height and aligned baselines unless size encodes a real quantitative difference. Small accidental height differences look like layout errors, not information.
- [KEEP_BACKLOG] Avoid forcing unrelated priors or mechanisms into a two-column comparison solely to fill the slide. If the objects are sequential or at different model levels, use a single reading direction.

## Advisor discussion questions

- [KEEP_BACKLOG] Discussion prompts should be answerable from the advisor’s expertise without requiring detailed knowledge of the project’s internal notation or implementation. For a statistically trained audience, phrase the question in terms of identifiable alternatives such as local finiteness vs expectation-only guarantees, full-scale vs bounded-working-set inference, or centering vs orthogonality constraints.
- [KEEP_BACKLOG] When a broad question previously produced vague answers, offer 2–3 defensible options with one-line tradeoffs. The goal is to elicit a decision, not to outsource an underspecified research problem to the audience.

## Follow-up consolidation

Future presentation-skill work should compare these items against existing `Audience-first`, `Scientific object first`, `Existing-method comparison`, theorem/statistics benchmark, and diagram-geometry rules. The main gap exposed here is not the absence of all such principles, but weak enforcement at rendered-slide review time: technically correct terminology and formulas can still be audience-hostile or planning-jargon-heavy.
