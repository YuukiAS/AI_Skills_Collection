# AI Skills 维护看板与完成语义 — Critic Review v1

- 日期：2026-09-22
- Review stage：`DESIGN_PROPOSAL`
- Result：`REVISE`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- human label：AI Skills 维护看板与完成语义
- source branch/ref：`main`
- reviewed proposal：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md` v1
- reviewed proposal commit：`e9804daf12611788f98d9ab3c2577c7744963c03`
- execution branch/worktree：NONE

## 1. 结论

GitHub Projects 技术上并不只有 Todo / In Progress / Done 三个状态。官方文档明确说明 single-select field 最多可以有 50 个选项；Board 的列既可以使用 Status，也可以使用其他 single-select / iteration field。

对 AI_Skills_Collection，我支持四个主状态：

```text
TODO -> DOING -> ADAPTING -> DONE
```

这里 `ADAPTING` 不是为了复制 Reviewed Handoff 的内部阶段，而是表达一个本仓库真实存在、且用户明确关心的差异：**中央 canonical source 已经落地，但完成合同中预先要求的 downstream consumer / repo / Host / server / normal entry 尚未全部适配并验证。**

三状态在逻辑上也能成立——把这种条目继续留在 DOING 即可——但会把“中央仍在开发”和“中央已完成、只差必要下游消费”混在一起。三状态再加一个 Phase 字段并没有更简单，反而形成两套需要同步的字段。七八个细状态则明显过重。

DONE 的边界应绑定 top-level idea 的 completion contract，而不是某一个 Reviewed Handoff task、PR 或中央 merge。DONE 至少表示：canonical owner source 已集成；冻结合同中的 required downstream adaptation 已完成或有明确 N/A/NO_CHANGE 依据；normal-entry / real-consumer 验证完成；关闭证据可长期定位；随后才关闭 tracking Issue。

本提案的主架构方向是对的，但当前 GitHub automation 语义存在一个会直接制造“假 DONE”的缺口，因此本轮不能 PASS。

## 2. 实际读取的仓库依据

本轮实际读取了最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md` v1.4
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` v1.4
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` v1.1
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `TODO.md`
- `docs/plugin-todos/README.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-todos/workflow-core.md`
- 当前 Proposal v1

并按需读取了：

- `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md`
- `docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_2.md`
- `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md`

这些材料共同支持一个重要现实：中央实现、release 或某个 workflow task 自己结束，并不能自动证明 downstream consumer 已经消费并验证该能力。056 的完成合同本身就把 canonical release、真实安装、Host 落地和 closure evidence 分开要求；058 也明确把中央 integration 后的 active repo adaptation 作为独立后续工作。

## 3. 独立 GitHub 现实核查

本轮独立检查了 GitHub 官方当前文档，结论如下。

1. Single-select field 最多支持 50 个选项，不存在“三状态上限”。
   - https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields

2. Board 可以以 Status、其他 single-select 或 iteration field 作为列。
   - https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout

3. GitHub Projects 内置自动化支持 issue closed -> Done；同时，新 Project 默认还启用 pull request merged -> Done。
   - https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations

4. Auto-add 支持 `is:issue`、`label:` 等过滤条件，因此可以只把专用 tracking Issues 加入 Project。
   - https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically

5. `gh project` / `gh project item-edit` 足以承担日常 item/field 生命周期维护；CLI 要求 token 具有 `project` scope。
   - https://cli.github.com/manual/gh_project
   - https://cli.github.com/manual/gh_project_item-edit

6. 另一个关键 GitHub 默认行为是：如果 PR 与 Issue 建立 GitHub 的 linked relationship，或使用支持的 closing keyword，PR merge 到默认分支会自动关闭该 Issue。
   - https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
   - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-auto-closing-issues

第 6 点是当前 Proposal 的实际 blocker。

## 4. 对核心设计的判断

### 4.1 四状态合理，且比“三状态 + Phase”更简单

推荐保留：

```text
TODO -> DOING -> ADAPTING -> DONE
```

原因是 `ADAPTING` 表达的是 top-level idea 的实质交付阶段，而不是 Planner / Critic / Implementation / Review 这类内部工作流步骤。

如果只用三状态，中央 source 已完成但 required consumer 尚未落地的条目只能继续叫 DOING；语义没有错，但 Board 无法回答用户特别关心的“哪些已经完成中央工作、现在卡在真实消费侧”。

若改成三状态 + Phase，则至少要同步两项字段，且可能出现 `Status=DOING, Phase=ADAPTING`、Phase 漂移或重复表达。对当前需求没有降低维护成本。

`WAITING / BLOCKED` 继续作为正交 label / next-action 信息，而不是第五个主状态，是正确的。

### 4.2 ADAPTING 不应无限扩大 DONE

Proposal 已经给出正确核心边界：只有 frozen completion contract 中的 required target，或执行中出现直接证据证明“不适配该 consumer 就不能成立原 completion claim”的目标，才阻止 DONE；未来可选 rollout 不应阻止关闭。

建议 v2 再写明一个 post-DONE 规则，但这不是本轮独立 blocker：

- 原 DONE 合同之外后来新增的可选 repo/server/consumer，应新建后续 work item，不追溯性扩大旧 DONE；
- 只有新证据证明原 DONE 所声称的范围当时其实没有成立，才按 regression 处理原 item 的 reopen / follow-up。

这样可以防止 `ADAPTING` 退化成“全世界所有未来 consumer 都要升级完”。

### 4.3 三层对象分工正确

我支持：

- plugin TODO = failure / evidence / maturity inbox；
- tracking Issue / Project item = top-level idea 的 execution lifecycle；
- Reviewed Handoff / Planner–Critic / Executor task = 某一轮具体设计、实现、review、integration evidence。

这与现有 `CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md` 中“TODO 标签不是第二套 workflow state machine”的边界一致，也避免把每个 task 都变成 Project 卡片。

原始 `NEW` 不自动进 Project、Planner triage 后才创建 tracking Issue，也是必要的 admission gate；否则只是把 Markdown 垃圾山复制成 Issue 垃圾山。

TODO 只保存 maturity/evidence 与 `tracking: #N`，执行状态留在 Issue/Project，足以避免双重维护，前提是后续不要再把 Board Status 复制回 Markdown。

### 4.4 Resolution commit 应是一枚 closure anchor，而不是“唯一实现 SHA”

Proposal 的方向成立。

跨 repo/server idea 往往天然有多个 component commits，甚至存在无 Git SHA 的 Host/server mutation，因此 Project 字段不应该塞成“所有 commit 列表”。推荐保持：

```text
Resolution commit = owner repo 的 canonical closure/evidence commit
```

Issue / closure evidence 中列出：

- central implementation / integration commits；
- required downstream repo commits；
- server / Host runtime evidence；
- normal-entry validation；
- N/A / NO_CHANGE 理由。

因此一个 `Resolution commit` 是**关闭证据的长期锚点**，不是声称“只有这个 commit 完成了全部代码”。

server mutation 没有 Git SHA 时，runtime evidence + owner repo closure commit 足够，但 runtime evidence 必须是 durable locator，不应只存在于一次临时 shell 输出。先形成 closure commit，再在 Project field / closing comment 回填其 SHA，也不会产生 self-reference 问题。

### 4.5 Codex/CLI 可以长期维护，不需要用户日常拖卡

稳态维护可以由 Planner/Codex 完成：

- 创建/更新/关闭 tracking Issue；
- `gh project item-add`；
- `gh project item-edit` 修改 Status、Area、Resolution commit；
- `gh project item-list` 做同步检查；
- GitHub built-in auto-add / close workflow 处理机械部分。

当前公开 `gh project` 命令集足以承担日常 item/field 操作。一次性的 view / built-in workflow bootstrap 应在 execution package 中明确采用当前真实支持的 Web UI / API / CLI 路线，不要把“稳态可 CLI 维护”误写成“所有 bootstrap 配置都有专用 gh project 子命令”。这不需要引入 daemon、controller、数据库或用户日常手工维护。

## 5. Stable blocker

### BOARD-01 — `issue closed -> DONE` 目前仍可被中间 PR merge 间接触发

**对应要求**

用户明确要求：

- central implementation / integration 完成不一定等于 top-level idea DONE；
- PR merge 不能自动代表 DONE；
- required downstream adaptation 未完成时 tracking Issue 必须保持 open。

**直接证据**

GitHub Projects 新建时默认启用 `pull request merged -> Done`。更关键的是，GitHub repository 默认会在“linked PR 合入默认分支”后自动关闭关联 Issue；closing keywords 也会建立这种关系。随后 Project 的 `issue closed -> Done` 会把这个 tracking Issue 标成 DONE。

因此，即使 Proposal 文本写了“禁止 PR merged -> idea DONE”，只要 implementation PR 被正常链接到 top-level tracking Issue，就存在：

```text
central implementation PR merged
-> tracking Issue auto-closed
-> Project issue-closed automation
-> Status = DONE
```

而 required adaptation 可能仍未开始。

**因果风险**

这是用户本次最关心的假完成风险。它不是文档措辞问题，而是 GitHub 当前默认行为会直接绕过 Proposal 的 completion contract。

**最小关闭条件**

Planner v2 只需把以下边界写入设计，不需要新增 GitHub Action、数据库或新状态机：

1. Auto-add 只收 tracking Issue，例如显式使用 `is:issue label:<tracking-label>`；implementation PR 不作为 lifecycle item。
2. 明确关闭 Project 默认的 `pull request merged -> Done` workflow。
3. 在 top-level tracking Issue 真正达到 DONE 前，中间 implementation/design PR **不得**使用会触发 auto-close 的 GitHub linked relationship，也不得使用 `Closes/Fixes/Resolves #N` 等 closing keywords。只保留不会自动关闭 Issue 的普通文本/URL reference，Issue body 继续保存 task/PR/commit locator。
4. `issue closed -> Done` 可以保留，但 Issue close 必须成为明确的 closure action：先核对 required adaptation checklist、normal-entry evidence、durable runtime evidence 与 Resolution commit，再关闭。
5. 不要求全仓关闭“linked PR auto-close”这一 GitHub repo 设置；避免为了一个 maintenance board 改变其他普通 Issue/PR 的合法工作方式。

**Owner**

Planner / repository-maintenance design。

## 6. Non-blocking clarification

建议 Planner 在 v2 顺手补两句即可：

- DONE 后出现的新 optional consumer 默认形成新的 follow-up item，不自动扩大旧 completion contract；
- execution package 区分一次性 Project bootstrap 与稳态 CLI maintenance，并在 bootstrap 时实际核对 `project` token scope 及当前 view/workflow 配置入口。

除此之外，不建议新增 Phase 字段、WAITING 主状态、同步 daemon、registry、ledger、controller 或 GitHub Action。

## 7. 审查结论

```text
RESULT = REVISE
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md
REVIEWED_PROPOSAL_COMMIT = e9804daf12611788f98d9ab3c2577c7744963c03
REVIEW_STAGE = DESIGN_PROPOSAL
STABLE_BLOCKERS = BOARD-01
```

这次 REVISE 不否定四状态、idea/task/TODO 分层、Resolution commit 或 CLI 长期维护路线。只要求把 GitHub 的真实 auto-close 链条封住，再复核 v2。

本 review 不授权创建 GitHub Project、修改 Issue、修改 AGENTS/TODO/plugin source、执行 backfill、启动 Codex、修改 Bridge Kit 或触碰 production/server/Host。
