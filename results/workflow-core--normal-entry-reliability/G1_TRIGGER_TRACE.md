# G1 Trigger Replay Trace

Final candidate commit: `671eb532e0ec949dc7889427379a1113cf7a6ea9`
Product version: `workflow-core 0.5`
Repository version: `5.4.1`
Status: `PASS`

This evidence repairs the Final Critic G1 concern by using production-compatible
candidate replay traces instead of relying only on source grep, trigger JSON, or
unit-test string assertions.

## Positive A: Implicit Workflow-Level Trigger

Command:

```text
python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g1_positive_implicit_task.md --input results/workflow-core--normal-entry-reliability/g1_positive_implicit_input.md
```

Result:

- ordinary prompt; it does not say "use workflow-core" or "use process skill";
- candidate identity: `workflow-core@ai-skills-candidate`, version `0.5`;
- actual consumption: `proven=true`, event `item.started`, line `7`;
- raw trace: `g1_positive_implicit_raw/`.

Key hashes:

| File | SHA256 |
|---|---|
| `g1_positive_implicit_task.md` | `0170e683a656be89a3657cecb80cf051824f6b6051cc75118b2ed7642077858d` |
| `g1_positive_implicit_input.md` | `0e1ab5e6b488b159656502f428d51355d06f225fcd78626e2d730405508f727e` |
| `g1_positive_implicit_raw/run.json` | `e38e15c4fd63608a2a2dd570fd042a4b16115cd14eaa01eec56a3185a05e19b6` |
| `g1_positive_implicit_raw/child.stdout.jsonl` | `e1ebb412e68f928a1da533be74ec3ca3643251d495f7b37e7a6ae56673072a74` |

## Positive B: Contextual Workflow Trigger

Command:

```text
python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --task results/workflow-core--normal-entry-reliability/g1_positive_contextual_task.md --input results/workflow-core--normal-entry-reliability/g1_positive_contextual_input.md
```

Result:

- contextual prompt asks for bounded execution across task evidence, branch
  publication, CI, and handoff state; it does not name workflow-core;
- candidate identity: `workflow-core@ai-skills-candidate`, version `0.5`;
- actual consumption: `proven=true`, event `item.started`, line `7`;
- raw trace: `g1_positive_contextual_raw/`.

Key hashes:

| File | SHA256 |
|---|---|
| `g1_positive_contextual_task.md` | `6ad5d856a79f78875c2db692dcb60aff0f8735eca31afdc99df632ca4d2c4c69` |
| `g1_positive_contextual_input.md` | `1854fbb0bd78b72bf67866db27052b6c474be558670b4b5d3369492bef9e6a96` |
| `g1_positive_contextual_raw/run.json` | `93a5e5b261c8d28a4634b4488f3e178480c71e588914b6f98f7db94160d85e7e` |
| `g1_positive_contextual_raw/child.stdout.jsonl` | `36e09d3e7d61479a996166254fecf10861a39fbe741315f46839f90b64b76324` |

## Negative C: Complex Specialist-Contained Hard Negative

Command:

```text
python3 results/workflow-core--normal-entry-reliability/tools/replay_observer.py --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --plugin workflow-core --plugin writing-style --expect-consumed writing-style --expect-not-consumed workflow-core --task results/workflow-core--normal-entry-reliability/g1_hard_negative_task.md --input results/workflow-core--normal-entry-reliability/g1_hard_negative_input.md --copy-run-to results/workflow-core--normal-entry-reliability/g1_hard_negative_raw --label g1-hard-negative
```

Result:

- complex writing/editing task remains specialist-contained;
- `workflow-core@ai-skills-candidate` is installed and discoverable, but
  `actual_consumption=null`;
- correct specialist is consumed:
  `writing-style@ai-skills-candidate`, version `0.4`, `proven=true`,
  event `item.started`, line `5`;
- observer expectation failures: `missing=[]`, `unexpected=[]`;
- raw trace: `g1_hard_negative_raw/`.

Key hashes:

| File | SHA256 |
|---|---|
| `g1_hard_negative_task.md` | `035dfcfef0fb0d747363ee7908235db094b8c496427023bb2142b9882d58ecd9` |
| `g1_hard_negative_input.md` | `3bfbaac85dc74fc6b702d727edaba62ea82e2657a48799e7fa9de65687b79b41` |
| `g1_hard_negative_raw/run.json` | `3a1c66f58825c9ea823bf9300cfe8fc5dc6f797418e3dc987a6b4267c2a84745` |
| `g1_hard_negative_raw/child.stdout.jsonl` | `87dc08d16ee71f9e921b656d432bc53c4757034d579671e8a45f34a0e6316b3d` |

## Negative D: Simple Negative

Command:

```text
python3 results/workflow-core--normal-entry-reliability/tools/replay_observer.py --candidate-commit 671eb532e0ec949dc7889427379a1113cf7a6ea9 --plugin workflow-core --expect-not-consumed workflow-core --task results/workflow-core--normal-entry-reliability/g1_simple_negative_task.md --input results/workflow-core--normal-entry-reliability/g1_simple_negative_input.md --copy-run-to results/workflow-core--normal-entry-reliability/g1_simple_negative_raw --label g1-simple-negative
```

Result:

- simple local summarization request does not trigger workflow-core;
- `workflow-core@ai-skills-candidate` is installed and discoverable, but
  `actual_consumption=null`;
- observer expectation failures: `missing=[]`, `unexpected=[]`;
- raw trace: `g1_simple_negative_raw/`.

Key hashes:

| File | SHA256 |
|---|---|
| `g1_simple_negative_task.md` | `109358b8e2672b5bfc11727718208e9051c19b0adc06132644cebb755ea981e4` |
| `g1_simple_negative_input.md` | `24d46a1ceae797099d69b0801cb7ddd729d7f900e2b50802cfc1aa243044b799` |
| `g1_simple_negative_raw/run.json` | `73602bb6db53a953b991afd022f74a7f5e44e0d5dbe6fbb4de686b17df103d2d` |
| `g1_simple_negative_raw/child.stdout.jsonl` | `db772c006a96cce70b1061dd6137cf235827512748b2b6f27eb204038d7a843a` |

## Boundary

This evidence changes only tracked replay inputs, observer output, and result
documentation. It does not modify production workflow-core source, generated
Marketplace payload, version metadata, release metadata, or the frozen trigger
criterion.
