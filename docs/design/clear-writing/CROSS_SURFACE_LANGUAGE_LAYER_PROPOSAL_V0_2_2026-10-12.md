# Clear Writing 跨 ChatGPT / Codex 通用表达层 — 精简架构提案 v0.2

- 日期：2026-10-12
- 状态：`ARCHITECTURE_PASS_USER_RELAYED / EXECUTION_PACKAGE_DRAFT`；尚无执行前 Critic PASS
- 追踪：`YuukiAS/AI_Skills_Collection#13`
- 仓库：`YuukiAS/AI_Skills_Collection`
- 规划分支：`planner/clear-writing-cross-surface-v0.1`
- 已审架构对象：该分支 `819f861de7dc626f473390df8a9c42b70d24dd92` 的 v0.1 提案、能力矩阵和交接
- 最新主线预检：`main@34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b`；与已审设计分支相比的后续主线修改仅在 `docs/plugin-todos/workflow-core.md`，尚无直接 Clear Writing 生产冲突
- 现有正式身份：`writing-style` / Clear Writing 0.4；仓库 `VERSION=5.4.4`
- 来源审查身份：用户在 2026-10-12 当前对话转述“独立 Critic 对精确 v0.1 架构给出 PASS，但只批准精简路线”；**该 Critic 结论尚未作为审查文件写入仓库。本文件不是 Critic 回执，不声称已实际见到原 Critic 全文。**
- 同版执行文件：`CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_2_2026-10-12.md`、`CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_2_2026-10-12.md`、`docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_2.md`、`docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_2.md`
- 权限：**本轮仅起草与独立审查；无权修改正式技能源、版本、插件、真实 Project/个性化设置，也不得启动 Executor、付费调用、发布或合并。**

## 1. 用户目标与边界

Clear Writing 是跨 ChatGPT 与 Codex 共用的通用读者表达能力，不是“六个写作技能每次全部运行”，也不是自动推理、事实核查、科学判断或视觉设计工具。

核心的正常体验：
1. 有 Project 的 ChatGPT 直接问技术、科研、统计、软件架构、服务器或生活问题时，**第一次完整回复**就以当前目标语言自然回答、先给有意义的判断、少非必要英文、少机械换行和状态日志，并保持必要精确字符串。用户不需每轮 `@Clear Writing`。
2. 无 Project 的 ChatGPT 聊天遵守当前个人个性化语言习惯，并在合适时自动使用已安装技能；一轮临时英文或纯机器请求不会污染之后的默认语言。
3. Codex 完成软件、界面、幻灯片、报告、中文技术文档及英文科研文字任务时，依据实际交付物选择合适的语言能力；领域负责人拥有事实、目标、结构、专业语义与真实渲染验收权。
4. 更自然不得换来科学事实丢失或错报完成：必须保留数字、公式、引用、主体、时态、因果、条件、否定、授权、权限、安全、适用边界、不确定性以及真正需要逐字匹配的代码/字段/路径/协议。

已曝光的 C5–C11、跨轮中文失效、用户提供的网页架构回答以及 050–055 长文重写失败可用于开发回归，不得作为最终未见样本，也不得把私有对话原文提交公开仓库。

## 2. 架构阶段裁定的落实

本 v0.2 **替代早先 v0.1 中“全面重命名”推荐**，只采纳用户转述的独立 Critic 允许路线：

- `writing-style` 和展示名 Clear Writing **不改**，不迁移顶级插件身份；
- `chinese-prose`、`scientific-prose`、`scientific-rewrite`、`product-ui-copy`、`writing-fidelity` 五项技能正式名称、目录、生成包路径的现有标识全部保留；不得默认实施 `chinese-writing`、`scientific-english`、`source-rewrite`、`interface-writing`、`meaning-fidelity` 等改名；
- 唯一新增正式技能名称：`response-clarity`，用于**普通面向人的解释性回答**，不重造整个中文写作功能；
- 对现有 `chinese-prose` 的名称/描述和新增 `response-clarity` 的正例、反例、边缘任务做最小区分，重点修技能自动发现与误路由；
- 保留 `scientific-rewrite` 的中文/中文主导科研技术长文重写链：含义映射 → 读者计划 → 中文实现 → 整篇组织 → 保真与有限修复；不要把它复用成普通聊天回答处理器；
- 保留 `writing-fidelity` 作为唯一共享保真原则的维护负责人；**不能依赖一个技能必然再调用另一个技能**。每个可独立选择的文字技能必须在自身可加载内容里拥有适合本场景的最小保护约束。
- ChatGPT 网页端与 Codex 端分别分发、分别实测；只保留一套仓库权威源，但各端使用实际支持的安装载体。
- 前端和演示文稿保持已存在的有效交接，不因为版本推进而改名或重设领域职责。

Research Authoring 的当前个人插件和仓库写作流程处于用户指定的冻结状态：**不研究、不修改、不重打包、不迁移、不使用它的成败充当本项目验收**。PIE 0.2 仅在本插件真实成立之后单独决定是否做一次性 Project 适配。已关闭且未合入的 PR #100 不是本轮审批对象。

## 3. 技能分工和真正的触发设计

| 现有或新增技能 | 正向使用任务 | 明确排除与边界 |
|---|---|---|
| **新增 `response-clarity`** | 已完成领域推理后，给用户解释判断、分析结果、问题原因、行动建议、进展或状态的普通聊天回复；特别是读取英文技术资料、英文日志与机器回执后 | 不接管事实发现、概率/统计判断、科研推导、源全文重写、文稿规划、产品 UI 短文案、纯代码/命令/机器协议、要求逐字引用的任务 |
| `chinese-prose` | 中文报告、README、教学材料、技术文档、普通段落润色与正式中文成稿 | 不接管普通问答的主路由、源材料重度结构重写、产品 UI 文字 |
| `scientific-prose` | 英文科研报告、论文段落、英文图注与科研演示文案的自然表达 | 不负责科研内容审定、文献查找或用户聊天通用终审 |
| `scientific-rewrite` | 已有中文或中文主导科研技术长文需要保留完整科学内容的结构性重写 | 不擅自扩展为所有语言/材料，也不抢轻量润色 |
| `product-ui-copy` | 已确定产品含义与界面角色后的网页/应用按钮、状态、提示、帮助及地区化短文案 | 不决定界面是否放这段字、用户权限和真实产品后果 |
| `writing-fidelity` | 内容发生实质改写时的受保护语义约束和需要独立核查的明确请求 | 不强制每次聊天都作为额外技能调用，不代替事实查证或领域决策 |

`response-clarity` 必须自带完整且简短的独立工作合同，包含目标语言、当前用户覆盖、解释/机器分层、精确身份保留、命题边界和自然段落组织。它可使用 `writing-fidelity` 的**同源规范**，但不能在当前运行表面没有实际加载它时宣称保真已由第二技能验证。

避免重复的实施方式：将保护规则的权威维护职责仍留在 `writing-fidelity`；在独立技能里直接写出必需的短保护要点，并用测试/审查核对两者没有语义冲突。只有发现真实不一致时才考虑最小可重复源生成，不为此新增第二个规则状态机、服务或通用依赖框架。

## 4. 用户语言规则与真正的自动生效

现有 ChatGPT Web 的公开机制：模型通过技能名称和描述判断是否加载，安装插件可在相关任务中自动使用，但没有提供面向普通聊天的通用强制发送前钩子、保证的多技能调用顺序或无需新服务的独立二次生成。插件内 `defaultPrompt` 是示例入口，不是所有答复强制执行的系统规则。Codex 的本地钩子不能假装是 ChatGPT Web 的钩子。

**两条互补而不互相冒充的机制：**

1. 持久、可独立生效的阅读偏好：无 Project 的个性化自定义指令，有 Project 的当前 Project instructions。只写轻量“目标语言、必要英文、先结论、段落自然、机器保真”等要求；遵守当前消息的明确覆盖。不把完整 `SKILL.md` 粘入项目设置；Project 指令会覆盖全局自定义指令。
2. 已安装的 Clear Writing：由明确且不互相争抢的技能描述提高相关性选择；能被自动加载时，提供比短规则更细的场景化处理。用户不需每轮标记 `@Clear Writing`；它只作为调试与手动显式能力，不能替代自动调用验收。

这套架构**不是数学上保证每条回复都会加载插件**。正式成功声明只能是“经真实测试，普通首次回答可重复满足阅读质量与保真，且相对于仅持久规则有可观察插件增量”。若新增技能没有稳定插件增量，必须退回最简路线，不可宣传自动终审。未来 PIE 0.2 可以消费经验证的一次性短项目配置，不是本次前置条件。

## 5. 包装与部署边界

### 5.1 Codex：现有 Marketplace，不新建中央插件

权威构建入口：`scripts/codex_marketplace_config.json`，正式插件版本来自其中 `writing-style` 条目；现有生成器 `scripts/build_codex_marketplace.py` 会把 `skills/writing/core/*` 源复制进 `plugins/codex/plugins/writing-style/skills/*` 并维护 Marketplace。新增同一条目的第六个源 `skills/writing/core/response-clarity/`，建议生成标识 `response-clarity`，不改原五项 `artifact_id`，不重造生成器。

专业消费：
- Frontend Design 已有 `frontend-visual-systems` → `product-ui-copy` 交接，产品角色和真实渲染仍归前端；对已存在消费入口仅作检查和回归，非必要不修改其正式源。
- Presentations 已有共享中英文文案交接，保持 `chinese-prose`、`scientific-prose` 和 `writing-fidelity`；实测完整幻灯片的文字与渲染。
- 软件、统计、服务器等 Codex 普通解释使用轻量自然回答语义；不得让新技能修改源码、日志、字段或执行结果。
- 研究/技术报告及论文文字由任务所属专业能力定义结构、证据、科学结论；Clear Writing 只保证措辞与已确定内容，**本轮不能修改 Research Authoring**。

### 5.2 ChatGPT：个人私有技能型插件包装

先通过 Plugin Creator 的只读个人插件目录确认目标身份。当前有个人 PIE 与 Project Thread Handoff，但未见独立 Clear Writing。只有在批准并经权限预检后，才创建**一个**个人私有、技能型 Clear Writing 包装，不建立新中央产品，不申请公开插件发布。

**默认采用完整六技能包装**，每项保持精确、互斥的任务说明，避免某个技能因被排除包装而无法在 ChatGPT 的合理文档/界面场景被使用。由相同冻结源码与已经验证的生成包构建，不为 Web 另维护一套写作原则。包装包含合法的 `.codex-plugin/plugin.json` 与六份自包含 `SKILL.md`/必需支持文件，插件显示名仍是 Clear Writing。公开仓库不存个人插件 ID、私有 URL、真实项目设置、私有测试聊天和认证凭据。Web 与 Codex 插件的**分发版本号格式可以受各自平台约束，但六项技能内容必须能逐文件核对为同一最终候选源**，不伪称两个平台天然共享实时版本。

个人 ChatGPT 环境中如已有其他插件带有同名技能，只做只读冲突检查及正反实际路由验证；不能擅自调整用户其他插件，尤其不能修改冻结的 Research Authoring。若冲突使正式普通入口不可证明，停下并返回 Planner，不能偷偷禁用其他插件或挑选只在空白环境成功的回答。

任何 Web 插件安装、更新或指定测试 Project/个性化设置修改均发生在用户后来明确批准的执行授权范围内；用户可见安装弹窗/批准仍受平台管控。未经批准不做真实账户修改。

## 6. 必要证据，不重造大量测试框架

按同版 G0–G7：安装与源身份、普通不点名调用与短规则增量、自然语言、保真与机器协议、中文/英文长文、真实 Frontend/Presentations、跨语言多轮、最终候选未见完整任务。原五技能不退化是本版本的兼容验收。

ChatGPT Project 中比较：安装无短桥、安装加短桥、无候选仅短桥、明确 `@Clear Writing`；Project 外在固定个性化规则下比较安装与未安装。若需用户账户上的临时开关，先确认是否有受支持且得到授权的可逆操作，不能改变实际用户的长期配置来创造实验条件。Codex 必须从正式安装的候选插件按自然任务触发，证明文字在真实消费者及其最终产物中被消费；只存在配置、单元测试或技能路径均不能证明这一点。

测试提前冻结任务族、尝试次数和标准；开发回归可重复，最终未见批次冻结后不允许换题或挑选赢家。科学来源保真与表达流畅分别审查；机器协议与项目/个性化语言合同是强制反例。最终评审应直接取得全文、需要的渲染及来源，不可只看摘要或检查回执。

## 7. 版本、权限、恢复及执行前条件

当前 `writing-style=0.4`。若新增 `response-clarity` 确实通过全部正式门槛并准备发布，建议本次**一次性**改为 `writing-style=0.5`，其余中央插件 `NO_BUMP`，成熟度不升级。仓库级版本按 `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`：该改动是已有插件的兼容增强，**Repository bump decision = PATCH（正式 release 时）**；精确新三段版本在集成前对当时有效正式发行基线算出，不能把目前的 `5.4.4` 当永恒起点。设计/实现中间提交均不提前修改版本。

同一正式候选完成：技能源、生成插件、私有 ChatGPT 包装、版本说明、变更记录、受影响 README（有修改则先真实 Clear Writing 终审）、回归、独立评审与用户验收；正式发行还需核对 `release` 与 `main` 差异以及现行发行策略。只有合规终审后的同一候选才能成为宣传依据；不得把正式安装之前的开发证据冒充发布能力。

不得新增外部模型、API 密钥、网络服务、钩子、浏览器扩展、后台 watcher 或自动付费评审。用户隐私与账户设置的修改必须单独守边界；私有测试结果放 `private/exports/` 或用户明确授权的私密位置，公共结果仅保存去敏任务、版本身份与可以公开的结论。失败恢复：停止发布，撤回尚未上线候选，恢复旧个人插件状态、旧 Codex 安装与测试项目指令；不自动改动其他真实 Projects。旧分支/资料不被清理或覆写。

该架构的 **下一步只能是同版完整执行包的独立执行前 Critic 审查**。用户转述的架构 PASS 不等于执行前 PASS，也不授权启动 Executor、创建插件、写入用户设置或发布。

## 8. 当前官方资料与核查边界

本次设计在 2026-10-12 重新核对官方说明。以下资料支持插件可以包含多个技能、技能根据名称/描述和任务相关性被加载、Web/Codex 共享插件目录但能力受当前表面限制，以及 Project 指令覆盖全局个性化：

- OpenAI, *Skills in ChatGPT*: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI, *Skills – Plugins*: https://developers.openai.com/plugins/concepts/skills
- OpenAI, *Build skills*: https://developers.openai.com/plugins/build/skills
- OpenAI, *Plugin architecture*: https://developers.openai.com/plugins/concepts/plugins
- OpenAI, *Package your plugin*: https://developers.openai.com/plugins/build/plugins
- OpenAI, *Plugins in ChatGPT*: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- OpenAI, *Projects in ChatGPT*: https://help.openai.com/en/articles/10169521-projects-in-chatgpt

官方支持“技能可包含指令与代码资源”，但**不能由此直接推断个人 ChatGPT Web 的技能运行环境必然具有重型中文重写脚本所需的本地执行能力**。包装预检必须同时审阅其真实依赖和使用表面；正式 Web 端若不能运行某项必要帮助脚本，不得悄悄删除该脚本并宣称六技能全功能成立。应明确记录该表面的能力缺口，返回 Planner 决定是按经审核的可用范围收缩，还是停止该跨表面发行。

这些官方页面不证明插件已经实际安装、每条回答都调用技能或两个技能按确定顺序运行。实际候选增量必须通过 G0–G7 规定的正常使用对照检验。
