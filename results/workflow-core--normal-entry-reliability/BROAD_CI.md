# workflow-core 0.5 Broad CI

Task: `workflow-core--normal-entry-reliability`

Branch: `work/workflow-core--normal-entry-reliability`

Final production candidate commit:
`671eb532e0ec949dc7889427379a1113cf7a6ea9`

Latest evidence repair commit covered by remote CI:
`877073bd47eba14bf4277de6b951015377368834`

## Local Broad Verification

The final candidate G1-G6 evidence records these PASS checks:

```text
python3 -m unittest tests.test_workflow_core_normal_entry_reliability
/usr/bin/python3 -m unittest tests.test_standalone_skill_baselines tests.test_codex_marketplace tests.test_central_plugin_icon_assets tests.test_candidate_plugin_replay tests.test_workflow_core_reviewed_handoff_routing
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
mkdir -p .local-runtime/mplconfig && MPLCONFIGDIR=.local-runtime/mplconfig python3 -m unittest discover -s tests
git diff --check
```

The broad `unittest discover` run passed 322 tests on the default Longleaf
runtime with `MPLCONFIGDIR=.local-runtime/mplconfig`.

## Remote Broad CI

Required remote workflow:

```text
.github/workflows/codex-marketplace.yml
```

Observed PASS runs:

- <https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/36984481687>
  - event: `workflow_dispatch`
  - head SHA: `877073bd47eba14bf4277de6b951015377368834`
  - conclusion: `success`
- <https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/36964684181>
  - head SHA: `331f2d155ff5bad015fb278dcd884ceb39a363e6`
  - conclusion: `success`
- <https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/36964897892>
  - head SHA: `4b6cd5e301f35ae68c731f377f3c011c5e89efba`
  - conclusion: `success`

The workflow jobs include:

- `codex-marketplace`
- `windows-sparse-checkout`
- `editable-install-smoke (ubuntu-latest)`
- `editable-install-smoke (windows-latest)`

If this evidence file or the Final Critic handoff file is committed after the
listed runs, the final Critic must verify the latest branch `HEAD` with:

```text
gh run list --workflow codex-marketplace.yml --branch work/workflow-core--normal-entry-reliability --limit 5 --json databaseId,status,conclusion,headSha,url,event
```

The required condition is a `workflow_dispatch` run whose `headSha` equals the
current evidence HEAD and whose `conclusion` is `success`.
