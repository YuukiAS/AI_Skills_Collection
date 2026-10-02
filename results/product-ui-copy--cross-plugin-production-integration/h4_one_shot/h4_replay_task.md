# Product UI Copy H4 Fresh Holdout One-Shot

You are evaluating the exact H3 fresh-holdout batch for the Product UI Copy
cross-plugin candidate.

Use the enabled candidate plugins:

- `web-development@ai-skills-candidate`
- `writing-style@ai-skills-candidate`

Read the relevant enabled skill instructions before answering. Process the
attached `final_holdout_batch.json` exactly once, in the scenario order given.

Constraints:

- Do not replace, skip, cherry-pick, or add scenarios.
- Do not modify source files.
- Do not invent product, legal, trust, retention, deletion, privacy, or safety
  facts that are not frozen in a scenario.
- Do not rewrite `KEEP` cases just to show activity.
- Treat content architecture as Frontend-owned and wording under frozen meaning
  as Product UI Copy-owned.
- Keep backend/runtime/data-only work out of Frontend Design and Product UI
  Copy when the user-visible interface is unchanged.

Write all outputs under `outputs/`:

1. `h4_holdout_response.md`
   - one section per scenario id;
   - include `route`, `outcome_class`, `decision`, and either final copy,
     content-architecture recommendation, product/legal/trust escalation, KEEP,
     or non-frontend routing explanation;
   - keep wording concise and product-interface-like.
2. `h4_holdout_verdict.json`
   - include the candidate commit, batch schema, scenario count, and a
     `scenario_results` array;
   - each item must include `id`, `expected_outcome_class`, `actual_outcome_class`,
     `verdict` (`PASS` or `FAIL`), and `notes`;
   - include top-level `overall_verdict`.

This is the only fresh H4 run for this batch.
