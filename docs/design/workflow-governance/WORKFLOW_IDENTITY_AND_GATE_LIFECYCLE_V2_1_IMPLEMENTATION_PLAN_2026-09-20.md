# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Implementation Plan v2.1

- Execution package version: `v2.1`
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Approved design: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md` v2.1
- Approved design commit: `ba2fc85f9c58b9b332eb07f821d1756b417fe1d1`
- Design Critic PASS: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_CRITIC_REVIEW_2026-09-20.md`
- Design Critic PASS commit: `1427c7060776719e2e1ae191b681ab2e1a608705`
- AI_Skills planning baseline: `YuukiAS/AI_Skills_Collection main@1427c7060776719e2e1ae191b681ab2e1a608705`
- Bridge planning baseline: `YuukiAS/GPT_Codex_AI_Bridge_Kit main@afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Execution branch/worktree: **not created; Critic PASS + user-sent approved Kickoff required**
- Paid API: **not authorized / not required**
- This Plan does not itself authorize execution, branch/worktree creation, production mutation, merge, release, deployment, or paid model calls.

## 1. Positive completion

本轮不是再设计一套 workflow，也不是把 0xx 换成更复杂的编号体系。真正完成后，用户应得到两项可直接感知的改进。

第一，新 workflow 的机器身份不再依赖 `055/056/057` 这种创建顺序。Bridge Kit 的正常 Reviewed Handoff 新任务入口接受 semantic task key，并且旧 numbered task 继续原样可读、可验证、可运行。technical key 只负责 branch/path/evidence 的稳定定位。

第二，AI_Skills 的插件回归机制从“Gate 随真实失败越长越多”收敛为：**Gate taxonomy 相对稳定，真实 regression bank 持续增长；release 根据风险选择验证深度，但 shared/cross-cutting/impact 不确定时必须 broad/full fallback。** 普通用户看到的是简短的人类名称，不需要反复解析 technical key、scope token、owner 或内部状态。

完成必须由真实 normal entry、最终 candidate、生成层、插件 replay 与独立审查共同证明；“文档写了新规则”或“regex/unit tests 绿了”都不等于完成。

## 2. Non-substitutable semantics

以下语义不可在执行中被“简化”为低质量替代：

1. **semantic new creation，legacy validation dual-format**：新的 canonical task creation 只接受 semantic key；已有 numbered task 不 rename、不 migrate，generic/existing-workspace validation 继续接受 legacy + semantic。
2. **technical task key != human label**：technical key 只用于稳定机器 locator；可控的 prompt、Goal、review/report heading 和普通交流默认使用短的人类名称。不得新增 task `display_name` schema、registry、title service 或第二套 identity mapping。
3. **scope precedence 不改写**：AI_Skills semantic scope 先按 mutable canonical repo 数量，再按 plugin scope；read-only reference 不计入。Bridge 只校验 lexical syntax，不理解 `cross-repo` / plugin registry。
4. **same-final-candidate 不削弱**：release-critical Gate 的直接证据必须来自同一 exact final candidate；本 cross-repo task 使用冻结的 AI_Skills + Bridge candidate tuple。
5. **risk-based selection 不是免测机制**：本任务本身修改 task creation/validation、shared workflow policy 和 production plugin consumer，属于 cross-cutting normal-entry change，故本轮 release selection 预先分类为 **BROAD_FULL_FALLBACK**，不得临时降为 narrow。
6. **Gate lifecycle 不成为第二套 eval framework**：Capability Gate taxonomy、regression bank、release selection 只是现有 policy/Plan 语义，不新增 registry/database/ledger/state。
7. **domain ownership 不移动**：workflow-core 负责流程；AI Skills Maintainer 负责 maintenance closure；领域 plugin 保留写作、PPT、统计、影像、生信等专业判断。本任务不修改任何领域 plugin 的专业行为。
8. **不控制平台自动标题**：只约束 repo/workflow 能控制的文字；不得为 ChatGPT/Codex sidebar/conversation auto-title 增加 API、hack 或 service。

## 3. Current source and version reality

### 3.1 AI_Skills_Collection

Planning baseline:

`main@1427c7060776719e2e1ae191b681ab2e1a608705`

Current release identity:

```text
Repository / CLI: 5.0.5
workflow-core:    0.1
ai-skills-core:  0.2
writing-style:   0.3
presentations:   0.3
web-development: 0.1
```

Relevant source authority:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/task-template.md`
- `skills/core/codex-system/codex-workflow-protocol/references/verification-matrix.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- `scripts/codex_marketplace_config.json`
- affected plugin changelogs / TODOs and existing generator/tests.

Current workflow-core reference still shows the legacy authoring form `task_key: <id>_<short_slug>`; this is a real consumer surface to align after Bridge provides the canonical lexical contract. workflow-core must not implement its own parser.

### 3.2 GPT_Codex_AI_Bridge_Kit

Planning baseline:

`main@afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`

Current source version:

`0.8.3`

Current production reality:

- `ai_bridge_kit/reviewed_handoff.py` hard-codes numeric `TASK_KEY_RE` and canonical `init_task()` rejects non-numbered keys;
- `ai_bridge_kit/cli.py` generic workspace validation has the same numeric grammar;
- `scripts/validate_handoff_workspace.py` has the same numeric grammar;
- Text Review and Visual Review propagate `task_key` through result paths and equality checks rather than defining a separate scope taxonomy;
- Review branch convention is `reviewed/<task_key>`;
- current docs/templates still teach numbered task authoring in several normal-entry surfaces.

Bridge is therefore the lexical/compatibility owner. AI_Skills must not fork this parser.

### 3.3 Overlap with historical 056

Current `056 Product Delivery Discipline` package is still not execution-ready in the source inspected for this Plan: its review package records `RESULT=REVISE` / `READY_FOR_CODEX=NO`. It overlaps `workflow-core`, `ai-skills-core` and Bridge.

Therefore these two changes must **not** execute concurrently against the same shared production source.

Execution preflight rule:

- if 056 remains unexecuted and the version/source tuple below is unchanged, this package may proceed after execution-ready Critic PASS and user authorization;
- if 056 or another task has meanwhile changed/integrated any affected AI_Skills/Bridge production surface or consumed the planned version slots, stop before mutation and return to Planner for bounded source-drift/version amendment;
- do not silently rebase semantic decisions, merge two packages, or auto-increment version numbers.

If this package executes first, 056 must later revalidate against the new canonical main; this package does not modify 056 files.

## 4. Exact future execution identity and authorization target

Only after execution-ready Critic PASS and the user sends the approved Kickoff:

### AI_Skills_Collection

- technical branch: `reviewed/cross-repo--workflow-identity-gate-lifecycle`
- preferred task-owned worktree: `/tmp/ai-skills-workflow-identity-gate-lifecycle`
- base: kickoff-time `origin/main` only if the approved package and expected source/version tuple remain compatible.

### GPT_Codex_AI_Bridge_Kit

- technical branch: `reviewed/cross-repo--workflow-identity-gate-lifecycle`
- preferred task-owned worktree: `/tmp/bridge-workflow-identity-gate-lifecycle`
- base: kickoff-time `origin/main` only if the expected Bridge source/version tuple remains compatible.

The `/tmp` paths are disposable Git worktree locations only. Any evidence/artifact needed for review or handoff must be written into the appropriate repository, normally under `results/cross-repo--workflow-identity-gate-lifecycle/` or an existing canonical repo path. Final evidence must not exist only under `/tmp`.

### Cutover bootstrap exception

This implementation is the task that introduces semantic canonical task creation, so it cannot truthfully bootstrap its own control object through the pre-change Bridge `reviewed-handoff task init`, which currently rejects semantic keys.

Therefore:

- do **not** create a legacy-numbered successor merely to implement the cutover;
- do **not** manually forge a semantic Reviewed Handoff `CURRENT.json` before the candidate supports it;
- the Critic-approved Plan/Goal/Kickoff + exact semantic Git branches are the execution contract for this cutover implementation;
- after the Bridge candidate implements semantic creation, G1/G4 normal-entry acceptance must use that candidate CLI in isolated temporary fixture repositories;
- the first ordinary production workflow created through the new semantic normal entry occurs after integration/release, not retroactively for this bootstrap task.

This is a one-time cutover boundary, not a new workflow mode or permanent exception.

## 5. Implementation scope — Bridge Kit

Bridge changes are limited to lexical syntax, legacy compatibility, canonical creation, generic validation and propagation.

### 5.1 One canonical lexical authority

Introduce one small canonical Bridge helper/module or equivalent single authority for task-key lexical validation. It must distinguish:

- legacy numbered key: accepted only where historical/existing validation is legal;
- semantic key: accepted for new creation and validation.

Semantic lexical requirements remain generic and Bridge-owned only:

- exactly one `--` separator between scope token and goal token;
- both components lowercase kebab-case;
- no empty component / malformed separator;
- bounded practical total length consistent with the approved design;
- reject Git/path-hostile forms;
- Bridge does **not** validate AI_Skills plugin slug, mutable repo count, or `cross-repo` business semantics.

Do not create a registry, key database, collision ledger or AI_Skills dependency.

### 5.2 Canonical Reviewed Handoff creation

Update `ai_bridge_kit/reviewed_handoff.py` so canonical new task creation:

- accepts valid semantic keys;
- rejects new legacy numeric keys after cutover;
- fails closed when task identity already exists;
- continues to generate task/result paths and optional text/visual evidence paths from the exact semantic key without truncation/remapping.

Do not change Review roles, state graph, CURRENT schema, review rounds or Plan schema for this feature.

### 5.3 Generic/existing workspace validation

Update:

- `ai_bridge_kit/cli.py`
- `scripts/validate_handoff_workspace.py`

to consume the canonical dual-format validator rather than carrying independent numeric regex semantics.

Validation must accept:

- existing valid legacy numbered identities;
- valid semantic identities;
- both in the same workspace.

Validation must reject malformed semantic keys, but must not guess from file timestamps whether an out-of-band numeric file is “old enough”. New numeric creation is blocked at canonical creation.

### 5.4 Propagation surfaces

Verify and, only where needed, repair semantic-key-safe propagation through existing consumers:

- `automation/reviewed_handoff/tasks/<task_key>/`
- `results/<task_key>/`
- `reviewed/<task_key>`
- CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT
- task-bound Planner / Reviewer / Executor paths
- `ai_bridge_kit/reviewed_runner.py`
- Text Review manifest/evidence paths and task-key equality
- Visual Review manifest/evidence paths and task-key equality.

Do not create a second identity field.

### 5.5 Normal authoring guidance

Update the minimum Bridge authoring/docs/templates that currently teach new numeric task creation so future normal entry uses semantic task keys.

At minimum inspect and align as applicable:

- `README.md` Reviewed Handoff task-init example;
- `QUICKSTART.md`;
- `templates/prompts/AGENT_RULES.md`;
- `templates/prompts/templates/TASK_TEMPLATE.md`;
- `chatgpt/GITHUB_MCP_REPO_INSTRUCTIONS.md`;
- relevant Review README/prompts/docs that explain task keys.

Historical example tasks/files such as `examples/example_project/prompts/tasks/001_structure_audit.md` remain legacy compatibility evidence and are not mass-renamed.

### 5.6 Bridge tests

Focused tests must cover:

- semantic valid / invalid lexical cases;
- canonical semantic task init succeeds;
- canonical numeric task init fails after cutover;
- collision fails closed;
- generic validation accepts legacy + semantic in one workspace;
- task/result directories preserve exact semantic key;
- branch ref form `reviewed/<semantic-key>` is Git-valid;
- CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT identities preserve the key;
- Text Review and Visual Review manifest/evidence paths preserve the key;
- runner / task-bound prompt consumers do not reject/remap the semantic key;
- legacy Reviewed Handoff fixtures remain valid.

Then run the full Bridge unit suite once on the stable candidate.

No real user Host Policy installation, deployment, external paid review, OpenAI Responses/Terra call, or production task creation is required for this feature.

## 6. Implementation scope — AI_Skills_Collection

AI_Skills changes implement the already-approved **semantic meaning and plugin-maintenance policy**, not lexical parsing.

### 6.1 Capability Gate policy

Amend `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` with the approved lifecycle:

- stable Gate taxonomy + growing regression bank;
- new real failure defaults to the existing Gate when capability/evidence/failure semantics match;
- split/new Gate when absorbing the case would change capability/normal-entry/evidence/PASS-FAIL meaning;
- merge/split/retirement requires obligation mapping and does not rewrite historical PASS/FAIL;
- all applicable cheap deterministic known regressions first;
- narrow release selection legal only under the approved isolation conditions;
- mandatory broad/full fallback for the approved cross-cutting triggers;
- all release-critical Gates retain same-final-candidate direct evidence;
- no fixed fresh/manual/paid sample count;
- no impact registry/dependency DB/ledger.

This policy remains the canonical authority; AI Skills Maintainer consumes it rather than creating a parallel Gate policy.

### 6.2 AI_Skills scope semantics and human-readable naming

Add only the minimum high-level consumer rules to `AGENTS.md` and Planner/Critic contracts needed for future work:

- mutually exclusive scope precedence:
  1. multiple mutable canonical repos -> `cross-repo`;
  2. one mutable AI_Skills repo + multiple central production plugins -> `cross-plugin`;
  3. one production plugin -> `plugin-<canonical-plugin-slug>`;
  4. single repo non-plugin-wide -> `repo`;
- read-only references do not count;
- technical task key belongs in locator blocks/branch/path/evidence;
- controlled user-facing headings/prose default to short human labels;
- frozen single-plugin release may use `Clear Writing 0.4`; unfrozen work uses an outcome phrase;
- broad work may use `开发交付流程完善（AI_Skills + Bridge）`;
- do not add a task/workflow `display_name` field/registry/title service;
- do not claim control of client auto-generated conversation/sidebar titles.

Do not duplicate the full Gate policy into every prompt.

### 6.3 workflow-core / Verified Workflow

Update the source `codex-workflow-protocol` and the smallest relevant references so workflow-core can **execute** the approved release-selection semantics:

- identify affected release-critical Gates from the frozen Plan;
- require applicable cheap deterministic regression bank first;
- apply narrow only when isolation is explainable;
- force broad/full on the approved shared/cross-cutting/uncertain triggers;
- keep same-final-candidate evidence;
- preserve should-not-change behavior;
- keep human-readable labels in normal user-facing reporting;
- route domain correctness to the target plugin.

Update the reusable task template away from mandatory `<id>_<short_slug>` authoring and refer to the canonical Bridge task-key contract rather than implementing a local regex.

workflow-core must not become a second parser.

### 6.4 AI Skills Maintainer

Update `ai-skills-repository-maintainer/SKILL.md` minimally so maintenance closure:

- applies the AI_Skills scope precedence;
- maps new real failures into existing Gate regression banks before proposing new Gates;
- detects when a Gate split/new design review is actually necessary;
- applies the approved narrow/broad release selection;
- preserves version/changelog/source/generated/replay closure;
- uses short human labels in controlled prose while keeping technical keys as locators;
- continues to defer domain correctness to the target plugin.

Do not create another Gate taxonomy, state machine or task-key parser.

### 6.5 Generated layer and parity

After source changes:

- regenerate canonical registry/catalog/Marketplace/plugin payloads with existing generators;
- verify generated `workflow-core` and `ai-skills-core` consume the updated source;
- do not hand-edit `.agents/plugins/marketplace.json` or `plugins/codex/plugins/`.

No domain plugin production source is modified.

### 6.6 AI_Skills tests

Add/adjust focused tests for:

- source/generated parity of changed workflow-core and ai-skills-core behavior;
- scope precedence examples, including 056-like two-mutable-repo -> `cross-repo`;
- read-only reference repos not changing scope;
- technical locator vs human-readable label convention in controlled prompts/headings;
- no new task/workflow `display_name` schema/registry/title service;
- Gate lifecycle existing-gate vs genuinely-new-capability cases;
- narrow selection allowed only for explainably isolated changes;
- each mandatory broad/full trigger;
- same-final-candidate and cheap deterministic bank requirements;
- no second parser / no new registry-ledger-state machinery.

Mechanical contract tests prove source/consumer alignment only. They do not substitute for the candidate plugin replay and independent qualitative review below.

Then run the existing canonical generator/validation and full AI_Skills unit suite once on the stable candidate.

## 7. Runtime/normal-entry capability replay

Because AI_Skills production plugin behavior changes, source-text assertions alone are insufficient.

After source + generated layers are stable, allow at most **two public-safe candidate plugin replays** through the existing candidate/production replay path using the current Codex identity. These are not OpenAI Responses/Terra paid-review calls and must not use private user data or external credentials.

### Replay A — Verified Workflow

Give the candidate a compact execution-planning scenario containing:

- one clearly isolated local change;
- one shared prompt/assembly/runtime/router/normal-entry change;
- one unresolved multi-Gate failure;
- a maturity-promotion case.

The candidate must correctly distinguish when narrow is legal and when broad/full fallback is mandatory, preserve same-final-candidate evidence, and not invent fixed paid/fresh sample counts or a new Gate.

### Replay B — AI Skills Maintainer

Give the candidate representative maintenance cases:

- one central plugin in AI_Skills;
- multiple central plugins in only AI_Skills;
- AI_Skills + Bridge both mutable with several product repos read-only;
- a new real failure that belongs under an existing Gate;
- a truly new capability that may require Gate redesign.

It must produce the approved scope semantics, keep the domain owner separate, use a short human-readable label in ordinary prose, keep the technical key as locator, and not implement a second parser/registry/state system.

If either replay reveals a real policy/consumer defect, repair only within the frozen architecture and rerun the affected replay. Do not add more replay cases adaptively to chase a PASS. If fixing it would change architecture/Gates/ownership/recovery semantics, stop and return to Planner/Critic.

## 8. Capability Gate Matrix — execution mapping

The approved G1–G7 remain unchanged.

| Gate | Final-candidate evidence required in this execution |
| --- | --- |
| **G1 Semantic creation & lexical identity** | Candidate Bridge normal-entry `reviewed-handoff task init` in isolated repo succeeds for semantic key; numeric new creation and malformed/collision cases fail closed. |
| **G2 Identity propagation** | Exact semantic key propagates through task/result dirs, branch form, CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT, runner/task-bound consumers, Text Review and Visual Review manifest/evidence fixtures. |
| **G3 Scope clarity** | AI_Skills policy/consumer examples + AI Skills Maintainer candidate replay prove mutually exclusive precedence and 056-like `cross-repo`; Bridge remains lexical-only. |
| **G4 Legacy coexistence & cutover** | Same isolated workspace validates at least one seeded legacy numbered task plus one semantic task; legacy validation stays legal while canonical new numeric creation fails. |
| **G5 Gate lifecycle** | Policy + Maintainer replay classify an existing-capability regression without adding a Gate and contrast it with a genuinely new capability; merge/split/retirement obligation preservation is present. |
| **G6 Release regression safety** | This task itself uses `BROAD_FULL_FALLBACK`; workflow-core replay proves narrow eligibility and all mandatory fallback triggers; exact final candidate tuple owns all release evidence. |
| **G7 No governance bloat** | Diff/review proves no new registry/database/ledger/controller/watcher/state machine/task display-name service/second parser/docs-layout migration; small isolated work remains able to use narrow selection. |

Because this task changes normal entry and shared workflow policy, **all G1–G7 are release-critical for this candidate**.

## 9. Broad/full release verification for this task

This task is pre-classified `BROAD_FULL_FALLBACK`.

Before freezing the candidate tuple:

### Bridge

1. focused semantic/legacy/cutover tests;
2. text/visual/reviewed-runner affected tests;
3. generic workspace validation compatibility tests;
4. full Bridge unit suite;
5. source/docs/version consistency.

### AI_Skills

1. focused workflow identity / Gate lifecycle contract tests;
2. generated/source parity;
3. canonical marketplace generator `--write --validate --check --path-report`;
4. `scripts/skills.py validate`;
5. `scripts/skills.py audit --all`;
6. affected plugin/repository version/changelog consistency;
7. full `python -m unittest discover -s tests`;
8. the two bounded candidate plugin replays.

No paid external review is required by the approved design. No fixed fresh/manual sample count is introduced.

## 10. Final candidate tuple and change freeze

After all production source, generated payload and candidate version metadata are stable, record:

```text
AI_SKILLS_FINAL_CANDIDATE_COMMIT=<sha>
BRIDGE_FINAL_CANDIDATE_COMMIT=<sha>
```

Together these form one **cross-repo final candidate tuple**.

All G1–G7 release-critical evidence in the pre-integration review must bind this exact tuple.

After tuple freeze:

- control/evidence-only files may be appended if they do not affect production behavior, generated payload, versions, rubric or tested normal entry;
- any production/source/generated/version/acceptance-semantic change in either repo invalidates the tuple and requires the affected evidence to be regenerated and the candidate re-reviewed;
- do not stitch Bridge evidence from one candidate with AI_Skills evidence from another.

## 11. Version and release decision

The current planning baseline supports the following candidate slots **only if unchanged at kickoff preflight**.

### AI_Skills_Collection

```text
Repository bump decision: PATCH
Reason: compatible repository/workflow improvement; no new top-level plugin or breaking install contract.

Affected plugins:
- workflow-core: 0.1 -> 0.2
  Reason: production workflow behavior gains the approved Gate lifecycle/release-selection execution semantics and human-readable naming discipline.
- ai-skills-core: 0.2 -> 0.3
  Reason: production maintenance behavior gains scope semantics, regression-bank lifecycle application and release-selection closure.
- all other plugins: NO_BUMP
  Reason: no production behavior change in this task.
```

Repository candidate slot:

`5.0.5 -> 5.0.6`

The implementation task must update the two affected plugin changelogs and repository release metadata consistently when the actual release candidate is formed. Do not bump `web-development`, writing, presentations, statistics, bioinformatics or medical-imaging.

### Bridge Kit

Current `0.8.3` -> next compatible candidate `0.8.4`, because semantic/legacy task-key creation/validation is a user-visible compatible workflow improvement.

Update Bridge `pyproject.toml`, changelog and normal version surfaces consistently when the candidate is formed.

### Stale-slot rule

If either repo's relevant source/version changes before kickoff, or another task consumes any planned slot, these version decisions are stale. Executor must not invent `5.0.7`, `workflow-core 0.3`, `ai-skills-core 0.4` or Bridge `0.8.5`; stop before production mutation and return to Planner for bounded revalidation.

## 12. Human-readable naming acceptance

Representative controlled surfaces must demonstrate the approved separation.

For example:

```text
Human-facing: 工作流命名与插件回归机制完善（AI_Skills + Bridge）
Technical locator: cross-repo--workflow-identity-gate-lifecycle
```

For a frozen single-plugin release:

```text
Clear Writing 0.4
Presentations 0.3
```

For unfrozen work:

```text
Clear Writing 发布收口
```

Acceptance fails if normal user-facing headings are dominated by raw `cross-repo--...`, internal state strings or owner lists when those are not needed for navigation.

Acceptance does **not** require control over ChatGPT/Codex automatically generated sidebar/conversation titles.

## 13. Recovery and failure attribution

### 13.1 Source/version drift before mutation

If affected source or version identity has materially drifted, stop and return to Planner. Do not merge in 056, rebase the approved package, or choose new versions autonomously.

### 13.2 Ordinary implementation/test failure

Within frozen scope, Executor may repair code/tests/docs and rerun affected development regressions. This does not require another architecture review.

### 13.3 Propagation failure

If one Bridge consumer still rejects/remaps semantic keys, treat it as G2 implementation defect and repair that existing consumer. Do not add a second identity field or registry.

### 13.4 Legacy compatibility failure

If old numbered tasks stop validating, treat it as G4 product regression. Repair dual-format validation; do not migrate history.

### 13.5 Candidate replay failure

First attribute to:

- policy/source omission;
- generated payload parity/loading;
- stale candidate install;
- prompt/consumer behavior;
- incorrect fixture expectation.

Repair within approved design. If the only proposed fix changes Gate taxonomy, ownership, parser responsibility, state machine or recovery semantics, stop and return to Planner/Critic.

### 13.6 Unrelated full-suite failure

Record and attribute. Do not absorb unrelated product work merely to turn CI green. If the failure is caused by this candidate, repair it; if truly unrelated and release-blocking under current repo policy, report the blocker truthfully.

### 13.7 No blind retries / no adaptive evidence chasing

Do not add more fresh/replay examples after seeing failures merely to find a winner. Known regression cases may be rerun after a valid repair; candidate identity/evidence history stays truthful.

## 14. Independent review and integration boundary

This execution package authorizes implementation-candidate preparation only after Critic PASS + user-sent Kickoff.

Executor must stop after:

- both task branches contain the complete candidate;
- required tests/replays/evidence are committed and pushed;
- final candidate tuple is recorded;
- remote branch tips are verified;
- no forbidden side effect occurred.

Then hand off for independent implementation/pre-integration review of the exact tuple.

No main merge, release/tag/package publication, Host install, deployment, branch deletion or paid review is authorized by this Kickoff.

A later integration/release step may proceed only after the required independent review confirms the exact tuple and the user authorizes any integration boundary required by the then-current contract.

## 15. Explicit out of scope

Do not:

- rename or migrate 001–057 or any historical task/result/branch/evidence;
- create a successor merely for naming;
- modify 056 Plan/Goal/Kickoff/source;
- add a second task-key parser in workflow-core or AI_Skills;
- add task `display_name` schema/registry/title service;
- add controller/watcher/database/registry/ledger/state machine;
- reorganize `docs/design/`, `docs/goals/` or prompt directories;
- modify domain-plugin professional behavior;
- change Bridge Review roles/states/schema because of this task;
- control/hack ChatGPT/Codex client auto-title;
- call Terra/OpenAI Responses or any paid external review API;
- use private user data in candidate replay;
- create PRs, force-push, rewrite history, modify remotes, merge to main, tag/release/publish/deploy under this Kickoff.

## 16. Execution-stage completion report

The Executor handoff must start with natural Chinese and use the human-readable task name, then provide a compact technical appendix.

It must report:

- what changed for ordinary users;
- semantic new creation vs legacy coexistence;
- Gate lifecycle / regression bank / broad-full behavior;
- human label vs technical locator behavior;
- exact AI_Skills + Bridge candidate SHAs;
- version candidate decisions;
- G1–G7 evidence map;
- focused/full test results;
- candidate plugin replay results;
- source/generated parity;
- any skipped/unavailable check and why;
- forbidden actions confirmed not performed;
- next owner: independent implementation/pre-integration review.

It must not claim overall release/production completion merely because implementation branches pass tests.
