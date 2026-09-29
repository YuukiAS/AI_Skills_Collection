# Cross-Surface Product Interface Review

Use the attached source bundle and fixture files to produce a concise review
under `outputs/`.

This is not only a wording pass. First judge the user-facing interface
architecture: surface type, placement, hierarchy, neighboring copy,
progressive disclosure, viewport/layout risk, and rendered acceptance boundary.
Then decide which visible strings can safely change under the protected product
meaning.

Review all five families:

1. Generic settings/deletion fixture.
2. Lucerna desktop/native-WebView compact-panel case.
3. Mica browser-extension popup case.
4. SeminarArc Compose UI positive case.
5. SeminarArc Room/WorkManager/data-only negative case.

For each family, write:

- whether user-facing interface design/copy work is in scope;
- the interface architecture or rendered-surface concern, if any;
- which facts must be protected before wording changes;
- any handoff fields needed before final wording;
- one or two improved strings only when wording is safe;
- `KEEP` for already-clear copy that should not be rewritten;
- any escalation when product, trust, legal, or safety facts are missing;
- rendered or platform-evidence limits that should be reported.

Also include one short `routing-boundary` section explaining why the
Room/WorkManager/data-only request should not be treated as user-interface work
when the UI is explicitly unchanged.

Do not modify source files. Do not contact external services. Keep the answer
plain text or Markdown.
