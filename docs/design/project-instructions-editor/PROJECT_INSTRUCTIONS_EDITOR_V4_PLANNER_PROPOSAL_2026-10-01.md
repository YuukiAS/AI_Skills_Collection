# Project Instructions Editor — Planner Proposal v4

Date: 2026-10-01  
Status: DRAFT_FOR_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Candidate future standalone Skill: `project-instructions-editor`

## 0. Decision requested from Critic

Decide whether the next Project-instruction readability refinement should:

1. keep the proven Project-level user-reading bridge;
2. normalize unnecessary ordinary English inside the Project governance instructions **without changing governance semantics**;
3. explicitly require a final user-reading rewrite before the answer is sent;
4. preserve exact formal names and machine strings;
5. remain planning-only until the user later authorizes standalone-Skill design/implementation.

This proposal does **not** implement the future standalone Skill.

## 1. Evidence from real use

Before the Project bridge, a real AI Research Stack answer heavily reused internal engineering language, including patterns such as:

- `specialist-first`
- `degraded fallback`
- `candidate consumption`
- `normal-entry run`
- `capability discovery`
- `workflow / state / daemon / environment manager`

After adding the Project Section 0 bridge, a comparable answer improved substantially. It explained the main `workflow-core 0.4` versus planned `0.5` difference in direct Chinese, and converted many concepts to natural Chinese.

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

The evidence therefore supports “partial success with a residual source-language problem,” not “the bridge failed.”

## 2. Root-cause model

The Project currently mixes three kinds of language.

### Layer 1 — exact names and machine strings

These require preservation when exact identity matters:

- repository and file names;
- paths and commands;
- fields and state values;
- fixed machine-readable blocks;
- formal product, Skill, role, or mechanism names;
- versioned identifiers.

These are not readability defects.

### Layer 2 — ordinary governance/control concepts

Examples include ordinary uses of:

- source
- scope
- blocker
- fallback
- runtime
- routing
- schema
- pipeline
- candidate
- artifact
- production-ready
- workaround
- capability discovery

When these terms do not need exact lookup, they can be expressed naturally in Chinese.

### Layer 3 — final user-facing explanation

This should be readable Chinese that communicates the actual judgment and effect, while selectively preserving Layer 1.

The remaining failure occurs when Layer 2 is copied directly into Layer 3.

## 3. Proposed architecture

### 3.1 Keep Section 0 as the user-reading contract

Do not replace the Project's governance system with a writing framework.

Section 0 remains responsible for:

- natural Chinese explanatory prose;
- exact-name / machine-string boundaries;
- natural paragraph structure;
- inline-versus-block mathematics;
- explanatory prose versus exact machine deliverables.

### 3.2 Make the final rewrite explicit

Add one semantic instruction:

> Project control language is for reasoning and execution. Before sending the final answer, rewrite explanatory prose into the user-reading layer instead of directly reusing wording from Project rules, logs, tables, or source documents. Preserve exact names and machine deliverables only where their exact form is functionally required.

This is a final-output constraint, not a new runtime, state machine, or second reasoning workflow.

### 3.3 Normalize Sections 1–18 without changing governance meaning

If Critic approves, a later revision may edit the existing AI Research Stack Project instructions to reduce unnecessary ordinary English.

Allowed change class:

- language normalization only;
- preserve all governance decisions and conditions;
- preserve formal names, files, fields, paths, commands, states, versions, and exact protocol strings;
- preserve Planner–Critic boundaries, Bridge behavior, authorization, Capability Gates, testing, evidence, release, resource, and research-integrity semantics.

Not allowed:

- redesigning governance;
- changing trigger thresholds;
- changing authority;
- changing approval meaning;
- deleting safety or evidence requirements;
- translating exact machine identifiers.

Examples of possible language normalization when the term is not a formal name:

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

These are examples, not a mandatory replacement dictionary.

### 3.4 Preserve exact-name semantics

Do not force all-English removal.

Likely retained items include formal names such as Planner, Critic, Executor, Reviewer/Terra, Bridge Kit, Reviewed Handoff, versioned Skill names, `AGENTS.md`, `CODEX_HOME`, `PATH`, PASS/REVISE, repository paths, commands, fixed fields, and state blocks when those names are functionally exact.

Critic should challenge any item whose “formal name” status is not actually necessary.

## 4. Why not keep strengthening Section 0 only?

Section 0 already produced a material improvement. The remaining Project context still contains many ordinary English engineering terms.

Continuing to add more output prohibitions while leaving the dominant local instruction language unchanged risks:

- duplicated rules;
- a longer Section 0;
- more conflict between instruction layers;
- continued lexical leakage from governance text.

The proposed refinement reduces the source pressure as well as preserving the output contract.

## 5. Why this should later become a standalone Skill candidate

The existing maintenance inbox already shows a broader reusable problem:

- Project instructions have finite budget;
- edits must preserve existing valid semantics;
- recent requests must not dominate the whole Project;
- Project instructions should keep stable ownership/routing/authority while leaving detailed workflows behind canonical locators;
- unnecessary ordinary English wastes budget and harms readability;
- exact identifiers must remain exact;
- before/after editing requires semantic preservation review, not mere shortening.

The current readability work adds another reusable capability requirement: distinguish internal Project control language from the final user-reading layer.

This is strong evidence for a future standalone `project-instructions-editor` Skill, but **implementation timing remains explicitly reserved for a later user instruction**.

## 6. Regression plan after a later approved Project-instruction revision

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

## 7. Critic decision

Critic should decide:

- whether source-language normalization in Sections 1–18 is justified by the real evidence;
- whether the final user-reading rewrite is a useful semantic constraint rather than redundant ceremony;
- whether the exact-name boundary is safe;
- whether the scope remains a language/readability refactor rather than governance redesign.

If PASS, the next step is **not Skill implementation**. The next step is only to prepare a complete revised AI Research Stack Project-instruction candidate for user review.

Standalone-Skill implementation remains blocked until the user explicitly opens that later phase.
