# Local production replay task for 044

Use the installed `writing-style@yuukias-ai-skills` plugin behavior to process
the copied input file `02_input_source_extracted_layout.txt`.

This is a bounded local verification replay for task
`044_writing_style_deep_research_chinese_replay`. Do not modify source files,
do not run Git, do not use network access, and do not access the original caller
repository. Read only the staged task/input files available in this replay
workspace and write outputs only under the replay `outputs` directory.

Required skills:

- Use the installed Chinese prose skill for reader-facing Chinese rewriting.
- Use the installed writing-fidelity skill as the guardrail for facts, formulas,
  citations, numbers, method names, dataset names, caveats, and claim strength.

Write:

- `rewritten_report.md`: a complete Chinese reader-facing rewrite of the full
  input, preserving all scientific content and not summarizing or deleting
  sections.
- `replay_summary.md`: a short non-private QA note naming the output path,
  confirming the full final artifact was read once after generation, and listing
  the checks performed.

Acceptance gates:

- The final report must contain zero reader-facing occurrences of `provenance`.
- Ordinary English abstraction labels must not carry Chinese sentence structure.
  Do not leave raw phrase scaffolding such as `estimand`, `scientific gap`,
  `residual gap`, `state of the art`, `resource contract`, `testbed`,
  `shared initialization`, `local drift`, `pooled gap`, `anchor`,
  `controlled-drift`, `shared-anchor`, `pooled-objective`,
  `local-mode posterior aggregation`, or `objective approximation`, unless the
  occurrence is a protected code/path/table-field/paper-title/exact quote.
- Keep true protected English names such as algorithm names, dataset names,
  metric names, model names, formulas, variables, code identifiers, paths,
  paper titles, and citations.
- If a concept can be stated in natural Chinese without losing precision, do so.
  For example, explain what the experiment is estimating, what the reference
  point is, what gap remains, what information is aggregated, and what target is
  being approximated.
- Do not add new scientific claims, examples, causes, certainty, or conclusions.

After writing `rewritten_report.md`, read the entire file once for QA, write
`replay_summary.md`, and stop. Do not perform additional self-revision loops
unless the explicit scan above fails.
