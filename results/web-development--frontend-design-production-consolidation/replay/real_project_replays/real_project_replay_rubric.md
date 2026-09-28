# Frontend Design Real-Project Replay Rubric

For each project, output exactly these fields:

- `PROJECT`
- `FROZEN_REF`
- `FROZEN_COMMIT`
- `COORDINATOR_SOURCE_CONSUMED`
- `DELEGATE_SOURCES_CONSUMED`
- `ROUTE_SUMMARY`
- `REPO_LOCAL_RULE_GAVE_ANSWER`
- `COORDINATOR_GENERIC_DECISION_OBSERVED`
- `COUNTS_AS_COMPATIBILITY`
- `COUNTS_AS_PLUGIN_CAPABILITY`
- `EVIDENCE_LOCATOR`
- `EVIDENCE_LIMITS`

Counting rules:

- Count compatibility when the project-local source already supplies the relevant answer or expected behavior.
- Count plugin capability only when the candidate coordinator makes a generic routing, admission, authority, scale, surface, or evidence-boundary decision not directly supplied by the project source.
- If all three projects only prove compatibility, maturity remains `unclassified`.
- Browser, native-WebView, Figma, provider, and runtime claims require matching evidence; source-only replay cannot prove actual UI behavior.
- Target repositories are read-only. Do not ask to modify them, do not assume missing runtime state, and do not add a fourth project.
- Output summaries and source-consumption evidence only. Do not quote more than a short phrase from project sources.
