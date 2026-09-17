# 057 Repo AGENTS Hygiene — Integration Kickoff Draft

- Task key: `057_repo_agents_hygiene`
- Integration package version: `v0.1`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.1
- Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md` v0.1
- Status: `DRAFT_NOT_AUTHORIZED`

Only after independent Critic reviews this exact integration package and returns `READY_FOR_INTEGRATION_CODEX=YES` does the user sending the approved `## Kickoff` text authorize canonical-branch integration.

## Kickoff

执行 `057_repo_agents_hygiene` 的 separately approved integration。严格按 integration v0.1 Plan/Goal，只把已经 independent implementation review PASS 的 exact reviewed tuple 集成到 canonical branches；不重新设计057，不修改 reviewed candidate 内容，不开始056。

Exact reviewed tuple：

- AI_Skills M3 `24051588d13f07e7f71e0edf5a723aca36754ed5`，其中 E3=`745281b70322b8508e43e59a5bdef70529749ea5`
- Bridge `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna `41cd1297af6901531d3135593bc9806bffc38829`
- Mica `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date `711fab75f044b7ad31e5ff8610c076f902ccc949` 只读，不得修改

Canonical targets：

- AI_Skills_Collection -> `main`
- GPT_Codex_AI_Bridge_Kit -> `main`
- Bobbio -> `develop`
- Lucerna -> `main`
- Mica-for-ChatGPT -> `main`
- Asteria -> `main`
- SeminarArc -> `main`

在第一次 canonical push 之前，先对所有 repo 做完整 read-only integration preflight：fetch canonical + existing `reviewed/057_repo_agents_hygiene`，验证 reviewed branch head 等于上面 exact SHA，验证 canonical freshness/identity，比较 merge base 和 changed paths。若 canonical branch 有涉及 candidate files、instruction/version/release authority 的相关语义漂移、reviewed branch head 已漂移、或出现真实 merge conflict，停止并回 Planner/Critic；不得自行改 candidate、cherry-pick 修补、force merge 或创建新 branch/worktree。

当前 planning-time 已验证：Bridge/Bobbio/Mica/Asteria/SeminarArc 可 fast-forward；AI_Skills 与 Lucerna 因 canonical branch 有独立后续提交而 diverged，但当前 changed paths 不与 reviewed candidate 冲突。执行时必须重新确认，不能沿用旧判断。

合并规则：

1. canonical 是 exact candidate ancestor 时，只允许：
   `git merge --ff-only <EXACT_REVIEWED_SHA>`
2. 对仍然 diverged 但确认无相关 overlap 的 AI_Skills / Lucerna：先 `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`；检查 staged result 和 `git diff --cached --check`；只有完全 mechanical、无需手工内容修改时才 commit merge。任何 conflict/语义不确定都 `git merge --abort` 后停止。
3. 禁止 squash、rebase、cherry-pick、force push、history rewrite。

建议 push 顺序：Bobbio -> Mica -> Asteria -> SeminarArc -> Lucerna -> Bridge -> AI_Skills。所有 repo 的 read-only/pre-commit preflight 必须在第一次 push 前完成。

本次授权仅包含上述 canonical branch 的普通 mechanical merge/fast-forward 和普通 push。若 remote 在 push 前再次前进导致 rejection，fetch 后重新判断；不得 force push。已成功的 repo 不通过历史重写回滚，若最终出现 partial integration，诚实报告 exact integrated/not-integrated state 并停止等待 Planner/Critic。

Bridge hard boundary：把 reviewed `0.8.3` source candidate 集成到 `main` 不等于授权 Git tag、GitHub Release、package publish、deployment、Host Policy install/update 或 `0.8.4` bump；这些全部禁止。

Integration 后只做最小 identity/merge 验证：canonical remote head、exact reviewed candidate reachability、integration mode、无额外文件/无手工内容修改、必要的 `git diff --check`。不要重新跑 product development、Bridge 363 tests、H1-H9、GPT Work、paid API/Terra；若 canonical drift 真的使旧 evidence失效，应停止回 Planner/Critic，而不是在integration阶段重新开发。

不得删除 `reviewed/057_repo_agents_hygiene` branches，不得创建 PR，不得修改 CUHK Date，不得写新的 product/runtime/AGENTS 内容，不得新增 workflow/state/schema/ledger/controller/watcher。

完成所有 canonical integration 后停止并报告每个 repo 的 old/new canonical head、FF_ONLY/CLEAN_MERGE、candidate reachability 和未验证边界。

不要在本任务里修改或执行 056。

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`
