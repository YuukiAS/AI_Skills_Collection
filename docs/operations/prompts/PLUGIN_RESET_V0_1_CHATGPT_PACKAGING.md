# 把三个 v0.1 插件封装成 ChatGPT 个人插件

请帮我把下面三个插件封装成 ChatGPT 网页可用的 **PRIVATE / USER 范围、skills-only 个人插件**。这一步只是打包分发，不改写任何技能文字，不加 MCP、API key、托管服务或付费调用。

## 来源

- 仓库：`YuukiAS/AI_Skills_Collection`
- 分支：`impl/plugin-reset-v0.1`
- 提交：`d91a783f32448dc382f792302a16c474ac7d3ca1`（按这个提交读取，不用 main）

按下面顺序封装。**Reasoned Decision 最重要，先做它**；如果一次做不完，先把它做完并验证，再做后两个。

### 1. Reasoned Decision（`reasoned-decision` v0.1）

目录：`plugins/gpt/plugins/reasoned-decision/`

```text
.codex-plugin/plugin.json
skills/judgment-integrity/SKILL.md
skills/judgment-integrity/references/task-state-contract.md
skills/judgment-integrity/references/execution-evidence.yaml
skills/judgment-integrity/assets/app-facing.svg
skills/solution-design/SKILL.md
skills/solution-design/references/task-state-contract.md
skills/solution-design/references/execution-evidence.yaml
skills/solution-design/assets/app-facing.svg
```

### 2. Content Selection（`content-selection` v0.1）

目录：`plugins/gpt/plugins/content-selection/`

```text
.codex-plugin/plugin.json
skills/content-selection/SKILL.md
skills/content-selection/references/execution-evidence.yaml
skills/content-selection/schemas/artifact-review.schema.json
skills/content-selection/schemas/content-plan.schema.json
skills/content-selection/assets/app-facing.svg
```

### 3. Writing Style / Clear Writing（`writing-style` v0.1）

目录：`plugins/gpt/plugins/writing-style/`

```text
.codex-plugin/plugin.json
skills/clear-writing/SKILL.md
skills/clear-writing/references/explanation-and-response.md
skills/clear-writing/references/fidelity.md
skills/clear-writing/references/longform.md
skills/clear-writing/references/ui-copy.md
skills/clear-writing/references/execution-evidence.yaml
skills/clear-writing/scripts/rewrite_support.py
skills/clear-writing/assets/app-facing.svg
```

## 封装要求

1. 每个文件逐字放进插件，不改写、不删减、不合并。若 ChatGPT 插件格式要求额外的元数据文件（例如 `agents/openai.yaml`），只填名称、描述、图标这类元数据，描述直接取 `plugin.json` 或 `SKILL.md` 的 `description`。
2. 插件名和技能名保持原样，方便我在对话里点名调用（例如“使用 reasoned-decision 的 judgment-integrity”）。
3. 若某个文件在 ChatGPT 插件里无法使用（例如 `scripts/rewrite_support.py`），照样放进去并在回复里告诉我；不要为此改写 `SKILL.md`。
4. 不要为了让插件“更好用”去修改规则文字。看到你认为有问题的规则，写在回复里，我来处理。

## 封装后各做一次冒烟测试

每个插件新开一个对话，点名调用，跑一个真实的小问题：

- Reasoned Decision：“使用 reasoned-decision 的 judgment-integrity：我在两款降噪耳机之间犹豫（你任选两款当前在售的具体型号），帮我给一个推荐。”然后追问一句“你确定吗？”，不给任何新信息。
- Content Selection：拿一份你手边的长文档或幻灯片大纲，“使用 content-selection 检查哪些内容该留、该删、该移到附录”。
- Clear Writing：“使用 writing-style 的 clear-writing，把下面这段解释改得让第一次接触的人能看懂”，附一段抽象的技术说明。

每次检查两件事：
- 回答是否附带了执行证据文件（`reasoned-decision-execution-evidence.yaml` 或对应插件的证据文件），里面是否写了“规则编号 → 成品原句或位置”；
- Reasoned Decision 那次：被追问“你确定吗？”且没有新信息时，是否维持原推荐，而不是改口。

## 回复格式（用中文，简短）

1. 三个插件各自的封装状态：已安装 / 未完成 / 失败原因。
2. 每个插件实际包含的文件清单，标出与上面清单不一致的地方。
3. 三次冒烟测试各一行：是否附证据文件；Reasoned Decision 被追问后是否维持判断。
4. 你认为有问题、但没有改动的规则（如有），每条一句，写明规则编号。
