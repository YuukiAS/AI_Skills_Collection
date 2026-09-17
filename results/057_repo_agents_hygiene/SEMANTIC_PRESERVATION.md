# 057 Semantic Preservation

Task key: `057_repo_agents_hygiene`

This file records the repaired E2 candidate. The earlier E/M tuple remains
historical failed evidence and is not reinterpreted as PASS.

## Current Candidate Refs

| Repo | Current ref | Branch | Status |
| --- | --- | --- | --- |
| GPT_Codex_AI_Bridge_Kit | `e1d6b781ad7e56d567bed419001069baf439d0a5` | `reviewed/057_repo_agents_hygiene` | repaired |
| Bobbio | `ab5dccb6b8b87c49671aa097233ce1bcc38be004` | `reviewed/057_repo_agents_hygiene` | repaired |
| Lucerna | `41cd1297af6901531d3135593bc9806bffc38829` | `reviewed/057_repo_agents_hygiene` | unchanged from prior 057 candidate |
| Mica-for-ChatGPT | `e49416f874f633aedc7521734ee5b0f441aae970` | `reviewed/057_repo_agents_hygiene` | repaired |
| Asteria | `0ce1d4daca1e410ce551570578dd563d4ef67e90` | `reviewed/057_repo_agents_hygiene` | repaired |
| SeminarArc | `74caaa4ecec16f1bc90987979458d1a4e93f52be` | `reviewed/057_repo_agents_hygiene` | repaired |
| CUHK_Date | `711fab75f044b7ad31e5ff8610c076f902ccc949` | `main` | inspect only |

## Bridge Kit

| Rule / authority | Repair | Preserved semantics |
| --- | --- | --- |
| Fresh Lite repos need root guidance plus managed Bridge protocol | `install_agents_snippet` writes scaffold bytes plus the canonical managed block when root `AGENTS.md` is absent. | Fresh repositories get root guidance and one managed block without inventing project-specific facts. |
| Existing root prose is project-owned | Existing `AGENTS.md` handling now reads/writes bytes and appends/replaces only the managed block span. | CRLF/CR/mixed newlines, trailing spaces and prose outside the managed block are preserved under normal init and `--force`. |
| Lite fallback versioning belongs in Lite rules | `templates/prompts/AGENT_RULES.md` adds docs/TODO/tests/helper-only and unreleased intermediate commit guidance. | Root README labels `0.8.3` as candidate state; formal versioning remains truthful and delegated. |

## Bobbio

| Rule / authority | Repair | Preserved semantics |
| --- | --- | --- |
| Current production visual design authority | Prior Figma authority closure remains in root and product brief. | Figma is canonical for visual design/components/screen composition; old PNGs are historical/supporting references. |
| GUI / Computer Use execution mechanics | Root now keeps hard boundaries and points to `docs/DEVELOPMENT_WORKFLOW.md`; missing self-inspection and single-action prompt details were moved into that owner. | Codex must self-inspect before asking the user, must not bypass GUI gates by mutating real Zotero data, and must avoid Software Update actions. |
| Native desktop acceptance/performance/copy | Root now summarizes hard rules and points to `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`. | Native release evidence, performance measurement, copy pass, and Work `INSUFFICIENT_NATIVE_EVIDENCE` semantics remain intact. |
| Zotero/native/knowledge/iPad/Pencil safety | Not relocated. | Core safety and product invariants remain in root. |

## Lucerna

No new edit was made in the repaired E2 candidate. The prior 057 branch commit
still contains the light meta-summary and preserves Windows release/tray
lifecycle, real provider truth, matching regression, screenshot helper/evidence
budget and Longleaf boundaries.

## Mica-for-ChatGPT

| Rule / authority | Repair | Preserved semantics |
| --- | --- | --- |
| Testing ladder | Replaced repeated testing subsections with one ladder. | Impact audit and focused checks still precede `npm test`; Tier 2 full E2E is still required for DOM/lifecycle candidates; stress remains risk-triggered; reports must distinguish evidence. |
| Authenticated real-site acceptance | Left outside the edited section and named in the ladder endpoint. | Automated authenticated ChatGPT regression remains forbidden; final long-conversation acceptance remains manual. |
| Privacy, fail-open, typing hot path and stable `dist/mica-dev` | Not edited. | Existing repo-specific runtime protections remain present. |

## Asteria

| Rule / authority | Repair | Preserved semantics |
| --- | --- | --- |
| Browser black-box contract | Root now names only the canonical contract, inline requirement and core invariant. | `可以自动操作页面；不能绕过页面` remains root-visible; fallback/timeout/contamination/result mechanics live in the canonical contract instead of duplicated root prose. |
| Development server/runtime mechanics | Root points to `docs/operations/development/RUNTIME_OPERATIONS.md`; detailed Vite/server rules moved there. | No duplicate servers, no dependency reinstall merely to start, fixed URL/public-entry constraints and Windows fallback mechanics remain discoverable. |
| GPT Work before human and scientific/visual delegated locators | Not weakened. | Root still points to GPT Work gate and `prompts/AGENT_RULES.md` delegated rules. |

## SeminarArc

| Rule / authority | Repair | Preserved semantics |
| --- | --- | --- |
| Root physical-device safety summary | Root now keeps a compact safety summary. | Emulator-first, protected physical device not generic target, no transport reset/recovery, explicit serial/pre-postflight, `DEVICE_CHANNEL_BLOCKED` scope and no secrets remain root-visible. |
| Detailed device/environment/test mechanics | Moved/centralized into `docs/DEVICE_TESTING.md`. | WSL/JDK/SDK/cache paths, Windows Emulator specifics, mixed-inventory fallback, command bans, harness commands, incident evidence and transport rules remain available in the detail owner. |

## CUHK_Date

CUHK_Date was inspect-only. No root `AGENTS.md` was created and no branch change
was made.
