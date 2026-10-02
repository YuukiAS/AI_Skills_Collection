# Project Instructions Editor — Planner Proposal v4.1

Date: 2026-10-01  
Status: DRAFT_FOR_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Tracking: #93  
Supersedes: `PROJECT_INSTRUCTIONS_EDITOR_V4_PLANNER_PROPOSAL_2026-10-01.md`  
Prior Critic review: `PROJECT_INSTRUCTIONS_EDITOR_V4_CRITIC_REVIEW_2026-10-01.md`  
Candidate future standalone Skill: `project-instructions-editor`

## 0. Planner disposition on v4 Critic findings

Planner accepts both blockers.

No rebuttal is needed on either architecture finding.

One point is intentionally narrowed rather than strengthened: the Project governance language is treated as a **credible contributing factor** to residual English leakage, not as the unique proven root cause. Old thread history, Project files, and general expression inertia may also contribute. The proposed real regression is what should determine how much source-language normalization helps.

This proposal remains planning-only. It does not authorize standalone Skill implementation.

## 1. Decision requested from Critic

Decide whether the next AI Research Stack Project-instruction readability refinement may proceed under these constraints:

1. keep the proven Project-level user-reading bridge;
2. normalize unnecessary ordinary English inside Project governance instructions without changing governance semantics;
3. explicitly require a final user-reading rewrite before the answer is sent;
4. apply a semantic invariant so the rewrite cannot weaken facts, conditions, authorization, safety, evidence strength, uncertainty, or conclusion boundaries;
5. preserve exact formal names and machine strings;
6. verify governance semantic preservation before real Project regression;
7. remain planning-only until the user later authorizes standalone-Skill implementation.

## 2. Evidence from real use

Before the Project bridge, a real AI Research Stack answer heavily reused internal engineering language, including patterns such as:

- `specialist-first`
- `degraded fallback`
- `candidate consumption`
- `normal-entry run`
- `capability discovery`
- `workflow / state / daemon / environment manager`

After adding the Project Section 0 bridge, a comparable answer improved substantially. It explained the main `workflow-core 0.4` versus planned `0.5` difference in direct Chinese and converted many concepts to natural Chinese.

Residual leakage remained:

- `source-of-truth`
- `specialist routing`
- `shell/PATH`
- `command not found`
- `fallback`
- “Bridge routing”

Reasonable retained exact names included:

- `workflow-core 0.4/0.5`
- Codex
- Python / R / Node
- XeLaTeX / Chromium
- Bridge Kit
- Reviewed Handoff
- W1–W5
- `PATH`

The evidence supports two bounded claims:

- the Project bridge has a real positive effect;
- the remaining Project governance language is a credible contributor to residual leakage.

It does **not** prove that governance text is the only cause.

## 3. Three-layer architecture

### 3.1 User-reading layer

Section 0 remains the Project-level user-reading contract.

It is responsible for:

- natural Chinese explanatory prose;
- exact-name / machine-string boundaries;
- natural paragraph structure;
- inline-versus-block mathematics;
- explanatory prose versus exact machine deliverables.

### 3.2 Final user-reading rewrite with semantic invariant

Before sending the final answer, explanatory prose should be rewritten into the user-reading layer instead of directly reusing wording from Project rules, logs, tables, or source documents.

Exact names and exact machine deliverables remain unchanged where their exact form is functionally required.

The rewrite has a strict semantic invariant:

> The final user-reading rewrite may change expression and information organization only. It must not change factual conclusions, conditional relationships, mandatory/optional meaning, authorization or safety state, evidence strength, uncertainty, or conclusion boundaries.

Examples of prohibited semantic drift:

- `REVISE` cannot become “总体没什么问题”;
- “未授权执行” cannot become “暂时不太建议执行”;
- “证据不足” cannot become “目前看来基本成立”;
- “必须读取” cannot become “可以参考”;
- a scoped conclusion cannot silently become a global conclusion.

This is a final-output constraint, not a new runtime, state machine, or second reasoning workflow.

### 3.3 Governance-layer language normalization with semantic-preservation gate

A later AI Research Stack Project-instruction candidate may reduce unnecessary ordinary English in Sections 1–18, but the mutation class is intentionally narrow.

Allowed:

- local natural-language normalization of ordinary engineering, management, and process vocabulary;
- preserving exact identifiers while making surrounding explanatory wording more natural.

Forbidden as part of this readability change:

- reordering governance rules;
- merging independent rules;
- deleting rules or exceptions;
- summarizing away conditions;
- redesigning the governance architecture;
- changing trigger thresholds;
- changing role authority;
- changing approval meaning;
- changing safety, authorization, evidence, Bridge, Capability Gate, release, resource, or research-integrity semantics;
- translating exact machine identifiers.

Before the candidate is used for real Project regression, perform a semantic-preservation comparison against the current Project instructions.

The comparison must explicitly confirm that these semantic classes are unchanged:

- role identities and role boundaries;
- trigger and escalation conditions;
- permissions and authorization;
- safety boundaries;
- evidence requirements and completion claims;
- Bridge / Reviewed Handoff responsibilities;
- Capability Gate semantics;
- release and deployment constraints;
- resource / cost boundaries;
- research-integrity requirements;
- exact identifiers and fixed machine protocol strings.

This is not a string-equality requirement. The acceptance question is whether the rules still mean the same thing.

Examples of possible language normalization when a term is not a formal name:

- source → 来源 / 事实来源
- scope → 范围
- blocker → 阻塞项
- fallback → 降级 / 替代路线
- routing → 路由
- runtime → 运行机制
- artifact → 产物
- candidate → 候选版本
- production-ready → 可投入生产
- workaround → 临时绕行方案

These are examples, not a replacement dictionary.

### 3.4 Exact machine/formal layer

Do not force all-English removal.

Exact formal names and machine strings stay exact where precision matters, including:

- repository and file names;
- paths and commands;
- fields and state values;
- fixed machine-readable blocks;
- formal product, Skill, role, or mechanism names;
- versioned identifiers.

Likely retained examples include Planner, Critic, Executor, Reviewer/Terra, Bridge Kit, Reviewed Handoff, versioned Skill names, `AGENTS.md`, `CODEX_HOME`, `PATH`, PASS/REVISE, repository paths, commands, fixed fields, and state blocks when those identities are functionally exact.

“Looks technical” is not enough to protect an English term.

## 4. Why source-language normalization is still worth testing

Section 0 already produced a material improvement. Project governance text still supplies many ordinary English engineering expressions in high-priority local context.

That makes governance-language normalization a reasonable intervention to test, but not a proven complete fix.

Other contributors may remain:

- old-thread wording;
- Project files;
- source documents;
- general model expression habits.

The real regression therefore tests whether reducing governance-layer English adds measurable practical benefit on top of the existing Section 0 bridge.

## 5. Why this remains a future standalone Skill candidate

The maintenance inbox already contains two different real Project families:

1. shared-course Project instructions with character-budget and multi-scope imbalance;
2. AI Research Stack instructions with governance-language / user-reading-layer leakage.

The reusable capability is broader than Chinese prose polishing:

- preserve existing valid semantics;
- make bounded edits;
- maintain multi-scope balance;
- distinguish stable Project-level rules from detailed recoverable workflows;
- use canonical locators instead of copying detail;
- preserve exact identifiers;
- respect finite instruction budget;
- keep internal control language from unnecessarily leaking into user-facing explanation.

This remains evidence for future standalone Skill design.

Implementation timing remains reserved for a later explicit user instruction.

## 6. Regression plan after an approved Project-instruction candidate

### Case A — workflow-core 0.4 vs planned 0.5

Ask for the actual-use difference.

Pass condition: exact product/mechanism names remain where useful; ordinary engineering terms do not leak unnecessarily.

### Case B — old-thread contamination

Continue in a thread with heavy historical mixed-English answers.

Pass condition: old wording does not drag new explanatory prose back into the old style.

### Case C — explanation plus machine block

Require natural explanation plus:

```text
RESULT=PASS
FINAL_HEAD=...
PUSHED=YES
```

Pass condition: prose is readable; machine block remains exact.

### Case D — statistical explanation

Use ordinary English statistical terminology, simple parameter estimates/intervals, and one genuinely complex formula.

Pass condition: ordinary terminology is naturally Chinese; simple math stays inline; complex math may remain block-form.

### Case E — semantic-invariant regression

Use a source package that simultaneously contains:

- one mandatory condition;
- one explicit authorization state;
- one uncertain conclusion;
- one Critic result such as `PASS` or `REVISE`.

Pass condition: the user-facing rewrite is easier to read but preserves the exact strength of all four semantic elements.

### Gate before Cases A–E — governance semantic preservation

Before using the revised Sections 1–18 in a real Project, compare the current and candidate Project instructions and confirm that every semantic class listed in §3.3 remains unchanged.

If that comparison fails, do not run user-facing regressions; fix the candidate first.

## 7. Maintenance tracking state

Tracking Issue: #93

The source TODO should contain:

`tracking: #93`

The intended AI Skills Maintenance Project state is `DOING`, with the current design anchor pointing to this v4.1 proposal.

The current connector surface used by this Planner exposes GitHub Issue mutation but not GitHub Project-field mutation. Therefore the Planner can legally update the Issue and source locator, but must not claim that the Project board itself has been synchronized.

Exact pending Project mutation:

- add/bind Issue #93 to the `AI Skills Maintenance` Project if not already present;
- set Project Status to `DOING`;
- set the current execution/design anchor to `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_1_PLANNER_PROPOSAL_2026-10-01.md`.

This is a maintenance-board synchronization item, not a user action request.

## 8. Critic decision

Critic should verify closure of only the prior blockers before adding new blockers:

- B1: governance semantic-preservation acceptance;
- B2: final user-reading rewrite semantic invariant.

If both are closed and no new evidence shows a real architecture risk, PASS should freeze the current design direction.

If PASS, the next phase is **not standalone Skill implementation**.

The next permitted phase is only one of:

- prepare a complete revised AI Research Stack Project-instruction candidate for user review and real regression;
- continue future standalone-Skill design if the user explicitly opens that design phase.

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```
