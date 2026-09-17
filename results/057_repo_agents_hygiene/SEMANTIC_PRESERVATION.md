# 057 Semantic Preservation

Task key: `057_repo_agents_hygiene`

This file records hard-rule preservation before product-repository edits. The
approved kickoff authorizes the Bridge scaffold plus Lite versioning amendment;
Bridge implementation preserves existing-root project prose and moves no
project-specific target-repo rule.

## Source Refs

| Repo | Base ref | Branch | Status |
| --- | --- | --- | --- |
| AI_Skills_Collection | `e8ba751561c9e61a5b0bbd094d2c280ff0b00b59` | `reviewed/057_repo_agents_hygiene` | evidence only |
| GPT_Codex_AI_Bridge_Kit | `cb77b1cc5a1fce097a38066d2db452291e359852` | `reviewed/057_repo_agents_hygiene` | mutable |
| Bobbio | `0811116ac7197590f0af773f3c6296d4ca41db80` | `reviewed/057_repo_agents_hygiene` | mutable |
| Lucerna | `760931ae8a1f0edffefe41c83c1667c7190c3014` | `reviewed/057_repo_agents_hygiene` | mutable |
| Mica-for-ChatGPT | `aa4ce52581fff2e207d1f93600becbb3018b0efc` | `reviewed/057_repo_agents_hygiene` | mutable |
| Asteria | `166791c27752c70255043f026dcbda4deb693c04` | `reviewed/057_repo_agents_hygiene` | mutable |
| SeminarArc | `71c59d39f4d7e9cd3a3d813ad55d5cf6a38a4b11` | `reviewed/057_repo_agents_hygiene` | mutable |
| CUHK_Date | `711fab75f044b7ad31e5ff8610c076f902ccc949` | `main` | inspect only |

## GPT_Codex_AI_Bridge_Kit

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Fresh Lite repos need root guidance plus managed Bridge protocol | `ai_bridge_kit/cli.py` created only managed block when root missing | Add scaffold without inventing project facts | `templates/repo/AGENTS_TEMPLATE.md` + canonical managed block from `codex/AGENTS_SNIPPET.md` | H7 real init validates one block and Lite locator |
| Existing root project-owned prose must be preserved, including `--force` | Existing `install_agents_snippet` append/update block behavior | Preserve behavior; add regression test | `ai_bridge_kit/cli.py` existing-root path | H8 normal/force fixture checks byte-order preservation outside managed block |
| Lite default versioning belongs in delegated Lite execution authority | No generic fallback in `templates/prompts/AGENT_RULES.md` | Add approved fallback there only | `templates/prompts/AGENT_RULES.md` | H7 checks generated Lite rules; H9 checks root does not copy policy |

## Bobbio

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Current canonical visual design/components/screen composition | `docs/design/FIGMA_HANDOFF.md`; `AGENTS.md` still points frontend work at product brief + old PNGs | Keep Figma as visual authority and add root locator | `docs/design/FIGMA_HANDOFF.md` + `AGENTS.md` read-first | H2 compares root, Figma handoff, design brief |
| Product/interaction constraints and historical concept images | `docs/PRODUCT_DESIGN_BRIEF.md` says brief + old PNGs are primary visual basis | Reword only authority paragraph; preserve design content | `docs/PRODUCT_DESIGN_BRIEF.md` | H2 three-way authority comparison |
| Zotero/native/knowledge/iPad/Pencil safety invariants | `AGENTS.md` sections 4-13, 20-21 | Keep in root; no relocation | `AGENTS.md` | H6 keyword and section inspection |

## Lucerna

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Windows release/tray lifecycle, real provider truth, matching regression, screenshot helper/evidence budget, Longleaf boundaries | `AGENTS.md` project-owned sections | Light normalize only; keep as distinct invariants | `AGENTS.md` | H6 direct inspection |
| Managed Bridge block | canonical Bridge managed block in root | Do not hand-edit | unchanged | H4 marker comparison |

## Mica-for-ChatGPT

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Focused testing budget and tiered checks | repeated testing subsections in `AGENTS.md` | Consolidate wording, not acceptance semantics | `AGENTS.md` testing ladder | H6 direct inspection |
| Final authenticated long-conversation acceptance is manual | `AGENTS.md` P0/browser-test boundary | Preserve; forbid automated authenticated ChatGPT loop | `AGENTS.md` browser-test boundary | H6 direct inspection |
| Privacy diagnostics, fail-open behavior, typing hot path, stable `dist/mica-dev` | `AGENTS.md` | Preserve | `AGENTS.md` | H6 direct inspection |

## Asteria

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Fixed public entry point and Cloudflare/local runtime mechanics | `AGENTS.md` | Keep fixed URL in root; move volatile commands/mechanics to one runtime owner | `AGENTS.md` summary + `docs/operations/development/RUNTIME_OPERATIONS.md` | H3/H6 root locator and runtime owner inspection |
| Browser contract and `可以自动操作页面；不能绕过页面` | `AGENTS.md` | Keep in root | `AGENTS.md` | H6 direct inspection |
| GPT Work-before-human, visual/scientific delegated rule locators | `AGENTS.md` and `prompts/AGENT_RULES.md` | Keep root locators; do not edit delegated prompt | `AGENTS.md` | H6 direct inspection |

## SeminarArc

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Prominent physical-device safety summary | `AGENTS.md` detailed sections | Keep prominent root summary | `AGENTS.md` | H2/H3/H6 root inspection |
| Detailed device/environment/test mechanics, command restrictions, volatile inventory, incident evidence | split between `AGENTS.md` and `docs/DEVICE_TESTING.md`; doc says root owns complete physical constraints | Make DEVICE_TESTING detail owner; root links to it | `docs/DEVICE_TESTING.md` | H2 owner wording comparison |
| Emulator-first, protected device not generic target, no auto recovery/reset, explicit serial pre/postflight, physical failure does not block WSL/headless/Emulator, no PIN/secrets | `AGENTS.md` + `docs/DEVICE_TESTING.md` | Preserve in root summary and detail doc | both | H6 direct inspection |

## CUHK_Date

| Rule / authority | Old owner | Decision | New owner | Evidence |
| --- | --- | --- | --- | --- |
| Prototype instruction surface | current `main` | Inspect only; no root `AGENTS.md` creation | unchanged | H6 inspect-only note |
