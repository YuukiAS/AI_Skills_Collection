# Project-memory isolation

- check_type: read-only capability inspection
- ChatGPT_Project_locators_visible: `YES`
- sanitized_ChatGPT_Project_count: `17`
- memory_mode_field_visible: `NO`
- cross_Project_history_isolation_visible: `NO`
- Project_files_or_knowledge_controls_visible: `NO`
- Project_connector_or_tool_controls_visible: `NO`
- result: `UNPROVEN`

The Project listing schema exposes locator metadata but no `project-only`
memory field or equivalent observable cross-arm history-isolation semantics.
The existence of ChatGPT Projects alone is insufficient under the frozen
contract.

No Project identifiers, names, paths, files, or unrelated content were stored.
