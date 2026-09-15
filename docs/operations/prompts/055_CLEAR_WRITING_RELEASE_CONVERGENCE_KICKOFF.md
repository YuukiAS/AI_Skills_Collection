# 055 Clear Writing Release Convergence — Codex Kickoff Draft

- Execution package version: `v0.1`
- Task: `055_clear_writing_release_convergence`
- Plan: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md`
- Goal: `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md`
- Architecture authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1 + `NEXT_RELEASE_CRITIC_REVIEW.md` PASS
- Status: `DRAFT_FOR_EXECUTION_CRITIC`

以下为等待 execution-ready Critic 审查的逐字 kickoff：

---

执行 `055_clear_writing_release_convergence`。

先读取最新 `origin/main` 的 `AGENTS.md`、本任务 Goal/Plan、Planner/Critic role contracts、Capability Gate policy、Paid External Review policy、当前 Clear Writing source 与必要 050–054 evidence。不要重新设计已通过的 architecture；按 Goal/Plan v0.1 实现，并显式使用 `workflow-core + ai-skills-core + writing-style` 职责。

Exact execution identity：

- branch: `reviewed/055_clear_writing_release_convergence`
- worktree: `/tmp/ai-skills-055-clear-writing-release-convergence`
- private read scope: `private/exports/054_clear_writing_release_closure/inputs/`、`private/exports/054_clear_writing_release_closure/deep_research_attempt1/`
- private write scope: `private/exports/055_clear_writing_release_convergence/` 与 task-local ignored `.local-runtime/`

**我发送这段 prompt 即授权当前 bounded execution scope。** 同一范围内不要重复向我询问 branch/worktree、candidate replay、CI、ordinary non-force push、下述一次 paid final review 或 bounded production smoke。

授权范围：

- 创建/使用上述 exact branch/worktree；普通 commit、fetch、merge latest main、non-force push；所有 Gate、review 和我最终 `ACCEPT` 后才可 non-force 集成 main；
- 使用 canonical repo-local candidate replay、existing Codex account/CODEX_HOME、temporary `@ai-skills-candidate` identity；不得复制 `auth.json` 或升级 global Codex；
- 运行本任务所需 focused/full zero-paid tests、render QA、generated parity、Marketplace/release CI；普通 push 不得触发付费 review；
- final stage 只允许 **1 次** `gpt-5.6-terra` Text Review：OpenAI `POST /v1/responses/input_tokens` preflight + `POST /v1/responses`，`store=false`，default tier，low reasoning，`max_output_tokens<=4096`，paid tools none，automatic retry `0`，per-call worst-case `<= USD 0.25`，campaign ceiling `<= USD 0.25`；只用 existing GitHub Actions `OPENAI_REVIEW_API_KEY`，不得读取/回显/复制或 fallback；可发送 final Deep Research candidate text、public-safe fresh candidate text和 frozen rubric，不得发送 private source/intermediates/log/credentials；
- final stage 允许一次 bounded `writing-style@yuukias-ai-skills` install/upgrade smoke：先记录 live state，exact candidate fresh-session smoke，结束后必须 restore 原 marketplace/plugin state。

严格顺序：known regression → 完整代表性长文+真实 render → pre-final independent Critic → freeze final candidate → exactly 3 个新 public-safe fresh holdouts → failure attribution → 一次 final Terra review → release CI → bounded production smoke+restore → final GPT Reviewer → 给我最终 artifact 做 `ACCEPT/REJECT` → ACCEPT 后才 integration。

Pre-final Critic PASS 前不得跑 fresh 或 Terra。fresh/最终评审发现真实产品缺陷时停止，不自动改 candidate 后重用 fresh，不追加第 4 个 fresh，不第二次 Terra，不自动创建 successor。Reviewer/rubric/source/environment 问题按 Goal 保留原证据并分类处理。

明确禁止：修改 Bridge Kit/Host Policy/execpolicy；新增 provider/account/credential location；扩大 private data、费用、paid calls 或 live-global target；新 runtime/state/schema/ledger；whole-branch 054 merge；sample-specific 特判；force push、破坏性 reset/clean、历史改写或其他 destructive Git。

如 latest main 的相关 policy/design 已变化、同名 task/branch 冲突、pre-final Critic 要求改变 architecture/Gate/预算/恢复合同、production restore 失败或出现 release-critical main drift，停止并报告，不自行扩大范围。

---
