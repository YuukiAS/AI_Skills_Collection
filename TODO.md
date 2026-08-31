# AI Skills Collection TODO

这是整个仓库的待办入口，作用和根目录 `CHANGELOG.md` 类似：这里只负责告诉人“应该去哪个 plugin 的 TODO 看”，不在这里复制十份具体问题。

真正的插件待办都放在：

```text
docs/plugin-todos/<plugin>.md
```

## Plugin TODO 入口

| Plugin | TODO |
|---|---|
| `workflow-core` | [docs/plugin-todos/workflow-core.md](docs/plugin-todos/workflow-core.md) |
| `ai-skills-core` | [docs/plugin-todos/ai-skills-core.md](docs/plugin-todos/ai-skills-core.md) |
| `writing-style` | [docs/plugin-todos/writing-style.md](docs/plugin-todos/writing-style.md) |
| `research-writing` | [docs/plugin-todos/research-writing.md](docs/plugin-todos/research-writing.md) |
| `presentations` | [docs/plugin-todos/presentations.md](docs/plugin-todos/presentations.md) |
| `scientific-visualization` | [docs/plugin-todos/scientific-visualization.md](docs/plugin-todos/scientific-visualization.md) |
| `web-development` | [docs/plugin-todos/web-development.md](docs/plugin-todos/web-development.md) |
| `statistical-modeling` | [docs/plugin-todos/statistical-modeling.md](docs/plugin-todos/statistical-modeling.md) |
| `bioinformatics` | [docs/plugin-todos/bioinformatics.md](docs/plugin-todos/bioinformatics.md) |
| `medical-imaging` | [docs/plugin-todos/medical-imaging.md](docs/plugin-todos/medical-imaging.md) |

详细规则见 [docs/plugin-todos/README.md](docs/plugin-todos/README.md)。

## 以后在真实项目里发现问题，记到哪里？

先问一个最简单的问题：

> **这个问题是项目本身的问题，还是我正在用的 plugin 做得不好？**

### 项目本身的问题 → 留在项目 repo

例如 TRACE 里：

- CAT-TRACE 还要补哪个实验；
- 某个 theorem 到底应该怎么写；
- Madagascar 数据应该怎么解释；
- 下一步模型要不要加新 prior；
- 某段代码本身有 bug。

这些属于 TRACE，自然继续写 TRACE 的 `ROADMAP.md`、任务结果、模型/数据文档等合适位置。

### Plugin 做得不好 → 直接写回 AI_Skills_Collection

例如在 TRACE 里调用 `presentations` 后发现：

- 箭头穿过文字；
- 已经接受的页面被返修时又改坏；
- 公式页层次还是很差；
- 图太小，投影时看不清；
- 本来要求“继续改现有 PPT”，plugin 却重新生成了一套。

这些问题本质上是 `presentations` 的问题，所以**不要再把它们当成 TRACE 的科研 TODO 保存一份**。直接读取：

```text
AI_Skills_Collection/TODO.md
AI_Skills_Collection/docs/plugin-todos/presentations.md
```

然后把这次真实问题作为 `NEW` 记录进去。

同理：报告插件的问题写 `research-writing.md`，统计插件的问题写 `statistical-modeling.md`，医学影像插件的问题写 `medical-imaging.md`。

## 真实项目 thread 应该怎样写一条新问题？

项目 thread 不需要自己发明“通用规则”，也不需要先在项目 repo 做一份中转记录。

它只需要把事实写清楚：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <能定位到实际输出的路径、链接、commit 或 render>
problem: <用户实际看到了什么问题>
project-specific context: <哪些细节只属于当前项目，不应该变成通用规则>
```

例如：

```text
### Existing-deck revision changed an accepted slide
status: NEW
source: TRACE / CAT-TRACE group-meeting revision
evidence: <实际 PDF / render / task 路径>
problem: 用户只要求修改 P10，但上轮已经接受的 P9 也发生了明显变化。
project-specific context: P9/P10 的 CAT-TRACE 科学内容本身不应成为通用规则。
```

这里先记录**真实失败**，不要急着写“以后所有 PPT 必须怎样”。

## 谁负责把这些问题整理成真正的插件规则？

AI_Skills_Collection 的 Planner / maintainer 负责。

它会先看：

1. 这个 plugin 现在是不是已经有同样的规则；
2. 对应 plugin TODO 里是不是已经有同一个问题；
3. 其他真实项目有没有遇到过类似问题；
4. 哪些部分只是当前项目的内容。

然后再决定：

- 已有 TODO → 把这次真实案例合进去，不再复制一条；
- 已有规则但还是做错 → 说明实际执行有问题，重点查实现；
- 只是项目特殊情况 → 标清后不升级成通用规则；
- 确实是新的通用问题 → 整理成长期候选；
- 证据已经足够 → 再单独开一轮去修改 plugin。

所以职责很简单：

> **真实项目 thread 负责把 plugin 的真实问题直接记回对应 plugin TODO；AI_Skills Planner 负责去重、提炼和决定以后到底怎么改。**

## TODO 和 CHANGELOG 怎么区分？

- `TODO.md`：整个 AI_Skills_Collection 的待办总入口。
- `docs/plugin-todos/<plugin>.md`：某个 plugin 还存在哪些问题、以后要改什么。
- `docs/plugin-changelogs/<plugin>.md`：这个 plugin 已经在哪个版本正式解决了什么。
- 根 `CHANGELOG.md`：整个 AI_Skills_Collection 每次正式发布改了什么。

不要在项目 repo 和中央 plugin TODO 同时维护同一份“插件问题清单”。