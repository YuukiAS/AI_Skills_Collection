# ChatGPT 网页批量回归：浏览器执行路线调研
推荐：技术上优先考虑“本机批处理脚本 + 微软 Playwright 扩展”，连接已登录的 Edge；CDP 作为备用连接方式。
原因：现成扩展支持复用当前登录会话，省去自建浏览器连接层；案例顺序、逐轮原文和结果归档仍由固定脚本管理。[扩展说明][EXT]
最大风险：OpenAI 个人服务条款明确禁止自动或程序化提取输出；完整自动收集回答与该限制直接冲突，投入使用前须确认适用合同及获得允许，换连接工具不能消除这一问题。[条款][TOU]

调研日期：2026-11-21（美东）；联网元数据快照日期为 2026-11-22 UTC。本文只做只读调查和方案比较，没有连接用户笔记本、登录 ChatGPT、运行案例或验证任何路线在用户账号上的实际可用性。下文的可行性、成本和风险排序属于依据文档与源码作出的工程判断。

## 1. 我们已有的东西

| 位置 | 已有什么 | 能直接复用什么 | 缺什么 |
| --- | --- | --- | --- |
| 本仓库：[回归说明](../plugin-reset-2026-11/regressions/HOW_TO_TEST.md)、11 份 `regressions/*/case.yaml`，如[重新解释案例](../plugin-reset-2026-11/regressions/reexplain-after-confusion/case.yaml) | 每案已有素材定位、期望行为、判定方式；说明表另列插件、技能、运行端、调用方式与执行证据。有纯网页案例，也有网页判断后交 Codex 制作、渲染、发布和回读的混合案例。 | 素材来源、原文判据和证据要求；“每案独立对话”的默认组织方式。 | YAML 当前只有 `输入来源路径`、`证据文件路径`、`期望行为`、`判定方式`，没有可直接发送的逐轮 prompt、模型、附件清单、运行记录与完成检测。部分来源是覆盖文档或测试代码，不能把整个来源文件自动当成首轮 prompt。混合案例也不能仅凭网页答复判整案通过。 |
| 本仓库：[CANDIDATE_PLUGIN_REPLAY.md](../../workflows/CANDIDATE_PLUGIN_REPLAY.md) | 针对 Linux x86_64 的 Codex 候选插件回放，绑定 committed tree、临时候选身份、新运行时、消费记录及清理。 | 输入和候选版本绑定、运行目录、失败分类、清理后验证、机械执行与产品质量分开判断的做法。 | 实际入口是 `codex exec`，没有 Edge、ChatGPT 网页、多轮 DOM 交互或网页附件下载；不能用它替代本任务的被测环境。 |
| 本仓库：[网页协作历史](../../workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md)、[PASS 可信度关闭计划](../../workflows/CHATGPT_WEB_PASS_INTEGRITY_REGRESSION_CLOSURE_PLAN_V0_3_2026-10-19.md) | 十类真实问题、Planner/Critic 合同、完整用户承诺与正常入口的验收边界；后续记录了两项复杂真实审查及证据路径。 | 独立判定必须读完整承诺与完整证据；组件通过、文件存在、历史 PASS 都不足以推出本次整体通过。 | 它们是治理记录与验收要求，没有网页执行器、统一案例格式或批量结果采集。其“不新增第三人工角色”不阻止后台独立判定，但不应再让用户手工路由一个新角色。 |
| `/users/a/e/aereinh/GPT_Codex_AI_Bridge_Kit`：[Text Review 说明](/users/a/e/aereinh/GPT_Codex_AI_Bridge_Kit/templates/text_review/README.md)、[实现](/users/a/e/aereinh/GPT_Codex_AI_Bridge_Kit/ai_bridge_kit/text_review.py)、[输入模板](/users/a/e/aereinh/GPT_Codex_AI_Bridge_Kit/templates/text_review/text_inputs.template.json) | 已有私有 UTF-8 文本 → age 加密 → GitHub Actions 临时解密 → OpenAI Responses API（`store=false`）→ 结构化 `TEXT_REVIEW.json`；已有输入 hash、rubric、身份绑定与付费调用预算约束。另有 Codex `plugin_replay.py` 和供 ChatGPT 使用的交接提示词。 | 独立文本判定的传输、完整文本输入、hash 绑定、结构化意见与预算保护；网页测试与判定可分开。 | 在 `ai_bridge_kit/`、`docs/`、`tests/` 定向搜索 Playwright、Selenium、CDP、remote debugging、browser-use，未找到浏览器控制实现。Text Review 不执行网页案例；其文本接口不能判断 PDF 全页、图像、版式或文件是否真的可用，也不是现成的多案例 runner。当前合同还绑定 Reviewed Handoff 输出布局和预算，不宜直接当无限批量判定服务。 |
| `/users/a/e/aereinh/AI_Instruction_Configuration`：[回归设计规则](/users/a/e/aereinh/AI_Instruction_Configuration/chatgpt/global/personalization-revisions/REGRESSION_DESIGN_RULES.md)、[R1](/users/a/e/aereinh/AI_Instruction_Configuration/chatgpt/global/personalization-revisions/02-math-question-negation/regressions/r1.md)及同目录 R2–R5 | 主要以 Markdown 保存真实失败、冻结题面、逐轮目的、继续/停止条件和判据。R1 有冻结九轮输入；已有一次 Edge、GPT-5.6 High 九轮重测的 `summary.md`、`transcript.md`、`judgment.md`。摘要记录为 `VALID_NON_REPRODUCTION`，并明确未运行 R2–R5。 | 多轮案例内容、独立 transcript/judgment 归档方式、前置有效性与“不复现不等于机制已解决”的结论边界。 | 未找到 `.py/.js/.ts/.sh` 执行脚本；现有记录本身不足以证明已有可复用的浏览器自动化。需要将 Markdown 中已经批准的逐轮协议机械映射到运行清单，不能让执行器重新设计题目。 |
| 同一指令仓库：[Project Atlas 回归](/users/a/e/aereinh/AI_Instruction_Configuration/chatgpt/projects/project-atlas/revisions/regressions/project-setting-v2.md) | 有 Project 级回归入口和判据，当前明确写着“尚未取得测试资格”“跑前检查尚未完成”。 | Project、当前设置和来源定位，以及测试资格检查。 | 不能因为有文件就加入可执行批次；需要先完成该案已有的准备要求。测试 Project setting 也必须进入对应 Project，普通聊天不能替代。 |
| `/users/a/e/aereinh/Asteria-Workspace/plugin-regressions`：[LOCAL_MAP.md](/users/a/e/aereinh/Asteria-Workspace/plugin-regressions/LOCAL_MAP.md)、[HOW_TO_TEST_LOCAL.md](/users/a/e/aereinh/Asteria-Workspace/plugin-regressions/HOW_TO_TEST_LOCAL.md) | 公共案例对应的本机私有素材映射与含实际路径的测试表。映射仍记录两项学生材料“本地文件：未观察”，两项科研材料“失败原稿对应关系：未观察”。 | 私有素材定位，公开 case 与本机材料的分离。 | 没有执行脚本或网页结果采集层；这些“未观察”记录须先补齐，不能当作素材就绪。该目录所在位置未识别为 Git 仓库，无法提供其自身的 Git 历史。 |

上述结论以当前文件为准。定向核对的本地 Git 快照为：本仓库 `30bdd398`、Bridge Kit `69fe058`、指令仓库 `ee26d95`；相关历史包括回归测试表 `d91a783f`（2026-11-19）、回归候选及缺口 `9115cecf`（2026-11-21）、Bridge Text Review 预算收紧 `cb77b1c`（2026-09-16）、指令修订目录整合 `34766af`（2026-11-19）。未整库通读，也未把历史通过当成本次运行证据。

这里有一个必须保留的差异：插件说明默认每案全新聊天；指令回归规则要求，对依赖模型自身历史状态的失败优先从原 conversation 的正确位置创建新分支，明确不接受把历史复制到 fresh thread 作为等价替代。因此统一 runner 需要支持“全新对话”和“指定历史位置的新分支”；无法完成指定分支时，该案应记未执行，不能静默改成全新聊天。[现行规则](/users/a/e/aereinh/AI_Instruction_Configuration/chatgpt/global/personalization-revisions/REGRESSION_DESIGN_RULES.md)

## 2. 路线比较

### 条款与账号验证：所有自动路线共同面对的限制

个人版适用的 Terms of Use 于 2026-01-01 生效，“What you cannot do” 原文包括：

> Automatically or programmatically extract data or Output (defined below).

自动保存整段回答正属于需要重点核实的输出提取行为。条款没有在此列出“本人账号”“低频”“回归测试”或“通过扩展操作”例外；拥有输出的权利也不自动赋予任意提取方式的权限。这里的结论是：**按已查到的个人条款，所需的完整自动采集与禁令直接冲突，不能作为已确认合规方案推荐上线。** [个人条款][TOU]

若账号属于 ChatGPT Business、Enterprise 等商业服务，应核对实际订单与 Services Agreement。其 §3.3(f) 原文为：

> extract data from the Services other than as permitted through the Services

商业合同的表述不同，但也不能由此推断任意网页采集已获准。两份条款还限制绕过限额或保护措施；验证码、异常活动和限额出现时应停止自动操作、保留现场并由用户处理，不能把规避验证当作 runner 能力。[商业协议][BIZ]

OpenAI 的排错文档明确说明，类似自动化或异常行为的流量可能触发 “Unusual Activity Detected”。未查到针对以下路线的触发概率或保证安全的发送频率；已登录、可见窗口与串行执行都不等于免检。[官方排错][ERR]

### 能力与维护成本

“可做”指基础工具具备相应能力，**不代表已经适配当前 ChatGPT 页面或在用户 Edge 上验过**。模型选择、插件选择、回答完成检测都还需要 ChatGPT 页面适配。表内维护成本是定性估计，不是工时承诺。

| 路线 | 如何接已登录 Edge | 多轮与回答完成判断 | 模型与插件 | 上传附件、保存文件 | 网页改版与稳定性 | 机器人或验证风险 | 条款判断 | 维护成本与适用性 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Playwright 直接 CDP | 用户先以 `--remote-debugging-port` 启动 Edge，再由本机脚本接入。普通已运行实例不能仅靠脚本自动补上该启动参数；微软文档要求先关闭实例再启动。[Edge][EDGE] | 脚本保留同案 page，逐轮发送；完成检测需另写页面条件，工具自带等待不等于模型已答完。[连接][CDP] | 可操作可见控件，但只能选择账号实际提供的模型、插件与工具；没有现成 ChatGPT 专用接口。[页面定位][LOC]、[插件][PLUG] | 有 `setInputFiles`、file chooser、下载事件与 `saveAs`；ChatGPT 是否已处理上传和是否交付所有文件还需检查。[上传][UPLOAD]、[下载][DOWNLOAD] | DOM 仍会变；CDP 官方注明连接保真度显著低于 Playwright 自有连接。适配成本中等。[CDP][CDP] | 未知，登录复用不排除验证。[排错][ERR] | 完整自动提取触及同一限制。[条款][TOU] | 中：连接层成熟；需维护 ChatGPT 适配、逐轮等待、归档和恢复。适合可接受重新启动或专用登录 profile 的场景。[Edge][EDGE]、[CDP][CDP] |
| **现成 Playwright 扩展 + 本机驱动，技术首选** | 官方支持 Chrome/Edge/Chromium，复用现有 profile 与登录；通过用户选择标签页或标签组授权连接，无须先启用调试端口。[扩展][EXT] | 支持持续控制已选标签页；MCP 提供读取、输入、点击、页面求值等原语，逐轮协议和完成判断仍由固定驱动负责。[工具][MCP] | 通过当前页面选择，并回读可见选择结果；安装或连接插件若需账户授权仍须用户完成。[工具][MCP]、[插件][PLUG] | MCP 有文件上传和页面求值保存能力；仍需补上生成文件发现、下载落盘与完整性核对，不能把一次 snapshot 当完整交付。[工具][MCP]、[下载][DOWNLOAD] | 连接层由上游维护；页面适配仍会失效，其他扩展插入受限 frame 也可能使调试连接断开。[扩展][EXT] | 未知；不会因采用微软扩展而获得 ChatGPT 自动化豁免。[排错][ERR] | 与 CDP 相同，先解决自动提取许可。[条款][TOU] | 中：比自建扩展少一套连接与权限维护；仍需本项目案例驱动。推荐理由是已有登录 Edge 的接入便利性。[扩展][EXT] |
| 自建 Edge/Chrome 扩展 | content script 在当前登录页面内运行；Edge 兼容 Chromium 扩展，部分 API 仍须兼容性检查。[Edge 扩展][EDGEEXT] | 可用 DOM 观察器追踪变化，但多轮队列、断线续接与完成判断全部自建；这是工程推断。[扩展机制][CONTENT] | 能操作页面，仍依赖 UI；没有额外模型或插件权限。[扩展机制][CONTENT]、[插件][PLUG] | 可使用浏览器下载能力；要与本机任意路径和脚本可靠交换文件，需文件选择或 native messaging 等桥接，不能假定 content script 可直接读磁盘。[本机通信][NATIVE] | 同时维护网页选择器、扩展权限、浏览器兼容与本机桥接，成本高于复用现成扩展。[兼容性][EDGEEXT]、[本机通信][NATIVE] | 未知，扩展不是规避检测的机制。[排错][ERR] | 同一提取限制。[条款][TOU] | 高；现成扩展不能满足的具体缺口出现前，不建议先造。[扩展][EXT]、[本机通信][NATIVE] |
| `fozooni/ChatGPT-Automation` | README 要求导出 cookies 到文件，然后运行单独 Chromium；不是直接接管用户 Edge。[项目][FOZ] | 有问题数组与定时调度；源码含固定等待，未见可靠的回答完成条件，也未形成每案多轮协议。[源码][FOZSRC] | README 只列 ChatGPT-3.5/4，未找到现行插件选择支持。[项目][FOZ] | 已查 README 和主实现未提供附件、生成文件归档闭环。[项目][FOZ]、[源码][FOZSRC] | 2023 年硬编码 DOM 路径与旧入口；当前可用性未验证，不能直接采用。[源码][FOZSRC] | 项目还讨论以发送间隔规避限额；这不能作为合规或稳定性依据。[项目][FOZ] | 同一提取限制，限额规避另有条款风险。[条款][TOU] | 高：需要大幅适配；仅可作为历史实现参考。[源码][FOZSRC] |
| `KudoAI/chatgpt.js` | DOM 模式可嵌入扩展或用户脚本，借用当前网页登录；它本身不负责接入 Edge。[用法][JS] | 有 `startNewChat`、`send`、`isIdle`、DOM 回答读取和导出；多轮批次、判据和恢复仍须编排。[用法][JS] | 已查接口不能证明支持用户当前模型菜单和插件启用；部分通用方法还支持 API provider，不能把 API 路径误当网页回归。[用法][JS] | 有聊天导出；未找到覆盖附件上传、全部生成文件与 hash 的成套流程。[用法][JS] | 已归档，发布记录显示曾因选择器变化修复空闲检测、导出和 DOM 读取；当前能否用未验证。[仓库][JSREPO]、[发布记录][JSREL] | 未知，没有可验证的免检承诺。[排错][ERR] | 同一提取限制。[条款][TOU] | 中高：可参考接口设计，归档后不宜直接承担核心适配。[仓库][JSREPO] |
| `browser-use/browser-use` 等通用浏览器代理 | 本地模式可接任意 CDP，因而可接调试模式 Edge；当前文档的“已有 Chrome”入口不能直接当作“已有 Edge”保证。[浏览器][BU] | 代理可连续点击、阅读、发送；但自动判断任务完成不等于 ChatGPT 完成生成，更不等于冻结多轮协议已全部执行，需外部约束。[代理][BUAGENT] | 可以尝试 UI 操作，成功率未实测；不能获得账号未开放的模型或插件。[代理][BUAGENT]、[插件][PLUG] | 有上传和下载工作目录支持，仍需核对每案附件与产物。[文件][BUFILES] | 能根据页面重新观察和规划，可能减少硬编码，但引入代理误操作与执行差异；此为工程判断。[代理][BUAGENT] | 未知；项目的 cloud/stealth 宣传不能证明可用于 ChatGPT，也不能替代许可。[仓库][BUREPO]、[条款][TOU] | 同一提取限制，换代理不改变。[条款][TOU] | 中高：增加驱动模型、费用和非确定性。当前 `Browser()` 默认是云浏览器，必须显式选本地/CDP 才符合本机登录目标。[浏览器][BU] |
| `acheong08/ChatGPT` 等逆向网页接口项目 | 不接管 Edge，以逆向接口和认证材料交互。[仓库][REV] | 历史上提供对话接口，但不能证明当前网页登录环境、插件与指令配置被同等执行。[仓库][REV] | 不是当前网页 UI 的选模、启用插件路径；不满足本任务验收对象。[仓库][REV] | 未证明当前附件与网页生成文件能力。[仓库][REV] | 已归档且多年无代码推送；不能认定当前可用。[仓库][REV] | 未知，另增加认证材料和非公开协议维护问题。[仓库][REV] | 同一提取限制；不能用逆向接口绕开网页约束。[条款][TOU] | 不采用：不符合必须在真实网页上测试的要求。[仓库][REV] |
| 人工跑网页，自动整理本地记录并独立判定 | 用户照常用已登录 Edge，不接管浏览器。[现有回归说明](../plugin-reset-2026-11/regressions/HOW_TO_TEST.md) | 按冻结逐轮协议手动发送和确认完成。[现有 R1](/users/a/e/aereinh/AI_Instruction_Configuration/chatgpt/global/personalization-revisions/02-math-question-negation/regressions/r1.md) | 人工选择并保存环境证据。[插件][PLUG]、[模型][MODELS] | 人工上传、复制回答、下载文件；后续本地整理可自动化。[上传说明][FILES] | 页面变化由人处理，批次越多人工成本越高。[现有回归说明](../plugin-reset-2026-11/regressions/HOW_TO_TEST.md) | 仍可能遇普通账号验证，未引入网页机器人。[排错][ERR] | 避开自动提取这一特定争议，仍受其他条款约束。[条款][TOU] | 浏览器维护低、人工成本高；属于自动采集许可未解决时的降级方案，**不满足原始全自动目标**。 |

### 开源项目状态快照

星数与时间来自本次直接读取 GitHub REST repository metadata。`updated_at` 可受仓库元数据活动影响，`pushed_at` 也不等于已验证的代码修复日期；因此分别列出。星数不作为“还能用”的证据。

| 仓库 | 星数 | `updated_at`（UTC） | `pushed_at`（UTC） | 是否归档 | 目前能否用：本次能支持的结论 |
| --- | ---: | --- | --- | --- | --- |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 39,982 | 2026-11-22 03:30:48 | 2026-11-18 18:50:37 | 否 | 有维护中的 Edge 扩展连接与通用浏览器工具；ChatGPT 专用流程未实测。[metadata](https://api.github.com/repos/microsoft/playwright-mcp) |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 121,694 | 2026-11-22 04:17:39 | 2026-11-22 03:44:56 | 否 | 有当前本地/CDP 文档；用户 Edge 和 ChatGPT 回归闭环未实测。[metadata](https://api.github.com/repos/browser-use/browser-use) |
| [KudoAI/chatgpt.js](https://github.com/KudoAI/chatgpt.js) | 2,036 | 2026-11-19 22:51:50 | 2026-08-10 08:03:14 | 是 | 有 DOM 发送、等待、读取接口；已归档，当前 ChatGPT 页面兼容性未验证。[metadata](https://api.github.com/repos/KudoAI/chatgpt.js) |
| [fozooni/ChatGPT-Automation](https://github.com/fozooni/ChatGPT-Automation) | 5 | 2026-04-23 13:16:38 | 2023-10-22 23:35:10 | 否 | 源码使用旧选择器和固定等待；没有足够证据认定现在能直接用。[metadata](https://api.github.com/repos/fozooni/ChatGPT-Automation) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 28,008 | 2026-11-22 00:26:00 | 2023-08-02 06:02:10 | 是 | 逆向接口路线，不满足本任务；未执行兼容性测试。[metadata](https://api.github.com/repos/acheong08/ChatGPT) |
| [mbroton/chatgpt-api](https://github.com/mbroton/chatgpt-api) | 121 | 2026-09-08 15:32:06 | 2024-11-07 15:33:19 | 是 | HTTP client/CLI；不作为接管真实 Edge 的现成方案，当前服务可用性未验证。[metadata](https://api.github.com/repos/mbroton/chatgpt-api) |

另有一个 CDP 接入细节：Chrome 从 136 起不再允许对默认数据目录直接使用 remote debugging switches，要求非默认 `user-data-dir`。这是 **Chrome 官方规则**，本次未找到足以证明 Edge 当前各版本完全同样执行的资料，不能直接套用；微软 Edge 文档仍给出启动调试端口的方法。实施前应在选定 Edge 版本验证，不能承诺给普通已登录实例追加参数就一定能连上。[Chrome 变更][CHROME]、[Edge 协议][EDGE]

当前 OpenAI 文档中的插件可以包含 skills 与 connected apps；可用性受计划、workspace、权限和地区影响。应以用户账号现行界面为准，明确测试的是 Chat、Work 或其他指定入口，并记录实际插件与设置身份。本次未查到面向外部网页测试器、稳定承诺的 ChatGPT DOM 选择器或回答完成事件。[插件说明][PLUG]、[模型说明][MODELS]

## 3. 推荐路线的最小骨架

以下是后续实现的结构草案，前提是自动采集用途获准；本文没有创建 skill、驱动程序或安装脚本。

### 在哪台机器运行，怎样和集群交换文件

**浏览器驱动应运行在用户选定的 Mac 或 Windows 笔记本上，与已登录 Edge 同机。** skill 若由集群 Codex 调用，只能准备案例和读取回传结果；要驱动浏览器，仍须本机进程执行。远程工作目录不会赋予集群对笔记本 `localhost` 或桌面的访问权。Playwright 扩展支持 Edge；本机接入方式仍须在最终选定的 OS、Edge 与扩展版本上验证。[扩展连接][EXT]

建议以文件批次交接：集群生成冻结输入包，本机通过既有 SSH/SFTP/SCP 连接拉取，运行后再主动上传结果包，集群按批次 ID 和 hash 核对。Windows 的 OpenSSH 包含 `ssh`、`scp`、`sftp`；OpenSSH 也提供跨平台的相应协议与工具。具体连接主机和认证方式沿用用户已有配置，本文没有测试笔记本至集群的连通性。[Windows OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview)、[OpenSSH 手册](https://www.openssh.org/manual.html)

该交接结构让两边都只需主动连接已有 SSH 入口，不需要笔记本开放入站端口，也不需要把 CDP 暴露给集群。传输包包含相对路径的素材、清单、大小和 hash；集群 `/users/...` 路径须映射成本机文件，不能直接当成本机上传路径。判据包与发送包分离，避免把答案泄入被测对话。Edge cookies、profile、扩展连接 token 留在本机；回传聊天和附件本身也须按私有材料处理。

若未来坚持让集群实时发控制命令，可另设计经过认证的本机连接，但这不是最小骨架必需部分。现阶段没有证据支持为它新增云中转、常驻服务或修改生产 tunnel。

### 多轮案例的文件格式草案

在现有 `case.yaml` 旁增加运行清单或由其生成清单，保留原文判据及其身份，不改现有文件。下面仅示意字段与层级，不预填模型、题目、阈值或判定结论；单轮也是 `turns` 中的一项。

```yaml
schema_version:
batch_id:
source_revision:
cases:
  - case_id:
    source_case_path:
    source_case_sha256:
    eligibility:
    environment:
      product_surface:
      workspace:
      project:
      model_label:
      reasoning_setting:
      plugins:
      plugin_version_or_hash:
      instruction_snapshot_sha256:
      memory_policy:
    conversation:
      start_mode:
      source_conversation_url:
      branch_after_message:
    inputs:
      - logical_id:
        relative_path:
        sha256:
        privacy_scope:
    turns:
      - turn_id:
        prompt_file:
        prompt_sha256:
        attachment_ids:
        prerequisites:
        continue_condition:
        stop_condition:
        completion_rule:
        timeout_policy:
        expected_artifacts:
    capture:
      transcript_formats:
      screenshots:
      required_files:
    judgment:
      rubric_path:
      rubric_sha256:
      judge_identity:
      judge_input_scope:
    execution_limits:
      max_attempts:
      approval_scope:
```

`start_mode` 用来区分 fresh thread 与原历史分支。`prerequisites`、继续/停止条件必须来自已冻结案例；执行器不能自行猜测“这轮回答差不多了，后面省略”。指令回归中若某前置轮次需要语义判断才能继续，应交独立判定者按冻结规则判断；没有该规则就先补足案例设计，不能现场改 prompt。[指令回归规则](/users/a/e/aereinh/AI_Instruction_Configuration/chatgpt/global/personalization-revisions/REGRESSION_DESIGN_RULES.md)

环境记录必须包含全局指令、Project 设置和 memory 的适用方式。新开聊天不会自动隔离所有账号记忆或设置；不能为了“更干净”切换到不加载被测指令或插件的入口。修改账号级设置还会影响同账号其他会话，批次应按设置版本分组并明确恢复边界。[Memory 说明](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)、[插件说明][PLUG]

### 一次批量运行的步骤

1. **冻结输入。** 汇集已具测试资格的案例，保留逐轮原文、顺序、来源版本、附件与判据 hash；未确认素材、未完成跑前检查的案例列为未就绪。把必须交 Codex 制作或验证的环节列入案例交付要求。
2. **本机接入。** 拉取输入包、核对文件，启动本机驱动并通过 Playwright 扩展连接目标 Edge profile。确认账号、workspace、Chat/Work 入口、Project、模型与推理设置、插件和指令版本；保存界面证据。无法选择指定模型或插件时停在该案，不自动换模型或重写调用方式。
3. **建立案例上下文。** 按冻结协议新开聊天或创建指定历史分支；默认串行，避免账号级设置相互影响。记录 conversation URL、起点与实际环境，不能只凭点名插件就宣布插件已加载。
4. **逐轮发送并等完整回答。** 先确认附件上传处理完，再原文发送。建议完成条件组合为：对应 user message 已出现、新 assistant 回答已出现、界面不再显示生成/工具处理中、当前输出在连续观察中不再变化，且所需文件任务已结束。**这些是待验证的启发式规则，不是官方完成信号。** 单靠固定 sleep、页面 `networkidle`、停止按钮消失或文字短暂不变都不足以判完整；网页定位等待只解决控件交互问题。[Playwright 等待说明](https://playwright.dev/docs/actionability)
5. **每轮立即归档。** 保存完整可见用户/助手记录、格式化正文或 HTML、公式、表格、引用链接、工具状态及截图。长对话须检查此前轮次仍已保存；截图和 accessibility snapshot 都不能单独替代全文。触发文件下载后等待实际落盘，保存原文件名、大小、hash、来源轮次；失败或缺件明确记录。ChatGPT 生成文件可能很快失效，不能只保存下载链接。[下载机制][DOWNLOAD]、[ChatGPT 下载问题][ERR]
6. **异常保留现场。** 登录失效、验证、限额、页面选择器失效、发送结果不明、模型改变或超时，分别记执行异常。发送结果不明时先检查已存在消息，不盲目重发；重试保留独立 attempt，不能只留下最好的一次。生成中断不能作为完整回答交付。
7. **独立判定并回传。** 将全部轮次、必要来源、原文判据、附件/成品和执行记录交给独立模型；先判证据与前置条件是否有效，再逐项判通过或失败。汇总后上传结果包，集群核对批次、hash、轮数、文件清单和判定输入是否一致。完成浏览器运行不自动代表混合案例的制作、渲染与回读环节也已完成。

步骤 4–6 仍需在后续实现时用真实页面验证；本次没有实测这些规则的误判率，也没有给出未经测量的等待时长或“稳定通过率”。

### 结果表的列

| 列组 | 字段 |
| --- | --- |
| 身份 | `batch_id`、`case_id`、`attempt_id`、案例版本/hash、素材与判据 hash |
| 实际环境 | 本机 OS、Edge/驱动/扩展版本、Chat/Work 入口、workspace/Project、实际可见模型及推理设置、插件/技能版本或 hash、指令快照 hash、memory 设置 |
| 执行 | conversation URL、fresh/branch 起点、计划轮数、完成轮数、每轮完成状态、起止时间与耗时、执行状态、异常原因 |
| 交付证据 | transcript 路径/hash、截图、输入附件清单、生成文件清单/hash、缺件、所需机械检查与渲染证据 |
| 判定 | 判定模型与独立会话/请求身份、判定输入 hash、逐条标准结论、支持结论的轮次/引文/页面、总体通过或失败、证据不足原因、人工复核状态 |

执行状态与内容判定必须分列：未运行、输入无效、超时、缺产物或无法判定，都不能写成内容 PASS。完整运行且证据充分后，才汇总通过/失败；指令案例的 `VALID_NON_REPRODUCTION` 等原有含义仍应保留，不能改写成长期问题已解决。

### 判定交给谁

推荐由**独立模型在独立上下文**中判定，被测对话不接触评分表；执行器只负责机械收集与核对。判定者读完整逐轮记录、权威输入和判据，并引用具体证据；回答中的自评或“已调用插件”声明不能自行证明通过。页面上的模型名称只能证明可见选择，不能证明服务端内部路由；技能自述也不能单独证明实际消费。

纯文本案例可优先评估复用 Bridge Text Review：测试仍在 ChatGPT 网页运行，API 只用于另一个模型判定，二者职责不同。但这条现成路径需要 GitHub Actions、外部传输授权、凭据配置和付费合同；当前本地文档绑定 `gpt-5.6-terra`、最多两次付费调用和总预留成本上限，不能直接承诺覆盖任意批次数量，也不能擅自改成另一个模型或提高预算。这些是本地现有合同，不是本次查证的当前模型价格。[现有 Text Review 合同](/users/a/e/aereinh/GPT_Codex_AI_Bridge_Kit/templates/text_review/README.md)

PDF、图像、版式及生成文件类案例需要具备相应输入能力的独立判定者读取原文件或全部目标页面，并保留必要机械检查。Text Review 的 UTF-8 文本接口不能以转述代替这类检查。如果用户要求判定也必须走网页，可开另一独立判定会话，但又会面对同样的网页采集许可和稳定性问题；它不属于已存在的自动判定闭环。

## 4. 未解决的问题：需要用户决定

1. **账号合同与自动采集许可。** 实际使用个人版还是 Business/Enterprise 等 workspace？是否先向 OpenAI 确认并取得该回归用途的自动提取许可？若暂时无法取得，是否接受“人工跑网页，后续自动整理和判定”的明确降级？
2. **首个本机运行环境。** 首版以 Mac 还是 Windows 笔记本为验收环境？使用哪个已登录 Edge profile，以及同账号的 Chat/Work 入口、workspace 和 Project？优先建议复用现成 Playwright 扩展，CDP 仅作备用。
3. **独立判定模型与数据路径。** 是否允许把哪些范围的聊天、私有素材和成品送到 OpenAI API/GitHub Actions 或其他指定判定端？选哪个判定模型、付费上限多少；是否要求判定也只在网页进行？
4. **被测设置的修改范围。** 批次只测试已安装插件和当前指令，还是也允许切换插件/指令版本？如需切换，须明确目标账号/Project、恢复范围，以及运行期间如何避免影响同账号其他会话。

[EXT]: https://github.com/microsoft/playwright/blob/main/packages/extension/README.md
[MCP]: https://github.com/microsoft/playwright-mcp#tools
[EDGE]: https://learn.microsoft.com/en-us/microsoft-edge/devtools/protocol/
[CDP]: https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp
[LOC]: https://playwright.dev/docs/locators
[UPLOAD]: https://playwright.dev/docs/input#upload-files
[DOWNLOAD]: https://playwright.dev/docs/downloads
[EDGEEXT]: https://learn.microsoft.com/en-us/microsoft-edge/extensions/
[CONTENT]: https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts
[NATIVE]: https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging
[CHROME]: https://developer.chrome.com/blog/remote-debugging-port
[TOU]: https://openai.com/policies/terms-of-use/
[BIZ]: https://openai.com/policies/services-agreement/
[ERR]: https://help.openai.com/en/articles/7996703-troubleshooting-chatgpt-error-messages
[PLUG]: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
[MODELS]: https://learn.chatgpt.com/docs/models
[FILES]: https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt
[FOZ]: https://github.com/fozooni/ChatGPT-Automation
[FOZSRC]: https://github.com/fozooni/ChatGPT-Automation/blob/main/src/OpenAI.ts
[JS]: https://github.com/KudoAI/chatgpt.js/blob/main/docs/USERGUIDE.md
[JSREPO]: https://github.com/KudoAI/chatgpt.js
[JSREL]: https://github.com/KudoAI/chatgpt.js/releases
[BU]: https://docs.browser-use.com/open-source/browsers
[BUAGENT]: https://docs.browser-use.com/open-source/agent
[BUFILES]: https://docs.browser-use.com/open-source/files
[BUREPO]: https://github.com/browser-use/browser-use
[REV]: https://github.com/acheong08/ChatGPT
