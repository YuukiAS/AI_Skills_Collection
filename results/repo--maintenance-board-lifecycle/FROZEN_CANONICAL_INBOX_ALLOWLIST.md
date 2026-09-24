# Frozen Canonical Inbox Allowlist

This file is bounded evidence for `repo--maintenance-board-lifecycle`.
It is not a long-term registry, runtime source, or service.

KICKOFF_BASE_COMMIT = ea2ae9c74fdbf230c97ccca6412aecc9a7e3dcb0
ROOT_TODO_BLOB_SHA = fa0590fc73759f8fa085b60da5109ffda87f3c3e
FROZEN_INBOX_COUNT = 11

Parsing rule:

- Read `TODO.md` at `KICKOFF_BASE_COMMIT`.
- Treat only structured navigation-table entries under `Plugin TODO 入口` and
  `Standalone skill TODO 入口` as canonical maintenance inbox declarations.
- Ignore explanatory prose, examples, changelog links, workflow links, and any
  other incidental Markdown links.
- Verify every parsed path exists at the same base commit.

FROZEN_CANONICAL_INBOX_PATHS =
- docs/plugin-todos/workflow-core.md
- docs/plugin-todos/ai-skills-core.md
- docs/plugin-todos/writing-style.md
- docs/plugin-todos/research-writing.md
- docs/plugin-todos/presentations.md
- docs/plugin-todos/scientific-visualization.md
- docs/plugin-todos/web-development.md
- docs/plugin-todos/statistical-modeling.md
- docs/plugin-todos/bioinformatics.md
- docs/plugin-todos/medical-imaging.md
- docs/skill-todos/render-chinese-math-pdf.md

Existence verification at `KICKOFF_BASE_COMMIT`: PASS for all paths above.
