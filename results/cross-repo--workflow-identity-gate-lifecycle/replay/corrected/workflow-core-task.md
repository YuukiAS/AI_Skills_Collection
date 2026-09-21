# Verified Workflow Corrected Candidate Replay Task

Use the installed Verified Workflow capability to classify the public cases in the attached input.

For each case, decide:

- `release_gate`: `NARROW_OK`, `BROAD_FULL_REQUIRED`, `NOT_RELEASE_READY`, or `MATURITY_NOT_PROVEN`;
- why the decision follows from source-scope and evidence scope;
- whether same-final-candidate evidence is required;
- whether a fixed paid/fresh sample count is required.

Return a concise Markdown answer with one subsection per case. Do not modify files. Do not fetch network resources. This is a public-safe candidate plugin replay.
