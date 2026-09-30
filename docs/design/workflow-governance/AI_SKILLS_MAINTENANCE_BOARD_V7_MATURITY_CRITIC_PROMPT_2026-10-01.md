# AI Skills Maintenance Board — Issue Maturity v7 Critic Prompt

你是 AI Research Stack 的独立 Critic thread。

当前只审 Maintenance Board v7 的 GitHub Issues 成熟化设计。不要实现 labels/forms/Actions，不修改 Issues/Project/.github/source，不启动 Codex，不执行 machine adaptation。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-issue-maturity
human_label = Maintenance Board Issues 成熟化
source_branch_or_ref = main
review_stage = MATURITY_DESIGN_REVIEW
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md v7
proposal_commit = 3d091421c7afe8d4f90687ef6e0ce2686bcaf426
execution_branch/worktree = NONE
```

## Prerequisite approved semantics

v6.1 Proposal:

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md`

v6.1 Proposal commit:

`515c42623c55f368eb84a1628839459afa909c09`

v6.1 Critic PASS:

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md`

v6.1 review commit:

`7566eb5726e92c4aff813e11b0d7addbf9852e6b`

Do not reopen v6.1 required-consumer selection semantics.

## 必须先实际读取 latest main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`
- `TODO.md`
- `docs/plugin-todos/README.md`
- `results/repo--maintenance-board-lifecycle/PROJECT_CONFIG_READBACK.md`
- `results/repo--maintenance-board-lifecycle/PROJECT_SURFACE_READBACK_AFTER_UI_AND_BACKFILL.md`
- `results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

并检查 current `.github` issue-triage相关配置：

- ISSUE_TEMPLATE / forms
- CODEOWNERS
- dependabot
- labeler
- stale
- existing workflows only as needed to understand current automation surface

Representative live Issues 至少复核：

- #4
- #5
- #35
- #63
- #86

## External research required

Independently check a small set of current primary/mature sources:

### GitHub official

- Issue Forms / templates
- labels
- Projects best practices
- native sub-issues
- native issue dependencies
- `actions/labeler`
- `actions/stale`
- CODEOWNERS
- Dependabot

### Mature repositories

- Rust issue triage / triagebot / label taxonomy
- VS Code issue triage
- PyTorch issue labeling / AutoLabel Bot

Use these as comparative evidence, not as requirements to copy.

## Current repo gap asserted by v7

v7 says the lifecycle layer is already mature, but the Issues layer is not:

- Project Status / Area work;
- canonical TODO + `tracking: #N` work;
- current Issues mostly have only `maintenance-track`;
- there are no Issue Forms or issue-triage configs;
- normal GitHub Issues search cannot efficiently answer kind/scope/area questions.

Check that this gap is real and user-visible.

## 1. Source-of-truth architecture

v7 proposes:

| Concern | Source of truth |
|---|---|
| problem/evidence/maturity | canonical TODO entry |
| source -> Issue mapping | source `tracking: #N` |
| lifecycle | Project `Status` |
| primary owner | Project `Area` |
| kind | Issue `kind:*` classification |
| scope | Issue `scope:*` classification |
| Bridge integration | optional Issue `integration:bridge-kit` |
| blocked-by | native GitHub dependency |
| hierarchy | native GitHub sub-issue |

`area:*` labels mirror Project Area for normal Issues search; Project Area wins if drift exists.

No lifecycle labels.

Please judge whether this split actually avoids three sources of truth.

## 2. Proposed label taxonomy

### Admission / pre-admission

- existing `maintenance-track`
- `triage:needed`
- `triage:needs-info`

Triage labels are pre-admission only, not Project lifecycle.

### Kind — exactly one per maintenance-track Issue

- `kind:regression`
- `kind:enhancement`
- `kind:new-capability`
- `kind:governance`

### Scope — exactly one

- `scope:plugin`
- `scope:standalone-skill`
- `scope:repo-workflow`
- `scope:cross-repo`

### Area — exactly one, mirrors Project Area

- workflow-core
- ai-skills-core
- writing-style
- research-writing
- presentations
- scientific-visualization
- web-development
- statistical-modeling
- bioinformatics
- medical-imaging
- standalone-skill
- repo
- cross-plugin

all prefixed `area:`.

### Optional integration

- `integration:bridge-kit`

No `area:bridge-kit`.

Check:

1. taxonomy is sufficiently expressive;
2. it is not too large for this repo;
3. forced exactly-one kind/scope/area is appropriate;
4. `kind:regression` vs enhancement is clear enough;
5. Bridge runtime bugs remain Bridge-owned.

If one category is missing, require the smallest real addition, not a mature-repo label explosion.

## 3. Issue intake

v7 proposes two forms only:

1. existing plugin / standalone-skill real failure
2. new capability proposal

Failure form defaults only:

- `triage:needed`

New capability defaults:

- `triage:needed`
- `kind:new-capability`

Neither adds `maintenance-track`.

Template chooser keeps blank issues enabled.

Planner/maintainer triage then:

- checks canonical TODO / duplicates;
- creates or updates source TODO;
- reuses intake Issue when correct granularity;
- adds exactly one kind/scope/area;
- writes `tracking: #N`;
- only then adds `maintenance-track` and Project TODO.

Check whether this correctly preserves canonical TODO ownership and avoids GitHub Issues becoming a second raw TODO inbox.

Also judge whether `blank_issues_enabled: true` is the right compromise or whether it weakens intake too much.

Do not require forms for Codex/API-created Issues unless there is a real need.

## 4. Hierarchy

v7 selects:

- native dependencies: adopt for real blocked-by relations;
- native sub-issues: use only for a genuine parent maintenance goal with independently meaningful children;
- do not create parent Issues merely to represent an implementation/release batch.

Check whether this stays consistent with:

`Project item = top-level maintenance idea`

and:

`execution task/workflow = evidence, not automatically a lifecycle item`.

If a refinement round aggregating regressions should use another native primitive, explain why without inventing a custom hierarchy database.

## 5. Automation options

v7 compares:

### A — no automation

Rejected because metadata drift is predictable with 60+ open tracked Issues.

### B — GitHub-native forms + one tiny pre-admission Action

Selected.

Action behavior:

- on new Issue;
- if already `maintenance-track`: do nothing;
- otherwise ensure `triage:needed`;
- never add maintenance-track;
- never guess kind/scope/area;
- never close;
- never edit Project Status or TODO source;
- minimum `issues: write` token permission.

Check whether this Action has enough value to justify existing at all.

If Forms alone already guarantee the same normal path and blank Issues are intentionally allowed, consider whether the Action is redundant. Do not keep automation merely because "mature repos have bots."

## 6. Metadata consistency audit

v7 proposes a bounded deterministic audit run by the existing Project-capable maintenance path, checking:

- exactly one kind/scope/area per maintenance-track Issue;
- no triage labels on maintenance-track Issues;
- area label matches Project Area;
- source backlink exists where applicable;
- close state remains compatible with BOARD-01.

It deliberately does **not** add a scheduled Project Action initially, because GitHub Projects v2 Actions commonly require a separate project-scoped token and v7 lacks evidence that a new long-lived secret/schedule is worth it.

Check:

- whether a bounded audit command is enough;
- whether this should be docs-only or a repo helper;
- whether a scheduled Action is actually necessary;
- whether new credentials would be disproportionate.

## 7. PR path labeler

v7 defers `actions/labeler`.

Reason:

- identified gap is Issues;
- PR path mapping is a separate metadata map;
- source/generated/shared paths make area inference non-trivial;
- taxonomy should stabilize first.

Check whether this is the correct defer decision.

If you think PR labeler should be in v7, give direct user-value evidence and a minimal safe path mapping, not "best practice" alone.

## 8. Stale

v7 explicitly rejects stale closing for maintenance-track Issues.

No inactivity-based close may create DONE or not-planned for tracked backlog.

Future stale handling, if ever proposed, must be pre-admission only and exclude maintenance-track.

Check this against `actions/stale` behavior and BOARD-01.

Do not import VS Code's needs-more-info auto-close unless it is safe for this repo's long-lived backlog.

## 9. CODEOWNERS / Dependabot

v7 defers both.

CODEOWNERS:

- only useful when human/team PR ownership or branch protection needs it.

Dependabot:

- dependency/supply-chain concern, not Issue maturity.

Check whether either one has direct Maintenance Board user value today.

Do not add them for maturity optics.

## 10. Migration/backfill

v7 proposes one-time migration across current open **and closed**
`maintenance-track` Issues.

Rules:

- snapshot existing labels + Project Area + open/closed state;
- create taxonomy labels;
- Area label mirrors Project Area;
- scope derives from canonical source/real issue contract;
- kind is semantic Planner/maintainer classification, not keyword/LLM Action;
- preserve Project Status;
- preserve canonical source maturity and `tracking: #N`;
- ambiguous kind -> exception / Planner, not guessed;
- Bridge integration ownership checked explicitly.

Representative expected mappings include #5, #35, #63, #86.

Check whether closed history should be backfilled too or whether that adds cost without enough search value.

## 11. Acceptance / rollback

v7 acceptance requires:

- exactly one kind/scope/area on every maintenance-track Issue;
- area label = Project Area;
- no lifecycle labels;
- no pre-admission triage labels on admitted Issues;
- source maturity/tracking unchanged;
- intake forms do not auto-admit Project;
- tiny Action never closes/admits/classifies;
- no stale close path for maintenance-track;
- real Issues search can answer cross-cutting queries.

Rollback removes only v7 labels/forms/action/relations and must not alter:

- maintenance-track;
- Project Status;
- Project Area;
- source tracking;
- Issue open/closed state solely for rollback.

Check whether rollback is complete.

## 12. Relationship to v6.1

v7 recommends:

```text
DO_NOT_COMBINE_IMPLEMENTATION_BY_DEFAULT
```

Rationale:

- v6.1 fixes a live #4 required-consumer semantic error;
- v7 is a broader new Issue-maturity enhancement;
- combining would delay the bounded #4 correction and move its completion target;
- v7 should get its own tracking/accountability.

Check whether this separation is correct.

If you think one final implementation package is safer, explain exactly why and how it avoids moving #4's goalposts.

## 13. Mature-practice rejection check

Explicitly judge whether v7 is right to NOT copy:

- Rust custom triagebot;
- Rust priority/team/status families;
- VS Code/PyTorch stale/needs-info closure for tracked backlog;
- PyTorch oncall;
- org-level Issue Types;
- PR path labeler now;
- CODEOWNERS now;
- Dependabot now;
- custom hierarchy store.

The standard is user value, not similarity to a famous repo.

## 14. Scope / version

This is design only.

No implementation is authorized.

Likely future changes are maintenance metadata / `.github` intake automation,
not production plugin behavior.

Do not decide final version/gate requirements beyond what evidence supports;
flag if any proposed future file would actually cross production-plugin behavior.

## 15. Output

First provide a natural Chinese assessment covering:

- current gap;
- label SoT design;
- forms;
- hierarchy;
- automation;
- stale;
- CODEOWNERS/Dependabot;
- backfill;
- v6.1 relationship;
- whether v7 is overbuilt or underbuilt.

Then:

```text
RESULT = PASS | REVISE
REVIEW_STAGE = MATURITY_DESIGN_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
REVIEWED_PROPOSAL_COMMIT = 3d091421c7afe8d4f90687ef6e0ce2686bcaf426
```

If REVISE:

- stable blocker IDs;
- direct evidence;
- causal risk;
- minimum close condition;
- full Planner repair prompt.

If PASS:

```text
NEW_BLOCKERS = NONE
NEXT_HANDOFF = PLANNER
```

明确 PASS 只批准 v7 maturity design。

它不授权：

- labels mutation;
- Issue/Project mutation;
- `.github` implementation;
- hierarchy/dependency mutation;
- v6.1 implementation;
- machine adaptation;
- production plugin source change.

下一步回 Planner 冻结 v7 独立 implementation package，不让用户拼 locator。

## Review file authorization

用户发送本 prompt，即授权你只在 latest main 新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_CRITIC_REVIEW_2026-10-01.md`

并 ordinary non-force push。

除此之外禁止修改任何 repo source / Issue / Project / `.github` configuration。
