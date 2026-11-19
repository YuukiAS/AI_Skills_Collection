---
name: literature-and-citations
description: "兼容入口：旧 `litcite`／`literature-and-citations` 名称转到 `research-citations`；文献与引用正文及行为保持现有实现。"
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: true
secrets_needed:
  - OPENROUTER_API_KEY
  - PARALLEL_API_KEY
  - ZOTERO_API_KEY
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/writing/research/literature-review
  - skills/writing/research/citation-verification
  - skills/science/discovery/citation-management
  - skills/science/discovery/research-lookup
  - skills/science/discovery/pyzotero
default_prompt:
---

[research-citations](../research-citations/SKILL.md)

旧 `litcite` 和 `literature-and-citations` 请求统一转到 `research-citations`。继续从新入口执行，文献检索、综述、引用核对与文献管理行为保持原样。
