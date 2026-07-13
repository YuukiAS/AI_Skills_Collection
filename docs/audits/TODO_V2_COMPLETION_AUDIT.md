# TODO v2 Completion Audit

Status vocabulary is limited to `PASS | PARTIAL | FAIL | DEFERRED_USER_ACTION | NOT_APPLICABLE`.

| Area | Status | Evidence |
|---|---|---|
| Central marketplace fixed to nine generic plugins | PASS | `scripts/codex_marketplace_config.json` contains the generic nine-plugin set and omits `cardiacnexus`. |
| Plugin versions synchronized | PASS | All marketplace plugin entries now use `version: "3.0.0"` after the v3 release bump. |
| `presentations` split from `research-writing` | PASS | `presentations` owns research/business routes and shared CUHK payload; `research-writing` no longer publishes legacy `pptx` or `scientific-slides`. |
| Chinese README direction | PARTIAL | Main README is Chinese-first; v3.1 continues tightening profile and environment sections. |
| CUHK LaTeX/PPTX template payload | PARTIAL | Beamer source, design tokens, PPTX builder/reference deck, and importer are tracked; live LaTeX/PPTX render verification depends on local tool availability. |
| CardiacNexus migration package | DEFERRED_USER_ACTION | Export package remains under `exports/cardiacnexus-repo-local/`; user will merge it into the CardiacNexus repo and then remove the temporary export package. |
| Historical source compression | PASS | Canonical history lives in `docs/provenance/INTEGRATION_HISTORY.md`; scratch intake remains outside tracked source. |
| Legacy bundles | PASS | Bundle JSON files moved under `archive/legacy-bundles/`; `scripts/install_bundle.py` is a compatibility shim. |
| Icon/provenance audit hooks | PARTIAL | Marketplace and app-facing icon audit exists; full source-skill icon coverage remains a planned P1, not a v3.1 blocker. |
| Live installation verification | DEFERRED_USER_ACTION | Codex App sparse install and real CUHK/UNC login verification require the user's authenticated local/remote environment. |
