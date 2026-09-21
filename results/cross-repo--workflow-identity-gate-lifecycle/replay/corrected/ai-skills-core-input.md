# Corrected Public Input: AI Skills Maintainer Scope And Gate Cases

Classify these five cases. They intentionally provide facts, not the answer.

## Case M1: Single Plugin Maintenance

Only `writing-style` source skill guidance changes. Generated `plugins/codex/plugins/writing-style/...` must be refreshed. The failure was a writing artifact regression already represented by an existing writing-style capability gate. No Bridge or other AI_Skills plugin source changes.

## Case M2: One AI_Skills Repo, Multiple Production Plugins

One bounded task changes `workflow-core` and `ai-skills-core` source skills, generated payloads, versions, changelogs, and repository release metadata. It does not change `writing-style`, `presentations`, or project product repos.

## Case M3: AI_Skills Plus Bridge Mutable, Product Repos Read-Only

A cross-repo task changes AI_Skills workflow guidance and Bridge task-key validation. Other downstream product repositories are referenced only as examples and must stay read-only. The final evidence must bind exact AI_Skills and Bridge candidate SHAs together.

## Case M4: Existing Capability Regression

A real user reports that a plugin output fails a behavior that the plugin already claims to support and that the active Capability Gate already names. The tempting fix is to create a new nearly identical gate with a different label.

## Case M5: Genuinely New Capability

A task proposes support for a user-visible capability not currently claimed by the plugin. It needs a different normal entry, evidence type, and failure semantics from all current gates.

Professional quality reminders: prose quality belongs to writing-style, slide quality belongs to presentations, statistical correctness belongs to statistical-modeling, and this maintainer only owns source authority, generated parity, replay/regression, version/changelog, and release closure.
