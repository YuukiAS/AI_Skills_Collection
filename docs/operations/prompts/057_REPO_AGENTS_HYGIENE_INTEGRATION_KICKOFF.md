# 057 Repo AGENTS Hygiene — Integration Kickoff Draft

- Task key: `057_repo_agents_hygiene`
- Integration package version: `v0.2`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.2
- Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md` v0.2
- Status: `DRAFT_NOT_AUTHORIZED`

Only after independent Critic reviews this exact v0.2 integration package and returns `READY_FOR_INTEGRATION_CODEX=YES` does the user sending the approved `## Kickoff` text authorize canonical-branch integration.

## Kickoff

执行 `057_repo_agents_hygiene` 的 separately approved integration。严格按 integration v0.2 Plan/Goal，只把已经 independent implementation review PASS 的 exact reviewed tuple 集成到 canonical branches；不重新设计057，不修改 reviewed candidate 内容，不开始056。

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

在第一次 canonical push 之前，先对所有 mutable repo 完成统一 integration preflight。对每个 repo 必须：

1. fetch canonical + existing `reviewed/057_repo_agents_hygiene` refs；
2. 验证 reviewed branch head 等于上面 exact SHA，AI_Skills reviewed branch 等于 M3；
3. 验证当前 canonical branch/head、freshness、merge base、changed paths 和既定 `FF_ONLY` / `CLEAN_MERGE` 关系仍成立；
4. 对真正准备执行 integration 的 canonical checkout 记录 `git status --porcelain` 或等价直接证据，并确认：
   - 当前 branch/HEAD 就是要求的 canonical branch/head；
   - 没有未完成 merge/rebase/cherry-pick/revert/bisect 或等价 Git operation；
   - index 没有 pre-existing staged changes；
   - tracked working tree 没有 pre-existing unstaged changes；
   - untracked files 不与 candidate paths、merge outputs 或 checkout/merge 目标冲突。

若发现 unrelated dirty/staged user work：不得 `git stash`、`git reset`、`git clean`、顺手 commit、移动/覆盖用户文件或把它夹进 integration commit；停止该 repo并报告 exact dirty state，回 Planner/Critic。若 untracked file 是否冲突存在不确定性，也停止；不得为了继续 integration 自动删除或覆盖。

上述 clean canonical checkout/index gate 同样适用于 fast-forward repos，并且所有 repo 的 source/drift/identity/clean-state preflight 都必须在第一次 canonical push 前完成。

当前已审 integration strategy 保持不变：Bridge/Bobbio/Mica/Asteria/SeminarArc 是 `FF_ONLY`；AI_Skills/Lucerna 是 `CLEAN_MERGE`。执行时重新确认，不得沿用旧判断绕过 drift gate。

合并规则：

1. canonical 是 exact candidate ancestor 且 clean-state gate 通过时，只允许：
   `git merge --ff-only <EXACT_REVIEWED_SHA>`
2. AI_Skills / Lucerna 只有在仍然 diverged、确认无相关 overlap、且 canonical checkout/index clean 时，才允许：
   `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`
   然后检查 staged result、`git diff --cached --check`、candidate-owned files和无额外/unrelated content。只有完全 mechanical、无需任何手工内容修改时才 commit。
3. 任何 conflict 或语义不确定都 `git merge --abort` 后停止；因为 merge 前必须先通过 clean-state gate，abort才有可信 recovery base。
4. 禁止 squash、rebase、cherry-pick、force push、history rewrite或自行换 merge strategy。

保持已审 push 顺序：Bobbio -> Mica -> Asteria -> SeminarArc -> Lucerna -> Bridge -> AI_Skills。

本次授权仅包含上述 exact canonical branch 的普通 mechanical merge/fast-forward 和普通 push。若 remote 在 push 前再次前进导致 rejection，fetch 后停止并重新判断；不得 force push。已成功的 repo 不通过历史重写回滚；若最终 partial integration，诚实报告 exact integrated/not-integrated state并停止等待 Planner/Critic。

Bridge hard boundary：把 reviewed `0.8.3` source candidate 集成到 `main` 不等于授权 Git tag、GitHub Release、package publish、deployment、Host Policy install/update、reviewed branch deletion 或 `0.8.4` bump；这些全部禁止。

Integration 后只做最小 identity/merge 验证：canonical remote head、exact candidate reachability、integration mode、clean-state evidence、无额外文件/无手工内容修改、必要的 `git diff --check`。不要重新跑 product development、Bridge 363 tests、H1-H9、GPT Work、paid API/Terra；若 canonical drift 真的使旧 evidence失效，应停止回 Planner/Critic，而不是在integration阶段重新开发。

不得删除 `reviewed/057_repo_agents_hygiene` branches，不得创建 PR/branch/worktree，不得修改 CUHK Date，不得写新的 product/runtime/AGENTS 内容，不得新增 workflow/state/schema/ledger/controller/watcher。

完成所有 canonical integration 后停止并报告每个 repo 的 old/new canonical head、FF_ONLY/CLEAN_MERGE、candidate reachability、preflight clean-state evidence 和未验证边界。

不要在本任务里修改或执行 056。

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`
