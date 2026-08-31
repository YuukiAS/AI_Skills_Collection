# Per-plugin Long-Term TODO Inboxes

根目录 [`TODO.md`](../../TODO.md) 是统一导航页；本目录保存十个中央 Marketplace plugin 的具体长期 TODO。

这里记录的是 **plugin 自己的问题**。如果用户在 TRACE、CARE、Distributed Imaging 或其他真实项目里调用某个 plugin，发现 plugin 的输出、路由、返修、检查或工作方式有问题，应该直接把这次真实问题记到对应的 `docs/plugin-todos/<plugin>.md`，不要先在项目 repo 再维护一份“插件问题清单”。

- `workflow-core.md`
- `ai-skills-core.md`
- `writing-style.md`
- `research-writing.md`
- `presentations.md`
- `scientific-visualization.md`
- `web-development.md`
- `statistical-modeling.md`
- `bioinformatics.md`
- `medical-imaging.md`

## 先分清：项目问题还是 plugin 问题

项目自己的科学、产品、代码和实验问题继续留在项目 repo。

例如 TRACE 的新实验、theorem 写法、数据解释、模型选择，属于 TRACE。

但如果问题是“我用了 `presentations`，结果箭头穿字 / 已接受页面被改坏 / 没按要求继续改现有 PPT”，那就是 `presentations` 的问题，应直接写这里。

一个简单判断是：

> 如果换成另一个真实项目，plugin 仍然可能犯同样的错吗？

如果答案大概率是“会”，就应该优先记到 plugin TODO。

## 真实项目 thread 可以直接写 `NEW`

项目 thread 不需要先在自己的 repo 写一份中转记录，也不需要自己证明问题已经足够通用。

它只负责把这次真实失败写清楚，并在对应 plugin TODO 里新增一个 `NEW` 条目：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <实际输出的路径、链接、commit 或 render>
problem: <用户实际看到的问题>
project-specific context: <哪些细节只属于当前项目>
```

这一步的目标是保存真实证据，不是发明永久规则。

AI_Skills_Collection 是公开仓库时，`source` / `evidence` / `project-specific context` 只写到足以定位和理解问题的程度。不要把未公开论文正文、私有数据、受限链接内容、个人信息或项目秘密复制进中央 TODO；必要时只保留本机路径、task id、commit 或一句不泄露内容的说明。

不要要求项目 thread 此时填写 `target layer`、`candidate action` 或 `promotion gate`。这些属于后面的中央整理工作。

## AI_Skills Planner / maintainer 负责整理

Planner 在处理 `NEW` 条目前必须先检查：

1. 当前 plugin 是否已经有同类规则；
2. 本 plugin TODO 是否已有同一个问题；
3. 其他真实项目是否出现过类似失败；
4. 哪些细节只是当前项目自己的内容。

然后再处理：

- 已有规则但真实输出又失败：这是实际执行问题，不再造一条近义规则；
- 已有 TODO：把新的真实案例合进去，不复制条目；
- 只属于当前项目：标成 `PROJECT_LOCAL`，必要时从活跃区清理，但不要把它扩成通用规则；
- 新的通用候选：整理成 `CANDIDATE_GENERIC`；
- 证据已经足够：升到 `PROMOTE_NOW`，再单独开一轮修改 plugin；
- 已经被更强规则覆盖或方向不成立：`SUPERSEDED` / `REJECTED`。

跨多个 plugin 的问题只指定一个主要 owner，其他文件只引用，避免重复维护。

## Planner 整理后的完整格式

项目 thread 新增 `NEW` 时只需要上面的最小字段。Planner 完成整理后，可以补充：

```text
### <short title>
status: NEW | PROJECT_LOCAL | CANDIDATE_GENERIC | PROMOTE_NOW | BLOCKED_NEEDS_EVIDENCE | PROMOTED | REJECTED | SUPERSEDED
source: <real project / artifact / user feedback / issue>
evidence: <repo path / review / render / result>
target layer: routing | reasoning | rendering | qa | writing | distribution | external-runtime
problem: <what actually failed>
project-specific context: <details that must not become generic rules>
candidate action: <smallest plausible generic change>
promotion gate: <what evidence is still required>
```

## Cleanup rule

- `PROMOTED` 项在正式发布后可以压缩到“Recently promoted”摘要，不永久堆积实现细节。
- `PROJECT_LOCAL`、`REJECTED`、`SUPERSEDED` 可以在判断完成后从活跃区清理或放进短历史区。
- 不允许为同一问题在多个 plugin TODO 重复维护。
- 不要把项目的科学 TODO 搬进这里；这里负责的是 plugin 的问题，不是项目本身的研究计划。

详细长期流程见：

`docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
