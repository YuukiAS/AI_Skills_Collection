# Raw Notes For C2 Development Replay

Project: public-safe CARE sequence modeling note.

Audience: PI/advisor.

Decision needed: whether the next week should focus on a personalization
ablation or on expanding robustness checks for a clean subject-disjoint split.

Observed evidence:

- Clean subject-disjoint replication finished on the current preprocessing
  contract.
- Macro-F1 for the compact temporal model was 0.714.
- Macro-F1 for the non-temporal baseline was 0.671.
- The paired bootstrap 95% confidence interval for the macro-F1 difference was
  [0.018, 0.071].
- Pattern H robustness on a shifted cohort kept the temporal model ahead, but
  the interval narrowed to [0.004, 0.049].
- Error inspection found most residual mistakes in short sequences with fewer
  than four observations.
- A pilot personalization run improved short-sequence recall from 0.46 to 0.51,
  but it used only one seed and should be treated as preliminary.

Constraints:

- Do not claim clinical validity.
- Do not claim deployability.
- Make it clear that the personalization result is only a pilot.
- The advisor needs a formal-PDF-ready source document later, but the current
  task is the Research Authoring stage.

Requested output:

- A stable Markdown source report.
- A production handoff that tells the downstream renderer what the document is,
  which tables or figures would be useful, and what layout/render checks remain
  pending.
