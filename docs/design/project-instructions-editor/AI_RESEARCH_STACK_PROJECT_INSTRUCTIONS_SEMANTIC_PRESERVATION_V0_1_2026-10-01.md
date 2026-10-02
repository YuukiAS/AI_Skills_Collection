# AI Research Stack Project Instructions — Semantic Preservation Audit v0.1

Date: 2026-10-01  
Status: PLANNER_SEMANTIC_PRESERVATION_PASS  
Tracking: #93  
Candidate: `AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_CANDIDATE_V0_1_2026-10-01.md`  
Governance baseline: `docs/skill-todos/project-instructions-editor.md` → Reference B  
Architecture authority: `PROJECT_INSTRUCTIONS_EDITOR_V4_1_PLANNER_PROPOSAL_2026-10-01.md`

## 0. Scope

This audit checks only whether the candidate preserves the governance meaning of AI Research Stack Sections 1–18 while normalizing ordinary language.

It does not claim that the candidate has already been applied to the real ChatGPT Project and does not claim that Cases A–E have already run.

The current Project reading bridge (Section 0) is treated as an already observed behavior change from the prior real regression. The candidate adds the v4.1 semantic invariant to that bridge.

## 1. Structural preservation

PASS.

- Sections remain numbered 1–18 in the same order.
- No governance section is removed.
- No governance section is merged with another section.
- No trigger family, role family, evidence family, authorization family, Bridge/Handoff family, Capability Gate family, release/resource family, or research-integrity family is deleted.
- Language normalization is local: ordinary English nouns and labels are rewritten into Chinese where exact identity is not required.
- Formal names and machine strings remain exact where precision matters.

## 2. Section-by-section governance comparison

| Section | Governance meaning that must survive | Candidate check |
|---|---|---|
| 1 | ordinary tasks stay lightweight; borderline governance asks once; listed high-risk/new-workflow classes require Planner–Critic; scope expansion stops and escalates | PASS — same three control clauses, only ordinary terms such as artifact/repo/workflow are normalized |
| 2 | Planner/Critic remain independent; three mandatory source files remain required; AI Skills maintenance tracking remains required; Reviewed Handoff/Bridge prerequisites remain; Kickoff authorization scope remains; target-repo rules must be read before PASS/Plan/Goal | PASS — all locators, roles, conditions and authorization clauses preserved |
| 3 | Planner proposes; Critic PASS/REVISE; Planner cannot self-approve; blockers close only through Critic; no implementation without required PASS; PASS is scoped and not user authorization; material changes trigger re-review | PASS — ACCEPT/PARTIAL_ACCEPT/REBUT/PASS/REVISE remain exact |
| 4 | Critic blocks real risks, not uncertainty; blocker requires requirement/evidence/causal risk/minimum closure; old blockers checked first; endpoint cannot move without evidence | PASS — “blocker” normalized to 阻塞项 without changing the test |
| 5 | fact precedence remains ordered; connected sources must actually be read; environment-sensitive facts require correct-environment verification; verified fact/inference/plan remain distinct; no unsupported completion/support claims | PASS — order and evidentiary strength unchanged |
| 6 | five preflight dimensions remain Product/Reality/Alternatives/Red Team/Execution Contract in meaning; plan freezes only after they are clear | PASS — labels translated only; each test remains intact |
| 7 | Planner/Critic substantive rounds perform bounded external verification; authoritative sources preferred; stable verified facts may be reused; no search/download/environment churn as a substitute for decision | PASS |
| 8 | Bridge Kit remains cross-repo reusable execution/handoff owner only; repo-specific work stays in target repo; AI_Skills_Collection remains owner of skill/plugin/profile/registry/catalog/provenance/Marketplace; workflow-core/ai-skills-core/domain responsibility split remains | PASS — exact component names retained |
| 9 | failures are attributed along source→task→contract→implementation/runtime→artifact→review; existing rules failing leads to caller/entry/implementation diagnosis before new rules; only cross-repo generic capability goes to Bridge | PASS |
| 10 | Skill/Plugin/Profile/Domain meanings remain distinct; prefer merge/extend/profile/repo-local/reference before adding entry | PASS — taxonomy names retained |
| 11 | reusable decisions recorded once; execution authorization remains bound to exact scope; only material authorization changes re-confirm; Critic PASS/AGENTS/history cannot impersonate authorization; risky probes need approval; refusals cannot be bypassed | PASS |
| 12 | manual Planner/Critic handoff remains default; no new control plane/runner/watcher/database/state machine merely for governance; role ownership unchanged; automation requires proposal+PASS+clear recovery+user authorization | PASS |
| 13 | Plugin behavior/release/maturity changes require policy-based Gate Matrix; Gate is capability/failure based; downloads/tests/CI/structure/receipts cannot impersonate capability; key release Gate uses same final candidate and normal entry; seen samples are not fresh; final evaluation rules unchanged | PASS |
| 14 | PASS remains scoped/evidence-backed; mechanical signals cannot prove professional/user-facing quality; final candidate must pass key verification; helper is not normal entry; completion requires implementation+real verification+independent review+needed user acceptance+integration; acceptance remains by actual consumption object | PASS |
| 15 | external resource provenance/adoption state remains required; discovery/check differs from real consumption; user template must be loaded; no silent low-quality fallback; mature dependency/selective port/adaptation preferred with license/source boundaries | PASS — fixed adoption-state enum remains exact |
| 16 | AI_Skills plans/reviews/tests/renders/reports/handoffs stay in repo; private/large files location unchanged; README closure rule unchanged; exact README no-update receipt preserved; branch/remote check and non-infinite waiting/retry rules unchanged | PASS |
| 17 | user-visible failure overrides internal PASS as evidence of regression; no fabricated DOI/literature/data/experiment/citation/runtime state; source/author/our inference separated; scientific notation/meaning/strength/traceability preserved | PASS |
| 18 | every major stage must add real capability; structure/audit/metadata/synthetic benchmark alone usually not enough; execution prompt requires goal/source/route/risk/acceptance/permission/recovery + valid Critic PASS; long goal stays in repo Goal; Codex prompt remains Chinese/short/current-task; prompt edits return full version | PASS — final reply-style sentence is delegated to approved Section 0 rather than changing execution semantics |

## 3. Protected semantic classes

### Roles and role boundaries

PASS.

Planner, Critic, Executor, Reviewer/Terra remain formal roles with the same ownership and non-self-review constraints.

### Trigger and escalation conditions

PASS.

All original task classes and all original escalation conditions remain. No trigger is widened or narrowed.

### Permissions and authorization

PASS.

The candidate preserves:

- PASS does not equal user authorization;
- Kickoff authorization stays bounded to task/branch/worktree scope;
- only material permission/scope/credential/cost/high-impact changes trigger reconfirmation;
- rejected actions cannot be bypassed.

### Safety and evidence strength

PASS.

“must,” “must not,” “only,” and evidence requirements remain strong. No mandatory clause is weakened into preference language.

### Bridge / Reviewed Handoff

PASS.

The Bridge boundary, prerequisite reading, successor/automatic-handoff availability check, and cross-repo-only escalation rule remain intact.

### Capability Gate

PASS.

The policy locator, Gate Matrix requirement, capability-based Gate semantics, final-candidate identity, and final-evaluation constraints remain intact.

### Release / deployment / resource boundaries

PASS.

Release and README closure requirements, external-resource provenance, cost/resource authorization, and deployment/installation distinctions are unchanged.

### Research integrity

PASS.

No fabrication, source/inference separation, sufficient source reading, notation/scientific meaning, conclusion strength, and traceability all remain intact.

### Exact identifiers

PASS.

The candidate keeps exact identifiers where they function as formal names or machine strings, including `AI_Skills_Collection`, `workflow-core`, `ai-skills-core`, Bridge Kit, Reviewed Handoff, Planner/Critic/Executor/Reviewer/Terra, PASS/REVISE/ACCEPT/PARTIAL_ACCEPT/REBUT, `AGENTS.md`, `CODEX_HOME`, `PATH` when used, file paths, `tracking: #N`, `README checked: no update required`, adoption-state enum values, and exact machine blocks.

## 4. Language-normalization classes

The candidate changes only presentation-level language where exact English is not functionally needed.

Examples:

- artifact → 产物
- repo → 仓库
- workflow → 工作流程
- source → 来源
- scope → 范围
- blocker → 阻塞项
- production-ready → 可投入生产
- workaround → 临时绕行方案
- render → 渲染结果
- branch/worktree → 分支/工作树 when referring to the concept rather than an exact value

These examples are not a replacement dictionary and do not authorize translation of exact identifiers.

## 5. v4.1 semantic-invariant regression

### Source semantics

The source package states:

- Critic result = `REVISE`;
- implementation is not authorized until Critic PASS;
- current evidence suggests governance language contributes to residual English leakage, but it is not proven to be the only cause;
- Planner must read the required contract files before freezing an executable Plan.

### User-reading rewrite

“Critic 的结论仍是 `REVISE`，所以当前还没有实现授权；在 Critic 给出 PASS 之前不能启动实现。现有证据只支持‘项目治理语言是残余英文泄漏的一个贡献因素’，不能把它说成唯一原因。Planner 在冻结可执行 Plan 之前仍必须先读取规定的合同文件。”

### Semantic check

PASS.

- `REVISE` remains `REVISE`;
- authorization remains absent;
- “contributing factor, not unique cause” remains uncertain/bounded rather than strengthened;
- “must read before freezing Plan” remains mandatory.

The rewrite improves readability without changing conclusion, condition, authorization state, evidence strength, uncertainty, or scope.

## 6. Planner conclusion

```text
STRUCTURAL_PRESERVATION=PASS
ROLE_BOUNDARIES=PASS
TRIGGER_ESCALATION=PASS
PERMISSION_AUTHORIZATION=PASS
SAFETY_EVIDENCE=PASS
BRIDGE_HANDOFF=PASS
CAPABILITY_GATE=PASS
RELEASE_RESOURCE=PASS
RESEARCH_INTEGRITY=PASS
EXACT_IDENTIFIER_PRESERVATION=PASS
FINAL_REWRITE_SEMANTIC_INVARIANT=PASS

PLANNER_SEMANTIC_PRESERVATION=PASS
READY_FOR_INDEPENDENT_CRITIC_REVIEW=YES
READY_FOR_REAL_PROJECT_REGRESSION=NO
READY_FOR_SKILL_IMPLEMENTATION=NO
```

Real Project regression remains blocked until an independent Critic confirms this candidate/audit package and the candidate is actually applied to the Project settings.
