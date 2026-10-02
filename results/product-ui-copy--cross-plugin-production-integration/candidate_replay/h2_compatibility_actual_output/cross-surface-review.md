# 跨平台界面与文案评审

前四类涉及用户界面，应先确定信息层级与产品事实，再定稿文案；第五类明确保持 UI 不变，不进入界面设计或文案流程。本次仅检查提供的三个文件，未修改源文件、未访问外部服务，也未运行浏览器或原生应用。以下布局风险来自源码分析，不代表已观察到渲染缺陷。

## 1. 通用设置与删除确认

**范围与结构：** 属于界面设计和文案工作。设置页应依次说明“先检查—预览并移除项目—确认后上传”，主操作是检查，次操作是继续本机使用。标题与正文重复强调确认门槛有助于信任，但预览用途和移除权利也应靠近操作区。当前窄屏单列布局把整个隐私侧栏放在按钮之后；建议把必要说明放到操作前，详细保留规则再通过链接展开。删除确认已把公开可见性变化、审计保留和删除按钮放在一起，这些后果不能折叠隐藏。

**保护事实：** 上传须经确认；检查结果只用于本次预览；确认前可以移除任何项目；删除公开回复后其他人无法再看到，但系统记录仍用于安全审计。不能改成“彻底清除”“不留痕迹”，也不能自行承诺恢复能力。引导区另有工作区可更改、勾选项目的共享范围、可暂停同步等含义，不能因缩短文案改变。

**交接与升级：** 已知 `SURFACE` 为设置页/移动端确认，`UI_ROLE` 为主次操作、披露、破坏性确认和保存状态，`LOCALE=zh-Hans`。最终交接还需确定 `PRODUCT_STATE`（检查前、预览中或已同步）、`USER_JOB`、`USER_CONSEQUENCE_OR_NEXT_ACTION`、完整 `NEIGHBORING_VISIBLE_COPY`、上述 `PROTECTED_MEANING`、`DISCLOSURE_LEVEL` 与实际 `LENGTH_OR_VIEWPORT_CONSTRAINT`。保留期限、记录范围、恢复能力未提供；涉及这些信息的新增措辞须交产品/隐私负责人确认。HTML 的 `#details` 没有对应目标，详细规则当前不可达。

**可安全修改：** “先保持本机使用” → “暂时仅在本机使用”。

**KEEP：** “同步只在你确认后开始”“检查可同步项目”“是否删除这条公开回复？”及其完整后果说明、“删除公开回复”“取消”；保存状态保留“已保存”“你的更改已同步到这台设备。”。

**验收边界：** HTML 引用 `./product-ui-copy-fixture.css`，实际附件名为 `03-product-ui-copy-fixture.css`，按现有文件名直接打开不会加载该样式。CSS 在 720px 以下堆叠、860px 以下调整步骤区；应检查 320px、720px 两侧和桌面宽度的换行、滚动、按钮与披露关系。手机框只是 HTML 模拟，按钮没有业务处理，确认区也没有原生对话框行为；不能证明上传门槛、删除、焦点管理或 Compose 运行效果。英文说明性标签和旁侧评测文字属于夹具说明，不应直接进入生产界面。

## 2. Lucerna 桌面紧凑面板

**范围与结构：** 属于用户界面工作。菜单栏/托盘是入口，紧凑面板是主界面。保留 Resources、Health、Network 分组，资源名与数值对齐；健康检查范围和数据新鲜度靠近对应状态，详细诊断再展开。长资源名、金额、百分比和速率单位同时出现，需检查窄面板和系统缩放下的截断。macOS 网络区不能未经确认复制成 Windows 已有能力。

**保护事实：** 保留 Lucerna、Codex、OpenAI API、GitHub Actions、UNC Bridge、Longleaf 等身份，以及余额/余量、单位和 Today 的时间范围。WidgetKit 快照不能写成实时刷新；TCP 或局部可用性不能写成全面业务健康。

**交接与升级：** `SURFACE` 必须区分 macOS 面板、Windows 面板和 WidgetKit；`UI_ROLE` 是指标/状态，`USER_JOB` 是快速查看资源和连接情况。补齐 `PRODUCT_STATE`、各状态的检查范围与时间、是否可点击及其 `USER_CONSEQUENCE_OR_NEXT_ACTION`、`NEIGHBORING_VISIBLE_COPY`、`LOCALE`、`PROTECTED_MEANING`、`DISCLOSURE_LEVEL` 和面板宽高约束。由产品及监控实现负责人解释 “Healthy” 的实际依据，再确定其文案。

**文案决策：** `KEEP`：“Resources”“Network · macOS”。“Healthy” 暂不定稿：只有确认仅验证 TCP 连通后，才能考虑 “TCP reachable”；当前材料不足以把这条条件建议当成最终替换。无需为凑改动改写清楚的指标。

**验收边界：** 只有平台/产品文档摘录，没有实际面板、刷新行为或截图。浏览器夹具不能证明 Tauri WebView、菜单栏/托盘交互和 WidgetKit 行为；需分别在目标系统验证面板打开、焦点、缩放、数值更新及过期状态。

## 3. Mica 浏览器扩展弹窗

**范围与结构：** 属于用户界面工作。固定小弹窗应先显示当前状态与可执行的下一步；普通诊断和 composer 检查应分组，详细采样计数与分类结果可逐步展开。复制反馈靠近对应复制按钮。“Reset” 需与开始/停止操作区分，避免在拥挤布局中被误触；不能仅靠改名掩盖未知重置范围。

**保护事实：** 产品名为 Mica for ChatGPT；支持范围来自两个列出的 host permissions。保留 Active、Native virtualization、Native only、Degraded、Disabled 的状态差异，不擅自合并。不得暗示诊断上传聊天内容；“本地处理”“隐私安全”须有实际采集、存储与网络行为证据。未知授权、删除、支付和工具权限提示不得自动关闭。

**交接与升级：** `SURFACE` 为扩展 popup，`UI_ROLE` 为状态、诊断操作及反馈，`LOCALE` 暂沿用英文。补齐 `PRODUCT_STATE` 与状态映射、`USER_JOB`、`USER_CONSEQUENCE_OR_NEXT_ACTION`（特别是 Reset、复制、停止后的结果）、分组后的 `NEIGHBORING_VISIBLE_COPY`、`PROTECTED_MEANING`、`DISCLOSURE_LEVEL`、实际弹窗宽高。隐私承诺和 Reset 影响范围交产品/实现负责人确认；权限字符串本身不能证明无上传。

**可安全修改：** “No diagnostics report available.” → “No diagnostics report yet.”；“Clipboard copy failed.” → “Couldn’t copy to clipboard.”。不补写未经验证的失败原因或恢复承诺。

**KEEP：** “Open a ChatGPT conversation.”、“Start diagnostics”、“Stop diagnostics”、“Copy report”、“Report copied to clipboard.”。

**验收边界：** 未提供完整弹窗 DOM/CSS 或运行证据。需在真实扩展中覆盖不支持页面、无报告、采集中、停止、复制失败等状态，检查键盘焦点、滚动和长文本；通用浏览器页面无法证明扩展权限、剪贴板结果或诊断隐私行为。

## 4. SeminarArc Compose UI 正向场景

**范围与结构：** 属于界面设计/文案工作；Android/Compose 实现仍由项目的平台负责人决定。列表筛选、现场采集、研究重建是不同任务层级。现场采集突出 Mark Moment、Capture Slide，录音状态及 Pause/Resume 相邻；End Seminar 与高频动作拉开。重建页按选图、运行本地 OCR、编辑/搜索文本组织，失败后提供重试或取消。详细任务信息可展开，录音状态和删除后果必须直接可见。

**保护事实：** PENDING、RUNNING、SUCCEEDED、FAILED、CANCELLED 是不同任务状态，不能把取消说成完成。保留本地 OCR 的处理范围；云端、AI 摘要、转写、Notion、公式 OCR、参考文献检索尚属未来能力，不能呈现为已启用。删除研讨会必须点名具体研讨会并列出将删除的资产类型。

**交接与升级：** 明确 `SURFACE` 是哪个 Compose 页面/对话框，`UI_ROLE`、`PRODUCT_STATE`、`USER_JOB`、`USER_CONSEQUENCE_OR_NEXT_ACTION`、相邻按钮与录音状态等 `NEIGHBORING_VISIBLE_COPY`、`LOCALE`、`PROTECTED_MEANING`、`DISCLOSURE_LEVEL` 和屏幕/字体缩放约束。删除前还需产品负责人提供真实资产种类、删除范围及可恢复性；End Seminar 是否停止录音和保存哪些内容也须确认，不能靠文案猜测。

**可安全修改：** “Select photos or key slides” → “Choose photos or key slides”。这只是已有动作的英文措辞候选，不改变功能可用性。

**KEEP：** “Create seminar”“Capture Slide”“Run local OCR”“Search OCR text”；不改代码枚举。删除文案因缺少资产清单不定稿，不用占位文案冒充可上线确认。

**验收边界：** HTML 手机框不能证明 Compose 的排版、TalkBack、返回行为或录音状态。需真实 Android 屏幕覆盖列表、采集、重建及删除对话框，检查长研讨会名称、大字体、屏幕旋转、触控区域和任务状态变化。

## 5. SeminarArc Room / WorkManager / 纯数据场景

**范围与结构：** 不属于用户界面或文案工作。请求是迁移 Room 与 WorkManager 的处理重试语义，并明确 UI 不变；没有新增可见界面、布局或文案问题。

**保护事实与交接：** 保持 UI、可见状态含义和用户动作不变；由数据/后台任务负责人确定迁移、重试计数、调度、取消、幂等与持久化契约。这是工程交接，不要求填写 Product UI Copy 表单。若迁移实际改变了可见状态或动作后果，应先交产品/平台负责人确认范围，再决定是否另行进入界面评审。

**KEEP：** 全部现有界面文案；无安全且必要的字符串改写。没有依据提出新的法律或信任措辞。

**证据边界：** 路径清单不能证明迁移正确；需 Room 迁移、WorkManager 重试/取消及进程重启后的恢复证据。UI 不变也需实现差异和相关回归支持，本次未执行这些验证。

## routing-boundary

是否进入界面工作取决于请求是否改变用户可见表面或含义，不取决于项目是否使用 Android/Compose。第四类直接涉及页面、操作、状态和删除确认；第五类明确保持 UI 不变，因此由 Room/WorkManager 数据与后台处理流程负责。强行引入界面重排或改文案会扩大任务范围。

本评审依据 `inputs/01-compatibility_sources.md` 的五类摘录，以及 `inputs/02-product-ui-copy-fixture.html`、`inputs/03-product-ui-copy-fixture.css`。源仓库 locator 仅作为材料来源记录，未读取对应仓库。文案候选已区分可直接保留、可安全修改和需事实确认三类；所有实际平台的渲染验收仍待补证。
