# G4 Normal Entry Trace

Final candidate commit: `671eb532e0ec949dc7889427379a1113cf7a6ea9`
Run id: `20261002T075939Z-1343181`
Status: `PASS`

Command:

```text
python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g4_candidate_replay_task_v2.md --input results/workflow-core--normal-entry-reliability/g4_capability_discovery_input_v2.md
```

Replay identity:

- plugin id: `workflow-core@ai-skills-candidate`
- plugin version: `0.5`
- runtime: `codex-cli 0.153.4`
- actual consumption: `proven=true`, event `item.started`, line `9`

Final Critic repair:

- ordinary prompt does not name workflow-core;
- child actually reads the candidate workflow skill;
- child actually consumes the PDF specialist instructions and the Chinese math
  PDF specialist instructions;
- child runs project/specialist probes and bases the route decision on their
  outputs;
- default PATH absence is not treated as capability absence;
- no non-equivalent HTML/PNG/screenshot fallback is executed;
- true absent contrast is recorded separately under
  `g4_absent_contrast_raw/` using a controlled closed-world fixture whose
  canonical, specialist, and project-declared routes are all probed.

Observed probes:

- project probe:
  `python3 results/workflow-core--normal-entry-reliability/g4_probe_project/tools/pdf_capability_probe.py outputs/g4_probe`
- specialist environment probe:
  `python3 /users/a/e/aereinh/.codex/skills/tools-documents-media-render-chinese-math-pdf/scripts/probe_pdf_render_env.py --root . --pretty > outputs/g4_render_env.json`

Probe facts:

- `g4_probe/probe.json` records `default_path.xelatex=/usr/bin/xelatex` and
  `default_path.typst=null`;
- `project_probe.minimal_pdf_writer.available=true`;
- `g4_probe/minimal_probe.pdf` exists with SHA-256
  `651c1d5beb8810f5442741b99bc878e2dc218f470838655cc38c1397f5925bae`;
- `g4_render_env.json` records Pandoc, XeLaTeX, LuaLaTeX, `pdfinfo`,
  `pdftotext`, `pdffonts`, `pdftoppm`, fontconfig, and local Chinese math
  render resources;
- `absent_contrast.definitely_missing_renderer=null` is from an actual
  nonexistent-renderer probe.

Tracked evidence:

| File | SHA256 |
|---|---|
| `g4_candidate_replay_task_v2.md` | `0afc12a9189c49aaef98c03c0dbb6979e59730c6b5197dd122e04d28c10b72b9` |
| `g4_capability_discovery_input_v2.md` | `4e23c5ef4d99d9ffad2c3d77721908dbb6004c8a7f79f72047a8cf84fa557921` |
| `g4_candidate_replay_raw_v2/run.json` | `355dd9da7282753ff8604730604f88aaa208b9a46fbe76a0e1563494217a24c8` |
| `g4_candidate_replay_raw_v2/plugin-add.json` | `c61246482d14ff4186eb92f8747bf14af1c2a8e80ae2c37c044114c2a1e0d037` |
| `g4_candidate_replay_raw_v2/child.stdout.jsonl` | `8e1a3a760f8805628f38892ffce55b3aeeec80f6e990069cfd6a369791c00cdf` |
| `g4_candidate_replay_raw_v2/g4_normal_entry_decision.md` | `25434e4f05001f12852c7e8af70203358026f69d806f4d35c421eac57d9ad748` |
| `g4_candidate_replay_raw_v2/g4_probe/probe.json` | `8d68b5f570df738cd42e0a1ec93ebdcae927cc1b11d200c93ed661cd1f49e824` |
| `g4_candidate_replay_raw_v2/g4_probe/minimal_probe.pdf` | `651c1d5beb8810f5442741b99bc878e2dc218f470838655cc38c1397f5925bae` |
| `g4_candidate_replay_raw_v2/g4_render_env.json` | `904d3f878338d025cdbb637f8b84f6e7db3375b8b708b7dd4be76d4807fa86ad` |

Decision summary:

- discovered local PDF capabilities are sufficient to keep PDF identity and a
  specialist route;
- the minimal byte-writer PDF is only diagnostic, not the delivery route;
- Chromium/HTML/PNG are not selected as equivalent fallback;
- full artifact rendering remains out of scope for this Gate and is not claimed.

## True Capability-Absent Contrast

Command:

```text
python3 results/workflow-core--normal-entry-reliability/tools/replay_observer.py --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --plugin workflow-core --expect-consumed workflow-core --task results/workflow-core--normal-entry-reliability/g4_absent_contrast_task.md --input results/workflow-core--normal-entry-reliability/g4_absent_contrast_input.md --writable-dir results/workflow-core--normal-entry-reliability/g4_absent_fixture --copy-run-to results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw --label g4-absent-contrast
```

Replay identity:

- plugin id: `workflow-core@ai-skills-candidate`
- plugin version: `0.5`
- runtime: `codex-cli 0.153.4`
- actual consumption: `proven=true`, event `item.started`, line `6`
- observer expectation failures: `missing=[]`, `unexpected=[]`

Controlled fixture:

- fixture contract:
  `g4_absent_fixture/.ai-skills/capability-contract.md`;
- declared legal routes:
  canonical task route, matched specialist route, and project-declared runtime
  route;
- safe probe:
  `g4_absent_fixture/tools/capability_absent_probe.py`.

Observed absent result:

- declared route count: `3`;
- usable route count: `0`;
- canonical task route usable: `false`;
- matched specialist route usable: `false`;
- project-declared runtime route usable: `false`;
- final status: `blocked_target_not_met`;
- dependency classification: `UNSUPPORTED_WITH_EVIDENCE`;
- user decision required: `false`;
- undeclared fallback attempted: `false`;
- replacement artifact produced: `false`;
- PDF artifact completed: `false`.

Trace boundary:

- the child read the candidate workflow skill and PDF specialist skill;
- the child read only the fixture contract/probe and workspace inputs/outputs
  for the absent decision;
- the child did not run Node, Chromium, browser print, screenshot, host PATH
  exploration, unrelated home/overflow filesystem search, network access, or a
  non-equivalent artifact fallback;
- the contrast is not a single made-up executable check: the probe checks all
  three fixture-declared legal route classes.

Absent contrast evidence:

| File | SHA256 |
|---|---|
| `g4_absent_contrast_task.md` | `a998455f3f23eeb7b65db151e9f64c4cccada8b60b0a7f9b53517611af497c1a` |
| `g4_absent_contrast_input.md` | `2b402a77b79d16334deef2dfc9a6e49d53455221e9bf2d1ec4cf8669446416ff` |
| `g4_absent_fixture/.ai-skills/capability-contract.md` | `34de7a817f087d2bee29a5deed83c2412948d743732d98a773c1dccf0e9224b4` |
| `g4_absent_fixture/tools/capability_absent_probe.py` | `bc25d1be10e929c0187f0ff694cd720807b33c32def72b02a5e3bc7796eefc02` |
| `g4_absent_contrast_raw/run.json` | `9ecb1eaf4e6f1bf07f9fccaf171df1d014c93d12260dda9c5efb704b6e640604` |
| `g4_absent_contrast_raw/child.stdout.jsonl` | `052053476641eb008cfda9e01775e7f63aa3ccf4e226dd2b69a34ec01485fa3e` |
| `g4_absent_contrast_raw/workspace/outputs/absent_probe/capability_report.json` | `3f0eb22601aebe7757974c04b76bf7534ecfec209c646153ec43794dd2aaad2f` |
| `g4_absent_contrast_raw/workspace/outputs/g4_absent_contrast_decision.md` | `c7bfb04feafc5d1d591a63448a12281fac814189ec94ac0866620a78355f23bc` |
| `g4_absent_contrast_raw/workspace/outputs/g4_absent_contrast_manifest.json` | `45e92f798808da68d3ea73fb5f8fd907e5f0e8b061df9d1f9311a5f090b6d2f7` |
