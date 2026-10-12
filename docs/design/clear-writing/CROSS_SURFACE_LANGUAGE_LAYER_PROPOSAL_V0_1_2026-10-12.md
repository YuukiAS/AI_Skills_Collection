# Clear Writing 跨 ChatGPT / Codex 通用表达层 — Planner 提案 v0.1

- 日期：2026-10-12
- 状态：DRAFT_FOR_INDEPENDENT_CRITIC_REVIEW；**尚无 Critic PASS**
- 仓库：YuukiAS/AI_Skills_Collection
- 事实基线：main@00a90661a3cb3e287ed83a7a2e5dc9beffbf8b91
- 提案分支：planner/clear-writing-cross-surface-v0.1
- 唯一产品负责人：Clear Writing（现有插件标识 `writing-style`，当前 main 版本 0.4）
- 跟踪：Issue #13；保留已有 #90 的界面文案事实，不新建重复 Issue
- 旧设计：PR #100 已关闭且未合入 main；其 v0.2 仅作为历史参考，**不是本提案的审批或执行授权**
- 本轮交付：产品与架构提案、命名及迁移判断、正常调用方案、能力验收矩阵、独立 Critic 交接
- 本轮禁止：正式技能/插件/配置/版本修改、创建或发布个人插件、修改真实 Project 或个性化设置、付费 API、模型服务、启动 Executor、发布与合并
- **Research Authoring 冻结且排除**：不修改、重设计、重新打包或要求其配合迁移；等待用户另行开启新轮次
- PIE 0.1 保持原职责；PIE 0.2 只在中央能力成立后作为可选的项目指令一次性配置适配，不在此实现

## 1. 产品目标与真正要解决的失败

Clear Writing 下一次改进不是把“改写文字”做成第六种润色功能，而是让它成为 ChatGPT 与 Codex 共用、由具体用户目标和交付形式驱动的**通用读者表达能力**。

目标覆盖：
1. ChatGPT 在有 Project 和无 Project 的普通对话中，面对科研、编程、统计、架构、管理、生活问题，第一条解释性回答就符合当前目标语言和读者要求：先给判断、自然连贯、非必要英文不成为叙事骨架、不过量换行或堆内部状态；不需要用户每轮 `@Clear Writing`。
2. Codex 正常写网页/应用、技术说明、报告、科研文稿、演示文稿时，由各领域任务在内容确定后消费对应语言能力；不需要用户每轮追加“说人话”。
3. 语言优化不得修改事实、数值、公式、条件、否定、引用、归因、权限、结论强度、用户决定、完成状态、精确机器标识或可编辑性；纯代码、纯日志、严格 JSON/YAML、明确逐字要求必须遵守原始协议。
4. 在英语、繁体、双语及当前消息覆盖语言的任务中遵守有效语言合同，**不将中文偏好误写成全平台固定中文**。
5. 让普通使用的真实输出变好，而不以插件安装、规则存在、测试、调用自述或本地单句演示冒充成功。

用户提供的长篇网页架构建议是**私有历史回归类型**：来源表达、内部角色、重复技术流程和碎片结构压过直接结论。不得在公共设计或测试文件原样复制该对话；以合成公开安全、语义等价材料复现失败族。原有 C5–C11 可作开发回归，不可重新称为未见样本。

## 2. 经实际核对的现状与平台限制

当前 main 的 Clear Writing 已包含五项正式技能：`chinese-prose`、`scientific-prose`、`scientific-rewrite`、`product-ui-copy`、`writing-fidelity`。其中 `scientific-rewrite` 是**已有中文或中文主导科研技术材料**的重度保真结构重写，不是任意语言/材料的通用重写；它已经有源锚点、含义映射、读者计划、中文实现、整篇组织与保真审计主链，不能为了新增普通回答能力而推倒。

Frontend Design 的 `frontend-visual-systems` 已将界面文字在内容角色固定后交给 `product-ui-copy`，并在真实界面中验收；Presentations 的共享路由已在相关技能安装时交给中文表达/保真或英文科研表达。**源码中的交接规则并不等于所有 ChatGPT/Codex 正常任务已经可靠执行**，尤其不能以“插件同装”推断技能按特定顺序自动调用。

OpenAI 当前文档明确：模型根据技能名称、描述及任务相关性决定加载；插件可含多项技能，但没有为普通 ChatGPT Web 公开提供可依赖的“所有回复必须经过指定技能”的发送前强制钩子、确定的多技能串行执行或独立第二次模型调用。ChatGPT Project 指令会覆盖全局自定义指令；因此全局偏好不能替代每个 Project 的基本阅读规则。Codex 本地钩子不代表 ChatGPT Web 可执行。此版本只能承诺在明确支持的正常入口得到**可观察、可重复的改善**，不得保证平台级每条消息的插件内部调用。

在当前已认证个人插件清单中没有独立的 Clear Writing 个人插件；仓库的 Codex Marketplace 0.4 不等于个人 ChatGPT Web 已安装。实现方案若只修改中央技能源而不完成目标 Web 个人插件实际创建/安装，就是交付缺口。

## 3. 方案比较：不重构重写核心，修真正缺口

| 现实方案 | 结论 | 因果理由 |
|---|---|---|
| 仅保留现有五项，给 Project/个性化加短规范 | 必须保留为基线对照；可能成为 ChatGPT 部分场景的最终最简解 | 可直接影响每次回答，但不能证明复杂写作与领域交接的专业能力已经消费 |
| 在现有 Clear Writing 内补普通回答能力并整理名字、触发、分发与领域入口 | **推荐待审** | 普通回答属于现有五项未单独覆盖的正常入口；其他任务复用成熟能力，增量集中在路由和表现 |
| 一个巨型“万能写作”技能，每次加载完整科研重写/保真/界面规则 | 拒绝 | 触发重叠、上下文与复杂度过高，普通问答会被重写流程污染，也难以维护不同专业边界 |
| 所有技能统一改成相同后缀、同时完全重写内部流程 | 拒绝 | 名称形式整齐不等于职责明确；旧调用点会断裂，重度重写核心回归风险高 |
| 外部改写 API、浏览器扩展、独立模型、发送前脚本、MCP 服务或持续后台 | 不进入本轮 | 改变正常使用表面、授权、费用、隐私及恢复方式，且不是用户希望的零额外操作路径 |

## 4. 六项能力与命名建议（提案，不是已执行迁移）

不追求所有名称相同后缀；应追求名称指向清楚的输入、产物和责任，不相互争抢触发。建议将“面向人的产品名称”与“精确机器技能标识”分开看待。

| 当前标识 | 候选标识 | 准确的正向触发 | 必须排除 |
|---|---|---|---|
| 新增 | `response-clarity` | 普通 ChatGPT / Codex 面向人的解释、诊断结论、建议、阶段说明；尤其长英文资料后的自然解释 | 纯机器内容、明确逐字回显、复杂已有文档重写、界面短文案 |
| `chinese-prose` | `chinese-writing` | 中文报告、说明、README、教学与普通文档成稿/轻量润色 | 需要保真结构重写的既有长文、产品界面、科研内容正确性判断 |
| `scientific-prose` | `scientific-english` | 英文科研文稿/技术报告/论文段落、图注与英文科研演示文字的表达 | 论文证据筛选、全篇科研结构与发表策略、普通中文问答 |
| `scientific-rewrite` | **`chinese-source-rewrite`**（不建议过宽的 `source-rewrite`） | 已有中文/中文主导科研技术材料要求结构性重写并保持完整含义 | 无源材料的新文稿、简单摘要/润色、未验证的外语重写 |
| `product-ui-copy` | `interface-writing` | 已冻结产品含义的网页、应用、移动端界面短文案/状态/帮助与地区化措辞 | 产品状态、权限、隐私事实的判定，以及界面结构/视觉层级 |
| `writing-fidelity` | `meaning-fidelity` | 实质改写风险中的受保护语义检查；可作其他技能共享原则/必要的独立核查 | 自动联网事实核查、代替领域推断、强制每次普通问答单独调用 |

前三者在句法形式上并不完全一致，但它们代表不同操作类型；“一致”应优先是统一发现逻辑、名称不重叠和用户能够理解，而不是机械后缀。

**命名迁移的真实代价必须单独复核**：当前 `scientific-rewrite` 内直接引用 `chinese-prose`、`writing-fidelity`；Frontend Design 使用 `product-ui-copy`；Presentations 使用 `chinese-prose`、`scientific-prose`、`writing-fidelity`；profiles、catalog、registry、生成的 Marketplace、文档和测试也含旧名称。改名必须做完整引用清单，在同一最终候选中更新实际消费者，并核对安装与路由；不能只改源目录。不能为了平滑迁移长期同时开放新旧同义技能造成重复选择。若 Critic 证明全面改名不能产生实质发现/可维护性收益，应允许只新增 `response-clarity` 并做少量名称修正，但必须给出逐项保留理由，不靠审美否决或支持。

## 5. 共享规范与按任务选择，不建立“六技能每轮串行链”

共享核心语义规范仅由 Clear Writing 一份正式源维护：目标语言、读者角色、允许的重组幅度、精确身份、受保护命题、必要英文、段落结构、来源包装与用户意义。各技能只补充其特有的生成/复核方式。对于通常只需说清楚答案的场景，应优先使用轻量契约；复杂科研结构重写仍保留完整 `scientific-rewrite` 主链，不从零改造，不要求普通聊天经历含义映射和全文重排。

能力选择逻辑：
- **普通解释性回答**：语言与阅读基本规范始终有效；在模型选择加载时由 `response-clarity` 提供细化；不承诺每次存在机械二次审校。
- **中文新文档或轻量编辑**：`chinese-writing`，需要改动事实/结构时消费统一保真原则。
- **英文科研表达**：`scientific-english`，不得冒充新的科学证据或文稿规划。
- **已有中文科研技术长文保真重写**：`chinese-source-rewrite` 保持现有重型流程，中文实现与保真要求来自同源能力，不依赖平台可保证的跨技能调用链。
- **产品界面**：专业产品/Frontend 决定内容意义与布局，`interface-writing` 只改措辞，回原负责人做渲染验收。
- **纯机器输出**：完全跳过阅读层重写；混合内容只改面向人的解释层；当前消息要求其他语言只覆盖本轮，不永久改变偏好。

不能把“已安装六技能”解释成“每次都调用六技能”，不能发明技能调用技能的确定执行机制。消费者若需要共用能力，可以使用已有伴随安装或同一权威源的构建时打包；不允许把同义语义规则永久复制到领域插件维护第二套。

## 6. ChatGPT 与 Codex 的正常入口与分发

### 6.1 ChatGPT：让回答正常，不能伪造每轮强制技能调用

目标是在当前个人 ChatGPT Web 上用 Plugin Creator 从同一权威源构建 **Clear Writing 技能型个人插件**，通过正式插件身份安装并在新会话中测试；不建新顶级产品，不添加 MCP、密钥、服务器或付费 API。

- 无 Project：用户全局自定义指令提供简短、可独立生效的阅读规范。该规范不应写满技能实现细节。
- 有 Project：有效 Project 指令直接保留该项目语言、数学与格式合同，以及简短阅读规范；因为项目指令覆盖全局自定义指令，不能只靠全局配置。PIE 0.2 以后可一次性帮忙保留这条规则，但不是当前交付前提。
- 已安装 Clear Writing：技能名称与描述争取按任务自动选择。用户不应每轮 `@`；只有显式诊断才允许指定插件。若某 Web 场景“必须每轮 @ 才能工作”，该场景不得宣称自动成立。
- 插件没有被选择：项目/全局的基本自然语言规则仍应独立发挥作用。记录实际答复效果，不杜撰调用事件。

包装采用**同一源、表面适配**，不允许 ChatGPT 私人插件与 Codex 市场版各自手工维护语义副本。建议网页默认暴露普通回答、中文文档、英文科研、中文长文重写等能在 ChatGPT 直接交付的任务；保真能力可作为同源共享材料，也可提供明确改写核查入口；界面文案技能可以随包存在，但描述应精确到真实界面文字任务，不能争抢普通聊天。最终包含哪些可选择技能，以正常路由对照证明其不互相误触发为准，而不是人为求数量齐全。

### 6.2 Codex：领域插件主导，Clear Writing 作为静默随行能力

正式 Codex Marketplace 插件继续使用 `writing-style` 标识与 `Clear Writing` 展示名。六项正式技能来自同一源，使用安装/个人或项目范围的有效指令与消费者已存在的专业交接，在正常任务中按阶段消费；仓库 `AGENTS.md`、profile、领域技能引用都只能提供调用要求，必须以真实运行证明而不是只看文字。

消费者分层：
1. Frontend Design：保留现有“产品含义与界面信息架构 → 界面文字 → 实际渲染验收”，升级名称时不能断开现有 `product-ui-copy` 能力。
2. Presentations：保留“幻灯片科学内容与叙事 → 局部中文/英文文案 → 全套幻灯片渲染/可读性验收”，语言技能不能决定页数、版式或科学结论。
3. 普通软件/服务器/统计任务：Codex 最终面向用户的说明应自然清楚；不改变源码、日志、机器输出的精确性；普通解释可使用轻量回答规则，不要求执行重度写作。
4. 报告/论文：领域负责人决定来源、论点、证据、章节与文献；Clear Writing 负责表达和保真。**Research Authoring 本轮无消费者迁移、无回归要求、无包装修改**；其它经批准的写作任务可以作为代表性验证。

跨消费者正式适配应在中央能力与真实正常入口通过之后进行；如有更改别的插件正式行为，必须单独说明范围、授权和必要的复核，不得静默推到领域仓库。

## 7. 必须证明的增量：安装与“静默”并不是验收

ChatGPT 的核心对照不是“有插件”和“无说明”比较，而是冻结同样的 Project/个性化规则、同样的任务，比较插件加入前后是否带来真实收益：

- A：候选插件已安装，无额外 Project 插件激活桥；保留相同有效语言合同。
- B：候选插件已安装，附一条尽可能短的 Project 阅读激活桥。
- C：不含新技能/禁用候选，使用与 B 完全相同的短桥与语言合同。
- D：显式 `@Clear Writing` 调用，仅用于诊断，**不计无 @ 正常成功**。

无 Project 的自定义指令场景另做 A/C 对照。B 对 C 没有稳定增量时，停止把新技能声称为自动终审，Planner 应接受“持久指令已足够”的更简路径；若 A 就稳定通过，B 可降为可选；若只有 D 通过，只能说明明确调用模式可用。

Codex 需要两种独立证据：普通用户任务从正式安装入口自然命中领域能力；领域负责人完成内容后，生成的文字实际受到 Clear Writing 规则影响，并经专业消费者实际使用及渲染/内容审查。只加载文件、读了规则、自报“用了插件”不能通过。

## 8. 验收、风险、复归与职责阶段

详见配套 `CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_1_2026-10-12.md`。高优先级风险是：普通首答不触发；短桥本身而非新技能产生全部改善；长英文资料后回退来源腔；为了自然中文误改专业语义；命名迁移破坏 Frontend/Presentations；一个长文技能抢走普通问答；纯机器内容被改写；Codex 测试通过却不能代表 ChatGPT Web；个人插件包装未安装；已知修复案例冒充新鲜泛化证据。

任务阶段建议：
1. **Critic 独立设计审查**：确认命名、范围、真正的自动使用边界、轻重路由、两端包装和 Gate；未 PASS 不进入正式实现。
2. **小成本机制探针与开发回归**：按审查批准的范围核实真实个人 Web 安装能力、正常路由和命名冲突；优先尝试更简单的路径，不新增基础设施。
3. **中央技能与版本候选**：只在获准范围内实现轻量能力、必要的重命名及其生成/配置引用一致性；重型重写主链保持兼容。所有关键证据来自同一最终候选。
4. **双端正式入口与消费者验证**：实际创建/安装个人 ChatGPT 插件、Codex Marketplace 安装回放、Frontend/Presentations 等真实产物（及其专业验收）；双端任一缺口必须分别报告。
5. **冻结未见完整任务与独立评审**：在规定预算内审第一条完整回答、整篇文档、界面文字和完整幻灯片；按保真与读者价值分别判断，禁止挑选赢家或用旧已曝光回归冒充未见。
6. **经用户单独接受后发布/集成**：版本和安装身份检查、必要 README/变更记录/registry/catalog 同步；失败时恢复上一版本和项目激活桥，不重开 C12，也不自动要求用户修改所有 Projects。
7. **可选的后续 PIE 0.2**：仅在目标阅读能力实际可用并经批准后单独规划一次性项目配置；不允许把它算作本轮中央技能通过的替代证据。

数据与费用：设计阶段仅访问公开仓库与官方资料；不得向公共仓库放私有聊天、敏感系统拓扑、账户配置或未公开文稿。实现阶段若需要私有真实验收，必须提前明确同意的接收方与保存方式；默认无新密钥、无新托管、无付费模型、无自动化和强制外部传输。基础设施失败与产品失败分开归因。无证据不能宣称全局永久保证。

## 9. Critic 必须裁定的争议与不允许随意放行的问题

1. 六个候选名称是更易理解、区分触发，还是为了整齐制造过大迁移？特别审 `source-rewrite` 过宽、`scientific-english` 与其它科研写作技能边界、`meaning-fidelity` 是否应保持可独立调用。
2. 新建 `response-clarity` 相对现有 `chinese-prose` 与“仅持久指令”的增量究竟是什么？能否在正常 Web 中观测，而非仅写规则？
3. Web 同包六技能还是按表面裁剪？如果不同包，怎样证明单一源和版本身份且防止隐藏别名/重复触发？
4. 已有 Frontend Design、Presentations 的消费合同如何随名称迁移不中断？哪些适配可由本插件发布直接完成，哪些必须由领域负责人单独验收？
5. 对 Codex 软件、统计、报告、论文、幻灯片的必要能力是否充分，但是否把“每种任务都必须实际运行 Clear Writing”夸大为平台强制保证？
6. 现有长文重写主架构是否应该原样保留；若要求重构，必须指出直接失败证据、最低改动以及完整长文回归范围。
7. 真正关键的双端正式入口、第一条完整回复、跨语言/纯机器绕过和语义保真是否都有阻断性验收，且 Gate 没有重叠堆砌？
8. Research Authoring、PIE、既有安装、权限/隐私/费用和无法调用插件时的停止条件是否保持清晰？

Critic 只能对**本提案明确版本与确切提交**给 `PASS` 或 `REVISE`。本 Planner 不作自我批准；Critic 通过不意味着已经授权创建 Executor、部署个人插件或批量修改真实设置。

## 10. 依据与可复核资料

### 当前仓库（main@00a90661a3cb3e287ed83a7a2e5dc9beffbf8b91）

- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/writing/core/chinese-prose/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/writing/core/scientific-prose/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/writing/core/scientific-rewrite/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/writing/core/product-ui-copy/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/writing/core/writing-fidelity/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/tools/frontend/frontend-visual-systems/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/skills/tools/documents-media/presentations/shared/ppt-skill-routing.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md
- https://github.com/YuukiAS/AI_Skills_Collection/issues/13
- https://github.com/YuukiAS/AI_Skills_Collection/pull/100（已关闭，仅历史证据）

### 官方资料（2026-10-12 实际核对）

- OpenAI, *Skills in ChatGPT*: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI, *Skills – Plugins*: https://developers.openai.com/plugins/concepts/skills
- OpenAI, *Build skills*: https://developers.openai.com/plugins/build/skills
- OpenAI, *Package your plugin*: https://developers.openai.com/plugins/build/plugins
- OpenAI, *Plugin architecture*: https://developers.openai.com/plugins/concepts/plugins
- OpenAI, *Projects in ChatGPT*: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI, *ChatGPT Custom Instructions*: https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt
- OpenAI, *Plugins in ChatGPT and Codex*: https://help.openai.com/en/articles/20001256
