---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: clear-writing--cross-surface-language-layer
decision: PLAN_FROZEN
---

# Clear Writing 跨 ChatGPT / Codex 通用表达层 — 冻结实施计划

- 审批对象：`YuukiAS/AI_Skills_Collection`，任务 `clear-writing--cross-surface-language-layer`。
- 执行分支：`reviewed/clear-writing--cross-surface-language-layer`；已发布首次任务提交 `32b60592c948afe65c988fd56499baea15bf33cc`，基线 `34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b`。
- 唯一执行合同：`planner/clear-writing-cross-surface-v0.1@b960ec57941fc058a22ca8896c92d5dc19191009` 的六份 v0.3 设计、验收、执行与交接文件；完整路径见同一任务的 `REQUEST.md`。本任务分支从 `main` 派生，**不能假定包含规划分支文件**；必须按其不可变提交读取。
- 独立执行前审查：`docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_CRITIC_REVIEW_V0_3_2026-10-12.md@0f8ee7d98ba8890d074b488c87cb65c20cd8b82f`，`PASS / READY_FOR_CODEX=YES`，旧 `CW-ER-01`、`CW-ER-02` 已关闭。
- 任务内本计划只将上述已批准合同落实为 Codex 可执行范围，不重新授予个人账户、私有资料、额外费用、合并或正式发布权限。

## Objective and value

使普通 ChatGPT（有 Project 与无 Project）在无需每轮手动 `@Clear Writing` 的情况下，首条完整解释性回答尽可能持续清楚、自然，减少非必要英文、机械换行和内部状态堆砌，同时保留事实、条件、权限、公式与精确机器字符串。Codex 的文档、英文科研表达、网页／应用界面文案、完整演示文稿及工程说明按真实任务使用对应表达技能，证明既有专业交接和最终产物确实受益。**是否成功以真实正常入口和完整产物判断，不以规则文件、安装或 CI 存在判断。**

## Frozen decisions

- 保留中央插件标识 `writing-style`、产品名 Clear Writing、既有五项技能 `chinese-prose`、`scientific-prose`、`scientific-rewrite`、`product-ui-copy`、`writing-fidelity` 的正式名称与已有能力。**只新增** `response-clarity`，严格用于普通面向用户的解释、诊断结论、建议和阶段说明。
- 仅最小调整 `chinese-prose` 与新技能的触发描述、正反例和必要的实际加载内容，使普通回答不抢中文报告／README，正式文档不误入普通回答路线；英文科研文字、产品界面短文案、已有中文科研技术长文重写和保真核查仍各归原负责人。
- 保留 `scientific-rewrite` 的源锚点／含义映射／读者计划／中文实现／整篇组织／保真审计主链，不改造成普通聊天处理器。每一项可独立被选择的技能须在自身可读取内容中获得适用的最小事实、条件、否定、证据强度、时间状态、权限与精确标识保护规则；**不假设平台必然连续调用另一个技能**。`writing-fidelity` 仍是共享保真原则权威源。
- Frontend Design 现有 `frontend-visual-systems → product-ui-copy` 交接，以及 Presentations 现有中英文文案／保真交接维持不变；专业插件仍负责产品事实、结构、来源和实际界面／整套幻灯片验收。不进行无收益迁移。
- ChatGPT 项目内的有效 Project 指令、项目外的个性化指令，是可以独立发挥作用的基础阅读规范；Clear Writing 是按任务相关性自动选择时的增强能力。**没有平台级每轮强制发送前终审保证**。显式 `@` 只能诊断，不能证明自动触发。
- 维护跟踪继续使用 Issue `#13`；不把旧 PR `#100` 或已曝光 C5–C11／050–055 重当未见证据。无新增通用插件、状态机、付费模型服务或自动调度器。

## Positive completion

只有经过同一最终候选的正常安装和完整任务证明：ChatGPT 真实首次答复在项目内外可读、语义保真，候选插件相对**匹配无插件**语言合同有可观察增量；Codex 从正式 `writing-style` 入口自然使用适当技能；原五项及 Frontend Design／Presentations 正常消费不回归；完整报告、实际界面和整套演示文稿通过来源保真与真实渲染审阅；G0–G7 冻结未见批次和独立 Reviewer／必要 Critic 均无阻断；用户最终接受后才可按授权集成／发行。

**成果声明的上限**由实际通过的表面与条件决定。若只有明确 `@` 能用，不能声称静默触发；若有 Project 短指令自身已产生同等效果，不能把功劳归于插件。任何匹配对照无法合法建立均记 `INCONCLUSIVE`；如果新增技能没有稳定额外价值，停下交 Planner 简化，而不是制造发布 PASS。PLAN 冻结、Executor 实现、单次测试或 Reviewer 阶段 PASS 均不等于整个产品已完成。

## Non-substitutable semantics

- 首次任务 `REQUEST/CURRENT` 已真实发布；本计划只从 `PLAN_REQUESTED / RUN_GPT_PLANNER` 首次冻结为 `PLAN_FROZEN / RUN_CODEX_EXECUTOR`，保持 `plan_revision=0`、`review_round=0`、`implementation_commit=null`、`ci_required=true` 与 `ci_status=PENDING`。不要二次 bootstrap、改派生工作树或跳过 Planner。
- G1 保留 **A/E** 与 **B/C** 两组匹配对照：A＝候选插件＋相同 Project 基础语言合同＋无桥，E＝无候选＋同合同＋无桥；B＝候选＋基础合同＋短激活桥，C＝无候选＋同合同／同短桥；D＝显式 `@Clear Writing` 只供诊断。两组内部除插件有无外，任务、模型、规则、尝试次数、评分准则应可比；无 Project 另以固定个性化指令进行插件有无对照。不能合法、可靠隔离时必须 `INCONCLUSIVE`，不得增加相似 Gate 或无限补样本。
- 人类可读表达与来源语义分开审查：准确保护数值、公式、引用、事实主体、条件、否定、完成状态、权限和安全；机器协议／原始代码／逐字内容不按中文风格重写。当前消息覆盖语言、繁体或英文项目要求须优先适用。
- Web 个人插件与 Codex Marketplace 必须来自相同冻结源、六份真实技能及支持文件；相同源码身份和各端包装／发行版本可独立核对。Web 是否能运行 `scientific-rewrite` 的必要脚本须由真实入口证明，不能仅因 ZIP 成功安装就宣称全功能。
- 原文档所规定的阶段顺序必须保留：先低成本开发与已知回归、代表性**完整**产物的独立定性检查，再同一正式候选的版本／生成包／评分封口及预最终 Critic，后才正式双端安装对照与冻结未见完整任务、独立 Review／用户验收。最终候选冻结后不能换题、挑赢家、混用提交或基于未见批次继续调优。
- 人工 Planner／Reviewer 交接是默认路径，不假定有已开启的自动任务；外部角色正常等待不得冒充产品失败。出现证据访问、匹配环境、权限或设计实质变化时停在合法状态交原 Planner／Critic，不增加服务器、外部接口或隐式降级。

## Implementation scope

1. **真实入口预检**：执行时确认 `origin/main`、任务分支、已有安装身份、Bridge／Codex 正常入口及 ChatGPT Plugin Creator 资格；无法实现双端关键 G0 时先停止，避免无意义的大规模开发。遵守 `workflow-core + ai-skills-core + writing-style` 正式维护组合。
2. **核心技能源**：新增 `skills/writing/core/response-clarity/` 的 `SKILL.md`、必要简短参考及触发正／间接／近似／负例；只最小调整 `skills/writing/core/chinese-prose/SKILL.md` 的发现边界。仅在证据需要时局部同步 `writing-fidelity` 的受保护含义，不能擅自重构旧四技能。
3. **正式生成与兼容**：在唯一 `scripts/codex_marketplace_config.json` 的 `writing-style` 配置中加入第六技能，保留旧 `artifact_id` `fidelity/sci/scientific-rewrite/product-ui-copy/zh`；复用 `scripts/build_codex_marketplace.py` 更新 `plugins/codex/plugins/writing-style/` 与 `.agents/plugins/marketplace.json`，按证据调整相关回归／`profiles/codex-writing-style.json`，不自造第二套构建系统。
4. **双端候选**：Codex 用现有正式安装及受控插件回放入口验证；按同一冻结公共安全源码准备 ChatGPT 私有、仅技能包装的可再现清单与哈希。个人 Plugin Creator 的真实创建／更新由具备该连接、且获得具体个人账户授权的 GPT 线程执行；不能假定 Codex 能直接读取 GPT 私有容器或修改用户个人插件。
5. **完整材料与结果**：公开安全开发及验收依据保存在 `results/clear-writing--cross-surface-language-layer/`；真实用户聊天、敏感设置或私有材料只在获批准的 `private/exports/clear-writing--cross-surface-language-layer/` 或指定私密接收表面。必要网页／演示实际渲染与完整中英文文稿必须交独立阅读者亲自检查；不得用截图摘要或脚本通过替代完整证据。
6. **版本与发行顺序**：有真实产品改进、兼容与验收证明且准备正式发行时，`writing-style 0.4 → 0.5` **恰好一次**，其余插件 `NO_BUMP`、成熟度不变；Repository 默认兼容补丁发行，具体版本按正式 `release` 基线确定，开发期不提前改版本。必要变更日志、catalog/registry、README 和发行校验随同一最终候选闭合。修改根 `README.md` 时须真正调用已安装 Clear Writing 终审；无法调用则暂停该修改与发布收口。

## Acceptance and regression gates

沿用审批包的 G0–G7，**不新增 Gate、固定样本数量或词频代用品**。每类须记录普通任务输入、目标语言合同、实际安装／候选身份、完整输出／渲染、来源和独立判断：

- **G0 分发**：六技能与支持文件同源、Codex 真安装、ChatGPT 个人包装真实创建／安装及 Web 新会话身份；重型脚本的 Web 可运行性必须实证，缺失即报告该表面不支持／不确定。
- **G1 自动入口与增量**：按 A/E、B/C 分别比较同条件下插件有无；D 只诊断；项目外固定个性化基线另比。仅模型自述、直接源路径调用或明确 `@` 不能通过静默入口。
- **G2 首答可读性**：真实科研统计、服务器排障、架构判断等完整回答首段说清判断，减少普通英文标签、碎片化段落与裸状态，不丢必要推理。
- **G3 保真和绕过**：数值／公式／引文／证据强度／权限和时间状态不变；纯代码、配置、日志和逐字协议不被语言处理破坏。
- **G4 原有专业写作**：中文文档、英文科研表达、中文长文源保真重写与独立保真核查不退化，必要 PDF/Markdown 实渲染、代码／表格／引用保留。
- **G5 领域消费**：Frontend Design 的真实宽窄界面及用户后果、Presentations 的完整可编辑／可渲染演示与科学结论、Codex 工程/统计说明均正常消费对应技能；只读生产消费者，不改其源码。
- **G6 多轮及语言模式**：项目内外多轮英文资料后自然回复、简繁英双语当前轮覆盖、后续恢复、短问答和机器任务负例。
- **G7 最终候选**：统一源码与 Web/Codex 发行身份、预先冻结任务及尝试次数／准则，同一正式候选的未见完整任务与独立 Review；不换样本、不拼不同候选或隐藏真失败。

失败先分清插件缺陷、来源问题、评价错误、入口/打包、环境和权限；已曝光 C5–C11、050–055 只作开发回归，不能充当未见样本。执行中完成 task-owned 源码和低成本检查后，按 `ci_required=true` 的 Reviewed Handoff 合法进入 `WAITING_FOR_CI`，CI 真值由当前任务状态及 GitHub 运行结果确认，再由人工独立 Reviewer 接手；不能跳过 CI 直接宣布 REVIEW/PASS。任一关键证据缺失均不报总体完成。

## Natural-language usage / routing expectations

正常用户不需要写技能名称。例如“这段英文错误日志说明哪里出问题、下一步如何修复？”、“这一统计结果应该怎样理解？”应面向人自然解释，避免转为 `chinese-prose` 的正式文档重写；“把这份中文研究报告改得自然且保持公式引用”应走 `chinese-prose` 或确需结构重写时走 `scientific-rewrite`；英文科研文字走 `scientific-prose`。创建网页按钮/状态由 Frontend Design 先确定真实产品含义，再交 `product-ui-copy`；演示文稿由 Presentations 负责整套页面和渲染，按语言调用既有写作入口。纯 JSON／日志／代码输出按机器要求原样输出。

## Out of scope

**绝不改动** Research Authoring 的仓库源、用户个人插件、打包或消费者；不实施 PIE 0.2，不重命名五个旧技能，不更改 Frontend Design／Presentations 的正式技能源，除非真实缺陷经新 Planner/Critic 授权。不得修改 Bridge Kit、项目以外用户账户或所有 Project 的自定义指令；不得新建中央插件、外部模型／API 密钥／收费评审、托管、MCP、全局发送前钩子、浏览器扩展、watcher 或新状态机。

本 task 不授权公开插件发布、合并 `main`、移动 `release`、破坏性 Git、用户私有资料传输或未经批准的账户操作。个人私有 Clear Writing 的正式创建与试点设置只在批准合同及实际平台授权范围内进行；最终整合／用户验收属于后续独立门槛。用户仅需在确有新权限、私人资料或最终接受决策时介入，其他等候保留正常任务状态。
