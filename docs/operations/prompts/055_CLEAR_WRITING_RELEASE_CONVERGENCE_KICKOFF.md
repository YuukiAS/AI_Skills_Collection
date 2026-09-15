# 055 Clear Writing Release Convergence — Codex Kickoff Draft

- Execution package version: `v0.2`
- Task: `055_clear_writing_release_convergence`
- Plan: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.2
- Goal: `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md` v0.2
- Architecture authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1 + `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md` PASS
- Prior execution-ready review: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW.md`, blockers `C1,C2,C3,C4`
- Status: `DRAFT_FOR_EXECUTION_CRITIC`

以下为等待 execution-ready Critic 审查的逐字 kickoff：

---

执行 `055_clear_writing_release_convergence`。

先读取最新 `origin/main` 的 `AGENTS.md`、Planner/Critic role contracts、本任务 Goal/Plan v0.2、Capability Gate policy、Paid External Review policy、version policy、当前 Clear Writing source 与必要 050–054 evidence。不要重新设计已经 PASS 的 architecture；按 Goal/Plan v0.2 实现，并显式使用 `workflow-core + ai-skills-core + writing-style`。

Exact execution identity：

- branch: `reviewed/055_clear_writing_release_convergence`
- worktree: `/tmp/ai-skills-055-clear-writing-release-convergence`
- private read scope: `private/exports/054_clear_writing_release_closure/inputs/`、`private/exports/054_clear_writing_release_closure/deep_research_attempt1/`
- private write scope: `private/exports/055_clear_writing_release_convergence/` 与 task-local ignored `.local-runtime/`

**我发送这段 prompt 即授权当前 bounded execution scope。** 同一范围内不要重复询问 branch/worktree、candidate replay、CI、ordinary non-force push、下面的一次 paid final review、manual pre-final Critic handoff 或 bounded production smoke。

授权范围：

- 创建/使用上述 exact branch/worktree；ordinary commit、fetch、pre-final candidate closure前的 ordinary merge latest main、non-force push；所有 Gate/review 和我最终 `ACCEPT` 后才可 non-force integration main；
- 使用 canonical repo-local candidate replay、existing Codex account/CODEX_HOME、temporary `@ai-skills-candidate` identity；不得复制 `auth.json` 或升级 global Codex；
- 运行本任务所需 focused/full zero-paid tests、render QA、source/generated parity、Marketplace/release CI；ordinary push不得触发 paid review；
- pre-final Critic handoff：只在 `private/exports/055_clear_writing_release_convergence/pre_final_critic_bundle/` 准备 `01_SOURCE_FULL.txt`、`02_CANDIDATE.md`、`03_RENDER.pdf`、`04_BUNDLE_MANIFEST.md`；如 canonical source不是纯文本，另把 exact original input放在 `source_original/`并写入 manifest。准备完成后**停止并把 exact paths告诉我，由我本人上传 manifest指定的 source/candidate/render到已有长期 Critic thread**。你不得主动上传 private plaintext，不得换 provider/transport；credentials、`auth.json`、JSONL、Meaning Map、Reader Plan、intermediate/self-audit、repo logs、无关 private artifacts不得进入该 bundle；
- final stage只允许 **1 次** `gpt-5.6-terra` Text Review：OpenAI `POST /v1/responses/input_tokens` preflight + `POST /v1/responses`，`store=false`，default tier，low reasoning，`max_output_tokens<=4096`，paid tools none，automatic retry `0`，per-call worst-case `<= USD 0.25`，campaign ceiling `<= USD 0.25`；只用 existing GitHub Actions `OPENAI_REVIEW_API_KEY`，不得读取/回显/复制/fallback；可发送 final Deep Research candidate text、public-safe fresh candidate text和 frozen rubric，不得发送 private source/intermediates/log/credentials；
- final stage允许一次 bounded `writing-style@yuukias-ai-skills` install/upgrade smoke：先记录 live state，exact certified candidate fresh-session smoke，结束后无论 PASS/FAIL都必须 restore原 marketplace/plugin state。

严格顺序：

1. known implementation + regression；
2. reconcile latest main、完成 version/changelog、generated payload、source/generated parity、freeze rubric并 commit candidate `C_n`；
3. **从 exact `C_n`** 重跑 G1–G6，生成完整代表性长文和真实 render；
4. 准备 public evidence + private Critic bundle，我手动上传后，由独立 Critic实际读 `C_n` 的 source/candidate/render；
5. Critic若要求任何 production/payload/rubric/代表性 artifact修改，形成新 candidate并重新走 2–4；**只有最后一次 Critic对 exact `C_n` PASS后，`C_n`才成为 `FINAL_CANDIDATE_COMMIT`**；
6. 从此不得改 candidate/payload/rubric；后续 replay全部 pin该 commit；
7. 冻结 exactly 3 个新 public-safe fresh sources；每项预先写明主要风险、适用 G2–G6 criteria 与是否必须 render；
8. 三项全部走同一 final candidate normal plugin entry；每项必须有 source-aware A、完整 candidate的真实 B qualitative reading，并按适用 G3/G4/G5/G6检查；需要 render的必须实际看 render；receipt/hash/mechanical audit不能单独判 PASS；只有 `3/3 PASS` 才算 G7 PASS；
9. failure attribution；无 unresolved blocker后才允许一次 final Terra；
10. release CI → bounded production smoke+restore → final GPT Reviewer → 给我 final artifact做 `ACCEPT/REJECT` → ACCEPT后才 integration。

Pre-final Critic PASS前不得跑 fresh或 Terra。Critic PASS后若 production source、generated payload、version/release identity、frozen rubric或已审代表性 artifact有任何变化，之前 PASS失效，禁止继续 fresh/Terra，必须重新走 candidate closure + representative artifact + Critic。

Failure attribution必须区分：`PLUGIN_DEFECT | SOURCE_DEFECT | REVIEWER_RUBRIC_DEFECT | ENVIRONMENT_DEFECT | WORKFLOW_DEFECT | CONTRACT_AMBIGUITY`。遇到 `CONTRACT_AMBIGUITY` 默认停止当前 certification，保留 candidate/source/output/fresh identity/original finding，不调 production、不临时改 rubric；交 Planner + Critic按 frozen user requirement/Goal/design裁定。只有不改变既有 requirement的解释性澄清可在同一 certification继续；实质改变 acceptance/rubric/product boundary/fresh/cost/recovery必须重新获得明确批准范围。不要自动新开 fresh、第二 Terra或 successor。

Fresh/最终评审发现 true product failure时停止：不改 candidate后重用 fresh，不替换/追加第 4 个样本，不第二次 Terra，不自动创建 successor。Reviewer/source/environment/workflow问题也必须保留原 evidence并按 Goal恢复。

明确禁止：修改 Bridge Kit/Host Policy/execpolicy；新增 provider/account/credential location；扩大 private data、费用、paid calls或 live-global target；新 runtime/state/schema/ledger；whole-branch 054 merge；sample-specific特判；Executor主动传输 private Critic bundle；force push、destructive reset/clean、历史改写或其他 destructive Git。

如 latest main相关 policy/design实质变化、同名 task/branch冲突、pre-final Critic要求改变 architecture/Gate/预算/授权/recovery、production restore失败或出现 release-critical main drift，停止并报告，不自行扩大范围。

---
