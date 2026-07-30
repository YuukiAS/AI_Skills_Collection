# Runtime Routing Audit - 2026-07-28

Scope: active source skills and generated Codex plugin snapshots across AI_Skills_Collection.

Purpose: remove brittle runtime triggers and legacy behavior that made skills depend on source repo names, old pipeline labels, provider/model brands, forced diagrams, forced human-blocking tools, or old Claude-specific wording.

Changes recorded:

- Archived the legacy `content-generation` runtime entry and routed current manuscript writing to `paper-workflow-orchestrator`, `scientific-writing`, `peer-review`, `writing-fidelity`, and `chinese-prose`.
- Kept `academic-paper-writer-pro` and `ocr-kb` for OCR, DOCX, Markdown, template, checkpoint, and final file delivery work; removed auto-update commands, unsafe deletion defaults, fixed pipeline trigger language, and blocking tool calls.
- Converted unconditional visual generation rules in conversion, ideation, poster, review, and Markdown/Mermaid skills into conditional routing based on user request, deliverable type, or actual structural complexity.
- Made image/schematic/infographic routing descriptions provider-neutral; provider names belong in compatibility/configuration notes, not route descriptions.
- Replaced old platform-specific document author/resource wording with Codex-neutral names and legacy compatibility notes.
- Added trigger evals for document formatting, conversion, research presentations, hypothesis generation, scientific critique, and Mermaid diagrams.
- Added `scripts/audit_skill_runtime_text.py` plus a unit test to prevent regression for the same hardcoded runtime phrases.

This record is about runtime behavior, not license provenance. Source attribution remains in provenance/source metadata where relevant.
