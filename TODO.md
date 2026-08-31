# AI Skills Collection TODO

这是仓库级 TODO 首页，作用和根目录 `CHANGELOG.md` 类似：提供一个统一入口，指向各个 plugin 自己的长期 TODO。

**本文件不是第二份 TODO 清单。** 具体问题、状态、证据和后续动作只维护在 `docs/plugin-todos/<plugin>.md`，这里不复制条目、不维护数量，也不单独决定优先级，避免长期漂移。

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

详细规则见 [docs/plugin-todos/README.md](docs/plugin-todos/README.md) 和 [docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md](docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md)。

## 真实项目怎么把问题带回来

真实项目（例如 TRACE、CARE、Distributed Imaging）首先在**自己的仓库**记录用户看到的实际问题，不直接在这里写“通用规则”。

对于采用任务制的项目，默认把本轮记录放进：

```text
results/<task_key>/result.md
```

并加入一个简短的：

```text
## AI_Skills feedback handoff

candidate plugin: <可能相关的 plugin>
raw problem: <用户实际看到的问题>
evidence: <项目中的 PDF/render/result/review 路径>
project-only boundary: <明显只属于当前项目的内容>
```

如果项目本身已有更合适的 review / revision result 文件，可以放在那里，但必须留下一个稳定、可引用的位置。

之后由 **AI_Skills Planner / maintainer** 读取这份项目记录，再检查现有 plugin TODO 和当前实现，负责：

- 判断问题是不是只属于当前项目；
- 和已有 TODO 合并，避免重复；
- 如果插件本来已经有规则但真实输出仍失败，则记录为实际实现问题，而不是再写一条近义规则；
- 只有真的可以推广到别的项目时，才写入对应 `docs/plugin-todos/<plugin>.md`；
- 只有证据足够时，才进入后续插件修改。

项目 Executor 可以提供候选判断，但不负责最终把项目经验改写成中央规则。

## TODO、项目记录、CHANGELOG 的区别

- 项目仓库的 `result.md` / review / revision note：记录这次真实任务发生了什么。
- `docs/plugin-todos/<plugin>.md`：中央插件以后可能要改什么。
- `TODO.md`：只负责导航到各 plugin TODO。
- `docs/plugin-changelogs/<plugin>.md`：这个 plugin 已经在哪个版本正式改了什么。
- 根 `CHANGELOG.md`：整个 AI_Skills_Collection 每次正式发布改了什么。

这样项目事实、待办和已经发布的变化不会混在一起。
