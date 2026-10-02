# Frontend Design Real-Project Replay Task

Use the installed `web-development` candidate plugin through the normal Frontend Design entry. Read the generated normal entry, then the coordinator source, then only the delegate sources selected for each project.

Input files provide frozen read-only source locators for Bobbio, Lucerna, and Asteria. Read the listed project sources from their frozen Git refs with read-only commands such as `git -C <repo_path> show <ref>:<path>`. Do not modify any target repository, do not check out another ref, and do not copy project source text into outputs.

For each project, determine the Frontend Design route and attribution supported by the source. Distinguish project-local compatibility from candidate coordinator capability. Do not claim browser, native-WebView, Figma, provider, or runtime evidence that is not present in the frozen source.

Write all outputs under `outputs/`:

- `real-project-attribution.md`: one section per project with the required attribution fields from the rubric.
- `real-project-attribution.json`: machine-readable version of the same conclusions.
- `real-project-source-consumption.json`: candidate plugin source paths read, route/delegate consumption, input manifest hash, and evidence-scope limitations.
