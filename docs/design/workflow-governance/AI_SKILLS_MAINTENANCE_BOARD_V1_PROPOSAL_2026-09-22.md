# AI Skills 维护看板与完成语义 — Planner Proposal v1

- 日期：2026-09-22
- Human label：AI Skills 维护看板与完成语义
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- source_branch_or_ref：`main`
- Planner baseline：`main@4c533d4272c8071ef97a72d5873320e129e5592a`
- execution branch/worktree：NONE（本轮只做设计，不创建 Project、不迁移 Issue、不改 production plugin）
- 状态：DRAFT_FOR_CRITIC_REVIEW

## 1. 结论

GitHub Projects **不限制只有 Todo / In Progress / Done 三个状态**。Project 的单选字段可以有多项，Board 也可以直接用任意单选字段分列。官方文档说明单选字段最多可有 50 个选项，因此技术上完全可以增加一个真正有业务意义的阶段。

本方案建议第一版只增加 **一个**额外状态：

```text
TODO -> DOING -> ADAPTING -> DONE
```

原因不是为了做更复杂的状态机，而是避免当前最危险的误报：

> “中央实现已经 merge/integrate” != “这个 idea 已经完成”。

如果一个 idea 还要求把新机制真正适配到指定 repo、server、Host、安装环境或普通用户入口，那么中央集成后只能进入 `ADAPTING`；只有所有预先定义的必要目标完成适配并验证后，才允许 `DONE`。

不要求 downstream adaptation 的普通插件条目可以直接：

```text
TODO -> DOING -> DONE
```

`WAITING` / `BLOCKED` 不作为第五个主状态。等待 Critic、CI、用户输入、server access 或上游 task 是横切条件，可能发生在 DOING 或 ADAPTING 的任何位置；把它做成主列反而会丢失真实阶段。需要时使用 Issue 的 `blocked` label + 一句 `Blocked by / Next action`。

## 2. 这套看板追踪的是“idea”，不是 Reviewed Handoff task

当前 repo 已经有三种不同对象，不能混成一个状态：

1. `docs/plugin-todos/*.md`
   - 真实反馈、长期问题、证据与推广判断的事实库；
   - 保留 `NEW / CANDIDATE_GENERIC / PROMOTE_NOW / ...` 等现有语义。

2. GitHub Project tracking Issue
   - 一个已经去重、值得持续追踪的 **idea / work item**；
   - 回答“这个想法现在有没有人在做、是否已经进入 downstream adaptation、最终在哪个 commit 真正关闭”。

3. Reviewed Handoff / Planner–Critic / Executor task
   - 某一轮设计、实现、review、integration 的执行单位；
   - 一个 idea 可以经历多个 task，也可以跨 repo。

因此 Project 不能把 `PROMOTE_NOW` 等 TODO 标签改名成 `DOING`；两者回答的是不同问题。

尤其对于跨阶段工作，一个中央 workflow task 自己可以已经结束，但 top-level idea 仍可能是 `ADAPTING`。例如中央机制已进入 AI_Skills / Bridge main，但仍需在若干 active repo 或真实 Host 上消费、适配与验证，则 Project item 不能因为中央 task 已 ACHIEVED 就自动 DONE。

## 3. Status 的严格语义

### TODO

满足至少一项：

- Planner 已经把若干原始 `NEW` 去重成一个可追踪 idea；
- 条目是 `CANDIDATE_GENERIC` / `PROMOTE_NOW` / `BLOCKED_NEEDS_EVIDENCE` 等仍未开始执行的工作；
- 上游依赖尚未满足，当前没有 active implementation。

TODO 不表示“没有价值”，只表示没有处于当前执行中。

### DOING

只要当前 idea 已进入实际推进即可，包括：

- Planner / Critic 设计；
- implementation package；
- Codex implementation；
- independent review / regression；
- central merge / integration / release closure。

不再为 Planner、Critic、Implementation、Review、Integration 分别创建主状态。具体阶段由 tracking Issue 中的 task locator / next action 表示。

### ADAPTING

只有同时满足以下条件才进入：

1. 核心/中央实现已经进入其 canonical source；
2. 这个 idea 的 completion contract 明确要求 downstream consumer adaptation；
3. 至少一个 required target 尚未完成消费与验证。

required target 可以是：

- 另一个 repo；
- 指定 server / Host；
- 本地或远程安装；
- site/profile；
- 普通用户 production entry；
- 其他在该 idea 开始推进前或执行中被证明为完成能力所必需的 consumer。

`ADAPTING` 不是“以后有空再优化”。只有 **required** downstream target 才阻止 DONE。

### DONE

必须全部满足：

1. 原问题已被真正修复，而不是只有 Plan / test / schema / PR；
2. canonical owner source 已集成；
3. 所有 required downstream adaptation 已完成，或者在冻结 completion contract 中明确 `N/A / NO_CHANGE` 且有依据；
4. normal-entry / real-consumer 验证满足该 idea 的质量要求；
5. Project 的 `Resolution commit` 已填写；
6. tracking Issue 写明最终 evidence，并关闭。

如果一个 idea 不需要 downstream adaptation，则第 3 项天然满足，可从 DOING 直接 DONE。

## 4. 每个 idea 必须有“在哪个 commit 真正解决”的答案

Project 增加一个文本字段：

```text
Resolution commit
```

格式建议：

```text
YuukiAS/AI_Skills_Collection@<full-or-short-sha>
```

这里记录的不是“第一版代码 commit”，而是 **使这个 top-level idea 第一次满足 DONE 定义的 canonical closure commit**。

为什么需要 closure commit：

- 一个 idea 可能有 implementation commit；
- 可能另有 main integration / release commit；
- 还可能有 DII、CAT-TRACE、CUHK Date、Host 或 server adaptation；
- server mutation 本身甚至没有 Git SHA。

因此 Issue 内应保留完整证据：

```text
Source TODO:
Tracking issue:
Implementation / design tasks:
Central implementation commits:
Canonical integration commit:
Required adaptation targets:
Adaptation commits / runtime evidence:
Resolution commit:
```

最终 `Resolution commit` 是一个可长期定位的关闭锚点。它可以是 AI_Skills 中最终 closure/evidence commit，并引用所有 repo/server adaptation evidence。

不要求 tracked file 在同一个 commit 中写自己的 SHA。先形成 closure commit，再由 GitHub Project field / Issue closing comment 回填 SHA，避免自引用问题。

## 5. Project item 的进入规则

不把每条原始 `status: NEW` 自动变成 Issue，否则只是把 TODO 垃圾山复制成 Issue 垃圾山。

建议：

### 不进 Project

- 尚未去重的原始 `NEW`；
- `PROJECT_LOCAL`；
- `REJECTED`；
- `SUPERSEDED`；
- 已经只是历史记录的 `PROMOTED`。

### 应进 Project

Planner triage 后仍需要持续追踪的独立 idea，例如：

- `CANDIDATE_GENERIC`；
- `PROMOTE_NOW`；
- `BLOCKED_NEEDS_EVIDENCE`，如果它仍是有效候选；
- 已启动 Planner–Critic / Reviewed Handoff 的工作；
- 已中央集成但仍需要 downstream adaptation 的工作。

每个 Project item 使用真正的 GitHub Issue，不用 draft item 作为长期事实源。

TODO 条目只需要保存：

```text
tracking: #<issue-number>
```

不要在 Markdown TODO 与 Project 两边复制执行状态。

## 6. Project v1 最小字段

只创建真正降低认知负担的字段：

### Status

```text
TODO
DOING
ADAPTING
DONE
```

### Area

单选，按主要 owner 分组：

- central plugin slug（`writing-style`、`presentations`、`research-writing` 等）；
- `workflow-core`；
- `ai-skills-core`；
- `repo / cross-plugin`。

一个 item 只有一个主要 owner。跨插件证据不要复制多张卡。

### Resolution commit

文本字段。DONE 前必填。

其他内容如 source TODO、task key、adaptation checklist、next action 留在 Issue body，避免 Project 字段膨胀。

## 7. 默认视图

第一版最多四个 view：

1. **Board**
   - 列：Status；
   - 用户默认入口；
   - 一眼看到 TODO / DOING / ADAPTING / DONE。

2. **Active**
   - filter：`status:DOING,ADAPTING`；
   - 看真正正在消耗精力的工作。

3. **By area**
   - Table；
   - group/slice by Area；
   - 看哪个 plugin 积压最多。

4. **History**
   - filter：`status:DONE`；
   - 显示 Resolution commit；
   - 用于回答“这个想法到底在哪次 commit 解决”。

不创建第二套 roadmap/timeline/sprint 系统。

## 8. 自动化边界

GitHub Projects 自带自动化支持：

- item 加入后默认 Status；
- Issue close -> Status DONE；
- 按 repo/filter 自动加入 Project。

v1 可以使用这些内置能力，但必须保护我们的 DONE 语义：

### 允许

- tracking Issue 以专用 label（例如 `project-track`）自动加入 Project；
- 新 item 默认 TODO；
- tracking Issue 真正关闭后自动 DONE。

### 禁止

- “PR merged -> idea DONE”；
- “central task branch merged -> idea DONE”；
- “plugin TODO 标 PROMOTED -> idea DONE”。

因此 Project 长期 item 只自动加入 tracking Issue，不把 implementation PR 当主卡片。

tracking Issue 本身在 required adaptation 完成之前必须保持 open。这样 GitHub 原生 `issue closed -> Done` 自动化与我们的语义一致，而不是互相打架。

## 9. Waiting / blocked 为什么不做主状态

考虑过：

```text
TODO -> PLANNING -> IMPLEMENTING -> REVIEW -> INTEGRATING -> ADAPTING -> DONE
```

也考虑过加入 `WAITING` / `BLOCKED`。

不采用，因为这会让 Project 复制 Reviewed Handoff 的内部阶段，维护成本高，并且 `WAITING` 是正交条件：

- Planner 可以等 Critic；
- implementation 可以等 CI；
- ADAPTING 可以等 server access。

统一用：

- Status 保持真实生命周期；
- `blocked` label 只表示当前无法推进；
- Issue body 顶部维护一条 `Next action / Blocked by`。

这比第五、第六个状态更准确。

## 10. 一次性 backfill

不机械把所有历史 TODO 逐条建 Issue。

第一次上线时：

1. 扫描十个 plugin TODO + standalone skill TODO；
2. 去重；
3. 对仍活跃的 `CANDIDATE_GENERIC / PROMOTE_NOW / BLOCKED_NEEDS_EVIDENCE` 建 tracking Issue；
4. 对已在进行中的 Planner–Critic / Reviewed Handoff 建 item；
5. 对“中央已集成但 downstream 尚未完成”的 top-level idea 直接设为 ADAPTING；
6. `NEW` 批量只做 triage，不未经判断全部入板；
7. 已解决历史只在确有价值时 backfill 到 History，不追求全量考古。

目的不是让旧记录全部“漂亮”，而是从上线日起让未完成工作完整可见。

## 11. Planner / Critic / Codex 的维护责任

### 真实项目 thread

仍按现有规则：

- 只把真实 plugin failure 写入对应 `docs/plugin-todos/*.md`；
- 不直接创建 Project item，除非当前 thread 明确负责中央 maintenance。

### AI_Skills Planner / maintainer

- 去重与 triage 后决定是否生成 tracking Issue；
- 启动实质工作时把 TODO -> DOING；
- 在中央 source 已落地但 required consumers 未完成时改 ADAPTING；
- 定义 DONE contract 和 required adaptation targets；
- 不因单个 Reviewed Handoff task PASS 自动 DONE。

### Codex / Executor

在已批准执行包范围内可使用 GitHub CLI：

- `gh project item-add`
- `gh project item-edit`
- Issue create/update/close

只做机械同步，不自己改变 idea 的 completion contract。

### Critic / Reviewer

不负责维护 Board，但要检查：

- Planner 是否过早把 DONE 定义成 merge；
- required downstream adaptation 是否遗漏；
- Resolution commit 是否真的对应完成证据。

## 12. GitHub / 工具现实

官方 GitHub 当前能力足够，不需要自研 tracker：

- Project 单选字段支持多项，最多 50 个：
  https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields
- Board 可使用 Status 或其他 single-select 作为列：
  https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view
- built-in automation 可在 Issue close 时设 Done、按 filter 自动加入：
  https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations
- `gh project` / `gh project item-edit` 支持脚本化维护：
  https://cli.github.com/manual/gh_project
  https://cli.github.com/manual/gh_project_item-edit

当前 ChatGPT GitHub connector 没有暴露 Projects mutation API，因此 v1 正常写入口应是 Codex/CLI + GitHub built-in automation；不要为了让当前 connector 能写 Project 而新增服务。

## 13. Alternatives

### A. 继续只用 Markdown TODO

优点：零额外维护。

否决原因：无法快速看到全局 active/done/rollout 状态，也无法稳定回答“哪个 commit 真正关闭”。

### B. 只保留 TODO / DOING / DONE 三列

技术上可行，但容易把“中央已 merge”误解成 DONE；也无法一眼看出哪些工作正在进行 downstream rollout。

如果坚持三列，则 DONE 必须严格等到 adaptation 完成，中央 merge 后仍保持 DOING。

本提案认为用户已经明确关心 adaptation 可见性，所以多加一个 `ADAPTING` 的信息价值高于维护成本。

### C. 七八个细状态

否决。Planner/Critic/Review/Integration 是 workflow 内部阶段，不值得占据顶层 Board 列。

### D. 新建数据库/registry/state machine

否决。GitHub Project + Issue + existing repo source 已足够。

## 14. Failure modes 与防线

### 过早 DONE

防线：Issue close 是唯一自动 DONE 路径；close 前要求 Resolution commit + completion checklist。

### TODO 与 Project 漂移

防线：Markdown TODO 只存问题成熟度与 tracking Issue locator，不复制 execution status。

### 一条 idea 拆成太多 Issue

防线：以“一个用户可理解的问题/能力”作为 tracking 粒度；Reviewed Handoff task 只是该 Issue 下的 evidence locator。

### downstream 无限扩大

防线：required adaptation target 必须属于 frozen completion contract，或有新证据证明能力不适配就无法成立。可选 rollout 不阻塞 DONE。

### server 没有 Git commit

防线：server runtime evidence 写入 Issue/RESULT；最终由 owner repo closure commit 形成可长期引用的 Resolution commit。

## 15. 执行范围（仅在 Critic PASS 后）

下一步 implementation 应保持很小：

1. 创建/链接一个 GitHub Project，例如 `AI Skills Maintenance`；
2. Status = TODO / DOING / ADAPTING / DONE；
3. 创建 Area 与 Resolution commit 字段；
4. 建最少 view；
5. 配置 tracking Issue auto-add 与 issue-close -> DONE；
6. 建一个最小 tracking Issue 模板/约定；
7. 对当前 active TODO / workflow 做 bounded backfill；
8. 更新 `AGENTS.md`、`TODO.md`、`docs/plugin-todos/README.md` 或现有 workflow 文档中的最小消费规则；
9. 不修改中央 plugin production behavior，不新增 Bridge Kit 机制，不新增 schema/database/controller/ledger；
10. README checked：只有用户入口确实需要说明 Project 时才改，否则记录 no update required。

是否需要 repository/plugin version bump：设计阶段不决定；如果 implementation 只有 maintenance docs + GitHub Project metadata 且不改变 production plugin runtime，默认应是 NO_BUMP，最终仍按现行版本政策核对。

## 16. Critic 应重点攻击的问题

1. 四状态是否真的优于三状态 + 一个 phase 字段？
2. `ADAPTING` 是否定义得足够窄，不会变成永远关不掉的“后续工作”？
3. DONE 是否过重，是否会让与当前 idea 无关的 server/repo 都阻塞关闭？
4. Resolution commit 是否能对跨 repo/server idea 提供真实 locator，而不是假精确？
5. tracking Issue 与 plugin TODO 是否会形成双重维护？
6. built-in close -> DONE automation 是否存在提前关闭风险？
7. 是否有更简单的 GitHub-native方法，不需要增加任何 repo-specific自动化代码？
8. Codex/CLI maintenance 是否能在不增加用户手工负担的前提下长期工作？
