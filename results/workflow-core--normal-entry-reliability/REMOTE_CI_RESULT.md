# workflow-core 0.5 Remote Broad CI Result

Task branch: `work/workflow-core--normal-entry-reliability`

Final production candidate commit: `671eb532e0ec949dc7889427379a1113cf7a6ea9`

Evidence-only HEAD commit tested by remote CI: `331f2d155ff5bad015fb278dcd884ceb39a363e6`

Remote CI:

- Workflow: `Codex Marketplace`
- Trigger: `workflow_dispatch`
- Run: <https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/36964684181>
- Head SHA: `331f2d155ff5bad015fb278dcd884ceb39a363e6`
- Status: `completed`
- Conclusion: `success`
- Created: `2026-10-02T04:28:11Z`
- Updated: `2026-10-02T04:29:25Z`

Jobs observed PASS:

- `codex-marketplace`
- `windows-sparse-checkout`
- `editable-install-smoke (ubuntu-latest)`
- `editable-install-smoke (windows-latest)`

Production-tree consistency:

`git diff --name-only 671eb532e0ec949dc7889427379a1113cf7a6ea9..331f2d155ff5bad015fb278dcd884ceb39a363e6`
lists only files under `results/workflow-core--normal-entry-reliability/`.

Therefore the evidence-only HEAD preserves the final candidate production source,
generated marketplace payload, version metadata, release metadata, and workflow-core
runtime surface from `671eb532e0ec949dc7889427379a1113cf7a6ea9`.
