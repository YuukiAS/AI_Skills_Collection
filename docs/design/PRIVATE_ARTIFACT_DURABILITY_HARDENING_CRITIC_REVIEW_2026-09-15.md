# Private Artifact Durability Hardening — Critic Review

- Date: `2026-09-15`
- Review stage: `WORKFLOW_HARDENING`
- Decision: `PASS`
- Target repo: `YuukiAS/AI_Skills_Collection`
- Target domain: Reviewed Handoff / private artifact lifecycle
- Source ref reviewed: `main@e98fb3ceb2c3effe32fae34947c93b0e22a4c9f7`
- Evidence branch: `reviewed/055_clear_writing_release_convergence@7fcc26d68754771cf22f0fd6d9f8ff8ee9cd9ecd`
- Proposal reviewed: Planner H1–H4, as supplied by the user in the current Critic handoff
- Clear Writing 055 architecture: explicitly out of scope

## 1. 结论

`PASS`。

这是一个真实的 AI_Skills_Collection 跨插件 workflow regression，不是 Clear Writing 产品 bug。现有规则虽然已经要求不可公开交付物放在 repo 内 `private/exports/`，并允许 task-owned `/tmp` worktree / cache 承担临时执行，但没有定义一个关键语义：**linked task worktree 里的 `private/exports/` 仍然跟着该 worktree 的生命周期走，并不天然等于跨 worktree / 跨 task 的 durable storage。**

因此 Planner 的 H1–H4 是最小且方向正确的修复：在 `AGENTS.md` 写清 repo-wide durability invariant，同时在所有 Reviewed Handoff Executor 实际消费的 `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md` 加 pre-disposal guard，再做 focused regression validation。无需新 cleanup framework、artifact database、state/schema/ledger，也无需修改 Bridge Kit。

## 2. 实际读取与事实

本轮实际读取了最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md` v1.3
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` v1.2
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V2_2026-09-14.md`
- `tests/test_reviewed_handoff_prompt_contract.py`

并读取 055 task branch 的：

- `results/055_clear_writing_release_convergence/PHASE4_PRIVATE_ARTIFACT_GAP.md`
- `automation/reviewed_handoff/tasks/055_clear_writing_release_convergence/CURRENT.json`

055 evidence 直接证明当前影响：Phase 4 需要复用 054 private Deep Research source/artifact，但预期的 `private/exports/054_clear_writing_release_closure/...` 在 055 worktree 和长期 checkout 都不存在；CURRENT 因此停在等待恢复/重新授权历史 artifact 的路径。该失败与 Clear Writing prose mechanism 无关，而来自历史 task private artifact 的生命周期。

现有 `AGENTS.md` 已明确：真实 execution/workflow/control-plane failure 若在其他 AI_Skills task 仍可能复现，应优先 harden 现有 AGENTS/workflow consumer，不要只埋进 RESULT，也不要新建 state/schema/ledger/framework。现有规则还允许 task-owned worktree/cache 写临时文件和清理可恢复临时副本，并允许后续 task 在明确冻结后复用旧 artifact。三者合在一起，已经说明 durable artifact 生命周期是 repository workflow concern。

`PRODUCT_DELIVERY_DISCIPLINE_V2` 已要求 AI_Skills 的不可公开交付物进入 repo 内 `private/exports/`、不要把 repo 外临时目录当交付位置；但 `/tmp/<linked-worktree>/private/exports/...` 同时满足“repo 内路径”表象和“临时 worktree”事实，当前规则没有解决这个歧义。

## 3. Consumer 核查

`AGENTS.md + automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md` 是当前最小真实修复面。

原因：当前 AI_Skills Reviewed Handoff 的 Executor prompt 本身已经负责 artifact handoff、repo-safe locator/hash、task cleanup/working-tree closure 等执行纪律；更关键的是，当前 Bridge Kit runner 的真实启动顺序明确要求 Executor 依次读取 repository `AGENTS.md`、Reviewed Handoff README、`prompts/CODEX_EXECUTOR.md`、REQUEST、PLAN、CURRENT。因此修改这两个文件不是“只写文档”，而是修改实际 Executor 被强制消费的合同。

本轮还搜索了当前 AI_Skills 和 Bridge Kit 的 Reviewed Handoff 实现，没有发现一个更直接、现成的 AI_Skills worktree deletion/cleanup helper 可以比 Executor contract 更小地承担这条规则。`git worktree remove` / 手工删除 worktree 的生命周期并不是当前仓库自己包装的统一 cleanup API。因此不应为了本事故新造 helper/service。

## 4. H1–H4 判定

### H1 — PASS

应明确区分：

- task-owned `/tmp` linked worktree（包括其内部 `private/exports/`）= 可清理 working copy；
- `.local-runtime/` = runtime temporary directory；
- future-required private artifact = cleanup 前必须有 durable copy。

Durable copy 默认应位于当前机器长期存在的 AI_Skills_Collection checkout 的 `private/exports/<task_key>/...`，或用户明确指定的其他 durable repo-local path。不要硬编码某台机器的绝对路径。

只保留后续 Critic/Reviewer、successor/known regression、后续 phase/gate、用户取得或 final handoff/report 真正会引用的 source/artifact/render/review bundle/evidence。不得把全部 cache/scratch/intermediate 永久化，也不得为了 durability 把 credential、`auth.json`、token-bearing config 等复制进 `private/exports/`。

### H2 — PASS

`CODEX_EXECUTOR.md` 应加入简短 pre-disposal guard。它应覆盖任何会删除 worktree、清理 task 私有 working copy、终止旧 worktree，或使当前 worktree 可安全丢弃的 final handoff。

Guard 的最小语义：

1. 识别后续仍需要的 private artifact；
2. 确认 durable copy 已存在；
3. 对关键文件在现有 RESULT/handoff/evidence surface 记录 durable locator + content hash；
4. durable copy 缺失时，不得删除唯一副本；
5. scratch/cache 只有确认不再需要才可 cleanup。

这里不需要新 manifest schema/ledger。已有 RESULT/handoff/evidence 足够记录 locator/hash。

技术措辞应注意：`git worktree prune` 主要清理 `$GIT_DIR/worktrees` 的 administrative metadata；真正导致文件丢失的是 linked worktree directory 被 `git worktree remove`、手工删除或其他 cleanup 移除。规则应写成“在任何删除或使 worktree disposable 的动作前”做 durability guard，而不要误写成 prune 本身会备份/删除内容。

### H3 — PASS

不能只验证 AGENTS 出现字符串。推荐最小 focused regression：

- 在 throwaway temp Git repo 建一个 linked task worktree；
- 在 ignored `private/exports/<task_key>/` 放一个 `future-required` artifact，并放一个 scratch-only artifact；
- 证明普通 `git status --porcelain` 不能可靠发现 ignored private artifact；
- 按新 contract 先把 future-required artifact复制到 durable checkout surrogate 的 `private/exports/<task_key>/`，记录 locator/hash；
- 删除 linked worktree 后验证 durable artifact仍存在、hash不变；
- scratch-only artifact不要求复制。

同时保留 `tests/test_reviewed_handoff_prompt_contract.py` 或最邻近现有 contract test 对 `AGENTS.md` / `CODEX_EXECUTOR.md` 的 focused assertion，证明 actual Executor consumer 具有该 guard。动态 lifecycle probe + actual prompt contract assertion 合起来才是本次足够的 validation。

不要为此新增 production cleanup helper。

### H4 — PASS

范围合理且必须保持：不修改 Clear Writing production、055 Gate/rubric、Bridge Kit、provider/credential/private external transmission、daemon/service/database/state/schema/ledger；不恢复丢失的 054 artifact；不建新的 numbered product successor。

本 hardening 是 repo workflow/docs/control test change，不触发 writing-style/plugin version bump，也不应借机发布新的 repository feature version。

## 5. 独立外部核查

本轮独立核查了 Git 官方文档：

- `git-worktree`: https://git-scm.com/docs/git-worktree/2.52.0 — `remove` 删除 linked worktree；`prune` 清理 `$GIT_DIR/worktrees` administrative information。
- `git-status`: https://git-scm.com/docs/git-status — 默认 status 不显示被 gitignore 忽略的路径；只有 `--ignored` 才显示 ignored files。
- `gitignore`: https://git-scm.com/docs/gitignore — ignored files 是 intentionally untracked files。

另做了一个完全隔离的本地 Git probe：linked worktree 中存在被 ignore 的 `private/exports/demo/future.txt` 和 `.local-runtime/scratch.txt` 时，普通 `git status --porcelain` 为空，而 `--ignored` 能看到这些目录；`git worktree remove` 在不使用 `--force` 的情况下成功，随后唯一的 ignored private artifact 随 worktree一起消失。这个 probe 直接复现了 H1/H2 所要阻止的 failure mode。

## 6. 最终判定

```text
DECISION=PASS
APPROVED_SCOPE=H1,H2,H3,H4
TARGET_FILES=AGENTS.md; automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md; focused Reviewed Handoff regression tests only
BRIDGE_KIT_CHANGE=NO
PRODUCT_CHANGE=NO
NEW_STATE_SCHEMA_LEDGER=NO
NEXT_HANDOFF=CODEX
```

该 PASS 只批准上述最小 workflow hardening 与 focused validation，不批准任何 Clear Writing/055 产品修改，也不授权恢复已经丢失的 054 files。